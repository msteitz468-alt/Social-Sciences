---
title: Principal Component Analysis (in population genetics)
method_type: statistical
disciplines: [population-genetics, archaeogenetics, sociology]
introduced_by: []
date_introduced: mid-20th century (statistics); applied to human genetics by Cavalli-Sforza (1970s–1990s)
supersedes: []
epistemic_leverage: >-
  Summarizes genome-wide variation across many individuals into a few axes,
  making population structure visible and letting ancient samples be projected
  against present-day variation.
key_limitations: >-
  Axes are summaries, not history; gradients can arise without migration, and the
  geometry can mislead about the direction of population movements.
sources_ingested: 2
last_updated: 2026-07-10
tags: [method]
---

# Principal Component Analysis (in population genetics)

## What It Does

Principal Component Analysis (PCA) reduces high-dimensional genetic data (many
variable positions across many individuals) to a small number of axes capturing
the most variation, so that population structure can be plotted and inspected.
In archaeogenetics it is used both to visualize present-day structure and to
project ancient individuals onto that structure.

## Procedure

Individuals are represented by their genotypes at many positions; the axes
(principal components) that summarize the greatest variance are computed and
plotted, typically the first two. Clusters and gradients in the plot are read as
signals of shared ancestry or admixture, then tested formally with
[[admixture-statistics]].

## Assumptions and Limitations

The central caution (Reich 2018, following John Novembre and colleagues 2008):
**gradients in a PCA/synthetic-map do not straightforwardly encode migrations**.
Novembre showed such gradients can arise without any migration, and that a real
Near Eastern farming expansion could produce a gradient *perpendicular* to the
actual direction of movement — undercutting [[cavalli-sforza-luigi-luca|Cavalli-Sforza]]'s
[[demic-diffusion]] interpretation of European blood-group maps. PCA describes;
it does not by itself demonstrate historical process.

## History

[[cavalli-sforza-luigi-luca|Cavalli-Sforza]], Paolo Menozzi, and Alberto Piazza
built **synthetic maps** of classical gene frequencies using PCA (program
summarized in *Genes, Peoples and Languages*, 2000, from HGHG 1994). For Europe
they moved from 39 genes (with Ammerman, 1978) to 95 genes; first three PCs
explained about half the variation in early work; first five PCs later explained
**28%, 22%, 11%, 7%, and 5%** of variance (as of Cavalli-Sforza 2000). He presents
PCs as successive independent weighted means that can isolate different
migrations when origins differ and replacement is partial (Rendine et al. 1986
simulations). Genome-wide PCA of individuals (not only population means) became
central after the 2000s ([[reich-who-we-are-2018|Reich 2018]]).

### European PC interpretation (as of Cavalli-Sforza 2000)

| PC | Variance | His reading |
|---|---|---|
| PC1 | 28% | Matches radiocarbon cereal-arrival map → Middle Eastern farmer expansion mixing with foragers ([[demic-diffusion]]) |
| PC2 | 22% | N–S cline; climate and/or dual postglacial poles (Basque SW vs Uralic NE) |
| PC3 | 11% | Expansion north of Black/Caspian Seas — aligned with Gimbutas Kurgan / steppe ([[yamnaya-culture]] associated program) |
| PC4 | 7% | Greek colonization first millennium BCE |
| PC5 | 5% | Basque homeland / contraction |

He cautions that PC order only *approximately* tracks time and that PCA is **not
a dating method**.

## Exemplary Applications

- Classical European synthetic maps (HGHG / GPL) — later reinterpreted.
- Modern whole-genome structure plots projecting ancient samples (Reich 2018).

## Debates

The interpretability of gradients and synthetic maps — cautionary case in how a
descriptive statistic was over-read as direct evidence of migration (Novembre
2008; aDNA revision of [[demic-diffusion]]). Still indispensable for visualization;
insufficient alone for historical inference.

## Key sources

- [[cavalli-sforza-genes-peoples-languages-2000]]
- [[reich-who-we-are-2018]]
