# Wiki validation scripts

Purpose-built for this vault's schemas (see `CLAUDE.md`). All run from the vault
root and auto-discover `wiki/`. Python 3.10+.

## Close-out wrapper (use this)

```bash
scripts/check.sh                      # full final pass: schema → wikilinks → lint
scripts/check.sh --baseline           # run at ingest START; snapshots current broken links
scripts/check.sh --only whyte-,cornerville   # fast changed-files check (scoped reporting)
```

- Runs all three validators once, in canonical order, and prints a combined result.
- If a baseline exists (from `--baseline`), the full pass auto-diffs it and reports
  only **NEW** broken links — the right signal when a concurrent session may also be
  introducing breakage.
- **Do not re-run a clean validator to reassure yourself** — they are idempotent
  whole-repo scans; a second passing run is pure wall-clock cost.

## The three validators

| Script | Checks | Fails (rc=1) on |
|---|---|---|
| `validate_schema.py` | frontmatter fields + required body sections per page type | any ERROR |
| `check_wikilinks.py` | every `[[link]]` resolves (stems, aliases, hub paths) | any broken (or NEW broken under `--compare`) |
| `lint_wiki.py` | reciprocal/hub links, genealogy symmetry, date-stamps, duplicate slugs, orphans, voice patterns, ethnographic present | any ERROR |

## Shared flags

- `--root PATH` — vault root (default: cwd or the script's parent's parent).
- `--only "<substrings>"` — comma/space separated. **Scopes REPORTING** to pages whose
  path contains a substring; the full vault is still loaded so link resolution and
  cross-page reciprocity stay correct. Use for a fast changed-files check instead of
  piping output through `grep` (which re-runs the whole script). Run the full pass
  (no `--only`) once before finishing an ingest.
- `--quiet` — summary line only.
- `check_wikilinks.py`: `--json FILE` (write baseline) · `--compare FILE` (report only
  NEW broken links, exit nonzero only on new breakage).
- `lint_wiki.py`: `--no-info` (suppress INFO, e.g. sanctioned hub/summary slug pairs).
- `validate_schema.py`: `--sections-warn` (downgrade missing-section ERROR→WARN).
