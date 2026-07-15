---
title: "Selection Bias"
concept_type: analytical
coined_by: ["Christopher Achen", "Gary King"]
date_coined: "1980s (Achen 1986; King 1989); qualitative-research formulation by King, Keohane, and Verba 1994"
disciplines: [political-science, sociology, methodology]
emic_or_etic: etic
operationalized_as: "Detected as a truncation or non-random restriction of the observed range of the dependent variable (or of a variable correlated with it), formally producing attenuation or inflation of estimated causal effects relative to their true value."
contested: "no"
related_concepts: ["[[endogeneity]]", "[[omitted-variable-bias]]", "[[descriptive-inference]]", "[[causal-inference]]", "[[causal-effect]]", "[[unit-homogeneity]]", "[[research-design]]", "[[indeterminate-research-design]]", "[[comparative-method]]"]
sources_ingested: 1
last_updated: 2026-07-10
tags: [concept, methodology]
---

## Definition as Coined

Selection bias, in its general statistical form, dates to Achen's (1986) and King's
(1989) work on truncated and censored samples in regression analysis: when cases are
included or excluded according to a rule correlated with the dependent variable, the
observed relationship between explanatory and dependent variables is a distorted
estimate of the true causal relationship. **King, Gary, Robert Keohane, and Sidney
Verba** (*Designing Social Inquiry*, 1994; hereafter KKV) translate this econometric
result into a rule for qualitative and small-n research design. KKV state what they
call the "basic and obvious rule" of case selection: "selection should allow for the
possibility of at least some variation on the dependent variable," and they criticize
research designs that study only wars, only revolutions, or only nonvoters in order to
explain war, revolution, or turnout (attributed to KKV 1994).

## Semantic History

The concept has two intertwined lives. In econometrics it names a formal property of
truncated/censored regression estimators (Achen 1986; Heckman's selection-correction
models; King 1989). KKV's contribution — attributed, not wiki-voice, since it is their
methodological argument — was to generalize this technical result into a design
prescription usable without regression machinery: **do not select cases (or, in
qualitative work, the sole cases available) on values of the outcome you are trying to
explain.** Because the qualitative tradition had few formal tools for diagnosing this,
KKV present the rule as a general translation of a known quantitative pathology into
case-selection logic, illustrated with a worked regression example rather than derived
from qualitative practice itself.

## Operationalizations

KKV formalize the consequence of dependent-variable-correlated truncation: "any
selection rule correlated with the dependent variable attenuates estimates of causal
effects on average," so that "numerical estimates of causal effects will be closer to
zero than they really are" (attributed to KKV 1994, citing Achen 1986 and King 1989). In
qualitative terms, they state, "the true causal effect is larger than the qualitative
researcher is led to believe." They illustrate this with a hypothetical scatterplot of
accounting courses against starting salary (their Figure 4.1): restricting the sample to
salaries at or above $100,000 flattens the regression slope, understating a true
per-course effect of roughly $10,000 as only about $5,000 (attributed to KKV 1994).

KKV distinguish degrees of the problem:
- **Complete truncation** — no variation at all on the dependent variable by design.
  KKV's position is unambiguous: "avoid them! We will not learn about causal effects
  from them" (attributed to KKV 1994).
- **Partial/correlated truncation** — variation exists but is restricted in a manner
  correlated with the outcome. Here KKV argue the resulting bias is at least
  predictable and partially correctable: "our inferences might be biased but they will
  be so in a predictable way that we can compensate for" (attributed to KKV 1994).

They also identify a **converse bias**: when causal effects vary across units and cases
are selected precisely because the effect is known to be large (e.g., Latin American
countries with a recent history of political violence), the resulting estimate of the
average causal effect will be an *overestimate* rather than an underestimate (attributed
to KKV 1994).

Critically, KKV hold that **selection on an explanatory variable causes no comparable
bias**: "selecting observations for inclusion in a study according to the categories of
the key causal explanatory variable causes no inference problems," provided the
variable is controlled for in the analysis, even where it correlates with the dependent
variable (attributed to KKV 1994). This asymmetry — selection on X is permissible,
selection on Y is not — is the operational heart of the concept as KKV present it.

KKV further note that selection bias can be **world-induced** rather than
investigator-induced: historical or political processes themselves truncate the
available evidence, as when a class of stone sculptures survives disproportionately to
wood ones (biasing assessments of early African art), or when only certain
nation-states survive to be studied, as in Tilly's (1975) observation that "England,
France, and even Spain are survivors of a ruthless competition in which most contenders
lost" (attributed to KKV 1994, citing Tilly 1975). Selecting on *both* the explanatory
and dependent variables in a theory-confirming pattern is treated as especially
dangerous — KKV warn it "can describe or explain nothing" — with a narrow exception for
mixed sampling across the marginal distribution of a rare or skewed dependent variable
(attributed to KKV 1994, citing Kohli 1987 on Indian antipoverty policy).

## Applications

KKV ground the concept in a series of illustrative cases (retained here as attributed
grounding rather than as separate wiki pages, per the source's own framing): Skocpol's
studies of social revolutions (selection on the dependent variable); Tilly's (1975)
account of surviving European states (world-induced selection); Kohli's (1987)
three-state study of Indian antipoverty policy (selection on both variables, redeemed
by disaggregating to many sub-observations); Laitin's (1986) Somalia/Yoruba comparison
and Inkeles and Rossi's (1956) industrialization studies (constant explanatory
variables later corrected by extending the case range); and Achen and Snidal's (1989)
critique of deterrence studies that examined only non-deterred "acute crisis" cases.
KKV also cite CDC cancer-cluster methodology as a case where retrospective selection on
extreme dependent-variable values is used only as a heuristic, to be followed by a
confirmatory study selecting on the explanatory variable (attributed to KKV 1994).

Selection bias bears directly on the [[qualitative-quantitative-divide-debate]]: KKV's
central argument in [[king-keohane-verba-designing-social-inquiry-study]] is that a
single logic of inference — in which selection-bias diagnostics translate across
methods — should govern both traditions; see [[king-keohane-verba-single-logic-debate]]
for the resulting dispute over that claim.

## Critiques and Limitations

KKV's own presentation qualifies the rule rather than treating it as absolute: their
"basic and obvious rule" is itself derived from a 3-unit, n=2 worked example in which
they show random selection in small samples produces selection bias "with two-thirds
probability" — a result that qualifies their general endorsement of randomization
(effective mainly in large-n research) with a specific small-n caveat (attributed to KKV
1994). This means the prohibition on selecting on the dependent variable interacts with
sample size and cannot be treated as a context-free rule. Critics within the
qualitative-quantitative divide have also questioned whether the regression-derived
formalism transfers cleanly to interpretive or single-case qualitative work where "the
dependent variable" may not be a well-defined quantitative construct at all — a
position recorded on [[king-keohane-verba-single-logic-debate]] rather than adjudicated
here.
