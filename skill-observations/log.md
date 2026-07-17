# Skill Observation Log

Observations captured during task-oriented work. Each entry identifies a
potential skill improvement or new skill opportunity.

**Status key:** OPEN = not yet actioned | ACTIONED = skill updated/created |
DECLINED = user decided not to pursue

---

## Active — resolved in weekly review 2026-07-16

These stay visible one cycle (archival-on-write moves them on the next session write).

### Observation 6: Concurrent full-session ingests create overlapping/duplicate canonical pages invisible to the wikilink checker
**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-08
**Session context:** Ingesting Weber *Politics as a Vocation* while a **separate parallel session was simultaneously ingesting Weber *Economy and Society***. Mid-ingest, my newly-created concept pages (`charismatic-authority.md`, `bureaucracy.md`) were edited by the other session to add authority-family `related_concepts` links, and it created `concepts/domination-herrschaft.md`, `concepts/charisma.md`, `traditional-authority.md`, `legal-rational-authority.md`, and a `concepts/rationalization.md` that duplicates the pre-existing `phenomena/rationalization.md`.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md — duplicate-page pre-scan, concurrent-session Edit-append rule, Naming Conventions vault-unique slugs)
**Type:** internal
**Phase/Area:** Step 1 duplicate pre-scan / Step 4 reconcile / lint

**Issue:** Two independent full sessions on the same author (Weber PaV + Weber E&S) independently created **overlapping canonical concept pages** the wikilink checker cannot flag because both targets resolve: my `legitimate-domination` (tripartite typology, with traditional/legal-rational covered *within* it) vs. the other session's `domination-herrschaft` (umbrella) + separate `traditional-authority` + `legal-rational-authority`; and my `charismatic-authority` vs. its `charisma`. The other session also duplicated `rationalization` (concept vs. existing phenomenon), producing a duplicate-slug lint ERROR and ~20 "ambiguous [[rationalization]]" warnings that bleed into my pages' links. CLAUDE.md's duplicate pre-scan (Step 1) only scans the *existing* vault; it cannot anticipate a *sibling session* creating the same entities in parallel. The Edit-append-not-Write rule protected existing pages but not the new-page namespace.

**Suggested improvement:** Add a note to CLAUDE.md Ingest Step 1/Step 4: when the same author/topic may be under concurrent ingest (multiple works from one thinker queued in `raw/`), (a) before scaffolding, agree a shared concept-slug convention for shared theoretical vocabulary (e.g. one canonical `domination-*`/authority-types scheme) or check for a sibling session's just-created pages by `ls`-ing `wiki/concepts` immediately before creating each new page; (b) at Step 4/lint, explicitly grep for near-synonym duplicate slugs created since session start (author's core concepts), since the wikilink checker passes them; (c) treat cross-session concept duplication (charisma/charismatic-authority, domination-herrschaft/legitimate-domination, rationalization concept/phenomenon) as a mandatory post-ingest merge item to surface to the user, not a silent pass.

**Principle:** Duplicate-canonical-page risk is highest not from a single session but from **concurrent sessions on the same author** — both resolve, so the wikilink checker is blind to it; only a same-session near-synonym grep plus an explicit "did a sibling session just create this?" check catches it. Links [[Observation 1 — source_type mixed]] only loosely; this is a concurrency/duplication defect, not an enum defect.



### Observation 8: OCR "first edition" texts may silently be revised editions

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-08
**Session context:** Ingest of Cooley *Human Nature and the Social Order* — Abika/public-domain OCR labeled and queued as 1902
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md source reliability / Chronological Uncertainty)
**Type:** internal
**Phase/Area:** Step 1 intake + source page reliability_notes

**Issue:** The source was filed and scaffolded as Cooley 1902 (first publication year). During extraction, claims flagged material impossible in a pure 1902 text: "we entered the war in 1917" / Argonne, citation of Sumner *Folkways* (1906), WWI Germans example, psychoanalysis end note. Standard scholarly fact: Cooley issued a revised *Human Nature* (1922). Treating the file as pure first edition would misdate claims and mislead chronology hygiene (theories dated by key-text publication vs later revision).

**Suggested improvement:** In CLAUDE.md Source-Type Handling or ingest Step 1 intake check, add: "For public-domain OCR monographs, scan for post-first-edition markers (war dates, later works cited, copyright lines, 'revised edition') before locking frontmatter `year`. Prefer year = first publication with an explicit reliability_notes clause when the *text body* is a later revision; never silently attribute revised interpolations to the first-edition date."

**Principle:** Bibliographic year and *textual state* are different facts. OCR labels and queue names often encode first publication; body content may be a later edition. Edition identity belongs in reliability_notes at intake, not as a late surprise during claim integration.



### Observation 9: Subagent page-creation prompts must put ALL mandatory frontmatter fields literally in the YAML block, not in prose

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-08
**Session context:** Ingesting Simmel's *The Sociology of Georg Simmel* (Wolff 1950) via 10 deployed subagents; several agents owned new concept/institution pages and were given a YAML frontmatter block plus a prose instruction "fill all fields; sources_ingested: 1; last_updated: 2026-07-08".
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md — Ingest Workflow Step 3 subagent prompts)
**Type:** internal
**Phase/Area:** Step 3 (spawn extraction/page-writing subagents) / Step 5 (lint)

**Issue:** The literal YAML block handed to each page-owning agent did NOT contain `sources_ingested` or `last_updated` lines — those two fields were mentioned only in adjacent prose ("fill all; sources_ingested: 1; last_updated: 2026-07-08"). All 8 page-writing agents reproduced the YAML block verbatim and ignored the prose, producing 16 schema errors (2 per page) caught only at Step 5 lint. Agents copy the frontmatter block they are given and treat surrounding prose as commentary.

**Suggested improvement:** In Ingest Workflow Step 3, add a standing instruction: when a subagent is told to create a schema'd page, the prompt's YAML block must be COMPLETE and copy-pasteable — every mandatory field present with its value inline (including `sources_ingested`, `last_updated`, `tags`) — never rely on prose like "fill all fields" to supply a field absent from the block. The block the agent sees is the block the agent writes.

**Principle:** Subagents transcribe the concrete artifact they are given far more reliably than they synthesize from instructions about it. Any structure you need in the output should appear, complete, in the example — prose caveats around an incomplete template are silently dropped.



### Observation 11: Eight-agent Dahrendorf batch completed without silent dropout
**Status:** DECLINED — Positive 8-agent Dahrendorf success — evidence only; inventory checklist remains the enforcement (review 2026-07-16)
**Date:** 2026-07-08
**Session context:** Social Sciences Wiki ingest of Dahrendorf *Class and Class Conflict* — 8 parallel extractors over disjoint cache ranges
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors

**Issue:** Prior observations (3, 5) documented silent per-range dropout on 6–7 agent Weber/Capital batches. This Dahrendorf run used **8 agents** over ~21k body lines with mandatory filesystem inventory of expected claims paths. **All 8** wrote complete non-empty claims files (`range_1.md`…`range_8.md`, ~3300 lines total) within ~6 minutes; no main-thread recovery needed. Short multi-waits + filesystem inventory used as completion signal.

**Suggested improvement:** Record as a positive counter-case to Obs 3/5: dropout is not automatic at N=8; keep the inventory checklist as the enforcement mechanism rather than lowering default N. Optional: note that denser theoretical slices (~2–3.5k lines) completed reliably when ranges aligned to chapter boundaries.

**Principle:** Multi-agent reliability should be measured by **output inventory**, not assumed from batch size alone; successful large batches are evidence, not proof that silent death is gone — keep detection structural.



### Observation 13: Blumer SI range-2 silent dropout after Obs 3/5 "fixes" — rules not structurally enforced

**Status:** ACTIONED — Reinforced Step 3 filesystem inventory as structural enforcement; reliability note that documentation alone is not the fix (review 2026-07-16)
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

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-08
**Session context:** Ingesting Parsons *The Social System* while a **separate concurrent session ingested Gouldner *The Coming Crisis of Western Sociology***. Both ingests independently needed `theories/structural-functionalism.md` and `thinkers/parsons-talcott.md`. My pre-scan at scaffold time (Step 1) showed both slugs absent, so I planned full Writes. By integration time (~18 min later) the Gouldner session had created both. My `Write` to `structural-functionalism.md` failed with "File has not been read yet" — the harness's Edit/Write safety gate, not a duplicate-page error — which is what surfaced the collision. I switched to Read-then-Edit-append, and the two sessions' content converged cleanly (Parsons's apparatus in attributed voice alongside Gouldner's critique; index/Structural_Sources/hub-portal entries merged without duplication).

**Suggested improvement:** In the Social Sciences Wiki ingest workflow (CLAUDE.md Step 4 "concurrent ingest" guidance), add: the duplicate-page pre-scan in Step 1 is a *point-in-time* check and goes stale during a long extraction phase. Before creating any page you scaffolded as "new," re-check existence immediately before writing; if a `Write` to a supposedly-new page returns the Read-precondition error, do not force it — Read the file and Edit-append, because a concurrent session has created it. The "integrate with Edit-append, never full Write, when a concurrent session may touch the same pages" rule should extend to *page creation*, not just updates to already-existing pages.

**Principle:** In multi-session/multi-agent environments, "this page doesn't exist yet" is only true at the instant you check it. Any write that assumes exclusive creation must revalidate at write time and degrade gracefully to merge-mode; the tooling's own preconditions (a read-gate failure) are a cheap collision detector if you read them as such instead of retrying the write.



### Observation 17: Lipset Political Man 7-agent batch completed without silent dropout
**Status:** DECLINED — Positive 7-agent Lipset success — evidence only (review 2026-07-16)
**Date:** 2026-07-09
**Session context:** Social Sciences Wiki ingest of Lipset *Political Man* — 7 parallel extractors, disjoint ranges ~3100–6100 lines under `/tmp/pm_cache/`
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor extractors

**Issue:** Positive recurrence data after Obs 3/5/13 pattern: all 7 extractors wrote non-empty claims files (`range_1.md`…`range_7.md`, ~296 claims) within ~2–3 minutes; filesystem inventory before integration found zero missing ranges. Progress checklist + non-blocking multi-wait used; no user "are you frozen?" interrupt this session.

**Suggested improvement:** Keep documenting successful batch sizes (here 7, content-weighted, ~3–6k lines each) alongside failures so the default agent count is evidence-based rather than folklore "avoid 6."

**Principle:** Success cases are as informative as dropouts for calibrating parallel extraction batch size; log them so the workflow's risk model is not only failure-driven.



### Observation 21: Theoretical ethnographies can switch field sites mid-book without TOC warning
**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** Ingest of Bourdieu *The Logic of Practice* — Book II Ch.1 is **Béarn** (French peasant inheritance/adot), Ch.2–3 + Appendix are **Kabyle**. TOC lists Book II under practical logics without flagging the site switch; a naive brief that labels all Book II as Kabyle would mis-file society claims.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Deployed Subagent Strategy / society pages)
**Type:** internal
**Phase/Area:** Step 2 chunk briefs; society claim routing

**Issue:** Extractor range 4 correctly flagged Béarn material as entity-mismatch vs the established `kabyle` society slug and filed it under Miscellaneous/theory targets. Without that discipline, matrimonial-strategy claims would have been written onto the Kabyle society page in ethnographic voice for the wrong people.

**Suggested improvement:** In CLAUDE.md ingest guidance for multi-site theoretical monographs: when scaffolding society pages from a theory book's fieldwork, spot-read Book II / empirical chapters for site names (not only the Preface) and list **all** documented populations in the extractor brief. Instruct agents: if material is near-match to target society but site differs, file under Miscellaneous with mismatch flag (already a standing instruction — emphasize site-switching as a common trigger).

**Principle:** A book's best-known field site is not the only field site. Spot-read empirical chapters for place names before assigning society ownership; treat site switches as entity boundaries, not chapter flavor.



### Observation 23: Era-tag-as-wikilink and escaped-pipe-in-table are recurring, lint-catchable integration defects

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** Ingesting Collins *Conflict Sociology* (1975), 9-agent extraction. During integration I wrote `[[critical-turn|critical turn]]` (a disciplinary-era *tag*, not a wiki page) in three places and one `[[slug\|Display]]` escaped-pipe wikilink inside a markdown key-texts table cell in the theory hub. Both produced broken links caught only by the final `check_wikilinks` pass, requiring a fix-and-recheck cycle.

**Suggested improvement:** Add a pre-lint integration checklist item to the Social Sciences ingest workflow (CLAUDE.md Step 4/5 already warns about escaped pipes in tables and era-tags — but the enforcement is narrative). Before the first validator run, grep new/edited pages for two patterns: (a) `\[\[(precursors|founding-era|classical-era|fieldwork-revolution|postwar-expansion|critical-turn|contemporary)` (era tags wrongly linked), and (b) `\[\[[^]]*\\\|` (escaped-pipe wikilinks, which break in table cells). Both are 100%-mechanical and catchable in one grep before the full lint.

**Principle:** When a known, recurring authoring mistake has a mechanical signature, a targeted grep run *before* the expensive whole-repo validator is cheaper than the write→lint→fix→re-lint loop. Turn recurring lint failures into pre-flight greps.



### Observation 24: Deployed-subagent ingest robust under three simultaneous concurrent sessions via Edit-append

**Status:** DECLINED — Positive concurrent Edit-append robustness — collaborative framing applied via #122 cluster; no separate rule (review 2026-07-16)
**Date:** 2026-07-09
**Session context:** The Collins *Conflict Sociology* ingest (9 parallel extractors, all claims files landed, 663 claims, no silent dropout) ran while THREE other sessions concurrently ingested Putnam *Bowling Alone*, Elias *The Civilizing Process*, and Wallerstein *Modern World-System*. Shared pages (disciplines/sociology, disciplines/political-sociology coverage notes; institutions/the-state and phenomena/state-formation frontmatter; index.md lists; theory-hub portal) were touched by multiple sessions in the same window. Every shared-page edit used the Edit tool with unique anchors (never a full Write); all sessions' additions coexisted with no clobbering. The session-start `--baseline` snapshot plus final `--compare` cleanly attributed all NEW broken links to the *other* sessions' pages (Wallerstein/Bourdieu-Passeron), confirming this ingest introduced zero.

**Suggested improvement:** Reinforce in the ingest workflow that the `--baseline`/`--compare` wikilink pattern is not just for "a concurrent session may break links" but is the *only* reliable way to attribute broken links to the right session when 3+ run at once — and that a broken link in the final report pointing at a page you never touched is expected, not a defect to chase. Keep filtering `--compare` output by *your* page slugs.

**Principle:** Under heavy concurrency, correctness attribution matters as much as correctness: a session must be able to prove *its own* footprint is clean without being blocked by other sessions' in-flight breakage. Baseline-snapshot + slug-filtered compare gives per-session attribution.



### Observation 34: Grep-verify a planned concept page's term against the source before creating it

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** Ingesting Bonilla-Silva *Racism without Racists* (5th ed.). Step-1 scaffolding pre-named a `concepts/racial-grammar.md` page (Bonilla-Silva is associated with "racial grammar" from his other work). Extractors flagged the exact term never appears in this book; a full-text grep confirmed zero occurrences. The page was dropped to avoid importing outside knowledge, and stray `[[racial-grammar]]` links were cleaned from three scaffolded pages.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md — Step 1 scaffolding / no-outside-knowledge principle)
**Type:** internal
**Phase/Area:** Step 1 scaffold (pre-establishing linkable page names)

**Issue:** A scholar's signature concept (well-known from their broader corpus) was pre-scaffolded as a page name before confirming the term is actually present in the *ingested* source. Had extractors not flagged it, the page could have been created and filled with recalled (not source-grounded) content.
**Suggested improvement:** In Step 1, before committing a pre-named concept/theory page that rests on a specific coined term, grep the converted source text for that term. If it is absent, either drop the page or route its content into an adjacent page that IS grounded in the source — never create a term-page the source doesn't support.
**Principle:** Pre-scaffolding sets linkable names from prior knowledge of the author; that knowledge can outrun the specific source. A cheap grep against the source text keeps scaffolding honest and prevents outside-knowledge contamination — the same discipline the wiki enforces on subagents ("no outside knowledge") should apply to the main thread's scaffolding.



### Observation 35: Subagents must not run task-observer
**Status:** ACTIONED — Task-Observer Activation scoped to main agent only; standing negative in Step 3 prompts (review 2026-07-16)
**Date:** 2026-07-09
**Session context:** Ingest of Fenstermaker & West *Doing Gender, Doing Difference* — parallel extractors
**Skill:** task-observer (one-skill-to-rule-them-all); Social Sciences Wiki CLAUDE.md Task-Observer Activation
**Type:** internal
**Phase/Area:** Session-start / subagent prompts

**Issue:** User corrected mid-ingest: only the main agent should invoke the task-observer skill. Subagents that inherit CLAUDE.md's "invoke task-observer at start of any task-oriented session" instruction may waste time on observation-log protocol, weekly-review checks, and skill loading instead of bulk extraction. Extraction subagents are scoped workers (read cache slice → write claims file); meta-skill monitoring belongs on the orchestrating main thread.

**Suggested improvement:** (1) In CLAUDE.md Task-Observer Activation, scope the mandate to the main/orchestrating agent only — e.g. "Main agent only: at the start of any task-oriented session, invoke task-observer… Subagents and extractors skip task-observer unless the user explicitly asks them to improve a skill." (2) Standing line in every ingest extractor prompt: "Do not load or run task-observer / skill-observation protocols; main agent owns that."

**Principle:** Session-level meta-skills (observation logging, weekly review, skill hygiene) are orchestrator responsibilities. Scoped subagents should receive an explicit negative instruction when project CLAUDE.md would otherwise trigger expensive session-start rituals on every child.



### Observation 38: Image-only DuXiu PDFs need parallel tesseract pipeline (ocrmypdf can fail)

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** Ingest of Tavory & Timmermans *Abductive Analysis* (2014) — DuXiu/Anna's Archive image-only PDF, 179 pages, no text layer
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Source-Type / intake; PDF OCR path)
**Type:** internal
**Phase/Area:** Step 1 word-count intake / source text recovery

**Issue:** `pdftotext` returned only ~75 words (Anna's Archive wrapper). `ocrmypdf --skip-text` failed with SubprocessOutputError (tesseract "lots of diacritics" warnings; no output PDF). Working path: `pdftoppm -png -r 180` then `xargs -P 8 tesseract` per page, concatenate by page order → ~71k words (~28 min OCR). Session spent most wall-clock on OCR before any wiki writing.

**Suggested improvement:** In CLAUDE.md ingest Step 1 (or a methods note under scripts/README), document recovery for image-only social-science PDFs: (1) detect empty pdftotext; (2) prefer parallel pdftoppm+tesseract over ocrmypdf when ocrmypdf fails; (3) cache OCR text to `/tmp/*_cache/full.txt` and file as `raw/.../author-title-year.txt` after ingest; (4) budget 15–40 min for ~150–200 page DuXiu scans at 180 dpi.

**Principle:** Source intake is not complete when a PDF exists on disk — only when body text of expected length is recoverable. Image-only library scans are a first-class failure mode for ebook collections and need a documented, parallelizable OCR fallback, not ad-hoc rediscovery each ingest.



### Observation 40: Nine-agent Golden Bough batch completed 9/9 without dropout
**Status:** DECLINED — Positive 9-agent Golden Bough success — evidence only (review 2026-07-16)
**Date:** 2026-07-09
**Session context:** Ingest of Frazer *The Golden Bough* (1922 abridgement) — ~410k body words, 9 parallel extractors over disjoint cache ranges under `/tmp/golden_bough_cache/`
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3)
**Type:** internal
**Phase/Area:** Step 3 spawn/monitor/inventory

**Issue:** Prior observations (3, 5, 12) documented silent per-range dropout on multi-agent batches. This run used **9 agents** over ~27.5k body lines (~410k words) with expected claims paths `claims/range_1.md`…`range_9.md`. **All 9** wrote complete non-empty claims files (~504 claims total) within ~2–2.5 minutes; no main-thread recovery needed. Short multi-wait + filesystem inventory used as completion signal. User-visible checklist posted before spawn.

**Suggested improvement:** Retain as positive counter-case to Obs 12 (Blumer dropout): large-N + large-book success is possible when ranges are sized ~2.2k–4.2k lines, cache slices cut before spawn, and completion is filesystem-based. Do not treat as "fixed forever" — continue mandatory inventory before integration.

**Principle:** Stochastic silent-agent death is real; full-batch success at N=9 on a large theoretical work shows the failure is not automatic at high N or long slices, but inventory-before-integration remains non-optional regardless of success rate.



### Observation 44: Concurrent ingest of two books by one author — partition by page-ownership (cases/concepts vs. shared thinker/theory) makes it collision-safe

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** Ingesting Benedict *Patterns of Culture* (1934) while a second live session ingested Benedict *The Chrysanthemum and the Sword* (1946). Both books feed the same thinker page (`benedict-ruth`) and the same theory (`configurationism`).
**Skill:** Social Sciences Wiki CLAUDE.md — Ingest Step 4 (concurrent-session integration) / Observation 6
**Type:** internal
**Phase/Area:** Integration under concurrency

**Issue:** The collision was benign and productive, not destructive. The other session had *pre-linked* pages I had not yet created (`[[dobu]]`, `[[zuni]]`, `[[configurationism]]`, `[[cultural-relativity-of-normality]]`) and, when it re-authored `benedict-ruth`, *folded in* my Patterns scaffold content (sources_ingested went to 2, both books covered) rather than clobbering it. I detected the overlap early via the harness "file was modified" notes and switched from full Writes to Edit-append on every shared page (thinker, theory summary, culture-and-personality, cultural-relativism, anthropology), reserving full Writes for pages only I created (the three society pages, four concept pages, source, study, Theory Hub). Final validation: 0 new broken links, 0 errors.

**Suggested improvement:** Add to CLAUDE.md's concurrent-ingest guidance a positive pattern: when two sessions ingest different works by the *same* author/subject, the natural safe partition is **case/subject-matter + concept pages to one session, shared thinker/theory pages authored by whichever session created them, cross-linked by the other via Edit-append**. The early-warning signal is the harness "file modified by user/linter" note on a page you thought you owned — treat it as the trigger to stop full-Writing that page. Reciprocally, a session that *creates* a shared thinker/theory page should fold in (not overwrite) any scaffold content a peer session already wrote.

**Principle:** Concurrency is safe when authorship is partitioned by page, not by source-range. The "file modified" harness note is the cheapest available collision detector — react to it by demoting full Writes to Edit-append on that page. Two ingests of one author converge cleanly if each owns a disjoint page-set and only cross-links into the other's.



### Observation 45: Concurrent ingest left content done but bookkeeping incomplete
**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** User asked to ingest Radcliffe-Brown *Structure and Function*; concurrent session had already written source + concepts + hub densification but left log/index/Structural_Sources/filing unfinished and Primitive Law underextracted.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Ingest Workflow Step 6 Bookkeeping)
**Type:** internal
**Phase/Area:** Step 6 bookkeeping; multi-session / concurrent-session handoff

**Issue:** A concurrent (or prior same-day) session completed the hard part of a theoretical ingest — source page with Section Plan, 4 concept pages, Thinkers/Theory Hub densification — but did **not** complete Step 6: no `wiki/log.md` entry, no `index.md` block, no `Structural_Sources.md` ✅ row, PDF still in `raw/` root, no permanent `.txt` filing. One claims range (Primitive Law) was also flagged by extractors as outside brief and never main-thread recovered. The user request "ingest X" therefore hit an ambiguous mid-state: content looked ingested, apparatus said otherwise.

**Suggested improvement:** In CLAUDE.md Step 6 (or session-start for "ingest X"), add a **resume-incomplete-ingest checklist**: if `wiki/sources/[slug].md` exists with `ingested:` date but (a) no matching log line, or (b) source still in `raw/` root, or (c) not marked in Structural_Sources — treat as incomplete and finish bookkeeping before re-extracting. Also: never close an ingest session without the four-item bookkeeping set (log + index + Structural_Sources + file out of raw root), even if content pages are done.

**Principle:** Ingest completion is an apparatus fact (log/index/sources-list/filing), not only a content fact (pages exist). Concurrent sessions that write content without bookkeeping leave the next agent (and the user) unable to tell "done" from "half-done" without a full inventory.



### Observation 62: Image-PDF OCR via ocrmypdf fills /tmp and loses sidecar text

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-09
**Session context:** Social Sciences Wiki ingest of Ferguson *The Anti-Politics Machine* — 338-page image-only PDF
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md intake / PDF conversion); OCR pipeline
**Type:** internal
**Phase/Area:** Source intake — image PDF → text before word-count

**Issue:** First attempt used `ocrmypdf --force-ocr --rotate-pages --deskew --jobs 4 --sidecar` writing intermediates to /tmp (tmpfs ~5.8G). At ~page 269/338 Ghostscript hit "No space left on device"; pipeline exception; **sidecar text file remained 0 words** despite most pages having been OCR'd in temp. User-visible multi-minute wait then total failure. Recovery path: page-by-page pymupdf render (200 DPI) + tesseract, writing page texts under workspace `scratchpad/` (not /tmp), deleting PNGs immediately, stitching at end — completed 338/338 pages, ~124k words.

**Suggested improvement:** For image-only PDFs in this wiki: (1) prefer workspace-local temp (`scratchpad/tmp_ocr` or `TMPDIR` on the project disk), never rely on small tmpfs for 300+ page @400 DPI ocrmypdf; (2) prefer incremental page OCR with immediate image delete + stitch over single ocrmypdf sidecar when disk is tight; (3) lower DPI (200) is adequate for claim extraction; (4) document in CLAUDE.md or a local OCR note that ocrmypdf default /tmp can silently zero the text output on ENOSPC.

**Principle:** OCR pipelines that buffer full-resolution intermediates on a small tmpfs will fail late and can leave the *only* intended artifact (sidecar text) empty even after substantial work. Stream to durable storage page-by-page; treat completion as the stitched text file existing and non-empty, not as the OCR tool's exit code alone.




### Observation 79: Dual taxonomy for lithic industries reintroduced mid-ingest

**Date:** 2026-07-10
**Session context:** Ingest of Gamble *Palaeolithic Societies of Europe* (1999)
**Skill:** Social Sciences wiki ingest / CLAUDE.md taxonomy
**Type:** internal
**Phase/Area:** Integration / culture vs concept page ownership
**Status:** ACTIONED — Lithic industries taxonomy: concepts/ only, no cultures/*-industry dual pages (Naming Conventions) (review 2026-07-16)

**Issue:** Prior Klein ingest deleted cultures/mousterian-industry|aurignacian-industry|chatelperronian-industry to fold onto concepts/mousterian|aurignacian|chatelperronian (concurrent-session collision fix). A Stage-2 integrator for Gamble 1999 recreated the three cultures/*-industry pages with substantial densification, while concepts bare pages retain Stringer-Gamble/Klein layers. Dual taxonomy is now live again (also matches oldowan/acheulean cultures/*-industry pattern). Main thread added reciprocal pointers rather than deleting densification.

**Suggested improvement:** CLAUDE.md or a short taxonomy note should state the standing rule for lithic industries: either (a) cultures/*-industry for material constructs + concepts/ bare for classificatory history is allowed and preferred, or (b) concepts only — so integrators inherit one rule and do not thrash pages across sessions.

**Principle:** When concurrent sessions resolve taxonomy differently, later integrators need an explicit canonical rule on disk; otherwise densification work recreates the conflict the previous session solved.



### Observation 86: Scanned-image epub intake needs ordered-page OCR, not ebook-convert alone

**Date:** 2026-07-10
**Session context:** Ingest Cunliffe *The Ancient Celts* (scanned-image epub, 362 JPGs)
**Skill:** Social Sciences wiki ingest / CLAUDE.md intake
**Type:** internal
**Phase/Area:** Word-count intake / OCR recovery path
**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)

**Issue:** ebook-convert and pandoc produced empty/placeholder text for an image-only epub (page JPGs embedded in index.html). Word-count intake correctly flagged 0 words, but the recovery path had to be invented mid-session: extract reading order from HTML img src, filter large JPGs, parallel tesseract with OMP_THREAD_LIMIT=1, optional 2× upscale for low-res (~521×751) scans.

**Suggested improvement:** In CLAUDE.md word-count intake (or a pdf/epub intake note), document the **image-epub branch**: if ebook-convert/pandoc yield <1k words but the archive contains many large page images, run ordered-page OCR (HTML reading order → tesseract) rather than treating the source as empty. Note low-res scans benefit from 2× upscale + psm 3.

**Principle:** Zero-word conversion of a large epub is a format-detection signal (scanned images), not proof the book is unavailable — recovery is ordered OCR of the plate stream, not a different acquisition.



### Observation 88: Structural_Sources greedy regex dedupe destroyed ledger

**Date:** 2026-07-10
**Session context:** Carneiro Evolutionism ingest bookkeeping
**Skill:** Internal (Social Sciences Wiki CLAUDE.md / ingest bookkeeping)
**Type:** internal
**Phase/Area:** Step 6 bookkeeping — Structural_Sources.md updates
**Status:** ACTIONED — Structural_Sources single-bullet append / no multi-line regex dedupe in Step 6 (review 2026-07-16)

**Issue:** After inserting a Carneiro ledger entry, a Python regex meant to dedupe two Carneiro occurrences used a non-greedy-looking but actually over-broad DOTALL pattern that matched from the first Carneiro bullet through a huge mid-file span (second false "match" ~32k chars), deleting most of the top-of-file 2026-07-10 recent-ingest ledger. No git repo in the vault, so recovery required session terminal logs. Restored Renfrew/Kirch/Cunliffe/Wilkinson/Kemp + Carneiro at top; residual size still ~23k below pre-edit.

**Suggested improvement:** Never use multi-line regex to dedupe ledger entries. Prefer: (1) single-line exact-string checks before insert; (2) insert only at a known anchor (`## Recently ingested` or first `- **YYYY-MM-DD**`) with exact prefix match; (3) if dedupe needed, match only one line starting with `- **DATE** — ✅ Author, *Title`. Add CLAUDE.md rule: Structural_Sources edits must be single-bullet appends; verify file size/line-count within ~2% after edit; never run multi-match delete without dry-run size check.

**Principle:** Bookkeeping files that accumulate concurrent session writes need append-only discipline; destructive multi-match edits on shared ledgers are high blast-radius and need pre/post size assertions.



### Observation 99: Chapter-boundary spillover flags read as gaps — cheap verbatim cross-check resolves them

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-10
**Session context:** Ingest of Powell & DiMaggio, *The New Institutionalism in Organizational Analysis* (1991); 8 range-partitioned extractors
**Skill:** CLAUDE.md ingest workflow (deployed subagent strategy)
**Type:** internal
**Phase/Area:** Step 3 completion inventory / gap recovery

**Issue:** 6 of 8 extractors flagged "coverage gap — chapter cut off mid-argument at my range boundary" in their completion summaries. Every one of these was chapter-boundary spillover already covered by the adjacent range (ranges were disjoint and contiguous by design); only one flag (range 2 stopping ~280 lines early by choice) was a genuine shortfall, and even that turned out to be low-value front-matter of the next chapter. The main thread spent a read cycle verifying each flag.

**Suggested improvement:** In extractor prompts, distinguish two completion codes: (a) "range fully read; final chapter continues past my upper bound" (expected, no action) vs (b) "stopped before my upper bound" (genuine gap, needs recovery). Instruct agents to state which applies and the exact last line read. The main thread then only investigates (b).

**Principle:** When work is partitioned by disjoint contiguous ranges, boundary spillover is the expected case, not an anomaly — make agents classify their own stopping condition so the orchestrator's inventory only escalates true shortfalls.



### Observation 100: User flags ~30-min ingest wall-clock as too slow — identify irreducible vs cuttable time per ingest

**Status:** ACTIONED — Wall-clock expectations note after Step 3 completion (review 2026-07-16)
**Date:** 2026-07-10
**Session context:** Powell & DiMaggio 1991 ingest (~23 min gate-to-gate; scanned PDF requiring ~7 min OCR)
**Skill:** CLAUDE.md ingest workflow (deployed subagent strategy)
**Type:** internal
**Phase/Area:** Overall wall-clock / user expectations

**Issue:** User complained about session length ("half an hour again"). Breakdown: OCR ~7 min (irreducible for scans), extraction wave ~4 min, integration wave ~5 min, main-thread claims review ~5 min, hub authoring + validation + bookkeeping the rest. Recurring feedback — user memory already records a speed/lean-execution preference.

**Suggested improvement:** (a) For well-structured anthologies with clean extractor summaries, replace full main-thread reads of every claims file with summary-skim + spot-check; (b) offered user a CLAUDE.md toggle to defer mandatory hub pages to explicit request — apply whichever they choose; (c) state expected wall-clock up front when a source is a scan (OCR tax) so long runs are anticipated, not discovered.

**Principle:** When a user repeatedly flags duration, decompose wall-clock into irreducible vs discretionary components and offer the discretionary cuts as explicit defaults — silence about expected duration reads as slowness.



### Observation 101: Extractors can invent relations BETWEEN correctly-identified entities — verify relational claims, not just identities

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-10
**Session context:** Ingest of Firth, Primitive Polynesian Economy (1939)
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Step 4a claims review)
**Type:** internal
**Phase/Area:** Extraction subagent output / claims review

**Issue:** A Sonnet extractor, despite the standing entity-mismatch instruction, glossed a footnote citation of "J. R. Firth, Speech" as Raymond Firth's "brother" — the source says nothing of the kind (J. R. Firth the linguist was unrelated). The entities were both correctly identified; the invented content was the *relationship* between them. The claim nearly propagated into a hub page.

**Suggested improvement:** In Step 4a claims review, spot-verify not only entity identities and grounding quotes but any RELATIONAL claim (kinship, teacher/student, institutional ties) an extractor asserts between named persons when it is not backed by a grounding quote. Extraction prompts could add: "state relationships between named persons only if the text states them."

**Principle:** Confabulation risk concentrates where extractors add connective tissue between correct facts; grounding-quote discipline covers claims but not the glosses attached to them.



### Observation 102: Disambiguate ethnonyms that collide with vault-unique slugs

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-10
**Session context:** Ingest of Gluckman *Politics, Law and Ritual* — Colson’s Plateau Tonga claims vs existing Polynesian `tonga.md`
**Skill:** New skill candidate: wiki-ingest (internal) / CLAUDE.md ingest pre-scan
**Type:** internal
**Phase/Area:** Step 1 duplicate-page pre-scan / society naming

**Issue:** Pre-scan showed `wiki/societies/tonga.md` EXISTS. Claims agents and integrators for African “Tonga” (Colson/Gluckman) would have appended Central African material to the Polynesian Tuʻi Tonga polity page if the bare ethnonym were used as the slug. Folder-agnostic existence checks alone are insufficient: the *entity* behind a shared ethnonym must be verified (region, language family, documenter).

**Suggested improvement:** In CLAUDE.md ingest Step 1 pre-scan, for society/culture ethnonyms that exist, require a one-line entity check (region + type) before locking the slug; if mismatch, create a disambiguated slug (`plateau-tonga`, etc.) and ban bare `[[tonga]]` for the other entity. Add to standing subagent instructions: “If an ethnonym matches an existing page but the region/documenter differs, file under Miscellaneous with proposed disambiguated slug.”

**Principle:** Vault-unique filenames prevent link breakage but do not prevent *entity* collisions when the same ethnonym names unrelated peoples; existence of a slug is not identity of referent.



### Observation 104: Concurrent sessions ingested the same source in parallel

**Status:** ACTIONED — Claim-the-ingest + resume-incomplete in Step 1 (review 2026-07-16)
**Date:** 2026-07-10
**Session context:** Ingest of Gluckman, *Order and Rebellion in Tribal Africa* (1963)
**Skill:** New skill candidate / CLAUDE.md ingest workflow
**Type:** internal
**Phase/Area:** Step 1 scaffold / session start

**Issue:** Two live sessions independently ingested the same book simultaneously (4-agent and 5-agent extractions, separate caches). Both wrote the source page, both updated gluckman-max (now carries two overlapping Order-and-Rebellion sections), both did bookkeeping. Content was mostly complementary thanks to Edit-append discipline, but a merge pass is needed and effort was duplicated wholesale.

**Suggested improvement:** Add a claim-the-ingest step to the ingest workflow: at Step 1, before scaffolding, check whether the source page slug already exists or whether a session-claim marker (e.g., a line in Structural_Sources or a lockfile in scratchpad-visible location like the wiki root) is present; if so, stop and ask the user. Symmetrically, write the source-page stub as the very first artifact so the sibling session's check can see it.

**Principle:** In multi-session wikis, the source page doubles as a lock; create it first and check for it first — Edit-append discipline limits damage but does not prevent duplicated whole-ingest effort.



### Observation 105: Extraction agents give internally contradictory coverage self-reports

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-11
**Session context:** Clifford *Predicament of Culture* ingest; range-3 agent reported covering "lines 1–~2600" yet flagged sections that actually lie before line 2600 as unread, so the main thread could not trust the stated boundary and re-read lines 2000–3158 to be safe.
**Skill:** CLAUDE.md ingest workflow (Step 3 standing instructions)
**Type:** internal
**Phase/Area:** extraction coverage reporting / gap recovery

**Issue:** The "report actual coverage" instruction yields a line number estimated after the fact; when it conflicts with the agent's own list of unread sections, the main thread must over-read to recover safely.

**Suggested improvement:** In extraction prompts, ask agents to report the LAST HEADING OR QUOTED LINE they actually read (verbatim), not an estimated line number — a verbatim anchor is checkable with grep and cannot be mis-estimated.

**Principle:** Self-reported numeric progress from an agent is unverifiable; a verbatim content anchor is. Prefer checkable anchors over estimates in any completion report.



### Observation 113: Seven-agent Martin & Grube Chronicle batch completed 7/7 without dropout

**Date:** 2026-07-15
**Session context:** Ingest Martin & Grube *Chronicle of the Maya Kings and Queens* (2nd ed. 2008); OCR PDF; 7 content-weighted extractors + 3 page-partitioned integrators
**Skill:** Social Sciences Wiki ingest (CLAUDE.md deployed-subagent protocol) / New skill candidate: none
**Type:** internal
**Phase/Area:** Step 3 extraction inventory; multi-agent reliability
**Status:** DECLINED — Positive 7-agent Martin & Grube success — evidence only (review 2026-07-16)

**Issue:** Seven parallel extraction agents (ranges covering ~14k body lines of noisy OCR dynastic text) all wrote non-empty claims files (70+78+80+120+68+93+100 ≈ 609 claims). Filesystem inventory 7/7 before integration; zero silent dropout. Stage-2 site integration (3 agents, exclusive page ownership) also completed cleanly.

**Suggested improvement:** Record as another positive multi-agent success case alongside Golden Bough / Orientalism batches. Content-weighted ranges (~1.3–2.7k lines) + sequential-chunk instruction for large ranges + exclusive claims paths remain the working pattern for OCR reference books.

**Principle:** For illustrated OCR reference volumes under ~100k words, 5–7 content-weighted agents with mandatory non-empty claims-path inventory is reliable; page-partitioned Stage-2 densification of pre-existing site pages avoids collision on shared culture/debate pages kept on the main thread.



### Observation 114: Integrator prompts should carry the schema-required section headings

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-15
**Session context:** Potts 1997 ingest (5 extractors + 5 page-owned integrators)
**Skill:** New skill candidate: wiki-ingest workflow (CLAUDE.md deployed-subagent strategy)
**Type:** internal
**Phase/Area:** Step 4b integration prompts

**Issue:** Integration agents wrote complete, high-quality stub fills (irrigation, seleucia-on-the-tigris) but omitted schema-mandated body headings ("Semantic History", "Operationalizations", "Significance"), producing 3 validate_schema errors the main thread had to patch after the fact. Same for the main-thread thinker page ("Overview").

**Suggested improvement:** When an integrator (or the main thread) is authorized to fully Write a new page, the prompt/checklist should include the exact required-section heading list for that page type, copied from CLAUDE.md's schema, so validation passes first try.

**Principle:** Validators encode the schema; prompts should too. Any agent allowed to create a page needs the page type's required headings inline in its brief, not just "follow the schema."



### Observation 115: Ingest body ranges should include Acknowledgments when they carry Rhind/origin facts

**Date:** 2026-07-15
**Session context:** Ingest Renfrew *Figuring It Out* (2003)
**Skill:** New skill candidate: social-sciences-wiki-ingest (internal) / CLAUDE.md ingest workflow
**Type:** internal
**Phase/Area:** Step 2 chunk boundaries / Step 3 recovery

**Issue:** Range 4 was cut at Postscript end (line 10802) so Acknowledgments (Rhind Lectures date, title, host, artist network) fell outside all exclusive slices. Extractor correctly reported gap; main thread recovered from full.txt. Same session: range_3 cache file truncated mid-chapter vs full.txt (agent recovered) — another signal that exclusive-range files need end-to-end length checks against assigned line numbers at cut time.

**Suggested improvement:** After cutting cache slices, assert each range file line count equals (end-start+1) and that Acknowledgments/colophon lines intended for extraction are assigned to a named range. Include "Acknowledgments if origin facts" in the last body range by default for lecture-based monographs.

**Principle:** Origin/paratext facts (lecture series, commission, dedications) are load-bearing for source pages; they must be inside an owned extraction range or explicitly main-thread-owned at scaffold time — not left to accidental recovery.
**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)



### Observation 116: Duplicate pre-scan must re-run when the create-manifest grows mid-session

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-15
**Session context:** Ingest of Hicks & Beaudry, *Cambridge Companion to Historical Archaeology* (2006)
**Skill:** Internal ingest workflow (CLAUDE.md deployed-subagent strategy)
**Type:** internal
**Phase/Area:** Step 1 duplicate-page pre-scan / Step 4a manifest lock

**Issue:** The Step-1 duplicate pre-scan checked only the slugs anticipated at scaffold time. The final manifest, locked after claims review (Step 4a), added `taskscape` — never pre-scanned. The page already existed (created 2026-07-09 by another session), and only the integration agent's own defensive existence check prevented a full-Write clobber.

**Suggested improvement:** At Step 4a manifest lock, re-run the folder-agnostic existence check (`find wiki -name "<slug>.md"`) over the *final* create-list, not just the scaffold-time candidates. One command over the locked list is cheap insurance.

**Principle:** A duplicate check is only as good as the moment it runs; any list that grows after validation must be re-validated at the point of commitment, not at the point of drafting.



### Observation 117: Integration agents re-litigate slug existence and get it wrong

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-15
**Session context:** Facing the Ocean (Cunliffe 2001) ingest — 10 extractors + 5 page-owned integrators
**Skill:** New skill candidate: wiki-ingest orchestration (CLAUDE.md deployed-subagent workflow)
**Type:** internal
**Phase/Area:** Stage-2 integration briefs

**Issue:** Two integration agents reported established slugs (hallstatt-culture, celtiberian-culture) as "do not exist" and left them as plain text / wrote "no wiki page yet" into frontmatter, even though the extraction brief's established-slug list included them and the pages exist. The "link only to slugs you can verify exist" rule caused agents to re-verify with a folder-scoped or failed check and downgrade valid links; main thread had to repair after the fact.

**Suggested improvement:** In integration briefs, state that the established-slug list is authoritative and pre-verified by the main thread — agents must link those without re-checking, and only verify slugs NOT on the list. Post-integration, grep agent-written pages for phrases like "no wiki page" / "does not exist" as an audit heuristic.

**Principle:** When an orchestrator pre-verifies facts, subagent briefs should transfer them as ground truth, not as things to re-derive — re-derivation under weaker context produces false negatives.



### Observation 119: Extraction subagent self-loads task-observer and stalls

**Status:** ACTIONED — Step 3 standing: do not load task-observer (with #35) (review 2026-07-16)
**Date:** 2026-07-15
**Session context:** Ingest of Cuno *Who Owns Antiquity?* — parallel claims extractors
**Skill:** CLAUDE.md Ingest Workflow — Deployed Subagent Strategy (Step 3); task-observer activation scope
**Type:** internal
**Phase/Area:** Extraction subagent prompts / skill activation

**Issue:** Range-1 extraction subagent spent its turn trying to activate the task-observer skill (session-start protocol) instead of reading its cache slice and writing claims. User had to interrupt and request a respawn with an explicit "do not load skills" constraint. Range 2–3 completed normally. The parent session correctly owns task-observer; child extractors should not inherit or re-run that protocol.

**Suggested improvement:** In CLAUDE.md Step 3 (and every extraction agent prompt template), add a hard negative constraint: extraction subagents must NOT load task-observer or run session-start skill protocols — extraction only, claims file only. Optionally set capability/prompt framing so skill discovery is suppressed for bulk extractors.

**Principle:** Session-start meta-skills are for the orchestrating main thread. Parallel extraction children that re-enter the full skill stack burn wall-clock and can fail silently from the user's perspective without producing the expected claims file.



### Observation 121: Sparse-verbatim + line-pointer instruction achieved 0/11 filter blocks on a maximally filter-prone source

**Status:** ACTIONED — Sparse-verbatim + line-pointer promoted to preferred filter-prone path in sensitive-content triage (review 2026-07-16)
**Date:** 2026-07-15
**Session context:** Ingest of Wistrich, *A Lethal Obsession* (2010) — 367k words of antisemitic/extremist/genocidal discourse quoted for analysis; historically the highest-risk content class for stochastic subagent content-filter blocks.
**Skill:** CLAUDE.md ingest workflow (sensitive-content triage)
**Type:** internal
**Phase/Area:** Step 2 sensitive-content triage / Step 3 extraction prompts

**Issue:** All 11 Sonnet extractors completed with zero content-filter blocks and zero silent deaths, on a source where CLAUDE.md predicts effectively stochastic blocking. Every prompt carried the standing instruction: extract facts/names/dates/doctrine in full but keep verbatim quotation of the most extreme passages sparse, preferring paraphrase + exact line pointer.

**Suggested improvement:** Treat the sparse-verbatim + line-pointer prompt clause as the confirmed primary mitigation (now 11/11 on the hardest case), with main-thread-recovery sizing as the fallback rather than the default routing. Ranges of ~2,500–4,300 lines remained recovery-sized and none needed it.

**Principle:** Filter blocks on charged-discourse sources are largely triggered by high-concentration verbatim reproduction, not by the subject matter itself; instructing extractors to paraphrase-with-pointers removes the trigger while preserving full informational fidelity (the main thread can pull exact quotes from cache slices on demand).



### Observation 122: Concurrent same-cluster ingests can converge productively — treat parallel sessions as collaborators, not just collision risks

**Status:** ACTIONED — Applied to CLAUDE.md (weekly review 2026-07-16, option A full-apply cluster)
**Date:** 2026-07-15
**Session context:** Ingest of Dinnerstein *Antisemitism in America* (1994) while two-plus parallel sessions ingested Cohn *Warrant for Genocide*, Nirenberg *Anti-Judaism*, and Wistrich *A Lethal Obsession* — four antisemitism sources in one day, all touching the same page cluster.
**Skill:** Social Sciences Wiki ingest methodology (CLAUDE.md Step 4 concurrent-session rules)
**Type:** internal
**Phase/Area:** Integration / concurrent-session Edit-append protocol

**Issue:** CLAUDE.md frames concurrency purely defensively (avoid clobbering). In practice the parallel sessions actively improved each other's pages: the Wistrich session appended an Operationalizations section to my just-created blood-libel page, fixing my validator error before I got to it, and another session had pre-linked my study slug into antisemitism.md's key_studies before the page body was written. The Edit-append discipline held and content converged cleanly with zero collisions.

**Suggested improvement:** Add to the concurrent-session guidance: when the user runs same-topical-cluster ingests in parallel (a deliberate curation pattern, evidently), (a) expect forward-links to your not-yet-written pages and treat a pre-existing link to your planned slug as confirmation, not a naming conflict; (b) before fixing validator errors on pages you created this session, re-read them — a sibling session may already have fixed the gap; (c) sibling-session appends to your new pages are normal, not contamination.

**Principle:** Concurrency rules written only as collision-avoidance miss the cooperative case; when parallel writers share a schema and a linker, their edits compose — the protocol should tell agents to check for sibling contributions before duplicating or "fixing" them.

### Observation 123: Reversed piped-wikilink order when display text leads the sentence
**Status:** OPEN

**Date:** 2026-07-16
**Session context:** Lenin CW landmark gap-fill ingest (M&E, Vol. 24, LWC, Testament)
**Skill:** CLAUDE.md ingest workflow (pre-lint greps)
**Type:** internal
**Phase/Area:** integration / wikilink hygiene

**Issue:** Main thread twice wrote [["Left-Wing" Communism|slug]] (display first, slug second) — inverted Obsidian syntax the checker caught as 2 broken links. Trigger: composing a sentence where the display title comes naturally first, especially titles containing quotes.

**Suggested improvement:** Add to the pre-lint mechanical greps a pattern for suspected reversed piped links, e.g. grep -rEn '\[\[[^]|]*[" ][^]|]*\|[a-z0-9-]+\]\]' on session-touched pages (display-like text before pipe, slug-like text after).

**Principle:** Syntax errors that mirror natural prose order recur; catch them with a cheap mechanical grep rather than relying on the full checker round-trip.
