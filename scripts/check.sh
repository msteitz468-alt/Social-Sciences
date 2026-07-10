#!/usr/bin/env bash
# Run all three wiki validators once, chained, in the canonical close-out order.
#
# Usage:
#   scripts/check.sh                 # full final pass (schema, wikilinks, lint)
#   scripts/check.sh --baseline      # write a wikilinks baseline (run at ingest START)
#   scripts/check.sh --only whyte-   # fast changed-files check (scopes reporting)
#   scripts/check.sh --only whyte-,cornerville
#
# Notes:
# - The validators load the FULL vault regardless of --only; --only scopes only
#   which findings are reported, so link resolution and reciprocity stay correct.
# - Run the full pass (no --only) once before finishing an ingest; do not re-run a
#   clean validator "to be sure" — trust the first clean result.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASELINE="/tmp/scs_links_baseline.json"

if [[ "${1:-}" == "--baseline" ]]; then
  python "$HERE/check_wikilinks.py" --json "$BASELINE" --quiet
  echo "baseline written to $BASELINE — run scripts/check.sh at the end to diff."
  exit 0
fi

ONLY_ARGS=()
if [[ "${1:-}" == "--only" ]]; then
  ONLY_ARGS=(--only "${2:?--only needs a value}")
fi

rc=0
echo "== validate_schema =="
python "$HERE/validate_schema.py" "${ONLY_ARGS[@]}" || rc=1
echo; echo "== check_wikilinks =="
if [[ -f "$BASELINE" && ${#ONLY_ARGS[@]} -eq 0 ]]; then
  python "$HERE/check_wikilinks.py" --compare "$BASELINE" || rc=1
else
  python "$HERE/check_wikilinks.py" "${ONLY_ARGS[@]}" || rc=1
fi
echo; echo "== lint_wiki =="
python "$HERE/lint_wiki.py" "${ONLY_ARGS[@]}" || rc=1

echo
if [[ $rc -eq 0 ]]; then echo "ALL CHECKS PASSED"; else echo "CHECKS REPORTED ISSUES (rc=$rc)"; fi
exit $rc
