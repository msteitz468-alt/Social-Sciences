# Binford ingest — new-page authoring brief (integration subagents)

You AUTHOR ONE new wiki page from already-extracted claims. You own its slug exclusively —
no other agent writes it, so you may use the Write tool to create it directly.

## Where the claims are (grep ALL of these for your page's slug and topic)
- New Perspectives (1968): `/home/mark/Documents/Social Sciences/scratchpad/binford_new_perspectives_cache/claims/range_1.md` … `range_5.md`
- In Pursuit of the Past (1983): `/home/mark/Documents/Social Sciences/scratchpad/binford_pursuit_cache/claims/range_1.md` … `range_4.md`
- Nunamiut Ethnoarchaeology (1978): `/home/mark/Documents/Social Sciences/scratchpad/binford_nunamiut_cache/claims/range_1.md` … `range_8.md`, plus `range_2b.md`, `range_gapA.md`, `range_gapB.md`

`grep -rin "<your-slug>\|<keyword>" <those dirs>` to find every claim tagged to your page,
then read the surrounding claim blocks for the grounding quotes.

## Voice & attribution (MANDATORY)
- Binford's program/theory/interpretive claims → **attributed voice** ("Binford argued…",
  "(Binford 1983)"). Never state a Binford framework claim as wiki-voice fact.
- Brute facts (what the book did, fieldwork dates, index definitions) → wiki voice OK.
- Nunamiut ethnographic facts → past tense, dated to the **1969–1973 fieldwork** / mid-20th-c.
  — NEVER the ethnographic present.
- Date-stamp method/dating claims; note calibration where relevant.

## Canonical links you may use (bare `[[slug]]`)
binford-lewis, binford-sally-r, bordes-francois, processual-archaeology,
culture-historical-archaeology, middle-range-theory-archaeology, ethnoarchaeology,
actualistic-studies, faunal-analysis, taphonomy, utility-index, site-formation-processes,
formation-processes, archaeological-record, ethnographic-analogy, nunamiut,
binford-bordes-mousterian-debate, agricultural-revolution, cultural-ecology,
universal-evolution, juhoansi, binford-in-pursuit-of-the-past-1983,
binford-nunamiut-ethnoarchaeology-1978, binford-binford-new-perspectives-1968,
binford-nunamiut-ethnoarchaeology-study. Do NOT invent other page links — write non-page
names as plain prose (no brackets). Do NOT bracket descriptive phrases in frontmatter lists.

## Quality bar
Fill ALL frontmatter fields for the page type (use `[[unknown]]` only where genuinely
unclear). Write complete body sections per the schema I give you — real prose grounded in
quotes, not stubs. Include the reflexivity/critique/limitations section the schema requires.
`last_updated: 2026-07-10`, `sources_ingested:` = number of the three Binford books that
bear on the page (1–3). Report the file you wrote and any cross-links the main thread should add.
