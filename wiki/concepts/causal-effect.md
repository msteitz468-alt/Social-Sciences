---
title: "Causal Effect"
concept_type: analytical
coined_by: ["Rubin / Holland (statistical formalization); qualitative-research formulation by [[king-gary]], [[keohane-robert]], [[verba-sidney]]"]
date_coined: "Rubin model 1970s–80s (Holland 1986); KKV formulation for qualitative research 1994"
disciplines: [political-science, sociology, methodology]
emic_or_etic: etic
operationalized_as: "The difference between the systematic component of an outcome when the explanatory variable takes one value and its systematic component when the variable takes another value — the 'mean causal effect' β = E(Y_I) − E(Y_N)"
contested: yes
related_concepts: ["[[counterfactual]]", "[[causal-inference]]", "[[unit-homogeneity]]", "[[conditional-independence]]", "[[selection-bias]]", "[[omitted-variable-bias]]", "[[endogeneity]]"]
sources_ingested: 1
last_updated: 2026-07-10
tags: [concept, methodology]
---

# Causal Effect

## Definition as Coined

A causal effect is, in [[king-gary|King]], [[keohane-robert|Keohane]] & [[verba-sidney|Verba]]'s (KKV) formulation, the difference a cause makes to an outcome, defined **counterfactually**. In *[[king-keohane-verba-designing-social-inquiry-1994|Designing Social Inquiry]]* (1994) they define it (attributed) as "the difference between the systematic component of observations made when the explanatory variable takes one value and the systematic component of comparable observations when the explanatory variable takes on another value." Because the two conditions cannot both be realized for one unit (the Fundamental Problem of Causal Inference; see [[causal-inference]]), the causal effect is a theoretical quantity, not a directly observable one.

KKV distinguish three formalizations (attributed): the **realized causal effect** for a single unit (the difference between its actual and its counterfactual outcome — theoretical and unobservable); the **random causal effect** (varying across hypothetical replications); and the **mean causal effect**, β = E(Y_I) − E(Y_N), the systematic feature actually targeted by estimation.

## Semantic History

The definition extends (attributed) Holland's (1986) statement of the **Rubin causal model** from statistics into qualitative and comparative social science. KKV insist the definition is "logically prior" to the identification of causal mechanisms: identifying a mechanism, they argue, itself requires causal inference at every link, so a mechanisms-only account (they cite Little 1991) leads to infinite regress rather than replacing the counterfactual definition. They likewise treat Ragin's "multiple causation"/equifinality and Lieberson's symmetric/asymmetric distinction as problems of *inference and specification*, not rival definitions of the causal effect — positions recorded on [[king-keohane-verba-single-logic-debate]].

## Operationalizations

KKV stress (attributed) that a causal effect is undefined without a precisely specified counterfactual contrast: one must state *which* two values of the explanatory variable are compared and *what is held constant* while it changes. A critical corollary: one must **not** hold constant variables that are themselves consequences of the explanatory variable, because "controlling for enough of the consequences of incumbency could make one incorrectly believe that incumbency had no effect at all" — the post-treatment-control problem (see [[omitted-variable-bias]]). Estimation of β proceeds under [[unit-homogeneity]] or [[conditional-independence]] and is judged, like descriptive estimators, by unbiasedness and efficiency.

## Applications

- KKV's running incumbency-advantage example: the causal effect of incumbency is the incumbent's systematic vote under incumbency minus the vote the same unit would systematically receive without it.
- The **constant-effect** assumption (a weaker form of unit homogeneity): units may differ in baseline expected outcome yet share a constant additive causal effect — the assumption KKV say underlies comparative case studies (see [[comparative-method]]).

## Critiques and Limitations

The counterfactual definition is contested. Jon Elster (1983) argued (attributed position) that counterfactual statements cannot render the meaning of causality where a third factor produces both apparent cause and effect; KKV read this as a warning about the difficulty of *inference*, not a refutation of the *definition*. Mechanism-oriented and interpretive critics hold that a difference-making definition abstracted from process misses what causal explanation in the social sciences is for. These positions are recorded on [[king-keohane-verba-single-logic-debate]] and [[counterfactual]]; this page does not adjudicate them.
