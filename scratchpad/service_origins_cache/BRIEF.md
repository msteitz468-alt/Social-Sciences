# Extraction Brief — Service, *Origins of the State and Civilization* (1975)

You are a claim-extraction subagent for a social-sciences wiki. Read ONLY your
assigned cache slice (a plain-text OCR excerpt). Do NOT read the wider book, the
wiki, or use outside knowledge. Extract claims **grounded in quotes from your slice
only**, with the source line/section noted where possible.

## The book (context, do not extract from this)
Elman R. Service, *Origins of the State and Civilization: The Process of Cultural
Evolution* (1975). Service's central thesis is the **integrative / managerial /
"benefit" theory of the state**: early states arose because centralized organization
(redistribution, coordination, war-leadership, mediation, bureaucracy) conferred
*benefits* and integrative advantages — NOT primarily from class conflict, coercion,
or repression (contra Fried, Marx/Engels, and the conflict/coercion theorists). He
distinguishes **chiefdom** (redistributional, ranked, no true force monopoly) from
**state** (legitimized monopoly of force / specialized bureaucratic-coercive
apparatus). He uses the band–tribe–chiefdom–state levels of sociocultural integration.

## Voice and Attribution Protocol — MARK EVERY CLAIM
Tag each extracted claim with one register:
- **[WIKI]** — brute descriptive fact (dates, what the book says on p.N, a case's
  reported chronology when source-independent). Rare here.
- **[ATTR]** — any theoretical claim, interpretation, single-source finding. Almost
  everything Service argues is [ATTR] → write "Service argued/held/claimed…".
- **[POS]** — a position in a live dispute (e.g. Service vs. Fried on state origins;
  integrative vs. coercion theory). Note whose position.

This is a **theoretical work** — nearly all content is [ATTR] to Service, or [POS] in
the state-origins debate. Do NOT let Service's theory become wiki-voice fact.

## Output format
Write to your assigned claims file. Group claims under `## Target: <page-slug>`
headings using the established slugs below. Each claim:

```
### <short claim title>
- register: [ATTR|WIKI|POS]
- target: <page-slug(s) it belongs on>
- claim: <one-sentence claim in attributed voice>
- quote: "<short grounding quote from your slice>" (line ~N)
```

If material near-matches a page but the entity differs, file under
`## Target: MISC` with an explicit mismatch flag. Flag verbatim internal duplication
(OCR artifacts) and extract once. In your final summary, state the exact line range
you actually covered and any point a block/cap stopped you short.

## Established page slugs you may link/target (do NOT invent structural names)
Thinkers: service-elman-r, fried-morton-h, sahlins-marshall, steward-julian-h,
white-leslie-a, engels-friedrich, childe-v-gordon, flannery-kent-v
Theories: band-tribe-chiefdom-model, egalitarian-rank-stratified-state-model,
multilinear-evolution, universal-evolution, social-evolutionism, cultural-ecology
Concepts: chiefdom, redistribution, pristine-state, secondary-state,
stratified-society, the-state, levels-of-sociocultural-integration, patrilocal-band,
sodality, urbanization
Phenomena: state-formation
Societies: zulu, banyankole, ashanti, hawaiians
Cultures: olmec-culture, shang-civilization, uruk-culture, harappan-civilization
Sites: teotihuacan, uruk
Debates: service-fried-political-typology-debate, consensus-vs-conflict-debate
NEW pages the main thread is creating (reference these exact slugs when relevant):
- integrative-theory-of-the-state  (Service's benefit/managerial theory)
- origin-of-the-state-integrative-vs-conflict-debate
- service-origins-state-1975  (the source page)
- archaic-state-formation-pathways  (comparison of the archaic civilizations)

Cases not yet paged — if your slice covers them richly, file under `## Target: MISC`
with a "NEW PAGE?" flag and a proposed slug: Ankole→banyankole (exists), Nupe,
Ashanti (exists), Kongo, Cherokee, Tahiti, Tonga, Peru/Chavin/Moche, Egypt (culture?),
Indus/Harappan (exists), China/Shang (exists), Teotihuacan (exists), Oaxaca/Monte-Alban.
Note them; the main thread decides taxonomy.
