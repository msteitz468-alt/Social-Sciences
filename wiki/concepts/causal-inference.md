---
title: "Causal Inference"
concept_type: analytical
coined_by: ["general statistical/methodological pedigree; qualitative-research formulation by [[king-gary]], [[keohane-robert]], [[verba-sidney]]"]
date_coined: "long pedigree; KKV formalization for qualitative research 1994"
disciplines: [political-science, sociology, methodology]
emic_or_etic: etic
operationalized_as: "Estimation of a [[causal-effect]] (a mean difference in the systematic component of an outcome across values of an explanatory variable) under assumptions of [[unit-homogeneity]] or [[conditional-independence]]; judged by unbiasedness and efficiency"
contested: yes
related_concepts: ["[[causal-effect]]", "[[counterfactual]]", "[[descriptive-inference]]", "[[unit-homogeneity]]", "[[conditional-independence]]", "[[observable-implications]]", "[[selection-bias]]", "[[endogeneity]]", "[[omitted-variable-bias]]"]
sources_ingested: 1
last_updated: 2026-07-10
tags: [concept, methodology]
---

# Causal Inference

## Definition as Coined

Causal inference is the drawing of conclusions about causal effects from observed data. In *[[king-keohane-verba-designing-social-inquiry-1994|Designing Social Inquiry]]* (1994), [[king-gary|King]], [[keohane-robert|Keohane]] & [[verba-sidney|Verba]] (KKV) present it, alongside [[descriptive-inference]], as one of the two forms of inference that define scientific research, and argue (attributed) that it obeys the **same logic in qualitative and quantitative research**. The object estimated is the [[causal-effect]], which KKV define counterfactually.

KKV adopt (attributed) Holland's (1986) statement of what they call the **Fundamental Problem of Causal Inference**: because only one of the two counterfactual conditions is ever realized for any unit, a causal effect can never be observed directly — "no matter how perfect the research design, no matter how much data we collect… we will never know a causal inference for certain." Causal inference is therefore always inference under uncertainty, licensed by assumptions rather than by direct observation.

## Semantic History

The counterfactual framing KKV use descends from the statistical literature on experiments (Neyman, Fisher) and its formalization as the Rubin causal model (Holland 1986). KKV's contribution (attributed) was to carry this apparatus into **qualitative and small-n research**, arguing that comparative case studies rest on the same assumptions as regression — chiefly [[unit-homogeneity]] (units with the same value of the explanatory variable share an expected outcome) or, alternatively, [[conditional-independence]] (values of the explanatory variable are assigned independently of the outcome). Random selection and assignment, they note, satisfy conditional independence automatically by ruling out [[endogeneity]], [[selection-bias]], and [[omitted-variable-bias]] at once; absent randomization, the analyst must control the assignment process.

The concept's meaning has continued to move since 1994: the "credibility revolution" in the social sciences (natural experiments, instrumental variables, regression discontinuity, difference-in-differences) and the qualitative reply of *causal-process observation* both post-date KKV and are, in part, reactions to it.

## Operationalizations

KKV extend the descriptive-inference criteria to causal estimators (attributed): an estimator of the causal effect β is **unbiased** if it equals β on average across hypothetical replications, and its **efficiency** is judged by variance across those replications (efficiency rising with the variance of the explanatory variable). They give a least-squares proof of unbiasedness under their assumptions. In the small-n / qualitative setting the same logic is realized through disciplined comparison and through multiplying [[observable-implications]] rather than through formal estimation.

KKV argue (attributed) against two evasions of causal inference: refusing all causal language for fear of "correlation is not causation," and relabeling unexamined speculation as "explanation." Both, they hold, dodge the disciplined work of inference.

## Applications

- The **n = 1 problem**: KKV argue a single true observation cannot escape the Fundamental Problem; they reject Eckstein's "crucial case" logic on three grounds (most explanations involve more than one causal variable; measurement is imperfect; social reality is not deterministic).
- **Process and mechanism evidence**: [[process-tracing]] is treated (attributed) as a way of generating more observations along a decision chain — but one that must still satisfy unit homogeneity, endogeneity, and omitted-variable standards.
- KKV's sample-size formula makes the number of observations needed a function of fundamental variability, tolerated uncertainty, collinearity, and the variance of the causal variable — yielding a rough rule of thumb of "more than five but fewer than twenty" in the simplest case.

## Critiques and Limitations

KKV's account is contested. Critics in the [[qualitative-quantitative-divide-debate|qualitative–quantitative]] and [[king-keohane-verba-single-logic-debate|single-logic]] debates argue (attributed) that reducing causal inference to a data-set-observation, regression-analogue logic undervalues the distinct leverage of within-case mechanistic evidence, and that "increase the number of observations" can smuggle in heterogeneity that violates the very [[unit-homogeneity]] assumption the inference requires. Rival framings — Elster's counterfactual skepticism, Little's causal-mechanisms view — are recorded as positions on the debate pages, not adjudicated here.
