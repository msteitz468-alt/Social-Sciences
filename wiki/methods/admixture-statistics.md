---
title: Admixture Statistics (f- and D-statistics)
method_type: statistical
disciplines: [archaeogenetics, population-genetics]
introduced_by: [[[reich-david]]]
date_introduced: 2009–2012
supersedes: []
epistemic_leverage: >-
  Formally test whether a population is a mixture of others and estimate mixture
  proportions and dates, using allele-frequency correlations across populations —
  turning "population mixture" from a narrative into a falsifiable statistical
  claim.
key_limitations: >-
  Detects that mixture occurred and roughly with whom, not the fine geography or
  the cultural meaning; sensitive to reference-population choice; can be confounded
  by unsampled "ghost" populations and by shared drift.
sources_ingested: 1
last_updated: 2026-07-10
tags: [method]
---

# Admixture Statistics (f- and D-statistics)

## What It Does

A family of allele-frequency methods, developed and popularized by
[[reich-david|Reich]] and the mathematician [[patterson-nick|Nick Patterson]], for detecting and
quantifying [[admixture]] between populations. Where earlier work read gradients
off maps, these statistics ask a sharp question: *is population X a mix of
populations related to Y and Z, and in what proportion?*

## Procedure

- **The Four-Population Test (*D*-statistic / ABBA-BABA).** Tests whether four
  populations fit a simple unmixed tree; a significant deviation is evidence of
  gene flow between branches that should be separate. Reich (2018) uses this to
  *prove* that ancient mixture occurred (e.g. Neanderthal ancestry in non-Africans).
- ***f*-statistics (f3, f4).** An *f3* statistic can show a target population is
  admixed (a significantly negative value); *f4*-ratios estimate mixture
  proportions.
- **Admixture graphs.** Fit populations into a graph combining tree-like splits
  with admixture edges, reconstructing networks rather than pure trees.
- **[[principal-component-analysis]]** and model-based clustering complement
  these by visualizing structure.

## Assumptions and Limitations

Results depend on the reference populations chosen; **[[ghost-population|ghost
populations]]** (real but unsampled) can distort inferences until modeled; the
statistics establish *that* and roughly *with whom* mixture happened, not the
migration's fine geography, direction in every case, or social meaning. A
statistical signal of association is `associated_with`, not identity.

## History

Emerged 2009–2012 out of the Neanderthal genome analysis (Reich, Patterson, and
colleagues) and became the standard toolkit of the aDNA revolution.

## Exemplary Applications

Proving Neanderthal admixture; detecting the third ([[yamnaya-culture|steppe]])
ancestral stream in Europeans; the [[ancestral-north-indians]] /
[[ancestral-south-indians]] model for South Asia — all in
[[reich-who-we-are-2018|Reich (2018)]].

## Debates

How much confidence to place in admixture-graph reconstructions given unsampled
ghosts; the balance between genetic inference and archaeological/linguistic
interpretation of the same events.
