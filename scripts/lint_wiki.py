#!/usr/bin/env python3
"""lint_wiki.py — wiki-specific heuristic linter for the Social Sciences Wiki.

Automates the mechanical subset of CLAUDE.md's Lint Workflow. Judgment items
(voice violations beyond crude patterns, caused_by-conflates-sequence,
near-synonym duplicate titles) still need a reading pass.

Usage:
    python scripts/lint_wiki.py [--root PATH] [--quiet] [--no-info]

Checks:
  ERROR  duplicate-slug        same filename stem in two folders (hub/summary
                               pairs are the sanctioned exception, reported INFO)
  ERROR  hub-reciprocity       hub page missing its *_page field, or pointing at
                               a page that doesn't exist in the summary folder
  WARN   hub-backlink          summary page doesn't link back to its hub page
  WARN   genealogy-symmetry    A trained_under B, but B's `trained` omits A
                               (and the reverse)
  WARN   supports-challenges   study declares supports:/challenges: [[theory]],
                               but the theory page never mentions the study
  WARN   date-stamp            archaeogenetic/paleoclimate keywords on a line
                               with no "(as of Author Year)" stamp
  WARN   orphan                page with no inbound links (links from index.md,
                               log.md, overview.md, and queries/ don't count)
  WARN   reversed-name         thinkers/a-b.md and thinkers/b-a.md both exist
  INFO   society-culture-twin  same stem in societies/ and cultures/
  INFO   ethnographic-present  present-tense "The X are/live/practice..." lines
                               on society pages
  INFO   voice-pattern         crude wiki-voice red flags ("proves that",
                               "it is a fact that", ...)

Exit status: 1 if any ERROR, else 0.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import (  # noqa: E402
    Page, Resolver, SUMMARY_FOR_HUB, load_vault, resolve_root, strip_fences,
    parse_only, rel_matches_only,
)

GENETIC_RE = re.compile(
    r"(aDNA|ancient DNA|archaeogenet\w*|paleogenom\w*|palaeogenom\w*|haplogroup"
    r"|admixture|paleoclimat\w*|palaeoclimat\w*|genome-wide)", re.I)
AS_OF_RE = re.compile(r"\(as of [^)]+\)|\bas of \w[\w.\s]*\d{4}", re.I)
PRESENT_TENSE_RE = re.compile(
    r"^The\s+[A-Z][\w'’-]+(?:\s+[A-Z][\w'’-]+)?\s+"
    r"(are|live|practice|practise|believe|herd|hunt|farm|worship|inhabit)\b")
VOICE_RE = re.compile(
    r"\b(proves? that|proved that|definitively (?:shows?|demonstrates?)"
    r"|it is a fact that|unquestionabl\w+|beyond dispute|settled science)\b", re.I)
SUPPORTS_RE = re.compile(r"\b(supports|challenges):\s*\[\[([^\]|#^]+)")

REL_FIELDS_GENEALOGY = [("trained_under", "trained"), ("trained", "trained_under")]
LINK_SOURCE_EXCLUDE = {"index.md", "log.md", "overview.md"}


class Reporter:
    def __init__(self, quiet: bool, no_info: bool, only=None):
        self.quiet, self.no_info, self.only = quiet, no_info, only
        self.counts = {"ERROR": 0, "WARN": 0, "INFO": 0}

    def emit(self, sev: str, check: str, rel: str, msg: str):
        # --only scopes both counts and output to the changed pages
        if not rel_matches_only(rel, self.only):
            return
        self.counts[sev] += 1
        if self.quiet or (self.no_info and sev == "INFO"):
            return
        print(f"{sev:5s} [{check}] {rel} :: {msg}")


def check_duplicate_slugs(pages: list[Page], rep: Reporter):
    by_stem: dict[str, list[Page]] = {}
    for pg in pages:
        if pg.is_template or pg.is_root_file:
            continue
        by_stem.setdefault(pg.slug.lower(), []).append(pg)
    sanctioned = {tuple(sorted((v[0], k))) for k, v in SUMMARY_FOR_HUB.items()}
    for stem, group in sorted(by_stem.items()):
        if len(group) < 2:
            continue
        folders = tuple(sorted({pg.hub_folder for pg in group}))
        if len(group) == 2 and folders in sanctioned:
            rep.emit("INFO", "duplicate-slug", group[0].rel,
                     f"stem '{stem}' shared with {group[1].rel} — sanctioned "
                     f"hub/summary pair; link the hub by full path")
            continue
        rels = ", ".join(pg.rel for pg in group)
        rep.emit("ERROR", "duplicate-slug", group[0].rel,
                 f"stem '{stem}' duplicated across: {rels} — bare [[{stem}]] "
                 f"links are ambiguous; rename per the type-suffix conventions")


def check_hub_reciprocity(pages: list[Page], resolver: Resolver, rep: Reporter):
    by_rel = {pg.rel: pg for pg in pages}
    for pg in pages:
        if pg.hub_folder not in SUMMARY_FOR_HUB or pg.is_template or pg.is_portal:
            continue
        summary_folder, field = SUMMARY_FOR_HUB[pg.hub_folder]
        targets = pg.fm_slugs(field)
        if not targets:
            rep.emit("ERROR", "hub-reciprocity", pg.rel,
                     f"hub page missing required '{field}' frontmatter field")
            continue
        target = targets[0]
        hits = [p for p in resolver.resolve(target) if p.hub_folder == summary_folder]
        if not hits:
            rep.emit("ERROR", "hub-reciprocity", pg.rel,
                     f"'{field}: {target}' does not resolve to a page in "
                     f"wiki/{summary_folder}/")
            continue
        summary = hits[0]
        hub_link_forms = (pg.rel[:-3].lower(), f"hubs/{pg.hub_folder.split('/')[1]}/{pg.slug}".lower())
        text = summary.all_text().lower()
        if not any(form in text for form in hub_link_forms):
            rep.emit("WARN", "hub-backlink", summary.rel,
                     f"summary page does not link back to its hub page {pg.rel} "
                     f"(link it by full path)")
    # summaries pointing at hubs that don't exist is fine (hub not yet written);
    # by_rel kept for future use
    _ = by_rel


def check_genealogy(pages: list[Page], resolver: Resolver, rep: Reporter):
    thinkers = {pg.slug.lower(): pg for pg in pages if pg.hub_folder == "thinkers"}
    for pg in thinkers.values():
        for src_field, recip_field in REL_FIELDS_GENEALOGY:
            for target in pg.fm_slugs(src_field):
                other = thinkers.get(target.lower())
                if other is None:
                    continue  # target page absent — orphan-actor lint is separate
                recip = [t.lower() for t in other.fm_slugs(recip_field)]
                if pg.slug.lower() not in recip:
                    rep.emit("WARN", "genealogy-symmetry", other.rel,
                             f"'{recip_field}' should include [[{pg.slug}]] "
                             f"(reciprocal of {pg.rel} '{src_field}')")


def check_supports_challenges(pages: list[Page], resolver: Resolver, rep: Reporter):
    for pg in pages:
        if pg.is_template:
            continue
        for m in SUPPORTS_RE.finditer(strip_fences(pg.all_text())):
            relation, target = m.group(1), m.group(2).strip()
            hits = [p for p in resolver.resolve(target) if p.hub_folder == "theories"]
            if not hits:
                continue
            theory = hits[0]
            if pg.slug.lower() not in theory.all_text().lower():
                rep.emit("WARN", "supports-challenges", theory.rel,
                         f"{pg.rel} declares '{relation}: [[{target}]]' but this "
                         f"theory page never references [[{pg.slug}]] — record the "
                         f"evidence relation on both ends")


def check_date_stamps(pages: list[Page], rep: Reporter):
    for pg in pages:
        if pg.is_template or pg.hub_folder in ("sources",):
            continue
        for n, line in enumerate(strip_fences(pg.body).split("\n"), start=1):
            if GENETIC_RE.search(line) and not AS_OF_RE.search(line):
                rep.emit("WARN", "date-stamp", pg.rel,
                         f"line {n}: fast-moving-science keyword with no "
                         f"'(as of Author Year)' stamp: {line.strip()[:90]!r}")


def check_orphans(pages: list[Page], resolver: Resolver, rep: Reporter):
    inbound: dict[str, int] = {pg.rel: 0 for pg in pages}
    for pg in pages:
        if pg.is_template or pg.path.name in LINK_SOURCE_EXCLUDE or pg.hub_folder == "queries":
            continue
        for target in set(pg.all_link_targets()):
            for hit in resolver.resolve(target):
                if hit.rel != pg.rel:
                    inbound[hit.rel] += 1
    for pg in pages:
        if (pg.is_template or pg.is_portal or pg.is_root_file
                or pg.hub_folder == "queries"):
            continue
        if inbound.get(pg.rel, 0) == 0:
            rep.emit("WARN", "orphan", pg.rel,
                     "no inbound links (index/log/overview/queries don't count)")


def check_reversed_names(pages: list[Page], rep: Reporter):
    thinkers = [pg for pg in pages if pg.hub_folder == "thinkers"]
    stems = {pg.slug.lower() for pg in thinkers}
    seen = set()
    for pg in thinkers:
        bits = pg.slug.lower().split("-")
        if len(bits) == 2:
            rev = f"{bits[1]}-{bits[0]}"
            pair = tuple(sorted((pg.slug.lower(), rev)))
            if rev in stems and rev != pg.slug.lower() and pair not in seen:
                seen.add(pair)
                rep.emit("WARN", "reversed-name", pg.rel,
                         f"both '{pg.slug}' and '{rev}' exist — likely the same "
                         f"person under both name orders; merge to surname-given")


def check_society_culture_twins(pages: list[Page], rep: Reporter):
    societies = {pg.slug.lower(): pg for pg in pages if pg.hub_folder == "societies"}
    cultures = {pg.slug.lower(): pg for pg in pages if pg.hub_folder == "cultures"}
    for stem, pg in sorted(societies.items()):
        for cand in (stem, f"{stem}-culture"):
            other = cultures.get(cand)
            if other and cand != stem:  # exact same stem already an ERROR elsewhere
                rep.emit("INFO", "society-culture-twin", pg.rel,
                         f"paired with {other.rel} — fine if deliberate "
                         f"(documented people vs. archaeological construct); "
                         f"cross-link them with `associated_with`, never identity")


def check_ethnographic_present(pages: list[Page], rep: Reporter):
    for pg in pages:
        if pg.hub_folder != "societies" or pg.is_template:
            continue
        for n, line in enumerate(strip_fences(pg.body).split("\n"), start=1):
            if PRESENT_TENSE_RE.match(line.strip()):
                rep.emit("INFO", "ethnographic-present", pg.rel,
                         f"line {n}: present-tense description — anchor to "
                         f"documentation_dates: {line.strip()[:80]!r}")


def check_voice_patterns(pages: list[Page], rep: Reporter):
    for pg in pages:
        if pg.is_template or pg.hub_folder == "debates":
            continue  # debate pages quote positions; skip
        for n, line in enumerate(strip_fences(pg.body).split("\n"), start=1):
            m = VOICE_RE.search(line)
            if m:
                rep.emit("INFO", "voice-pattern", pg.rel,
                         f"line {n}: '{m.group(0)}' — check the Voice and "
                         f"Attribution Protocol register")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None)
    ap.add_argument("--quiet", action="store_true", help="summary only")
    ap.add_argument("--no-info", action="store_true", help="suppress INFO findings")
    ap.add_argument("--only", default=None,
                    help="report only findings anchored to pages whose path "
                         "contains one of these substrings (comma/space "
                         "separated). Cross-page checks still use the full vault.")
    args = ap.parse_args()

    root = resolve_root(args.root)
    pages = load_vault(root)
    resolver = Resolver(pages)
    rep = Reporter(args.quiet, args.no_info, parse_only(args.only))

    check_duplicate_slugs(pages, rep)
    check_hub_reciprocity(pages, resolver, rep)
    check_genealogy(pages, resolver, rep)
    check_supports_challenges(pages, resolver, rep)
    check_date_stamps(pages, rep)
    check_orphans(pages, resolver, rep)
    check_reversed_names(pages, rep)
    check_society_culture_twins(pages, rep)
    check_ethnographic_present(pages, rep)
    check_voice_patterns(pages, rep)

    c = rep.counts
    print(f"\nlint_wiki: {len(pages)} pages — "
          f"{c['ERROR']} error(s), {c['WARN']} warning(s), {c['INFO']} info")
    return 1 if c["ERROR"] else 0


if __name__ == "__main__":
    sys.exit(main())
