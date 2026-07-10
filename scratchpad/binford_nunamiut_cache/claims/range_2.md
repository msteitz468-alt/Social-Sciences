# Nunamiut Ethnoarchaeology (Binford 1978) — range 2 (book lines 3801–7600) — claims

## coverage: ACTUALLY READ book lines ~3801–~4900 only (file offset lines 1–1100 of the
~4300-line slice). This chunk is exceptionally dense (Ch. 2 "Some General
Considerations: Butchering, Kill Sites, and Recording Procedures" — MNI calculation,
the Modified General Utility Index, and the seasonal kill-butchering-location dataset)
and the OCR is very heavily garbled with interleaved data-table noise (the raw text
alternates prose paragraphs with unreadable OCR'd statistical tables — these were
skipped per the brief's "skip pure data tables" instruction, but the *concepts* they
demonstrate were extracted). Given the density, I was not able to complete the full
3801–7600 range within a single reading pass; book lines ~4900–7600 (continuing Ch. 2
into what the brief flags as Ch. 3) were **not read** and should be flagged to the main
thread as a gap for recovery/main-thread reading. Everything below is grounded only in
the ~1100 lines actually read.

### page: utility-index
- [ATTR] Binford argued that a realistic model of butchering/transport behavior at a
  kill site must be based on "anatomical sets" that the hunter actually decides to
  transport or abandon as bundled units, not on the standard list of discrete
  anatomical elements used by conventional faunal analysts. — L311-320 "not rendered
  into units equal in number to the anatomical parts... Instead the anatomy is divided
  into sets that normally contain more than a single bone element... The sets are what
  the hunter decides to transport or abandon."
- [ATTR] Binford proposed a rule that a part of intrinsically low utility value,
  positioned anatomically between two parts of higher value, becomes "assimilated" to
  the adjacent higher-value part in transport/butchering decisions — e.g. the humerus
  (moderate value) was assimilated to the scapula, and the metatarsal (low value) to
  the femur — as a function of the mean utility value of the parts around it. — L364-370
  "the probability of a given part being assimilated to a part of higher value will
  increase as a function of the mean value between the two parts."
- [ATTR/method] From this reasoning Binford built the Modified General Utility Index
  (MGUI), presented in Table 2.7, which corrects the raw (unweighted) General Utility
  Index by merging anatomically-adjacent parts into transport-relevant sets (e.g. the
  cervical vertebrae assimilated with atlas/axis, ribs assimilated with sternum sets,
  humerus raised to scapula value) rather than treating each skeletal element as an
  independent analytic unit. — L301-320, Table 2.7 (L309-378) "This reasoning, applied
  to the data, resulted in a modified general utility index or MGUI (Table 2.7)."
- [WIKI] The General Utility Index (unweighted) is derived by dissecting carcasses of
  both caribou and sheep, measuring meat/muscle-tendon, marrow, and bone-grease
  proportions in the appendicular skeleton, multiplying element-by-element indices by
  these proportions, summing, and standardizing to a 1–100 scale. — L143-233 "Using
  these proportions we may obtain a general utility index by multiplying the
  unweighted indices thus far developed by these proportions, summing the result, and
  standardizing to a scale from 1 to 100."
- [WIKI] In Binford's carcass dissections, meat-and-tendon accounted for 94.04% of the
  gross weight (minus dry bone weight) in caribou and 96.74% in sheep; marrow 4.78%
  (caribou) vs. 2.29% (sheep); bone grease 1.20% (caribou) vs. 0.97% (sheep) — grease
  in meat itself was excluded. — L84-99 "Meat-muscle and tendon-accounted for 94.04% of
  the gross weight minus the dry bone weight in caribou and for 96.74% in sheep. Marrow
  accounted for 4.78% in caribou and only 2.29% in sheep."
- [ATTR] Binford interpreted the contrast between sheep and caribou proportions (higher
  grease/marrow relative to muscle-tendon in the larger-bodied caribou) as reflecting a
  general condition related to body size, generalizable (he suspected but had not yet
  tested) to bison and other large mammals. — L124-146 "the contrasts between sheep and
  caribou in these proportions appear to reflect a general condition related to body
  size... My experience with the bones of bison and other large mammals has led me to
  suspect that the grease-marrow proportions increase with body size."
- [WIKI] Binford found a high positive linear correlation (r = .88) between the general
  utility indices computed independently for sheep and caribou, with the regression
  near a 1:1 relationship (intercept 2.589, slope 1.018), meaning the two species'
  utility profiles are structurally very similar despite differing grease/marrow vs.
  meat balance. — L287-307 "the correlation between the indices for sheep and caribou
  is very high (r = .88)... the intercept value is 2.589 and the slope value is 1.018."
- [ATTR] Binford explicitly linked the MGUI to prediction: kill-butchering-location
  assemblages should show a strong, curvilinear, *negative* relationship between a
  part's general-utility value and its frequency of abandonment at the kill site —
  high-utility parts are transported away (so under-represented at the kill site),
  low-utility parts are left behind (over-represented) — and reports this relationship
  held for nearly all seasonal assemblages examined except summer dispersed kills.
  — L490-502 "There is indeed a strong relationship between the frequencies of parts
  and the MCUI [MGUI] for all assemblages with the possible exception of the data from
  summer dispersed kills. This relationship is uniform in that it is curvilinear and
  negative."
- [ATTR] Binford described a "family" of curves relating kill-assemblage part
  frequencies to the MGUI, ranging from "bulk" strategies (select large quantities of
  high- and moderate-value parts, abandon only the very lowest-utility parts) to
  "gourmet" strategies (select only the highest-value parts, abandon moderate and low
  value), with "sigmoid" or mixed strategies between — and argued the shape of the
  curve reflects situational contingencies of the decision (e.g. transport distance,
  season, logistics), NOT differences in hunters' underlying cultural knowledge of
  anatomy. — L774-828 "curves marked x represent strategies that select for high
  frequencies... abandon parts of the lowest utility at rapidly accelerating rates...
  In no way are they relevant to differences in the 'culture' or knowledge that the
  actors bring to concrete situations."

### page: faunal-analysis
- [ATTR] Binford argued strongly against the conventional zooarchaeological practice of
  calculating Minimum Number of Individuals (MNI) per identification unit independently
  and then summing/comparing counts across bone categories without dividing by the
  element's per-animal frequency — he insisted all MNI figures be standardized
  ("fractional MNIs") by dividing the observed bone count by the number of that element
  present in one complete animal, to avoid distorting the assemblage's true anatomical
  composition. — L15-48 "all MNIs will be calculated by dividing the observed bone
  count for a given identification unit by the number of units of that unit in a
  complete animal... Such conversions may result in fractional values."
- [ATTR] Binford argued that calculating MNI by treating rights and lefts (or age/sex
  classes) as separately diagnostic individuals systematically inflates MNI, because
  hunters do not butcher, transport, or discard body parts in a way that respects
  side-symmetry — Binford reported hunters characteristically butcher one side then
  turn the animal for the other, a handedness-linked bias that has nothing to do with
  numbers of animals present. — L49-70 "I have found that hunters make no such
  discrimination... any estimates of meat available based on data from the numbers of
  rights or lefts will always be inflated."
- [ATTR] Binford constructed a hypothetical (and, he implies, empirically-grounded)
  worked example of three houses sharing meat from animals butchered elsewhere and
  distributed in units smaller than standard identification units (e.g. individual rib
  slabs), showing that conventional MNI/age-sex-weighted procedures would produce a
  badly distorted reconstruction (falsely inferring 3 individuals from ribs that were
  actually from 1 animal) and obscure the actual social fact of meat-sharing between
  houses. — L15-70 "If the archaeologists were naive... they might tabulate the
  assemblages from the three houses independently. The result... would be a tabulation
  of three individuals based on ribs when in fact only one individual was present."
- [ATTR] Binford's central methodological claim: the goal of his procedures is NOT to
  reconstruct "how many animals stand behind" an assemblage (the conventional aim) but
  to accurately describe the relative proportions of anatomical parts having similar
  utility values within the assemblage as actually deposited — a shift from a "kill
  population" estimation goal to a goal of describing the assemblage itself as a
  product of decisions. — L1-70 "Our interest is in the actual use made of animals as
  food, not in making poor estimates for what could have been a kill population while
  ignoring the reality of the assemblage before us."

### page: taphonomy / site-formation-processes
- [ATTR] Binford treated the composition of dispersed kill-butchering-location bone
  assemblages as directly produced by a chain of human decision-making (what to
  butcher, transport, cache, abandon) rather than as a passive residue — the central
  "schlepp effect" logic: low-utility parts are systematically left at the kill site
  while high-utility parts are removed, so the archaeological bone assemblage at a kill
  site is an inverse, decision-filtered image of what was consumed elsewhere. — L1-70,
  L490-502 (see utility-index entries above)
- [WIKI] Binford recorded that kill sites and consumption/residential locations among
  the Nunamiut were spatially and temporally distinct — "the locations where animals
  are killed are never the primary locations where they are consumed" — so
  decision-making at kill sites is governed by transport logistics rather than
  potential-use considerations per se. — L175-200 "Thus, Nunamiut decision making at
  kill sites is generally made in terms of transport considerations rather than in
  terms of different potential uses for anatomical parts."
- [WIKI] Binford documented systematic seasonal variability in how much decomposition/
  destructive taphonomic history affected bone assemblages before recording — e.g.
  antlers surviving to be recorded at a fresh fall site vs. deteriorating over years of
  weathering at a site observed later, and skull cartilage bias inflating skull-based
  utility calculations by an estimated ~50% due to poor recovery of cartilage-embedded
  meat weight. — L897-935 "the dispersed kills from spring were observed a longer time
  after the hunting and butchering episodes... Frequently only traces of the antlers
  remained... The utility indices for the skull may well be inflated on the order of
  50%."
- [ATTR] Binford treated cached meat/heads as playing a dual taphonomic role: caches
  function partly as facility markers (head bones support strings/cloth used to
  frighten ravens away from the cache) rather than purely as stored food, which biases
  the rate at which head elements are removed/consumed vs. left as facility residue,
  and thus biases their frequency in the kill-location assemblage independent of pure
  dietary utility. — L907-937 "heads in caches are not simply alternative pieces of
  stored food; they are useful architectural components of a temporary facility... The
  head is thus invariably the last item removed from a cache."

### page: nunamiut
- [WIKI] Binford's Nunamiut fieldwork ran 1969–1973; during this period he collected
  inventory data at 111 separate kill-butchering locations, 72 of which were
  single-animal kill/butchering sites and 39 of which were locations of multiple-animal
  kill or butchering activity, documenting a minimum of 277 individual caribou. — L323
  -335 "Over the entire span of my fieldwork with the Nunamiut Eskimo (1969-1973) I
  collected inventory data on kill-butchering locations... a minimum of 277 individual
  caribou were recorded at 111 separate kill-butchering locations."
- [WIKI] The two largest documented spring migration hunting sites were Anaktiqtauk
  (minimum 58 animals inventoried, 1972) and Anavik (53 animals, 1971). — L340-345
  (Figures 2.9, 5.2 referenced)
- [WIKI] Binford dated the 1971 spring caribou migration through the passes to have
  begun in substantial numbers on May 19, 1971, with intensive hunting on the 19th and
  20th; river-ice breakup began May 22 and made the Anavik crossing impassable by May
  23, forcing abandonment of unrecovered meat. In 1972, migration hunting at
  Anaktiqtauk ran May 17–23, with breakup beginning May 24. — L301-340, L865-925 "in
  1971 caribou began moving through the passes in substantial numbers on May 19... in
  1972... caribou began moving through the passes in substantial numbers on May 17."
- [WIKI] Fall-1969 kill-butchering data recorded a total of 125 mature-animal
  individuals (fall), 25 winter, and spring-dispersed-kill data 12 (or a more probable
  estimate of 19); summer dispersed data totaled only 8 individuals — Binford flagged
  the summer sample as anomalously small and behaviorally distinct (expeditionary
  encounter-hunting, not aggregated kills). — L918-923, Table 2.12/2.13 area "the
  summer sample is the smallest, with a total of only 8 individuals represented,
  whereas the fall total is 125."
- [WIKI] Binford recorded a male-biased sex ratio of roughly 3:1 in Nunamiut caribou
  kill records across fall and spring migration-hunting locations (kill-site
  archaeological ratios matched actual recorded kill ratios closely), attributed to
  hunters deliberately searching "bull range" during winter/fall when bulls are
  considered nutritionally poorest but most available in areas commonly hunted; cows
  were considered nutritionally better in winter. — L994-1017 "there is a bias in favor
  of males of roughly three to one in all records... the sex ratios observed at the
  sites are essentially indistinguishable from the actual kill records, a three to one
  bias in favor of bulls."
- [WIKI] Nunamiut hunters interviewed by Binford distinguished caribou "killed for
  meat" (mature animals) from those "killed for skins" (calves, taken selectively for
  clothing in late summer/early fall) or obtained incidentally as fetuses; calves taken
  for skins were typically only partially butchered (often just the head taken, as a
  delicacy), and pack dogs were commonly fed on calf carcasses at the kill site.
  — L1028-1067 "Calves are considered only as sources of skins for clothing in late
  summer and early fall. At that time, they are killed selectively for clothing but are
  not normally butchered for food."
- [WIKI] Binford recorded strong seasonal differences in transport/caching strategy:
  fall kills are normally cached near the kill location with meat transported to the
  residential location as needed over the winter/early spring, whereas spring kills
  must be transported immediately to the village (for ice-cellar freezing or drying)
  because of the imminent river-ice breakup that would cut off access. — L360-377 "Fall
  kills are normally cached near the kill location, and meat is transported to the
  residential location as it is needed over the entire winter and early spring. Spring
  kills, on the other hand, must be transported immediately to the village."
- [WIKI] Binford recorded that summer hunting is logistically distinct: it is
  expedition/encounter hunting conducted by 2+ men working out of temporary hunting
  camps away from the residential village, animals are killed as sighted rather than
  aggregated, and — uniquely among the seasonal datasets — the summer data shows a dual
  transport concern (maintaining the hunting expedition's pack dogs in the field AND
  returning meat to the residential location), producing an assemblage that does not
  fit the MGUI-based curvilinear model as well as other seasons. — L978-1018 "Summer
  hunting is encounter hunting. Animals killed are rarely aggregated and they are few...
  in all the data considered except that for the summer, removal of parts from
  kill-butchering locations is primarily a concern for returning parts to a single
  residential location."
- [WIKI] Binford noted that spring caribou are generally in poor nutritional condition
  (fat depleted) whereas fall caribou are prime, and that Nunamiut hunters therefore
  treat necks and front quarters of spring caribou as of little use (frequently
  abandoned) while the same parts are fat and useful in fall — a seasonally-conditioned
  utility difference layered on top of the anatomical MGUI. — L460-489 "necks and front
  quarters of spring caribou are of little use, but in fall these parts are fat and
  useful."

### page: ethnoarchaeology / actualistic-studies
- [ATTR] Binford framed his own multi-year, cross-seasonal kill-site inventory as a
  deliberate corrective to reliance on a single "idealized" ethnographic description of
  butchering (contrasting his approach with Yellen's 1977 !Kung San study, which
  Binford characterizes as satisfied with describing "a single 'typical' Bushman
  butchering episode" claimed to conform to "the standard pattern"); Binford instead
  emphasizes that his own Nunamiut data show high variability in butchering procedure
  driven by situational contingencies (season, transport distance, available
  labor/dogs), and that comparably high variability characterizes Great Plains bison
  hunter-butchering as documented archaeologically. — L1073-1100 "Yellen (1977, pp.
  280-285) is perfectly satisfied with a description of a single 'typical' Bushman
  butchering episode that 'conforms to the standard pattern'... I must admit that
  variability is the name of the game in my Eskimo data."
- [ATTR] Binford compared Nunamiut butchering variability against previously observed
  Navajo butchering (Binford and Bertram 1977) and Alyawara (Australian) butchering,
  reporting that variability was comparatively low among Navajo and Alyawara but high
  among the Nunamiut, and concluded there is no single universal "method of
  butchering" shared cross-culturally even among broadly similar subsistence economies
  — each group follows its own procedure, and even within a group the specific variant
  used depends on situational factors. — L1073-1100 "no common butchering procedure is
  shared by !Kung Bushmen, the Alyawara Australians, and the Navajo. In turn, the
  variants characteristic of each were not all observed among the Nunamiut."

### page: binford-nunamiut-ethnoarchaeology-study
- [WIKI] The book documents Binford's development, in Chapter 2, of a quantitative
  method (MNI standardization procedure + General/Modified General Utility Index) for
  linking observed bone-part frequencies at archaeological/ethnographic kill sites to
  the underlying human transport decisions, tested against his own 1969–1973 Nunamiut
  inventory dataset (277+ caribou, 111 kill-butchering locations). — (see faunal-
  analysis, utility-index, nunamiut entries above)

### Miscellaneous / unresolved
- Heavy OCR corruption throughout this slice: numerous data tables (Tables 2.7–2.13)
  are rendered as unreadable character garbage interleaved with column headers; I
  extracted the surrounding prose describing what each table demonstrates rather than
  attempting to reconstruct table contents, per the brief's instruction to skip pure
  data tables.
- "Whyte" / "Chaplin" (D. Chaplin 1971, cited repeatedly as a rival MNI methodology —
  "Chaplin (1971): 70-75") is a citation Binford argues against re: side-based MNI
  counting and White's (1953) dietary-percentage method — these are third-party
  methodological citations within Binford's text, not new page targets per the brief's
  canonical list; flagging in case the main thread wants a methodological-debate note
  on the faunal-analysis or utility-index page (Binford vs. Chaplin/White on MNI
  counting procedure) — possible candidate for a debate page but only one side (Binford's)
  is visible in this slice, so NOT filed as [POSITION] pending confirmation from other
  ranges.
- **GAP FLAG for main thread**: book lines ~4900–7600 of this range were not read
  (reading was capped partway through the assigned slice due to density/length). This
  portion likely continues Ch. 2 (Sex and Age Data section, Summary) into Ch. 3 per the
  brief's description. Recommend main-thread or fresh-extractor recovery of the
  remainder before integration, especially since the brief flagged this range as the
  core "schlepp effect" logic section — worth confirming nothing further downstream
  materially expands on the MGUI/transport-decision material already captured here.
