---
title: "Network Constraint"
concept_type: measurement-construct
coined_by: ["[[burt-ronald-s|Ronald S. Burt]]"]
date_coined: "1992 (Structural Holes, ch. 2)"
disciplines: [sociology]
emic_or_etic: etic
operationalized_as: "An ego-network index Cij = (proportional investment in reaching contact j, direct + indirect)^2 × (organization of j's cluster, Oj); aggregate C = Σj Cij, ranging 0 (contact fully replaceable) to 1 (sole contact). Implemented in the software STRUCTURE."
contested: yes
related_concepts: ["[[structural-holes]]", "[[tertius-gaudens]]", "[[structural-holes-theory]]", "[[network-analysis]]"]
sources_ingested: 2
last_updated: 2026-07-10
tags: [concept]
---

# Network Constraint

*(Attributed to [[burt-ronald-s|Burt]].)* **Network constraint** is the formal
ego-network measure that operationalizes [[structural-holes|structural holes]]:
the extent to which a player's network time and energy is invested in contacts who
are *not* separated by holes, and so who leave the player few opportunities to
broker. It is the workhorse variable in every empirical test in
*[[burt-structural-holes-1992|Structural Holes]]*. Its inverse — freedom from
constraint at one's own end plus holes at the other — is **structural autonomy**.

> This page records the **measurement construct**. For the underlying idea see
> [[structural-holes]]; for the analytic tradition it extends see [[network-analysis]].

## Definition as Coined

The constraint that contact *j* poses on player *i* combines two things
[FACT — measurement definitions]:

- **Investment in reaching *j*** — *i*'s proportional time and energy invested in
  *j* directly, plus indirectly through other contacts *q* who are tied to *j*:
  the quantity *p_ij + Σ_q p_iq p_qj*.
- **Lack of holes around *j*** — the degree to which *j*'s surrounding cluster is
  organized (*O_j*), i.e. whether *j*'s potential replacements are themselves
  connected.

The contact-specific constraint is *C_ij = (p_ij + Σ_q p_iq p_qj)² × O_j*, and
aggregate constraint is *C_i = Σ_j C_ij*, ranging from 0 (a contact wholly
replaceable through disconnected alternatives) to 1 (a sole contact). Burt's
interpretation: "Contact *j* constrains your entrepreneurial opportunities to the
extent that (a) you've made a large investment of time and energy to reach *j*,
and (b) *j* is surrounded by few structural holes with which you could negotiate."
Constraint is based on **dependence** (exclusive access); the companion redundancy
measure is based on **connection** — "the redundancy measure is based on
connection; the constraint measure is based on dependence, indicated by exclusive
access."

Related summary measures from the same chapter: **effective size** (the count of
non-redundant contacts), **efficiency** (effective size ÷ observed size), and
**hierarchy** (a Coleman–Theil disorder index measuring how far constraint is
concentrated in a single relationship — empirically distinct from the *level* of
constraint).

## Semantic History

"Constraint" in Burt's technical sense (1992) descends from his own earlier
*Toward a Structural Theory of Action* (1982) and, more distantly, from the
Coleman–Theil disorder index of mathematical sociology (for the hierarchy
component) and from Freeman's centrality and industrial-organization concentration
ratios (for the cluster-organization component). The term should not be confused
with "constraint" in ordinary usage or in structural-equivalence blockmodeling: in
Burt it names a specific quantity — dependence on non-substitutable contacts. After
1992 the measure was absorbed as a standard network statistic (the "Burt
constraint") in social-network software beyond his own STRUCTURE package, and its
inverse — brokerage/structural autonomy — became the more commonly cited framing.

## Operationalizations and Debates

- **Exclusive vs. marginal access.** Burt contrasts his exclusive-access formula
  (using proportional strength *p_qj*) with an alternative using raw marginal
  strength *m_qj*. The two are identical in one-contact and zero-density networks —
  which is why existing exchange-network lab studies (Cook & Emerson and others,
  all run in zero-density networks) could not decide between them — but diverge as
  networks grow. Burt's market and manager tests (Ch. 3–4 appendices) favour the
  **exclusive-access** measure on construct-validity grounds.
- **Data sources.** Constraint can be built from sociometric choices, joint-
  involvement counts, or direct interaction measures (e.g., dollar flows). Where
  no relational data on the surrounding cluster exist, *O_j* can be crudely
  approximated from concentration ratios (markets) or status attributes — Burt
  flags the attribute proxy as "a weak measure in two ways."
- **Adjusted constraint.** For players crossing a status boundary, Burt adds
  coefficients capturing the sponsorship value of a hierarchical network built
  around a strategic partner (the *λ* terms; see the legitimacy finding on
  [[burt-structural-holes-study]]).
- **Robustness.** Constraint estimated from limited survey-style data correlates
  0.998 with constraint estimated from full economy-wide data — the measure is
  recoverable from partial networks.

## Applications

- **Markets** — aggregate constraint predicts (lower) profit margins across 77 US
  product markets, *R²* ≈ 0.53 ([[burt-structural-holes-study|Ch. 3]]).
- **Managers** — constraint predicts (later) promotion, but the effect is small in
  aggregate and strongly moderated by rank, sex, and insider/outsider status
  ([[burt-structural-holes-study|Ch. 4]]).
- **Structural autonomy** as a nonlinear function of constraint — holes have their
  greatest effect "at low levels of constraint," a diminishing-returns curve
  fitted in both study populations.
- **Brokerage and Closure (2005)** — constraint remains the workhorse inverse of
  brokerage; nonlinear performance and idea-value associations restated as
  stylized facts #1–#2 (supply-chain managers; multi-sample corroboration). See
  [[vision-advantage]], [[burt-brokerage-and-closure-2005]].

## Critiques and Limitations

The measure inherits the [[structural-holes|concept's]] contested status: it
records the *absence* of ties precisely but infers the *presence* of holes
indirectly; its returns are contingent (the legitimacy reversal); and its causal
priority over outcomes is not established by cross-sectional data. As a
contribution to [[network-analysis]] it extends the cohesion and structural-
equivalence traditions and borrows its hierarchy component from Coleman's
mathematical sociology and its cluster-organization component from Freeman's
centrality and from industrial-organization concentration ratios.
