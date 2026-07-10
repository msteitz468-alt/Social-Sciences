#!/usr/bin/env python3
"""wikilib.py — shared vault-parsing library for the Social Sciences Wiki lint tooling.

Stdlib only. The frontmatter parser is deliberately *tolerant*: a linter must be
able to read the slightly-broken files it exists to report, so this does not use
a strict YAML library. It parses the flat scalar / flow-list / block-list subset
the wiki's schemas use, and records anything it cannot parse as a warning
instead of crashing.

Used by: validate_schema.py, check_wikilinks.py, lint_wiki.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# [[target]] / [[target|Display]] / [[target#Section]] / [[target^block]]
WIKILINK_RE = re.compile(r"\[\[([^\[\]|#^]+)(?:[#^][^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
KEY_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s+-\s*(.*)$")

ROOT_FILES = {"index.md", "log.md", "overview.md"}
HUB_PORTALS = {"theory-hub.md", "thinkers-hub.md", "studies-hub.md"}

# hub folder -> (summary folder, reciprocal frontmatter field)
SUMMARY_FOR_HUB = {
    "hubs/theory": ("theories", "theory_page"),
    "hubs/thinkers": ("thinkers", "thinker_page"),
    "hubs/studies": ("studies", "study_page"),
}


def clean_scalar(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1].strip()
    return s


def split_flow(s: str) -> list[str]:
    """Split a flow-list interior on commas, respecting [[...]] bracket nesting."""
    items, depth, cur = [], 0, ""
    for ch in s:
        if ch == "[":
            depth += 1
            cur += ch
        elif ch == "]":
            depth -= 1
            cur += ch
        elif ch == "," and depth <= 0:
            items.append(cur)
            cur = ""
        else:
            cur += ch
    items.append(cur)
    return [clean_scalar(x) for x in items if x.strip()]


def parse_frontmatter(text: str):
    """Return (fm: dict[str, str|list], warnings: list[str], fm_text: str, body: str).

    Values are scalars (str) or lists of str. Tolerant: unparseable lines become
    warnings, not exceptions.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, ["no frontmatter block"], "", text

    fm: dict = {}
    warnings: list[str] = []
    current_list_key = None
    close_idx = None

    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            close_idx = i
            break
        if not line.strip():
            continue
        m_item = LIST_ITEM_RE.match(line)
        if m_item is not None and current_list_key is not None:
            if not isinstance(fm[current_list_key], list):
                fm[current_list_key] = [fm[current_list_key]]
                warnings.append(
                    f"line {i+1}: block-list items under scalar key '{current_list_key}'"
                )
            fm[current_list_key].append(clean_scalar(m_item.group(1)))
            continue
        if line.startswith("#"):
            continue
        m = KEY_RE.match(line)
        if m is None:
            warnings.append(f"line {i+1}: unparseable frontmatter line: {line.strip()!r}")
            current_list_key = None
            continue
        key, val = m.group(1), m.group(2).strip()
        if key in fm:
            warnings.append(f"line {i+1}: duplicate frontmatter key '{key}'")
        if val == "":
            fm[key] = []  # may fill via block list; empty list if not
            current_list_key = key
        elif re.fullmatch(r"\[\[[^\[\]]+\]\]", val):
            fm[key] = val  # scalar wikilink, not a flow list
            current_list_key = None
        elif val.startswith("["):
            if not val.endswith("]"):
                warnings.append(f"line {i+1}: unclosed '[' in '{key}'")
                fm[key] = clean_scalar(val)
            else:
                fm[key] = split_flow(val[1:-1])
            current_list_key = None
        else:
            fm[key] = clean_scalar(val)
            current_list_key = None

    if close_idx is None:
        warnings.append("frontmatter never closed with '---'")
        return fm, warnings, "\n".join(lines[1:]), ""

    fm_text = "\n".join(lines[1:close_idx])
    body = "\n".join(lines[close_idx + 1 :])
    return fm, warnings, fm_text, body


def strip_fences(text: str) -> str:
    """Blank out fenced code blocks, preserving line count/numbers."""
    out, in_fence = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
        else:
            out.append("" if in_fence else line)
    return "\n".join(out)


def normalize_target(t: str) -> str:
    t = t.strip()
    if t.lower().endswith(".md"):
        t = t[:-3]
    return t.strip().strip("/")


def link_targets(text: str) -> list[str]:
    return [normalize_target(m.group(1)) for m in WIKILINK_RE.finditer(strip_fences(text))]


def iter_links_with_lines(text: str):
    """Yield (lineno_1based, target) for every wikilink outside code fences."""
    for n, line in enumerate(strip_fences(text).split("\n"), start=1):
        for m in WIKILINK_RE.finditer(line):
            yield n, normalize_target(m.group(1))


class Page:
    def __init__(self, path: Path, root: Path):
        self.path = path
        self.rel = path.relative_to(root).as_posix()
        self.slug = path.stem
        parts = path.relative_to(root / "wiki").parts
        self.parts = parts
        # top-level folder under wiki/ ("" for wiki-root files like index.md)
        self.folder = parts[0] if len(parts) > 1 else ""
        # for hub pages: "hubs/theory" etc.; else same as folder
        self.hub_folder = "/".join(parts[:2]) if self.folder == "hubs" and len(parts) > 2 else self.folder
        self.is_template = "templates" in parts
        self.is_portal = path.name in HUB_PORTALS
        self.is_root_file = self.folder == "" and path.name in ROOT_FILES
        text = path.read_text(encoding="utf-8", errors="replace")
        self.fm, self.fm_warnings, self.fm_text, self.body = parse_frontmatter(text)

    # -- convenience -------------------------------------------------------
    def fm_list(self, key: str) -> list[str]:
        """Return a frontmatter value coerced to a list of cleaned strings."""
        v = self.fm.get(key)
        if v is None:
            return []
        if isinstance(v, list):
            return [x for x in (clean_scalar(i) for i in v) if x]
        v = clean_scalar(v)
        return [v] if v else []

    def fm_slugs(self, key: str) -> list[str]:
        """fm_list with wikilink brackets and display text stripped -> bare slugs."""
        out = []
        for item in self.fm_list(key):
            m = WIKILINK_RE.fullmatch(item)
            if m:
                out.append(normalize_target(m.group(1)))
            else:
                out.append(normalize_target(item.split("|")[0].strip("[]")))
        return [o for o in out if o]

    def headings(self) -> list[str]:
        return [
            m.group(1).strip().lower()
            for m in re.finditer(r"^#{2,4}\s+(.*)$", strip_fences(self.body), re.M)
        ]

    def all_text(self) -> str:
        return self.fm_text + "\n" + self.body

    def all_link_targets(self) -> list[str]:
        return link_targets(self.all_text())


def resolve_root(cli_root: str | None) -> Path:
    if cli_root:
        root = Path(cli_root).resolve()
        if not (root / "wiki").is_dir():
            sys.exit(f"error: {root} does not contain a wiki/ directory")
        return root
    for cand in (Path.cwd(), Path(__file__).resolve().parent.parent):
        if (cand / "wiki").is_dir():
            return cand
    sys.exit("error: no wiki/ directory found; pass --root /path/to/vault")


def load_vault(root: Path) -> list[Page]:
    return [Page(p, root) for p in sorted((root / "wiki").rglob("*.md"))]


def parse_only(only_arg: str | None) -> list[str] | None:
    """Split a --only value (comma/space/newline separated) into substrings.
    Returns None when nothing was passed (meaning 'report everything')."""
    if not only_arg:
        return None
    parts = [s for s in re.split(r"[,\s]+", only_arg.strip()) if s]
    return parts or None


def rel_matches_only(rel: str, only: list[str] | None) -> bool:
    """True if `rel` should be REPORTED. `only` is a list of path substrings
    (e.g. 'whyte-' or 'societies/cornerville.md'); None means report all.
    Note: --only scopes REPORTING, not resolution — the full vault is still
    loaded so links and reciprocity resolve correctly."""
    if not only:
        return True
    return any(o in rel for o in only)


class Resolver:
    """Resolve wikilink targets against the vault: stems, frontmatter aliases,
    and path-style links (used for hub pages that share their summary's slug)."""

    def __init__(self, pages: list[Page]):
        self.by_stem: dict[str, list[Page]] = {}
        self.by_alias: dict[str, list[Page]] = {}
        self.rel_noext: list[tuple[str, Page]] = []
        for pg in pages:
            self.by_stem.setdefault(pg.slug.lower(), []).append(pg)
            noext = pg.rel[:-3].lower() if pg.rel.lower().endswith(".md") else pg.rel.lower()
            self.rel_noext.append((noext, pg))
            for alias in pg.fm_list("aliases"):
                self.by_alias.setdefault(alias.lower(), []).append(pg)

    def resolve(self, target: str) -> list[Page]:
        t = normalize_target(target).lower()
        if not t:
            return []
        if "/" in t:
            hits = [pg for noext, pg in self.rel_noext if noext == t or noext.endswith("/" + t)]
            if hits:
                return hits
            t = t.rsplit("/", 1)[-1]  # fall back to the stem
        return self.by_stem.get(t, []) or self.by_alias.get(t, [])
