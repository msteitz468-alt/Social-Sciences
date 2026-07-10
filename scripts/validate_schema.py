#!/usr/bin/env python3
"""validate_schema.py — frontmatter + required-section validator for the
Social Sciences Wiki. Schemas encode CLAUDE.md's "Page Types and Formats".

Usage:
    python scripts/validate_schema.py [--root PATH] [--sections-warn] [--quiet]

Checks per page (by top-level folder under wiki/):
  - every schema field PRESENT (missing key = ERROR)
  - critical fields NON-EMPTY (empty = ERROR; others empty = WARN;
    `[[unknown]]` / `unknown` counts as filled — the schemas require
    explicitness, not omniscience)
  - enum fields hold allowed values (ERROR)
  - conditional rules (e.g. studies: fieldwork_dates mandatory for
    ethnography/excavation; disciplines: parent_discipline for subfields;
    hub pages: analysis_type matches folder, reciprocal *_page field set)
  - required body sections present as ## headings (ERROR, or WARN with
    --sections-warn)
  - date fields look like YYYY-MM-DD (WARN)
  - first-class type tag present in tags (WARN)
  - frontmatter parse warnings surfaced (WARN)

Exit status: 1 if any ERROR, else 0.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import (  # noqa: E402
    Page, load_vault, resolve_root, clean_scalar, parse_only, rel_matches_only)

DATE_PRECISION = ["exact", "year", "decade", "quarter-century", "century",
                  "approximate", "disputed", "unknown"]

# folder -> schema
SCHEMAS: dict[str, dict] = {
    "disciplines": dict(
        fields=["title", "discipline_type", "founded", "founding_figures",
                "core_questions", "major_methods", "subfields",
                "collection_coverage", "sources_ingested", "last_updated", "tags"],
        critical=["title", "discipline_type", "collection_coverage"],
        enums={"discipline_type": ["discipline", "subfield"],
               "collection_coverage": ["strong", "moderate", "weak", "absent", "unaudited"]},
        sections=[["scope"], ["historical development"], ["theoretical landscape"],
                  ["methods"], ["relations"], ["current state"], ["reflexivity"],
                  ["coverage"]],
        tag="discipline",
    ),
    "theories": dict(
        fields=["title", "theory_type", "disciplines", "era_origin", "date_origin",
                "originated_by", "key_texts", "core_claims", "developed_from",
                "competes_with", "status", "sources_ingested", "last_updated", "tags"],
        critical=["title", "theory_type", "core_claims", "status"],
        enums={"theory_type": ["grand-theory", "middle-range", "school",
                               "research-program", "paradigm", "method-theory"],
               "status": ["active", "contested", "declining", "absorbed", "abandoned"]},
        sections=[["core claims"], ["intellectual origins"], ["proponents"],
                  ["empirical program"], ["method commitments"], ["critiques"],
                  ["current status"], ["reflexivity"]],
        tag="theory",
    ),
    "thinkers": dict(
        fields=["title", "date_birth", "date_death", "disciplines", "era",
                "affiliated_theories", "trained_under", "trained", "key_works",
                "key_concepts", "fieldwork_sites", "sources_ingested",
                "last_updated", "tags"],
        critical=["title", "date_birth", "date_death", "disciplines"],
        enums={},
        sections=[["overview"], ["contributions"], ["genealogy"],
                  ["critiques", "reappraisals"], ["historiography"]],
        tag="thinker",
    ),
    "methods": dict(
        fields=["title", "method_type", "disciplines", "introduced_by",
                "date_introduced", "supersedes", "epistemic_leverage",
                "key_limitations", "sources_ingested", "last_updated", "tags"],
        critical=["title", "method_type", "key_limitations"],
        enums={"method_type": ["data-collection", "analytic", "dating", "sampling",
                               "statistical", "interpretive", "experimental"]},
        sections=[["what it does"], ["procedure"], ["assumptions", "limitations"],
                  ["history"], ["applications"], ["debates"]],
        tag="method",
    ),
    "studies": dict(
        fields=["title", "author", "year_published", "study_type", "disciplines",
                "fieldwork_location", "fieldwork_dates", "population_studied",
                "methods_used", "key_findings", "concepts_introduced",
                "replication_status", "sources_ingested", "last_updated", "tags"],
        critical=["title", "author", "study_type", "replication_status"],
        enums={"study_type": ["ethnography", "survey", "comparative", "excavation",
                              "experiment", "longitudinal", "archival", "mixed"],
               "replication_status": ["replicated", "partially-supported",
                                      "failed-replication", "reanalyzed-contested",
                                      "not-applicable", "unknown"]},
        sections=[["question"], ["design", "methods"], ["findings"], ["impact"],
                  ["critiques", "reanalyses", "replications"], ["standing"]],
        tag="study",
    ),
    "concepts": dict(
        fields=["title", "concept_type", "coined_by", "date_coined", "disciplines",
                "emic_or_etic", "operationalized_as", "contested",
                "related_concepts", "sources_ingested", "last_updated", "tags"],
        critical=["title", "concept_type", "emic_or_etic", "contested"],
        enums={"concept_type": ["analytical", "classificatory", "emic-term",
                                "measurement-construct", "periodization", "other"],
               "emic_or_etic": ["emic", "etic", "migrated"],
               "contested": ["yes", "no"]},
        sections=[["definition"], ["semantic history"], ["operationalization"],
                  ["applications"], ["critiques", "limitations"]],
        tag="concept",
    ),
    "debates": dict(
        fields=["title", "dispute_type", "disciplines", "era", "positions",
                "key_texts", "resolution_status", "last_updated", "tags"],
        critical=["title", "dispute_type", "positions", "resolution_status"],
        enums={"dispute_type": ["theoretical", "methodological", "empirical",
                                "interpretive", "ethical", "priority",
                                "source-reliability", "replication"],
               "resolution_status": ["open", "partially-resolved",
                                     "resolved-by-consensus", "dissolved"]},
        sections=[],
        tag="debate",
    ),
    "societies": dict(
        fields=["title", "society_type", "region", "language_affiliation",
                "subsistence_economy", "kinship_system", "documented_by",
                "documentation_dates", "endonym_exonym_note", "sources_ingested",
                "last_updated", "tags"],
        critical=["title", "society_type", "documented_by", "documentation_dates"],
        enums={"society_type": ["ethnolinguistic-group", "community",
                                "nation-population", "diaspora", "subculture",
                                "organization-population", "other"],
               "subsistence_economy": ["foraging", "pastoral", "horticultural",
                                       "agrarian", "industrial", "mixed", "other"]},
        sections=[["overview"], ["social organization"], ["economy", "subsistence"],
                  ["belief", "ritual"], ["documentation history"],
                  ["identity cautions"]],
        tag="society",
    ),
    "cultures": dict(
        fields=["title", "culture_type", "date_start", "date_end", "date_precision",
                "dating_methods", "period", "region", "defined_by",
                "construct_status", "type_site", "key_sites", "preceded_by",
                "succeeded_by", "language_affiliation", "genetic_signature",
                "sources_ingested", "last_updated", "tags"],
        critical=["title", "culture_type", "construct_status", "date_precision"],
        enums={"culture_type": ["archaeological-culture", "language-family",
                                "genetic-population"],
               "construct_status": ["robust", "conventional", "contested", "obsolete"],
               "date_precision": DATE_PRECISION,
               "defined_by": ["material-culture", "linguistic", "genetic", "mixed"]},
        sections=[["construct history"], ["signature"], ["distribution"],
                  ["lifeways"], ["relations"], ["identity cautions"],
                  ["historiography"]],
        tag="culture",
    ),
    "sites": dict(
        fields=["title", "site_type", "modern_country", "coordinates",
                "date_earliest", "date_latest", "date_precision", "dating_methods",
                "periods_of_occupation", "region", "cultures", "excavated_by",
                "excavation_years", "key_finds", "sources_ingested",
                "last_updated", "tags"],
        critical=["title", "site_type", "date_precision", "dating_methods"],
        enums={"site_type": ["settlement", "tell", "cemetery-necropolis",
                             "cave-rockshelter", "monument-ceremonial",
                             "quarry-mine", "kill-butchery", "hoard-deposit",
                             "shipwreck", "rock-art", "survey-region", "other"],
               "date_precision": DATE_PRECISION},
        sections=[["excavation history"], ["occupation sequence"],
                  ["significance"], ["debates"]],
        tag="site",
    ),
    "institutions": dict(
        fields=["title", "institution_type", "distribution", "key_variants",
                "theorized_by", "key_studies", "sources_ingested",
                "last_updated", "tags"],
        critical=["title", "institution_type", "distribution"],
        enums={"institution_type": ["kinship", "political", "economic", "religious",
                                    "legal", "educational", "stratification", "other"],
               "distribution": ["universal", "widespread", "regionally-specific",
                                "historically-specific"]},
        sections=[["definition"], ["variation"], ["theoretical treatments"],
                  ["studies"], ["debates"]],
        tag="institution",
    ),
    "phenomena": dict(
        fields=["title", "phenomenon_type", "scale", "date_start", "date_end",
                "period", "region", "measured_by", "driven_by", "produces",
                "theorized_by", "key_studies", "sources_ingested",
                "last_updated", "tags"],
        critical=["title", "phenomenon_type", "scale"],
        enums={"phenomenon_type": ["demographic", "economic", "political",
                                   "religious", "cultural", "technological",
                                   "stratification", "other"],
               "scale": ["micro", "meso", "macro", "global"]},
        sections=[["definition"], ["measurement"], ["patterns", "findings"],
                  ["explanatory theories"], ["interaction"], ["debates"]],
        tag="phenomenon",
    ),
    "comparisons": dict(
        fields=["title", "compares", "dimension", "method", "galton_note",
                "sources_ingested", "last_updated", "tags"],
        critical=["title", "compares", "method", "galton_note"],
        enums={"method": ["controlled-comparison", "statistical-crosscultural",
                          "paired-case", "typological"]},
        sections=[],
        tag="comparison",
    ),
    "sources": dict(
        fields=["title", "author", "year", "source_type", "disciplines",
                "era_coverage", "region_coverage", "methodological_approach",
                "reliability_notes", "pages_created", "pages_updated",
                "ingested", "tags"],
        critical=["title", "author", "year", "source_type"],
        enums={"source_type": ["primary-study", "theoretical-work", "reference",
                               "textbook-handbook", "excavation-report",
                               "ethnography", "scientific-study", "series",
                               "history-of-discipline", "polemic", "mixed"],
               "methodological_approach": ["ethnographic", "quantitative",
                                           "comparative", "archaeological",
                                           "theoretical", "historical", "genetic",
                                           "linguistic", "demographic", "mixed",
                                           "other"]},
        sections=[],
        tag="source",
    ),
    # High-detail hubs -------------------------------------------------------
    "hubs/theory": dict(
        fields=["analysis_type", "theory_page", "disciplines", "era_origin",
                "originated_by", "key_texts", "status", "key_sources"],
        critical=["analysis_type", "theory_page"],
        enums={"analysis_type": ["theory"],
               "status": ["active", "contested", "declining", "absorbed", "abandoned"]},
        sections=[["intellectual origins"], ["core claims"], ["key texts"],
                  ["empirical program"], ["method commitments"], ["debates"],
                  ["critiques"], ["what survived"], ["current status"]],
        tag=None,
    ),
    "hubs/thinkers": dict(
        fields=["analysis_type", "thinker_page", "date_birth", "date_death",
                "disciplines", "key_works", "key_concepts", "fieldwork_sites",
                "primary_sources", "key_sources"],
        critical=["analysis_type", "thinker_page"],
        enums={"analysis_type": ["thinker"]},
        sections=[["formation"], ["genealogy"], ["career phases"], ["major works"],
                  ["conceptual contributions"], ["empirical base"],
                  ["reception"], ["legacy"], ["historiography"]],
        tag=None,
    ),
    "hubs/studies": dict(
        fields=["analysis_type", "study_page", "author", "year_published",
                "study_type", "fieldwork_location", "fieldwork_dates",
                "methods_used", "replication_status", "key_sources"],
        critical=["analysis_type", "study_page", "replication_status"],
        enums={"analysis_type": ["study"],
               "study_type": ["ethnography", "survey", "comparative", "excavation",
                              "experiment", "longitudinal", "archival", "mixed"],
               "replication_status": ["replicated", "partially-supported",
                                      "failed-replication", "reanalyzed-contested",
                                      "not-applicable", "unknown"]},
        sections=[["question"], ["design"], ["site", "sample", "data"],
                  ["findings"], ["moves"], ["reception"],
                  ["critiques", "restudies", "replications"],
                  ["current standing"], ["historiography"]],
        tag=None,
    ),
}

DATE_FIELDS = {"last_updated", "ingested"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
UNKNOWN_OK = {"unknown", "[[unknown]]", "none", "n/a"}


def is_empty(v) -> bool:
    if v is None:
        return True
    if isinstance(v, list):
        return len([x for x in v if clean_scalar(str(x))]) == 0
    return clean_scalar(str(v)) == ""


def enum_values(v) -> list[str]:
    items = v if isinstance(v, list) else [v]
    out = []
    for item in items:
        s = clean_scalar(str(item)).strip()
        s = s.strip("[]").split("|")[0].strip()  # tolerate [[value]] / [[v|Display]]
        if s:
            out.append(s.lower())
    return out


def validate_page(page: Page, schema: dict, sections_severity: str):
    findings = []  # (severity, message)
    fm = page.fm

    for w in page.fm_warnings:
        findings.append(("WARN", f"frontmatter: {w}"))

    for f in schema["fields"]:
        if f not in fm:
            findings.append(("ERROR", f"missing frontmatter field '{f}'"))
        elif is_empty(fm[f]):
            sev = "ERROR" if f in schema["critical"] else "WARN"
            findings.append((sev, f"field '{f}' is empty — fill it or use [[unknown]] explicitly"))

    for f, allowed in schema["enums"].items():
        if f in fm and not is_empty(fm[f]):
            for val in enum_values(fm[f]):
                if val not in allowed and val not in UNKNOWN_OK:
                    findings.append(("ERROR",
                        f"field '{f}' has value '{val}' not in allowed set {allowed}"))

    for f in DATE_FIELDS & set(fm):
        if not is_empty(fm[f]):
            v = clean_scalar(str(fm[f] if not isinstance(fm[f], list) else fm[f][0]))
            if not DATE_RE.match(v):
                findings.append(("WARN", f"field '{f}' should be YYYY-MM-DD (got '{v}')"))

    tag = schema.get("tag")
    if tag and "tags" in fm and not is_empty(fm["tags"]):
        tags = [t.lower() for t in enum_values(fm["tags"])]
        if tag not in tags:
            findings.append(("WARN", f"tags should include the type tag '{tag}'"))

    # ---- conditional rules -------------------------------------------------
    folder = page.hub_folder
    if folder == "disciplines":
        if enum_values(fm.get("discipline_type", "")) == ["subfield"] and is_empty(fm.get("parent_discipline")):
            findings.append(("ERROR", "subfields must set 'parent_discipline'"))
    if folder in ("studies", "hubs/studies"):
        st = enum_values(fm.get("study_type", ""))
        if any(x in ("ethnography", "excavation") for x in st) and is_empty(fm.get("fieldwork_dates")):
            findings.append(("ERROR",
                "'fieldwork_dates' is mandatory for ethnography/excavation "
                "(kills the ethnographic-present trap)"))

    # ---- required body sections -------------------------------------------
    if schema["sections"]:
        heads = page.headings()
        for alts in schema["sections"]:
            if not any(alt in h for h in heads for alt in alts):
                findings.append((sections_severity,
                    f"missing required body section (## heading containing "
                    f"{' or '.join(repr(a) for a in alts)})"))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None, help="vault root (contains wiki/)")
    ap.add_argument("--sections-warn", action="store_true",
                    help="downgrade missing-body-section findings from ERROR to WARN")
    ap.add_argument("--quiet", action="store_true", help="summary only")
    ap.add_argument("--only", default=None,
                    help="report only pages whose path contains one of these "
                         "substrings (comma/space separated) — scopes a fast "
                         "changed-files check; the final pass omits it")
    args = ap.parse_args()

    root = resolve_root(args.root)
    pages = load_vault(root)
    only = parse_only(args.only)
    sections_severity = "WARN" if args.sections_warn else "ERROR"

    n_err = n_warn = n_checked = 0
    for page in pages:
        if page.is_template or page.is_portal or page.is_root_file:
            continue
        if not rel_matches_only(page.rel, only):
            continue
        schema = SCHEMAS.get(page.hub_folder)
        if schema is None:
            continue  # queries/, timelines/, hub roots — no schema
        n_checked += 1
        for sev, msg in validate_page(page, schema, sections_severity):
            if sev == "ERROR":
                n_err += 1
            else:
                n_warn += 1
            if not args.quiet:
                print(f"{sev:5s} {page.rel} :: {msg}")

    print(f"\nvalidate_schema: {n_checked} pages checked — "
          f"{n_err} error(s), {n_warn} warning(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
