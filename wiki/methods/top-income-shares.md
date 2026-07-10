---
title: "Top Income Shares"
method_type: analytic
disciplines: [economic-sociology, political-economy, sociology]
introduced_by: ["Simon Kuznets (early); revived and scaled by Atkinson, Piketty, Saez and collaborators"]
date_introduced: "1950s Kuznets; systematic multi-country revival ~2000s"
supersedes: ["[[unknown]]"]
epistemic_leverage: "Tracks upper-tail income concentration when household surveys top-code or undercover the rich"
key_limitations: ["tax-unit definitions", "tax avoidance and evasion", "income definition changes", "labor vs capital income composition requires additional splits"]
sources_ingested: 1
last_updated: 2026-07-09
tags: [method]
---

# Top Income Shares

## What It Does

Uses income-tax tabulations (and related fiscal data) to estimate shares of total income held by the top 10%, 1%, 0.1%, etc., over long periods—often linked to national-income control totals. In *[[piketty-capital-twenty-first-century-2014|Capital in the Twenty-First Century]]*, the World Top Incomes Database (WTID; ~30 researchers; Atkinson, Piketty, Saez, Alvaredo, Dell, Banerjee, Qian, et al.) is the primary income-inequality source. The method answers questions surveys cannot: evolution of the extreme upper tail, labor vs capital composition *within* the top, and century-scale U-curves.

Piketty prefers **decile/centile share tables** to synthetic indices (Gini, Theil, P90/P10): official interdecile ratios ignore everything above the 90th percentile and can give an artificially rosy picture when the top decile holds 20%, 50%, or 90% of the total.

## Procedure

1. **Fiscal tabulations** from progressive income taxes (often introduced around WWI: US 1913, France 1914, Britain 1909, India 1922, Argentina 1932).
2. **Pareto interpolation** and related techniques on grouped tax statistics; align with national-income denominators.
3. **Decompose** labor income (wages, salaries, bonuses, options) vs capital income (rent, dividends, interest, profits, capital gains, royalties); track composition as one climbs the top decile (“the 9 percent” vs “the 1 percent”).
4. **Present primary (before-tax) distributions** in standard tables (Piketty Tables 7.1–7.3 style: bottom 50% / middle 40% / top 10% and top 1%).
5. **Caveats applied case-by-case:** capital gains inclusion (better in US than France, where Piketty often excludes them); underreporting corrections (France: +2–3 points, up to ~5 under high-evasion assumptions, to capital’s share); tax-haven and undeclared capital income.

Scale note: France ~2013, ~50 million adults → top centile ≈ 500,000 people; US ~260 million adults → top centile ≈ 2.6 million.

## Assumptions and Limitations

- Depends on tax law, filing units, and compliance; missing non-filers and exempt incomes.
- Income definitions change (capital gains treatment differs across countries and time).
- Tax returns do **not** show whether capital was inherited or saved from labor.
- Household surveys alone, Piketty argues, give a “biased and misleadingly complacent” view—especially in emerging economies where tax publication often deteriorated after computerization or disaffection with progressive tax.
- “Black hole” of growth: official production growth can exceed survey income growth; for India 1990–2000, rise in top centile share may explain one-quarter to one-third of the gap (as of Piketty’s estimates).

## History

Kuznets’s 1953 *Shares of Upper Income Groups in Income and Savings* covered only the United States 1913–1948—first ambitious historical income-share measurement of this kind—finding top-decile share fall from 45–50% of national income to ~30–35%. Piketty attributes the 1914–1945 compression largely to wars and shocks, not Kuznets’s later “bell curve” of tranquil intersectoral mobility, and treats the 1955 AEA presidential optimistic reading as partly Cold War product.

Atkinson–Piketty–Saez multi-country revival and WTID made the method infrastructure for *Capital* and later WID.world. French estate taxes since 1791 complement income tax (from 1914) for wealth concentration; US labor-income detail only from 1927 despite federal income tax from 1913.

## Exemplary Applications

Findings below are **attributed to Piketty (2014)** from the series in [[piketty-capital-twenty-first-century-study]] Part Three.

### Orders of magnitude (Tables 7.1–7.3 style)

| Dimension | Low (e.g. Scandinavia 1970s–80s) | Medium (e.g. Europe ~2010) | High (e.g. US ~2010) | Extreme (e.g. Europe ~1910 wealth; US 2030? income) |
|---|---|---|---|---|
| Labor top 10% | ~20% | ~25% | ~35% | ~45% (projection) |
| Wealth top 10% | ~50% (Scand. “medium”) | ~60% | ~70% | ~90% (Europe 1910) |
| Total income top 10% | ~25% | ~35% | ~50% | ~60% (US 2030? projection) |

Labor: bottom 50% typically ~25–35% of labor income. Wealth: bottom 50% invariably <10%, generally <5% (France 2010–11: top 10% 62%, bottom 50% 4%; US Fed survey: top 10% 72%, bottom 50% 2%—surveys understate largest fortunes).

### France (Ch.8)

- Top decile of national income: 45–50% on eve of WWI → 30–35% today; drop ~15 points of NI.
- Top centile: >20% of NI (1900–1910) → 8–9% (2000–2010); almost entirely collapse of top *capital* incomes (“fall of the rentier”); top wage centile stable ~6–7% of wages.
- Compression concentrated 1914–1945; three postwar phases: rise 1945–67 (top decile <30%→36–37%); fall 1968–83 (back to ~30%); rise after 1983 (~33% by 2000–2010).
- Within top: capital exceeds labor only in top 0.1% by 2005 (vs top 0.5% still capital-dominated in 1932).

### United States (Ch.8–9)

- 1900–1910 top decile ~40%+ of NI (below Europe’s 45–50%); 1920s peak >50% on eve of 1929.
- Lowest ebb 1950–1980: top decile 30–35% of NI.
- Explosion since 1980: top decile 30–35% (1970s) → 45–50% (2000s); slightly >50% eve of 2008 and early 2010s with underreporting awareness. Excluding capital gains: ~32% → >46% (~14 points structural).
- Bulk of rise to “the 1%”: ~9% → ~20% of NI (+11 of ~15 points to top decile); roughly half of that to top 0.1%.
- 1977–2007: richest 10% appropriated ~3/4 of growth; richest 1% nearly 60%; bottom 90% income growth <0.5%/year.
- Mechanism: unprecedented wage inequality—[[supermanagers]]; top wage decile 25%→35% explains ~2/3 of top-decile NI rise; capital income ~1/3. Vast majority (60–70%) of top 0.1% in 2000–2010 are top managers; athletes/artists <5%.

### Cross-country (Ch.9)

- Anglo-Saxon top-centile takeoff since 1980 (US ~20% early 2010s; Britain/Canada 14–15%; Australia 9–10%) vs milder continental Europe/Japan (+2–3 points of NI to top 1%).
- Emerging long series (South Africa, India, Indonesia, Argentina): top centile same order of magnitude as rich countries in high phases; China estimate ~10–11% in 2000–2010; Colombia ~20% 1990–2010.

## Debates

How much of the post-1980 rise is real vs fiscal artifact; capital-gains and tax-haven bias; Gini vs share tables; education–technology vs institutions for top labor incomes—see [[piketty-capital-debate]] and study Critiques. Secondary reanalyses not fully ingested.
