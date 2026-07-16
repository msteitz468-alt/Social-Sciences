---
title: Ancient DNA
method_type: data-collection
disciplines: [archaeogenetics, biological-anthropology, archaeology]
introduced_by: [[[paabo-svante]]]
date_introduced: 1980s (mitochondrial); 2009–2010 (genome-wide)
supersedes: []
epistemic_leverage: >-
  Direct genetic evidence from people who actually lived in the past, rather
  than inferences projected backward from present-day variation; can detect
  migration, admixture, and population turnover that present-day genomes cannot
  recover.
key_limitations: >-
  DNA degrades and fragments after death; overwhelming microbial contamination;
  modern-human contamination; preservation bias toward cold, dry climates
  (Eurasia over the Near East and sub-Saharan Africa); silent on language,
  culture, and self-identification.
sources_ingested: 4
last_updated: 2026-07-15
tags: [method]
---

# Ancient DNA

## What It Does

Ancient DNA (aDNA) recovers and sequences genetic material from the remains of
long-dead organisms — for human prehistory, chiefly from bone and teeth. Whole-
genome aDNA lets researchers place ancient individuals directly into the tree of
population relationships and detect [[admixture]] events, making it, in Reich's
(2018) claim, a more definitive source on *what happened* in deep population
history than archaeology or historical linguistics.

## Procedure

Powder is drilled from skeletal remains (the petrous portion of the temporal
bone is an especially rich source); DNA is extracted and converted to a
sequenceable library. Because typically only a tiny fraction of recovered DNA is
endogenous (Reich reports ~0.02% for the ~40,000-year-old Tianyuan individual,
the rest microbial), the key enabling step is **in-solution hybridization
capture**: synthetic ~52-base "bait" sequences, tiling >1 million informative
genome positions, bind and enrich the target human DNA (developed by Matthias
Meyer and Qiaomei Fu in [[paabo-svante|Pääbo]]'s laboratory; scaled to whole-
genome "factory" throughput by [[reich-david|Reich]] and Nadin Rohland).
Robotics allow one worker to process ~90+ samples at once; sequences are then
computationally sorted, authenticated against contamination, and analyzed with
[[admixture-statistics]].

## Assumptions and Limitations

- **Preservation and recovery bias.** Success rates track climate — Reich (2018)
  reports ~75% for cold Russian samples vs. ~30% for the hot Near East —
  systematically skewing the sampled record toward some regions.
- **Contamination.** Both microbial and modern-human; requires stringent
  authentication (characteristic aDNA damage patterns, controls).
- **Evidence-class silence.** aDNA speaks to *populations, kinship, and
  demography*, never directly to language or ethnicity — enforce the four-way
  non-identity (see [[admixture]], [[ghost-population]]).
- **Sampling frames are content.** Which sites and skeletons get sampled shapes
  which populations become visible.

## History

Early aDNA (1980s–2000s) was limited to short mitochondrial fragments and
plagued by contamination. Genome-wide aDNA arrived 2009–2010 (first archaic
[[neanderthals|Neanderthal]] and [[denisovans|Denisovan]] genomes, plus a
~4,000-year-old Greenlander). Capture methods and next-generation sequencing
drove an exponential data explosion after 2015 (Reich 2018).

## Exemplary Applications

The steppe migration into Europe; [[ancestral-north-indians]] /
[[ancestral-south-indians]] in South Asia; Denisovan discovery; multiple
migration pulses into the Americas — all as reported in [[reich-who-we-are-2018|Reich (2018)]].

## Debates

Whether aDNA has genuinely "surpassed" archaeology (Reich's framing) or is one
evidence class among several; how to prevent nationalist and racial misuse of
origins claims ([[race-and-genomics-debate]]); the revival of migrationism
against processual archaeology's anti-migrationism.

## From Renfrew & Bahn (2012)

*(Attributed — *[[renfrew-bahn-archaeology-2012|Archaeology]]* 6th ed., Ch. 11 “Who Were They?”.)* Renfrew & Bahn place aDNA within the [[bioarchaeology]] of people (human remains from sites; osteology still fundamental for biological profile). Landmark narrative: [[paabo-svante|Svante Pääbo]] first extracted/cloned mtDNA from a 2400-year-old Egyptian mummy (1985); later PCR from bone/tooth >5000 years old led to Neanderthal mtDNA (1997) and the 2010 draft Neanderthal genome — “a new era in biological anthropology.” Applications they highlight: DNA sexing of fragmentary/infant remains (e.g. Ashkelon neonates); kinship at Eulau (Corded Ware Tomb 99 — father, mother, two sons as earliest genetic nuclear family, with Sr isotopes showing non-local women); pathogen aDNA (TB bacterium in a 900-year-old Peruvian mummy, proving pre-European presence in the Americas).

On deep history they report Cann, Stoneking & Wilson’s 1987 mtDNA “Eve” result and Out-of-Africa expansion ~60,000 years ago as widely accepted against multiregional continuity; living-population genetics cannot recover extinct lineages, so aDNA is required. The 2010 Vindija Neanderthal genome estimates divergence ~440–270 kya and **1–4% Neanderthal gene flow** into non-Africans (possibly Middle Eastern mixing before Eurasian expansion); Denisovan aDNA marks a further distinct lineage. Gene–language correlations (Cavalli-Sforza et al.) are noted with caution: language changes faster than genes and elite dominance can decouple them (attributed, as of 2012 textbook).

## Stringer — *Lone Survivors* (2012)

*Source: [[stringer-lone-survivors-2012]], [[stringer-chris]]; method history and archaic-genome applications **as of Stringer 2012**.*

**Field history.** aDNA took off in the early 1980s with partial mtDNA of the quagga (museum skins); PCR (1984) made millions of copies of specific sequences feasible. Early work targeted **mtDNA** because cells hold hundreds/thousands of copies vs one nuclear autosomal set, and the mtDNA genome was fully known by 1981. First Neanderthal mtDNA (1997) from the 1856 Neander Valley skeleton (Pääbo); by Stringer’s writing, **20+ Neanderthal fossils** had yielded mtDNA. By 2006 two international teams produced first large-scale Neanderthal **autosomal** maps; partial 2006 genomes had contamination problems (perhaps ~15% modern DNA in places). Composite nearly entire Neanderthal genome drafted by >50 researchers, predominantly three Vindija female bone fragments (~40 ka); >3 billion bits of coding reconstructed. **454 Life Sciences** shotgun sequencing (~250,000 strands/~5 hours per machine) suited tiny nuclear fragments; **SPEX** (Brotherton et al.) offered a more targeted approach.

**Key sites and preservation.** Vindija (Croatia) and El Sidrón (Spain) especially valuable; Stringer notes possible cannibalism/defleshing at both may have aided DNA preservation by limiting proximate decay; Vindija leg fragments had the best Neanderthal DNA preservation then known. Tropical/subtropical heat and humidity severely impair aDNA — unfortunate for *Homo floresiensis*; northern Asia and high-altitude sites better; bone **proteins** may survive where DNA does not. Cro-Magnon aDNA published but some sequences carry lingering contamination doubts; damage-signal authentication expected to resolve early modern authenticity.

**What autosomal aDNA revealed that mtDNA/Y could not.** mtDNA/Y-DNA long suggested zero or near-zero Neanderthal–Cro-Magnon admixture (simulations near zero), but they are only ~1% of DNA; autosomal data revealed ~**2% Neanderthal** input in non-Africans and **Denisovan** relatedness to Melanesians (~5% Denisovan; total archaic ~8% in New Guinea/Bougainville as of Stringer 2012). Head-lice DNA also used to probe archaic contact. Cann–Stoneking–Wilson 1987 modern mtDNA had the biggest pre-Neanderthal genetic impact on origins research; Stringer holds later analyses showed 1987 conclusions essentially correct though somewhat overinterpreted. Australian fossil aDNA claims (Willandra/Kow Swamp/Mungo 3, 2001) used to support Multiregional/Assimilation; Stringer, Cooper, and Collins criticized exceptional recovery rates under desert heat and protocols — reanalysis showed Mungo 3 was not an outgroup and did not seriously challenge recent African origin.

See [[neanderthals]], [[denisovans]], [[molecular-clock]], [[recent-african-origin]], [[admixture-statistics]].

## African genetics–archaeology interface (*Oxford Handbook*, 2013)

*(Attributed — Scott MacEachern, Ch. 5 “Genetics and Archaeology,” with de Maret Ch. 43 and Blench Ch. 4, in *[[mitchell-lane-oxford-handbook-african-archaeology-2013|Mitchell & Lane 2013]]*; **as of handbook ~2012** — pre-dates much of the post-2015 African aDNA boom. Prefer present-day and early-aDNA literature cited then; do not overwrite later Reich-layer findings.)*

- **Sampling bias:** Genetic research concentrates on forager groups (Khoisan, Pygmy/BaTwa) and some areas (southern Lake Chad Basin); farming populations poorly sampled across central/SW/southern Africa beyond few Bantu groups; gaps between Senegambia and Lake Chad; little Saharan work. Archaeological knowledge similarly patchy; congruence often reflects access/politics, not research design.
- **Mutual failure of disciplines:** Social scientists intimidated by genetics either ignore it or uncritically accept concluding historical paragraphs; geneticists use outdated/superficial African history sources (encyclopedias, mass media, 50-year-old texts). Prehistory syntheses (Phillipson 2005; Stahl 2005) give little weight to genetics especially for recent periods (MacEachern).
- **Deep isolation claims and reflexivity:** Research (e.g. Behar et al. 2008) suggesting San and Pygmy lineages near roots of mtDNA/NRY trees with Middle/Upper Pleistocene isolation must not reinscribe foragers as fossilized remnants; non-adaptive markers do not make carriers “less modern”; “oldest human population” media phrasing conflates genetic variability with historical identity. Isolation over 50–100 kyr hard to reconcile with archaeology alone (MacEachern).
- **Bantu expansion genetics (provisional as of ~2012):** Genetic data indicate substantial demographic movements as well as linguistic/cultural change, but are **not fine-grained enough** to independently locate origins (still from southern Nigeria–Cameroon border via historical linguistics). Lower NRY than mtDNA diversity among Bantu speakers interpreted as asymmetrical reproduction (forager women into farmer communities; polygyny) — yet same asymmetry in Yoruba (no comparable range expansion) weakens this as a full explanation (MacEachern). de Maret: markers *seem to indicate* demic movement if confirmed; risk of uncritical language–genes–agriculture package (Diamond & Bellwood). See [[bantu-expansion]].
- **Four-way non-identity:** Gene clusters ≠ language families ≠ ceramic styles ≠ peoples (Blench; MacEachern; de Maret; Sadr). Use `associated_with`; date-stamp every claim.
- **Preservation:** Tropical heat/humidity severely impair aDNA recovery relative to Eurasia — structural limit for sub-Saharan deep-time genomes until later laboratory advances (contextual note; Stringer layer above already flags tropics).

Cross-links: [[khoe-san]], [[kalahari-debate]], [[phillipson-david-w]], [[admixture]].
