# Skill Observation Log

Observations captured during task-oriented work. Each entry identifies a
potential skill improvement or new skill opportunity.

**Status key:** OPEN = not yet actioned | ACTIONED = skill updated/created |
DECLINED = user decided not to pursue

---

### Observation 1: source_type enum lacks mixed hybrid
**Status:** ACTIONED — Applied to CLAUDE.md Source Page schema + validate_schema.py (added `mixed` to source_type; hybrid guidance under schema) — review 2026-07-08
**Date:** 2026-07-08
**Session context:** Ingest of Du Bois *The Souls of Black Folk* (genre hybrid essay/history/observation)
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md schema / validate_schema)
**Type:** internal
**Phase/Area:** Source page frontmatter / validate_schema

**Issue:** CLAUDE.md study_type and methodological_approach allow `mixed`, but `source_type` allowed set does not. Using `source_type: mixed` failed `validate_schema.py`. Had to pick `primary-study` (because a studies/ page was warranted) while documenting hybridity in reliability_notes and methodological_approach: mixed.

**Suggested improvement:** Either add `mixed` to the source_type enum in CLAUDE.md + validate_schema, or document explicitly that hybrid works pick the primary genre and put hybridity in reliability_notes / methodological_approach only.

**Principle:** Schema enums and prose guidance must match; hybrid classics are common in social science (essay-collections with empirical chapters) and agents will reach for `mixed` if study_type already allows it.

### Observation 2: Escaped-pipe wikilinks inside markdown tables break check_wikilinks.py
**Status:** ACTIONED — Applied to CLAUDE.md Step 5 linting-repair (no piped wikilinks in markdown table cells) — review 2026-07-08
**Date:** 2026-07-08
**Session context:** Ingesting Simmel's *The Philosophy of Money* into the Social Sciences Wiki; building concept/source pages with "Semantic History" and "Section Plan" tables.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md, Lint Workflow / linting-repair section)
**Type:** internal
**Phase/Area:** Step 5 lint & validate — wikilink repair

**Issue:** To place a piped wikilink `[[slug|Display]]` inside a markdown table cell without the `|` breaking the table columns, the natural move is to escape it as `[[slug\|Display]]` (Obsidian renders this correctly). But `scripts/check_wikilinks.py` parses the escaped form as a link to target `slug\` and reports it BROKEN. This produced 8 spurious "new broken link" reports across the new concept and source pages until the escaped-pipe links were converted to plain text (each slug was already linked in prose elsewhere on the page).

**Suggested improvement:** Add a bullet to CLAUDE.md's linting-repair guidance: "Do NOT put piped wikilinks in markdown table cells. The escaped form `[[slug\|Display]]` renders in Obsidian but the wikilink checker reads it as a broken link to `slug\`; an unescaped `|` breaks the table. In table cells, use a bare `[[slug]]` or plain display text and link the slug in adjacent prose instead."

**Principle:** A convention that satisfies the *renderer* (Obsidian) can still fail the *validator* when the two parse the same syntax differently. When a wiki is checked by custom scripts, author to the intersection of what the renderer AND the validator accept — and encode that intersection as an explicit authoring rule so it isn't rediscovered page-by-page every ingest.

### Observation 3: Parallel subagent waits freeze / silent dropouts mid-ingest
**Status:** ACTIONED — Applied to CLAUDE.md Step 3 (filesystem completion checklist, non-blocking polls, inventory-before-integration, interrupt → inventory first, missing-range recovery/respawn) — review 2026-07-08
**Date:** 2026-07-08
**Session context:** Social Sciences Wiki ingest of Weber *The Protestant Ethic and the Spirit of Capitalism* — deployed-subagent strategy, 7 parallel extractors over disjoint cache ranges writing claims files only.
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3); also orchestration of `spawn_subagent` + `get_command_or_subagent_output` (platform)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors; main-thread recovery path

**Issue:** Parallel extraction subagents repeatedly produce a "frozen session" failure mode that the user has to interrupt:

1. **Opaque long wait.** After launching N background extractors, the main thread blocks on `get_command_or_subagent_output` with a long `timeout_ms`. From the user's view the session looks dead ("Did the subagent freeze?"). When the user messages mid-wait, the wait tool is cancelled/interrupted and the agent loses the completion signal without a clean status table.
2. **Silent per-range dropout.** On this PE run, 6 of 7 extractors wrote complete claims files (`range_1`, `3`–`7`; ~398 claims) within ~4 minutes; **range 2 never produced `/tmp/pe_cache/claims/range_2.md`** even though its cache slice existed and the other agents finished. No crash artifact, no claims partial, no main-thread recovery auto-triggered — the missing range was only discovered when the user asked to verify.
3. **Verify-only after user prompt.** The workflow relies on "monitor to completion" but does not hard-require a post-batch filesystem inventory (claims dir listing + expected filename set) before the main thread proceeds or before the next long wait. User had to say "please verify" to surface the gap.
4. **Recurrence.** User reports this keeps happening across sessions (not a one-off PE quirk): long parallel-subagent batches + blocking waits + occasional silent agent failure = session feels frozen and ranges are lost unless the human intervenes.

**Suggested improvement:**
1. **CLAUDE.md / ingest Step 3 — hard post-spawn checklist (structural enforcement, not narrative):** After spawning, do **not** sit on a single multi-minute blocking wait as the only progress mechanism. Instead: (a) spawn all; (b) short-poll or proceed to other main-thread work; (c) **mandatory filesystem inventory** of expected claims paths (`range_1.md`…`range_N.md`) before integration; (d) any missing path → main-thread recovery of that cache slice immediately (already in CLAUDE.md as recovery path — make the *detection* mechanical).
2. **Progress communication:** After spawn, tell the user expected agent count, cache paths, and that completion is checked by claims-file presence — not only by subagent task_ids — so a cancelled wait is not mistaken for total failure.
3. **Avoid one giant wait.** Prefer non-blocking status snapshots (`timeout_ms: 0`) interleaved with useful main-thread work (reading key passages, scaffolding frontmatter) over a single 10-minute block that looks frozen and is vulnerable to user-message cancellation.
4. **Platform/skill fix if available:** Document that `get_command_or_subagent_output` long waits are cancelled when the user sends a message; treat that as expected, not as agent death — always re-check task status + claims files after any interruption.
5. **Optional:** cap parallel extractors or stagger spawn if silent dropouts correlate with batch size (test; do not assume without evidence).

**Principle:** In multi-agent batch work, **completion is a filesystem fact (expected outputs present), not a wait-tool return value.** Blocking waits are a UX and cancellation hazard; silent agent death is expected enough that missing-output detection must be automatic and must trigger main-thread recovery without the user having to ask "did it freeze?"

### Observation 4: debate dispute_type enum lacks 'source-reliability' despite Contradiction Protocol naming it
**Status:** ACTIONED — Applied to CLAUDE.md Debate schema + validate_schema.py (`source-reliability`, `replication`); Contradiction Protocol maps prose → enum; refiled mind-self-society-authorship-debate.md — review 2026-07-08
**Date:** 2026-07-08
**Session context:** Ingest of Mead *Mind, Self, and Society* — created a debate page on the book's authorship/reconstruction (the text is a posthumous editorial compilation from student lecture notes).
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md debate schema / validate_schema)
**Type:** internal
**Phase/Area:** Debate page frontmatter / validate_schema dispute_type enum

**Issue:** CLAUDE.md's Contradiction and Replication Protocol explicitly classifies disputes as "factual dispute / interpretive difference / **source-reliability conflict** / failed replication," and the intuitive dispute_type for a debate about how a text was constructed is 'source-reliability'. But validate_schema.py's allowed dispute_type set is [theoretical, methodological, empirical, interpretive, ethical, priority] — 'source-reliability' fails. Had to file it as 'interpretive' (the live part of the dispute) while the shared ground is really empirical/philological facts about the text's construction.

**Suggested improvement:** Either add 'source-reliability' (and possibly 'replication') to the dispute_type enum in CLAUDE.md's Debate Page schema + validate_schema.py, or add a one-line note in the Debate schema that source-reliability/replication disputes should be filed as 'empirical' or 'interpretive'. Same class of defect as Observation 1 (source_type 'mixed'): the classification vocabulary in the prose protocols is wider than the frontmatter enum the validator enforces.

**Principle:** When a doc gives two vocabularies for the same thing — a rich classification list in prose and a narrow enum in the validator — agents reach for the prose term and hit a validation wall. Enum and prose guidance must be reconciled, or the prose must point explicitly to the enum value to use. Links to [[Observation 1 — source_type mixed]].

### Observation 5: Capital Vol I — silent subagent dropout ranges 4 & 5 (recurrence of Obs 3)

**Status:** ACTIONED — Applied with Observation 3 to CLAUDE.md Step 3 (confirmed-recurrent path; missing-range-only recovery/respawn) — review 2026-07-08
**Date:** 2026-07-08
**Session context:** Social Sciences Wiki ingest of Marx *Capital* Volume I — deployed-subagent strategy, 6 parallel extractors over disjoint cache slices under `/tmp/capital_v1_cache/`; ranges 1–3 and 6 wrote full claims files; ranges 4 and 5 produced nothing.
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3); platform `spawn_subagent` / `get_command_or_subagent_output`
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors; missing-output detection; main-thread recovery

**Issue:** Same failure class as **Observation 3** (Weber *Protestant Ethic*), now reproduced on Capital Vol I in the same session day:

1. **Silent per-range dropout (no artifact).** After batch spawn of 6 background extractors:
   - **Wrote claims:** `range_1_claims.md`, `range_2_claims.md`, `range_3_claims.md`, `range_6_claims.md` (complete; ~2.5k lines total claims).
   - **Never wrote:** `range_4_claims.md` (Parts 5–6 + Ch 23–24 + Ch 25 §§1–4; cache `/tmp/capital_v1_cache/range_4_3978_5223.txt` present, 1246 lines / ~47k words).
   - **Never wrote:** `range_5_claims.md` (Ch 25 §5 A–E England illustrations; cache `range_5_5224_6550.txt` present, 1327 lines / ~17k words).
   - No partial claims file, no error dump on disk, no automatic main-thread recovery. Gap found only because the user noticed and asked for new subagents / to log the pattern.

2. **Blocking multi-wait + user interrupt.** Main thread was on a long `get_command_or_subagent_output` multi-wait (`timeout_ms` 600000). User message mid-wait interrupted the wait (“Wait interrupted”); session felt frozen. User then reported ranges 4 and 5 not producing anything and asked to respawn — then asked to log that this **keeps happening**.

3. **Non-correlation with “hard” content alone.** Range 6 (Ireland + primitive accumulation — violence/colonial content) **succeeded**. Range 5 is empirical England illustrations (lighter theoretically). Range 4 is core accumulation theory. Dropout is not cleanly explained by content-filter density on the failed ranges; it looks stochastic / orchestration-side (silent agent death, lost completion, or cancelled wait without inventory).

4. **Recovery still human-triggered.** CLAUDE.md already says: if a subagent fails for any reason, main thread recovers *that range alone* from the cache slice. That path did not auto-fire because **failure was not detected** (wait interrupted; no post-batch claims-dir inventory). User had to instruct “start two new subagents.”

**Suggested improvement:**
1. **Treat Observation 3 as confirmed recurrent, not PE-specific.** Apply Obs 3’s hard post-spawn checklist on every multi-agent ingest: expected claims path set → `ls` inventory → missing → immediate main-thread recovery or respawn of *only* missing ranges — before integration and without waiting for the user to notice.
2. **Never use a single multi-minute multi-wait as the only completion signal.** After spawn: short non-blocking polls (`timeout_ms: 0`) + filesystem checks every few minutes; do scaffold/pre-read work on the main thread while agents run.
3. **On any user-message interruption of a wait:** first action is inventory of expected claims files and task status table — not re-planning the whole ingest.
4. **Respawn policy:** when a range is missing and cache exists, spawn a fresh extractor for that range only (as the user requested for Capital 4 & 5); do not re-run successful ranges.
5. **Optional metric:** log agent batch size and missing-range rate in `wiki/log.md` or session notes so the “keeps happening” claim becomes countable.

**Principle:** Silent subagent dropout in parallel ingest batches is a **recurring platform/orchestration failure**, not a one-off content or prompt bug. Completion must be defined as **expected output files present on disk**; missing files must auto-trigger recovery. User detection is not an acceptable control plane.

**Related:** Observation 3 (Weber PE range-2 dropout + frozen wait). This entry is the Capital Vol I confirmation with filesystem evidence (claims dir: r1/r2/r3/r6 present; r4/r5 absent while caches present).

### Observation 6: Concurrent full-session ingests create overlapping/duplicate canonical pages invisible to the wikilink checker
**Status:** OPEN
**Date:** 2026-07-08
**Session context:** Ingesting Weber *Politics as a Vocation* while a **separate parallel session was simultaneously ingesting Weber *Economy and Society***. Mid-ingest, my newly-created concept pages (`charismatic-authority.md`, `bureaucracy.md`) were edited by the other session to add authority-family `related_concepts` links, and it created `concepts/domination-herrschaft.md`, `concepts/charisma.md`, `traditional-authority.md`, `legal-rational-authority.md`, and a `concepts/rationalization.md` that duplicates the pre-existing `phenomena/rationalization.md`.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md — duplicate-page pre-scan, concurrent-session Edit-append rule, Naming Conventions vault-unique slugs)
**Type:** internal
**Phase/Area:** Step 1 duplicate pre-scan / Step 4 reconcile / lint

**Issue:** Two independent full sessions on the same author (Weber PaV + Weber E&S) independently created **overlapping canonical concept pages** the wikilink checker cannot flag because both targets resolve: my `legitimate-domination` (tripartite typology, with traditional/legal-rational covered *within* it) vs. the other session's `domination-herrschaft` (umbrella) + separate `traditional-authority` + `legal-rational-authority`; and my `charismatic-authority` vs. its `charisma`. The other session also duplicated `rationalization` (concept vs. existing phenomenon), producing a duplicate-slug lint ERROR and ~20 "ambiguous [[rationalization]]" warnings that bleed into my pages' links. CLAUDE.md's duplicate pre-scan (Step 1) only scans the *existing* vault; it cannot anticipate a *sibling session* creating the same entities in parallel. The Edit-append-not-Write rule protected existing pages but not the new-page namespace.

**Suggested improvement:** Add a note to CLAUDE.md Ingest Step 1/Step 4: when the same author/topic may be under concurrent ingest (multiple works from one thinker queued in `raw/`), (a) before scaffolding, agree a shared concept-slug convention for shared theoretical vocabulary (e.g. one canonical `domination-*`/authority-types scheme) or check for a sibling session's just-created pages by `ls`-ing `wiki/concepts` immediately before creating each new page; (b) at Step 4/lint, explicitly grep for near-synonym duplicate slugs created since session start (author's core concepts), since the wikilink checker passes them; (c) treat cross-session concept duplication (charisma/charismatic-authority, domination-herrschaft/legitimate-domination, rationalization concept/phenomenon) as a mandatory post-ingest merge item to surface to the user, not a silent pass.

**Principle:** Duplicate-canonical-page risk is highest not from a single session but from **concurrent sessions on the same author** — both resolve, so the wikilink checker is blind to it; only a same-session near-synonym grep plus an explicit "did a sibling session just create this?" check catches it. Links [[Observation 1 — source_type mixed]] only loosely; this is a concurrency/duplication defect, not an enum defect.

### Observation 7: Re-run the duplicate-page pre-scan at integration time when concurrent ingests are possible

**Date:** 2026-07-08
**Session context:** Ingesting Weber's *Economy and Society* (Tribe 2019) via the deployed-subagent strategy. A **concurrent *Politics as a Vocation* ingest** (plus Sumner/Cooley ingests) was running in the same vault. The Step-1 duplicate-page pre-scan came back clean, so I scaffolded and authored a `theories/legitimate-domination.md` summary and a `concepts/domination-herrschaft.md`. Only when I went to wire cross-links (Step 4) did I discover the concurrent session had, in the interim, created `theories/types-of-legitimate-rule.md` (a near-verbatim duplicate of my theory page, and the canonical slug a linter had already steered other pages toward) and `concepts/legitimate-domination.md` (a concept-layer near-duplicate). My theory page was a straight duplicate + slug collision; it had to be deleted and all references re-pointed.
**Skill:** CLAUDE.md ingest workflow (Deployed Subagent Strategy) — Step 1 duplicate pre-scan and Step 4 review. (Project-internal; the wiki's own CLAUDE.md, not an open-source skill.)
**Type:** internal
**Phase/Area:** Ingest Workflow — duplicate-page pre-scan / Step-4 reconciliation

**Issue:** The duplicate-page pre-scan is specified as a one-time Step-1 (pre-spawn) action. That is insufficient when other ingest sessions may write to the same name-space *during* a long ingest: a scan that is clean at scaffold time can be stale by the time pages are authored, producing duplicate pages and slug collisions that are expensive to unwind after cross-links exist.

**Suggested improvement:** In the CLAUDE.md "Step 4 — Review and tie together" (and/or the duplicate-page pre-scan paragraph), add: "When a concurrent ingest session may touch the same entities, **re-run the duplicate-page pre-scan immediately before authoring/integration**, not only at Step 1 — grep both name orders and synonymous titles again against the live tree, since another session may have created a canonical page (or a competing slug) in the interim. Adopt the existing canonical slug and merge into it rather than creating a parallel page." This complements the existing 'integrate with Edit-append, never a full Write' rule, which already anticipates concurrency but only for *updates*, not for *new-page* collisions.

**Principle:** In any workspace where multiple agents/sessions write shared, filename-addressed state, uniqueness checks must be re-validated at write time, not just at plan time — a plan-time scan is a stale read by the time of the write. (Same class of insight as the observation log's own check-then-act-then-verify numbering guard.)

### Observation 8: OCR "first edition" texts may silently be revised editions

**Status:** OPEN
**Date:** 2026-07-08
**Session context:** Ingest of Cooley *Human Nature and the Social Order* — Abika/public-domain OCR labeled and queued as 1902
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md source reliability / Chronological Uncertainty)
**Type:** internal
**Phase/Area:** Step 1 intake + source page reliability_notes

**Issue:** The source was filed and scaffolded as Cooley 1902 (first publication year). During extraction, claims flagged material impossible in a pure 1902 text: "we entered the war in 1917" / Argonne, citation of Sumner *Folkways* (1906), WWI Germans example, psychoanalysis end note. Standard scholarly fact: Cooley issued a revised *Human Nature* (1922). Treating the file as pure first edition would misdate claims and mislead chronology hygiene (theories dated by key-text publication vs later revision).

**Suggested improvement:** In CLAUDE.md Source-Type Handling or ingest Step 1 intake check, add: "For public-domain OCR monographs, scan for post-first-edition markers (war dates, later works cited, copyright lines, 'revised edition') before locking frontmatter `year`. Prefer year = first publication with an explicit reliability_notes clause when the *text body* is a later revision; never silently attribute revised interpolations to the first-edition date."

**Principle:** Bibliographic year and *textual state* are different facts. OCR labels and queue names often encode first publication; body content may be a later edition. Edition identity belongs in reliability_notes at intake, not as a late surprise during claim integration.

### Observation 9: Subagent page-creation prompts must put ALL mandatory frontmatter fields literally in the YAML block, not in prose

**Status:** OPEN
**Date:** 2026-07-08
**Session context:** Ingesting Simmel's *The Sociology of Georg Simmel* (Wolff 1950) via 10 deployed subagents; several agents owned new concept/institution pages and were given a YAML frontmatter block plus a prose instruction "fill all fields; sources_ingested: 1; last_updated: 2026-07-08".
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md — Ingest Workflow Step 3 subagent prompts)
**Type:** internal
**Phase/Area:** Step 3 (spawn extraction/page-writing subagents) / Step 5 (lint)

**Issue:** The literal YAML block handed to each page-owning agent did NOT contain `sources_ingested` or `last_updated` lines — those two fields were mentioned only in adjacent prose ("fill all; sources_ingested: 1; last_updated: 2026-07-08"). All 8 page-writing agents reproduced the YAML block verbatim and ignored the prose, producing 16 schema errors (2 per page) caught only at Step 5 lint. Agents copy the frontmatter block they are given and treat surrounding prose as commentary.

**Suggested improvement:** In Ingest Workflow Step 3, add a standing instruction: when a subagent is told to create a schema'd page, the prompt's YAML block must be COMPLETE and copy-pasteable — every mandatory field present with its value inline (including `sources_ingested`, `last_updated`, `tags`) — never rely on prose like "fill all fields" to supply a field absent from the block. The block the agent sees is the block the agent writes.

**Principle:** Subagents transcribe the concrete artifact they are given far more reliably than they synthesize from instructions about it. Any structure you need in the output should appear, complete, in the example — prose caveats around an incomplete template are silently dropped.

### Observation 10: Capture the wikilink baseline at session start when a concurrent ingest is possible

**Date:** 2026-07-08
**Session context:** Ingesting Marcuse *One-Dimensional Man* while a second session concurrently ingested *Dialectic of Enlightenment* (Horkheimer/Adorno) and Goffman/Chicago material into the same apparatus pages.
**Skill:** CLAUDE.md ingest workflow (Step 5 lint / snapshot-compare)
**Type:** internal
**Phase/Area:** Step 5 — "0 new broken links" snapshot-compare

**Issue:** CLAUDE.md says to snapshot `check_wikilinks.py --json baseline` "before integration." With a concurrent session, the other session's in-progress pages (adorno, horkheimer-max, mental-hospital) accrued ~40 broken links *during* my run, so a bare `check_wikilinks` at the end showed 45 broken and I had to grep-filter by filename to prove none were mine. A baseline captured at the very START of my session (before any of my edits) would have made `--compare` attribute breakage cleanly regardless of the other session's churn.

**Suggested improvement:** In the Step 5 snapshot-compare note, add: "when a concurrent ingest session may be running, capture the `--json` baseline at session start (before scaffolding), not merely before integration — the other session's breakage accrues throughout your run, and only a start-of-session baseline isolates *your* new broken links."

**Principle:** A differential check is only as clean as the moment its baseline is taken; under concurrency the baseline must predate all of your own edits, because the shared state is moving the whole time.

### Observation 11: Eight-agent Dahrendorf batch completed without silent dropout
**Status:** OPEN
**Date:** 2026-07-08
**Session context:** Social Sciences Wiki ingest of Dahrendorf *Class and Class Conflict* — 8 parallel extractors over disjoint cache ranges
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors

**Issue:** Prior observations (3, 5) documented silent per-range dropout on 6–7 agent Weber/Capital batches. This Dahrendorf run used **8 agents** over ~21k body lines with mandatory filesystem inventory of expected claims paths. **All 8** wrote complete non-empty claims files (`range_1.md`…`range_8.md`, ~3300 lines total) within ~6 minutes; no main-thread recovery needed. Short multi-waits + filesystem inventory used as completion signal.

**Suggested improvement:** Record as a positive counter-case to Obs 3/5: dropout is not automatic at N=8; keep the inventory checklist as the enforcement mechanism rather than lowering default N. Optional: note that denser theoretical slices (~2–3.5k lines) completed reliably when ranges aligned to chapter boundaries.

**Principle:** Multi-agent reliability should be measured by **output inventory**, not assumed from batch size alone; successful large batches are evidence, not proof that silent death is gone — keep detection structural.

### Observation 12: Proving "0 new broken links" under concurrent ingest sessions

**Date:** 2026-07-08
**Session context:** Ingesting *Dialectic of Enlightenment* while two other ingest sessions (Dahrendorf/conflict-theory and Whyte/Street Corner Society) ran concurrently against the same wiki.
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md Step 5 lint), task-observer methodology
**Type:** internal
**Phase/Area:** Step 5 — Lint and validate; the `check_wikilinks.py --compare baseline` proof of "0 new broken links"

**Issue:** The CLAUDE.md Step 5 method for proving no new broken links is a snapshot compare (`--json baseline` before, `--compare baseline` after). With concurrent sessions, the "after" snapshot includes *other sessions'* in-progress pages, which legitimately reference not-yet-created targets. My final compare reported "25 NEW broken links" — all of them from the parallel Whyte ingest (cornerville, corner-boys, whyte-boelen), none from my pages. The global new-broken count is therefore not a valid pass/fail signal for *my* ingest when other sessions are mid-flight.

**Suggested improvement:** When concurrent ingests are known to be running, don't rely on the global `--compare` count. After the compare, filter its output by *your own* new page slugs (`grep -iE 'adorno|horkheimer|culture-industry|...'`) to prove your ingest added zero broken links, and explicitly attribute the remaining new-broken entries to the other session(s). Add a note to CLAUDE.md Step 5 that under concurrent sessions the snapshot-compare must be filtered to the current ingest's slugs.

**Principle:** A shared-state validator's global delta is only a valid pass/fail signal for one actor when that actor is the sole writer. Under concurrent writers, prove your own cleanliness by filtering the diff to the artifacts you own, rather than trusting an aggregate count that other writers also move.

### Observation 13: Blumer SI range-2 silent dropout after Obs 3/5 "fixes" — rules not structurally enforced

**Status:** OPEN
**Date:** 2026-07-08
**Session context:** Social Sciences Wiki ingest of Blumer *Symbolic Interactionism: Perspective and Method* (1969) — deployed-subagent strategy, 4 parallel extractors over disjoint cache ranges under `/tmp/blumer_si_cache/`; claims expected at `claims/range_1.md`…`range_4.md`.
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3); also task-observer / orchestration of `spawn_subagent` + `get_command_or_subagent_output`
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor/inventory; missing-range recovery; user-facing latency

**Issue:** User believed silent-dropout / frozen-wait failure mode was **fixed** after Observations 3 and 5 were ACTIONED into CLAUDE.md Step 3 (filesystem completion checklist, non-blocking polls, inventory-before-integration, missing-range-only recovery). On this Blumer run the failure **recurred anyway**:

1. **Silent per-range dropout.** After batch spawn of 4 extractors:
   - **Wrote claims:** `range_1.md`, `range_3.md`, `range_4.md` (complete; dense extractions).
   - **Never wrote:** `range_2.md` (Ch.2 Mead reconstruction + Ch.3–5; cache `range_2_2501_4600.txt` present, 2100 lines / ~22k words).
   - No partial claims file, no crash artifact. Gap found only after wait interrupt + filesystem inventory (same class as Obs 3/5).

2. **Long multi-wait still used.** Main thread blocked on `get_command_or_subagent_output` with a long `timeout_ms` (~180s); user interrupted ("What the fuck is taking so long?" / earlier wait cancel). Session felt frozen for a long stretch of an otherwise finite theoretical monograph (~86k words, only 4 agents).

3. **Recovery path not auto-fired.** CLAUDE.md already requires: inventory expected claims paths; missing path → recover that range only. Inventory and main-thread recovery *did* eventually run — but only after the user-visible freeze/interrupt, not as an automatic tight loop (short poll → inventory → recover without looking dead). A respawn for range 2 alone was started; when it lagged, main thread wrote `range_2.md` (recovery labeled "Main-thread recovery (silent agent dropout)"). End state correct; **UX and latency still failed**.

4. **Positive counter-case does not mean fixed.** Observation 11 (Dahrendorf 8/8 success) was logged OPEN as evidence dropout is not automatic at N=8. User inference "we fixed it" from ACTIONED Obs 3/5 + occasional full-batch success was reasonable — and wrong. Documentation + one successful batch ≠ elimination of stochastic silent death.

5. **User impact.** Frustration that a fix believed done still produced multi-minute hangs and missing-range drama on a medium book. Trust cost is higher than the recovery cost once inventory runs.

**Suggested improvement:**
1. **Treat Obs 3/5 ACTIONED status as incomplete.** The CLAUDE.md *narrative* checklist is present; the failure is **non-enforcement at runtime**. Strengthen Step 3 with a non-optional operational loop that cannot be skipped for "I'll wait once for everyone":
   - After spawn: announce N, cache dir, expected filenames to the user immediately.
   - Poll with short `timeout_ms: 0` (or ≤30–60s) only; **never** a single multi-minute multi-wait as the sole progress mechanism.
   - Every poll cycle: `ls` expected claims paths; print present/missing table.
   - Any missing path after a grace window (e.g. 4–6 min from spawn, or when ≥N−1 peers have finished): **auto** main-thread recover or single-range respawn — do not wait for user interrupt.
2. **Hard cap on wait opacity.** If total wall-clock since spawn exceeds ~3 minutes without a full claims inventory, force inventory + status message to user even if agents are still "running."
3. **Optional structural aid:** a tiny project script `scripts/wait_claims.py --dir /tmp/.../claims --expect range_1.md ... --timeout 600` that exits nonzero on missing files — so completion is a command result, not agent memory of the checklist.
4. **Do not mark "fixed" from partial success.** Observation 11-style full batches should remain counter-evidence, not closure; close only when N consecutive multi-agent ingests complete with zero missing ranges *and* no user-facing freeze (or when a mechanical waiter replaces the soft checklist).

**Principle:** A recurring orchestration failure is not fixed when it is **documented** in the workflow; it is fixed when the **default execution path cannot complete without detecting missing outputs and recovering them** — without a long opaque wait and without the user having to ask why it is stuck. ACTIONED documentation that the agent still skips under cognitive load is the same class of defect as a skill rule without a verification step (task-observer Pre-Flight Principle): rules that are not structurally enforced will reappear as user-facing freezes.

**Related:** Observation 3 (Weber PE range-2 + frozen wait); Observation 5 (Capital Vol I ranges 4–5); Observation 11 (Dahrendorf 8/8 success — positive counter-case, not proof of fix). This entry is the **post-ACTIONED recurrence** on Blumer SI with filesystem evidence (claims dir: r1/r3/r4 present; r2 absent while cache present; later main-thread `range_2.md`).

### Observation 14: A full Write to a "new" scaffolded page can fail because a concurrent session already created it — treat the Read-precondition error as a collision signal

**Status:** OPEN
**Date:** 2026-07-08
**Session context:** Ingesting Parsons *The Social System* while a **separate concurrent session ingested Gouldner *The Coming Crisis of Western Sociology***. Both ingests independently needed `theories/structural-functionalism.md` and `thinkers/parsons-talcott.md`. My pre-scan at scaffold time (Step 1) showed both slugs absent, so I planned full Writes. By integration time (~18 min later) the Gouldner session had created both. My `Write` to `structural-functionalism.md` failed with "File has not been read yet" — the harness's Edit/Write safety gate, not a duplicate-page error — which is what surfaced the collision. I switched to Read-then-Edit-append, and the two sessions' content converged cleanly (Parsons's apparatus in attributed voice alongside Gouldner's critique; index/Structural_Sources/hub-portal entries merged without duplication).

**Suggested improvement:** In the Social Sciences Wiki ingest workflow (CLAUDE.md Step 4 "concurrent ingest" guidance), add: the duplicate-page pre-scan in Step 1 is a *point-in-time* check and goes stale during a long extraction phase. Before creating any page you scaffolded as "new," re-check existence immediately before writing; if a `Write` to a supposedly-new page returns the Read-precondition error, do not force it — Read the file and Edit-append, because a concurrent session has created it. The "integrate with Edit-append, never full Write, when a concurrent session may touch the same pages" rule should extend to *page creation*, not just updates to already-existing pages.

**Principle:** In multi-session/multi-agent environments, "this page doesn't exist yet" is only true at the instant you check it. Any write that assumes exclusive creation must revalidate at write time and degrade gracefully to merge-mode; the tooling's own preconditions (a read-gate failure) are a cheap collision detector if you read them as such instead of retrying the write.

### Observation 15: Mandatory user-visible progress checklist during multi-agent ingest
**Status:** ACTIONED — Applied to CLAUDE.md Deployed Subagent Strategy (Progress Checklist section + Step 3 ties) — 2026-07-08
**Date:** 2026-07-08
**Session context:** Homans *The Human Group* ingest; user experienced multi-minute "frozen" silence during parallel extract + integration, then requested CLAUDE.md require a progress checklist.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Ingest Workflow — Deployed Subagent Strategy)
**Type:** internal
**Phase/Area:** Step 3 orchestration / user-visible progress; UX of parallel extract

**Issue:** Filesystem-completion rules (claims files present) prevent silent *dropout* but do not prevent silent *UX*. Main thread can be working (7 extractors, integration) for several minutes with no chat updates; the user correctly experiences the session as frozen and interrupts. Optional "tell the user N agents" guidance was not strong enough — it was skipped or not refreshed during the wait.

**Suggested improvement:** Make a **user-visible progress checklist** mandatory at ingest start (TodoWrite + chat), with per-range rows during extract, ticks during integration, and a no-multi-minute-silence rule. On "are you frozen?" reply with checklist state first.

**Principle:** Completion signals for the *agent* (files on disk) and completion signals for the *user* (visible checklist updates) are different controls. Both are required; satisfying only the filesystem inventory still fails the human-in-the-loop.


### Observation 16: Word-count intake must first check for a text layer (image-only scans need OCR)

**Date:** 2026-07-09
**Session context:** Ingesting Garfinkel, *Studies in Ethnomethodology* (1967). The raw file was a 152-page PDF produced by OmniPage (an OCR program) but containing NO text layer — pdftotext returned 0 words. It was image-only (CCITT scans). Required an ocrmypdf pass (~2 min) before any word-count intake or slicing could happen.

**Skill:** wiki ingest workflow (CLAUDE.md "Step 1 — word-count intake check")
**Type:** internal
**Phase/Area:** Deployed-subagent ingest, Step 1 intake

**Issue:** The documented intake check ("wc -w the raw text and compare against expected length") silently assumes a machine-readable text layer. A scanned/image-only PDF returns 0 words, which looks like an empty/failed file rather than a routine "needs OCR" condition. The producer metadata was misleading (OmniPage suggested text existed).

**Suggested improvement:** Add to the intake step: before wc -w on a PDF-derived file, verify a text layer exists (pdffonts / pdftotext word count); if ~0 words but pdfimages shows page images, run OCR (ocrmypdf --sidecar, or tesseract) to produce the text, and note "OCR-derived text — proof against silent recognition errors" in the source page reliability_notes. Treat 0 words from a nonempty PDF as an OCR signal, not a corrupt-file error.

**Principle:** Intake heuristics that assume a text layer fail silently on image-only scans; a robust intake distinguishes "no text extracted" from "no content" and routes the former to OCR before proceeding.

### Observation 17: Lipset Political Man 7-agent batch completed without silent dropout
**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Social Sciences Wiki ingest of Lipset *Political Man* — 7 parallel extractors, disjoint ranges ~3100–6100 lines under `/tmp/pm_cache/`
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors

**Issue:** Positive recurrence data after Obs 3/5/13 pattern: all 7 extractors wrote non-empty claims files (`range_1.md`…`range_7.md`, ~296 claims) within ~2–3 minutes; filesystem inventory before integration found zero missing ranges. Progress checklist + non-blocking multi-wait used; no user "are you frozen?" interrupt this session.

**Suggested improvement:** Keep documenting successful batch sizes (here 7, content-weighted, ~3–6k lines each) alongside failures so the default agent count is evidence-based rather than folklore "avoid 6."

**Principle:** Success cases are as informative as dropouts for calibrating parallel extraction batch size; log them so the workflow's risk model is not only failure-driven.

### Observation 18: Duplicate pre-scan should cover concept slugs, not just thinkers/theories

**Date:** 2026-07-09
**Session context:** Ingesting Blau, *Exchange and Power in Social Life* (1964) via the deployed-subagent workflow.
**Skill:** CLAUDE.md ingest workflow (Step 1 duplicate-page pre-scan)
**Type:** internal
**Phase/Area:** Step 1 scaffolding — duplicate-page pre-scan

**Issue:** The Step-1 duplicate pre-scan, as written, targets "the thinkers/entities the ingest will touch" (name orders, synonymous theory titles, cross-folder splits). I ran it for thinkers/theories but did not pre-grep the *concept* slugs the ingest would create. Two concept pages I planned to create — `relative-deprivation` and `reference-group` — already existed from a prior Merton ingest. The collision was caught only reactively, by the Write tool's "file already exists" error, not by the pre-scan. In a full-Write (rather than Edit) integration, or with a subagent authoring, this could have clobbered existing pages.

**Suggested improvement:** Extend the Step-1 duplicate pre-scan instruction to explicitly include a grep of every candidate **concept** slug the ingest intends to create (not only thinker/theory/school names), since fine-grained concept pages are the highest-volume page type and the most likely to already exist under a shared analytic name (relative-deprivation, reference-group, exchange, legitimation, institutionalization all recur across sources). One `ls concepts/ | grep -f candidate_slugs` pass before authoring is cheap.

**Principle:** Collision risk scales with the *number and genericness* of pages a source creates, and concept pages are both the most numerous and the most likely to be shared across sources. A duplicate pre-scan that checks only proper-noun entities (people, schools) misses the highest-probability collision class (common analytic concepts). Pre-scan the full create-set, weighted toward the most generic slugs.

### Observation 19: Disciplinary-era slugs are a recurring broken-wikilink trap in the Social Sciences Wiki

**Date:** 2026-07-09
**Session context:** Ingest of Skocpol, *States and Social Revolutions* (1979) into the Social Sciences Wiki.
**Skill:** New skill candidate: social-sciences-wiki-ingest (or a CLAUDE.md addendum)
**Type:** internal
**Phase/Area:** Integration / wikilink hygiene (Step 4–5 of the deployed-subagent ingest workflow)

**Issue:** CLAUDE.md defines seven named **Disciplinary Eras** (Precursors, Founding Era, Classical Era, Fieldwork Revolution, Postwar Expansion, **Critical Turn**, Contemporary) and many **deep-time periods**, all written kebab-cased in frontmatter (`era_origin: critical-turn`). These read like linkable page slugs, so it is natural during page-writing to render them as body wikilinks (`[[critical-turn|Critical Turn]]`). But no page exists for any era, so every such link is a broken wikilink. This ingest introduced three (`critical-turn` in the theory page, study summary, and study hub) and they only surfaced at the final `check_wikilinks.py` pass. This is a predictable, recurring class of error because era tags appear in almost every knowledge-layer page's frontmatter.

**Suggested improvement:** Add an explicit rule to the ingest guidance (CLAUDE.md "Naming Conventions" or the wikilink-hygiene bullets in Step 5, and/or a future ingest skill): "Disciplinary eras and deep-time periods are frontmatter TAG VALUES, not pages — never wrap them in `[[...]]` in body prose; write them as bold/plain text (e.g. **Critical Turn**). Only create/link an era page if one is deliberately built under `timelines/`." Optionally, teach subagents this in the extraction prompt so era references never come back bracketed.

**Principle:** In a wiki whose frontmatter vocabulary (eras, periods, regions, tags) is kebab-cased exactly like page slugs, controlled-vocabulary tag values are a standing source of phantom wikilinks. The fix is a single explicit "these are tags, not pages" rule applied at authoring time, which is far cheaper than catching each instance at the final link-check. Distinguish linkable entities from controlled-vocabulary tags once, in the guidance, rather than rediscovering the boundary every ingest.

### Observation 20: Under many concurrent ingests, shared bookkeeping files need append/insert, not Edit

**Date:** 2026-07-09
**Session context:** Ingesting Polanyi, *The Great Transformation*, while 5+ other ingest sessions (Bourdieu, Skocpol, Massey–Denton, Hochschild, Tilly, Wilson) ran concurrently and repeatedly rewrote wiki/index.md, wiki/overview.md, and wiki/log.md.
**Skill:** CLAUDE.md ingest workflow (Step 4 integration / Step 6 bookkeeping)
**Type:** internal
**Phase/Area:** concurrent-session integration of shared apparatus files (index/log/overview)

**Issue:** CLAUDE.md already says to Edit-append (not full Write) shared *content* pages under concurrent sessions. But for the shared *bookkeeping* files (index.md, overview.md, log.md), the Edit tool itself became unusable: with many sessions writing every few seconds, the file changed on disk between the required Read and the Edit, so Edit repeatedly failed with "file has been modified since read" even on the immediately-following call. The reliable fallbacks were: (a) for append-only log.md and dated coverage notes in overview.md, a shell heredoc `>>` append (atomic, no clobber, no read-state dependency); (b) for catalog bullet-lists in index.md, `sed -i '/anchor/a <new line>'` inserts after a stable plain-text anchor (single quick op, verified by grep after) — safe here because the inserted text is whole new bullet lines, not substitutions inside piped wikilinks.

**Suggested improvement:** Add a note to the ingest workflow's bookkeeping step: under heavy concurrency, update append-only files (log.md, dated overview notes) with a shell append rather than Edit, and update index.md catalog lists with anchored `sed` line-inserts (append whole bullets, never substitute inside `[[slug|Display]]`), verifying with grep. Reserve the Edit tool for content pages where Read-then-Edit is not being invalidated by other writers.

**Principle:** The right write primitive depends on contention, not just file type. Edit's read-before-write contract is a liveness hazard on hot, many-writer files; append-only and line-insert operations that don't depend on a stable prior read are the robust choice there. Match the tool to the concurrency regime.

### Observation 21: Theoretical ethnographies can switch field sites mid-book without TOC warning
**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingest of Bourdieu *The Logic of Practice* — Book II Ch.1 is **Béarn** (French peasant inheritance/adot), Ch.2–3 + Appendix are **Kabyle**. TOC lists Book II under practical logics without flagging the site switch; a naive brief that labels all Book II as Kabyle would mis-file society claims.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Deployed Subagent Strategy / society pages)
**Type:** internal
**Phase/Area:** Step 2 chunk briefs; society claim routing

**Issue:** Extractor range 4 correctly flagged Béarn material as entity-mismatch vs the established `kabyle` society slug and filed it under Miscellaneous/theory targets. Without that discipline, matrimonial-strategy claims would have been written onto the Kabyle society page in ethnographic voice for the wrong people.

**Suggested improvement:** In CLAUDE.md ingest guidance for multi-site theoretical monographs: when scaffolding society pages from a theory book's fieldwork, spot-read Book II / empirical chapters for site names (not only the Preface) and list **all** documented populations in the extractor brief. Instruct agents: if material is near-match to target society but site differs, file under Miscellaneous with mismatch flag (already a standing instruction — emphasize site-switching as a common trigger).

**Principle:** A book's best-known field site is not the only field site. Spot-read empirical chapters for place names before assigning society ownership; treat site switches as entity boundaries, not chapter flavor.

### Observation 22: Line-range/topic mismatch at a chapter boundary causes a silent extraction gap between two subagents

**Date:** 2026-07-09
**Session context:** Deployed-subagent ingest of Bourdieu & Passeron, *Reproduction* (4 line-range extractors). Range 3's slice was full-text lines 5690–8900 but its brief said "Book II ch. 2–3 only"; Range 4's slice began at 8901 with brief "ch. 4 + Appendix." Book II ch. 4 actually began at line ~8483, inside Range 3's slice. The Range 3 agent honored the *topical* brief ("ch. 2–3") over its *line-range*, deliberately declining to extract lines 8483–8900 (the ch. 4 opening) as "out of scope." Range 4 started at 8901. Result: ~420 lines — the entire theoretical opening of ch. 4, incl. the load-bearing "relative autonomy / dependence through independence" thesis — were covered by neither agent. Caught on the main thread only because I cross-checked the two agents' reported coverage boundaries against each other and against the chapter map, then read + recovered the gap.

**Suggested improvement:** In the deployed-subagent ingest workflow (CLAUDE.md Step 2–3), add a standing rule: **the assigned line-range is authoritative; topical/chapter labels in a brief are orientation only.** Every extraction prompt should say "extract everything within your exact line-range regardless of where chapter boundaries fall inside it; do not stop early because content seems to belong to another chapter." Additionally, in the Step-3 completion inventory, add an explicit **contiguity/overlap check**: verify that consecutive agents' *actually-covered* line ranges (from their COVERAGE reports) meet with no gap — not just that each claims file is non-empty. A non-empty file per range does not prove full line coverage.

**Principle:** When work is partitioned by an objective key (line numbers) but each partition also carries a human-readable topical label, agents may follow the label and silently drop material where the two disagree at a boundary. Make the objective key authoritative in the instructions, and verify coverage by reconciling adjacent partitions' reported boundaries — the per-partition "did it produce output" check cannot detect a between-partition gap.

### Observation 23: Era-tag-as-wikilink and escaped-pipe-in-table are recurring, lint-catchable integration defects

**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingesting Collins *Conflict Sociology* (1975), 9-agent extraction. During integration I wrote `[[critical-turn|critical turn]]` (a disciplinary-era *tag*, not a wiki page) in three places and one `[[slug\|Display]]` escaped-pipe wikilink inside a markdown key-texts table cell in the theory hub. Both produced broken links caught only by the final `check_wikilinks` pass, requiring a fix-and-recheck cycle.

**Suggested improvement:** Add a pre-lint integration checklist item to the Social Sciences ingest workflow (CLAUDE.md Step 4/5 already warns about escaped pipes in tables and era-tags — but the enforcement is narrative). Before the first validator run, grep new/edited pages for two patterns: (a) `\[\[(precursors|founding-era|classical-era|fieldwork-revolution|postwar-expansion|critical-turn|contemporary)` (era tags wrongly linked), and (b) `\[\[[^]]*\\\|` (escaped-pipe wikilinks, which break in table cells). Both are 100%-mechanical and catchable in one grep before the full lint.

**Principle:** When a known, recurring authoring mistake has a mechanical signature, a targeted grep run *before* the expensive whole-repo validator is cheaper than the write→lint→fix→re-lint loop. Turn recurring lint failures into pre-flight greps.

### Observation 24: Deployed-subagent ingest robust under three simultaneous concurrent sessions via Edit-append

**Status:** OPEN
**Date:** 2026-07-09
**Session context:** The Collins *Conflict Sociology* ingest (9 parallel extractors, all claims files landed, 663 claims, no silent dropout) ran while THREE other sessions concurrently ingested Putnam *Bowling Alone*, Elias *The Civilizing Process*, and Wallerstein *Modern World-System*. Shared pages (disciplines/sociology, disciplines/political-sociology coverage notes; institutions/the-state and phenomena/state-formation frontmatter; index.md lists; theory-hub portal) were touched by multiple sessions in the same window. Every shared-page edit used the Edit tool with unique anchors (never a full Write); all sessions' additions coexisted with no clobbering. The session-start `--baseline` snapshot plus final `--compare` cleanly attributed all NEW broken links to the *other* sessions' pages (Wallerstein/Bourdieu-Passeron), confirming this ingest introduced zero.

**Suggested improvement:** Reinforce in the ingest workflow that the `--baseline`/`--compare` wikilink pattern is not just for "a concurrent session may break links" but is the *only* reliable way to attribute broken links to the right session when 3+ run at once — and that a broken link in the final report pointing at a page you never touched is expected, not a defect to chase. Keep filtering `--compare` output by *your* page slugs.

**Principle:** Under heavy concurrency, correctness attribution matters as much as correctness: a session must be able to prove *its own* footprint is clean without being blocked by other sessions' in-flight breakage. Baseline-snapshot + slug-filtered compare gives per-session attribution.

### Observation 25: Ingesting a source leaves stale "not yet ingested" flags and pre-broken forward-links on existing pages; add a pre/post grep sweep

**Date:** 2026-07-09
**Session context:** Ingesting Bourdieu, *Outline of a Theory of Practice* (1972/1977) — a well-trodden source into a vault already dense with Bourdieu coverage.
**Skill:** Social Sciences wiki ingest workflow (project CLAUDE.md)
**Type:** internal
**Phase/Area:** Ingest Workflow Step 1 (duplicate/forward-reference pre-scan) and Step 4 (integration)

**Issue:** Existing pages had accumulated two kinds of debt that only a targeted grep surfaces: (1) **pre-broken forward-links** — ~23 pages already wrote `[[bourdieu-outline-1977]]` and `[[levi-strauss-claude]]` before those pages existed, counting as broken links until this ingest created the targets (they auto-"fixed" on creation); (2) **stale "not yet ingested" flags** — the Bourdieu *thinker hub* still declared *Outline* AND *Reproduction* "not yet ingested," even though *Reproduction* was ingested in a prior session and never reconciled. The `[[unknown|Claude Lévi-Strauss]]` placeholder link also persisted across three pages. None of these are caught by schema/lint; the broken-forward-links are caught by check_wikilinks but only reported as generic breakage, and the stale flags are pure prose falsehoods invisible to all validators.

**Suggested improvement:** In Step 1's duplicate-page pre-scan, add a **forward-reference sweep** for the source's anticipated slug(s) and title: `grep -rn "<new-slug>\|<Source Title>\|not yet ingested" wiki/` — this reveals (a) pages already linking the to-be-created page (confirm the planned slug matches what the vault expects), and (b) every "not yet ingested / queued / not yet ingested as primary" flag naming this source, which becomes a checklist of provenance updates for Step 4. Also grep for `[[unknown|<Author Name>]]` to catch placeholder links the new page can resolve. Re-run the same grep in Step 4 to confirm no stale flag survived.

**Principle:** A wiki that anticipates future ingests (writing forward-links and "not yet ingested" flags) accumulates reconciliation debt that no schema/link validator flags as *content* errors — a page can be fully valid and still falsely say a now-ingested work is unavailable. Making "grep the vault for the source's name and slug, before and after" a standard ingest step turns that invisible debt into an explicit, cheap checklist and prevents cross-session staleness.

### Observation 26: Extraction subagents silently truncate large line-range slices unless told to read in sequential chunks

**Date:** 2026-07-09
**Session context:** Ingesting Coleman, *Foundations of Social Theory* (1990) — 7-agent deployed-subagent extraction over Parts I–V of a ~41k-line body.
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md Deployed Subagent Strategy, Step 3)
**Type:** internal
**Phase/Area:** Step 3 — spawning extractors / read-cap handling

**Issue:** Of seven range-partitioned Sonnet extractors, most ranges 5,000–5,700 lines were read fully by agents that spontaneously chunked their Read calls (range_2 read 5,470 lines in 5 passes; range_4 read 5,730 in several). But range_6 (~5,277 lines) hit a single-read token cap, stopped silently ~3,150 lines in, and its agent reported the shortfall only in its completion summary — requiring a scoped gap-fill agent (range_6b) for ch.23–24, which happened to contain the highest-value "replacement of primordial social capital" material. The behavior is stochastic: identical-size slices either get chunk-read or get truncated depending on whether the agent decides to chunk. The current prompt says "read only that range" and "report actual coverage," but does not *mandate* sequential chunked reading, so truncation is left to chance.

**Suggested improvement:** In the Step 3 standing extraction-prompt instructions, add an explicit directive: "Your slice may exceed a single Read's capacity. Read it in sequential chunks (e.g. 1,500–2,000 lines per Read) until you reach your last assigned line; do not stop after one Read. State your exact last-covered line." Additionally, when sizing ranges (Step 2), keep single-agent slices at ≲3,500 lines OR pre-cut sub-slices for any range >~4,000 lines so a single-read cap cannot truncate silently. This makes the gap-fill a planned fallback rather than a post-hoc rescue.

**Principle:** When a subagent's assigned input can exceed its single-read capacity, mandate chunked reading explicitly and size inputs defensively — relying on the agent to notice and self-chunk produces stochastic silent truncation, and the truncated tail is disproportionately likely to hold end-of-section synthesis (the most valuable material).

### Observation 27: Filter-prone sexuality/charged-discourse source ingested via 5-agent batch with zero content-filter blocks

**Date:** 2026-07-09
**Session context:** Ingesting Foucault, *The History of Sexuality* Vol. I (deployed-subagent workflow) — a source dense in charged discourse (sexuality, 19th-c. "perversions," the sexualization of children, the 1867 Jouy child-case, incest, state racism/Nazism).
**Skill:** CLAUDE.md ingest workflow (sensitive-content triage)
**Type:** internal
**Phase/Area:** Step 2 sensitive-content triage / Step 3 spawn

**Issue:** Per triage, I routed only the single most-charged chapter (Part Two Ch.2, "The Perverse Implantation") to the main thread and gave the other 5 ranges to Sonnet subagents — including range_1 (which contained the Jouy child-case) and range_5 (child-sexualization, incest, degeneration/racism). All 5 subagents returned full-fidelity extractions with verbatim quotes and ZERO content-filter blocks; all 6 claims files landed non-empty on first inventory. This matches the CLAUDE.md note that filter blocks on such sources are "effectively stochastic" — but here the observed block rate was zero across a whole filter-prone book.

**Suggested improvement:** The triage rule (route the single densest range to main thread, size all ranges for comfortable single-range main-thread recovery) worked and cost little. No rule change needed; worth recording as confirmatory evidence that the current triage + recovery-path design is correctly calibrated (don't over-route to main thread on charged-but-analytic theory sources — subagents handle them fine, and the recovery path is the real safeguard).

**Principle:** For scholarly/analytic treatments of charged subject matter (as opposed to verbatim atrocity documentation), default to subagent extraction with ONE sensitive range main-threaded; reserve heavier main-thread routing for high-concentration graphic verbatim material. The Step-3 recovery path, not pre-emptive over-routing, is the safeguard.

### Observation 28: Date-stamp lint keywords ("genetic", "admixture", "climate") false-positive on social-theory prose and recursively on the log entry describing the fix

**Date:** 2026-07-09
**Session context:** Ingesting Beck, *Risk Society* (deployed-subagent). The final lint flagged `theories/risk-society.md` twice for "fast-moving-science keyword with no '(as of Author Year)' stamp": once on the frontmatter word "genetic" (in Beck's 1986 hazard typology "nuclear, chemical, genetic") and once on "admixtures" inside a verbatim Beck quote ("the sociology of all the admixtures, amalgams and agents of knowledge"). Neither is an archaeogenetic/paleoclimate empirical claim. Rewording to "biotechnological" and trimming the quote cleared them — but then the *log.md ingest entry that described the fix* itself contained the words "genetic"/"admixtures" and tripped the same warning, requiring a second reword ("a fast-moving-science keyword").
**Skill:** New skill candidate / CLAUDE.md refinement (Social Sciences Wiki ingest workflow) — closest existing: [[social-sciences-wiki lint conventions]] (the wiki's Step 5 lint guidance)
**Type:** internal
**Phase/Area:** Step 5 lint / `lint_wiki.py` date-stamp check

**Issue:** The date-stamp keyword matcher (`genetic|admixture|climate|aDNA|genom|paleo|...`) is a bare substring match with no domain gating. In a social-theory ingest, these words appear legitimately in non-archaeogenetic senses (biotech *hazards*, a quoted metaphor "admixtures ... of knowledge", "climate risk" as a rhetorical example). Each is a false positive that costs an author edit, and the trap recurs when the ingest's own bookkeeping narrative quotes the offending word.

**Suggested improvement:** Two options, pick per taste: (a) When authoring social-theory/sociology pages, pre-empt the known false-positive keywords — prefer "biotech(nological)" over "genetic", trim quotes that carry "admixture"/"climate", and when writing the log/index bookkeeping entry describing such a fix, do not restate the literal trigger word. (b) Better structural fix: narrow `lint_wiki.py`'s date-stamp check to skip `log.md`, and gate the keyword on co-occurrence with a datable-claim signal (a year, "study", "et al.", "sample") so a bare metaphor doesn't fire.

**Principle:** Bare-substring lint rules built for one discipline (archaeogenetics date-stamping) produce recurring false positives when the same corpus hosts another discipline (social theory) that uses the words differently. The cheapest durable fix is either to gate the rule on a second co-occurring signal or to exclude bookkeeping files; absent that, authors should learn the discipline's specific false-positive vocabulary and route around it — including in the prose that documents the workaround.

### Observation 29: Differently-labelled ebook files can be byte-identical duplicates of ONE volume, hiding a missing volume — word-count intake + diff catches it

**Date:** 2026-07-09
**Session context:** Ingesting Habermas, *The Theory of Communicative Action*. The collection held two files apparently for the two volumes: one azw3 labelled "Lifeworld and Systems" and one epub labelled "The Critique of… 2,2" with a different ISBN and different filename metadata.
**Skill:** CLAUDE.md ingest workflow (Step 1 word-count intake / duplicate pre-scan)
**Type:** internal
**Phase/Area:** Step 1 intake / duplicate-page pre-scan (extended to source files)

**Issue:** After ebook-convert, both files had IDENTICAL word/line counts (5177 lines / 189038 words). `diff -q` confirmed they were byte-identical, and both were Volume 2 (Lifeworld and System). Volume 1 (Reason and the Rationalization of Society) — which holds the foundational apparatus (communicative rationality, validity-claims typology, action typology) — was NOT in the collection at all, despite the metadata strongly implying a two-volume set was present. Distinct ISBNs, filenames, and formats masked that the two files were the same content. This is a stronger form of [[Observation 8]] (edition mislabeling): here the mislabeling hid a *missing volume*, which would have silently produced a half-complete "TCA" ingest asserting Vol-1 concepts as if sourced.

**Suggested improvement:** Add to the Step-1 intake / duplicate pre-scan: when a source is a multi-volume/multi-file work, after converting, compare word/line counts and run `diff -q` (or checksum) across the files BEFORE planning sections. Identical counts → verify each file's actual title/volume from its first lines; treat metadata/filename/ISBN as unreliable. If a volume proves missing, scope every page to note it and flag to the user, rather than filling from back-references as if primary.

**Principle:** Source-file identity must be verified from *content*, not from filename/ISBN/format metadata — collections contain same-content twins with divergent metadata, and a twin can stand in for a genuinely absent volume. A cheap checksum/word-count diff at intake prevents a structurally incomplete ingest.

### Observation 30: Concurrent sessions on a shared page can hand off cleanly via a de-link/re-link protocol

**Date:** 2026-07-09
**Session context:** While this session ingested TCA Vol. 2, a concurrent session ingested Habermas's *Structural Transformation of the Public Sphere*. Both needed the shared `thinkers/habermas-jurgen.md` page; the concurrent session created it first.
**Skill:** CLAUDE.md ingest workflow (Step 4 concurrent-session Edit-append discipline)
**Type:** internal
**Phase/Area:** Step 4 integration under concurrency

**Issue:** The concurrent session created the thinker page and integrated THIS session's TCA additions, but rendered the concept mentions as **plain text** (de-linked), with an explicit note that "the full concept-page network is the concurrent TCA ingest's responsibility." This avoided broken links during the window when the TCA concept pages did not yet exist. Once this session finished creating those pages, it re-linked the plain-text mentions. Net result: no broken links at any point, no clobbering, clean division of labor — an improvement over blind Edit-append, which would have introduced broken links that the session baseline would then flag.

**Suggested improvement:** Document a "de-link/re-link handoff" convention for concurrent sessions sharing a page: the session that creates a shared page first may reference the *other* session's not-yet-created pages as **plain text (unbracketed)**, leaving a one-line note naming which session owns the eventual links; the owning session converts them to wikilinks once its pages land. Pair with the existing rule that the final `check_wikilinks --compare` against a session-start baseline is what proves no net new breakage.

**Principle:** Under concurrency, a broken wikilink is a temporary coordination artifact, not a defect, IF ownership is explicit — deferring links as plain text until the target exists, then re-linking, keeps every intermediate state valid and avoids both clobbering and phantom-link noise.

### Observation 31: Era names and adjacent-field terms are not pages — don't wikilink them in prose

**Date:** 2026-07-09
**Session context:** Ingesting Swidler's *Talk of Love* into the Social Sciences wiki. On first draft of the new theory/concept/discipline/thinker pages, the wikilink checker flagged ~15 broken links — all of them prose wikilinks to (a) disciplinary-era names (`[[critical-turn]]`, `[[contemporary]]`, `[[classical-era]]`, `[[postwar-expansion]]`) and (b) adjacent-field terms with no page yet (`[[thick-description]]`, `[[interpretive-anthropology]]`, `[[symbolic-anthropology]]`, `[[anthropology]]`, `[[sewell-william-h]]`, `[[bellah-robert]]`). Eras are frontmatter tag values, never pages; the field terms were legitimately uncreated. All had to be converted to plain text.
**Skill:** Social Sciences wiki CLAUDE.md (ingest workflow / naming conventions)
**Type:** internal
**Phase/Area:** Step 4 integration — cross-linking

**Issue:** When writing rich prose, the natural instinct is to wikilink every salient term. In this vault, disciplinary-era names are tags, not pages, and many named concepts/thinkers/subfields do not exist yet. Both produce broken links caught only at validation, requiring a cleanup pass.
**Suggested improvement:** Before/while drafting, keep a "do-not-link" reflex: (1) never wikilink the seven disciplinary-era names — write them as plain text; (2) only wikilink a thinker/concept/method/theory that is in the pre-established Step-1 name set or already on disk; write everything else as plain text (optionally noting it as a future-page candidate). A one-line grep of the new pages' `[[...]]` targets against the vault before running the full validator would catch these in bulk.
**Principle:** In a wiki where eras and periods are frontmatter vocabulary rather than pages, prose links to those vocabulary terms are always broken; disciplined authors link only to the known page-name set and leave everything else as plain text, treating the validator as a backstop, not the first line of defense.

### Observation 32: `check_wikilinks --compare` "0 NEW" counts unique targets, not per-file instances — read the BROKEN lines too

**Date:** 2026-07-09
**Session context:** Same *Talk of Love* ingest. After first integration, `check_wikilinks.py --compare` printed a list of BROKEN links located in my brand-new files, yet the summary read "0 NEW broken link(s)". The reconciliation: the broken *targets* (e.g. `[[critical-turn]]`, `[[thick-description]]`) were already broken elsewhere in the vault at baseline, so as unique targets they were not "new" — even though my new files added fresh *instances* of them.
**Skill:** Social Sciences wiki CLAUDE.md (Step 5 validation)
**Type:** internal
**Phase/Area:** Step 5 — lint/validate; "0 new broken links" gate

**Issue:** Relying on the "0 NEW" summary line alone would have left real broken links in the newly created pages, because the comparator dedupes by target slug. The signal that mattered was the per-file BROKEN listing, which showed the new pages by name.
**Suggested improvement:** Treat "0 NEW broken links" as necessary but not sufficient. Always scan the BROKEN output for the paths of the pages this session created/edited and fix any that appear, regardless of whether the target was already broken elsewhere. The CLAUDE.md validation guidance could note that the compare summary counts unique targets.
**Principle:** A diff/summary that dedupes by target can report "no new problems" while a freshly authored file still contains broken references to an already-broken target; verify against the files you touched, not only against the aggregate count.

### Observation 33: Six-agent Burt batch completed with full coverage; well-trodden area handled single-stage

**Date:** 2026-07-09
**Session context:** Ingest of Burt, *Structural Holes* (1992), ~117k words / 313pp, into the Social Sciences wiki via deployed-subagent strategy.
**Skill:** Social Sciences wiki CLAUDE.md (deployed-subagent ingest workflow)
**Type:** internal
**Phase/Area:** Step 3 (spawn/inventory) + Two-stage variant guidance

**Issue:** 6 Sonnet extractors over disjoint body ranges (Intro+Ch1 / Ch2 / Ch3 / Ch4 / Ch5–6 / Ch7) all returned non-empty claims files with self-reported full coverage of their slices; filesystem inventory confirmed all 6 present before integration; no silent dropouts, no content-filter blocks. This is a fourth clean multi-agent run (cf. Obs 11 Dahrendorf-8, Obs 17 Lipset-7, Obs 24 concurrent-3). Separately: the source hit a "well-trodden area" (existing Granovetter/Coleman/social-capital/network-analysis coverage) whose CLAUDE.md guidance suggests a two-stage (extract-then-integrate-by-page) variant to avoid collisions — but because this was a single non-concurrent session, single-stage main-thread integration was collision-free and simpler. The two-stage variant's trigger is really *concurrency*, not *well-troddenness* per se.

**Suggested improvement:** Consider clarifying in the "Two-stage variant for well-trodden sources" note that the variant earns its cost mainly when (a) the area is well-trodden AND (b) integration agents would run concurrently or a parallel session may touch the same pages; a solo main-thread integration of a well-trodden source does not need it.

**Principle:** Partition-by-page integration exists to prevent write collisions; when there is a single writer (main thread, no concurrent session), range-partitioned extraction + serial main-thread integration is already collision-free regardless of how many existing pages get updated. Match the mechanism to the actual collision risk, not to a proxy for it.

### Observation 34: Grep-verify a planned concept page's term against the source before creating it

**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingesting Bonilla-Silva *Racism without Racists* (5th ed.). Step-1 scaffolding pre-named a `concepts/racial-grammar.md` page (Bonilla-Silva is associated with "racial grammar" from his other work). Extractors flagged the exact term never appears in this book; a full-text grep confirmed zero occurrences. The page was dropped to avoid importing outside knowledge, and stray `[[racial-grammar]]` links were cleaned from three scaffolded pages.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md — Step 1 scaffolding / no-outside-knowledge principle)
**Type:** internal
**Phase/Area:** Step 1 scaffold (pre-establishing linkable page names)

**Issue:** A scholar's signature concept (well-known from their broader corpus) was pre-scaffolded as a page name before confirming the term is actually present in the *ingested* source. Had extractors not flagged it, the page could have been created and filled with recalled (not source-grounded) content.
**Suggested improvement:** In Step 1, before committing a pre-named concept/theory page that rests on a specific coined term, grep the converted source text for that term. If it is absent, either drop the page or route its content into an adjacent page that IS grounded in the source — never create a term-page the source doesn't support.
**Principle:** Pre-scaffolding sets linkable names from prior knowledge of the author; that knowledge can outrun the specific source. A cheap grep against the source text keeps scaffolding honest and prevents outside-knowledge contamination — the same discipline the wiki enforces on subagents ("no outside knowledge") should apply to the main thread's scaffolding.

### Observation 35: Subagents must not run task-observer
**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingest of Fenstermaker & West *Doing Gender, Doing Difference* — parallel extractors
**Skill:** task-observer (one-skill-to-rule-them-all); Social Sciences Wiki CLAUDE.md Task-Observer Activation
**Type:** internal
**Phase/Area:** Session-start / subagent prompts

**Issue:** User corrected mid-ingest: only the main agent should invoke the task-observer skill. Subagents that inherit CLAUDE.md's "invoke task-observer at start of any task-oriented session" instruction may waste time on observation-log protocol, weekly-review checks, and skill loading instead of bulk extraction. Extraction subagents are scoped workers (read cache slice → write claims file); meta-skill monitoring belongs on the orchestrating main thread.

**Suggested improvement:** (1) In CLAUDE.md Task-Observer Activation, scope the mandate to the main/orchestrating agent only — e.g. "Main agent only: at the start of any task-oriented session, invoke task-observer… Subagents and extractors skip task-observer unless the user explicitly asks them to improve a skill." (2) Standing line in every ingest extractor prompt: "Do not load or run task-observer / skill-observation protocols; main agent owns that."

**Principle:** Session-level meta-skills (observation logging, weekly review, skill hygiene) are orchestrator responsibilities. Scoped subagents should receive an explicit negative instruction when project CLAUDE.md would otherwise trigger expensive session-start rituals on every child.

### Observation 36: Scaffold link-target pages only from source-confirmed entities, not the author's wider oeuvre

**Date:** 2026-07-09
**Session context:** Ingesting R. W. Connell's *Masculinities* (Social Sciences Wiki, deployed-subagent strategy). During Step-1 scaffolding I pre-created a stub for `concepts/emphasized-femininity.md` because I knew from general knowledge that "emphasized femininity" is a core Connell concept. All three extractors then reported the term appears *nowhere* in this book — it belongs to Connell's earlier *Gender and Power* (1987). The stub had to be deleted and replaced with `body-reflexive-practice` (a concept actually defined in this source and flagged by the extractor).
**Skill:** Social Sciences Wiki CLAUDE.md — Ingest Workflow Step 1 (scaffold)
**Type:** internal
**Phase/Area:** Scaffold-first / pre-spawn duplicate-and-name pre-scan

**Issue:** The ingest workflow warns that TOC-derived *chunk briefs* are expectations to verify, but it does not explicitly warn against scaffolding **page stubs** for concepts drawn from the agent's prior knowledge of an author's whole body of work. A canonical concept for a thinker may live in a *different* book than the one being ingested; creating its stub during scaffolding manufactures a page the source cannot ground, risking either a broken link (if deleted late) or, worse, an unsourced page written from memory.

**Suggested improvement:** Add a line to Step 1 scaffolding: "Scaffold link-target pages only for entities confirmed present in *this source* (via TOC, intro, or a targeted grep of the raw text), not from general knowledge of the author's oeuvre. A concept strongly associated with a thinker may belong to a different work — grep the raw text for the term before creating its stub." A 5-second `grep -i "term" raw.txt` at scaffold time would have caught this.

**Principle:** In source-grounded knowledge bases, every page must be earned by the source in hand. Prior knowledge should guide *where to look*, never *what to assert or create* — verify presence in the actual text before committing a page to disk.

### Observation 37: Edit-appends to a substantive content page another session is actively authoring get clobbered; add only minimal stubs

**Status:** ACTIONED — Applied to CLAUDE.md Step 4 concurrency guidance (2026-07-09)
**Date:** 2026-07-09
**Session context:** Ingesting Ragin *The Comparative Method* (1987) concurrently with a Lieberson *Making It Count* session. Both needed content on the shared new page `debates/qualitative-quantitative-divide-debate.md`.
**Skill:** CLAUDE.md ingest workflow (Step 4 concurrency guidance) — relates to [[Observation 20]], [[Observation 24]], [[Observation 30]].
**Type:** internal
**Phase/Area:** Step 4 integration under concurrent sessions.

**Issue:** The Lieberson session *created* the debate page (referencing my not-yet-existing source). Following the "Edit-append, never full Write on shared pages" rule, I invested in rich multi-paragraph Edit-appends filling the case-oriented and synthesis positions. Minutes later the other session did a full rewrite (Write) of the page that clobbered all my appends. The outcome was fine only because their rewrite happened to integrate my pages coherently (it linked QCA, multiple-conjunctural-causation, case-oriented-vs-variable-oriented, ragin-charles). The existing rule protects the *appending* session's additions on bookkeeping files (index, log), but does NOT protect substantive prose appended to a *content* page the other session considers its own to author — that session's next Write wins.

**Suggested improvement:** Add a clause to the concurrency guidance: when a *content* page (not a bookkeeping file) was created by another live session, the non-creating session should add only minimal cross-link stubs / a single attributed paragraph, and let the creating session own the body — rather than investing in rich Edit-appends that a full Write will clobber. If richer content is needed, leave it on the owned pages (method/concept/source) that link *to* the shared page, where it is safe. Reserve rich Edit-append for pages neither session claims ownership of.

**Principle:** "Edit-append not Write" prevents *accidental* clobbering of additive bookkeeping, but it does not arbitrate *authorship* of a shared content page. When two sessions both want to author the same new page, ownership goes to the creator; the other contributes stubs and keeps its depth on pages it owns. Effort spent appending prose to someone else's actively-authored page is effort at risk.

### Observation 38: Image-only DuXiu PDFs need parallel tesseract pipeline (ocrmypdf can fail)

**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingest of Tavory & Timmermans *Abductive Analysis* (2014) — DuXiu/Anna's Archive image-only PDF, 179 pages, no text layer
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Source-Type / intake; PDF OCR path)
**Type:** internal
**Phase/Area:** Step 1 word-count intake / source text recovery

**Issue:** `pdftotext` returned only ~75 words (Anna's Archive wrapper). `ocrmypdf --skip-text` failed with SubprocessOutputError (tesseract "lots of diacritics" warnings; no output PDF). Working path: `pdftoppm -png -r 180` then `xargs -P 8 tesseract` per page, concatenate by page order → ~71k words (~28 min OCR). Session spent most wall-clock on OCR before any wiki writing.

**Suggested improvement:** In CLAUDE.md ingest Step 1 (or a methods note under scripts/README), document recovery for image-only social-science PDFs: (1) detect empty pdftotext; (2) prefer parallel pdftoppm+tesseract over ocrmypdf when ocrmypdf fails; (3) cache OCR text to `/tmp/*_cache/full.txt` and file as `raw/.../author-title-year.txt` after ingest; (4) budget 15–40 min for ~150–200 page DuXiu scans at 180 dpi.

**Principle:** Source intake is not complete when a PDF exists on disk — only when body text of expected length is recoverable. Image-only library scans are a first-class failure mode for ebook collections and need a documented, parallelizable OCR fallback, not ad-hoc rediscovery each ingest.

### Observation 39: Scanned-image-PDF sources need an OCR intake path, and naive parallel tesseract oversubscribes cores

**Date:** 2026-07-09
**Session context:** Ingesting Sewell, *Logics of History* (2005) — the raw/ file was a 422-page scanned image PDF (producer "FreePic2Pdf") with NO embedded text layer, so `pdftotext` returned 0 words.
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md, Step 1 word-count intake)
**Type:** internal
**Phase/Area:** Step 1 — source intake / word-count check

**Issue:** The CLAUDE.md intake protocol assumes a text or text-bearing PDF/epub and jumps to `wc -w`. It has no branch for image-only scans, which are common in this collection (z-library rips). Two failure modes surfaced: (1) `pdftotext`/`pdftotext -layout` silently produced an empty file — a word-count intake of 0 that could be misread as "conversion failed" rather than "no text layer, needs OCR"; (2) the first OCR attempt (`ocrmypdf` on the original, then `xargs -P12 tesseract`) drove load average to ~56 on a 12-core box and crawled at ~0.1 pages/sec, because tesseract spawns multiple OpenMP threads per process, so 12 processes × N threads massively oversubscribed the cores. Fix that worked: render pages with `pdftoppm -r 100 -png` (down-sampling the ~282-megapixel embedded scans to ~17MP), then `OMP_THREAD_LIMIT=1` on each tesseract with `xargs -P<cores>` — single-threaded-per-process parallelism fit the core count and ran at ~1.8 pages/sec. Spot-checking one rendered page's OCR quality BEFORE the full batch confirmed 100 dpi was legible.

**Suggested improvement:** Add an image-PDF branch to the Step-1 intake in CLAUDE.md: after locating the source, if `pdftotext` yields ~0 words (or `pdfinfo` shows an image producer / no text), route to an OCR intake — `pdftoppm -r 100 -png` then `OMP_THREAD_LIMIT=1 tesseract` under `xargs -P(nproc-2)`, concatenating page text with page markers, then run the normal word-count intake on the OCR output. Note the OCR provenance and expected-artifact caveat in the source page's `reliability_notes` (done here). Always spot-check one page's OCR before batching, and always set `OMP_THREAD_LIMIT=1` when parallelizing tesseract.

**Principle:** When an ingest pipeline assumes machine-readable input, add an explicit detection-and-recovery branch for the input class it silently fails on (here, image-only scans) rather than treating a zero-length conversion as an error. And when fanning out a CPU-bound tool across cores, check whether the tool is already internally multithreaded — pin it to one thread per process before multiplying processes, or the fan-out thrashes instead of scaling.

### Observation 40: Nine-agent Golden Bough batch completed 9/9 without dropout
**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingest of Frazer *The Golden Bough* (1922 abridgement) — ~410k body words, 9 parallel extractors over disjoint cache ranges under `/tmp/golden_bough_cache/`
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor/inventory

**Issue:** Prior observations (3, 5, 12) documented silent per-range dropout on multi-agent batches. This run used **9 agents** over ~27.5k body lines (~410k words) with expected claims paths `claims/range_1.md`…`range_9.md`. **All 9** wrote complete non-empty claims files (~504 claims total) within ~2–2.5 minutes; no main-thread recovery needed. Short multi-wait + filesystem inventory used as completion signal. User-visible checklist posted before spawn.

**Suggested improvement:** Retain as positive counter-case to Obs 12 (Blumer dropout): large-N + large-book success is possible when ranges are sized ~2.2k–4.2k lines, cache slices cut before spawn, and completion is filesystem-based. Do not treat as "fixed forever" — continue mandatory inventory before integration.

**Principle:** Stochastic silent-agent death is real; full-batch success at N=9 on a large theoretical work shows the failure is not automatic at high N or long slices, but inventory-before-integration remains non-optional regardless of success rate.

### Observation 41: Step-4 artifact grep misses extractor claim-IDs and hedges

**Date:** 2026-07-09
**Session context:** Post-ingest audit of Maine, *Ancient Law* (1861). Found two subagent artifacts surviving into live pages: an extractor claim-ID citation ("R1-017") in the thinker page's prose genealogy, and a "(if present)" editorial hedge plus bare "index/log/Structural_Sources" in the source page's Pages Updated list.
**Skill:** CLAUDE.md Ingest Workflow — Step 4 (Review and tie together)
**Type:** internal
**Phase/Area:** Step 4 artifact-removal grep

**Issue:** Step 4 already instructs "remove agent artifacts (stray instructions, prompt echoes, `</content>`-style tags — grep first)", but the enumerated patterns miss two recurring leak classes: (1) internal claim-ID references (e.g. `R1-017`, `R2-004`) that extractors cite to ground claims and that get copied verbatim into prose; (2) provisional hedges like "(if present)" left in when the main thread wasn't sure a page existed at integration time. Validators pass clean on both — they are not broken links or schema errors — so only a reading pass catches them.

**Suggested improvement:** Extend the Step 4 grep pattern list to include claim-ID citations (`R[0-9]-[0-9]{3}` / `range_[0-9]` outside the source page's own Claims-Extracted bookkeeping section) and provisional hedges ("(if present)", "(if exists)", "(verify)"). Add these to the standing artifact-grep so the check is mechanical, not memory-dependent.

**Principle:** Artifact-removal checklists must enumerate the actual leak classes observed, not a generic "stray tags" instruction. Leaks that pass all validators (well-formed prose, valid links) are invisible to automated checks and only caught by an explicit grep — so the grep pattern set is the real enforcement surface and should grow each time a new leak class is found.

### Observation 42: Three-agent Sapir *Language* batch completed 3/3 without dropout; grep-verify killed two anachronistic concept pages

**Date:** 2026-07-09
**Session context:** Deployed-subagent ingest of Sapir, *Language: An Introduction to the Study of Speech* (1921) — 3 Sonnet agents by chapter (I–IV / V–VI / VII–XI).
**Skill:** CLAUDE.md ingest workflow (deployed-subagent method)
**Type:** internal
**Phase/Area:** Step 3 (extraction) + Step 1 (concept pre-scan / grep-verify)

**Issue:** All 3 background extractors wrote complete, non-empty claims files with full line-range coverage and no silent dropout (continuing the clean-batch pattern of Obs 11/17/40 at N=3). Separately, the Obs-34 grep-verify caught two would-be anachronisms before any page was created: "phoneme"/"phonemic" = 0 hits in the 1921 text (→ page named `phonetic-pattern`, Sapir's own term, not `phoneme`) and "typolog" = 0 hits (→ `linguistic-typology` created but the *term* attributed to later usage, not to Sapir). A concurrent session (Rivers/Melanesian diffusionism) was active throughout; its in-flight broken links appeared in the vault-wide compare but none in this session's pages, and Edit-append on shared bookkeeping held.

**Suggested improvement:** No change needed — confirms the deployed-subagent method and the grep-verify-before-create rule (Obs 34) are working. Countable record: batch sizes N=3,7,8,9 now all clean.

**Principle:** Grep-verifying a planned concept page's term against the actual source text is highest-value for older texts, where the modern name for a concept (phoneme, typology) routinely postdates the author's own vocabulary; the check prevents anachronistic wiki-voice attribution at essentially zero cost.

### Observation 43: Hub pages created at summary depth are silently counted as complete during ingest

**Date:** 2026-07-09
**Session context:** User asked to "ingest Argonauts of the Western Pacific"; it was already ingested earlier the same day. On challenge, verification showed both warranted hub pages (Studies + Thinkers) existed but were ~1,380 and ~852 words — far below the locked hub floors (3,500–5,500 and 4,000–5,000). User then asked to build both to standard.
**Skill:** New skill candidate: none — this targets the CLAUDE.md ingest workflow (project-internal), specifically hub-build enforcement.
**Type:** internal
**Phase/Area:** Ingest Workflow Step 1 ("A warranted hub page is part of the ingest, not a follow-up") + Studies/Thinkers/Theory Hub analysis standards.

**Issue:** The prior ingest created the hub pages, linked them reciprocally, and counted them in the "Pages created: 11" tally — so every mechanical check (page exists, reciprocal link present, validators pass) reported success. But the hubs were written at summary resolution, missing the mandatory word floor, verbatim-passage analysis, and full tables. A hub that exists but is 20–35% of the required length passes all automated gates while silently violating the locked standard. Nothing in the validators checks hub word count or section depth, so the defect was invisible until the user's instinct ("You're sure it was ingested?") prompted a manual word-count audit.

**Suggested improvement:** Add a hub-completeness gate to the ingest checklist: when a hub page is created, verify `wc -w` meets the page-type floor (studies ≥3,500; thinkers ≥4,000; theory ≥3,500) AND that it contains the required verbatim-quote analysis and canonical tables, before counting it as "created." Consider a lightweight validator check (`lint_wiki.py`) that flags any `tags: [hub, *-analysis]` page under the floor as a WARNING. Treat "hub exists but under floor" as equivalent to "required body section missing," not as done.

**Principle:** Existence and link-reciprocity are cheap to verify and therefore get verified; depth-to-standard is expensive to verify and therefore gets skipped. When a standard specifies a quantitative floor (word count) or qualitative depth (verbatim analysis), completion must be gated on that floor, not on the artifact merely existing. Automated link/schema checks create false confidence precisely because they pass on under-built pages.

### Observation 44: Concurrent ingest of two books by one author — partition by page-ownership (cases/concepts vs. shared thinker/theory) makes it collision-safe

**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Ingesting Benedict *Patterns of Culture* (1934) while a second live session ingested Benedict *The Chrysanthemum and the Sword* (1946). Both books feed the same thinker page (`benedict-ruth`) and the same theory (`configurationism`).
**Skill:** Social Sciences Wiki CLAUDE.md — Ingest Step 4 (concurrent-session integration) / Observation 6
**Type:** internal
**Phase/Area:** Integration under concurrency

**Issue:** The collision was benign and productive, not destructive. The other session had *pre-linked* pages I had not yet created (`[[dobu]]`, `[[zuni]]`, `[[configurationism]]`, `[[cultural-relativity-of-normality]]`) and, when it re-authored `benedict-ruth`, *folded in* my Patterns scaffold content (sources_ingested went to 2, both books covered) rather than clobbering it. I detected the overlap early via the harness "file was modified" notes and switched from full Writes to Edit-append on every shared page (thinker, theory summary, culture-and-personality, cultural-relativism, anthropology), reserving full Writes for pages only I created (the three society pages, four concept pages, source, study, Theory Hub). Final validation: 0 new broken links, 0 errors.

**Suggested improvement:** Add to CLAUDE.md's concurrent-ingest guidance a positive pattern: when two sessions ingest different works by the *same* author/subject, the natural safe partition is **case/subject-matter + concept pages to one session, shared thinker/theory pages authored by whichever session created them, cross-linked by the other via Edit-append**. The early-warning signal is the harness "file modified by user/linter" note on a page you thought you owned — treat it as the trigger to stop full-Writing that page. Reciprocally, a session that *creates* a shared thinker/theory page should fold in (not overwrite) any scaffold content a peer session already wrote.

**Principle:** Concurrency is safe when authorship is partitioned by page, not by source-range. The "file modified" harness note is the cheapest available collision detector — react to it by demoting full Writes to Edit-append on that page. Two ingests of one author converge cleanly if each owns a disjoint page-set and only cross-links into the other's.

### Observation 45: Concurrent ingest left content done but bookkeeping incomplete
**Status:** OPEN
**Date:** 2026-07-09
**Session context:** User asked to ingest Radcliffe-Brown *Structure and Function*; concurrent session had already written source + concepts + hub densification but left log/index/Structural_Sources/filing unfinished and Primitive Law underextracted.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Ingest Workflow Step 6 Bookkeeping)
**Type:** internal
**Phase/Area:** Step 6 bookkeeping; multi-session / concurrent-session handoff

**Issue:** A concurrent (or prior same-day) session completed the hard part of a theoretical ingest — source page with Section Plan, 4 concept pages, Thinkers/Theory Hub densification — but did **not** complete Step 6: no `wiki/log.md` entry, no `index.md` block, no `Structural_Sources.md` ✅ row, PDF still in `raw/` root, no permanent `.txt` filing. One claims range (Primitive Law) was also flagged by extractors as outside brief and never main-thread recovered. The user request "ingest X" therefore hit an ambiguous mid-state: content looked ingested, apparatus said otherwise.

**Suggested improvement:** In CLAUDE.md Step 6 (or session-start for "ingest X"), add a **resume-incomplete-ingest checklist**: if `wiki/sources/[slug].md` exists with `ingested:` date but (a) no matching log line, or (b) source still in `raw/` root, or (c) not marked in Structural_Sources — treat as incomplete and finish bookkeeping before re-extracting. Also: never close an ingest session without the four-item bookkeeping set (log + index + Structural_Sources + file out of raw root), even if content pages are done.

**Principle:** Ingest completion is an apparatus fact (log/index/sources-list/filing), not only a content fact (pages exist). Concurrent sessions that write content without bookkeeping leave the next agent (and the user) unable to tell "done" from "half-done" without a full inventory.

### Observation 46: A source page's existence does not guarantee the source supports what downstream pages attribute to it

**Date:** 2026-07-09
**Session context:** Rebuilding the `world-systems-analysis` theory hub to standard. A `sources/wallerstein-modern-world-system-longue-duree-2004` page existed and the hub cited it, so the source looked ingested and usable. On mining the raw text for verbatim passages, it turned out to be an EDITED multi-author conference volume (Braudel Center 25th anniversary) — only two short reflective pieces are actually Wallerstein's; the core world-systems theory (world-economy typology, core/periphery/semiperiphery, the long-16th-century origin) is simply not in it. The hub could not be brought to standard without padding from outside knowledge, so it was deferred and flagged rather than faked.
**Skill:** Project ingest workflow (CLAUDE.md) — source-page integrity.
**Type:** internal
**Phase/Area:** Ingest Workflow Step 1 (scaffold/verify source) and Source-Type Handling.

**Issue:** Downstream pages (a theory hub, a theory summary) had been built citing this source as if it were a Wallerstein monograph. Nobody had recorded that the volume is multi-authored and thin on the core theory. The defect is invisible from the wiki side — the source page exists, the links resolve, the hub reads plausibly — and only surfaced when someone actually opened the raw text to quote it. A reader trusting the wiki would take world-systems core claims as sourced to Wallerstein when they are not.

**Suggested improvement:** At ingest, the source page should record (a) whether the work is single- or multi-authored and, for edited volumes, WHICH pieces are by the named author, and (b) what the source does and does NOT cover relative to the claims the wiki will attribute to it. Add a lint/heuristic: when a `theories/` or hub page attributes core doctrine to a named thinker via a `sources/` page whose `source_type` is `reference`/`edited`/`mixed` or whose author list is long, flag for a coverage check. More generally: before building a high-resolution page on a source, spot-open the raw text to confirm it contains the load-bearing material — do not infer contents from the title or a pre-existing source page.

**Principle:** "A source page exists" and "the source supports the claim" are different facts, and the gap between them is invisible to every automated check that operates on the wiki alone (links resolve, schema passes). Integrity of attribution can only be verified against the source text itself. Treat a pre-existing source page as a pointer to be re-verified at the raw text, not as a warranty of coverage — especially for edited/multi-author/reference volumes, where the named "author" may not have written the relevant part.

### Observation 47: Edit-append does NOT protect shared bookkeeping files against a concurrent full-Write

**Date:** 2026-07-09
**Session context:** Ingesting *The Nuer* (Evans-Pritchard 1940) while a concurrent session ingested *African Political Systems*. Both touched `Structural_Sources.md`.
**Skill:** Social Sciences Wiki CLAUDE.md (ingest workflow — concurrency guidance)
**Type:** internal
**Phase/Area:** Step 4 / Step 6 integration under concurrent sessions

**Issue:** CLAUDE.md states "Edit-append protects additive *bookkeeping* (index, log, `Structural_Sources`, coverage map), but it does NOT arbitrate authorship of a shared *content* page." In practice, my Edit-append additions to `Structural_Sources.md` (a bookkeeping file) were silently clobbered by the concurrent session's full **Write** of that same file — the exact failure the guidance implies is confined to content pages. Edit-append only protects a file if *every* writer also uses Edit-append; one full Write wins regardless of file category. I recovered by re-inserting with a single atomic `perl -i` pass (read+write in one shell call, not Read-tool→Edit), which is race-robust for append-only bookkeeping; a naive retry created duplicates I then had to de-dupe.

**Suggested improvement:** Amend the concurrency section: the bookkeeping-vs-content distinction is about *authorship arbitration*, not *clobber-safety*. For append-only bookkeeping files that a concurrent session may full-Write (index, log, Structural_Sources, overview), prefer a single-shot atomic insert (`perl -i`/`awk` in one Bash call keyed to a stable anchor line) over Read-tool→Edit, and re-verify presence + de-dupe after, since the other session may have rewritten between your read and write.

**Principle:** Under concurrent writers, the safe pattern for shared append-only state is check-insert-verify in one atomic operation keyed to content, not line numbers — and never assume a file category ("bookkeeping") confers clobber-safety when any writer may issue a full overwrite.

### Observation 48: Read-cap shortfall in one agent leaves a gap the adjacent agent does not backfill

**Date:** 2026-07-09
**Session context:** Dual ingest of Turner *The Forest of Symbols* + *The Ritual Process*. FoS range C (assigned lines 4796–8200) hit a read cap at ~7446 and reported the shortfall; range D began at 8200, so FoS 7446–8200 (Mukanda *nfunda*-preparation material) was covered by neither agent.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Deployed Subagent Strategy, Step 3 completion / recovery)
**Type:** internal
**Phase/Area:** Step 3 filesystem-inventory + gap recovery

**Issue:** The standing "Report actual coverage" instruction worked exactly as designed — range C explicitly stated it stopped at ~line 2650 of its slice — but the main thread must act on that report. Because adjacent agent D's disjoint slice started at C's *assigned* upper boundary (8200), D did not and could not backfill C's shortfall (7446–8200). The gap is invisible to a pure "all N claims files present and non-empty" inventory, which passed. Main-thread recovery (reading the 754-line cache slice directly and folding it into the Ndembu/concept pages at full fidelity) closed it.

**Suggested improvement:** Add to the Step 3 inventory checklist an explicit sub-check: for each agent, compare its *reported actual coverage* against its *assigned* line-range, not just file presence/non-emptiness. Any agent that reports stopping short of its assigned upper bound created a gap between it and the next agent's start — recover that specific span on the main thread (or with a scoped gap-fill agent). "All claims files present" is necessary but not sufficient; "all assigned lines actually covered" is the real completion criterion.

**Principle:** Disjoint line-range partitioning guarantees no *overlap*, not full *coverage*: a read-cap shortfall in one agent opens a gap the next agent's fixed start boundary cannot absorb. Completion must be measured as assigned-lines-covered, not claims-files-present.

### Observation 49: A generic concept slug already occupied by one author's treatment forces later primary sources to graft or fork

**Date:** 2026-07-09
**Session context:** Ingesting Sahlins *Stone Age Economics*; the reciprocity/trade pages needed to link a generic "economic exchange" concept, but `concepts/exchange.md` is titled "Exchange (Simmel)" and occupies the bare `exchange` slug with Simmel-specific content.
**Skill:** Social Sciences Wiki CLAUDE.md (ingest workflow / naming conventions)
**Type:** internal
**Phase/Area:** Step 1 scaffolding / duplicate pre-scan / naming conventions

**Issue:** The bare, generic slug `exchange` was already claimed by a single thinker's version of the concept (Simmel). When a later primary source (Sahlins on primitive trade/exchange value) needed a home for generic-exchange content, the options were (a) graft an attributed subsection onto the author-specific page, or (b) fork a new slug (`exchange-value`/`primitive-trade`). I chose (a) since the Simmel page's Applications section explicitly invited anthropology-of-exchange cross-links, but the fit is imperfect and the page's title/scope now understates its content. This is the same pattern as `generalized-reciprocity` being scaffolded from Putnam's civic use before its primary anthropological source arrived.

**Suggested improvement:** During the duplicate pre-scan (Step 1), when a planned link target is a *generic* concept slug, check whether the existing page is actually an *author-specific* treatment squatting the generic slug. If so, decide up front: either (i) retitle/rescope the existing page to be genuinely generic with per-author sections, or (ii) reserve the bare slug for the generic concept and move the author-specific version to a qualified slug. Add "generic-slug-squatted-by-one-author" to the pre-scan heuristics alongside name-order and same-entity-across-folders checks.

**Principle:** In a multi-source wiki, the first source to touch a concept tends to define its page's scope and title; a bare generic slug filled by one author's version creates friction for every later primary source. Naming the *generic* concept generically (with attributed per-author sections) keeps the slug reusable, which is exactly what the wiki's "constructs are dated / many traditions measure it differently" principle wants.

### Observation 50: Duplicate-slug pre-scan must sweep ALL folders, not just the target folder

**Date:** 2026-07-09
**Session context:** Ingesting *Man the Hunter* (Lee & DeVore 1968) into the Social Sciences wiki via the deployed-subagent strategy, concurrently with two other live ingest sessions (*The Forest People*, *Rise of Anthropological Theory*).
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md) — Step 1 duplicate-page pre-scan
**Type:** internal
**Phase/Area:** Ingest Workflow Step 1 (duplicate-page pre-scan) and Step 5 (validation)

**Issue:** During the pre-scan I checked `methods/` for an "ethnographic-analogy"/"analogy" slug (returned MISSING) but did not check `concepts/` for the same slug — I only grepped `concepts/` for unrelated terms. A `concepts/ethnographic-analogy.md` already existed (from a prior/concurrent Morgan–Tylor ingest). I created `methods/ethnographic-analogy.md`, producing a duplicate-slug ERROR (bare `[[ethnographic-analogy]]` ambiguous across concepts/methods) caught only at final validation. Fix required deleting the new methods page, folding its content into the existing concept page, and repointing all links.

**Suggested improvement:** In the duplicate-page pre-scan, grep the *entire* `wiki/` tree for each candidate slug stem (e.g. `find wiki -name '<slug>.md'` or `grep -rl` across all page folders), not just the folder the new page will live in. A concept can pre-exist under a different page-type than the one the ingest expects (analogy as concept vs. method; a school as theory vs. discipline). The lint duplicate-slug check catches it, but only after pages and links are written.

**Principle:** Vault-unique slugs mean a name collision can occur across *any* two folders, so a folder-scoped existence check gives false confidence. Pre-scans that enforce a global uniqueness invariant must query the global namespace, not a local partition of it — otherwise the check silently misses exactly the cross-folder collisions the invariant exists to prevent.

### Observation 51: Scanned image-PDF ingests need a standard OCR recovery path in the word-count intake step

**Date:** 2026-07-09
**Session context:** Ingesting Geertz, *Local Knowledge* (1983) — the source PDF was a 126-page scanned image with no text layer; `pdftotext` returned 0 words. Recovered via `ocrmypdf --force-ocr` + `pdftotext` (~103k words). The Sewell *Logics of History* ingest (same day, per log.md) hit the identical problem and recovered via `pdftoppm@100dpi` + parallel `tesseract`.
**Skill:** Project workflow (CLAUDE.md "Ingest Workflow — Step 1 word-count intake"); not a packaged skill.
**Type:** internal
**Phase/Area:** Step 1 scaffolding — word-count intake check.

**Issue:** CLAUDE.md's Step-1 intake assumes a text layer exists (`wc -w` the raw text vs. expected length). For scanned image PDFs the extraction silently yields ~0 words, which reads like an empty/failed source rather than a format problem. Two ingests in one day hit this and each improvised a different OCR recovery (ocrmypdf vs pdftoppm+tesseract). The recovery adds several minutes of wall-clock that must run before slicing/scaffolding can proceed.

**Suggested improvement:** Add an explicit branch to the Step-1 intake: "If `wc -w` on the extracted text is near-zero or far below the page-count expectation, the PDF is likely scanned/image-only — run OCR before proceeding (`ocrmypdf --force-ocr <in> <out>` then `pdftotext -layout`, or `pdftoppm` + `tesseract` for stubborn files). Kick OCR off in the background early (right after locating the source) so it overlaps scaffolding/pre-reading." Note that OCR running-heads/marginalia garble heavily but body prose survives — flag this in `reliability_notes` and instruct extractors to read through it.

**Principle:** Intake validation should distinguish *format failure* (no text layer) from *content failure* (truncated/empty source); the two look identical to a word count but need opposite responses. Building the recovery path into the checklist prevents each session from re-improvising it and prevents a silent zero-word read from being misdiagnosed as a missing source.

### Observation 52: Word-count intake misses a missing contiguous middle section; page-marker gap-scan catches it

**Date:** 2026-07-09
**Session context:** Two-book Sahlins ingest (*Culture and Practical Reason* + *Islands of History*) via the deployed-subagent strategy.
**Skill:** CLAUDE.md Ingest Workflow (Step 1 word-count intake / Step 3 coverage reporting) — social-sciences-wiki ingest process.
**Type:** internal
**Phase/Area:** Scaffold-first word-count intake check; subagent coverage verification.

**Issue:** The *Culture and Practical Reason* PDF (89-page 2-up scan) was silently missing book pages ~126–203 — the entire bodies of Ch.3 and Ch.4. The mandatory `wc -w` intake check did NOT flag it: the surviving text (Chs. 1, 2, 5 + references) was dense enough to total ~69k words, a plausible length for the whole ~240-page book, so the ratio looked fine. What actually caught the gap was a subagent reporting that its assigned line-range didn't contain the chapter its brief described (a chapter-content mismatch), which prompted a page-marker scan: `grep -nxE` for standalone book-page-number markers found ZERO markers for pp.126–203, and reading the boundary showed the text jumping straight from the end of Ch.2 (p.125) to Ch.5 (p.204). A `-layout` re-extraction confirmed the gap was in the source PDF, not the extraction.

**Suggested improvement:** Add to the Step-1 intake check (and note in Step 3): word-count ratio alone cannot detect a *missing contiguous interior section* when surviving text is dense. When the TOC lists chapters, additionally (a) grep the body for each chapter's opening to confirm all are present, and (b) for paginated scans, scan for monotonic standalone page-number markers and flag any large gap or non-monotonic jump. Treat a subagent's "my range didn't contain the briefed chapter" report as a possible source-incompleteness signal, not just a mis-briefing, and run the page-gap scan before assuming the text is complete.

**Principle:** A single aggregate metric (total word count) can pass a corpus that is locally incomplete; completeness verification needs a *structural* check (every expected unit present, monotonic pagination) in addition to the aggregate. Subagent coverage-mismatch reports are a cheap early-warning signal for silent source corruption.

### Observation 53: `check_wikilinks --compare` can report "0 NEW" while your own new page has a broken link

**Date:** 2026-07-09
**Session context:** Ingest of Comaroff & Comaroff, *Of Revelation and Revolution, Vol. 1*. After integration, `check_wikilinks.py --compare /tmp/scs_links_baseline.json` printed a full BROKEN list that included two genuinely new broken links in freshly-created pages (`colonization-of-consciousness.md :: [[consciousness]]`, `historical-anthropology.md :: [[critical-turn]]`) yet summarized "0 NEW broken link(s)". The targets (`consciousness`, `critical-turn`) were already broken elsewhere in the baseline, so the comparator — keying on the broken-target set rather than on (file,line,target) occurrences — did not count them as new.
**Skill:** Social Sciences Wiki CLAUDE.md — Ingest Workflow Step 5 (Lint and validate) / the "0 new broken links" guidance.
**Type:** internal
**Phase/Area:** Step 5 validation, wikilinks baseline compare.

**Issue:** The workflow leans on "`--compare` reports only NEW broken links" as the completeness signal. But when a new page links to a slug that is *already* broken somewhere in the vault, `--compare` folds it into the existing-broken set and reports 0 new — so a real defect in this session's output passes the gate silently. Here it was caught only because the operator also read the full BROKEN list and noticed the paths were session-created files.

**Suggested improvement:** In Step 5, add: "Do not treat `--compare`'s '0 NEW' as sufficient on its own. Also scan the full BROKEN list for any path this session created/edited, and confirm the absolute broken count did not rise. A new broken link to an already-broken target can read as '0 NEW'." Optionally note that filtering `check_wikilinks.py` output by this session's page slugs is the reliable check.

**Principle:** A diff/baseline comparator that keys on a value-set (broken *targets*) rather than on occurrences (file+line+target) will under-report regressions whenever the new bad value already exists elsewhere. Completeness gates built on set-difference must be paired with an absolute-count check or an own-artifact scan, or they give false all-clears.

### Observation 54: Five-agent Orientalism batch completed 5/5 without dropout

**Date:** 2026-07-09
**Session context:** Social Sciences Wiki ingest of Said *Orientalism* (1978) — 5 parallel extractors over disjoint cache ranges (~16k–36k words each) under `/tmp/orientalism_cache/`; claims expected at `claims/range_1.md`…`range_5.md`.
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors

**Issue:** All 5 background Sonnet extractors returned complete, non-empty claims files (87–108 lines each); filesystem inventory before Step 4 confirmed 5/5 present. Each self-reported exact coverage and correctly flagged expectation mismatches (range 1 noted latent/manifest absent from Intro; range 3 flagged Sacy/Renan/Lane lacking thinker pages). No content-filter block despite the book densely reproducing colonial/racial discourse (Balfour, Cromer, Renan on Semites, Patai) — the range-sizing-for-recovery precaution was not needed this time but remains cheap insurance.

**Suggested improvement:** None required — continues the reliability pattern of Obs 11/17/40. Data point: for a ~136k-body-word dense theoretical work, 5 agents split by chapter/subsection boundaries (not even line counts) worked well; the densest chapter (Ch3, 52k words) split cleanly at an internal subsection header.

**Principle:** Weighting extractor ranges by content boundaries and density (splitting the one oversized chapter at a subsection header) rather than even line counts keeps each agent's slice coherent and recoverable.

### Observation 55: Active source queue lives in "Outstanding sources.md", not "Structural_Sources.md"

**Date:** 2026-07-09
**Session context:** Bookkeeping (Step 6) for the Said *Orientalism* ingest. CLAUDE.md Step 6 and the Collection Coverage Map both name `Structural_Sources.md` as "the sole active list." The actual numbered, ✅-markable ingestion queue is in `Outstanding sources.md` (Said was line item #64 there; grep of `Structural_Sources.md` for the source returned nothing).
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Ingest Workflow Step 6 / Collection Coverage Map)
**Type:** internal
**Phase/Area:** Step 6 bookkeeping — source-queue update

**Issue:** CLAUDE.md instructs updating `Structural_Sources.md` to mark a source ingested, but the live line-item queue with numbered sources and `✅ ingested <date>` marks is maintained in `Outstanding sources.md`. Both files exist (~90k and ~32k). A curator following CLAUDE.md literally would update the wrong (or a stale) file and leave the real queue item unmarked. Recent ingests (Strathern #62) confirm the ✅ convention lives in `Outstanding sources.md`.

**Suggested improvement:** Reconcile CLAUDE.md with reality — either rename references so Step 6/Coverage Map point to `Outstanding sources.md` as the active queue, or clarify the division of labor between the two files. Until reconciled, at Step 6 grep BOTH files for the source and mark whichever holds the numbered line item.

**Principle:** When a workflow's named canonical file diverges from the file the project actually maintains, follow the evidence of recent practice (where the ✅ marks are) and flag the doc drift, rather than trusting the doc's self-description.

### Observation 56: epub intake — pandoc `-t plain` inflates word count via ASCII-art page borders; use ebook-convert

**Date:** 2026-07-09
**Session context:** Ingesting Renato Rosaldo, *Culture and Truth* (epub) into the Social Sciences wiki.
**Skill:** Social Sciences CLAUDE.md — Ingest Workflow, Step 1 word-count intake check
**Type:** internal
**Phase/Area:** Step 1 scaffold / word-count intake

**Issue:** Converting the epub with `pandoc -f epub -t plain` produced a text file whose `wc -w` reported ~257k words for a ~250-page book (expected ~75–80k). The inflation came from pandoc rendering the epub's cover/title pages as ASCII-art tables (`+---+`, `|`, `-- --`), each border glyph counting as a "word." This would have falsely signaled a bloated or corrupt source and could have driven the wrong agent count. Re-converting the same epub with `ebook-convert` (Calibre) gave a clean ~81k words / 11,540 lines with normal prose.

**Suggested improvement:** In the Step 1 intake note for epub sources, prefer `ebook-convert in.epub out.txt` over `pandoc -t plain` for the word-count check; if pandoc must be used, strip table-border lines before `wc -w`, or treat an implausibly high word count on an epub as a converter artifact (spot-check the head) rather than a real length signal.

**Principle:** The word-count intake check assumes the converter emits prose, not layout. Format converters that reproduce page furniture as text can inflate counts several-fold; validate the *character of* the extracted text (spot-read the head), not just its size, before trusting the ratio.

### Observation 57: Scanned image-PDF sources need an OCR intake path (ocrmypdf), not just pdftotext

**Date:** 2026-07-09
**Session context:** Ingesting Rabinow, *Reflections on Fieldwork in Morocco* (1977) — the raw PDF was a scanned image with no embedded text layer.
**Skill:** Social Sciences Wiki CLAUDE.md (ingest workflow, Step 1 word-count intake)
**Type:** internal
**Phase/Area:** Ingest Workflow Step 1 (source intake / word-count check)

**Issue:** `pdftotext` returned 0 words and `pdffonts` showed no embedded fonts — the source was a scanned image-PDF. The CLAUDE.md word-count-intake guidance covers silent epub→txt truncation but not the image-PDF case, which fails differently (0 words, not partial). Recovery: `ocrmypdf --force-ocr --sidecar out.txt in.pdf out.pdf` (tesseract) yielded ~43.4k words on-target. One gotcha: `ocrmypdf --output-type none` conflicts with naming an output PDF file (pydantic ValidationError) — either name a real output PDF or use `-` for stdout.

**Suggested improvement:** Add a line to the Step-1 word-count intake: "If `pdftotext` yields near-zero words, check `pdffonts` — an empty font table means a scanned image-PDF; OCR it (`ocrmypdf --force-ocr --sidecar`) before proceeding, and note the OCR provenance + residual artifacts in `reliability_notes`." Several queued raw/ sources (Taussig, Stocking, Kuper) are also likely scanned.

**Principle:** Source-intake validation must detect *how* a conversion failed, not just *that* text is short — a 0-word result and a half-captured result need different recovery paths (OCR vs. chapter-grep). Encode the diagnostic (`pdffonts` empty → OCR), not just the symptom.

### Observation 58: Duplicate-page pre-scan must be folder-agnostic (concept↔theory collision)

**Date:** 2026-07-09
**Session context:** Ingesting Stocking, *Victorian Anthropology* (1987). Created `concepts/social-darwinism.md`, but `theories/social-darwinism.md` already existed — a duplicate-slug collision caught only at Step-5 lint (lint error + wikilink ambiguity warnings across ~17 pages).
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md, "duplicate-page pre-scan", Step 1)
**Type:** internal
**Phase/Area:** Step 1 duplicate-page pre-scan

**Issue:** The pre-scan guidance lists name-order variants and *specific* cross-folder pairs (school in `theories/` vs `disciplines/`; people in `societies/` vs `cultures/`). It does not state the general rule: before creating ANY new page slug, grep the *entire* `wiki/` for that bare slug regardless of folder. I scanned `concepts/` and `methods/` for my planned concept slugs but not `theories/`, so `social-darwinism` (a plausible concept name that was already a theory page) slipped through. Recovery was cheap here (fold content into the existing page, delete the dup, re-point links resolve automatically) but it cost a lint round-trip and could have clobbered had the existing page been actively authored by a concurrent session.

**Suggested improvement:** In CLAUDE.md's duplicate-page pre-scan, add an explicit first step: "For every new slug the ingest will create, `grep -rl 'slugname' wiki/` (or `ls wiki/*/slug.md`) across ALL page-type folders — Obsidian resolves wikilinks by bare filename, so a slug that is unique within its intended folder can still collide with a page of another type. Especially check the concept↔theory↔method triangle and the discipline↔theory pair." Fold this into the existing name-order/cross-folder bullet as the general principle it is an instance of.

**Principle:** When a namespace is flat (filename-unique across folders), any uniqueness check scoped to one folder is unsound. Duplicate detection must run over the whole namespace, not the subtree you intend to write into.

### Observation 59: Word-count intake should detect zero-text (scanned) PDFs and trigger OCR

**Date:** 2026-07-09
**Session context:** Same ingest. The source PDF (449 pp) had no text layer (JBIG2 scan); `pdftotext` returned 0 words. Ran `ocrmypdf` (tesseract, 12 jobs) to a sidecar `.txt` (~186k words) before proceeding — this worked well and produced clean, usable text.
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md, Step 1 word-count intake)
**Type:** internal
**Phase/Area:** Step 1 "word-count intake check"

**Issue:** The intake step is written for the *converted-ebook-truncation* failure mode (epub→txt capturing only Part One). It does not name the *scanned-PDF* failure mode, where extraction yields ~0 words and the whole ingest is blocked until OCR. The fix (detect near-zero `wc -w`, run `ocrmypdf --sidecar`) is not in the workflow, so an operator could misread an empty extraction as a corrupt/missing file.

**Suggested improvement:** Extend the Step-1 word-count intake to branch on the ratio: (a) badly-low but nonzero → suspect truncation (existing guidance); (b) ~zero words with nonzero page count → scanned/image PDF, run OCR (`ocrmypdf -l eng --jobs N --sidecar out.txt --force-ocr in.pdf -`, or per-page `pdftoppm`+`tesseract`), then re-run the intake against the OCR output. Note OCR artifacts in `reliability_notes`. Background the OCR (449 pp ≈ several minutes) and cut cache slices from the OCR sidecar.

**Principle:** Intake validation should classify *why* text is missing (truncation vs. no-text-layer vs. genuinely absent) and route to the matching remedy, rather than treating all low word-counts as the same defect.

### Observation 60: Intake must verify text CONTENT matches the expected book, not just word count

**Date:** 2026-07-09
**Session context:** Ingesting *Death Without Weeping* (Scheper-Hughes). The first raw/ file bearing that title's metadata actually contained the full text of a different book (Mary Brinton, *Women and the Economic Miracle*, on Japan) — a mislabeled scan.
**Skill:** CLAUDE.md ingest workflow (Step 1 word-count intake)
**Type:** internal
**Phase/Area:** Ingest Workflow — Step 1 scaffold / word-count intake check

**Issue:** The existing Step-1 "word-count intake check" is designed to catch *truncation* (epub→txt dropping chapters). It would NOT have caught this failure: the mislabeled file had a perfectly plausible word count and a real book inside — just the wrong book. It was caught only because a content sample happened to show "Japan"/"Mary Brinton". A pure word-count/TOC check passes a wrong-book-behind-right-title file.

**Suggested improvement:** Add to Step 1 a **content-marker verification**: after conversion, grep the body for a handful of expected terms (author surname, key place/subject names, protagonist/site) AND confirm the absence of obviously off-topic markers, before scaffolding. One line, e.g. `grep -ci "brazil|nordeste|alto"` vs `grep -ci "japan"`. Treat a mismatch as a hard stop and surface to the user (source collections hold near-duplicate twins and mislabeled scans).

**Principle:** Word count validates *quantity*; it does not validate *identity*. A source-intake check must confirm the text is the book you think it is — cheap content-marker greps catch mislabeled/swapped files that length checks pass silently.

### Observation 61: Naive frontmatter validator chokes on YAML folded/block scalars in ingest pages

**Date:** 2026-07-09
**Session context:** Ingesting Kleinman, *The Illness Narratives*, into the Social Sciences wiki. Wrote a `sources/` page whose `reliability_notes` used a YAML folded block scalar (`reliability_notes: >` with an indented multi-line body). `scripts/validate_schema.py` emitted ~11 "unparseable frontmatter line" warnings — its frontmatter parser is line-based, not a real YAML parser, so every continuation line of the folded scalar was read as a stray key.
**Skill:** New skill candidate / CLAUDE.md guidance for the Social Sciences (and World History) wiki ingest workflow
**Type:** internal
**Phase/Area:** Ingest Step 4 (page authoring) / Step 5 (validation)

**Issue:** The wiki's purpose-built validators parse frontmatter with a naive line scanner, not PyYAML. Folded (`>`) and literal (`|`) block scalars, which are valid YAML, produce a cascade of false "unparseable line" warnings. The established convention (seen in every existing source page, e.g. `scheper-hughes-death-without-weeping-1992.md`) is a single double-quoted string for long values like `reliability_notes`, with inner quotes backslash-escaped. Fix was to collapse the block scalar to one quoted line.

**Suggested improvement:** Add a one-line rule to the ingest workflow / CLAUDE authoring guidance: "Multi-line frontmatter values (reliability_notes, long notes) must be a single double-quoted string, never a YAML `>`/`|` block scalar — the schema validator is line-based and will flag every continuation line." Cheaply prevents a re-do cycle on nearly every source-page ingest.

**Principle:** When a repo ships its own bespoke, non-standard-library validator, author to the validator's actual parser, not to the spec the format nominally follows. Match the convention already present in passing files rather than using a technically-valid construct the tooling can't handle.

### Observation 62: Image-PDF OCR via ocrmypdf fills /tmp and loses sidecar text

**Status:** OPEN
**Date:** 2026-07-09
**Session context:** Social Sciences Wiki ingest of Ferguson *The Anti-Politics Machine* — 338-page image-only PDF
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md intake / PDF conversion); OCR pipeline
**Type:** internal
**Phase/Area:** Source intake — image PDF → text before word-count

**Issue:** First attempt used `ocrmypdf --force-ocr --rotate-pages --deskew --jobs 4 --sidecar` writing intermediates to /tmp (tmpfs ~5.8G). At ~page 269/338 Ghostscript hit "No space left on device"; pipeline exception; **sidecar text file remained 0 words** despite most pages having been OCR'd in temp. User-visible multi-minute wait then total failure. Recovery path: page-by-page pymupdf render (200 DPI) + tesseract, writing page texts under workspace `scratchpad/` (not /tmp), deleting PNGs immediately, stitching at end — completed 338/338 pages, ~124k words.

**Suggested improvement:** For image-only PDFs in this wiki: (1) prefer workspace-local temp (`scratchpad/tmp_ocr` or `TMPDIR` on the project disk), never rely on small tmpfs for 300+ page @400 DPI ocrmypdf; (2) prefer incremental page OCR with immediate image delete + stitch over single ocrmypdf sidecar when disk is tight; (3) lower DPI (200) is adequate for claim extraction; (4) document in CLAUDE.md or a local OCR note that ocrmypdf default /tmp can silently zero the text output on ENOSPC.

**Principle:** OCR pipelines that buffer full-resolution intermediates on a small tmpfs will fail late and can leave the *only* intended artifact (sidecar text) empty even after substantial work. Stream to durable storage page-by-page; treat completion as the stitched text file existing and non-empty, not as the OCR tool's exit code alone.


### Observation 63: Tesseract OCR of scanned-PDF ingests needs OMP_THREAD_LIMIT=1 under parallel

**Date:** 2026-07-09
**Session context:** Ingesting Kleinman's *Patients and Healers* (1980), a 445-page scanned image PDF with no text layer, into the Social Sciences wiki. Rasterized with pdftoppm then OCR'd with tesseract under GNU parallel -j 12.
**Skill:** CLAUDE.md ingest workflow (scanned-source OCR step) / atlas-curator-adjacent OCR guidance
**Type:** internal
**Phase/Area:** Ingest Step 1 (word-count intake / source prep) when the PDF is image-only

**Issue:** Running `parallel -j 12 tesseract ... --oem 1` (LSTM) crawled at ~0.08 pages/sec (ETA ~80 min for 445 pages). Cause: tesseract's LSTM engine uses OpenMP multithreading by default, so 12 concurrent processes each spawned ~12 threads → ~144 threads oversubscribing 12 cores, thrashing. Setting `OMP_THREAD_LIMIT=1` (single thread per process, one per core) jumped throughput to ~3.5 pages/sec (~40× faster; ETA ~90s). Also note: `{.}` (extension strip) is a GNU parallel token, NOT xargs — using it under `xargs -I{}` silently writes every page to a literal `{.}.txt`.

**Suggested improvement:** Add to the ingest workflow's scanned-PDF/OCR path: "When OCR-ing a scanned source, rasterize with pdftoppm then run `OMP_THREAD_LIMIT=1 parallel -j <ncores> 'tesseract {} {.} --oem 1 --psm 3 -l eng txt'`. The OMP_THREAD_LIMIT=1 is mandatory — without it, per-process OpenMP threads oversubscribe cores and OCR runs ~40× slower. Use GNU parallel (supports {.}), not xargs -I{} (which treats {.} literally)."

**Principle:** When fanning out an already-multithreaded tool across cores, pin each instance to one thread (OMP_THREAD_LIMIT/OPENBLAS_NUM_THREADS/etc.) or you get quadratic thread oversubscription that is far slower than either pure serial or pure parallel. Verify throughput with a short timed sample before committing to a long unattended run.

### Observation 64: Duplicate pre-scan should read near-match pages for delegation/authorship signals, not just existence

**Date:** 2026-07-09
**Session context:** Ingesting *Cannibal Metaphysics* (Viveiros de Castro) while a parallel session was actively densifying the Descola/ontological-turn cluster.
**Skill:** Social Sciences Wiki CLAUDE.md — Ingest Workflow (duplicate-page pre-scan; concurrent-session integration)
**Type:** internal
**Phase/Area:** Step 1 duplicate pre-scan → Step 4 integration

**Issue:** The Step-1 duplicate pre-scan found an existing `concepts/perspectivism.md`. Reading it (not just noting existence) revealed the concurrent Descola session had deliberately shaped it as a shared dual-source node with an explicit in-body delegation note ("densify from that source on the Viveiros-owned pages") and forward-links to pages I had not yet created. That reading changed my whole integration plan: I created the dedicated `multinaturalism`/`ontological-turn`/`controlled-equivocation` pages as the depth-bearing "owned" pages and kept perspectivism as a shared node with a single surgical edit (removing a now-duplicate alias). Had I only checked existence, I would likely have heavily rewritten a page another session was actively authoring. Separately, ~7 update-target pages threw "file modified since read" mid-integration — concurrency was pervasive.

**Suggested improvement:** In the duplicate-pre-scan guidance, add: when a pre-scan hit lands in a topic cluster another session may be working, *open and read* the page for delegation/authorship signals (in-body "densify elsewhere" notes, forward-links to not-yet-existing pages, recent `last_updated`) before deciding create-vs-update, and prefer creating your own depth-bearing pages while leaving the shared node minimally edited.

**Principle:** Existence checks answer "does a page exist?"; integration safety needs "who is authoring it right now and what do they expect me to do?" — which only reading the page reveals. In concurrent-ingest environments, the pre-scan is also an authorship-negotiation read.

### Observation 65: Source-page reliability_notes must be single-line quoted, not a YAML block scalar

**Date:** 2026-07-10
**Session context:** Ingesting Everett, *Don't Sleep, There Are Snakes* into the Social Sciences wiki.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md)
**Type:** internal
**Phase/Area:** Step 4/5 integration + validation (source page frontmatter)

**Issue:** I wrote the source page's long `reliability_notes` as a YAML folded block scalar (`reliability_notes: >` with indented continuation lines). `scripts/validate_schema.py` does not parse block scalars and emitted one "unparseable frontmatter line" WARN per continuation line (~14 warnings), forcing a rewrite to a single double-quoted line. The established convention across existing source pages is a single quoted string.

**Suggested improvement:** Add a one-line note to the CLAUDE.md Source Page schema / ingest checklist: "long frontmatter prose fields (reliability_notes, epistemic_leverage, endonym_exonym_note) must be single-line quoted strings — the validator does not accept YAML `>`/`|` block scalars." Prevents a guaranteed validation round-trip on every source ingest.

**Principle:** Author frontmatter to the parser you will actually run, not to YAML's full spec. When a custom validator defines the schema, its accepted subset is the real contract — encode that in the authoring guidance so it is right on the first write.

### Observation 66: Pull required body sections from the schema before writing new page types, not after validation

**Date:** 2026-07-10
**Session context:** Same Everett ingest — created 11 new pages across 8 page types (society, culture, thinker, theory, concept, method, study, debate, study-hub).
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md)
**Type:** internal
**Phase/Area:** Step 1/4 scaffolding of new content pages

**Issue:** Several first-draft pages missed required `##` body sections the schema mandates (concept: Operationalizations + Applications; culture: Lifeways + Relations and Successions; theory: Key Proponents and Texts; thinker: Contributions/Genealogy/Historiography), plus empty mandatory list fields that needed explicit `[[unknown]]`. Each surfaced only at `validate_schema.py` and cost an extra edit round. The positive counterpart: the recursion and study pages, where I had the required-section list in mind, passed first time.

**Suggested improvement:** Before writing a new page of a given type, paste that type's required body-section list and mandatory fields from CLAUDE.md into a quick checklist and author against it; treat empty list fields as requiring explicit `[[unknown]]`. Cheaper than a validate→fix→revalidate loop, especially when one ingest spans many page types.

**Principle:** For schema-governed artifacts, front-load the schema into the drafting step. A 20-second required-sections check before writing beats a validation round-trip after, and the saving scales with the number of distinct page types an ingest touches.

### Observation 67: Integration-agent frontmatter: instruct "[[unknown]]" not empty lists for mandatory fields

**Date:** 2026-07-10
**Session context:** Reich *Who We Are and How We Got Here* (2018) ingest — founding archaeogenetics layer; 5 Sonnet integration agents wrote ~25 pages partitioned by page-ownership.
**Skill:** Social Sciences CLAUDE.md — Deployed Subagent Strategy (Step 4 / two-stage integration variant)
**Type:** internal
**Phase/Area:** Integration-agent prompt / schema validation

**Issue:** The integration brief told thinker-page agents to "keep trained_under/trained EMPTY (describe collaborations in prose) to avoid genealogy-symmetry lint errors." Agents complied with literal empty lists (`trained: []`), which then tripped `validate_schema.py` WARNs ("field empty — fill it or use [[unknown]] explicitly"). The two lint checks pull in opposite directions: `lint_wiki.py` penalizes asymmetric genealogy links, while `validate_schema.py` penalizes empty mandatory fields. The correct resolution — `[[unknown]]` — satisfies both, but wasn't specified, so the fix had to be applied post-hoc.

**Suggested improvement:** In the deployed-subagent integration brief, when instructing agents to omit a link-bearing frontmatter field to avoid reciprocity lint, explicitly say "set it to `[[unknown]]`, never an empty list `[]`." Generalize: any mandatory schema field an agent cannot fill should be `[[unknown]]`, not blank — state this once in the standing integration instructions.

**Principle:** When two validators impose opposing constraints (reciprocity vs. completeness), the agent brief must name the value that satisfies both, or subagents will pick a locally-reasonable option that fails the other check. Don't leave the reconciliation to post-hoc cleanup.

### Observation 68: End-matter exclusion can silently truncate the last body chapter

**Date:** 2026-07-10
**Session context:** Ingesting Wheeler, *Archaeology from the Earth* (1954) via the deployed-subagent strategy; drawing the 4 line-range chunk boundaries.
**Skill:** CLAUDE.md ingest workflow (Deployed Subagent Strategy, Step 2 — "Split the book by disjoint line-ranges")
**Type:** internal
**Phase/Area:** Step 2 chunk-boundary drawing / body-vs-endmatter delimitation

**Issue:** To exclude the bibliography+index, I set the final chunk's end at line 10100 (estimated body end), but Chapter 17 — the pivotal "aims" chapter — actually ran to ~10245 before the "SELECT BIBLIOGRAPHY" heading at 10247. ~145 lines containing the book's peroration (the "problem of numbers" demographic-archaeology program, the "dig up people rather than mere things" restatement, the Pater coda) were dropped from all subagent ranges. The extractor correctly flagged the mid-sentence truncation; I recovered the tail on the main thread. No data lost, but the miss was avoidable.

**Suggested improvement:** When drawing the final chunk boundary, set the end at the *actual* line of the first end-matter heading (grep for "BIBLIOGRAPHY"/"INDEX"/"NOTES"/"APPENDIX"), never at an estimated body-end line. The word-count intake step already greps TOC chapter headings; extend that to grep the end-matter heading and anchor the last range to `endmatter_line - 1`. Cost is one grep; it closes a systematic tail-truncation risk that lands precisely on a book's concluding argument (often the most important chapter).

**Principle:** Body/end-matter boundaries are filesystem facts to be located, not estimated. Estimating the end of the body systematically risks truncating the final chapter — which in argument-driven books is disproportionately the payload. Anchor range edges to grepped headings, not guessed line numbers.

### Observation 69: Detect and yield on concurrent same-source ingest, not just concurrent same-page edits

**Date:** 2026-07-10
**Session context:** Ingesting Childe, *The Dawn of European Civilization* (1958). Midway through integration it emerged that a parallel session was ingesting the SAME book (plus the companion *Danube in Prehistory*), further along — it rewrote the shared source page, the pots-and-peoples debate, and built a Childe Thinkers Hub, while my index edits lost repeated read-modify-write races.

**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md) — concurrency handling
**Type:** internal
**Phase/Area:** Step 1 duplicate-page pre-scan; Step 4 integration under concurrency

**Issue:** CLAUDE.md's concurrency guidance covers "another session created a content page you reference" (Edit-append, keep depth on pages you own). It does not explicitly cover the stronger case: **another session ingesting the same source concurrently.** The pre-scan didn't catch it (the other session's Childe/culture pages didn't exist yet at pre-scan time; they appeared during my extraction). The collision surfaced only when the shared source page and a debate page were rewritten under me and index Edits failed on hash-mismatch races. Net waste: I authored a full pots-and-peoples debate and a source-page body that were superseded.

**Suggested improvement:** Add to the ingest workflow: (1) at pre-scan, when the raw queue shows the same author/topic being actively worked (e.g. a companion volume just ingested today), treat same-source collision as a live risk; (2) right before scaffolding the source page, and again before Step-4 integration, re-check whether the source-page slug now exists (created by another session) — if so, that session owns the ingest; switch to contributing only distinct additive pages (a missing concept, cross-layer construct-history) rather than re-authoring shared pages; (3) for hot shared bookkeeping files (index.md) under active contention, prefer a race-safe EOF/heredoc append over a prepend Edit that keeps losing read-modify-write races.

**Principle:** Concurrency safety is not only about not clobbering another session's *page* — it's about not duplicating another session's *task*. When two sessions ingest one source, the second to notice should yield authorship of shared pages and retreat to genuinely additive, uncontested contributions. Detect the collision by re-checking the source-page slug at each phase boundary, not once at the start.

### Observation 70: Table-cell piped wikilinks written despite the documented ban

**Date:** 2026-07-10
**Session context:** Ingesting Lucas, *Critical Approaches to Fieldwork* (2002) into the Social Sciences wiki; building a source page with a Section Plan table.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md)
**Type:** internal
**Phase/Area:** Step 5 lint/validate — wikilink hygiene

**Issue:** CLAUDE.md states explicitly under lint guidance: "No piped wikilinks in markdown table cells" (escaped `[[slug\|Display]]` renders in Obsidian but `check_wikilinks.py` parses the target as `slug\` and reports a broken link). Despite this documented rule, I wrote four escaped-pipe wikilinks inside the Section Plan table on the source page (`[[pitt-rivers-augustus\|Pitt Rivers]]` etc.), producing four broken links that were only caught at the final validation pass and required a fix-and-revalidate cycle. The rule is documented but did not reach the moment of authoring the table.

**Suggested improvement:** Add a pre-write structural check to the ingest workflow's scaffolding step: whenever authoring a markdown table that will contain wikilinks, use bare `[[slug]]` in cells by default and never the piped/escaped form. Consider a cheap mechanical guard — grep new/changed files for the pattern `\[\[[^]]*\\\|` (escaped-pipe inside a wikilink) as part of Step 4 before running the full validators, so this specific, known-recurring error is caught at authoring time rather than at final lint.

**Principle:** A documented prohibition that is violated during the creative flow of authoring needs structural enforcement, not just narrative statement. For known, mechanically-detectable formatting errors, a targeted grep run at write-time (not just the end-of-session validator) closes the gap between "the rule exists" and "the rule is followed."

### Observation 71: Running-header pollution defeats chapter-title grep for boundary detection in typeset-book PDFs

**Date:** 2026-07-10
**Session context:** Ingesting Clark, *Archaeology and Society* (1957) — a typeset book PDF where every page carries the chapter title as a running header.
**Skill:** Social Sciences ingest workflow (CLAUDE.md — Deployed Subagent Strategy, Step 2 boundary-drawing)
**Type:** internal
**Phase/Area:** Step 2 (split the book by disjoint line-ranges)

**Issue:** Grepping the raw text for chapter titles (`CHRONOLOGY`, `EXCAVATION`, etc.) to find chunk boundaries returned dozens of false hits because those strings appear as running headers on every page, not just at chapter openings. Only the TOC occurrence and the true chapter-opening were wanted. Boundary line numbers had to be found instead via distinctive first-sentence content and the TOC's page-number mapping cross-checked against a spot-read.

**Suggested improvement:** In Step 2, note that for typeset-book PDFs the reliable boundary signal is (a) the TOC page→content mapping plus (b) a distinctive first-sentence phrase from each chapter opening, NOT the chapter-title string (which recurs as a running header). Add one line to the boundary-drawing guidance: "chapter-title grep is unreliable in books with running headers — locate openings by distinctive opening-sentence phrases and TOC page numbers."

**Principle:** Structural landmarks that repeat as page furniture (running heads, folios, plate captions) are noise, not signal, for programmatic boundary detection; anchor partitioning to content that occurs exactly once per section.

### Observation 72: Pre-scan for existing target pages before dispatching authoring subagents in a paralleled/resumed ingest

**Date:** 2026-07-10
**Session context:** Ingesting the three Binford books (New Perspectives 1968, In Pursuit 1983, Nunamiut 1978) while a parallel session was independently ingesting the same author — it had already created stub versions of most target pages (concepts, methods, theory, debate, source pages).
**Skill:** Social Sciences Wiki CLAUDE.md (Ingest Workflow — Deployed Subagent Strategy)
**Type:** internal
**Phase/Area:** Step 4 integration / new-page authoring subagents

**Issue:** I dispatched 4 subagents to AUTHOR new concept/method pages "from scratch" (own-the-slug, Write directly). All four target files already existed as stubs created by the concurrent session. Three of the four agents failed with transient API "connection closed mid-response" errors *after* discovering the file existed and starting a full rewrite; the one that succeeded overwrote a stub. The duplicate-page pre-scan (CLAUDE.md Step 1) was run for THINKERS/theories but not extended to the concept/method/debate slugs the ingest would create, so the collisions were not anticipated.

**Suggested improvement:** Before dispatching any "author this new page" subagent, `ls`/grep the exact target path. If it already exists, switch that agent's instruction from Write-new to Read-then-Edit-densify (or handle on the main thread), and tell it what the stub already contains. Extend the Step-1 duplicate pre-scan to the FULL set of slugs the ingest will create (concepts, methods, debates, sources), not just thinkers/theories — especially when resuming an interrupted session or running alongside a concurrent one, where stubs are likely to already be on disk.

**Principle:** In a resumed or concurrent ingest, "new page" is an assumption, not a fact. Verify page existence per-slug immediately before authoring, and route existing pages to Edit-densify — this avoids clobbering a concurrent session's work and avoids wasting a full-rewrite agent (and the mid-write API-failure risk) on a file that only needed additive densification.

### Observation 73: Duplicate pre-scan should check hyphenation/phrasing variants of NEW concept slugs, not just person-name orders

**Date:** 2026-07-10
**Session context:** Ingesting Johnson, *Archaeological Theory* (2nd ed.) — an integration subagent was told to CREATE `concepts/emic-etic.md`, but discovered `concepts/emic-and-etic.md` already existed and correctly appended to it instead of forking a duplicate slug.
**Skill:** CLAUDE.md ingest workflow (duplicate-page pre-scan step)
**Type:** internal
**Phase/Area:** Step 1 duplicate-page pre-scan / Step 4 reconciliation

**Issue:** The Step-1 duplicate pre-scan guidance focuses on person-name order (`durkheim-emile`/`emile-durkheim`) and same-entity-across-folders. It does not explicitly call for checking *phrasing/hyphenation variants* of planned NEW concept/theory slugs (`emic-etic` vs `emic-and-etic`, `world-systems-theory` vs `world-systems-analysis`). Here the near-duplicate was caught only because the integration agent independently `ls`-checked before writing; a less careful agent would have created a colliding second page the wikilink checker cannot flag.

**Suggested improvement:** In the CLAUDE.md duplicate pre-scan, add: before finalizing any planned NEW concept/theory slug, grep existing filenames for connective/hyphenation variants (insert/drop `-and-`, `-of-`, singular/plural, `-theory`/`-analysis`/`-archaeology` suffix swaps). State the confirmed canonical slug in each integration agent's brief so agents don't independently rediscover the collision.

**Principle:** Slug collisions the wikilink checker cannot catch (both resolve) are cheapest to prevent at planning time. Name-order variants are one case of a broader class — any two strings that a human would read as the same concept but that differ by connectives, suffixes, or number. Pre-resolve the canonical form once, centrally, rather than relying on each parallel agent to notice.

### Observation 74: Web/secondary-source ingests must flag warranted hub pages as unbuilt, not fabricate depth

**Date:** 2026-07-10
**Session context:** "ingest web dubois race and the city" — first web-based ingest (The Philadelphia Negro, 1899), built from Wikipedia/encyclopedia/retrospective article/volume description rather than a source file in raw/.
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md)
**Type:** internal
**Phase/Area:** Ingest Workflow Step 1 (hub warranted-but-unbuilt) + Source-Type Handling

**Issue:** The Philadelphia Negro clearly meets Studies-Hub selection criteria (founded a subfield), which CLAUDE.md says makes the hub page mandatory in-session, not deferrable. But the source material was thin web secondary sources — no primary text — so an excavation-grade hub with verbatim load-bearing quotation could not be honestly produced. Resolved by building full normal-resolution pages (source/study/society/concept/debate) and explicitly flagging the hub as warranted-but-unbuilt pending a full-text ingest, in the source page, study page, log, and Structural_Sources.

**Suggested improvement:** Add a short note to CLAUDE.md's hub rules (or Source-Type Handling) that when an ingest is web/secondary-source-only, a warranted hub is flagged-and-deferred with the evidentiary reason (cannot support verbatim primary quotation), rather than either fabricated from secondary sources or silently skipped. Pair with a standing reliability_notes convention documenting the web-derived basis and unverified figures.

**Principle:** Hub-grade depth has an evidentiary floor (primary-text access). When a source class can't meet it, the honest move is to build to the resolution the sources support and flag the gap explicitly with its cause — not to counterfeit depth or drop the requirement silently.

### Observation 75: Two-column / illustrated PDFs undercount ~9× under pdftotext -layout, mimicking a truncated conversion

**Date:** 2026-07-10
**Session context:** Ingesting Leakey & Lewin, *Origins* (1977) — a heavily illustrated, two-column popular-science book — into the Social Sciences wiki.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md word-count intake step)
**Type:** internal
**Phase/Area:** Step 1 — word-count intake check

**Issue:** `pdftotext -layout` on this 272-page book produced only ~10,525 words across 95k lines (mostly whitespace) because the -layout mode tried to preserve the two-column + scattered-caption layout and fragmented/dropped body text. Against the ~250-350 w/page heuristic this reads as a badly truncated conversion (would-be ~68-95k expected), which would have triggered a spurious incompleteness investigation. Plain `pdftotext` (no -layout) on the same file gave 94,191 words — the true body — by using reading-order flow instead of spatial layout. The `-layout` flag is the culprit, not the source.

**Suggested improvement:** In the word-count intake step, when a PDF is multi-column or heavily illustrated (or when a first `wc -w` comes in far below the page-count heuristic), extract BOTH ways — `pdftotext` (plain, reading-order) and `pdftotext -layout` — and take the higher/cleaner word count before concluding the conversion is incomplete. Prefer plain pdftotext for prose ingestion of multi-column books; reserve -layout for tabular/gazetteer material where column structure matters.

**Principle:** A low word count from one extraction mode is a tool-configuration signal, not necessarily a truncated-source signal. Layout-preserving extractors scramble and undercount flowing prose in multi-column designs; cross-checking a second extraction mode cheaply distinguishes "bad flag" from "bad file" before escalating to a grep-for-chapters incompleteness hunt.

### Observation 76: Concurrent ingests of the same topic cluster silently create duplicate pages under divergent slugs

**Date:** 2026-07-10
**Session context:** Ingesting Klein, *The Human Career* (paleoanthropology) while a parallel session ingested Stringer & Gamble / Gamble *Timewalkers* — the SAME Neanderthal/modern-human-origins cluster — at the same time.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md deployed-subagent strategy)
**Type:** internal
**Phase/Area:** Step 1 duplicate pre-scan / Step 4 reconciliation

**Issue:** The CLAUDE.md duplicate pre-scan checks the vault state at *session start*, but a concurrently-running ingest of an overlapping topic creates pages *during* the session that the pre-scan never saw. Result: two sessions independently created duplicate pages under divergent slugs — my `cultures/mousterian-industry.md` vs the other session's `concepts/mousterian.md`; `sites/qafzeh-skhul.md` vs separate `qafzeh.md`+`skhul.md`; and a same-slug collision `concepts/control-of-fire.md` vs pre-existing `phenomena/control-of-fire.md`. The wikilink checker does NOT catch divergent-slug duplicates (both resolve). Caught only by noticing the other session's link targets on a shared discipline page and running a targeted `find`/`ls` before my new-page agents finished. Had to stop one integration agent mid-run (it was about to clobber the other session's `shanidar.md`) and delete 6 of my own pages, folding their content as attributed layers onto the other session's canonical pages.

**Suggested improvement:** When a concurrent session may touch the same cluster (detectable: shared pages show recent mtimes / unfamiliar link targets to slugs you didn't create), (a) BEFORE spawning new-page agents, `ls`/`find` the target folders for the entity names — not just the vault-start pre-scan; (b) prefer folding into the other session's canonical page over creating a parallel page; (c) you may freely delete/repoint your OWN pages but must never clobber the other session's — so consolidation always deletes your duplicate, not theirs; (d) run new-page agents with `run_in_background` so you can `TaskStop` one if a collision surfaces mid-run.

**Principle:** The duplicate pre-scan assumes the vault is static during a session; under concurrent ingests of an overlapping topic it is not. Re-scan target folders immediately before the write step, and treat "delete mine, defer to theirs" as the collision-resolution rule since you can only safely mutate pages your session owns.

### Observation 77: Extraction subagents should write their claims file in ONE final Write to survive mid-stream API deaths

**Date:** 2026-07-10
**Session context:** Same Klein ingest — two of eight extraction subagents (the two largest chapters) died with "Connection closed mid-response" transient API errors.
**Skill:** Social Sciences wiki ingest workflow (deployed-subagent strategy, Step 3)
**Type:** internal
**Phase/Area:** Step 3 extraction prompts / Step 3-completion filesystem inventory

**Issue:** Both dead agents' final transcript note said "now writing the claims file" — they had completed extraction but died before (or during) the write, leaving NO claims file on disk. The filesystem inventory correctly flagged both ranges as missing, but all extraction work was lost and the ranges had to be fully re-run. The two re-spawns, whose prompts explicitly said "write the file in ONE Write call once extraction is done," both succeeded.

**Suggested improvement:** Add to every extraction-agent prompt: "Do all reading/extraction first, then emit the claims file in a SINGLE Write call at the very end — do not build it incrementally with multiple appends." A one-shot terminal write means a mid-stream death loses nothing recoverable anyway (extraction wasn't persisted) but guarantees that any agent that reaches the write step produces a complete file, and avoids partial/truncated claims files that look complete to the inventory.

**Principle:** For fan-out subagents whose only durable output is a file, make the write atomic and terminal. Incremental writing creates a window where a transient death yields a partial file that passes an existence check but is silently incomplete; a single terminal write collapses that window to all-or-nothing.

### Observation 78: Word-count intake check misses font-CMap text-layer corruption; add a per-range legibility-ratio gate

**Date:** 2026-07-10
**Session context:** Ingesting Service, *Origins of the State and Civilization* (1975), a scanned PDF from Anna's Archive. `pdftotext -layout` produced a file that passed the CLAUDE.md word-count intake check (163k words ≈ expected for ~360 pp) but whose text layer was gibberish on the majority of pages (bad embedded-font→Unicode CMap). Four of six extraction subagents returned "text is corrupted" and one died; two ranges happened to use a correctly-mapped font and extracted fine.

**Skill:** CLAUDE.md ingest workflow (Step 1 "word-count intake check") — project skill, internal.
**Type:** internal
**Phase/Area:** Ingest Step 1 (intake) / Step 3 recovery

**Issue:** The mandated intake check verifies *quantity* (word count vs. page count) but not *legibility*. Font-CMap corruption preserves word count (garbage tokens still count as words) while destroying content, so it sails through. The failure only surfaced after spawning six extractors — expensive — when it could have been caught in seconds at intake. Recovery required a full `ocrmypdf --force-ocr` re-OCR + re-cut + re-spawn, roughly doubling the ingest's agent cost.

**Suggested improvement:** Add a **legibility-ratio gate** to the intake check: `clean = ratio of [A-Za-z]{3,} tokens to total words`. A healthy English text layer scores ~0.75–0.85; corrupted pages score ~0.01–0.05. Compute it whole-file AND per intended cache slice before spawning (a whole-file average can hide localized corruption — here whole-file was ~0.5 while individual ranges were 0.01). If any slice scores below ~0.5, re-OCR with `ocrmypdf --force-ocr` (or tesseract on `pdftoppm` images) before extraction. One-liner: `tot=$(wc -w <f); cl=$(grep -oE '[A-Za-z]{3,}' f | wc -l); awk "BEGIN{print cl/tot}"`.

**Principle:** Intake validation should test the property you actually depend on (readable text), not a proxy that correlates with it under normal conditions (word count). Corruption modes that preserve the proxy while destroying the target are exactly the ones a quantity-only check is blind to — and catching them at intake is orders of magnitude cheaper than catching them after fan-out.

### Observation 79: Dual taxonomy for lithic industries reintroduced mid-ingest

**Date:** 2026-07-10
**Session context:** Ingest of Gamble *Palaeolithic Societies of Europe* (1999)
**Skill:** Social Sciences wiki ingest / CLAUDE.md taxonomy
**Type:** internal
**Phase/Area:** Integration / culture vs concept page ownership
**Status:** OPEN

**Issue:** Prior Klein ingest deleted cultures/mousterian-industry|aurignacian-industry|chatelperronian-industry to fold onto concepts/mousterian|aurignacian|chatelperronian (concurrent-session collision fix). A Stage-2 integrator for Gamble 1999 recreated the three cultures/*-industry pages with substantial densification, while concepts bare pages retain Stringer-Gamble/Klein layers. Dual taxonomy is now live again (also matches oldowan/acheulean cultures/*-industry pattern). Main thread added reciprocal pointers rather than deleting densification.

**Suggested improvement:** CLAUDE.md or a short taxonomy note should state the standing rule for lithic industries: either (a) cultures/*-industry for material constructs + concepts/ bare for classificatory history is allowed and preferred, or (b) concepts only — so integrators inherit one rule and do not thrash pages across sessions.

**Principle:** When concurrent sessions resolve taxonomy differently, later integrators need an explicit canonical rule on disk; otherwise densification work recreates the conflict the previous session solved.

### Observation 80: Wall-clock is the primary defense against concurrent-ingest collisions — slow sessions cause the collisions they then have to reconcile

**Date:** 2026-07-10
**Session context:** Klein *Human Career* ingest collided repeatedly with three parallel ingests (Stringer&Gamble, Gamble Timewalkers, Gamble Palaeolithic Societies) building the same Neanderthal/modern-origins cluster; user feedback: "you're running into problems with concurrent agents because you move at a snail's pace."
**Skill:** Social Sciences wiki ingest workflow (deployed-subagent strategy)
**Type:** internal
**Phase/Area:** whole-session pacing / Step 1 scaffold / Step 4 integration

**Issue:** The duplicate-collision reconciliation (obs #76) was expensive, but its ROOT cause was session duration: the longer the ingest ran, the more pages the parallel sessions created in the overlap zone, and the more reconciliation was needed. Time was lost to avoidable latency: (a) reading ~6 existing pages one-at-a-time "to prep integration," most of which were then only EOF-appended (so the reads were unnecessary — shell append doesn't need the Edit gate); (b) reading all 8 claims files sequentially before integrating any page; (c) largely sequential phases (scaffold → existing-page appends → spawn new-page agents → bookkeeping) when large parts were independent.

**Suggested improvement:** Treat minimizing wall-clock as an explicit collision-mitigation goal, not just efficiency. Concretely: (1) overlap phases — spawn extraction, write scaffold, and queue new-page integration agents in overlapping waves rather than finishing each phase first; (2) do NOT pre-read pages you will only EOF-append to (collision-safe shell append needs no prior Read); (3) batch every independent Read/Edit/Bash into single multi-tool messages; (4) integrate each page as soon as its claims inputs exist, don't gate on reading the full claims set; (5) re-scan target folders cheaply right before the write step instead of front-loading expensive reads. A short session is the best collision defense — reconciliation is a symptom of a long one.

**Principle:** Under concurrent sessions on an overlapping topic, latency is not just slow — it is the mechanism that manufactures the collisions. Compressing wall-clock (parallelism, batching, skipping unnecessary reads) prevents collisions upstream, which is cheaper than reconciling them downstream.

### Observation 81: Duplicate-page pre-scan must re-run just before page creation, not only at session start

**Date:** 2026-07-10
**Session context:** Ingesting Fagan *The Great Journey* while a Meltzer 2009 ingest was concurrently creating the same subject-matter pages (paleoindian, clovis-culture, monte-verde, folsom-site, pre-clovis, overkill debate).
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md) — New skill candidate: N/A (project-internal)
**Type:** internal
**Phase/Area:** Ingest Step 1 duplicate-page pre-scan; Step 4 integration

**Issue:** The Step-1 duplicate pre-scan ran once at session start and found no Clovis/Beringia/Paleo-Indian pages. But a concurrent Meltzer ingest created canonical pages (`paleoindian.md`, `folsom-site.md`, etc.) *during* my session, after my scan. I created `concepts/paleo-indian.md` as a duplicate of the existing `paleoindian.md` before catching it, and repeatedly misread the save-time linter's "file modified since read" as evidence of a live concurrent agent, wasting cycles theorizing about concurrency instead of just re-reading and merging.

**Suggested improvement:** (1) Re-run the duplicate/existence check with a quick `ls`/`test -e` **immediately before each page Write**, not only at Step 1 — cheap and catches pages created mid-session. (2) On the first "file exists" / "modified since read" error, default to *read-then-merge* rather than diagnosing concurrency; treat these as routine when a linter hook or parallel ingest is possible. (3) When creating a concept slug, check both hyphenation variants (`paleo-indian` vs `paleoindian`) in the pre-scan, as with name-order variants for people.

**Principle:** In a shared, linter-hooked, possibly-multi-session vault, existence/duplication is a filesystem fact that can change mid-session — verify it at point-of-write, not once up front, and treat write-time "file changed" signals as merge cues, not anomalies to investigate.

### Observation 82: phenomenon_type enum lacks an 'environmental' value, forcing environmental-science phenomena to 'other'

**Date:** 2026-07-10
**Session context:** Ingesting Roberts, *The Holocene: An Environmental History* (1998) into the Social Sciences Wiki — created 7 environmental phenomenon pages (holocene-climate-change, sea-level-change, deforestation, soil-erosion, desertification, eutrophication, freshwater-acidification).
**Skill:** New skill candidate / CLAUDE.md schema (Social Sciences Wiki Phenomenon Page schema + validate_schema.py)
**Type:** internal
**Phase/Area:** Phenomenon Page frontmatter — phenomenon_type enum

**Issue:** All seven environmental phenomena naturally took `phenomenon_type: environmental`, which is not in the allowed set [demographic, economic, political, religious, cultural, technological, stratification, other]; validate_schema flagged 7 errors until changed to 'other'. Environmental/physical-process phenomena are core subject matter for this wiki (archaeology + environmental archaeology), yet the enum has no dedicated value, so they all collapse to the uninformative 'other'.

**Suggested improvement:** Add `environmental` to the phenomenon_type enum in both the CLAUDE.md Phenomenon Page schema and scripts/validate_schema.py. Until then, the standing convention is: environmental/physical-process phenomena use `phenomenon_type: other`.

**Principle:** When a wiki's stated scope includes a domain (here, environment-as-subject-matter, explicit throughout CLAUDE.md's design principles and evidence-class framework), the frontmatter enums should carry a first-class value for it; otherwise every page in that domain is filed under a catch-all, defeating the classification. Enum coverage should track declared scope.

### Observation 83: Stage-2 integration subagents violate frontmatter enums and omit required body sections

**Date:** 2026-07-10
**Session context:** Ingesting Roux, *Ancient Iraq* into the Social Sciences Wiki via 6 page-owned Stage-2 integration subagents (each creating/editing a disjoint slug set from claims files).
**Skill:** Social Sciences Wiki CLAUDE.md ingest workflow (deployed-subagent strategy)
**Type:** internal
**Phase/Area:** Step 4/5 integration + validation

**Issue:** Despite being handed exact per-page-type frontmatter templates and enum lists, integration subagents repeatedly (a) put *descriptive prose* into closed-enum frontmatter fields — `contested: "no (as a script family); yes (details of origin...)"`, `emic_or_etic: "emic corpus, analyzed etically"` — instead of the allowed `yes`/`no`/`emic`/`etic`/`migrated`; and (b) omitted required body sections (culture pages missing `## Lifeways` and `## Relations and Successions`; concept pages missing `## Operationalizations` / `## Semantic History`). Main thread caught all 14 via `validate_schema.py --only` and fixed them, but it was ~15 min of avoidable rework across 5 pages.

**Suggested improvement:** In the shared integration-conventions file, add an explicit "CLOSED ENUM — use one token only, put nuance in the body" callout next to `contested`, `emic_or_etic`, `culture_type`, `date_precision`, etc., AND a per-page-type "REQUIRED SECTIONS CHECKLIST" the agent must self-verify against before finishing (mirrors the Pre-Flight Principle). Better still: instruct each integration agent to run `python scripts/validate_schema.py --only <its-own-slugs>` before reporting done, and fix its own errors — pushing validation into the agent instead of the main thread.

**Principle:** When delegating schema-constrained artifact creation to subagents, give them the *validator*, not just the schema. A closed enum stated as prose is the single most common failure; a self-run validation gate converts a main-thread rework loop into an in-agent fix loop.

### Observation 84: "Unresolved [[slug]] is acceptable" conflicts with the 0-new-broken-links gate

**Date:** 2026-07-10
**Session context:** Roux *Ancient Iraq* integration; agents created ~19 wikilinks to not-yet-existent pages (Assyrian kings [[sargon-ii]], [[ashurbanipal]], etc.; [[hammurabi]]; [[tepe-gawra]]; [[concepts/empire]]).
**Skill:** Social Sciences Wiki CLAUDE.md ingest workflow
**Type:** internal
**Phase/Area:** cross-linking conventions vs. Step 5 wikilink validation

**Issue:** The integration-conventions text told agents "a [[slug]] that doesn't exist yet is acceptable (it marks a future page)." But `check_wikilinks.py` counts every such link as broken, and the ingest's hard gate is "0 NEW broken links vs baseline." So the guidance directly manufactured 19 gate failures that the main thread then had to de-link by hand (perl fixed-string replacement of `[[slug|Display]]` → `Display`).

**Suggested improvement:** Change the convention to: "Only link a `[[slug]]` that already exists OR that THIS ingest will create (the master slug list). For any entity you mention but are NOT creating a page for (individual rulers, minor sites, un-minted concepts), write it as **plain text / bold**, never as a wikilink. Forward-reference links are NOT acceptable — they break the validator." Optionally: reserve a single sanctioned placeholder (`[[unknown]]`) which resolves, for genuinely-unknown targets.

**Principle:** "Mark a future page with a dead link" only works if the link checker tolerates dead links. When the completion gate is zero-new-broken-links, the convention must forbid forward-reference links outright and route un-minted entities to plain text. Align authoring guidance to the exact validator that gates the work.

### Observation 85: Anchoring extraction chunk boundaries on trailing per-chapter "Notes" lines causes a systematic ~1-chapter offset

**Date:** 2026-07-10
**Session context:** Ingesting Van De Mieroop, *A History of the Ancient Near East* — a textbook whose converted text places a per-chapter "Notes" section AFTER each chapter body, plus interspersed "Debate"/"Box" inserts.
**Skill:** Social Sciences Wiki CLAUDE.md ingest workflow (Step 2, drawing disjoint line-range chunks)
**Type:** internal
**Phase/Area:** Step 2 chunk-boundary drawing for extraction

**Issue:** I sized the 7 extraction chunks by `wc -w` on line ranges whose boundaries I set at the per-chapter "Notes" grep lines, assuming Notes marked chapter ends. Because each chapter's Notes block sits after its body AND the file also had front-matter Debate/Box lists reusing chapter headings, every back-half slice landed ~1 chapter later than intended: range_1 got Ch2–3 not Ch1–2, range_3 got Ch6–7 not Ch5–6–7 (missing the Old Assyrian trade), range_5 got Ch11–12 not Ch10–11, etc. Coverage survived only because adjacent chunks overlapped (Ch5 was caught as range_2 "overflow"); the tail of Ch10 fell through entirely (low-impact only because another source already covered it). Six agents each independently flagged "my slice isn't what the brief said."

**Suggested improvement:** In Step 2, before cutting slices, VERIFY boundaries against body content, not just heading/Notes greps: (1) grep the actual chapter-BODY opening line (e.g. the chapter title immediately followed by its first section like "2.1") and confirm the *next* chapter's body-open is past the boundary; (2) spot-read ~5 lines at each proposed boundary to confirm it's a true body transition, not a Notes/Debate/Box insert or a TOC echo; (3) when converted ebooks interleave notes/boxes, prefer anchoring on the chapter-body-open line minus 1, never on the trailing Notes line. Add a one-line "boundary spot-check" to the Step-2 checklist. Cost: ~1 minute; benefit: avoids 6 agents extracting shifted content and a silent coverage gap.

**Principle:** A chunk boundary is only as good as the assumption that the anchor line marks the content transition you think it does. Ebook conversions relocate/duplicate structural markers (notes after body, TOC/list echoes of headings), so grep-on-heading is unreliable for boundary-drawing — verify each boundary against the actual body text before committing N agents to it.

### Observation 86: Scanned-image epub intake needs ordered-page OCR, not ebook-convert alone

**Date:** 2026-07-10
**Session context:** Ingest Cunliffe *The Ancient Celts* (scanned-image epub, 362 JPGs)
**Skill:** Social Sciences wiki ingest / CLAUDE.md intake
**Type:** internal
**Phase/Area:** Word-count intake / OCR recovery path
**Status:** OPEN

**Issue:** ebook-convert and pandoc produced empty/placeholder text for an image-only epub (page JPGs embedded in index.html). Word-count intake correctly flagged 0 words, but the recovery path had to be invented mid-session: extract reading order from HTML img src, filter large JPGs, parallel tesseract with OMP_THREAD_LIMIT=1, optional 2× upscale for low-res (~521×751) scans.

**Suggested improvement:** In CLAUDE.md word-count intake (or a pdf/epub intake note), document the **image-epub branch**: if ebook-convert/pandoc yield <1k words but the archive contains many large page images, run ordered-page OCR (HTML reading order → tesseract) rather than treating the source as empty. Note low-res scans benefit from 2× upscale + psm 3.

**Principle:** Zero-word conversion of a large epub is a format-detection signal (scanned images), not proof the book is unavailable — recovery is ordered OCR of the plate stream, not a different acquisition.

### Observation 87: Stage-2 integration agents invent page slugs for chapters and mis-copy the source slug

**Date:** 2026-07-10
**Session context:** Ingesting *Directions in Sociolinguistics* (Gumperz & Hymes 1972) via 8 extraction + 5 Stage-2 integration subagents (deployed-subagent strategy).
**Skill:** Social Sciences Wiki ingest workflow (CLAUDE.md), Deployed Subagent Strategy / Stage-2 integration.
**Type:** internal
**Phase/Area:** Step 4 integration — subagent prompting for new-page creation.

**Issue:** Every Stage-2 integration agent that authored thinker pages populated `key_works` with `[[author-chapter-title-1972]]` wikilinks to per-chapter *study* pages that were never created (chapters do not each earn a studies/ page), and several copied the source slug as `gumperz-hymes-directions-IN-sociolinguistics-1972` instead of the canonical `gumperz-hymes-directions-sociolinguistics-1972`. Both produced broken links caught only at the final wikilink validation (~10 broken links across 6 files), requiring a main-thread cleanup pass. One agent also linked a plausible-but-nonexistent concept (`[[ethnoscience]]`) and set an out-of-enum `concept_type: migrated`.

**Suggested improvement:** In the Stage-2 integration prompt template, add three explicit rules: (1) state the canonical source slug ONCE, verbatim, and say "copy this exact string — do not reconstruct it"; (2) "Do NOT invent slugs for book chapters — a chapter is not a studies/ page; cite it as plain text '<Title>' (in [[source-slug|Source]], year), never as a [[chapter-slug]] wikilink"; (3) "Only bracket a slug you can see in the provided canonical-slug list or that your own cluster creates; everything else is plain text." Optionally have integration agents self-check with a grep for `[[` targets against the known page set before finishing.

**Principle:** Subagents creating pages will confidently mint non-existent link targets (chapter-as-study slugs, near-miss source slugs, plausible concept pages) unless the prompt both forbids slug invention and supplies exact canonical strings to copy. Broken links are cheap to prevent at prompt time and expensive to chase at validation time across many files.

### Observation 88: Structural_Sources greedy regex dedupe destroyed ledger

**Date:** 2026-07-10
**Session context:** Carneiro Evolutionism ingest bookkeeping
**Skill:** Internal (Social Sciences Wiki CLAUDE.md / ingest bookkeeping)
**Type:** internal
**Phase/Area:** Step 6 bookkeeping — Structural_Sources.md updates
**Status:** OPEN

**Issue:** After inserting a Carneiro ledger entry, a Python regex meant to dedupe two Carneiro occurrences used a non-greedy-looking but actually over-broad DOTALL pattern that matched from the first Carneiro bullet through a huge mid-file span (second false "match" ~32k chars), deleting most of the top-of-file 2026-07-10 recent-ingest ledger. No git repo in the vault, so recovery required session terminal logs. Restored Renfrew/Kirch/Cunliffe/Wilkinson/Kemp + Carneiro at top; residual size still ~23k below pre-edit.

**Suggested improvement:** Never use multi-line regex to dedupe ledger entries. Prefer: (1) single-line exact-string checks before insert; (2) insert only at a known anchor (`## Recently ingested` or first `- **YYYY-MM-DD**`) with exact prefix match; (3) if dedupe needed, match only one line starting with `- **DATE** — ✅ Author, *Title`. Add CLAUDE.md rule: Structural_Sources edits must be single-bullet appends; verify file size/line-count within ~2% after edit; never run multi-match delete without dry-run size check.

**Principle:** Bookkeeping files that accumulate concurrent session writes need append-only discipline; destructive multi-match edits on shared ledgers are high blast-radius and need pre/post size assertions.

### Observation 89: Duplicate-page pre-scan must grep the slug across ALL folders, not one folder

**Date:** 2026-07-10
**Session context:** Ingesting Kirch, *On the Road of the Winds* (2017) into the Social Sciences wiki via deployed subagents.
**Skill:** Social Sciences wiki CLAUDE.md ingest workflow (Step 1 duplicate-page pre-scan) — internal.
**Type:** internal
**Phase/Area:** Step 1 scaffold / duplicate pre-scan; Step 4 integration.

**Issue:** During scaffolding I checked whether `ancestral-polynesian-society` existed by testing `societies/ancestral-polynesian-society.md` (missing) and concluded the wikilink was "broken" and needed creating. In fact `concepts/ancestral-polynesian-society.md` already existed (from a prior Kirch ingest) and resolved the link fine. A Stage-2 society agent then created a `societies/` page with the same slug → a duplicate-slug collision (Obsidian resolves ambiguously; lint flags it). I caught it only at bookkeeping when reading the Structural_Sources ledger, then had to fold content into the canonical concept page and delete the duplicate — a ~10-minute detour.

**Suggested improvement:** In the duplicate-page pre-scan, resolve every candidate slug with a **folder-agnostic** check — `find wiki -name "<slug>.md"` or `grep -rl` across the whole vault — never a single-folder `[ -f folder/slug.md ]` test. Obsidian resolves wikilinks by bare filename across all folders, so a slug is "taken" if it exists in ANY folder. Add this as an explicit instruction to CLAUDE.md's Step-1 pre-scan bullet ("check both name orders AND all folders; a bare `[[slug]]` resolves vault-wide").

**Principle:** When a system resolves references by a flat namespace (filename) but stores files in folders, existence checks must query the flat namespace, not the folder path. A per-folder existence test gives false "missing" results and manufactures duplicates.

### Observation 90: Word-count intake check must account for `wc` column order

**Date:** 2026-07-10
**Session context:** Ingesting Liu & Chen, *The Archaeology of China* (2012), 500-page PDF, via the deployed-subagent workflow.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md "word-count intake check")
**Type:** internal
**Phase/Area:** Deployed Ingest Step 1 — word-count intake check

**Issue:** Ran `wc -w -l "$file"` and read the output as `30504` words for a 500-page book (~61 w/p), which tripped the "converted ebooks fail silently / incomplete conversion" alarm and prompted an investigation. The file was actually complete: `wc` always prints counts in fixed order (lines, then words), regardless of flag order, so `30504` was the LINE count and `187522` was the word count (~375 w/p, healthy). The false alarm cost one extra verification round (inspecting mid-file content, recounting via awk).

**Suggested improvement:** In the CLAUDE.md "word-count intake check" instruction, specify `wc -w <file>` (words only) or `awk '{n+=NF} END{print n}' <file>` for the intake ratio, and note that `wc -l -w`/`wc -w -l` both emit lines-first — never infer words from column position when both flags are set.

**Principle:** A verification heuristic that keys on a single number must pin down the number's provenance unambiguously; `wc`'s fixed column order (lines, words, bytes) ignores flag order, so any "words per page" gate should request words in isolation to avoid a self-inflicted false-positive on the very completeness check meant to catch real truncation.

### Observation 91: Main-thread-author theory chapters of a comparative-theoretical treatise; subagents only for empirical illustration

**Date:** 2026-07-10
**Session context:** Ingesting Kroeber, *Configurations of Culture Growth* (1944) — a ~281k-word comparative treatise whose wiki payload is concentrated in Ch. I (method/genius) and Ch. XI (Review/Conclusions), with Chs. II–X being domain-by-domain empirical surveys that only *illustrate* the argument.
**Skill:** CLAUDE.md ingest workflow (deployed-subagent strategy)
**Type:** internal
**Phase/Area:** Step 2 (chunking) / Step 4 (integration)

**Issue:** For a theoretical work where the analytic core lives in one or two chapters, the fastest correct path was to (a) spawn subagents over ALL chapters for structured claims, but (b) read the two theory chapters directly on the main thread while agents ran, and author the concept/study/debate pages from those direct reads — treating the empirical-chapter claims files as a source of *generalizations and a few illustrative cases only*, never as subject-matter findings. Several empirical extractors self-reported partial coverage of the per-country catalogue; this was fine and required no gap-fill, because that catalogue detail is explicitly illustration, not wiki content (Source-Type Handling: "empirical illustrations inside theoretical works are illustrations, not findings").

**Suggested improvement:** In the ingest workflow, make explicit that for theoretical/comparative treatises the main thread should pre-identify the 1–2 "payload" chapters and author their pages from direct reads in parallel with extraction, and that partial empirical-chapter coverage is acceptable-by-design (no gap-fill) when those chapters are illustration. This prevents both the reflex to gap-fill every flagged range and the mistake of promoting illustrative cases onto subject-matter pages.

**Principle:** Match extraction depth to where a source's *reusable knowledge* actually concentrates, not to uniform page coverage. For argument-driven works, the argument chapters deserve main-thread authorship; the evidence chapters deserve only enough mining to supply generalizations and exemplars.

### Observation 92: Tracker files can be fully rebuilt mid-session, breaking line-anchored ✅ marks

**Date:** 2026-07-10
**Session context:** Ingesting Higham, *The Archaeology of Mainland Southeast Asia* (1989) into the Social Sciences wiki, concurrent with other ingest sessions.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md Step 6 bookkeeping)
**Type:** internal
**Phase/Area:** Step 6 — Outstanding sources.md ✅ marking

**Issue:** I marked the matching line in `Outstanding sources.md` early (line 94, "94. Higham — ...1989."). Later in the same session the entire file was rebuilt/renumbered by the user or a linter (a "deepening pass" that retired the old 100×3 list and renumbered every item). My ✅ was on a now-defunct line; the rebuilt file listed Higham differently (arch item #2, offering the 1989 book as an alternative to the 2002 volume). I had to re-grep and re-mark. A blind trust that "I already marked it" would have left the ingest unmarked on the live roadmap.

**Suggested improvement:** In the ingest bookkeeping step, do the `Outstanding sources.md` ✅ mark LATE (just before final close), not early — and immediately before closing, re-grep the author surname to confirm the mark is present on the current file, since the roadmap is user-maintained and may be rebuilt mid-session. Treat the roadmap as mutable like `raw/`.

**Principle:** User-maintained checklist/roadmap files are not append-only and can be wholesale-rewritten by the user or a linter during a long session; any bookkeeping mark keyed to a line number or item number must be re-verified by content (grep for the entity) at close time, not assumed persistent from an earlier write.

### Observation 93: Intake check must verify content *identity*, not just word-count length

**Date:** 2026-07-10
**Session context:** "Ingest the archaeology of southern Africa" — the source PDF (labeled Mitchell, *Archaeology of Southern Africa*; archive.org ID archaeologyofsou0000mitc; embedded PDF title "The archaeology of southern Africa") in fact contained the full text of M. Anne Pitcher, *Transforming Mozambique* (2002) — a completely different book. Zero archaeology content across all 328 pp / ~141k words.
**Skill:** CLAUDE.md ingest workflow (Step 1 word-count intake check) — project-specific, but the principle generalizes to any document-ingestion skill.
**Type:** internal
**Phase/Area:** Step 1 scaffold / word-count intake check

**Issue:** The CLAUDE.md intake protocol's "word-count intake check" is framed entirely around *truncation* (epub→txt capturing only Part One; ratio of words to expected page count). It caught nothing here because the file was full-length — it was simply the wrong book. What actually caught the mislabel was an ad-hoc content grep (searching for domain-marker terms: "Stone Age", "Khoisan", "rock art", "hunter-gatherer" → zero hits; "Mozambique" → 1,172 hits; index/back-cover confirmed Pitcher). Filename, embedded PDF title, and archive.org ID were ALL consistent with the wrong label — no metadata signal would have caught it.

**Suggested improvement:** Extend the Step-1 intake check from a length check to a length-AND-identity check: after word-count intake, run a cheap content-identity probe — grep the body for a handful of domain/topic markers the source is *expected* to contain (author surname, subject keywords, key place/person names from the title). Zero hits on expected markers = wrong or corrupt content, even at correct length. Costs one grep; catches catastrophic mislabeling that the length ratio cannot. Collections sourced from shadow-library scans (z-library etc.) are especially prone to bound-with-wrong-text-layer errors.

**Principle:** A document can be complete and still be the wrong document. Intake validation that only measures *quantity* (length/truncation) misses *identity* failures. Always confirm the ingested text is *about what its label claims* with a cheap positive-marker probe before scaffolding — filename and embedded metadata can all agree and all be wrong.

### Observation 94: Five-agent Gender Trouble batch completed 5/5 without dropout; theoretical-work ingest kept all integration on main thread

**Date:** 2026-07-10
**Session context:** Deployed-subagent ingest of Butler, *Gender Trouble* (1990/1999), ~85k words / 256 pp, into the Social Sciences wiki.
**Skill:** CLAUDE.md ingest workflow (deployed-subagent strategy)
**Type:** internal
**Phase/Area:** Step 3 spawn + Step 4 integration

**Issue:** A dense theoretical monograph (feminist philosophy) was split into 5 disjoint line-ranges (prefaces / ch1 / ch2 / ch3a / ch3b+conclusion), one Sonnet extractor each, fired in one wave. All 5 claims files landed non-empty; no silent dropout. Because it is a theoretical work (all claims attributed by definition) and the pages are central/contested, integration was kept entirely on the main thread rather than delegated — 6 pages created + 6 existing updated with minimal attributed reception notes. No entity mismatches survived review; one interlocutor-heavy set (Wittig, Irigaray, Kristeva, Lacan, Rubin, Newton) was correctly handled as attributed prose with no pages, avoiding broken links.

**Suggested improvement:** Continue treating the batch-completion counter as evidence that one-wave dispatch of ~5 agents is reliable for ~250-page dense works. Reinforce: for theoretical works, main-thread integration is the right default (not a fallback) because every claim is attributed and the four-way-non-identity / theory-as-fact risks concentrate on exactly the central pages.

**Principle:** Agent count should track *body density and page-centrality*, not just length; and delegation of integration should be declined, not merely allowed to lapse, when the whole page set is high-stakes attributed theory.

### Observation 95: Non-English-translation source — flag paraphrase-of-translation, don't skip

**Date:** 2026-07-10
**Session context:** Ingest of Bourdieu, *Homo Academicus* — the only copy on disk was the Brazilian **Portuguese** translation of the French original, not the standard English (Collier) edition the wiki cites.
**Skill:** Social Sciences wiki CLAUDE.md ingest workflow
**Type:** internal
**Phase/Area:** Step 1 scaffold / extractor briefs / source-page reliability_notes

**Issue:** The source was a translation-of-a-translation (FR→PT), so any "verbatim quote" pulled by extractors is doubly mediated and cannot be presented as the author's canonical wording. Handled by: (a) instructing every extractor to extract in English but flag all quotes as "paraphrase-of-translation," (b) recording the extraction-language mismatch prominently in the source page `reliability_notes` and edition-history section, (c) using canonical English concept names (from the standard Bourdieu literature) for slugs/pages rather than transliterating the Portuguese. Worked cleanly; no canonical-wording errors leaked into wiki-voice.

**Suggested improvement:** Add a one-line note to the Source-Type Handling / ingest checklist: when the ingested copy is a translation into a language other than the wiki's citation language, (1) flag paraphrase-of-translation in every extractor brief, (2) note extraction-language in `reliability_notes` + edition history, (3) map to canonical (English) concept/term names, not transliterations. This is distinct from the existing English-translation-of-a-foreign-original convention already handled routinely.

**Principle:** A source's language is a reliability fact. Extraction from a non-citation-language translation is fine and should never be skipped, but the mediation must be surfaced (paraphrase-of-translation flag + reliability note) so downstream readers never mistake a re-translated phrase for the author's canonical wording.

### Observation 96: Ingest end-phase is serialized — redundant full-vault validation + one-round-trip-per-bookkeeping-step

**Date:** 2026-07-10
**Session context:** Ingest of Collins, *Black Feminist Thought* (deployed-subagent workflow). User flagged that the post-extraction phase "takes forever" even though the subagents themselves were fast.
**Skill:** CLAUDE.md ingest workflow (Steps 4–6); task-observer general
**Type:** internal
**Phase/Area:** Integration + Validate + Bookkeeping (deployed Steps 4–6)

**Issue:** After the 6 extractors finished, wall-clock was dominated by avoidable serialization, not by the writing itself: (1) the whole-vault validator (`check.sh`, ~3,585 pages) was run THREE times — scoped `--only`, then full, then a separate `check_wikilinks --compare` — despite CLAUDE.md's explicit "run validators ONCE, chained; do not re-run a clean validator." (2) Bookkeeping was split into ~7 sequential Bash round-trips (check trackers, mark Outstanding, append log, inspect Structural, append Structural, append index, file source), each its own latency wait. (3) Confirmatory greps/`tail`s were run before edits to inspect format that was already known. (4) The 12 page writes were issued one-per-message rather than batched in parallel.

**Suggested improvement:** Codify an end-phase fast path in the ingest workflow: (a) author independent new pages in PARALLEL batches (multiple Write calls per message); (b) do ALL bookkeeping in ONE combined Bash script — mark Outstanding + append log + append Structural + append index + `mv` the source out of raw/ — not seven calls; (c) run the full `check.sh` EXACTLY once at the very end (take the `--baseline` at session start, compare once), never scoped-then-full-then-compare; (d) skip confirmatory greps for file formats already seen this session.

**Principle:** In a workflow with a fixed, well-understood tail (validate + bookkeeping), the tail should be a single batched operation, not a step-by-step interactive dialogue with the filesystem. Each independent tool call issued alone costs a full round-trip; the whole-repo validator is the single most expensive action and must run once. Latency compounds invisibly — 10 avoidable round-trips + 2 redundant full scans feel like "working in slow motion" to the user even when total token/compute cost is modest.

### Observation 97: A tracker ✅ ingest mark is not proof the wiki content exists — verify pages, not the checklist
**Date:** 2026-07-10
**Session context:** Ingesting Willis, *Learning to Labour*. At session start `Outstanding sources.md` item 42 already carried "✅ ingested 2026-07-10 (source page present; root PDF filed raw/sociology/ this session — bookkeeping repair)" and the PDF was already moved out of raw/ root — yet the folder-agnostic duplicate pre-scan found NO willis wiki pages at all (source/study/thinker/concepts all absent). A prior (cleared) session had filed the PDF and marked the tracker without building any wiki content.
**Skill:** Social Sciences wiki CLAUDE.md ingest workflow (Step 1 duplicate-page pre-scan / Step 6 bookkeeping) — internal.
**Type:** internal
**Phase/Area:** Step 1 scaffold / pre-scan; interaction with Step 6 tracker marks.

**Issue:** A ✅ "ingested" mark plus a filed PDF can exist while zero wiki pages have been written (a bookkeeping-repair or interrupted prior session). An agent that trusts the tracker mark as evidence of completion would wrongly skip the ingest or treat it as "already done." Only the folder-agnostic `find wiki -name "<slug>.md"` pre-scan revealed the pages were missing.
**Suggested improvement:** In Step 1, state explicitly: the source-existence signal is the **wiki pages on disk** (via the folder-agnostic pre-scan), never the tracker ✅ or the PDF's location. When a tracker already shows ✅ but the pre-scan finds no pages, treat it as an incomplete/aborted prior ingest and proceed to build content; then reconcile the tracker note to reflect the real state.
**Principle:** Bookkeeping and content can drift out of sync in either direction. Completion must be verified against the artifact that matters (the pages), not against the record that is supposed to describe it. A checklist mark is a claim, not proof.

### Observation 98: Parallel tesseract OCR must set OMP_THREAD_LIMIT=1 and parallelize pdftoppm rendering by page ranges

**Date:** 2026-07-10
**Session context:** Bourdieu *State Nobility* ingest — 499-page image-only PDF OCR intake
**Skill:** New skill candidate / extends CLAUDE.md OCR guidance (obs 38, 62 lineage)
**Type:** open-source
**Phase/Area:** Source intake / OCR pipeline

**Issue:** Two successive OCR pipeline stalls: (1) serial pdftoppm rendered ~7s/page (would take ~1 h for 499 pp) — fixed by splitting into 12 parallel -f/-l page-range chunks (finished in ~3 min); (2) GNU parallel -j 11 tesseract produced load average 53 on 12 cores and ~7 pages/min because each tesseract spawns ~4 OpenMP threads (11×4 threads thrashing 12 cores).

**Suggested improvement:** Canonical image-PDF intake recipe: parallel pdftoppm by page ranges (seq 1 N step | parallel pdftoppm -f {} -l {end}), then OMP_THREAD_LIMIT=1 parallel -j <cores-1> tesseract. Also write a todo-list of missing txt files before (re)launching so restarts skip done pages.

**Principle:** When parallelizing tools that are themselves multi-threaded, cap their internal thread pools to 1 — outer parallelism × inner threads must not exceed core count, or throughput collapses below serial speed.

### Observation 99: Chapter-boundary spillover flags read as gaps — cheap verbatim cross-check resolves them

**Status:** OPEN
**Date:** 2026-07-10
**Session context:** Ingest of Powell & DiMaggio, *The New Institutionalism in Organizational Analysis* (1991); 8 range-partitioned extractors
**Skill:** CLAUDE.md ingest workflow (deployed subagent strategy)
**Type:** internal
**Phase/Area:** Step 3 completion inventory / gap recovery

**Issue:** 6 of 8 extractors flagged "coverage gap — chapter cut off mid-argument at my range boundary" in their completion summaries. Every one of these was chapter-boundary spillover already covered by the adjacent range (ranges were disjoint and contiguous by design); only one flag (range 2 stopping ~280 lines early by choice) was a genuine shortfall, and even that turned out to be low-value front-matter of the next chapter. The main thread spent a read cycle verifying each flag.

**Suggested improvement:** In extractor prompts, distinguish two completion codes: (a) "range fully read; final chapter continues past my upper bound" (expected, no action) vs (b) "stopped before my upper bound" (genuine gap, needs recovery). Instruct agents to state which applies and the exact last line read. The main thread then only investigates (b).

**Principle:** When work is partitioned by disjoint contiguous ranges, boundary spillover is the expected case, not an anomaly — make agents classify their own stopping condition so the orchestrator's inventory only escalates true shortfalls.

### Observation 100: User flags ~30-min ingest wall-clock as too slow — identify irreducible vs cuttable time per ingest

**Status:** OPEN
**Date:** 2026-07-10
**Session context:** Powell & DiMaggio 1991 ingest (~23 min gate-to-gate; scanned PDF requiring ~7 min OCR)
**Skill:** CLAUDE.md ingest workflow (deployed subagent strategy)
**Type:** internal
**Phase/Area:** Overall wall-clock / user expectations

**Issue:** User complained about session length ("half an hour again"). Breakdown: OCR ~7 min (irreducible for scans), extraction wave ~4 min, integration wave ~5 min, main-thread claims review ~5 min, hub authoring + validation + bookkeeping the rest. Recurring feedback — user memory already records a speed/lean-execution preference.

**Suggested improvement:** (a) For well-structured anthologies with clean extractor summaries, replace full main-thread reads of every claims file with summary-skim + spot-check; (b) offered user a CLAUDE.md toggle to defer mandatory hub pages to explicit request — apply whichever they choose; (c) state expected wall-clock up front when a source is a scan (OCR tax) so long runs are anticipated, not discovered.

**Principle:** When a user repeatedly flags duration, decompose wall-clock into irreducible vs discretionary components and offer the discretionary cuts as explicit defaults — silence about expected duration reads as slowness.

### Observation 101: Extractors can invent relations BETWEEN correctly-identified entities — verify relational claims, not just identities

**Status:** OPEN
**Date:** 2026-07-10
**Session context:** Ingest of Firth, Primitive Polynesian Economy (1939)
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Step 4a claims review)
**Type:** internal
**Phase/Area:** Extraction subagent output / claims review

**Issue:** A Sonnet extractor, despite the standing entity-mismatch instruction, glossed a footnote citation of "J. R. Firth, Speech" as Raymond Firth's "brother" — the source says nothing of the kind (J. R. Firth the linguist was unrelated). The entities were both correctly identified; the invented content was the *relationship* between them. The claim nearly propagated into a hub page.

**Suggested improvement:** In Step 4a claims review, spot-verify not only entity identities and grounding quotes but any RELATIONAL claim (kinship, teacher/student, institutional ties) an extractor asserts between named persons when it is not backed by a grounding quote. Extraction prompts could add: "state relationships between named persons only if the text states them."

**Principle:** Confabulation risk concentrates where extractors add connective tissue between correct facts; grounding-quote discipline covers claims but not the glosses attached to them.

### Observation 102: Disambiguate ethnonyms that collide with vault-unique slugs

**Status:** OPEN
**Date:** 2026-07-10
**Session context:** Ingest of Gluckman *Politics, Law and Ritual* — Colson’s Plateau Tonga claims vs existing Polynesian `tonga.md`
**Skill:** New skill candidate: wiki-ingest (internal) / CLAUDE.md ingest pre-scan
**Type:** internal
**Phase/Area:** Step 1 duplicate-page pre-scan / society naming

**Issue:** Pre-scan showed `wiki/societies/tonga.md` EXISTS. Claims agents and integrators for African “Tonga” (Colson/Gluckman) would have appended Central African material to the Polynesian Tuʻi Tonga polity page if the bare ethnonym were used as the slug. Folder-agnostic existence checks alone are insufficient: the *entity* behind a shared ethnonym must be verified (region, language family, documenter).

**Suggested improvement:** In CLAUDE.md ingest Step 1 pre-scan, for society/culture ethnonyms that exist, require a one-line entity check (region + type) before locking the slug; if mismatch, create a disambiguated slug (`plateau-tonga`, etc.) and ban bare `[[tonga]]` for the other entity. Add to standing subagent instructions: “If an ethnonym matches an existing page but the region/documenter differs, file under Miscellaneous with proposed disambiguated slug.”

**Principle:** Vault-unique filenames prevent link breakage but do not prevent *entity* collisions when the same ethnonym names unrelated peoples; existence of a slug is not identity of referent.

### Observation 103: User again flags ingest pace mid-bookkeeping — bookkeeping tail is the slow phase to compress

**Status:** ACTIONED — Batching rule added to CLAUDE.md Ingest Step 6 (2026-07-10, user-confirmed diagnosis)
**Date:** 2026-07-10
**Session context:** Douglas *How Institutions Think* ingest (2-agent lean run; extraction+integration fast, ~15 tool-round bookkeeping tail)
**Skill:** CLAUDE.md ingest workflow (Step 6 bookkeeping); relates to Observation 100
**Type:** internal
**Phase/Area:** Step 6 bookkeeping / tracker edits

**Issue:** User sent "speed it up, you're lollygagging again" during the bookkeeping phase. Extraction (2 agents, ~3 min) and integration were quick; the tail cost came from serial small reads/edits of trackers (Read-before-Edit failures, grep-then-read-then-edit loops for Outstanding sources), plus separate index/log/tracker steps.

**Suggested improvement:** Batch all bookkeeping into one or two Bash heredoc appends + a single python in-place edit where possible; for tracker line-marking, use a python one-liner (read/replace/write) instead of Read+Edit tool round-trips, since trackers are append/mark-only files the session owns the diff for.

**Principle:** The user's perceived latency concentrates in long tails of small serial tool calls, not in the parallelized heavy lifting; compress the tail by batching file mutations into single scripted operations.

### Observation 104: Concurrent sessions ingested the same source in parallel

**Status:** OPEN
**Date:** 2026-07-10
**Session context:** Ingest of Gluckman, *Order and Rebellion in Tribal Africa* (1963)
**Skill:** New skill candidate / CLAUDE.md ingest workflow
**Type:** internal
**Phase/Area:** Step 1 scaffold / session start

**Issue:** Two live sessions independently ingested the same book simultaneously (4-agent and 5-agent extractions, separate caches). Both wrote the source page, both updated gluckman-max (now carries two overlapping Order-and-Rebellion sections), both did bookkeeping. Content was mostly complementary thanks to Edit-append discipline, but a merge pass is needed and effort was duplicated wholesale.

**Suggested improvement:** Add a claim-the-ingest step to the ingest workflow: at Step 1, before scaffolding, check whether the source page slug already exists or whether a session-claim marker (e.g., a line in Structural_Sources or a lockfile in scratchpad-visible location like the wiki root) is present; if so, stop and ask the user. Symmetrically, write the source-page stub as the very first artifact so the sibling session's check can see it.

**Principle:** In multi-session wikis, the source page doubles as a lock; create it first and check for it first — Edit-append discipline limits damage but does not prevent duplicated whole-ingest effort.

### Observation 105: Extraction agents give internally contradictory coverage self-reports

**Status:** OPEN
**Date:** 2026-07-11
**Session context:** Clifford *Predicament of Culture* ingest; range-3 agent reported covering "lines 1–~2600" yet flagged sections that actually lie before line 2600 as unread, so the main thread could not trust the stated boundary and re-read lines 2000–3158 to be safe.
**Skill:** CLAUDE.md ingest workflow (Step 3 standing instructions)
**Type:** internal
**Phase/Area:** extraction coverage reporting / gap recovery

**Issue:** The "report actual coverage" instruction yields a line number estimated after the fact; when it conflicts with the agent's own list of unread sections, the main thread must over-read to recover safely.

**Suggested improvement:** In extraction prompts, ask agents to report the LAST HEADING OR QUOTED LINE they actually read (verbatim), not an estimated line number — a verbatim anchor is checkable with grep and cannot be mis-estimated.

**Principle:** Self-reported numeric progress from an agent is unverifiable; a verbatim content anchor is. Prefer checkable anchors over estimates in any completion report.

### Observation 106: Integration subagents emit `[[folder/]]` placeholder wikilinks that break the checker

**Date:** 2026-07-15
**Session context:** Ingest of Stocking, *After Tylor* (1995) into the Social Sciences wiki. Two integration subagents wrote the placeholder link `[[debates/]]` when flagging a candidate future debate page (Spencer–Gillen ethnographic reliability), producing 2 new broken links that `check_wikilinks.py` caught.
**Skill:** Social Sciences wiki CLAUDE.md (deployed-subagent ingest workflow)
**Type:** internal
**Phase/Area:** Step 4b integration subagent prompts / Step 5 validation

**Issue:** When a subagent wants to note that material *could* become a future `debates/` (or other folder) page, it reaches for a bracketed `[[debates/]]` form, which the wikilink checker parses as a broken link to a non-existent `debates/` slug. This is the same class as the existing CLAUDE.md guidance against bracketing descriptive phrases, but the folder-with-trailing-slash placeholder is a distinct recurring variant.

**Suggested improvement:** Add one line to the standing integration/extraction subagent instructions: "To point at a folder or a not-yet-created page as a *candidate*, write it as inline code (``debates/``) or plain prose — never as a bracketed wikilink `[[debates/]]`, which the checker counts as broken."

**Principle:** Wikilink brackets should be reserved for real, resolvable targets; any "this could become a page" gesture must use non-link syntax, or it manufactures broken-link noise that the validator then forces the main thread to clean up.

### Observation 107: Duplicate-page pre-scan must grep the *composite* concept slug, not just its parts

**Date:** 2026-07-15
**Session context:** Ingesting Stocking, *Race, Culture, and Evolution* (1968) into the Social Sciences wiki. Essay 1 is the famous "presentism vs. historicism" methodology piece.
**Skill:** Social Sciences wiki ingest workflow (CLAUDE.md, Step 1 duplicate-page pre-scan) — New rule candidate for the wiki, not an open-source skill.
**Type:** internal
**Phase/Area:** Step 1 scaffolding — duplicate-page pre-scan

**Issue:** The pre-scan `find`-checked candidate slugs `presentism` and `historicism` (both MISS) and I created `concepts/presentism.md`. But the canonical page already existed as `concepts/presentism-and-historicism.md` (built from Victorian Anthropology 1987), linked as `[[presentism-and-historicism]]` from six pages. I created a duplicate. Caught during validation because the Stocking thinker page's `[[presentism-and-historicism]]` links and my new `[[presentism]]` links pointed at two different slugs. Fix: merged my (richer, origin-grounded) content into the canonical page, added `aliases`, deleted the duplicate, repointed my links. This is the same class as the documented `ancestral-polynesian-society` duplicate trap, but a *different mechanism*: not folder-blindness — slug-composition-blindness. A concept commonly named as an "X and Y" / "X vs Y" pair lives under a composite slug that a single-word check will never hit.

**Suggested improvement:** In the CLAUDE.md Step-1 duplicate pre-scan guidance, add: for any concept expressible as a paired/compound term (X vs Y, X and Y, X-and-Y), also grep the composite slug and both single terms (`grep -rl "presentism" wiki/` catches the composite via substring), not just the individual heads. A cheap `grep -ril "<head-term>" wiki/concepts` substring scan before creating a concept page would have surfaced `presentism-and-historicism.md` immediately.

**Principle:** Existence checks for a new page must match how the vault actually *names* the entity, which may be a composite of the terms you searched. When the head term is a substring of a longer canonical slug, an exact-filename `find` gives a false "missing." Prefer a substring `grep -ril` over exact `find` for the concept pre-scan; the cost is one extra grep, the saving is a merge-and-delete cleanup mid-integration.

### Observation 108: Bash-read pages still trip the Edit precondition mid-integration

**Date:** 2026-07-15
**Session context:** Ingest of Abu-Lughod, *Do Muslim Women Need Saving?* (2013)
**Skill:** New skill candidate: none — CLAUDE.md ingest workflow
**Type:** internal
**Phase/Area:** Step 4b integration

**Issue:** The thinker page was previewed via Bash (sed) during scaffolding, then Edit calls on it were rejected ("File has not been read yet") at integration time, costing a retry round-trip. CLAUDE.md already documents the rule ("open with the Read tool, not Bash cat"), but the violation happened anyway because the Bash preview occurred long before the edit.

**Suggested improvement:** In the ingest workflow, when a page is previewed via Bash during pre-scan/scaffold AND is on the update manifest, immediately Read it with the Read tool at claims-review time (batch all manifest Reads in one parallel call) rather than relying on remembering at edit time.

**Principle:** Documented rules that fire at a different workflow moment than the mistake need a structural anchor (batch the Reads at manifest-lock time), not louder documentation.

### Observation 109: Cap extraction ranges at ~2,500 lines for Sonnet extractors

**Date:** 2026-07-15
**Session context:** Scott, Domination and the Arts of Resistance ingest (4-agent extraction)
**Skill:** CLAUDE.md ingest workflow (internal)
**Type:** internal
**Phase/Area:** Step 2 — chunk sizing

**Issue:** The one range sized at ~3,100 lines (range 3) stopped at ~59% coverage (read cap), while all ~2,100–2,600-line ranges completed fully. The "report actual coverage" standing instruction caught it and a scoped gap-fill agent recovered cleanly, but it cost a serial recovery round.

**Suggested improvement:** In the deployed-subagent workflow, treat ~2,500 lines as the practical per-agent ceiling (not the documented 2,000–3,500 band's top end); split denser ranges rather than letting one exceed it.

**Principle:** Size ranges to the extractor's observed read capacity, not the nominal band — the coverage-report instruction is the detector, but right-sizing avoids the recovery round entirely.

### Observation 110: Bookkeeping idempotency guards must use a precise anchor, not a loose substring

**Date:** 2026-07-15
**Session context:** Ingesting Haraway, *Staying with the Trouble*, with a concurrent Strathern/Viveiros ingest session active in the same vault.
**Skill:** Social Sciences Wiki CLAUDE.md (deployed-subagent ingest, Step 6 bookkeeping)
**Type:** internal
**Phase/Area:** Step 6 bookkeeping — scripted batch appends to Structural_Sources.md / log.md / index.md

**Issue:** My batch bookkeeping script guarded each append with `if "Staying with the Trouble" not in file` to avoid double-writing. Both the Structural_Sources and log guards falsely tripped ("already present") because a *concurrent* session's Strathern entry, and its own log line, mentioned the phrase "concurrent *Staying with the Trouble* session also active." The loose substring matched the other session's text, so my real entries were silently skipped; only a post-write `grep -c` on my entry's exact format caught it, and I re-ran with a precise anchor.

**Suggested improvement:** In the CLAUDE.md Step 6 batch-bookkeeping guidance, add: idempotency checks for "already wrote this entry?" must key on a **precise anchor unique to your own entry** (e.g. `"Haraway, *Staying with the Trouble"` in the exact Structural bullet format, or `"ingest | <Title>"` in the log line format), never a bare title substring — because concurrent sessions routinely *mention* your source title in their own notes. Always follow the batch with a `grep -c` verification of each entry's exact format.

**Principle:** In a shared, concurrently-written workspace, "does my write already exist?" and "does this string appear anywhere in the file?" are different questions. Presence-of-substring is a false proxy for presence-of-my-entry whenever other writers can reference the same identifiers. Guard on the entry's own canonical format and verify after writing.
