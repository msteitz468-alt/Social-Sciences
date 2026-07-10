# scripts/ — Social Sciences Wiki lint tooling

Purpose-built for this wiki's CLAUDE.md schemas. Python 3.9+, stdlib only —
no dependencies. All scripts auto-detect the vault root (any directory
containing `wiki/`) or take `--root /path/to/vault`. All exit 1 on errors
(usable as a pre-commit gate) and never cap their output.

## validate_schema.py

Frontmatter + required-body-section validator. Encodes every page type's
schema: required fields, critical-nonempty fields, enum values, conditional
rules (`fieldwork_dates` mandatory for ethnography/excavation studies;
`parent_discipline` for subfields; hub pages' `analysis_type` and reciprocal
`*_page` field), date formats, and type tags. `[[unknown]]` always counts as
filled — the schemas demand explicitness, not omniscience.

    python scripts/validate_schema.py
    python scripts/validate_schema.py --sections-warn   # downgrade missing sections

## check_wikilinks.py

Broken-link checker. Resolves against filename stems (case-insensitive, with
a WARN on case mismatch), frontmatter `aliases:`, and path-style links
(`[[hubs/theory/practice-theory]]`) — the sanctioned way to link hub pages,
which intentionally share their summary's slug. Bare-stem links resolve to
the summary page by convention; genuine cross-folder ambiguity is a WARN.
Flags broken targets of 4+ words as likely free-text phrases wrapped in
`[[ ]]`. Links inside code fences and `templates/` files are ignored.

Proving "0 new broken links" after an ingest — no stash-comparison needed:

    # before integration:
    python scripts/check_wikilinks.py --json /tmp/links_baseline.json
    # after integration (exits 1 only on NEW breakage):
    python scripts/check_wikilinks.py --compare /tmp/links_baseline.json

## lint_wiki.py

The mechanical subset of CLAUDE.md's Lint Workflow:

| severity | check | what it catches |
|---|---|---|
| ERROR | duplicate-slug | same stem in two folders (hub/summary pairs → INFO) |
| ERROR | hub-reciprocity | hub missing `*_page`, or target absent from summary folder |
| WARN | hub-backlink | summary doesn't link back to its hub page |
| WARN | genealogy-symmetry | `trained_under`/`trained` not reciprocal |
| WARN | supports-challenges | evidence relation recorded on one end only |
| WARN | date-stamp | genetics/paleoclimate keyword with no "(as of Author Year)" |
| WARN | orphan | no inbound links (index/log/overview/queries don't count) |
| WARN | reversed-name | thinker present under both name orders |
| INFO | society-culture-twin | paired society/culture stems — check `associated_with` |
| INFO | ethnographic-present | present-tense "The X are..." on society pages |
| INFO | voice-pattern | crude wiki-voice red flags ("proves that", ...) |

    python scripts/lint_wiki.py
    python scripts/lint_wiki.py --no-info

Judgment items stay manual: voice violations beyond crude patterns,
`caused_by` that conflates sequence with causation, and near-synonym
duplicate titles need a reading pass.

## wikilib.py

Shared library (not a CLI): tolerant frontmatter parser (a linter must be
able to read the slightly-broken files it exists to report — strict YAML
parsers crash on exactly what you want flagged), wikilink extraction with
code-fence masking, alias/path-aware link resolution.

## Suggested post-ingest sequence (CLAUDE.md Step 5)

    python scripts/validate_schema.py && \
    python scripts/check_wikilinks.py --compare /tmp/links_baseline.json && \
    python scripts/lint_wiki.py --no-info
