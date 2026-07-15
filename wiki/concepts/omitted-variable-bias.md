---
title: "Omitted Variable Bias"
concept_type: analytical
coined_by: ["econometric tradition (regression specification-error literature)"]
date_coined: "mid-20th-century econometrics; qualitative-research formulation by King, Keohane, and Verba 1994"
disciplines: [political-science, sociology, methodology]
emic_or_etic: etic
operationalized_as: "Formalized as E(b1) = b1 + Fb2, where F is the correlation between the included and omitted explanatory variables and b2 is the omitted variable's own effect on the dependent variable; bias arises only if the omitted variable both affects the dependent variable and correlates with the included variable."
contested: "no"
related_concepts: ["[[endogeneity]]", "[[selection-bias]]", "[[control-variables]]", "[[causal-effect]]", "[[causal-inference]]", "[[multicollinearity]]", "[[comparative-method]]", "[[research-design]]"]
sources_ingested: 1
last_updated: 2026-07-10
tags: [concept, methodology]
---

## Definition as Coined

Omitted variable bias is the standard econometric name for the distortion in a
regression coefficient that arises when a variable causally relevant to the outcome is
left out of the model and is correlated with an included explanatory variable. **King,
Keohane, and Verba** (1994; hereafter KKV) restate the condition as **two jointly
necessary requirements**: an omitted variable biases the estimate of an explanatory
variable's effect on the dependent variable only if it (a) affects the dependent
variable, *and* (b) is correlated with the included explanatory variable — either
condition alone being absent avoids bias (attributed to KKV 1994). KKV quote their own
formulation: "we can omit a control variable if either / The omitted variable has no
causal effect on the dependent variable... or / The omitted variable is uncorrelated
with the included variable" (attributed to KKV 1994).

## Semantic History

The concept is a staple of regression-based econometrics predating KKV by decades; KKV's
distinct contribution, as with [[selection-bias]] and [[endogeneity]], was to present
the specification-error logic as a diagnostic qualitative researchers can apply
informally — reasoning about direction and plausibility of omitted confounds — without
running a regression. In *Designing Social Inquiry*, omitted-variable bias is presented
alongside measurement error, the inclusion of irrelevant variables, and endogeneity as
one of four sources of "bias and inefficiency" in causal inference (attributed to KKV
1994).

## Operationalizations

KKV formalize the bias as **E(b1) = b1 + Fb2**: the estimated effect of the included
variable equals its true effect plus a bias term equal to the correlation (F) between
the included and omitted variable, multiplied by the omitted variable's own effect (b2)
on the dependent variable (attributed to KKV 1994, quoting "E(b1) = b1 + Fb2"). This
formalization lets researchers reason about the *direction* of likely bias even without
data on the omitted variable itself, since the sign of F and b2 can often be argued from
substantive knowledge.

Two safe-to-omit conditions follow directly:
- **Irrelevant omitted variables cause no bias** — a variable with zero effect on the
  dependent variable cannot bias inference regardless of its correlation with the
  explanatory variable (attributed to KKV 1994, quoting "irrelevant omitted variables
  cause no bias").
- **Omitted variables uncorrelated with the explanatory variable cause no bias, even if
  influential** — a variable strongly affecting Y but uncorrelated with X can safely be
  dropped without biasing the causal estimate, though at a cost to forecasting power
  (attributed to KKV 1994, quoting "we can safely omit control variables, even if they
  have a strong influence on the dependent variable, as long as they do not vary with
  the included explanatory variable").

KKV also warn against a specific, easily-missed failure mode, **post-treatment bias**:
researchers should not control for a variable that is itself a consequence of the key
explanatory variable, since doing so misattributes part of the true causal effect to the
control (attributed to KKV 1994, quoting "in general, we should not control for an
explanatory variable that is in part a consequence of our key causal variable"). More
generally, KKV argue that choosing which variables to control for cannot be done
atheoretically: "without a theoretical model, we cannot decide which potential
explanatory variables should be included in our analysis" (attributed to KKV 1994) —
without such a model, researchers risk either omitted-variable bias or trivial,
data-mined results.

KKV further flag a subtler variant arising from matching designs: choosing units that
match on some control variables but differ on the key explanatory variable can render
the matched cases "special" in a way that introduces a new, unidentified confound. KKV
state the diagnostic bluntly: "the odds are that something is 'special' about Country B.
Why is it not getting aid if it has such favorable conditions?... the something that is
'special' is an omitted variable that will cause bias" (attributed to KKV 1994).

## Applications

KKV illustrate the concept with Helen Milner's study of U.S. and French trade policy
(*Resisting Protectionism*), in which Milner controlled for the severity of import
competition by selecting for study only industries severely affected by foreign
competition — holding that confound constant by case selection rather than statistical
control — while KKV note this leaves other variables (public opinion, ideology, labor)
uncontrolled and costs the design some efficiency from restricting case variation
(attributed to KKV 1994, quoting "Milner dealt with this problem by selecting for study
only industries that were severely affected by foreign competition. Hence, she held
constant the severity of import competition"). KKV also use the omitted-variable
framework to reject the classical comparative-politics "most similar systems" versus
"most different systems" design debate (Lijphart against Przeworski and Teune) as
underspecified, since it ignores the question of "similar in relation to what," proposing
instead that researchers maximize leverage over the causal hypothesis directly
(attributed to KKV 1994, citing Lijphart; Przeworski and Teune).

Omitted-variable bias is one of the four sources of bias and inefficiency KKV catalog in
their chapter on causal inference (alongside measurement error, irrelevant-variable
inclusion, and [[endogeneity]]), and functions as a formal bridge concept in their
argument for [[king-keohane-verba-designing-social-inquiry-study]]'s "single logic of
inference" claim, contested on [[king-keohane-verba-single-logic-debate]] and bearing
on the wider [[qualitative-quantitative-divide-debate]].

## Critiques and Limitations

KKV's own framework limits the concept's force in two directions they state explicitly:
bias requires *both* correlation with the included variable *and* an effect on the
dependent variable, so intuitions that "more controls are always safer" are not
supported by their formalization — over-controlling risks post-treatment bias, and
KKV's matching discussion shows that control-variable choices can introduce new,
unidentified confounds rather than only removing old ones. As with [[endogeneity]] and
[[selection-bias]], KKV insist the diagnostic requires a theoretical model to select
candidate controls in the first place, so the concept cannot be applied mechanically
without prior substantive argument about which variables are causally relevant — a
limitation KKV state directly rather than treat as a gap in their own account.
