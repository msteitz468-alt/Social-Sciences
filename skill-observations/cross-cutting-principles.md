# Cross-Cutting Principles

Principles that apply to all skills. This file is read as a mandatory
checklist during any skill creation or regeneration.

---

## Active Principles

### 1. Prose classification lists and validator enums must be the same set
**Added:** 2026-07-08
**Applies to:** all skills / project CLAUDE.md schemas with enums
**Requirement:** When documentation names classification options (dispute types,
source types, protocol taxonomies), those exact values must appear in the
validator enum — or the prose must map each label to a specific enum value.
Do not leave a richer prose vocabulary than the frontmatter allows.
**Propagation:** opportunistic
**Status:** active
**Source observations:** Social Sciences #1 (source_type mixed), #4 (dispute_type source-reliability)
