---
title: "Chronicle of the Maya Kings and Queens (2nd edition)"
author: ["Simon Martin", "Nikolai Grube"]
year: 2008
source_type: reference
disciplines: [archaeology]
era_coverage: [critical-turn, contemporary]
region_coverage: [mesoamerica]
methodological_approach: [archaeological, historical, linguistic]
reliability_notes: "Thames & Hudson 2nd ed. 2008 (1st ed. 2000); popular-scholarly dynastic chronicle based on post-decipherment epigraphy + archaeology. Not a primary excavation report — dynastic reconstructions, war narratives, and overkingship claims are attributed to Martin & Grube (as of 2008). Glyph readings and absolute dates follow the Thompson correlation (GMT) as used by the authors. Fast-moving epigraphy and LIDAR after 2008 may revise individual reigns, toponyms, and settlement scale. Source PDF is Adobe Paper Capture OCR (2009); text layer is complete (preface–index) but noisy — names and dates verified against context when garbled. Word-count intake: 241 PDF pages / ~98.5k words / 17,469 body lines — complete volume (epilogue, notes, bibliography, index present)."
study_page: 
pages_created: 4
pages_updated: 18
ingested: 2026-07-15
tags: [source]
---

# Chronicle of the Maya Kings and Queens (Martin & Grube, 2nd ed. 2008)

Dynastic political history of eleven Classic Maya kingdoms, by epigraphers [[martin-simon|Simon Martin]] and [[grube-nikolai|Nikolai Grube]] (Thames & Hudson; 1st ed. 2000, **2nd ed. 2008**). Dedicated to [[schele-linda|Linda Schele]] (1942–1998). Reconstructs royal biographies, wars, marriages, and hierarchical “overkingship” networks from hieroglyphic monuments and archaeology — the standard post-decipherment political narrative that textbooks (e.g. [[coe-houston-the-maya-2015]], [[sharer-traxler-ancient-maya-2006]]) compress as the Tikal–Calakmul “Great Game.”

## Framing (Preface, attributed — Martin & Grube)

- Classic Maya never a single empire: a patchwork of **60+ kingdoms**, each under a [[kuhul-ajaw|holy lord]], locked in struggles for autonomy or dominance.
- Especially successful rulers built far-flung patronage networks as **overkings** — no kingdom held permanent regional monopoly.
- The book examines **11** of the most influential / best-documented dynasties shaping the Classic highpoint.
- Decipherment (after Proskouriakoff, Knorosov, Schele generation) lets kings and queens speak through their own monuments.

## Section Plan

| Section | Book pp. | Cache lines | Focus |
|---|---|---|---|
| Front matter + TOC | 1–5 | 1–143 | Title, dedication, contents |
| Preface: Discovering the Maya Past | 6–7 | 144–249 | Stephens/Catherwood; decipherment; book aims |
| Introduction | 8–23 | 250–1328 | Periods; map; writing & calendars; royal culture; Classic politics; comparative timelines |
| Tikal | 24–53 | 1329–3390 | Mutul dynasty; *entrada*; hiatus; Late Classic recovery; Terminal Classic end |
| Dos Pilas | 54–67 | 3391–4237 | Bajlaj Chan K'awiil exile dynasty; Calakmul alliance; wars with Tikal |
| Naranjo | 68–83 | 4238–5271 | Foreign domination; Lady Six Sky; K'ahk' Tiliw Chan Chaak |
| Caracol | 84–99 | 5272–6390 | 6th-c. rise; wars with Tikal; hiatus; Late Classic recovery |
| Calakmul | 100–115 | 6391–7433 | Snake (Kaan) dynasty; 6th–7th-c. hegemony; defeat by Tikal 695 |
| Yaxchilan | 116–137 | 7434–8913 | Itzamnaaj Bahlam III; Lady K'abal Xook; Bird Jaguar IV |
| Piedras Negras | 138–153 | 8914–9970 | Proskouriakoff’s breakthrough site; dynastic sequence |
| Palenque | 154–175 | 9971–11517 | K'inich Janaab Pakal; dynastic crises; artistic peak |
| Tonina | 176–189 | 11518–12369 | Militaristic hillside capital; Baaknal Chaak; Palenque wars |
| Copan | 190–213 | 12370–13979 | Yax K'uk' Mo' founding; 16 kings; artistic florescence |
| Quirigua | 214–225 | 13980–14677 | Vassal under Copan; K'ahk' Tiliw Chan Yopaat revolt; giant stelae |
| Epilogue: Fall of the Sacred Kings | 226–230 | 14678–15111 | Terminal Classic end of divine kingship |
| Notes, Bibliography, Index | 231–240 | 15112–end | Apparatus (not extracted for claims) |

## Extraction plan

**7-agent** content-weighted line-range extraction (`scratchpad/martin_grube_maya_kings_cache/`). Claims inventory expected: `claims/range_1.md` … `range_7.md`. Main-thread owns high-stakes synthesis ([[classic-maya]], [[classic-maya-collapse-debate]], overkingship model) and new thinker pages; site densifications may be page-partitioned after claims review.

## Volume Synthesis Note

*Chronicle of the Maya Kings and Queens* (2nd ed. 2008) is the vault’s primary **dynastic political narrative** for Classic lowland Maya civilization. Where [[coe-houston-the-maya-2015]] and [[sharer-traxler-ancient-maya-2006]] synthesize geography, settlement, economy, and collapse at handbook scale, Martin & Grube deliver reign-level biography for eleven kingdoms and make [[overkingship]] — *yajaw* vassalage, foreign-supervised accessions, patronage without territorial empire — the explicit organizing model of Classic politics.

**What this ingest adds:** dense, date-stamped political arcs for [[tikal]], [[calakmul]], [[caracol]], [[dos-pilas]], [[naranjo]], [[yaxchilan]], [[piedras-negras]], [[palenque]], [[tonina]], [[copan]], and [[quirigua]]; a concept page for overkingship; thinker pages for [[martin-simon]] and [[grube-nikolai]]; and an attributed multi-causal Terminal Classic position (ecological overshoot + drought as exacerbator + failed hegemonies) on [[classic-maya-collapse-debate]]. Load-bearing narrative spine: AD 378 *entrada* → 562 Tikal defeat → 7th-c. Snake hegemony → 695 Tikal recovery → Petexbatun/Lady Six Sky → 738 Copan–Quirigua break → 9th-c. fall of public sacred kingship.

**Limits:** popular-scholarly synthesis as of 2008 epigraphy (GMT correlation); OCR source text is noisy; post-2008 LIDAR demography and revised glyph readings will supersede some details. Not a studies/hub candidate (reference chronicle, not a single landmark research act). Pair always with Coe & Houston / Sharer & Traxler for settlement and collapse paleoclimate breadth, and with [[coe-breaking-the-maya-code-2012]] for decipherment historiography.

## Extraction notes

7-agent content-weighted extraction (`scratchpad/martin_grube_maya_kings_cache/`): range_1 intro (70) · range_2 Tikal (78) · range_3 Dos Pilas+Naranjo (80) · range_4 Caracol+Calakmul (120) · range_5 Yaxchilan+Piedras (68) · range_6 Palenque+Tonina (93) · range_7 Copan+Quirigua+Epilogue (100) = **~609 claims**, inventory 7/7 non-empty, zero silent dropout.
