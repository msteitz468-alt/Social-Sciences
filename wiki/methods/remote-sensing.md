---
title: "Remote Sensing (Archaeology)"
method_type: data-collection
disciplines: [archaeology]
introduced_by: ["aerial photography tradition; spaceborne imaging and airborne laser scanning programs late 20th–early 21st c."]
date_introduced: "aerial photography early 20th c.; satellite archaeology late 20th c.; LIDAR/ALS major archaeological uptake early 21st c."
supersedes: ["[[unknown]]"]
epistemic_leverage: "Detects and records archaeological landscapes from airborne or satellite sensors (optical, multi-/hyperspectral, radar, LIDAR) and integrates with ground-based sensing; reveals plan, canopy-hidden earthworks, and regional infrastructure at scales ground survey alone cannot match."
key_limitations: "Season/vegetation/geology dependent; reveals plan more than date or cultural attribution; images do not themselves reveal sites—interpreters do; computerized analysis cannot fully automate prospection; requires ground survey and often excavation verification."
sources_ingested: 1
last_updated: 2026-07-10
tags: [method]
---

# Remote Sensing (Archaeology)

Detection and mapping of archaeological features and landscapes using sensors at a distance—from aircraft and satellites above, and non-invasive instruments on or under the ground. Textbook synthesis follows [[renfrew-bahn-archaeology-2012|Renfrew & Bahn 2012]]. Overlaps [[aerial-archaeology]] (optical air photography and interpretation) and [[geophysical-survey]] (ground-based remote sensing); this page emphasizes the integrated remote-sensing framework and spaceborne/airborne non-optical systems.

## What It Does

Renfrew & Bahn (2012) divide airborne/spaceborne remote sensing into **data collecting** (photos/images from aircraft or satellite) and **data analysis** (interpretation, integration with field survey, ground remote sensing, and documents). For the analyst, satellite, multi-/hyperspectral, and traditional air photos differ mainly in scale/resolution and are collectively “aerial images.” Images do not themselves reveal sites—taker and interpreter do, requiring experience to separate archaeology from tracks, river beds, and canals (WWII military intelligence used archaeologists as photo interpreters).

Satellite remote sensing **supplements, does not replace**, survey or excavation: it reveals (sub)surface features, places sites in larger social landscapes, aids quality assessment and excavation siting; rising resolution forces rethinking of survey/excavation strategies.

Ground-based remote sensing (GPR, resistivity, magnetometry, etc.) is treated under [[geophysical-survey]]; the same non-destructive-first logic applies.

## Procedure

### Optical aerial practice

- **Oblique vs vertical images.** Obliques usually targeted on recognized features (easier pictorial effect; harder for plan conversion). Verticals usually non-archaeological cartographic area survey (better for maps/plans; need thorough search). Both can form stereoscopic pairs for 3D confidence and photogrammetric base maps; rectification/georeferencing with DEM/LIDAR corrects perspective and tilt.
- **Crop-marks and soil alteration.** For detection a site generally must have altered soil/subsoil—negative features (ditches, pits) or positive (banks, mounds, walls)—surviving in relief or buried under leveled farmland. Crop-marks: crops grow taller/thicker over sunken features and stunted over buried walls due to soil depth/moisture differences—often invisible on the ground; more features discovered via crop-marks than by any other prospection form. Season and lighting matter; reverse-relief illusion if shadows fall away from viewer on verticals. Smallest features (postholes) rarely show. Natural (periglacial cracking) and recent (leveled boundaries, quarries) disturbances mimic archaeology.
- **Digital workflow.** Digital sensors/cameras (>10 MP adequate for many uses), GPS-planned flight tracks and Exif coordinates, archival storage (short digital-format life). Georeferenced mosaics in GIS are useful comparative layers but interpretation is still best with stereoscopic pairs; on-screen N-up viewing often violates ideal shadow-toward-viewer convention. Computerized image analysis is in infancy and will never fully automate prospection—field observation and human expertise remain indispensable.

### LIDAR / ALS

**LIDAR** (Light Detection and Ranging) / **ALS** (Airborne Laser Scanning): aircraft with differential GPS emits laser pulses; return time yields a digital elevation/surface model. Software can filter “first return” (tree canopy) to see woodland earthworks and move sun angle/azimuth for optimal lighting—advantages over conventional photography.

### Radar and satellite suites

- **SLAR** (sideways-looking airborne radar): penetrates cloud and partly rainforest; large-area landscape features (e.g. Maya lowlands lattice lines that may be canals).
- **SAR** (Synthetic Aperture Radar): multi-image processing for detailed topography day/night/weather-independent; can inventory sites without artifact collection as rapid alternative to surface survey.
- **Commercial high-res optical:** Ikonos (~1 m), QuickBird (60 cm), GeoEye (40 cm); Google Earth as LANDSAT base (28.5 m) plus high-res blocks.
- **CORONA** Cold War photography (best ~2 m): cheap historic base maps with stereo pairs for 3D DEM.
- **LANDSAT / ASTER:** large features and multi-band temperature, reflectance, elevation; ASTER stereo DEM capability beyond LANDSAT.

### Integration

Combine aerial images, geophysics, site plans, and artifact distributions in GIS if spatially located; always plan ground confirmation.

### Technique trade-offs (textbook table, Renfrew & Bahn 2012)

| Technique | Strengths | Limits |
|---|---|---|
| Oblique air photo | Clear site views/illustrations | Needs prior recognition of features |
| Vertical air photo | Landscape/historic change, stereo, vast archives | Often non-optimal timing; needs expertise |
| CORONA | Cheap historic ~2 m stereo | Not worldwide; distortion |
| QuickBird/Ikonos/GeoEye | Sub-meter where no air photos | Cost |
| LANDSAT | Worldwide multi-date | Coarse resolution |
| LIDAR | High-res upstanding features/terrain; canopy removal | Expensive; huge point clouds |
| SLAR/SAR | Terrain models, large features, canopy tools | Spaceborne often coarser |

## Assumptions and Limitations

- **Visibility rules apply across platforms.** Same conditions that hide crop-marks hide sites on satellites; absence on one date ≠ absence of archaeology; untrained users often expect sites always visible.
- **Detection requires soil/landscape alteration** for many feature types; post-depositional and natural mimics confuse interpreters—experienced local analysts needed.
- **Ground truth.** Caracol LIDAR and all ground-based remote sensing still need ground confirmation / excavation verification (Renfrew & Bahn 2012).
- **Not a substitute** for [[archaeological-survey]] or [[stratigraphic-excavation]].
- **Experimental timescale for earthwork “fossilization.”** Overton Down experimental earthwork suggests grass-stabilized banks/ditches can fossilize in relief within ~16 years—linking [[experimental-archaeology]] to what remote sensing can see.

## History

Aerial archaeology’s early history is treated on [[aerial-archaeology]] (military reconnaissance; O. G. S. Crawford). Renfrew & Bahn 2012 update the remote-sensing story with:

- Landscape mapping from air photo archives (Danebury environs; Chaco Canyon roads).
- Spaceborne optical and radar programs (LANDSAT, CORONA declassification, commercial sub-meter satellites, Google Earth “aerial revolution”).
- Airborne LIDAR applications (Stonehenge environs; Caracol as first large-site LIDAR application of its kind in the textbook account).
- SAR at Greater Angkor.

## Exemplary Applications

As reported in Renfrew & Bahn 2012:

- **Crop-mark discovery** — primary medium of aerial discovery of leveled arable sites (general finding).
- **Rog Palmer / Danebury** — 450 sq km Iron Age landscape: ≥8 other hillforts, 120 ditched enclosures, hundreds of acres of fields, 240 km linear ditches.
- **Chaco Canyon roads** — NPS 1970s aerial work; ~2400 km estimated prehistoric network, ~208 km ground-verified (11th–12th c. AD).
- **Caracol LIDAR (Chase & Chase; Weishampel design)** — ground mapping 23 sq km under dense forest in >25 years; air survey in weeks extended the city to 177 sq km; ~4 days/24 flight hours, >4 billion measurements, 3 weeks analysis; new ruins, terraces, causeways.
- **Stonehenge environs LIDAR** — new field-system enlargements and locational corrections.
- **SLAR Maya lowlands (Richard Adams et al.)** — 80,000 sq km; possible intensive canal agriculture if field-tested ancient.
- **CORONA hollow ways (Jason Ur)** — ~6025 km of Bronze Age tracks in northern Mesopotamia; moisture/vegetation-filled tracks radiating 2–5 km from sites—movement without direct major-center tracks, suggesting weak centralization.
- **Greater Angkor SAR** — ruins possibly covering up to 3000 sq km; moats/pools; ancient canals for rice irrigation and stone transport.
- **Google Earth / high-res blocks** — fossil-cave discovery context (Australopithecus sediba); hundreds of Afghan sites.
- **LANDSAT** — Mesopotamian levees, Arabian–Kuwait paleoriver, Ethiopian Rift sediments.
- **Giza probes / microgravimetry** — high-tech cavity detection beyond most projects’ resources (borderline remote sensing).

## Debates

- **Automation vs expertise.** Computerized image analysis will not fully replace human photo interpretation and field observation (textbook position).
- **Satellite archaeology hype.** Untrained expectation of universal visibility vs actual seasonal/geological constraints.
- **Environmental determinism in predictive models** that fuse remote sensing with GIS site-location models (see [[archaeological-survey]]).
- **How much ground survey can radar/LIDAR replace?** Rapid inventory without artifact collection is possible for large features, but cultural attribution, dating, and low-density scatters still need ground methods.
- **Data archive fragility** for digital formats vs long-lived film archives.

## Related

- [[aerial-archaeology]] · [[geophysical-survey]] · [[archaeological-survey]] · [[underwater-archaeology]]
- [[experimental-archaeology]] (Overton Down earthwork visibility)
- [[archaeological-feature]] · [[archaeological-site]]
- Source synthesis: [[renfrew-bahn-archaeology-2012]]
