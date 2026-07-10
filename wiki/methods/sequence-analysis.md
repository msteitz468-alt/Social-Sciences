---
title: "Sequence Analysis"
method_type: analytic
disciplines: [sociology, demography, historical-sociology]
introduced_by: ["[[abbott-andrew]]"]
date_introduced: "1983–1986 (early papers); review synthesis 1995; collected discussion in Time Matters 2001"
supersedes: ["[[unknown]]"]
epistemic_leverage: "Compares whole trajectories (careers, institutionalization paths, life courses) as ordered strings rather than as cross-sectional variable bundles; recovers typical sequences, distances between careers, and order-sensitive patterning that net-effects models miss."
key_limitations: ["Requires careful colligation of events vs occurrences", "Alignment algorithms (e.g. optimal matching) embed substitution/indel costs that are theoretically consequential", "Descriptive pattern search does not by itself supply causal identification", "Computational and coding burden; sensitivity to alphabet definition"]
sources_ingested: 1
last_updated: 2026-07-09
tags: [method, methodology]
---

# Sequence Analysis

## What It Does

Treats social processes as **ordered sequences of events** (careers, professionalization steps, policy adoptions, interaction turns) and analyzes resemblance, typology, and structure of those sequences. In sociology associated especially with [[abbott-andrew|Andrew Abbott]] (*[[abbott-time-matters-2001|Time Matters]]*; *Annual Review of Sociology* 1995 “Sequence Analysis”) and with [[optimal-matching]] algorithms borrowed from biology and computer science. Central formal tool of Abbott's [[narrative-positivism|narrative positivism]] program — relaxing the sequence and time-horizon assumptions of [[general-linear-reality|GLR]].

## Procedure

Summary resolution (wiki, not a manual), from Abbott's account (attributed):

1. **[[colligation|Colligate]]** — bind happenings into coherent **events** at one narrative level ([[event-occurrence-distinction|event vs occurrence]]).
2. Encode each case as a **string** over an event alphabet (optionally with duration).
3. Measure pairwise **distances** — often via [[optimal-matching]] (minimum-cost alignment); alternatives include other edit metrics, enumeration (common in demography), or Abell-style homomorphisms.
4. **Cluster or scale** the distance matrix to recover sequence types / “plots.”
5. Interpret substantively (typical careers, order of institutionalization, welfare-state sequences, etc.).

Abbott (ch. 6, attributed) groups related formal work into families: modeling (time series, event history, games), formal description of narrative structure (Heise ESA; Abell comparative narrative), and empirical categorization (OM + scaling).

## Assumptions and Limitations

- Order and duration are theoretically load-bearing (contra GLR assumption 4).
- Cost matrices and event coding are theory-laden; biological defaults may not map to social meaning.
- Pattern discovery is closer to **description** than to Hempelian covering-law causal identification — a point Abbott embraces (epilogue: methodological narrative work is explicitly descriptive; theoretically, narrative can still be explanatory).
- Empty regions of state space and local regularities matter; main-effects models can misdescribe sparse trajectory data (ch. 5, attributed).

## History

Abbott's path (attributed, *Time Matters* prologue):

- 1981 Rutgers historical-sociology course → focus on sequence/order
- Reverse-engineering of methods; *History and Theory*; structuralist sequence (Propp, Todorov, Barthes)
- “Sequences of Social Events” (*Historical Methods* 1983)
- Seriation of professionalization; **order-statistics failure** (Wilensky problem) → discarded draft chapters of *System of Professions*
- “Event Sequence and Event Duration” (1984) — colligation and measurement
- Contact with Joseph Kruskal → Sankoff optimal matching → Abbott & Forrest 1986 (e.g. morris-dance and later career applications)
- Parallel formalisms: Peter Abell on narrative syntax; demographers often by enumeration rather than alignment
- “Sequence Analysis” *ARS* 1995; collected methodological essays in *Time Matters* 2001

## Exemplary Applications

Professions and medical-community institutionalization; careers; welfare-state sequences; interaction sequences — as discussed in *Time Matters* (attributed). Applications are illustrations of method, not independent substantive findings for wiki voice.

## Debates

Reception within event-history community (Abbott notes critiques, including Wu 1999); cost-scheme and colligation disputes; relation to [[qualitative-quantitative-divide-debate]] and to [[case-oriented-vs-variable-oriented]] work (shared discontent with pure variable ontology, different formal solutions than [[qualitative-comparative-analysis|QCA]]).
