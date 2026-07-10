---
title: "Optimal Matching"
method_type: analytic
disciplines: [sociology, biology, computer-science, historical-sociology]
introduced_by: ["Joseph Kruskal", "David Sankoff", "[[abbott-andrew]] (sociological application)"]
date_introduced: "biology/CS literature pre-1980s; sociological import mid-1980s (Abbott & Forrest 1986)"
supersedes: ["[[unknown]]"]
epistemic_leverage: "Gives a principled distance between whole sequences by minimum-cost alignment (substitutions, insertions, deletions), enabling clustering of careers and institutional paths."
key_limitations: ["Substitution and indel costs are theoretically arbitrary unless justified", "Sensitive to sequence length and alphabet", "Alignment similarity ≠ shared generative process"]
sources_ingested: 1
last_updated: 2026-07-09
tags: [method]
---

# Optimal Matching

## What It Does

Dynamic-programming **alignment** of two sequences to compute a minimum-cost edit distance. Imported into sociology as the workhorse distance for [[sequence-analysis]] by [[abbott-andrew|Abbott]] and collaborators (*[[abbott-time-matters-2001|Time Matters]]* prologue; Abbott & Forrest 1986).

## Procedure

1. Define an alphabet of states/events.
2. Assign costs for substituting one state for another and for inserting/deleting states (indels).
3. Compute optimal alignment cost via dynamic programming.
4. Use the distance matrix for clustering, scaling, or typology of sequences.

## Assumptions and Limitations

Cost schemes **encode theory**. Biological default costs may not map to social meaning. Distance is a descriptive similarity measure — not proof of shared causal mechanism. Sensitive to alphabet grain and sequence length.

## History

Kruskal–Sankoff tradition in sequence comparison. Abbott (attributed, prologue) contacted Joseph Kruskal after order-statistics problems destroyed seriation-based chapters on professionalization; Kruskal sent a preprint of the Kruskal–Sankoff book chapter on optimal matching. Software lineage includes programs used for bird-song sequence comparison (David Bradley for his biologist brother), adapted for social data. First sociological applications: Abbott & Forrest 1986; later career and institutional sequences; Abbott & Barman 1997 on alignment and Gibbs sampling; Abbott & Tsay 2000 review.

## Exemplary Applications

Sociological sequence analyses of careers, professions, cultural performances (e.g. dance sequences in early work), and related domains — see [[sequence-analysis]].

## Debates

Cost sensitivity; whether OM should be replaced or supplemented by other sequence metrics; relationship to event-history models; whether distances recover theoretically meaningful types.
