---
title: "Variable Rule"
concept_type: analytical
coined_by: ["[[labov-william]]"]
date_coined: "1969–1972 (copula chapter; formalized with Cedergren & Sankoff probability model)"
disciplines: ["linguistics", "sociolinguistics"]
emic_or_etic: etic
operationalized_as: "Ordered phonological/grammatical rules with probabilistic application (φ, p₀) constrained by linguistic environment and social factors; frequencies predicted rather than free variation assumed; principle of accountability for all environments"
contested: no
related_concepts: ["[[sociolinguistic-variable]]", "[[variationist-sociolinguistics]]", "[[black-english-vernacular]]", "[[speech-community]]", "[[observers-paradox]]"]
sources_ingested: 1
last_updated: 2026-07-15
tags: [concept]
---

## Definition as Coined

[[labov-william]] introduced the **variable rule** as a formal device for incorporating systematic variation into generative grammar. In the copula chapter of *Language in the Inner City* (1972; first published in *Language* 1969, radically revised for the book), Labov argued that neither “optional” parentheses nor “free variation” nor categorical dialect-mixture models (always / never / free) capture the gradients of forms such as full, contracted, and deleted *is/are* in [[black-english-vernacular|Black English Vernacular (BEV)]].

Labov held that each variable rule has a probability φ (between 0 and 1) of applying in a given environment, predicting relative frequency over the population of eligible environments rather than treating each token as random. In the Cedergren–Sankoff revision adopted in the 1972 version, φ is treated as an **abstract property of the rule for the speech community**, not merely a sample-specific output frequency. Formal notation uses angled brackets for variable outcomes and constraints (e.g. X → \<Y\> / A \_ B), with starred features marking near-invariance (v ≈ 1).

The concept is inseparable from the **principle of accountability**: any variable form must be reported as the proportion of cases in which it occurred in the relevant environment over the total cases in which it might have occurred. Labov argued that isolated examples can “prove any theory,” whereas accountable frequencies reveal regular patterns of the [[speech-community|speech community]].

## Semantic History

The 1969 *Language* paper stated contraction and deletion as variable rules with an earlier mathematical interpretation in which φ was closer to observed output frequency. For *Language in the Inner City*, Labov reported a **revised mathematical interpretation** following Cedergren and Sankoff (1972): a product model of independent constraints,

φ = 1 − (1 − p₀)(1 − vᵢ)(1 − vⱼ) … (1 − vₙ),

where **p₀** is the input probability of the rule (varying with age, style, class, sex, ethnicity) and the **v** terms are constraint weights. Labov equated the independence-of-constraints hypothesis with the legitimacy of assembling subrules into rule schemata (Chomsky & Halle abbreviatory conventions): if constraints were not independent, many free empirical φ values would replace a smaller parameter set.

Within the same volume, Labov had already used informal variable-rule sketches (angled brackets and asterisk constraints) for (r) and t,d deletion in Chapter 2, arguing that BEV and white nonstandard (WNS) (r) rules differ by simple constraint adjustments rather than wholly separate systems. Chapter 3 is the full formal development. Later variationist practice (Varbrul/GoldVarb and successors) generalized the apparatus beyond Labov’s generative phonology framing; that later history is outside the present ingest.

## Operationalizations

In the BEV **copula** case study, Labov operationalized two ordered variable phonological rules embedded in a seventeen-rule chain (about half shared with Standard English):

1. **Rule 10 — contraction**: remove schwa before ≤1 consonant in a word carrying a tense marker, yielding a lone oral continuant (e.g. *is* → [z]). Favored by preceding pronoun (+Pro), preceding vowel/glide, and following verbal/future environments.
2. **Rule 13 — auxiliary deletion**: remove the lone oral continuant left by contraction ([z] from *is*; also [v] from *have*; not [m] of *I’m*). Grammatical constraints parallel contraction; **phonetic** constraints are opposed — deletion favored by preceding consonant, contraction by preceding vowel.

Labov’s decisive claim was that surface zero copula in environments such as *He a friend*, *He working*, *He gon’ try* is not absence of high-level *be* insertion, nor free dialect mixture, but **ordered contraction then deletion** of residual consonant — with categorical environments (clause-final *is/are*, tags, yes-no questions under emphasis, modals/infinitives/imperatives, *I’m* at ~99%) showing that finite *is/are* are present underlyingly.

Quantitative operationalization used multi-track peer-group sessions and interviews with south-central Harlem groups ([[south-central-harlem-youth|Thunderbirds, Aces, Cobras, Jets, Oscar Brothers]]), adult samples, and white Inwood controls. Cedergren and Sankoff estimated contraction parameters for twelve cells of Labov’s Table 3.5 by maximum likelihood (e.g. p₀ = 0.25; v(Pro_) = 0.95; v(V_) = 0.65; v(_gon) = 0.89); predicted contracted counts closely matched found counts, supporting constraint independence. Wolfram’s Detroit analysis (1969) and other city studies were cited as convergent replications of the qualitative and quantitative relations.

Related BEV variables treated in the same program include final t,d and s,z cluster simplification, r-lessness (including intervocalic vocalization), and (elsewhere in the volume) negative concord as a variable rule contrasted with obligatory negative attraction.

## Applications

- **BEV copula contraction/deletion** — the paradigm application; Labov argued that *He wild* is equivalent to SE *He’s wild*, not *He is wild*, so the applied task is teaching control of contraction *without* ensuing deletion, not simply “adding *is*” ([[labov-language-inner-city-study]]).
- **(r) and t,d deletion** — informal variable-rule statements showing BEV vs WNS differ by relative constraint weights (phonological vs grammatical) rather than presence/absence of rules (Ch. 2).
- **Speech-community grammar** — Labov claimed variable-constraint profiles were essentially the same across peer groups studied, so the rule is part of a single grammar constructable for that community, more regular than any idiolect.
- **Program-level payoffs** Labov listed: most general form of linguistic rule; relations between rules; relations between rule systems (dialect range); historical change; acquisition toward community norms.

See [[variationist-sociolinguistics]] for the research program that made variable rules a signature formalism, and [[sociolinguistic-variable]] for the measurement construct that variable rules formalize as competence-level knowledge.

## Critiques and Limitations

Within *Language in the Inner City*, Labov anticipates and rejects treating variable constraints as mere “performance” wastebasket: the constraints require grammatical categories and boundaries and are interwoven with categorical rules, so quantitative relations *are*, he argued, the form of the grammar. He also rejected simple bidialectal “switch” models for closely related dialects: learning new rules influences old ones.

Limitations that the source itself flags or that follow from its design:

- **p₀ social dimensions** are only partly unpacked in Ch. 3; the chapter focuses on relatively uniform vernacular of male black street-culture members, with later chapters linking deletion rates to distance from that culture (members vs lames).
- **Adult grammars** recorded only in interviews, not long-term peer observation — Labov cautioned against firm claims about adult vernacular rates (see [[observers-paradox]]).
- **Creole-origin arguments** are noted as historical background, not settled by the synchronic variable-rule analysis; Labov’s synchronic claim is surface-rich, underlying-structure-shared dialect difference.
- Later field debates over whether probabilistic rules belong in competence, and over generative vs purely statistical implementations of constraint models, are not covered by this ingest and should not be projected onto Labov 1972 in wiki voice.
