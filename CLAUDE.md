# CLAUDE.md — Social Sciences Wiki

## Overview

A persistent, LLM-maintained wiki covering the social sciences — **anthropology** (all
four fields: cultural, biological, linguistic, archaeological), **sociology**, and
**archaeology** — as both bodies of knowledge and objects of study. The wiki holds two
coordinate layers: the **knowledge structures** (disciplines, theories, thinkers,
methods, landmark studies, debates) and the **subject matter** (societies, cultures,
sites, institutions, social phenomena). You read sources and build a structured,
interlinked knowledge base. I direct the analysis; you do all filing, cross-referencing,
synthesis, and bookkeeping.

Environment: Obsidian; all wiki files are markdown. Sources live in the collection
directory; the wiki lives in `wiki/`. **Never modify source files.** The source
collection is new and still being assembled. Two root-level trackers serve different
roles and **both must be updated on every ingest**:
- **`Outstanding sources.md`** — the user's **working roadmap** (curated tiered
  wish-list). When a listed work is ingested, mark its line item with ✅ and the
  ingest date (format used elsewhere on that file: `✅ ingested YYYY-MM-DD`). Partial
  ingests use ⚠️. Missing this mark is a bookkeeping defect — the same severity as
  skipping the `log.md` entry.
- **`Structural_Sources.md`** — the acquisition/queue/ingest ledger (what is on
  disk, queued, and filed). Mark ingested items with ✅ there too; create it as a
  prioritized tiered list on first ingest session if it does not exist.

This wiki is deliberately separate from the World History Wiki. Do not create
cross-vault wikilinks; where historical context is needed, state it in prose.

---

## Task-Observer Activation (mandatory)

**Main agent / orchestrating session only.** At the start of any task-oriented
session (ingest, lint, query, or any tool-using work), the **main agent** invokes
the `task-observer` (`one-skill-to-rule-them-all`) skill **before** reading source
content or beginning work. It captures skill-improvement observations and runs the
session-start protocol (weekly-review check, observation log). When loading any
skill, also check `skill-observations/log.md` for OPEN observations relevant to the
work and apply their insight even if the skill file isn't yet updated.

**Subagents must not run task-observer.** Extraction, integration, and other scoped
child agents skip task-observer and all session-start skill protocols unless the user
explicitly asks that child to improve a skill. Put this negative instruction in every
extractor/integrator prompt — inherited CLAUDE.md activation is not a license for
children to re-enter the meta-skill stack (it burns turns and can stall claims files).

---

## Core Design Principles

- **Two layers, one network.** Every substantive claim lives at the intersection of the
  layers: a finding is always *someone's finding, by some method, about some case*. A
  page in either layer that cannot be linked into the other is either a stub or a
  mistake. Links must preserve the connection — who studied it, how, and what they found.
- **Findings are not theories; theories are not facts.** The most common corruption in a
  social-science wiki is theory stated in wiki voice. The Voice and Attribution Protocol
  governs which register every claim is written in. Never assert a framework's claim as
  a finding.
- **Methods are first-class content.** How a result was produced — design, sampling,
  operationalization, dating method, fieldwork conditions — belongs alongside the result.
  Every study and society page records how we know, not just what we know.
- **The disciplines have histories and politics.** Anthropology's colonial entanglements,
  sociology's reform origins, archaeology's nationalist uses — reflexivity is content,
  not apology. Discipline, theory, and study pages carry a Reflexivity section where the
  production context shaped the knowledge.
- **Constructs are dated.** Concepts drift ("culture" in 1900 ≠ 1970 ≠ now); ethnography
  documents a fieldwork moment, not a timeless people; genetic and archaeological claims
  get superseded. Date-stamp aggressively — the ethnographic-present trap and the
  stale-science trap are the same error in two costumes.
- **Cultures, languages, genes, and peoples are four different things.** Never silently
  equate an archaeological culture with a language, a genetic population, or a
  self-conscious people. Equations must be argued, attributed, and flagged — use
  `associated_with`, not identity (see Evidence-Class Framework).
- **Evidence classes are plural and unequal by task.** Ethnographic depth, survey scale,
  material time-depth, experimental causal leverage — each class answers questions the
  others cannot, and fails in ways the others don't. Know which class carries each claim.
- **The collection's bias is unknown until audited.** The collection is new. On each
  ingest, note what the source does and does not cover; maintain the coverage map from
  evidence, not assumption, and flag thin areas explicitly on discipline overviews.

---

## Directory Structure

```
wiki/
  index.md              # Master catalog — updated after every ingest session
  log.md                # Append-only record of all ingests, queries, lint passes
  overview.md           # Current coverage map and known gap register

  # ── Knowledge-structure layer ─────────────────────────────────────────────
  disciplines/          # Discipline and subfield overviews (sociology, cultural
                        #   anthropology, archaeology, biological anthropology, ...)
  theories/             # Named theories, frameworks, schools, research programs
  thinkers/             # Scholars — concise network-oriented summaries
  methods/              # Field, analytic, dating, and statistical methods
  studies/              # Landmark empirical works as objects of analysis
  concepts/             # Analytical concepts (habitus, anomie, liminality, ...)
  debates/              # Disputes within and between the disciplines

  # ── Subject-matter layer ──────────────────────────────────────────────────
  societies/            # Ethnographically/sociologically documented peoples,
                        #   communities, and groups
  cultures/             # Archaeological cultures, language families,
                        #   genetically-defined populations
  sites/                # Archaeological sites — excavated loci
  institutions/         # Recurrent social forms (kinship systems, caste, markets,
                        #   religious organization, the state as social form)
  phenomena/            # Social processes and patterns (urbanization,
                        #   secularization, migration, stratification, ...)

  # ── Shared apparatus ──────────────────────────────────────────────────────
  comparisons/          # Cross-cultural and cross-case comparisons
  timelines/            # Disciplinary and archaeological chronologies
  queries/              # Filed answers to significant questions
  sources/              # One summary page per ingested source

  hubs/                 # High-resolution special sections (see the three Hubs)
    theory/             # Deep analyses of major theoretical programs & their debates
    thinkers/           # Graduate-level intellectual biographies
    studies/            # Deep analyses of classic studies (design, findings,
                        #   critiques, replication/reanalysis history)
```

---

## Temporal Frameworks

Two clocks run through this wiki. Anchor knowledge-layer pages to a **disciplinary
era**; anchor subject-matter pages (sites, cultures, long-run phenomena) to an
**archaeological/historical period** where deep time applies. Pages may carry both.

### Disciplinary Eras (knowledge layer)

| # | Era | Date Range | Markers |
|---|---|---|---|
| 1 | Precursors | before 1830 | travelers' accounts, political arithmetic, antiquarianism, moral philosophy |
| 2 | Founding Era | 1830–1890 | Comte, Spencer, Marx, Morgan, Tylor; three-age system; armchair anthropology |
| 3 | Classical Era | 1890–1920 | Durkheim, Weber, Simmel, Boas; professionalization; first chairs and journals |
| 4 | Fieldwork Revolution | 1920–1945 | Malinowski, Radcliffe-Brown, Chicago School; participant observation; culture-history archaeology |
| 5 | Postwar Expansion | 1945–1968 | structural-functionalism's peak, Parsons, Lévi-Strauss, survey research at scale, radiocarbon revolution |
| 6 | Critical Turn | 1968–1990 | conflict theory, feminism, Bourdieu, Geertz, processualism and its post-processual reaction, Writing Culture |
| 7 | Contemporary | 1990–present | globalization studies, practice theory consolidation, aDNA revolution, replication crisis, decolonization debates |

Era boundaries are conventional; when a source periodizes differently, note it on the
relevant discipline page rather than forcing the frame.

### Deep-Time Periods (subject-matter layer)

For sites, cultures, and long-run phenomena, use the standard archaeological
periodization, kebab-cased in frontmatter: `deep-prehistory` (before 3.3M BP),
`early-prehistory` (3.3M–300k BP), `late-prehistory` (300k–50k BP),
`behavioral-modernity` (50k–12k BP), `mesolithic` (12k–9.5k BP), `neolithic`
(9,500–3,000 BCE), `chalcolithic` (5,500–3,300 BCE), `bronze-age` (3,300–1,200 BCE),
`iron-age` (1,200–500 BCE), `classical-antiquity` (500 BCE–600 CE), `medieval`
(600–1500 CE), `early-modern` (1500–1800 CE), `modern` (1800–present). Regional
period systems (e.g., Woodland, Jōmon, Preclassic) are welcome as *additional* tags —
record the regional system's name on first use in `timelines/`.

BCE/CE throughout; BP for dates before 10,000 BCE. Always state dating method and
confidence for prehistoric dates (see Chronological Uncertainty Protocol).

---

## Regional Framework

Tag pages with the most specific applicable region; add parent regions as secondary tags.

```
Africa:      north-africa, sub-saharan-africa, east-africa, west-africa,
             central-africa, southern-africa, horn-of-africa
Americas:    north-america, mesoamerica, caribbean, andes, amazonia,
             southern-cone, eastern-north-america
Asia:        near-east, levant, mesopotamia, anatolia, iran-plateau,
             arabian-peninsula, central-asia, south-asia, southeast-asia,
             east-asia, china, japan, korea, steppe
Europe:      western-europe, northern-europe, eastern-europe, mediterranean,
             iberia, british-isles, balkans, scandinavia
Oceania:     australia, polynesia, melanesia, micronesia
Transregional: atlantic-world, indian-ocean, pacific-rim, global-north,
             global-south, diaspora
```

---

## Voice and Attribution Protocol — Mandatory

Every claim in the wiki is written in exactly one of three registers. Choosing the
wrong register is this wiki's equivalent of conflating sequence with causation.

| Register | Use for | Form |
|---|---|---|
| **Wiki voice** | Findings established across multiple independent studies/evidence classes; brute descriptive facts (dates, locations, sample sizes, what a study did) | plain declarative prose |
| **Attributed voice** | Any theoretical claim; any single-study finding; any interpretation; any contested figure | "Durkheim argued…", "Mead reported…", "(as of Reich 2018)" |
| **Position recording** | Live disputes between serious scholars | each position stated in its strongest form on a `debates/` page; no adjudication in wiki voice |

Rules of thumb: a claim that would be *revised if one book were refuted* is attributed;
a claim that names a mechanism or a meaning (not just a pattern) is attributed; theory
pages state core claims in attributed voice even on the theory's own page. Promotion
from attributed to wiki voice is an editorial event — do it only when independent
convergence is documented, and note the basis. Single-study findings additionally carry
replication status where known (see Contradiction and Replication Protocol).

---

## Page Types and Formats

Each page type's frontmatter schema is below. Fill **all** fields; use `[[unknown]]`
explicitly where genuinely unclear — never leave mandatory fields blank.

### Discipline Page (`wiki/disciplines/`)
One page per discipline and per major subfield (subfields nest under the parent, e.g.
`linguistic-anthropology.md` under `anthropology.md`).

```yaml
---
title: [Discipline/Subfield Name]
discipline_type: [discipline / subfield]
parent_discipline: [for subfields]
founded: [approximate era of professionalization]
founding_figures: []
core_questions: []
major_methods: []
subfields: []
collection_coverage: [strong / moderate / weak / absent / unaudited]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [discipline]
---
```
Required body: **Scope** (what the discipline claims as its object) · **Historical
Development** (by disciplinary era; institutionalization, national traditions) ·
**Theoretical Landscape** (linked theories, current balance of schools) · **Methods**
(linked) · **Relations to Adjacent Disciplines** (boundary disputes included) ·
**Current State** (active research fronts) · **Reflexivity** (the discipline's politics
and blind spots — colonial context, funding, WEIRD sampling, whatever applies) ·
**Collection Coverage Note**.

### Theory Page (`wiki/theories/`)
A named framework, school, or research program: structural-functionalism, symbolic
interactionism, practice theory, cultural evolutionism, processual archaeology,
world-systems theory. Schools of thought (Chicago School, Frankfurt School) are
theories with `theory_type: school`.

```yaml
---
title: [Theory/School Name]
theory_type: [grand-theory / middle-range / school / research-program / paradigm / method-theory]
disciplines: []
era_origin: [disciplinary era]
date_origin: [approximate]
originated_by: []
key_texts: []
core_claims: [3–6 one-line claims, attributed voice]
developed_from: []
competes_with: []
status: [active / contested / declining / absorbed / abandoned]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [theory, discipline-name]
---
```
`status: absorbed` marks frameworks whose vocabulary survives after the program died
(functionalism's "function"). Required body: **Core Claims** (attributed) ·
**Intellectual Origins** (what it reacted against — theories are usually answers to
predecessors) · **Key Proponents and Texts** (linked) · **Empirical Program** (what it
explained, predicted, or organized; linked studies) · **Method Commitments** ·
**Critiques and Responses** · **Current Status** (who still works in it, what got
absorbed where) · **Reflexivity** (where the program's context shaped its claims).
Deep treatments live in the Theory Hub (`hubs/theory/`) with a reciprocal
`theory_page` link; the summary links back.

### Thinker Page (`wiki/thinkers/`)
The **concise network-oriented summary** of a scholar. Very detailed intellectual
biographies live in the **Thinkers Hub** (`hubs/thinkers/`) — see that section.

```yaml
---
title: [Thinker Name]
date_birth: []
date_death: [or "living"]
disciplines: []
era: [disciplinary era(s)]
affiliated_theories: []
trained_under: []
trained: [notable students]
key_works: []
key_concepts: [concepts they coined or transformed]
fieldwork_sites: [for field researchers; with dates]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [thinker, discipline-name]
---
```
`trained_under`/`trained` build the intellectual genealogy — fill them diligently; the
genealogy network is one of this wiki's chief analytical products. Required body:
compact **Overview** · **Contributions** (concepts, theories, methods, findings — all
linked) · **Intellectual Genealogy** (teachers, students, rivalries) · **Critiques and
Reappraisals** (including posthumous reassessments and any misconduct/ethics record —
factual, attributed, not celebratory or prosecutorial) · **Historiography** (biographies,
archives, how the reputation has moved). Every detailed hub biography declares
`thinker_page` pointing to its summary; the summary carries a reciprocal link back.

### Method Page (`wiki/methods/`)
Participant observation, comparative method, survey research, regression, network
analysis, radiocarbon dating, stratigraphic excavation, seriation, discourse analysis.

```yaml
---
title: [Method Name]
method_type: [data-collection / analytic / dating / sampling / statistical /
              interpretive / experimental]
disciplines: []
introduced_by: []
date_introduced: [approximate]
supersedes: []
epistemic_leverage: [what questions it can answer that others cannot]
key_limitations: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [method]
---
```
Required body: **What It Does** · **Procedure** (summary resolution — this is a wiki,
not a manual) · **Assumptions and Limitations** (validity threats, known failure modes)
· **History** (introduction, refinements, controversies) · **Exemplary Applications**
(linked studies) · **Debates** (linked where promoted to `debates/`).

### Study Page (`wiki/studies/`)
A landmark empirical work treated as an **object of analysis**: *Argonauts of the
Western Pacific*, *Suicide*, *Middletown*, *The Nuer*, *Distinction*, a landmark
excavation campaign. Distinct from the `sources/` page (bibliographic record of
ingestion): the study page analyzes the research act itself. Create one when the work
is itself a reference point in the field — most ingested sources do NOT get one.

```yaml
---
title: [Study Short Title]
author: []
year_published: []
study_type: [ethnography / survey / comparative / excavation / experiment /
             longitudinal / archival / mixed]
disciplines: []
fieldwork_location: []
fieldwork_dates: [start–end; mandatory for ethnography and excavation]
population_studied: [linked society/culture/site where applicable]
methods_used: []
key_findings: [attributed voice]
concepts_introduced: []
replication_status: [replicated / partially-supported / failed-replication /
                     reanalyzed-contested / not-applicable / unknown]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [study, discipline-name]
---
```
`fieldwork_dates` and `replication_status` are mandatory — the first kills the
ethnographic-present trap, the second keeps the replication crisis visible. Required
body: **Question and Context** · **Design and Methods** · **Findings** (attributed) ·
**Theoretical Impact** · **Critiques, Reanalyses, and Replications** (Mead–Freeman-type
afterlives belong here, promoted to `debates/` when live) · **Current Standing**. Deep
treatments live in the Studies Hub with a reciprocal `study_page` link.

### Concept Page (`wiki/concepts/`)
Analytical concepts, both emic and etic: habitus, anomie, liminality, social fact,
agency, ethnicity, chiefdom, class.

```yaml
---
title: [Concept Name]
concept_type: [analytical / classificatory / emic-term / measurement-construct /
               periodization / other]
coined_by: []
date_coined: [approximate]
disciplines: []
emic_or_etic: [emic / etic / migrated — emic term turned analytic]
operationalized_as: [how it gets measured, if quantified]
contested: [yes / no]
related_concepts: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [concept]
---
```
Required body: **Definition as Coined** · **Semantic History** (how the meaning has
drifted — mandatory; concepts are the wiki's most time-sensitive objects) ·
**Operationalizations** (how different traditions measure it, and how the
measurements disagree) · **Applications** · **Critiques and Limitations**. Always
distinguish emic from etic; for migrated terms (taboo, totem, caste) record both lives.

### Debate Page (`wiki/debates/`)
Genuine disputes between serious scholars — theoretical, methodological, empirical,
interpretive, or ethical.

```yaml
---
title: [Debate Description]
dispute_type: [theoretical / methodological / empirical / interpretive /
               ethical / priority / source-reliability / replication]
disciplines: []
era: [disciplinary era(s)]
positions: []
key_texts: []
resolution_status: [open / partially-resolved / resolved-by-consensus / dissolved]
last_updated: [YYYY-MM-DD]
tags: [debate]
---
```
`source-reliability` is for disputes about how a text or dataset was produced, edited,
or reconstructed (authorship, editorial contamination, archive integrity) — not for
competing interpretations of shared evidence. `replication` is for failed or contested
replications / reanalyses of a study's findings. These two values match the Contradiction
and Replication Protocol classifications; do not file those as `interpretive` or
`empirical` solely because the older enum lacked the right label.
`dissolved` marks debates the field abandoned rather than settled (record why). Do not
adjudicate unless I explicitly ask — record each position in its strongest form with
its holders. **Standing debates to create during early ingestion:** Mead–Freeman
(Samoa) · processual vs. post-processual archaeology · structure vs. agency ·
nature–nurture and the sociobiology wars · the Kalahari debate (Kung ethnography) ·
Chagnon–Tierney and Yanomami research ethics · Clovis-first and peopling of the
Americas · qualitative–quantitative divide · the replication crisis and WEIRD sampling
· anthropology's colonial origins and the decolonization debate.

### Society Page (`wiki/societies/`)
An ethnographically or sociologically documented people, community, or group: the
Trobriand Islanders, the Nuer, the !Kung San, Middletown, a diaspora community.

```yaml
---
title: [Society/Community Name]
society_type: [ethnolinguistic-group / community / nation-population / diaspora /
               subculture / organization-population / other]
region: []
language_affiliation: []
subsistence_economy: [foraging / pastoral / horticultural / agrarian /
                      industrial / mixed / other]
kinship_system: [if documented; with source]
documented_by: [linked studies]
documentation_dates: [fieldwork/data dates — NOT "the present"]
endonym_exonym_note: [what they call themselves vs. what the literature calls them]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [society, region-name]
---
```
`documentation_dates` is mandatory and governs the whole page: **write in the past
tense of the documentation moment** ("in the 1930s the Nuer herded…"), never the
ethnographic present. Required body: **Overview** · **Social Organization** (kinship,
politics, stratification — as documented, with dates) · **Economy and Subsistence** ·
**Belief and Ritual** · **Documentation History** (who studied them, when, under what
conditions and relations of power) · **Representation Debates** (where the group
became a battleground — Kalahari, Yanomami — link the debate page) · **Identity
Cautions** (what the ethnonym does and does not pick out; state boundaries and
self-identification honestly).

### Culture Page (`wiki/cultures/`)
An analytically-defined grouping known primarily through non-textual evidence:
archaeological cultures, language families, genetically-defined populations.

```yaml
---
title: [Culture/Group Name]
culture_type: [archaeological-culture / language-family / genetic-population]
date_start: [approximate]
date_end: [approximate]
date_precision: [century / approximate / disputed / unknown]
dating_methods: []
period: [deep-time period(s)]
region: []
defined_by: [material-culture / linguistic / genetic / mixed]
construct_status: [robust / conventional / contested / obsolete]
type_site: []
key_sites: []
preceded_by: []
succeeded_by: []
language_affiliation: [if argued; note confidence]
genetic_signature: [brief, date-stamped — "(as of Author Year)"]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [culture, period-name, region-name]
---
```
`construct_status` is mandatory — archaeological cultures are **etic analytical
constructs**, not observed peoples; `obsolete` marks constructs the field has abandoned
(keep the page; record why). Required body: **Definition and Construct History** (who
defined it, when, on what evidence) · **Material / Linguistic / Genetic Signature**
(each evidence class stated separately — never merged into one undifferentiated
identity) · **Distribution and Chronology** · **Lifeways** (as evidenced) · **Relations
and Successions** (use `associated_with` / `descends_from` precisely) · **Identity
Cautions** (what the construct does *not* claim) · **Historiography**.

### Site Page (`wiki/sites/`)
An excavated (or systematically surveyed) archaeological locus.

```yaml
---
title: [Site Name]
site_type: [settlement / tell / cemetery-necropolis / cave-rockshelter /
            monument-ceremonial / quarry-mine / kill-butchery / hoard-deposit /
            shipwreck / rock-art / survey-region / other]
modern_country: []
coordinates: [approximate lat/lon]
date_earliest: [with BP/BCE/CE]
date_latest: []
date_precision: [exact / century / approximate / disputed / unknown]
dating_methods: []
periods_of_occupation: []
region: []
cultures: []
excavated_by: [principal investigators/institutions]
excavation_years: []
key_finds: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [site, period-name, region-name]
---
```
Required body: **Discovery and Excavation History** (who dug, when, how well —
excavation quality is a reliability fact; a 1900s spoil-heap dig and a modern
single-context excavation are not equal witnesses) · **Occupation Sequence** (summary
resolution) · **Significance** (what the site settles or anchors) · **Key Debates**
(linked) · dense links to cultures, phenomena, methods, studies.

### Institution Page (`wiki/institutions/`)
A recurrent social form analyzed across cases: marriage systems, caste, markets, the
firm, priesthood, age-grades, the prison, the school.

```yaml
---
title: [Institution Name]
institution_type: [kinship / political / economic / religious / legal /
                   educational / stratification / other]
distribution: [universal / widespread / regionally-specific / historically-specific]
key_variants: []
theorized_by: [linked theories/thinkers]
key_studies: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [institution]
---
```
Required body: **Definition and Scope** (what counts as a case, and who says so) ·
**Cross-Cultural Variation** (the comparative record, linked societies/cultures) ·
**Theoretical Treatments** (attributed — functionalist, conflict, evolutionary readings
side by side) · **Key Studies** (linked) · **Debates**.

### Phenomenon Page (`wiki/phenomena/`)
A social process or pattern: urbanization, secularization, migration, social mobility,
state formation, demographic transition, globalization.

```yaml
---
title: [Phenomenon Name]
phenomenon_type: [demographic / economic / political / religious / cultural /
                  technological / stratification / other]
scale: [micro / meso / macro / global]
date_start: [approximate, or "recurrent"]
date_end: [approximate, "ongoing", or "recurrent"]
period: [if deep-time]
region: []
measured_by: [operationalizations and indices]
driven_by: []
produces: []
theorized_by: []
key_studies: []
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [phenomenon, region-name]
---
```
Required body: **Definition and Scope** (what it is and is not) · **Measurement** (how
it's operationalized, and how measures disagree) · **Patterns and Findings** (wiki voice
only where convergent; otherwise attributed) · **Explanatory Theories** (side by side,
attributed) · **Interaction** (relation to other phenomena) · **Debates**.

### Comparison Page (`wiki/comparisons/`)
Explicit structural comparisons across societies, cultures, institutions, or cases —
the wiki's HRAF-style layer.

```yaml
---
title: [Comparison Description]
compares: [linked pages]
dimension: [what is being compared]
method: [controlled-comparison / statistical-crosscultural / paired-case / typological]
galton_note: [how case non-independence is handled — mandatory]
sources_ingested: [count]
last_updated: [YYYY-MM-DD]
tags: [comparison]
---
```
`galton_note` is mandatory: cross-cultural comparison's oldest methodological trap is
treating related cases as independent (Galton's problem) — every comparison page states
how diffusion/shared descent is handled, even if the answer is "not controlled; treat
as suggestive."

### Source Page (`wiki/sources/`)
One page per ingested source.

```yaml
---
title: [Source Title]
author: []
year: [publication year]
source_type: [primary-study / theoretical-work / reference / textbook-handbook /
              excavation-report / ethnography / scientific-study / series /
              history-of-discipline / polemic / mixed]
disciplines: []
era_coverage: [disciplinary era(s)]
region_coverage: []
methodological_approach: [ethnographic / quantitative / comparative /
                           archaeological / theoretical / historical /
                           genetic / linguistic / demographic / mixed / other]
reliability_notes: []
study_page: [if the work earned a studies/ page]
pages_created: [count]
pages_updated: [count]
ingested: [YYYY-MM-DD]
tags: [source]
---
```
`source_type: mixed` is for genre hybrids (essay-collections with empirical chapters,
works that are both primary study and theoretical program). If a `studies/` page is
warranted, prefer `primary-study` **or** `mixed` with `study_page:` set; put hybrid
detail in `reliability_notes` and set `methodological_approach: mixed` when methods
span types. Do not invent other ad-hoc type labels — use the enum.

---

## Link Types — Mandatory Distinctions

### Subject-matter links (causation, time, evidence)

| Label | Meaning |
|---|---|
| `caused_by: [[X]]` | X is a direct causal antecedent |
| `contributed_to: [[X]]` | X is a partial or enabling cause |
| `preceded_by: [[X]]` / `followed_by: [[X]]` | temporal order; causation not asserted |
| `produced: [[X]]` | this directly caused or created X |
| `enabled: [[X]]` | created conditions for X without direct causation |
| `concurrent_with: [[X]]` | simultaneous; relationship uncertain or absent |
| `part_of: [[X]]` / `contains: [[X]]` | composition |
| `analogous_to: [[X]]` | structurally similar in a different time/place |
| `contrasts_with: [[X]]` | explicitly different in important ways |
| `evidenced_by: [[X]]` / `evidence_for: [[X]]` | evidential relation (site, study, corpus, dataset) |
| `associated_with: [[X]]` | material/spatial/statistical association; identity NOT asserted |
| `descends_from: [[X]]` | genetic or linguistic descent; never political succession |

### Knowledge-layer links (ideas, people, findings)

| Label | Meaning |
|---|---|
| `proposed_by: [[X]]` / `proposed: [[X]]` | origination of a theory/concept/method |
| `developed_from: [[X]]` | intellectual descent with modification |
| `reacted_against: [[X]]` | defined itself in opposition to X |
| `supports: [[X]]` | study/evidence bears positively on theory X |
| `challenges: [[X]]` | study/evidence bears negatively on theory X |
| `refines: [[X]]` | narrows or corrects X without overthrowing it |
| `applies: [[X]]` | uses method/concept X |
| `operationalizes: [[X]]` | turns concept X into a measurement |
| `trained_under: [[X]]` / `trained: [[X]]` | intellectual genealogy |
| `studied: [[X]]` / `studied_by: [[X]]` | study ↔ society/culture/site/phenomenon |
| `debated_in: [[X]]` | the dispute over this lives on debate page X |

Two distinctions are load-bearing. First, `caused_by` vs. `preceded_by`: never conflate
temporal sequence with causation. Second, `supports`/`challenges` vs. wiki-voice truth:
a study *supporting* a theory is a recorded relation, not a verdict — verdicts, where
they exist, are documented convergence on the theory page. And as everywhere:
`associated_with` is not identity (see Evidence-Class Framework).

---

## Scale Framework

| Scale | Definition |
|---|---|
| `micro` | Individuals and face-to-face interaction |
| `meso` | Organizations, communities, networks |
| `macro` | Whole societies, national populations, civilizational systems |
| `global` | World-systems, transnational processes |

Phenomenon pages specify `scale`; study pages should state their unit of analysis in
the Design section — scale mismatch between theory and evidence (macro claims from
micro data, ecological fallacies the other way) is a standing lint concern.

---

## Chronological Uncertainty Protocol

| Flag | Meaning |
|---|---|
| `exact` | Documented to the day or year |
| `year` | Documented to the year |
| `decade` | Known within a decade |
| `quarter-century` | Known within 25 years |
| `century` | Known within a century |
| `approximate` | Known within a few centuries; consensus exists |
| `disputed` | Scholars disagree significantly |
| `unknown` | No reliable dating available |

**Scientific-dating hygiene:**
- Radiocarbon dates are **calibrated by default** — write `cal BP` / `cal BCE` and never
  mix calibrated and uncalibrated dates in one comparison; if a source reports
  uncalibrated dates, say so explicitly.
- Carry the reported uncertainty (± range or 2σ interval) for lab dates that anchor a
  page's chronology; a bare year laundered from a dated range is a precision error.
- Glottochronology and other absolute linguistic dating is **contested** — flag any date
  resting on it and prefer relative linguistic sequence plus independent anchors.
- Dendrochronology and ice-core/varve chronologies are the strongest absolute anchors
  available; when a page's date rests on one, say which.
- For the knowledge layer: date theories by key-text publication, not by later fame;
  date fieldwork by the fieldwork, not the monograph (Malinowski's Trobriand work is
  1915–18, not 1922).

---

## Evidence-Class Framework

Social science's archives are plural. Every substantive claim rests on one or more of
the evidence classes below; know which, and weight accordingly.

| Class | Typical carriers | Strengths | Characteristic failure modes |
|---|---|---|---|
| ethnographic | fieldnotes, participant observation, interviews | depth, meaning, emic view, mechanism | observer effects; positionality; tiny n; ethnographic-present trap; unverifiable fieldnotes |
| survey/statistical | surveys, censuses, datasets, indices | scale, comparability, trend detection | operationalization validity; sampling bias; WEIRD samples; self-report ≠ behavior |
| experimental | lab and field experiments | causal identification | external validity; replication failures; demand effects |
| material | excavated assemblages, architecture, artifacts | deep time-depth; behavior not self-report; non-elite life | mute on meaning and names; preservation/recovery bias; interpretation-laden |
| textual/archival | documents, records, media corpora | actors' own categories; institutional memory | survivorship; production context; archive politics |
| genetic | aDNA, population genetics, isotopes | migration, admixture, kinship, demography, diet | silent on culture and language; sampling bias; fast supersession |
| linguistic | comparative reconstruction, loanwords, sociolinguistic data | deep contact/migration signals; classification | weak absolute dating; chronic homeland disputes |
| environmental | ice cores, pollen, tree rings, varves | independent chronologies; ecological constraint | correlation-to-causation trap in collapse/change narratives |

**Standing rules:**

1. **Four-way non-identity.** Archaeological culture ≠ language ≠ genetic population ≠
   self-conscious people. Pots are not people; genes are not languages. Any equation
   across these categories is a *claim* requiring argument and attribution — link with
   `associated_with`, record who asserts it and on what evidence, and note dissent.
2. **Independent convergence is the gold standard.** A conclusion supported by two or
   more *independent* evidence classes outranks any single-class claim, and is the only
   basis for promoting a finding to wiki voice. On major pages, state which classes
   agree, which are silent, and which conflict.
3. **Cross-class conflict → debate page.** When the material record contradicts
   ethnography, or genetics contradicts an archaeological model, or survey data
   contradicts ethnographic report, create/update a `debates/` page. These conflicts
   are often the field's most productive sites.
4. **Date-stamp fast-moving science and fieldwork alike.** Archaeogenetic and
   paleoclimate claims carry "(as of Author Year)"; ethnographic claims carry their
   fieldwork dates. Supersession is expected — update via the Contradiction and
   Replication Protocol; never silently overwrite.
5. **Ethnographic analogy is flagged, never smuggled.** Using a documented society to
   interpret an archaeological one is legitimate *only* when marked as analogy, with the
   bridging argument stated. Analogy is a hypothesis-generator, not evidence.
6. **Self-report is not behavior.** What people say they do (surveys, interviews) and
   what they observably do are different data; when they diverge, that divergence is a
   finding — record both.
7. **Sampling frames are content.** WEIRD samples, salvage-era ethnography's selection
   of the "untouched," excavation's bias toward monumental sites — note the frame on
   any page whose generalizations depend on it.
8. **Climate and environment are contributors, rarely causes.** A proxy synchronous with
   a social change licenses `concurrent_with`; promoting to `contributed_to` requires a
   stated mechanism; sole `caused_by` from environment alone is almost never defensible.

---

## Source-Type Handling

- **Landmark Primary Studies (classic ethnographies, foundational monographs,
  major excavation reports)** — the wiki's richest inputs. Dual-file: a `sources/` page
  (bibliographic, always) plus a `studies/` page (the research act as object of
  analysis) when the work is a reference point in the field. Record fieldwork/excavation
  dates, methods, and the author's theoretical school; extract findings in attributed
  voice; feed society/culture/site pages with date-stamped material. The work's
  afterlife — critiques, reanalyses, replications — belongs on the study page and, where
  live, a `debates/` page.
- **Theoretical Works (grand theory, programmatic statements, manifestos)** — feed
  `theories/`, `concepts/`, and `thinkers/` pages. Everything extracted is attributed
  voice by definition. Record what the work reacted against (`reacted_against`) — the
  polemical target is usually the key to the structure. Empirical illustrations inside
  theoretical works are illustrations, not findings; do not let them onto subject-matter
  pages as evidence.
- **Reference Works and Handbooks (Oxford/Cambridge Handbooks, Annual Review essays,
  encyclopedias of the disciplines)** — the most authoritative secondary layer;
  multi-author and peer-reviewed. Use the Large-Volume Protocol; never read in one pass.
  On conflict with monographs, give handbooks presumptive weight on the *state of the
  field* but not on primary findings — a handbook summarizing a study is downstream of
  the study. Excellent scaffolding sources for discipline and theory pages.
- **Textbooks** — useful for scaffolding discipline pages and standard narratives;
  weak as evidence. Note the edition year — textbook consensus lags the research front
  by a decade. Never cite a textbook as the sole basis for a contested claim.
- **Excavation Reports and Site Monographs** — treat as primary evidence. Record
  excavation dates and methods (excavation quality is a reliability fact — a 1900s
  spoil-heap dig and a modern single-context excavation are not equal witnesses); note
  which claims rest on the excavator's interpretation vs. the finds themselves. Feed
  `sites/` pages. When archaeology conflicts with ethnographic or textual claims,
  create a debate page.
- **Ethnographies (as a class, beyond the landmarks)** — record fieldwork dates and
  location, the ethnographer's positionality and school, emic vs. etic framing
  throughout. Avoid the **ethnographic-present trap**: an ethnography documents a
  society at its fieldwork moment — date every claim drawn from one. Classic
  ethnographies double as primary sources for the history of the discipline; file
  cross-links to `disciplines/` and `thinkers/` accordingly.
- **Archaeogenetics and Bioarchaeology Studies** — record sample size, provenance, and
  publication year; date-stamp every claim. Treat single-study conclusions as
  provisional until replicated; beware press-release inflation of cautious papers. aDNA
  speaks to populations and kinship, never directly to language or ethnicity — enforce
  the four-way non-identity rule at ingest.
- **Historical-Linguistics Works** — record the reconstruction's confidence tier
  (secure sound-law correspondence vs. speculative long-range comparison) and whether
  absolute dates rest on glottochronology (contested — flag). Homeland and macro-family
  arguments route to `debates/` pages, not wiki voice.
- **Quantitative Studies and Datasets (surveys, cross-national analyses, cliometrics)**
  — record the sampling frame, operationalizations, and error structure; ranges and
  effect sizes, not bare point claims, in wiki voice. A statistical association is
  `associated_with` until a design supports more.
- **Histories of the Disciplines** — feed disciplinary-era sections, thinker pages, and
  the genealogy network. Watch for winners' history: the standard origin story
  (Malinowski invented fieldwork; Durkheim founded sociology) is itself contested
  terrain — record revisionist accounts as positions.
- **Polemics and advocacy works (partisan popular non-fiction, not scholarship)** —
  ingest in **artifact mode** to keep the wiki's factual layer uncontaminated:
  (a) the source page carries heavy `reliability_notes` flagging its partisan character;
  (b) **all wiki writing stays on the main thread** — subagents extract to the scratchpad
  only, never to live pages; (c) split every extract into **FACTS** (with named-source
  attribution chains), **THESES**, and **QUOTES**: well-documented facts may flow onto
  subject-matter pages as *attributed* material, while the book's interpretive theses
  are quarantined as **positions on a `debates/` page**, never asserted in wiki voice;
  (d) keep the footprint deliberately small (source + debate + any genuinely new concept
  + cross-links). Instruct extractors to flag the author's uncorroborated first-person
  claims. **The curator adjudicates contested sources, not the wiki:** debate pages use
  neutral position labels, state each position in its strongest form, record a "shared
  factual ground, framed per side" section rather than a wiki-voice verdict, and carry a
  dated curator's note for the curator's own view — do not let adjudication leak into
  position labels, `resolution_status`, or `reliability_notes`. Much of the
  social-science culture-war literature (race and IQ, sociobiology polemics,
  decolonization polemics from any direction) belongs in this mode.
- **Public-domain OCR monographs (edition vs year).** Bibliographic year and
  *textual state* are different facts. Queue names and Anna's Archive labels often
  encode first publication; the body may be a later revision. Before locking
  frontmatter `year`, scan for post-first-edition markers (war dates after the
  claimed year, later works cited, copyright/revised-edition lines). Prefer
  `year` = first publication with an explicit `reliability_notes` clause when the
  body is a later revision — never silently attribute revised interpolations to the
  first-edition date.

---

## Ingest Workflow — Deployed Subagent Strategy (DEFAULT)

**Primary ingest method for all sources.** Parallelizes claim extraction across Sonnet
subagents while keeping all scaffolding, reconciliation, and validation on the main
thread. The Standard and Large-Volume protocols below are **reference material** for
per-page schema, section logic, and reflexivity requirements — not separate workflows
to choose between.

Non-negotiable principle: **the main thread owns structure; subagents own bulk
extraction.** Subagents never decide taxonomy, naming, or cross-links — they fill claims
within boundaries the main thread already drew.

### Progress Checklist (mandatory — user-visible)

Long tool loops (especially multi-agent extraction) look **frozen** from the user's
side even when work is progressing. Silent progress is a defect. Enforce a **visible
progress checklist** for every multi-step ingest (and any other multi-phase session of
comparable length).

1. **Post the checklist at session start** — before spawning extractors, not after the
   first long wait. Use the session todo list (`TodoWrite` or equivalent) **and** state
   the same plan in chat so the user sees it without opening a side panel.
2. **Minimum ingest checklist** (adapt labels; keep the phases):
   - [ ] Source located · word-count intake · cache slices cut
   - [ ] Scaffold (source page + key link targets on disk)
   - [ ] Extractors spawned — **N agents**, cache dir, expected claims filenames
   - [ ] Claims inventory — per-range status: pending / running / done / missing→recover
   - [ ] Integration — pages created/updated (tick in batches as they land)
   - [ ] Validate (`scripts/check.sh`; 0 new broken links vs session baseline)
   - [ ] Bookkeeping (index, log, `Outstanding sources.md` ✅, `Structural_Sources`, file source out of `raw/` root)
   - [ ] Cache cleanup (this ingest’s `scratchpad/` and/or `/tmp/` cache dir only)
3. **Update the checklist as phases complete.** After spawn, show a **per-range row**
   (e.g. `range_1` … `range_N`) and flip each to done when its claims file is non-empty
   on disk. During integration, tick major page batches — do not hold all updates until
   the very end.
4. **No multi-minute silence.** If extractors or integration will run more than ~1–2
   minutes, interleave short user-visible status (checklist tick or one-line progress)
   with tool work. A session that is "working" with no checklist/status update for
   several minutes **violates this rule** — same severity class as skipping the
   filesystem inventory.
5. **On user "are you frozen?" / mid-wait messages:** first reply is the current
   checklist state + claims inventory (which ranges done/missing), not a re-plan and
   not a long apology without status.

**Step 1 — Scaffold first, on the main thread.**

**Claim-the-ingest (before scaffolding).** Check whether `wiki/sources/[slug].md`
already exists or the work is already marked ingested on `Outstanding sources.md` /
`Structural_Sources.md`. If another session owns this source, **stop and ask the user**
— do not run a second full extract. Write the source-page stub as the first artifact so
a sibling session's check can see it. Same-source parallel ingest wastes wall-clock and
produces colliding bookkeeping even when Edit-append limits content damage.

**Resume-incomplete check.** If a source page exists with an `ingested:` date but (a)
no matching `wiki/log.md` line, or (b) the file is still in `raw/` root, or (c) the
trackers are unmarked — treat as incomplete bookkeeping and finish Step 6 before
re-extracting.

**Word-count / text-layer intake check.** Run `wc -w` on the raw text and compare
against expected length (~250–350 words/page × page count). Note: `wc` prints
*lines words chars* — use the words column, not the first number. Converted ebooks
fail silently — an epub→txt run can capture only Part One and drop the rest while the
TOC still lists every chapter, so a TOC-only read won't catch it. If the ratio is badly
off, grep for each TOC chapter heading in the body to find where the text actually
ends, and note incompleteness on the source page and in `reliability_notes`.

**Scanned / image-only recovery ladder** (when pdftotext/ebook-convert yield ~0 or
<< expected words):
1. Confirm image-only: many page images in the archive, empty or wrapper-only text.
2. Prefer workspace-local temp (`scratchpad/tmp_ocr` or `TMPDIR` on the project disk) —
   never rely on small tmpfs `/tmp` for 300+ page OCR (ocrmypdf can hit ENOSPC and
   silently zero the sidecar).
3. **PDF:** try `ocrmypdf` at ~200 DPI with project-local temp; if it fails (DuXiu
   diacritic crashes, etc.), fall back to parallel `pdftoppm` + `tesseract` with
   `OMP_THREAD_LIMIT=1` per worker (naive parallel tesseract oversubscribes cores).
4. **Image-only epub:** do not treat as empty — run ordered-page OCR following HTML
   reading order (low-res scans: 2× upscale + psm 3). Prefer `ebook-convert` over
   pandoc `-t plain` for normal epubs (pandoc can inflate word count via ASCII-art
   borders); image epubs still need OCR.
5. Cache OCR text to the session cache (`…/full.txt`) and file as
   `raw/…/author-title-year.txt` after ingest. Budget 15–40 min for ~150–200 page
   scans — state the OCR tax up front so long runs are expected, not discovered.

Then read enough (TOC, intro, conclusion, targeted sampling) to: write the **source
page** (with Section Plan for large volumes); create the **key
thinker/theory/concept/method/society/site pages** everything links to; decide whether
the work earns a **`studies/` page**, and whether a **hub page** (`hubs/thinkers/`,
`hubs/studies/`, `hubs/theory/`) is warranted — pre-establish its name; decide the
**topic taxonomy** and **naming conventions** for every page the ingest will create.
Do not spawn any agent until naming conventions and the set of linkable page names
exist on disk — subagents inherit names, never invent structural ones.

**Grep-verify coined terms before scaffolding concept pages.** Before committing a
pre-named concept/theory page that rests on a specific term, grep the converted source
for that term. If absent, drop the page or route content into an adjacent
source-grounded page — never create a term-page the ingested source does not support
(outside-knowledge contamination at scaffold time).

**Multi-site theoretical monographs.** A book's best-known field site is not always
its only site. Spot-read empirical chapters (not only the preface) for place names and
list **all** documented populations in extractor briefs. Site switches are entity
boundaries — agents already flag entity mismatches; emphasize site-switching as a
common trigger.

**A warranted hub page is part of the ingest, not a follow-up.** If the source meets a
hub's selection criteria (see the three Hub sections), create the hub page **in the same
session as the ingest** — do not defer it to "a future session," log it as "not done,"
or treat it as optional polish. The judgment call is only *whether the criteria are met*;
once they are, building the page is mandatory, not discretionary. Deferring a warranted
hub entry is a defect, the same as leaving a required body section unwritten. If genuine
scope limits force a split, that is the user's call to make, not yours to assume — flag
the warranted-but-unbuilt hub explicitly and ask, rather than silently skipping it.

Before spawning, run a **duplicate-page pre-scan** over the thinkers/entities the ingest
will touch. **Resolve every candidate slug folder-agnostically** — `find wiki -name
"<slug>.md"` (or a whole-vault `grep -rl`), NEVER a single-folder `[ -f folder/slug.md ]`
test. Obsidian resolves wikilinks by bare filename across all folders, so a slug is already
taken if it exists in *any* folder; a per-folder check gives false "missing" results and
manufactures duplicate-slug collisions (this exact mistake created a duplicate
`ancestral-polynesian-society` — the pre-existing page was in `concepts/`, the folder-blind
check only looked in `societies/`). Grep both name orders (`durkheim-emile` /
`emile-durkheim`), check synonymous titles (`structural-functionalism` / `functionalism`),
and watch for the same entity split across folders (a school in both `theories/` and
`disciplines/`, a people in both `societies/` and `cultures/`). **Ethnonym collision
check:** if a society/culture slug already exists, verify region + type before locking
it — the same ethnonym can name unrelated peoples (e.g. African Tonga vs Polynesian
Tonga); on mismatch, use a disambiguated slug (`plateau-tonga`, etc.) and ban bare
`[[tonga]]` for the other entity. **Concurrent same-author risk:** when multiple works
by one thinker may be under concurrent ingest, `ls`/`find` shared concept slugs
immediately before creating each new page and agree a shared vocabulary scheme — the
wikilink checker cannot see duplicate *canonical* pages that both resolve. State the
canonical name in every agent prompt and queue any duplicates found for a main-thread
merge in Step 4. Pre-resolving naming ambiguity once is far cheaper than letting N
agents each rediscover and work around the same duplicate.

**Step 2 — Split the book by disjoint line-ranges.** Divide raw text into N contiguous,
non-overlapping chunks by line number.
- **Size N to the book, not a fixed number.** Base it on *body* length × density (exclude
  front matter, endnotes, bibliography, index — can be half the file). Rule of thumb: one
  agent per ~2,000–3,500 body lines; floor 2–3; up to 10 for very large/multi-volume
  references. **Do NOT default to 6** — a ~2,700-body-line book wants ~3 agents; over-
  splitting starves agents of context.
- **Weight chunks by content density and importance, not even boundaries.** Dense/pivotal
  stretches get their own agent (or multiple passes over one major section for dense,
  multi-doctrine material); lighter material combines into a larger range. Align edges to
  natural section/chapter boundaries only where it doesn't fight the weighting — content
  weight wins.
- Ranges must be **disjoint** — every line in exactly one chunk.
- **Include Acknowledgments/colophon when they carry origin facts.** Lecture series
  dates, commission notes, Rhind/host facts, and similar paratext are load-bearing for
  the source page. Fold them into the last body range by default (or assign them to
  main-thread ownership at scaffold) — do not leave them outside all exclusive slices.
- **Sensitive-content triage (mandatory).** While drawing chunk boundaries, flag any
  range dense in atrocity/persecution documentation — genocide, mass violence, slavery,
  torture, sexual violence, residential-school and forced-assimilation records — **and
  any range dense in charged *discourse*** (race-science claims quoted to refute them,
  extremist doctrine reproduced for analysis, graphic ethnographic material on violence
  or sexuality). Filters trigger on the *presence* of the material, not on whether the
  author endorses or refutes it. These chapters are **first-class wiki content and are
  never toned down, summarized around, or omitted** — the risk is mechanical: automated
  output filters can block a subagent's *entire* extraction when it reproduces such
  material verbatim at high concentration. Handle flagged ranges as follows:
  1. **Preferred for filter-prone charged-discourse sources:** spawn extractors with a
     **sparse-verbatim + line-pointer** clause — paraphrase claims; record exact line
     numbers for load-bearing quotes the main thread can pull from the cache slice.
     Filters are largely triggered by high-concentration verbatim reproduction, not by
     subject matter alone. Size ranges so a single-range main-thread recovery stays
     comfortable (~2.5k–4k lines) as the fallback.
  2. **Route maximally graphic atrocity documentation to the main thread** when
     sparse-verbatim is not enough — main thread reads the cache slice and extracts at
     full fidelity. Give subagents the surrounding lighter ranges.
  3. If a flagged range is too long for comfortable main-thread reading, split it:
     subagents take procedural/analytic stretches; main thread takes concentrated
     documentation.
  The end state is identical in every case: the wiki page carries the complete
  record, with verbatim quotes where they are load-bearing.
  - **Race-science, sociobiology-war, and extremist-ideology sources are filter-prone
    regardless of graphic density.** Content-filter blocks on these sources are
    effectively stochastic — the *least* graphic range (definitional typology, doctrine
    exposition, refutation) is as likely to be blocked as the most graphic. Do not rely
    on triage to predict which range blocks. A block is a routing signal, never a
    content problem.

**Step 3 — Spawn one Sonnet subagent per chunk (parallel + background).** Use
the Agent tool with **`model: sonnet`** and `run_in_background: true`, one agent per
chunk. Each prompt must contain: its **exclusive line-range** (read only that range); the
**schema and naming conventions** from this file — including the **Voice and Attribution
Protocol** (extractions must mark each claim's register: finding vs. theoretical claim
vs. position); the **established page names** it may link to (Step 1) as **ground truth
already verified by the main thread** — agents link those without re-deriving existence;
**exclusive ownership of the claim titles it creates** (distinct title namespace/prefix
or topic set so no two agents write the same file); the instruction to extract claims
**with grounding quotes from its range only** — no outside knowledge, no reading beyond
its range.

**Complete templates in the prompt.** When a subagent creates schema'd pages, the
prompt's YAML example must be **complete and copy-pasteable** — every mandatory field
present with a value inline (`sources_ingested`, `last_updated`, `tags`, etc.). Prose
like "fill all fields" does not supply a field absent from the block. For new pages,
also paste the **exact required body-section headings** for that page type from this
file's schema so validation passes first try.

Every extraction prompt must also carry these standing instructions (each earned from a
recurring subagent failure mode):
- **Do not load task-observer** or run session-start skill protocols — extraction only;
  claims file only. Main agent owns observation logging.
- **Flag, don't force, entity mismatches.** If material near-matches a target page name
  but the entity differs (a different Redfield, the *other* Chicago School, same
  ethnonym different region), file it under Miscellaneous with an explicit mismatch
  flag and a proposed disambiguated slug rather than under the target.
- **No invented relations.** State relationships between named persons (kinship,
  teacher/student, institutional ties) only when the text states them — do not glue
  correctly identified entities together with confabulated connective tissue.
- **Flag internal duplication.** If you find passages duplicated verbatim within your
  slice (an ebook-conversion artifact), flag them and extract once — do not double-count.
- **Report actual coverage with checkable anchors.** In the completion summary: (a)
  state the **last heading or quoted line actually read** (verbatim — greppable), not
  only an estimated line number; (b) classify stopping as either *range fully read;
  final chapter continues past my upper bound* (expected boundary spillover — no
  recovery) or *stopped before my upper bound* (genuine gap — needs recovery). The
  main thread only escalates (b).
- **Treat chunk-brief content descriptions as expectations, not facts.** Any content
  summary in your brief was inferred from the TOC; verify against the text and extract
  what is actually there, flagging any mismatch. (When drafting briefs, phrase them as
  "likely covers X — verify," never as assertions; a ~10-line spot-read per chapter at
  boundary-drawing time grounds them cheaply.)
- **Large slices:** read the cache file in sequential chunks if needed; do not silently
  truncate mid-range. Write the claims file in **one final Write** so a mid-stream API
  death does not leave an empty path that looks like success.

Prepare small per-range cache files first (`/tmp/..._cache/range_N_START_END.txt`) so
each agent does cheap one-shot reads of only its slice. **Cut the cache slices to the
scratchpad immediately after locating the source — before scaffolding, not just before
spawning.** `raw/` is user-curated and mutable mid-session; slicing to session-local
storage first makes the ingest immune. Re-verify any source path right before a read
that follows a gap in time, and if a file disappears, check for deliberate curation
before treating it as an error. **Fire ALL extraction subagents in ONE immediate wave** —
launch them together (one dispatch), never dribbled out across several dispatch moments.
Extraction agents are independent by range with no cross-agent dependency, so staggering
buys nothing and serialised dispatch is the single biggest wall-clock sink (a staged ingest
took ~30 min; the same book in one wave + one integration wave took a fraction of that).
Collect all task_ids.

**Step 3 completion is a filesystem fact, not a wait-tool return value.** Silent
subagent death (no crash artifact, no partial claims file) is a recurring
orchestration failure: long multi-waits look frozen, user messages cancel the wait,
and missing ranges go unnoticed until the human asks. Enforce this checklist every
multi-agent ingest — structural, not optional narrative. **Also enforce the
user-visible Progress Checklist above** — filesystem inventory without user-facing
status still produces "frozen" sessions.

1. **Record the expected claims path set at spawn.** One naming convention per
   session, stated in every agent prompt and held by the main thread (e.g.
   `/tmp/..._cache/claims/range_1.md` … `range_N.md`, or `range_N_claims.md`). Tell
   the user: N agents, cache dir, expected filenames **as checklist rows**. Completion
   means those files exist and are non-empty — not that a wait tool returned.
2. **Do not use a single multi-minute multi-wait as the only completion signal.**
   Prefer short non-blocking status snapshots (`timeout_ms: 0` or equivalent) interleaved
   with useful main-thread work (scaffold remaining frontmatter, pre-read key passages,
   draft the source-page section plan) **and with checklist/status updates to the user**.
   A long blocking wait is a UX and cancellation hazard: when the user messages mid-wait,
   the wait is interrupted and the completion signal is lost without an inventory.
3. **Mandatory filesystem inventory before Step 4.** `ls` the claims dir (or expected
   paths). Missing path + cache slice present → that range failed, even if its task_id
   looked fine or the wait was cancelled. Do not start integration until every expected
   path is present or explicitly recovered. **Mirror the inventory in the progress
   checklist** (per-range done/missing) so the user sees the same facts.
4. **On any wait interruption or mid-batch user message:** first action is inventory of
   expected claims files + task status table **posted as the current checklist state** —
   not re-planning the whole ingest, not a status-free apology.
5. **Recovery for a missing range only** (leave successful ranges alone):
   - **Default:** main thread reads that range's cache slice, extracts claims at full
     fidelity, labels the block `Main-thread recovery (<failure mode>)`.
   - **Large range / silent agent death:** spawn one fresh extractor for *that range
     only*, or main-thread recover if the slice is short enough. Do not re-run ranges
     that already wrote complete claims files.
   - Content-filter blocks, rate limits, and crashes use the same path: recover the
     missing range; do not treat a block as a content problem.
6. **Optional bookkeeping:** note batch size and missing-range count in `wiki/log.md`
   for the ingest so recurrence is countable.

**Reliability note (evidence-based, not folklore):** multi-agent batches of 5–9
content-weighted agents complete without silent dropout when the filesystem inventory
+ recovery path above is enforced. Dropout is not automatic at a given N — detection
and recovery are the fix, not lowering default N. Success cases and failures both
belong in the ingest log when useful for calibration.

**Wall-clock expectations.** State expected duration up front when OCR is required
(scan tax dominates). Cuttable time: one-wave extract + one-wave integrate (never
staggered dispatch); summary-skim claims files with spot-check on well-structured
anthologies; avoid re-running clean validators. Irreducible: OCR, main-thread claims
review on contested material, hub pages when criteria are met.

**Step 4 — Review and tie together (main thread).** This step has two beats: a
**main-thread claims review** (the checkpoint), then **integration**.

**4a — Claims review (the safety gate; do this before any integration).** Read the claims
files yourself. Dedupe overlapping claims, resolve entity mismatches, catch collisions,
spot-verify **relational** claims between named persons (not only entity identities —
confabulated kinship/teacher glosses are a recurring extractor failure), and **lock the
final page manifest + canonical slugs + which claims feed which page**. **Re-run the
folder-agnostic duplicate pre-scan over the final create-list** (`find wiki -name
"<slug>.md"`) — the Step-1 scan is stale if the manifest grew mid-session. This
checkpoint is what makes delegating integration safe: once naming, dedup, and the
attributed-vs-wiki-voice calls are decided here, integration is just execution within
rails. Skipping it is what produces duplicate-slug collisions.

**4b — Integration.** Integration MAY be delegated to a wave of integration subagents
(the Two-stage variant below), fired in **ONE wave after the review**, each under an
explicit rule set you articulate (exact page ownership, the locked slug list as
**authoritative ground truth** — agents must not re-litigate slug existence or write
"no wiki page yet" for list members; schema + required body headings; Voice/Attribution
Protocol; don't-touch-others'-pages; no invented slugs). **Guardrail — keep the
highest-stakes pages on the main thread and write them yourself**: the central
culture/discipline page, the most contested `debates/`, and anything heavy on the four-way
non-identity rule. Delegate the rest. Rationale: the validator gates links and schema but
NOT prose nuance or subtle theory-as-fact leakage, and parallel agents can't see each
other's live text — so the trickiest ~10% of pages keep a higher ceiling when authored on
the main thread. After integration, run the voice-audit grep (below) over the
**agent-written** pages specifically, not just your own; also grep for phrases like
"no wiki page" / "does not exist" as a false-negative audit.

The integration mechanics: dedupe overlapping claims; fix
cross-links between new pages (subagents only linked Step-1 names); fill the source
page's claim list; remove agent artifacts (stray instructions, prompt echoes,
`</content>`-style tags — grep first); reconcile naming; **audit voice** — grep new and
updated pages for theory-as-fact leakage into wiki voice. **Before editing any existing
page, open it with the Read *tool* (not Bash `cat`) on the lines you'll change** — the
harness's Edit safety gate only tracks Read-tool calls, so a page you only `cat`-ed will
reject every Edit until you Read it. `cat` is fine for fast multi-file scanning, but it
does not satisfy the Edit precondition.

**Write-time revalidation.** The Step-1 "page does not exist" check goes stale during
a long extraction phase. Before creating any page scaffolded as "new," re-check
existence; if a `Write` fails the Read-precondition because a concurrent session already
created the file, **Read and Edit-append** — do not force a full Write.

**Concurrent sessions — collision and collaboration.** When a concurrent ingest may
touch the same pages, integrate with Edit-append, never a full Write — a full Write
silently clobbers the other session's additions. Reserve full Writes for pages this
session created and owns. **Edit-append protects additive *bookkeeping* (index, log,
`Outstanding sources.md`, `Structural_Sources`, coverage map), but it does NOT arbitrate
*authorship* of a shared *content* page.** If another live session *created* a content
page (theory, debate, concept, etc.) — even one that references your not-yet-written
source — that session owns its body, and its next full Write will clobber your appends.
On a content page another session created, add only **minimal cross-link stubs or a
single attributed paragraph**, and keep real depth on pages *you* own. Reserve rich
Edit-append for shared pages **neither** session claims to author.

Same-topic-cluster parallel sessions are often **deliberate collaboration**, not only
collision risk: (a) a pre-existing wikilink to your planned slug is confirmation, not a
naming fight; (b) before "fixing" validator errors on pages you created this session,
re-read them — a sibling may already have fixed the gap; (c) sibling appends on your
new pages are normal. When two books by one author run in parallel, **partition by
page ownership** (cases/concepts vs shared thinker/theory) rather than racing the same
slugs. At lint, grep for near-synonym duplicate slugs created since session start
(author's core concepts) — the wikilink checker is blind to dual-resolving duplicates.

**Pre-lint mechanical greps** (before the first full validator run — cheaper than
write→lint→fix→re-lint):
- Era tags wrongly wikilinked:
  `\[\[(precursors|founding-era|classical-era|fieldwork-revolution|postwar-expansion|critical-turn|contemporary)`
- Escaped-pipe wikilinks (break in tables / confuse the checker): `\[\[[^]]*\\\|`

**Two-stage variant for well-trodden sources.** When the wiki already has dense coverage
of a source's subject (e.g., a third Durkheim commentary into a wiki already holding two),
most claims are UPDATEs to existing pages, and many extraction ranges target the *same*
pages (one thinker can appear in half the ranges). Applying range-partitioned agents'
updates directly would collide on those shared files. Split the work into two parallel
waves instead:
- **Stage 1 — extraction, partitioned by disjoint line-range.** Agents own exclusive
  line-ranges and write **claims files only** (no edits to live wiki pages).
- **Stage 2 — integration, partitioned by exclusive wiki-page ownership.** Each agent
  owns a disjoint set of page slugs, greps *all* Stage-1 claims files for its owned
  slugs, and is restricted to the **Edit tool (no full rewrites)** to fold claims in.
The main thread keeps the filter-prone/sensitive pages and all new-page creation it
scaffolded. Partitioning Stage 2 by page (not by source range) is what makes concurrent
integration collision-free.

**Step 5 — Lint and validate.** Run and fix until clean:
`scripts/validate_schema.py` (frontmatter schemas + required body sections),
`scripts/check_wikilinks.py` (must report **0 broken links**; reads frontmatter
`aliases:` directly — no separate alias-sync step), and `scripts/lint_wiki.py`
(reciprocal links, genealogy symmetry, date-stamps, duplicates, orphans). All three
are purpose-built for this wiki's schemas — see `scripts/README.md`.
- **Run validators ONCE, chained, via `scripts/check.sh` — do not re-run a clean
  validator "to be sure."** The validators are idempotent whole-repo scans; a second
  run of a passing check is pure wall-clock with zero information gain (this was a
  measured time sink). Trust the first clean result and the harness's file-state
  tracking. `scripts/check.sh` runs all three in the canonical order and auto-diffs
  the wikilinks baseline if one exists.
- **Scope mid-ingest checks to the pages you touched with `--only`.** Every
  validator accepts `--only <substrings>` (comma/space separated), e.g.
  `scripts/check.sh --only whyte-,cornerville`. This reports findings only for
  matching pages (resolution still uses the full vault, so links/reciprocity stay
  correct) — use it instead of piping output through `grep`, which re-runs the whole
  script. Run the **full** pass (no `--only`) exactly once before finishing.
- **Take the wikilinks baseline at the START of the session:**
  `scripts/check.sh --baseline` (writes `/tmp/scs_links_baseline.json`). Then the
  final `scripts/check.sh` reports only NEW broken links — the correct signal when a
  concurrent session may also be introducing (its own) breakage. Under 3+ concurrent
  sessions this is also the only reliable way to **attribute** breakage: a broken link
  pointing at a page you never touched is expected noise — filter `--compare` output
  by *your* page slugs; do not chase sibling-session in-flight links.
- **Batch page writes; don't write→re-read→verify each file.** Edit/Write error if a
  write fails, so a confirmation read is redundant. Reserve reads for pages you must
  Read before Editing (the Edit safety gate).
- **Repair wikilinks with the Edit tool, not `sed`.** Piped wikilinks (`[[slug|Display]]`)
  and quoted YAML frontmatter break under bulk regex: `|` doubles as both the sed
  delimiter and the wikilink display separator, and blind substitutions corrupt
  frontmatter entries. Use Edit with exact old/new strings; if you must use sed, use a
  `#` delimiter with a verbatim-checked replacement, then re-grep the exact edited lines
  before re-running the checker.
- **No piped wikilinks in markdown table cells.** Unescaped `|` in `[[slug|Display]]`
  breaks table columns; escaped `[[slug\|Display]]` renders in Obsidian but
  `check_wikilinks.py` parses the target as `slug\` and reports a broken link. In table
  cells use a bare `[[slug]]` or plain display text, and put the piped form in adjacent
  prose if a custom display label is needed. Author to the intersection of what the
  renderer *and* the validator accept.
- **Proving "0 new broken links" is a snapshot-compare, not a stash-dance.** Before
  integration: `python scripts/check_wikilinks.py --json /tmp/links_baseline.json`.
  After: `python scripts/check_wikilinks.py --compare /tmp/links_baseline.json` — it
  reports exactly the NEW broken links and exits nonzero only on new breakage. (The
  checker never caps its output, so the history-wiki stash-comparison workaround is
  unnecessary here.)
- In `causes:`/`consequences:`/`core_claims:` and similar frontmatter lists, use
  `[[slug]]` only for real page links; write descriptive phrases as **free text, not
  brackets** — bracketing a phrase makes the wikilink checker count a phantom broken
  link to a non-existent slug.

**Step 6 — Bookkeeping and file.**
**Never close an ingest with content pages done but bookkeeping incomplete.** The
four-item close set is mandatory: `Outstanding sources.md` mark · `Structural_Sources`
update · `wiki/log.md` entry · `wiki/index.md` update · source filed out of `raw/`
root (and cache cleanup). Content-done / bookkeeping-incomplete is a resume case (see
Step 1), not a successful close.

**Batch the whole step — bookkeeping is the measured slow-motion phase.** Do NOT run
Step 6 as serial Read→Edit round-trips per file. One or two Bash calls should cover it:
a single scripted pass (python read/replace/write, or heredoc appends) that marks the
`Outstanding sources.md` line, appends the `Structural_Sources.md` entry, appends the
`log.md` entry, inserts the `index.md` line, moves the source file, and removes the
cache. These are append/mark-only files whose diff this session owns — the Read-tool
Edit precondition is wasted latency here; reserve Read+Edit for content pages. Draft
all bookkeeping text in one go before executing.
1. **Update `Outstanding sources.md`** (mandatory when the work appears there): find
   the matching line item and append `✅ ingested YYYY-MM-DD` (plus a short note if
   useful — pages created, partial scope). Use `⚠️ **partial**` when only part of a
   multi-work line or multi-volume set is done. Grep author surname + short title if
   the tier/number is unknown. **Do not close the ingest with the wiki marked done
   but this file still unmarked** — it is the user's working checklist.
2. **Update `Structural_Sources.md`**: if the source is a line item, mark it ingested
   (append ✅ / change status) and update any note. **Single-bullet appends only** —
   insert at a known anchor with exact prefix match. Never multi-line / DOTALL regex
   "dedupe" passes (a greedy match has destroyed the ledger). If dedupe is needed,
   match one line starting with `- **DATE**` for that author/title; dry-run and verify
   file size/line-count within ~2% after any delete.
3. **File the source** into the right `raw/` subfolder (create discipline- or
   era-grouped subfolders as the collection takes shape; underscore-prefixed grouping
   folders for multi-volume sets). Move both the text file (`.md`/`.txt`) and its
   original (`.pdf`/`.epub`) out of `raw/` root so the root holds only the un-ingested
   queue. **File by the exact path the cache slices were cut from** — collections hold
   near-duplicate twins (an abridged copy and the full edition), and filing a
   plausible-looking twin leaves the real ingested source in the queue. Echo the source
   path from the session or `wc -l`-match against the cache total before moving.
4. Append the `log.md` entry and update `index.md`. **Do not run `git commit` or
   `git push` — the user handles all git operations.** Leave the work
   staged-or-unstaged as-is.
5. **Cache cleanup (mandatory after a successful close).** Once Steps 1–4 of this
   bookkeeping block are done **and** validation reported 0 new broken links (or only
   pre-existing / concurrent-session noise), delete **this ingest’s** extraction cache
   so `scratchpad/` does not accumulate forever. Apply the same rule to any
   session-local `/tmp/..._cache/` used for the same ingest.
   - **What to delete:** the single cache directory named at spawn (e.g.
     `scratchpad/carneiro_cache/`, `scratchpad/kirch_chiefdoms_cache/`,
     `/tmp/carneiro_cache/`) — full tree: source slices, OCR intermediates, claims
     files, briefs. Also delete any one-off OCR sidecars or full-text dumps created
     under `scratchpad/` **for this source only** (e.g. `scratchpad/foo-book.txt` cut
     for this ingest).
   - **What not to delete:** other sessions’ cache dirs; the whole of `scratchpad/`;
     anything under `raw/` or `wiki/`; files you did not create for this ingest.
   - **When to skip or defer:** (a) ingest is partial / failed mid-integration and
     re-extraction may be needed; (b) the user asked to keep the cache; (c) a
     concurrent session still owns the same cache path (should not happen — use
     unique dir names). Note the skip in the log entry if you leave a large cache
     behind on purpose.
   - **How:** `rm -rf` the named cache dir only after a path check (`ls` the parent;
     confirm the basename matches this session’s cache). Do not wild-delete
     `scratchpad/*`. Tick the progress-checklist cleanup row when done.

> The two protocols below remain authoritative for **what each page must contain** (page
> types, frontmatter, link taxonomy, reflexivity) and **how to draw section boundaries**
> in large volumes (the Section Plan). Apply them within Steps 1–2 above.

---

## Ingest Workflow — Standard (books under ~400 pages)

For each source under ~400 pages:
1. **Identify** source type, disciplinary/era/regional coverage, methodological approach.
2. **Read** the full source in one pass.
3. **Write a source page** in `wiki/sources/` (and a `studies/` page if the work earns one).
4. **Create or update** discipline, theory, thinker, method, study, concept, debate,
   society, culture, site, institution, and phenomenon pages as the material warrants.
5. **Update `index.md`** with all new/modified pages.
6. **Append to `log.md`**:
   `## [YYYY-MM-DD] ingest | [Source Title] | [Discipline(s)] | [Era(s)/Period(s)] | [Pages created: N] | [Pages updated: N]`
7. **Mark ingest status on both trackers**: `Outstanding sources.md` (✅ on the
   matching line item — mandatory when listed) and `Structural_Sources.md` (✅ / note).
8. **File the source** to its `raw/` folder. If a PDF, convert to `.md` first, confirm
   the `.md` exists on disk, then delete the PDF.
9. **Cache cleanup** — same rule as deployed Step 6.5: after a successful close, delete
   this ingest’s `scratchpad/` and/or `/tmp/` cache dir only (not the whole scratchpad).
10. **Do not run `git commit` or `git push`** — the user handles all git operations once
   the ingest is complete.

A theoretical monograph may touch 5–15 pages; a classic ethnography 10–25 through
cross-links (society, study, thinker, concepts, methods, debates). Both are correct.

---

## Ingest Workflow — Large-Volume Protocol (books over ~400 pages)

Large reference volumes (handbooks, multi-volume histories of the disciplines, major
excavation reports, collected works) are processed in logical sections, not mechanical
token chunks. Keep the full context of a coherent argument in the window while writing
its pages, then commit to disk before advancing. **Never hold one section's content in
context while reading the next. Write first, then advance.**

**Step 1 — Read the Structural Map first.** Before any chapter content, read only the
TOC, the editor's introduction/preface, and the conclusion/afterword if present. From
these produce a **Section Plan** in `wiki/sources/[source-slug].md` listing every logical
section with: title and chapter numbers, discipline(s), era(s)/period(s), estimated page
count, and key thinkers/theories/studies flagged in the introduction. Write and save
this page before any content reading. Format:

```
## Section Plan

| Section | Chapters | Pages | Discipline | Era/Period | Key Topics |
|---|---|---|---|---|---|
| Classical Foundations | 1–3 | 1–90 | sociology | classical-era | Durkheim, Weber, method disputes |
| The Fieldwork Revolution | 4–6 | 91–180 | anthropology | fieldwork-revolution | Malinowski, Boas school |
...
```

**Step 2 — Process one section at a time** (complete this full cycle before the next; do
not read ahead):
- **2a. Read the section** in one pass; hold in context for the next step only.
- **2b. Identify all pages affected** — list new pages (with file names) and existing
  pages to update (with what changes) before writing anything.
- **2c. Write all affected pages** — complete content (not stubs), all frontmatter, all
  cross-links from this section, plus the reflexivity/historiography section where the
  page type requires one.
- **2d. Commit all pages to disk** before reading the next section. Critical discipline:
  Section N must be fully on disk before Section N+1 enters context.
- **2e. Append a section log entry**:
  `## [YYYY-MM-DD] section | [Volume Title] | Section: [Section Title] | [Pages created: N] | [Pages updated: N]`
- **2f. Clear and advance** only after pages are written and the log entry appended.

**Step 3 — Cross-Section Synthesis Pass** (with the source page and `index.md` in
context, not the raw text): read all pages from this volume; identify arguments spanning
multiple sections captured in separate pages; add cross-links visible only at the
whole-volume level; write a **Volume Synthesis Note** at the bottom of the source page
(3–5 paragraphs: the volume's overall argument, what it adds to the wiki, any tensions
with already-ingested sources).

**Step 4 — File the source** (PDF → `.md`, confirm on disk, delete PDF) to its `raw/`
folder. Mark `Outstanding sources.md` and `Structural_Sources.md` with ✅ (same rule
as deployed Step 6).

**Step 5 — Final log entry**:
`## [YYYY-MM-DD] ingest-complete | [Volume Title] | [Total pages created: N] | [Total pages updated: N] | [Sections processed: N]`

**Step 6 — Stop after bookkeeping and cache cleanup.** Confirm both source trackers
carry the ingest mark. Run the same **cache cleanup** as deployed Step 6.5 (this
volume’s `scratchpad/` / `/tmp/` cache dir only). Do not run `git commit` or
`git push` — the user handles all git operations once the volume is complete.

### Applied to specific series types
- **Discipline handbooks (Oxford/Cambridge Handbooks, Sage Handbooks)** — boundaries
  follow the editors' parts (typically 4–8 thematic parts), one part = one cycle. The
  editors' introduction frames the state of the field — give it its own cycle and let it
  drive updates to the relevant `disciplines/` page.
- **Multi-volume histories of a discipline** — boundaries follow era divisions; the
  synthesis pass must reconnect national traditions the volume treats separately.
- **Collected works / readers (a thinker's or school's anthology)** — group selections
  by phase of the career or program; feed the thinker page and hub biography heavily;
  every selection is primary material in attributed voice.
- **Major excavation monographs** — boundaries follow the report's structure
  (stratigraphy, finds classes, specialist appendices); specialist appendices (fauna,
  lithics, dating) are dense and get their own cycles; feed the site page and, where
  warranted, `studies/`.

### What "commit to disk" means (after each Step 2c)
1. Write every new `.md` file. 2. Edit every existing `.md` file. 3. Confirm each by
reading its path back. 4. Only then proceed to Step 2e. If a write fails, retry before
advancing. Context is ephemeral; disk is permanent — always resolve to disk.

---

## Reflexivity and Historiography Protocol

Every discipline page and every major theory, study, and society page requires a
`## Reflexivity` or `## Historiography` section (theory/discipline pages: Reflexivity;
study/society/culture/site pages: Historiography — the concern is the same) covering:
**evidence quality** (what the claims rest on; biases and gaps); **scholarly debates**;
**methodological approaches**; **recent revisionism** (significant changes in the
standard account, last 30 yrs); **production context** (who produced this knowledge,
under what conditions and relations of power — colonial administration, reform
movements, funding bodies — where it demonstrably shaped the claims); **collection
coverage** (what covers this well, where gaps exist). For archaeological pages, cover
excavation quality, theoretical lens (culture-historical / processual / post-processual
— name the school that shaped the standard interpretation), and dating basis
explicitly. For culture pages, cover construct history. Absence of written sources is
not absence of evidence.

---

## Contradiction and Replication Protocol

When new material contradicts existing content: 1. flag with `[CONTRADICTION]` on both
pages; 2. create/update the `wiki/debates/` page; 3. classify using a
`dispute_type` from the Debate schema enum — map prose labels as follows: factual
dispute → `empirical`; interpretive difference → `interpretive`; source-reliability
conflict → `source-reliability`; failed replication → `replication` (also
`theoretical` / `methodological` / `ethical` / `priority` when those fit better);
4. never silently overwrite — preserve both claims with attribution and date.

Replication and reanalysis get first-class handling: when a study's findings fail
replication or a reanalysis overturns them (Mead–Freeman, Tepoztlán restudied), update
the study page's `replication_status`, record the challenge in its Critiques section,
propagate to any page that cited the finding (grep for the study's slug), and demote
affected claims from wiki voice to attributed voice. A famous finding that failed
replication stays in the wiki — as a documented episode, not as a fact.

---

## Query Workflow

1. Read `index.md` for relevant pages. 2. Read those pages. 3. Synthesize with citations
to wiki pages, honoring the Voice and Attribution Protocol in the synthesis itself.
4. Offer to file as `wiki/queries/` if the synthesis was non-trivial. 5. Append to
`log.md`: `## [YYYY-MM-DD] query | [Question summary]`.

---

## Lint Workflow

The mechanical subset is automated — run `scripts/validate_schema.py`,
`scripts/check_wikilinks.py`, and `scripts/lint_wiki.py` first (see
`scripts/README.md`). The judgment items below (voice violations beyond crude
patterns, `caused_by` conflation, near-synonym duplicates) still need a reading pass.

On a health-check request, report:
- **Voice violations** — theoretical claims or single-study findings asserted in wiki
  voice (grep new/updated pages for unattributed mechanism-and-meaning claims)
- Study pages missing `fieldwork_dates` or `replication_status`
- Society pages written in the ethnographic present, or missing `documentation_dates`
- Culture pages missing `construct_status` or the Definition and Construct History /
  Identity Cautions sections
- **Silent culture=language=genes equations** — prose or links asserting identity across
  the four-way non-identity boundary without attribution or an `associated_with` link
- Archaeogenetic or paleoclimate claims lacking a "(as of Author Year)" date-stamp
- Chronology-anchoring dates lacking a stated dating method or calibration status
- Comparison pages missing `galton_note`
- Thinkers mentioned repeatedly without a thinker page; methods applied without a
  method page; concepts used analytically without a concept page
- Asymmetric genealogy links (`trained_under` without the reciprocal `trained`, or
  vice versa)
- `supports`/`challenges` links whose study page doesn't mention the theory (or vice
  versa)
- Debates described inline not yet promoted to `debates/`
- `caused_by` links that appear to conflate sequence with causation, and macro claims
  resting solely on micro evidence (scale mismatch)
- Orphan pages (no inbound links)
- **Duplicate canonical pages** — the wikilink checker cannot catch these (both targets
  resolve). Heuristic scan: near-synonymous titles, both name orders for a person
  (`durkheim-emile` / `emile-durkheim`), the same school under two names, the same
  entity split across folders (`societies/` vs `cultures/`, `theories/` vs
  `disciplines/`)
- Hub pages missing the reciprocal link from their summary page (or vice versa)
- Discipline pages where `collection_coverage` is `weak`, `absent`, or `unaudited`
- **Ingested sources missing the `Outstanding sources.md` ✅** — for any source page
  with `ingested:` in frontmatter whose work appears on that roadmap, the line item
  must carry `✅ ingested` (or ⚠️ partial). Spot-check recent `wiki/log.md` ingests
  against the roadmap; unmarked lines are bookkeeping defects
- 3–5 sources from `Outstanding sources.md` (unmarked items) / `Structural_Sources.md`
  to prioritize next
- 3–5 analytical questions worth investigating

**Frontmatter hygiene**: Run `python scripts/normalize_frontmatter.py --dry-run` (then
`--fix`) after large batches of edits or ingests (port the script from the World History
Wiki on first setup). It fixes scalar vs list inconsistency, unquoted values containing
special characters, and empty scalars, producing clean, consistently quoted,
Obsidian-Bases-friendly YAML while preserving all data. Re-run schema + wikilink check
after.

---

## Naming Conventions

- File names: `kebab-case.md`
- Thinkers: `[surname]-[given-name].md`
- Theories/schools: `[theory-name].md` (`structural-functionalism.md`,
  `chicago-school.md`)
- Methods: `[method-name].md`
- Studies: `[author-surname]-[short-title]-study.md` (`-study` suffix keeps slugs
  distinct from the `sources/` page: `malinowski-argonauts-study.md` vs. source
  `malinowski-argonauts-1922.md`)
- Concepts: `[concept-name].md`
- Debates: `[debate-name]-debate.md` (`mead-freeman-debate.md`)
- Societies: `[people-or-community-name].md` — prefer the endonym where established
  in the literature; record alternatives as aliases
- Cultures: `[culture-name]-culture.md` for archaeological cultures
  (`yamnaya-culture.md`); `[family-name]-languages.md` for language families
- **Lithic industries (standing taxonomy):** classificatory history and analytical
  debates live on `concepts/` (e.g. `mousterian`, `aurignacian`, `chatelperronian`).
  Do **not** also create parallel `cultures/*-industry` pages for the same industry —
  that dual taxonomy was reintroduced mid-ingest and thrashed across sessions. Material
  culture constructs that are true archaeological cultures keep the `-culture` suffix;
  industry names as etic type labels stay in concepts.
- Sites: `[site-name].md` — conventional archaeological name (`catalhoyuk.md`);
  modern-country qualifier if ambiguous
- Institutions and phenomena: `[name].md`
- Sources: `[author-surname]-[short-title]-[year].md`
- Obsidian links: `[[page-name|Display Name]]`
- Dates: BCE/CE throughout; BP for prehistoric before 10,000 BCE
- **Slugs must be vault-unique, with one sanctioned exception** — Obsidian resolves
  wikilinks by filename across folders; the type suffixes above (`-study`, `-culture`,
  `-debate`) exist to guarantee uniqueness. The exception: hub pages intentionally
  share their summary page's slug. Convention: a bare `[[slug]]` always means the
  summary page; link hub pages by full path (`[[hubs/theory/practice-theory|...]]`).
  `lint_wiki.py` enforces this — sanctioned hub/summary pairs pass, any other
  collision is an error. Check for collisions in the duplicate-page pre-scan.

---

## Special Page Types

**Comparison Pages** — the wiki's cross-cultural engine; see the Comparison Page schema
(with its mandatory `galton_note`). Standing comparisons worth building early: kinship
terminologies across regions · state formation pathways (linked to `phenomena/`) ·
secularization across national cases · foraging societies as documented vs. as
theorized · burial practice and social stratification in the archaeological record.

**Timeline Pages** — file in `wiki/timelines/`: disciplinary chronologies (founding of
departments, journals, associations), regional archaeological sequences (record each
regional period system here on first use), and method timelines (the radiocarbon
revolution, the statistical turn).

**Counterfactual and What-If Queries** — file in `wiki/queries/` with tag
`counterfactual`; useful for genealogy questions (does structuralism happen without
Jakobson meeting Lévi-Strauss?) — analytical tools, not content pages.

---

## Theory Hub — The High-Detail Section for Theoretical Programs

`wiki/hubs/theory/` is the **first of three high-resolution sections**: graduate-level
analyses of major theoretical programs and the debates that formed them. This depth
applies *only* here — do not let it leak into ordinary `theories/` or `debates/` pages.

**Division of labor (hub vs. theories//debates/)** — the `theories/` page owns the
**summary** (core claims, origins, proponents, critiques, status, dense links) at normal
resolution; the hub page owns the **depth** (full intellectual context, the conceptual
architecture worked through claim by claim, the empirical program's hits and misses,
verbatim key passages with analysis, the debate history blow by blow). Each hub page
links its summary via `theory_page`; the summary carries a reciprocal link back.

**Structure and naming** — `hubs/theory/[program-slug].md`, slug exactly matching the
`theories/` summary. The hub root holds `theory-hub.md` (portal + selection criteria +
list of completed analyses) and `templates/`.

**Analysis standard (to be locked).** The single source of truth will be
`wiki/hubs/theory/templates/theory-analysis-template.md` — create it from this section's
standard on the first hub ingest, then treat it as locked (copy it; do not redefine the
schema inline). Frontmatter is flat and quoted (Obsidian-Bases-friendly):
`analysis_type: theory`, `theory_page`, `disciplines`, `era_origin`, `originated_by`,
`key_texts`, `status`, `key_sources`. Content standard:
- **3,500–5,500+ words.**
- **TABLES**: key-texts table (text | year | move it makes | reception); a
  claims-vs-evidence matrix (claim | supporting studies | challenging studies | current
  standing).
- **Quote the program's key passages verbatim and analyse them** — what the words
  actually commit the program to, versus what followers and critics made of them.
- Work the **empirical program honestly**: what it explained that predecessors could
  not, where it failed, what anomalies accumulated.
- Always include a **"What Survived"** section — where the program's concepts and
  results live on in current work, even (especially) if the program itself is dead.
- Nine canonical body sections: Intellectual Origins and Context · Core Claims and
  Conceptual Architecture · Key Texts and Proponents · The Empirical Program ·
  Method Commitments · Major Debates and Rivals · Critiques and Responses · What
  Survived · Current Status and Research Frontiers.

**Selection criteria** — programs that organized a generation's research
(structural-functionalism, structuralism, processual archaeology, practice theory,
rational choice, world-systems) or debates that restructured a field (processual vs.
post-processual, the Writing Culture moment, the sociobiology wars). Exclude
one-author frameworks with no research community — those live on the thinker's pages.

---

## Thinkers Hub — The High-Detail Section for Scholars

`wiki/hubs/thinkers/` is the **second high-resolution section**: graduate-level
intellectual biographies of the discipline-makers. This depth applies *only* here — do
not let it leak into ordinary `thinkers/` pages.

**Division of labor (hub vs. thinkers/)** — the `thinkers/` page owns the **summary**
(compact overview, contributions, genealogy, critiques, historiography, dense links) at
normal resolution; the hub page owns the **depth** (formation and training, phased
career with the intellectual moves analyzed, verbatim primary-text analysis, fieldwork
or empirical base examined critically, reception history, politics and ethics record in
full). Each hub page links its summary via `thinker_page`; the summary carries a
reciprocal link back.

**Structure and naming** — `hubs/thinkers/[person-slug].md`, slug exactly matching
`thinkers/[person-slug].md`. The hub root holds `thinkers-hub.md` (portal + selection
criteria + completed list) and `templates/`.

**Analysis standard (to be locked).** Single source of truth:
`wiki/hubs/thinkers/templates/thinker-analysis-template.md` — create from this standard
on first use, then locked. Frontmatter flat and quoted: `analysis_type: thinker`,
`thinker_page`, `date_birth`/`date_death` + precision, `disciplines`, `key_works`,
`key_concepts`, `fieldwork_sites`, `primary_sources`, `key_sources`. Content standard:
- **4,000–5,000+ words** (flex by significance).
- **TABLES**: works timeline (work | year | move it makes | reception); a
  concepts-introduced matrix (concept | where coined | how it drifted | current use).
- **Verbatim primary-text quotation with analysis** — the thinker in their own words,
  read against what the textbooks say they said; reconcile or flag the gaps.
- **The empirical base examined critically**: fieldwork conditions, data quality,
  what restudies found (Freeman on Mead, the Kalahari restudies) — neither hagiography
  nor demolition; the ethics record stated factually and attributed.
- Strong **counterfactual genealogy** treatment: what the field looks like without
  this figure — which moves were personal, which were structural and coming anyway.
- Nine canonical body sections: Formation and Training · Intellectual Genealogy
  (teachers, students, rivals) · Career Phases · Major Works and Their Moves ·
  Conceptual Contributions and Their Mechanics · The Empirical Base (fieldwork/data
  examined) · Reception, Politics, and Ethics · Legacy and Counterfactual Significance
  · Historiography and Primary Sources.

**Selection criteria** — reserved for discipline-makers (founders, program-builders,
method-inventors) **or** figures with rich primary material and consequential
controversy (Mead, Chagnon). Exclude figures adequately served by the summary page.

---

## Studies Hub — The High-Detail Section for Classic Studies

`wiki/hubs/studies/` is the **third high-resolution section**: deep analyses of
landmark studies — the research acts that became reference points. This depth applies
*only* here — do not let it leak into ordinary `studies/` pages.

**Division of labor (hub vs. studies/)** — the `studies/` page owns the **summary**
(question, design, findings, impact, critiques, standing, dense links) at normal
resolution; the hub page owns the **depth** (the design reconstructed and critiqued,
the fieldwork/data-collection as actually conducted, findings in detail with the
evidence behind each, the full afterlife of critique, reanalysis, and replication).
Each hub page links its summary via `study_page`; the summary carries a reciprocal
link back.

**Structure and naming** — `hubs/studies/[study-slug].md`, slug exactly matching the
`studies/` summary (including its `-study` suffix). The hub root holds
`studies-hub.md` (portal + selection criteria + completed list) and `templates/`.

**Analysis standard (to be locked).** Single source of truth:
`wiki/hubs/studies/templates/study-analysis-template.md` — create from this standard on
first use, then locked. Frontmatter flat and quoted: `analysis_type: study`,
`study_page`, `author`, `year_published`, `study_type`, `fieldwork_location`,
`fieldwork_dates`, `methods_used`, `replication_status`, `key_sources`. Content
standard:
- **3,500–5,500+ words.**
- **TABLES**: design summary (question | unit | sample/site | method | period); a
  findings table (finding | evidence base | later status: confirmed / contested /
  overturned).
- **Reconstruct the study as conducted, not as advertised** — fieldwork conditions,
  access and informants, sample construction, what the methods section omits; use
  restudies, memoirs, and archival scholarship where ingested.
- **Quote the study verbatim at its load-bearing moments and analyse the rhetoric** —
  classic studies persuaded as texts, not just as data.
- **The afterlife in full**: every major critique, reanalysis, restudy, and replication
  attempt, each as a position with its evidence; the current balance stated in
  attributed voice.
- Nine canonical body sections: Question and Intellectual Context · Design and Methods
  as Conducted · The Site/Sample/Data · Findings in Detail · Analytic and Rhetorical
  Moves · Reception and Theoretical Impact · Critiques, Restudies, and Replications ·
  Current Standing · Historiography and Sources.

**Selection criteria** — studies that founded a method or a subfield, anchor a standing
debate, or carry an instructive failure (a famous finding that collapsed). A study page
in `studies/` is the prerequisite; the hub page is for the subset that repays
excavation-grade attention. **When a study meets these criteria, its hub analysis is
built during the ingest** (see Ingest Workflow Step 1: "A warranted hub page is part of
the ingest, not a follow-up") — do not close the ingest with a warranted study-hub page
merely pre-named or listed under "not done."

**Reference exemplars** — Studies Hub: `hubs/studies/durkheim-division-of-labor-study`
(Durkheim, *The Division of Labor in Society*) is the designated exemplar. Theory and
Thinkers Hubs: none yet. Designate the first completed analysis in each hub as its
exemplar in the hub portal page, and hold subsequent pages to it.

---

## Collection Coverage Map

The collection is new; the map starts empty. **Maintain this table from evidence**: on
each ingest, update the touched rows; run a fuller audit when the collection stabilizes.

| Area | Coverage | Notes |
|---|---|---|
| Sociology — classical (Durkheim, Weber, Marx, Simmel) | Unaudited | |
| Sociology — postwar and contemporary | Unaudited | |
| Cultural anthropology — classic ethnographies | Unaudited | |
| Cultural anthropology — contemporary | Unaudited | |
| Biological anthropology / archaeogenetics | Unaudited | aDNA literature is largely post-2010 — date-stamp everything |
| Linguistic anthropology / historical linguistics | Unaudited | |
| Archaeology — method and theory | Unaudited | |
| Archaeology — regional syntheses and site reports | Unaudited | |
| Histories of the disciplines | Unaudited | |
| Methods literature (qualitative and quantitative) | Unaudited | |

Populate `Structural_Sources.md` with a tiered acquisition/ingestion list as the
collection takes shape. The user's day-to-day working checklist is
`Outstanding sources.md` — every ingest that matches a line there must leave a ✅
(or ⚠️) on that line; `Structural_Sources.md` remains the acquisition/queue ledger.

---

## Division of Labor

**I handle**: sourcing, directing focus, adjudicating contradictions when asked, asking
questions, reading the wiki, deciding what matters.

**You handle**: all writing, cross-referencing, maintenance, filing, bookkeeping, and
link management. Every word in `wiki/` is yours unless I explicitly edit it.
