#!/usr/bin/env python3
"""check_wikilinks.py — broken-wikilink checker for the Social Sciences Wiki.

Usage:
    python scripts/check_wikilinks.py [--root PATH] [--json OUT.json]
                                      [--compare BASELINE.json] [--quiet]

Resolution rules:
  - [[slug]] resolves against every page's filename stem (case-insensitive)
    and against frontmatter `aliases:` entries
  - [[path/to/slug]] resolves against relative paths — this is how hub pages
    (which intentionally share their summary's slug) are linked unambiguously
  - [[unknown]] is always valid — the schemas *require* it for honest gaps
  - links inside fenced code blocks are ignored (templates quote schemas)
  - template files (*/templates/*) are skipped entirely

Extra diagnostics:
  - a broken target containing 4+ words is flagged as a likely free-text
    phrase wrapped in [[ ]] (a recurring ingest failure mode — descriptive
    phrases in causes/consequences-style fields must be plain text)
  - a link that resolves only case-insensitively is reported as a WARN
  - a bare-stem link whose stem is shared by a summary page and its hub page
    is reported as ambiguous (WARN) — link hubs by full path

Proving "0 new broken links" after an ingest (no stash-comparison needed):
    before: python scripts/check_wikilinks.py --json /tmp/links_baseline.json
    after:  python scripts/check_wikilinks.py --compare /tmp/links_baseline.json

Exit status: 1 if any broken links (or, with --compare, any NEW broken links).
Output is never capped.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import (  # noqa: E402
    Resolver, load_vault, resolve_root, iter_links_with_lines, normalize_target,
    parse_only, rel_matches_only,
)

ALWAYS_OK = {"unknown"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None)
    ap.add_argument("--json", dest="json_out", default=None,
                    help="write a snapshot of broken links to this file")
    ap.add_argument("--compare", default=None,
                    help="compare against a snapshot; fail only on NEW broken links")
    ap.add_argument("--quiet", action="store_true", help="summary only")
    ap.add_argument("--only", default=None,
                    help="report only broken links whose SOURCE page path "
                         "contains one of these substrings (comma/space "
                         "separated). Resolution still uses the full vault.")
    args = ap.parse_args()

    root = resolve_root(args.root)
    pages = load_vault(root)
    only = parse_only(args.only)
    resolver = Resolver(pages)

    broken: list[dict] = []
    warns: list[str] = []
    n_links = 0

    for page in pages:
        if page.is_template:
            continue
        for lineno, target in iter_links_with_lines(page.all_text()):
            t = normalize_target(target)
            if not t or t.lower() in ALWAYS_OK:
                continue
            n_links += 1
            hits = resolver.resolve(t)
            if not hits:
                entry = {"file": page.rel, "line": lineno, "target": t}
                if len(t.split()) >= 4:
                    entry["note"] = "likely a free-text phrase wrapped in [[ ]] — unbracket it"
                broken.append(entry)
                continue
            # exact-case check for stem links (aliases count as exact)
            if "/" not in t and not any(
                    pg.slug == t or t in pg.fm_list("aliases") for pg in hits):
                warns.append(f"{page.rel}:{lineno} :: [[{t}]] resolves only "
                             f"case-insensitively (actual: {hits[0].slug})")
            # ambiguity: a bare stem is fine if exactly one NON-hub page holds it
            # (convention: bare link = summary page; hub pages are linked by path)
            if "/" in t or len(hits) <= 1:
                continue
            non_hub = [pg for pg in hits if pg.folder != "hubs"]
            if len(non_hub) == 1:
                continue
            folders = sorted({pg.hub_folder for pg in hits})
            warns.append(f"{page.rel}:{lineno} :: [[{t}]] is ambiguous across "
                         f"{folders} — disambiguate (type suffix or full path)")

    if only:
        broken = [b for b in broken if rel_matches_only(b["file"], only)]
        warns = [w for w in warns if rel_matches_only(w, only)]

    if not args.quiet:
        for b in broken:
            note = f"  ({b['note']})" if "note" in b else ""
            print(f"BROKEN {b['file']}:{b['line']} :: [[{b['target']}]]{note}")
        for w in warns:
            print(f"WARN   {w}")

    print(f"\ncheck_wikilinks: {len(pages)} pages, {n_links} links — "
          f"{len(broken)} broken, {len(warns)} warning(s)")

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps({"broken": broken, "total": len(broken)}, indent=2),
            encoding="utf-8")
        print(f"snapshot written to {args.json_out}")

    if args.compare:
        base = json.loads(Path(args.compare).read_text(encoding="utf-8"))
        base_keys = {(b["file"], b["target"]) for b in base.get("broken", [])}
        new = [b for b in broken if (b["file"], b["target"]) not in base_keys]
        fixed = base_keys - {(b["file"], b["target"]) for b in broken}
        print(f"vs baseline: {len(new)} NEW broken link(s), {len(fixed)} fixed")
        for b in new:
            print(f"NEW    {b['file']}:{b['line']} :: [[{b['target']}]]")
        return 1 if new else 0

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
