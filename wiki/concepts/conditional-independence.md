---
title: "Conditional Independence"
concept_type: analytical
coined_by: ["[[king-gary]]", "[[keohane-robert]]", "[[verba-sidney]]"]
date_coined: "1994"
disciplines: [political-science, sociology, methodology]
emic_or_etic: etic
operationalized_as: "The assumption that, after controlling for explanatory variables, the process assigning values to those variables is independent of the values taken by the dependent variable; satisfied automatically by random selection and assignment, or achievable without randomization by identifying and controlling for the (nonrandom) assignment process itself"
contested: no
related_concepts: ["[[causal-effect]]", "[[causal-inference]]", "[[unit-homogeneity]]", "[[counterfactual]]", "[[selection-bias]]", "[[endogeneity]]", "[[omitted-variable-bias]]", "[[control-variables]]"]
sources_ingested: 1
last_updated: 2026-07-10
tags: [concept, methodology]
---

## Definition as Coined

King, Keohane, and Verba (KKV) define conditional independence as "the assumption that
values are assigned to explanatory variables independently of the values taken by the
dependent variables" (King, Keohane, and Verba 1994). They offer it as the second of two
routes — alongside [[unit-homogeneity]] — around the Fundamental Problem of Causal
Inference (see [[causal-inference]]): where unit homogeneity licenses inference by
treating different units as comparable, conditional independence licenses inference by
ensuring that whatever process determined a unit's value on the explanatory variable was
not itself entangled with the dependent variable.

## Semantic History

KKV present conditional independence as a term of art coined for their methodological
program, formalizing an assumption long implicit in the logic of randomized experiments
and extending it explicitly to observational and qualitative research design. Their
innovation is to decompose the assumption into three named component failures whose
absence jointly constitutes conditional independence: no [[endogeneity]] (the explanatory
variable is not itself caused by the dependent variable), no [[selection-bias]] (units are
not selected into the sample in a way correlated with the dependent variable), and no
[[omitted-variable-bias]] (no uncontrolled variable drives both the explanatory and
dependent variables). KKV state that "random selection and assignment... automatically
satisfy three assumptions that underlie the concept of conditional independence: (1)...
no endogeneity problem; (2)... selection bias... is absent; and (3)... omitted variable
bias... is also absent" (KKV 1994) — an attributed methodological claim, not a
wiki-voice statistical theorem, though it restates a standard result from the
statistical theory of randomized experiments that KKV adopt for social-science design.

## Operationalizations

KKV's central operationalization is that random selection and random assignment of
units to values of the explanatory variable guarantee conditional independence
automatically, without requiring [[unit-homogeneity]]. Where randomization is not
available or was not used, KKV argue conditional independence can still be achieved
non-experimentally if the researcher identifies the (nonrandom) process that generated
values of the explanatory variable and includes an adequate measure of that process
among the study's [[control-variables]]: "if the process by which the values of the
explanatory variables are 'assigned' is not independent of the dependent variables, we
can still meet the conditional independence assumption if we learn about this process
and include a measure of it among our control variables" (KKV 1994). KKV illustrate this
with a comparison of residential segregation and ideology in Israeli–Palestinian West
Bank communities, where accounting for the nonrandom sorting process that placed
residents into communities is treated as substituting for actual random assignment.

## Applications

Conditional independence functions in KKV's framework as the observational-research
analogue to the guarantees provided by a randomized experiment, and is invoked across
their treatment of qualitative and quantitative designs alike as part of the book's
broader "single logic" argument (see [[king-keohane-verba-single-logic-debate]]). It is
also invoked in KKV's discussion of process tracing and mechanism-based research:
individual- or decision-level mechanism studies must still address endogeneity and
omitted-variable bias — the components of conditional independence — at that level of
analysis, not merely at the level of the aggregate research design. Violation of
conditional independence, together with violation of unit homogeneity, is treated by KKV
as a less severe problem for causal inference than an outright
[[indeterminate-research-design]], in which no causal hypothesis can be evaluated at
all regardless of these assumptions.

## Critiques and Limitations

Because conditional independence's non-experimental route depends on the researcher
correctly identifying and measuring the entire nonrandom assignment process, its
credibility rests on a judgment call about whether all relevant confounding channels
have in fact been located and controlled — a difficulty structurally identical to the
standard critique of control-variable-based causal inference more generally (see
[[omitted-variable-bias]]). KKV's own West Bank illustration concedes that meeting the
assumption without randomization requires a substantive causal argument about the
assignment process, not merely a statistical adjustment; where that argument is
incomplete or contested, conditional independence remains an assumption asserted for
the design rather than a demonstrated property of it.
