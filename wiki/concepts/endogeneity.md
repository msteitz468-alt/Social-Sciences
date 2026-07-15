---
title: "Endogeneity"
concept_type: analytical
coined_by: ["James Heckman"]
date_coined: "1970s–1980s econometric formulation; qualitative-research formulation by King, Keohane, and Verba 1994"
disciplines: [political-science, sociology, methodology]
emic_or_etic: etic
operationalized_as: "Detected via nonzero covariance between an explanatory variable and the model's disturbance term, formalized as E(b) = b + Bias, where Bias arises from feedback running from the dependent variable back to the explanatory variable."
contested: "no"
related_concepts: ["[[selection-bias]]", "[[omitted-variable-bias]]", "[[causal-effect]]", "[[causal-inference]]", "[[conditional-independence]]", "[[control-variables]]", "[[research-design]]"]
sources_ingested: 1
last_updated: 2026-07-10
tags: [concept, methodology]
---

## Definition as Coined

Endogeneity is an econometric concept naming the condition in which an explanatory
variable's observed value is partly a *consequence*, rather than solely a *cause*, of
the dependent variable — a structural problem in nonexperimental research, since
researchers rarely control the assignment of their explanatory variables. **King,
Keohane, and Verba** (1994; hereafter KKV) state the definition directly: "endogeneity
[is] that the values our explanatory variables take on are sometimes a consequence,
rather than a cause, of our dependent variable" (attributed to KKV 1994). KKV formalize
the resulting distortion as E(b) = b + Bias, where the bias term derives from nonzero
covariance between the explanatory variable and the disturbance term — an econometric
signature of feedback running from Y back to X (attributed to KKV 1994).

## Semantic History

Endogeneity has long been a central concern of econometrics (simultaneous-equations
bias, instrumental-variables literature, Heckman-style selection models for
sample-selection-induced endogeneity). KKV's contribution to the social-science
methodology literature was to import this apparatus into qualitative and small-n
comparative research, presenting it alongside [[selection-bias]] and
[[omitted-variable-bias]] as one of several sources of "bias and inefficiency" that
qualitative researchers must diagnose even without running a regression (attributed to
KKV 1994). Unlike selection bias, which concerns which cases enter a study, endogeneity
concerns the causal *direction* of a relationship within the cases already selected —
KKV treat it as sometimes an intrinsic feature of a research question (e.g., arms races)
rather than a fixable design defect.

## Operationalizations

KKV enumerate **five remedies** for coping with endogeneity in a study already underway
(attributed to KKV 1994):
1. **Correcting a biased inference** by estimating the direction and rough magnitude of
   the bias analytically, even without new data.
2. **Parsing the dependent variable** to isolate the component that is genuinely
   dependent, removing the endogenous portion from the outcome measure itself.
3. **Transforming the endogeneity problem into an omitted-variable problem** by
   identifying and controlling for the variable that jointly drives both X and Y.
4. **Selecting observations without the endogeneity problem** — choosing cases where the
   feedback loop from Y to X plausibly does not operate.
5. **Parsing the explanatory variable** into exogenous and endogenous components and
   using only the exogenous part in the analysis.

KKV also hold that **random assignment**, where feasible in large-n research,
eliminates endogeneity outright: "random assignment of values of the explanatory
variables eliminates the possibility of endogeneity... and measurement error... [and]
makes omitted variable bias extremely unlikely" (attributed to KKV 1994) — though they
note this guarantee weakens as sample size shrinks, echoing their small-n caveat on
[[selection-bias]].

## Applications

KKV illustrate each remedy with a worked case (attributed grounding, not separate wiki
pages): David Laitin's (1986) reverse-causation critique of Weber's Protestant-ethic
thesis — that people already inclined toward capitalism may have left the church for
that reason, reversing Weber's causal arrow (attributed to KKV 1994, citing Laitin 1986
and Tawney 1935); the congressional constituency-service paradox, in which legislators
at greatest electoral risk perform the most constituency service, masking a true
positive effect of service on vote share (attributed to KKV 1994); Gary King's (1991a)
incumbency-advantage study, which parsed the dependent variable to isolate the
incumbency-attributable component of the vote and found a positive constituency-service
effect of roughly 1.54 percentage points per $10,000 spent (attributed to KKV 1994,
citing King 1991a); the Weimar/proportional-representation debate, in which prior
social fragmentation was identified as an omitted variable driving both PR adoption and
parliamentary collapse, transforming an apparent PR→collapse endogeneity problem into an
omitted-variable one (attributed to KKV 1994, citing Lakeman and Lambert 1955, against
Hermens's 1941 PR-causes-collapse thesis); Nina Halpern's (1993) study of Stalinist
economic doctrine, which selected China and Yugoslavia as cases where Soviet military
coercion could not explain command-economy adoption, isolating the causal role of ideas
(attributed to KKV 1994); Verba, Schlozman, and Brady's parsing of church attendance
into an exogenous civic-skills component and an endogenous political-stimulation
component, using only the former as the explanatory variable (attributed to KKV 1994);
and arms-race and alliance research, where KKV treat endogeneity as effectively
unavoidable, since military spending or alliance choice is itself shaped by
anticipation of war (attributed to KKV 1994).

Endogeneity diagnostics are central to KKV's broader argument in
[[king-keohane-verba-designing-social-inquiry-study]] that qualitative and quantitative
research share "a single logic of inference" — a claim contested on
[[king-keohane-verba-single-logic-debate]] — and the concept bears on the
[[qualitative-quantitative-divide-debate]] more generally, since KKV present formal
econometric diagnostics as translatable into qualitative research practice without
regression.

## Critiques and Limitations

KKV themselves flag that not every instance of endogeneity is remediable within a given
study — arms-race and alliance research is presented as a case where the problem is
"intrinsic rather than a fixable design flaw" (attributed to KKV 1994), meaning the five
remedies are a a toolkit of partial fixes rather than a guarantee that endogeneity can
always be eliminated. The random-assignment solution is explicitly limited to large-n
settings; KKV do not claim it resolves endogeneity in small-n or single-case qualitative
designs, where several of the parsing and case-selection remedies instead apply. As with
[[selection-bias]], critics in the [[qualitative-quantitative-divide-debate]] have
questioned how cleanly a formalism built for regression models (nonzero covariance with
a disturbance term) transfers to interpretive qualitative traditions that do not build
explicit statistical models of their cases — a dispute recorded, not adjudicated, on
[[king-keohane-verba-single-logic-debate]].
