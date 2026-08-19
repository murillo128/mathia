from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from experiments.agnostic_mathia_corpus import RELEASE_ID
from experiments.agnostic_mathia_corpus.catalog_ecosystems import (
    ECOSYSTEM_BY_ID,
    ECOSYSTEMS,
)
from experiments.agnostic_mathia_corpus.catalog_sources import SOURCE_BY_ID, SOURCES
from experiments.agnostic_mathia_corpus.catalog_synthesis import (
    DERIVATIVE_VARIANTS,
    SYNTHESIS_SPECS,
)
from experiments.agnostic_mathia_corpus.catalog_depth import SATURATION_PROBES
from experiments.agnostic_mathia_corpus.catalog_units import UNIT_SPECS
from experiments.mathia_corpus.interchange import (
    INTERCHANGE_VERSION,
    build_record,
    canonical_json,
    load_jsonl,
    materialize_mixed_manifest,
    render_record,
    sha256_text,
    validate_release,
    write_jsonl,
)


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[1]
RELEASE_ROOT = ROOT / "release_v1"
COMMON_FIXTURE_ROOT = ROOT.parent / "mathia_corpus" / "fixtures" / "riemann_representative_v1"
DEFAULT_ARTIFACT_ROOT = Path("/workspace/mathia-artifacts/agnostic-corpus-v1")
ACQUISITION_SNAPSHOT = RELEASE_ROOT / "acquisition_snapshot.json"
QUALITY_REVIEWS_PATH = RELEASE_ROOT / "quality_reviews.jsonl"
REVIEW_CONTENT_FREEZE_PATH = RELEASE_ROOT / "review_content_freeze.json"
USER_AGENT = "Mathia issue-44 corpus acquisition/1.0 (research metadata preservation)"


CALIBRATION_REQUIREMENTS = [
    {
        "requirement": "geometric reformulation is the central simplifying move",
        "object_ids": ["cso_separation"],
        "result": "pass",
        "evidence": "separation replaces disjoint convex feasibility by one affine certificate and records failure without convexity",
    },
    {
        "requirement": "tempting geometric analogy is wrong or incomplete",
        "object_ids": ["cbp_parallel_postulate"],
        "result": "pass",
        "evidence": "the disk drawing preserves points while changing geodesics, metric, and intrinsic straightness",
    },
    {
        "requirement": "algebraic or universal-property case",
        "object_ids": ["qf_kernel_factor", "up_product"],
        "result": "pass",
        "evidence": "factorization and mapping behavior remain mathematically distinct rather than becoming a generic abstraction slogan",
    },
    {
        "requirement": "analytic, spectral, or transform case",
        "object_ids": ["ts_fourier_modes", "dc_spectral_split"],
        "result": "pass",
        "evidence": "operator-adapted modes and the symmetry hypothesis are explicit",
    },
    {
        "requirement": "probabilistic case",
        "object_ids": ["pic_conditioning", "pic_pairwise_mutual"],
        "result": "pass",
        "evidence": "conditioning is an information-state change and higher-order dependence supplies a concrete boundary",
    },
    {
        "requirement": "combinatorial or discrete case",
        "object_ids": ["cgeb_hall", "rgf_recurrence_encoding"],
        "result": "pass",
        "evidence": "matching obstructions and formal-series encoding preserve different discrete mechanisms",
    },
    {
        "requirement": "local-to-global or compactness/completeness case",
        "object_ids": ["lg_sheaf_gluing", "cc_compact_fip", "cc_contraction_completion"],
        "result": "pass",
        "evidence": "overlap compatibility, finite intersection consistency, and metric completion are distinguished",
    },
    {
        "requirement": "two different proofs of the same result expose different mechanisms",
        "object_ids": ["grc_euler_induction", "grc_euler_dual_tree"],
        "result": "pass",
        "evidence": "invariance under deletion is contrasted with a primal-dual spanning-tree decomposition",
    },
]


QA_CRITERIA = [
    "mathematical_faithfulness",
    "non_paraphrase_conceptual_value",
    "domain_specificity",
    "epistemic_status_distinction",
    "representation_sensitivity",
    "analogy_limits",
    "unit_boundary_sufficiency",
    "geometry_preservation",
    "domain_and_source_type_bias",
    "teacher_template_shortcut",
    "cross_source_synthesis_support",
    "concrete_mathematics_retention",
]


QA_SAMPLE_UNIT_IDS = [
    "qf_correspondence_lattice",
    "sa_burnside_double_count",
    "dc_spectral_induction",
    "du_kkt_exact_certificate",
    "ic_spectrum_under_similarity",
    "lg_partition_of_unity",
    "cc_compactness_equivalence_proof",
    "sp_uniform_limit_proof",
    "ts_heat_mode_evolution",
    "dit_preimage_theorem_proof",
    "cg_gauss_bonnet_consequences",
    "cso_closest_point_separator",
    "pc_generalized_circle_invariance",
    "mp_automorphisms_obstruct_fine_space",
    "ho_circle_encode_decode",
    "pic_chebyshev_second_moment",
    "cgeb_hall_augmenting_proof",
    "rgf_recurrence_operator",
    "up_product_uniqueness",
    "fit_compactness_direct_proof",
    "eac_completion_embedding",
    "aor_residual_cut_certificate",
    "cbp_moving_spike",
    "grc_normal_equations_projection",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def acquisition_snapshot() -> dict[str, Any]:
    if ACQUISITION_SNAPSHOT.is_file():
        return read_json(ACQUISITION_SNAPSHOT)
    return {
        "snapshot_version": "agnostic-source-acquisition-v1",
        "artifact_root_policy": "external_to_git",
        "retrieved_at": None,
        "artifacts": [],
    }


def acquire_sources(artifact_root: Path) -> dict[str, Any]:
    artifact_root.mkdir(parents=True, exist_ok=True)
    rows = []
    for source in SOURCES:
        url = source.get("acquisition_url")
        filename = source.get("artifact_filename")
        if not source.get("selected_for_release") or not url or not filename:
            continue
        target = artifact_root / filename
        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,application/gzip,*/*"},
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            with target.open("wb") as handle:
                shutil.copyfileobj(response, handle)
            effective_url = response.geturl()
            content_type = response.headers.get_content_type()
        rows.append(
            {
                "source_id": source["source_id"],
                "requested_url": url,
                "effective_url": effective_url,
                "artifact_filename": filename,
                "artifact_sha256": sha256_file(target),
                "artifact_bytes": target.stat().st_size,
                "content_type": content_type,
                "storage_boundary": "external_to_git",
                "redistribution_boundary": source["redistribution"],
            }
        )
    snapshot = {
        "snapshot_version": "agnostic-source-acquisition-v1",
        "artifact_root_policy": "external_to_git",
        "retrieved_at": utc_now(),
        "artifacts": rows,
    }
    write_json(ACQUISITION_SNAPSHOT, snapshot)
    return snapshot


def source_licensing(source: Mapping[str, Any]) -> dict[str, str]:
    return {
        "license_id": source["license_id"],
        "attribution": f'{source["title"]} — {", ".join(source["authors"])}',
        "redistribution": source["redistribution"],
        "license_evidence_url": source["license_evidence_url"],
    }


def source_lineage(
    source: Mapping[str, Any], exact_span: str, acquired_by_id: Mapping[str, Mapping[str, Any]]
) -> dict[str, Any]:
    acquisition = acquired_by_id.get(source["source_id"])
    return {
        "source_id": source["source_id"],
        "source_url": source["canonical_url"],
        "exact_span": exact_span,
        "source_version": source["version"],
        "artifact_sha256": acquisition.get("artifact_sha256") if acquisition else None,
        "artifact_availability": (
            "external_hash_bound"
            if acquisition
            else "external_or_metadata_only_not_locally_frozen"
        ),
        "transformation": "independently written mathematical restatement; no silent formula repair",
    }


def object_id(role: str, local_id: str) -> str:
    return f"mathia:agnostic:v1:{role}:{local_id}"


def build_records(snapshot: Mapping[str, Any]) -> list[dict[str, Any]]:
    acquired_by_id = {row["source_id"]: row for row in snapshot.get("artifacts", [])}
    records: list[dict[str, Any]] = []
    unit_by_id = {spec["unit_id"]: spec for spec in UNIT_SPECS}
    source_object_by_unit: dict[str, str] = {}

    teacher = {
        "kind": "Codex-authored source-grounded editorial derivative",
        "model_family": "GPT-5-family Codex",
        "exact_service_checkpoint": "not exposed in client context",
        "capture_date": "2026-08-19",
        "generation_protocol": "specific mathematical restatement followed by directed conceptual reading; negative and boundary variants retained separately",
    }
    extractor = {
        "kind": "Codex-authored source-grounded mathematical restatement",
        "model_family": "GPT-5-family Codex",
        "exact_service_checkpoint": "not exposed in client context",
        "capture_date": "2026-08-19",
        "extraction_protocol": "independent non-verbatim restatement from the exact cited source span; source artifacts and locators remain the authority",
        "verbatim_source_text": False,
    }

    for spec in UNIT_SPECS:
        source = SOURCE_BY_ID[spec["source_id"]]
        lineage = [source_lineage(source, spec["exact_span"], acquired_by_id)]
        source_id = object_id("source", spec["unit_id"])
        source_object_by_unit[spec["unit_id"]] = source_id
        dependency = []
        if spec.get("sidecar_id"):
            dependency = [
                {
                    "sidecar_id": spec["sidecar_id"],
                    "necessity": "helpful",
                }
            ]
        local_metadata = {
            "title": spec["title"],
            "ecosystem_id": spec["ecosystem_id"],
            "representation_modes": spec["representation_modes"],
            "concepts": spec["concepts"],
            "conceptual_moves": spec["conceptual_moves"],
            "epistemic_role": spec["epistemic_role"],
            "geometry_involvement": spec["geometry_involvement"],
            "acquisition_phase": spec["acquisition_phase"],
            "depth_contribution": spec["depth_contribution"],
            "depth_tier": spec["depth_tier"],
            "source_word_count": len(spec["source_math"].split()),
            "content_kind": spec["content_kind"],
        }
        records.append(
            build_record(
                corpus_release=RELEASE_ID,
                corpus_origin="agnostic",
                object_id=source_id,
                object_role="source",
                content=spec["source_math"],
                source_ids=[source["source_id"]],
                lineage=lineage,
                extractor_provenance=extractor,
                licensing=source_licensing(source),
                representation_dependencies=dependency,
                local_metadata=local_metadata,
            )
        )
        records.append(
            build_record(
                corpus_release=RELEASE_ID,
                corpus_origin="agnostic",
                object_id=object_id("interpretation", spec["unit_id"]),
                object_role="interpretation",
                content=spec["interpretation"],
                source_ids=[source["source_id"]],
                lineage=lineage,
                parent_ids=[source_id],
                teacher_provenance=teacher,
                licensing=source_licensing(source),
                representation_dependencies=dependency,
                local_metadata={
                    **local_metadata,
                    "uncertainty_scope": "conceptual interpretation; theorem content remains attributed to the source locator",
                },
            )
        )

    for variant in DERIVATIVE_VARIANTS:
        spec = unit_by_id[variant["parent_unit_id"]]
        source = SOURCE_BY_ID[spec["source_id"]]
        accepted = variant["acceptance_state"] == "accepted"
        records.append(
            build_record(
                corpus_release=RELEASE_ID,
                corpus_origin="agnostic",
                object_id=object_id("interpretation", variant["variant_id"]),
                object_role="interpretation",
                content=variant["content"],
                source_ids=[source["source_id"]],
                lineage=[source_lineage(source, spec["exact_span"], acquired_by_id)],
                parent_ids=[source_object_by_unit[spec["unit_id"]]],
                teacher_provenance=teacher,
                acceptance_state=variant["acceptance_state"],
                training_eligible=accepted,
                exclusion_reason=variant["exclusion_reason"],
                licensing=source_licensing(source),
                local_metadata={
                    "title": f'QA variant: {variant["variant_id"]}',
                    "ecosystem_id": spec["ecosystem_id"],
                    "qa_issue": variant["qa_issue"],
                    "preserved_negative_evidence": True,
                },
            )
        )

    for spec in SYNTHESIS_SPECS:
        parents = [source_object_by_unit[item] for item in spec["parent_unit_ids"]]
        parent_specs = [unit_by_id[item] for item in spec["parent_unit_ids"]]
        source_ids = sorted({item["source_id"] for item in parent_specs})
        lineage = [
            source_lineage(
                SOURCE_BY_ID[item["source_id"]], item["exact_span"], acquired_by_id
            )
            for item in parent_specs
        ]
        accepted = spec["acceptance_state"] == "accepted"
        records.append(
            build_record(
                corpus_release=RELEASE_ID,
                corpus_origin="agnostic",
                object_id=object_id("synthesis", spec["synthesis_id"]),
                object_role="synthesis",
                content=spec["content"],
                source_ids=source_ids,
                lineage=lineage,
                parent_ids=parents,
                teacher_provenance=teacher,
                acceptance_state=spec["acceptance_state"],
                training_eligible=accepted,
                exclusion_reason=spec["exclusion_reason"],
                licensing={
                    "license_id": "source-linked-original-analysis-no-license-grant",
                    "attribution": "; ".join(SOURCE_BY_ID[item]["title"] for item in source_ids),
                    "redistribution": "preserve every source locator and review the listed source-specific boundaries before external redistribution",
                    "license_evidence_url": "multiple; see lineage",
                },
                local_metadata={
                    "title": spec["title"],
                    "concepts": spec["concepts"],
                    "conceptual_moves": spec["conceptual_moves"],
                    "analogy_limits": spec["analogy_limits"],
                    "cross_source": len(source_ids) > 1,
                    "preserved_negative_evidence": not accepted,
                },
            )
        )
    return records


def build_sidecars() -> list[dict[str, Any]]:
    specifications = [
        (
            "sidecar_fundamental_polygon",
            "qf_surface_identification",
            "assets/fundamental_polygon.svg",
            ["hitchman_geometry_2020"],
            "paired arrows make the boundary identification relation visually recoverable",
        ),
        (
            "sidecar_subspace_intersection",
            "dit_subspace_bound",
            "assets/subspace_intersection.svg",
            ["interactive_linear_algebra_2026"],
            "two planes sharing a line visualize dimension-forced intersection",
        ),
        (
            "sidecar_curvature_triangles",
            "cg_angle_curvature",
            "assets/curvature_triangles.svg",
            ["hitchman_geometry_2020"],
            "the schematic preserves the sign change of triangle-angle defect across curvature models",
        ),
        (
            "sidecar_convex_separation",
            "cso_separation",
            "assets/convex_separation.svg",
            ["boyd_vandenberghe_convex_2009"],
            "the affine separator exposes a single dual witness for disjoint convex sets",
        ),
    ]
    rows = []
    for sidecar_id, source_unit_id, relative_path, source_ids, description in specifications:
        path = ROOT / relative_path
        rows.append(
            {
                "sidecar_id": sidecar_id,
                "source_unit_id": object_id("source", source_unit_id),
                "path": relative_path,
                "sha256": sha256_file(path),
                "available": True,
                "unavailable_reason": None,
                "necessity": "helpful",
                "representation_type": "svg_editorial_reconstruction",
                "description": description,
                "source_ids": source_ids,
                "source_relationship": "repository-authored schematic derived from the cited mathematical configuration; not copied source artwork",
                "license_id": "repository-authored-no-external-license-grant",
                "redistribution": "contains no copied third-party artwork; external redistribution remains subject to the repository's licensing decision",
            }
        )
    return rows


def build_source_inventory(snapshot: Mapping[str, Any]) -> list[dict[str, Any]]:
    acquired = {row["source_id"]: row for row in snapshot.get("artifacts", [])}
    inventory = []
    for source in SOURCES:
        row = dict(source)
        row["acquisition"] = acquired.get(source["source_id"])
        if row["acquisition"]:
            row["acquisition_status"] = "acquired_external_hash_bound"
        elif source["selected_for_release"]:
            row["acquisition_status"] = "external_or_metadata_only_not_locally_frozen"
        else:
            row["acquisition_status"] = "seed_alternative_not_acquired"
        row["used_unit_ids"] = sorted(
            spec["unit_id"] for spec in UNIT_SPECS if spec["source_id"] == source["source_id"]
        )
        inventory.append(row)
    return inventory


def coverage_map() -> dict[str, Any]:
    return {
        "map_id": "agnostic-conceptual-coverage-map-v1",
        "status": "working_search_instrument_not_ontology",
        "revision_history": [
            {
                "version": "v0",
                "ecosystem_count": 22,
                "change": "initial cross-cutting map before extraction calibration",
            },
            {
                "version": "v1",
                "ecosystem_count": 24,
                "change": "added counterexamples/boundary phenomena and geometricization as explicit ecosystems after calibration exposed their cross-cutting role",
            },
        ],
        "audit_axes": [
            "domain",
            "representation_mode",
            "concept",
            "conceptual_move",
            "epistemic_role",
            "depth",
            "cross_domain_analogue",
            "geometry_involvement",
        ],
        "ecosystems": ECOSYSTEMS,
    }


def acquisition_history() -> dict[str, Any]:
    return {
        "history_id": "agnostic-adaptive-acquisition-v1",
        "uniform_expansion_used": False,
        "phases": [
            {
                "phase": "coverage_map_and_seed_selection",
                "input": "24-ecosystem working map with three deliberately contrasting seeds per ecosystem",
                "result": "selected open textbooks, lecture notes, collaborative references, classical works, and negative-material alternatives",
            },
            {
                "phase": "heterogeneous_calibration",
                "input_unit_ids": sorted({item for row in CALIBRATION_REQUIREMENTS for item in row["object_ids"]}),
                "gate": "passed_before_gap_fill",
                "observed_gaps": [
                    "geometry needed distinct curvature, transversality, quotient-surface, projective, and moduli mechanisms",
                    "transform analogy needed a probability case with explicit independence and convergence limits",
                    "negative material needed to be a first-class ecosystem rather than annotations on positive theorems",
                    "universal properties needed both mapping-in and free-extension directions",
                ],
            },
            {
                "phase": "targeted_geometry_gap_fill",
                "sources": [
                    "hitchman_geometry_2020",
                    "walpuski_differential_geometry_2021",
                    "stacks_project_ed88ff78",
                    "poincare_analysis_situs_1895",
                ],
                "added": "curvature, transversality, quotient surfaces, projectivization, moduli, homotopy obstruction, and model-sensitive analogy failures",
            },
            {
                "phase": "targeted_cross_domain_gap_fill",
                "sources": [
                    "hott_book_578b85c",
                    "grinstead_snell_probability_2006",
                    "open_logic_2026_snapshot",
                    "applied_combinatorics_2017_3",
                ],
                "added": "equivalence with retained identity data, higher-order dependence boundaries, logical compactness, min-max and certificate mechanisms",
            },
            {
                "phase": "baseline_corpus_scale_quality_audit",
                "result": "failed the 48-unit candidate for shallow unit boundaries and a dominant four-sentence interpretation template",
            },
            {
                "phase": "targeted_depth_and_form_expansion",
                "input": "one proof or worked development per ecosystem plus source-specific rewrites of eighteen compact interpretations",
                "result": "raised the release to three units per ecosystem, created a 24-unit proof/worked stratum, and reduced the four-sentence interpretation share from 42/48 to 26/72",
            },
            {
                "phase": "synthesis_and_saturation_audit",
                "result": "tested one named post-expansion candidate per ecosystem; stopped where it repeated a represented mechanism and recorded distinct future extensions without claiming bibliographic completeness",
            },
        ],
    }


def coverage_audit(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_ecosystem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for spec in UNIT_SPECS:
        by_ecosystem[spec["ecosystem_id"]].append(spec)
    rows = []
    for ecosystem in ECOSYSTEMS:
        specs = by_ecosystem[ecosystem["ecosystem_id"]]
        rows.append(
            {
                "ecosystem_id": ecosystem["ecosystem_id"],
                "source_unit_count": len(specs),
                "distinct_source_count": len({item["source_id"] for item in specs}),
                "representation_modes": sorted({mode for item in specs for mode in item["representation_modes"]}),
                "epistemic_roles": sorted({item["epistemic_role"] for item in specs}),
                "geometry_involvement": sorted({item["geometry_involvement"] for item in specs}),
                "depth_contributions": [item["depth_contribution"] for item in specs],
                "proof_or_worked_unit_count": sum(
                    item["depth_tier"] == "proof_or_worked_development"
                    for item in specs
                ),
                "maturity": (
                    "bounded_v1_stop_supported_by_duplicate_probe"
                    if SATURATION_PROBES[ecosystem["ecosystem_id"]]["disposition"]
                    == "repeat_represented_mechanism"
                    else "represented_at_depth_with_named_future_extension"
                ),
            }
        )
    return {
        "coverage_audit_id": "agnostic-coverage-audit-v1",
        "ecosystem_count": len(ECOSYSTEMS),
        "all_ecosystems_have_three_source_units": all(
            row["source_unit_count"] >= 3 for row in rows
        ),
        "all_ecosystems_have_proof_or_worked_unit": all(
            row["proof_or_worked_unit_count"] >= 1 for row in rows
        ),
        "ecosystems": rows,
    }


def saturation_log() -> dict[str, Any]:
    units_by_ecosystem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for spec in UNIT_SPECS:
        units_by_ecosystem[spec["ecosystem_id"]].append(spec)
    rows = []
    for ecosystem in ECOSYSTEMS:
        specs = units_by_ecosystem[ecosystem["ecosystem_id"]]
        probe = SATURATION_PROBES[ecosystem["ecosystem_id"]]
        mature = probe["disposition"] == "repeat_represented_mechanism"
        rows.append(
            {
                "ecosystem_id": ecosystem["ecosystem_id"],
                "latest_material_addition": specs[-1]["depth_contribution"],
                "post_expansion_candidate": probe["candidate"],
                "candidate_disposition": probe["disposition"],
                "disposition_evidence": probe["reason"],
                "important_gap_remaining": (
                    "no additional mechanism needed for the bounded v1 release; broader theorem coverage remains possible"
                    if mature
                    else probe["reason"]
                ),
                "recent_expansion_mostly_duplication": mature,
                "further_search_disposition": (
                    "stop_for_v1_revisit_only_if_training_design_needs_more_depth"
                    if mature
                    else "named_future_extension_after_v1_depth_floor"
                ),
            }
        )
    return {
        "saturation_log_id": "agnostic-saturation-log-v1",
        "stop_rule": "conceptual_saturation_not_source_count",
        "bounded_v1_stop_ecosystem_count": sum(
            row["recent_expansion_mostly_duplication"] for row in rows
        ),
        "represented_with_named_future_extension_count": sum(
            not row["recent_expansion_mostly_duplication"] for row in rows
        ),
        "ecosystems": rows,
    }


def calibration_audit() -> dict[str, Any]:
    calibration_ids = sorted({item for row in CALIBRATION_REQUIREMENTS for item in row["object_ids"]})
    ecosystems = sorted(
        {next(spec["ecosystem_id"] for spec in UNIT_SPECS if spec["unit_id"] == item) for item in calibration_ids}
    )
    return {
        "calibration_id": "agnostic-cross-domain-calibration-v1",
        "status": "passed_before_adaptive_expansion",
        "distinct_ecosystem_count": len(ecosystems),
        "ecosystem_ids": ecosystems,
        "unit_ids": calibration_ids,
        "requirements": CALIBRATION_REQUIREMENTS,
        "domain_anchor_audit": {
            "status": "pass",
            "finding": "outputs retain kernels, overlap equalities, transform modes, joint factorizations, tangent spans, convex segments, and embedding-dependent faces rather than one recurring generic discourse pattern",
        },
    }


def qa_sample() -> dict[str, Any]:
    negative_ids = [variant["variant_id"] for variant in DERIVATIVE_VARIANTS] + [
        spec["synthesis_id"]
        for spec in SYNTHESIS_SPECS
        if spec["acceptance_state"] != "accepted"
    ]
    return {
        "qa_sample_id": "agnostic-corpus-qa-sample-v1",
        "selection_rule": "fixed before final independent review; spans domains, representations, source types, geometry, and every negative quality stratum",
        "accepted_unit_ids": QA_SAMPLE_UNIT_IDS,
        "negative_or_evaluation_ids": negative_ids,
        "criteria": QA_CRITERIA,
    }


def load_quality_reviews() -> list[dict[str, Any]]:
    if not QUALITY_REVIEWS_PATH.is_file():
        return []
    return load_jsonl(QUALITY_REVIEWS_PATH)


def report(
    records: list[dict[str, Any]],
    inventory: list[dict[str, Any]],
    sidecars: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
    review_content_freeze_id: str,
) -> dict[str, Any]:
    role_counts = Counter(record["object_role"] for record in records)
    state_counts = Counter(record["acceptance_state"] for record in records)
    representation_counts = Counter(
        mode for spec in UNIT_SPECS for mode in spec["representation_modes"]
    )
    geometry_counts = Counter(spec["geometry_involvement"] for spec in UNIT_SPECS)
    source_ids = {spec["source_id"] for spec in UNIT_SPECS}
    source_type_counts = Counter(
        SOURCE_BY_ID[source_id]["source_type"] for source_id in source_ids
    )
    source_unit_type_counts = Counter(
        SOURCE_BY_ID[spec["source_id"]]["source_type"] for spec in UNIT_SPECS
    )
    primary_domain_counts = Counter(
        ECOSYSTEM_BY_ID[spec["ecosystem_id"]]["domains"][0] for spec in UNIT_SPECS
    )
    source_word_counts = [len(spec["source_math"].split()) for spec in UNIT_SPECS]
    interpretation_word_counts = [
        len(spec["interpretation"].split()) for spec in UNIT_SPECS
    ]
    interpretation_sentence_counts = [
        len(re.findall(r'[.!?](?:["”’)]*)\s+', spec["interpretation"].strip())) + 1
        for spec in UNIT_SPECS
    ]
    by_id = {record["object_id"]: record for record in records}
    rendered_word_count = sum(
        len(render_record(record, by_id).split())
        for record in records
        if record["training_eligible"]
    )
    review_verdict_counts = Counter(review.get("verdict", "unknown") for review in reviews)
    material_review_failures = [
        review for review in reviews if review.get("material") and review.get("verdict") == "fail"
    ]
    reviewed_criteria = {review.get("criterion") for review in reviews}
    review_is_complete = (
        len(reviews) == len(QA_CRITERIA)
        and reviewed_criteria == set(QA_CRITERIA)
        and all(review.get("verdict") == "pass" for review in reviews)
        and all(review.get("fresh_subagent") is True for review in reviews)
        and all(
            review.get("reviewer_agent") == "/root/expanded_corpus_qa"
            for review in reviews
        )
        and all(
            review.get("review_content_freeze_id") == review_content_freeze_id
            for review in reviews
        )
        and not material_review_failures
    )
    final_decision = (
        "AGNOSTIC_MATHIA_CORPUS_READY"
        if review_is_complete
        else "AGNOSTIC_MATHIA_CORPUS_REVISE"
    )
    return {
        "report_id": "agnostic-mathia-corpus-final-report-v1",
        "release_id": RELEASE_ID,
        "final_decision": final_decision,
        "decision_scope": "ready only after complete fresh QA as an auditable corpus input for a separate training-design issue; no training ratio or run is authorized",
        "counts": {
            "seed_source_inventory": len(inventory),
            "sources_used": len(source_ids),
            "semantic_source_units": len(UNIT_SPECS),
            "objects_by_role": dict(sorted(role_counts.items())),
            "objects_by_acceptance_state": dict(sorted(state_counts.items())),
            "trainable_objects": sum(record["training_eligible"] for record in records),
            "accepted_cross_domain_syntheses": sum(
                record["object_role"] == "synthesis" and record["training_eligible"]
                for record in records
            ),
            "representation_sidecars": len(sidecars),
            "sources_by_type": dict(sorted(source_type_counts.items())),
            "semantic_units_by_source_type": dict(
                sorted(source_unit_type_counts.items())
            ),
            "semantic_units_by_primary_domain": dict(
                sorted(primary_domain_counts.items())
            ),
            "representation_modes": dict(sorted(representation_counts.items())),
            "geometry_involvement": dict(sorted(geometry_counts.items())),
            "rendered_trainable_words": rendered_word_count,
        },
        "coverage_map_change": "v0 began with 22 ecosystems; calibration promoted counterexamples/boundaries and geometricization/representation change to explicit ecosystems in v1",
        "geometry_audit": {
            "status": "pass",
            "primary_source_unit_count": geometry_counts["primary"],
            "represented_modes": [
                "synthetic_and_non_euclidean",
                "projective_and_compactified",
                "differential_and_curvature",
                "convex_and_separation",
                "topological_and_deformation",
                "discrete_planar_and_dual",
                "moduli_and_parameter_space",
                "group_action_and_transformation",
            ],
            "representative_geometricizations": [
                "disjoint feasibility to a separating hyperplane",
                "dimension excess to forced subspace intersection",
                "nonlinear intersection to tangent transversality",
                "inconsistent linear equations to orthogonal projection",
                "planar counting to primal-dual spanning trees",
            ],
            "limitations": "four repository-authored SVG schematics are helpful but dispensable; no eligible text object claims to preserve an omitted essential source diagram",
        },
        "depth": {
            "all_ecosystems_have_three_units": all(
                count >= 3
                for count in Counter(
                    spec["ecosystem_id"] for spec in UNIT_SPECS
                ).values()
            ),
            "all_ecosystems_have_proof_or_worked_development": all(
                any(
                    spec["ecosystem_id"] == ecosystem["ecosystem_id"]
                    and spec["depth_tier"] == "proof_or_worked_development"
                    for spec in UNIT_SPECS
                )
                for ecosystem in ECOSYSTEMS
            ),
            "proof_or_worked_development_count": sum(
                spec["depth_tier"] == "proof_or_worked_development"
                for spec in UNIT_SPECS
            ),
            "bounded_v1_stop_ecosystem_count": sum(
                probe["disposition"] == "repeat_represented_mechanism"
                for probe in SATURATION_PROBES.values()
            ),
            "open_depth_gaps_are_recorded": True,
            "source_unit_word_count": {
                "minimum": min(source_word_counts),
                "mean": round(sum(source_word_counts) / len(source_word_counts), 1),
                "maximum": max(source_word_counts),
                "proof_or_worked_minimum": min(
                    len(spec["source_math"].split())
                    for spec in UNIT_SPECS
                    if spec["depth_tier"] == "proof_or_worked_development"
                ),
            },
            "warning": "v1 is finite and intentionally not mathematically or bibliographically exhaustive",
        },
        "teacher_style_audit": {
            "interpretation_word_count": {
                "minimum": min(interpretation_word_counts),
                "mean": round(
                    sum(interpretation_word_counts) / len(interpretation_word_counts), 1
                ),
                "maximum": max(interpretation_word_counts),
            },
            "interpretation_sentence_count_histogram": dict(
                sorted(Counter(interpretation_sentence_counts).items())
            ),
            "exactly_four_sentence_fraction": round(
                interpretation_sentence_counts.count(4)
                / len(interpretation_sentence_counts),
                3,
            ),
            "observed_forms": [
                "proof_anatomy",
                "worked_construction",
                "counterexample_design",
                "question_and_diagnosis",
                "dependency_chain",
                "representation_comparison",
            ],
            "baseline_finding_addressed": "the baseline 48-unit release had 42 four-sentence interpretations; the expanded release rewrites 18 compact interpretations and adds 24 proof/worked interpretations with mathematics-shaped structures",
        },
        "adaptive_acquisition": "calibration preceded targeted geometry, cross-domain, negative-material, and synthesis gap fills; expansion was not uniform",
        "extraction": {
            "ocr_used": False,
            "verbatim_source_text_committed": False,
            "method": "exact source locators plus independently written mathematical restatements; accessible source artifacts are hash-bound outside Git",
            "failure_handling": "no formula corruption was silently repaired; suspect overclaims and flattened interpretations are retained as quarantined or rejected records",
        },
        "quality_audit": {
            "review_content_freeze_id": review_content_freeze_id,
            "fresh_review_count": len(reviews),
            "reviewed_criteria": sorted(item for item in reviewed_criteria if item),
            "complete_criterion_coverage": reviewed_criteria == set(QA_CRITERIA),
            "verdict_counts": dict(sorted(review_verdict_counts.items())),
            "unresolved_material_failure_count": len(material_review_failures),
            "criteria": QA_CRITERIA,
        },
        "licensing_and_storage": {
            "raw_artifacts": "external to Git under /workspace/mathia-artifacts by default",
            "open_sources": "retain source-specific GFDL or Creative Commons attribution/share-alike boundaries",
            "restricted_sources": "only metadata, exact locators, and independently written mathematical restatements are committed",
            "corpus_derivatives": "no repository-wide external license grant is inferred; review source-specific lineage before redistribution",
        },
        "known_gaps": [
            "fourteen ecosystems retain a named candidate for a future distinct-depth extension; this v1 claims a three-unit depth floor, not ecosystem-level exhaustion",
            "no source-native figure is bundled; the four sidecars are traceable editorial reconstructions",
            "advanced arithmetic geometry, stochastic processes, PDE, and numerical analysis remain thinner than algebra, topology, and geometry",
            "teacher provenance cannot name an exact service checkpoint because the client does not expose it",
        ],
        "before_training_recommendation": "design an explicit license-compatible sampling policy, inspect the open depth gaps, and test behavioral consequences separately; do not infer training utility from corpus prose quality",
        "prohibited_implications": [
            "no model training or GPU work was performed",
            "no final concept ontology was fixed",
            "no mathematical correctness claim is based on teacher similarity",
            "the synthetic mixed manifest chooses no future corpus ratio",
        ],
    }


def representative_fixture() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    common_license = {
        "license_id": "representative-fixture-no-source-redistribution",
        "attribution": "structural compatibility fixture derived from issue #42's documented corpus roles",
        "redistribution": "fixture prose only; it is not a substitute for the frozen issue #42 source release",
        "license_evidence_url": "https://github.com/murillo128/mathia/issues/44",
    }
    first_content = next(
        spec["source_math"] for spec in UNIT_SPECS if spec["unit_id"] == "ts_fourier_modes"
    )
    source_one = build_record(
        corpus_release="riemann-representative-fixture-v1",
        corpus_origin="riemann",
        object_id="mathia:riemann-fixture:v1:source:fourier_modes",
        object_role="source",
        content=first_content,
        source_ids=["fourier_theorie_chaleur_1822"],
        lineage=[
            {
                "source_id": "fourier_theorie_chaleur_1822",
                "source_url": SOURCE_BY_ID["fourier_theorie_chaleur_1822"]["canonical_url"],
                "exact_span": "representative shared Fourier source used only to exercise duplicate detection",
                "source_version": SOURCE_BY_ID["fourier_theorie_chaleur_1822"]["version"],
                "artifact_sha256": None,
                "artifact_availability": "representative_fixture",
                "transformation": "exact duplicate of a source-unit restatement in the companion fixture",
            }
        ],
        extractor_provenance={
            "kind": "hand-authored compatibility-fixture restatement",
            "authoring_context": "issue #44 representative fixture for issue #42",
            "verbatim_source_text": False,
        },
        licensing=common_license,
        local_metadata={"fixture_only": True},
    )
    second_source = build_record(
        corpus_release="riemann-representative-fixture-v1",
        corpus_origin="riemann",
        object_id="mathia:riemann-fixture:v1:source:functional_symmetry",
        object_role="source",
        content="Let ξ be a completed analytic function satisfying ξ(s) = ξ(e − s) and a compatible conjugation symmetry. Any zero away from a fixed point of these symmetries belongs to the orbit obtained by reflection and conjugation.",
        source_ids=["issue42_representative_source"],
        lineage=[
            {
                "source_id": "issue42_representative_source",
                "source_url": "https://github.com/murillo128/mathia/issues/42",
                "exact_span": "representative fixture for the symmetry role; not a frozen source excerpt",
                "source_version": "issue-42-work-in-progress-at-2026-08-19",
                "artifact_sha256": None,
                "artifact_availability": "representative_fixture",
                "transformation": "generic structural fixture",
            }
        ],
        extractor_provenance={
            "kind": "hand-authored compatibility-fixture restatement",
            "authoring_context": "issue #44 representative fixture for issue #42",
            "verbatim_source_text": False,
        },
        licensing=common_license,
        local_metadata={"fixture_only": True},
    )
    interpretation = build_record(
        corpus_release="riemann-representative-fixture-v1",
        corpus_origin="riemann",
        object_id="mathia:riemann-fixture:v1:interpretation:symmetry_orbits",
        object_role="interpretation",
        content="The functional identities act as transformations of the zero set, so the useful unit is an orbit rather than an isolated zero. A proposed zero configuration must close under both transformations. The symmetry constrains placement but does not by itself locate the zeros or prove that every orbit meets a preferred locus.",
        source_ids=["issue42_representative_source"],
        lineage=second_source["lineage"],
        parent_ids=[second_source["object_id"]],
        teacher_provenance={"kind": "hand-authored compatibility fixture", "exact_checkpoint": None},
        licensing=common_license,
        local_metadata={"fixture_only": True},
    )
    synthesis_record = build_record(
        corpus_release="riemann-representative-fixture-v1",
        corpus_origin="riemann",
        object_id="mathia:riemann-fixture:v1:synthesis:modes_and_symmetry",
        object_role="synthesis",
        content="Both source units recommend choosing a representation adapted to an action: frequency modes diagonalize an evolution, while symmetry orbits organize a zero set. The shared move is representation by invariant components. The analogy stops there—Fourier coefficients support reconstruction under analytic hypotheses, whereas orbit closure alone supplies constraints rather than a decomposition or proof.",
        source_ids=["fourier_theorie_chaleur_1822", "issue42_representative_source"],
        lineage=source_one["lineage"] + second_source["lineage"],
        parent_ids=[source_one["object_id"], second_source["object_id"]],
        teacher_provenance={"kind": "hand-authored compatibility fixture", "exact_checkpoint": None},
        licensing=common_license,
        local_metadata={"fixture_only": True, "analogy_limits": ["constraint orbit is not spectral reconstruction"]},
    )
    fixture_records = [source_one, second_source, interpretation, synthesis_record]
    fixture_manifest = {
        "interchange_version": INTERCHANGE_VERSION,
        "corpus_release": "riemann-representative-fixture-v1",
        "fixture_for_issue": 42,
        "not_a_corpus_release": True,
        "eligible_object_ids": sorted(record["object_id"] for record in fixture_records),
    }
    return fixture_records, [], fixture_manifest


SOURCE_TREE_PATHS = (
    ROOT / "catalog_sources.py",
    ROOT / "catalog_ecosystems.py",
    ROOT / "catalog_units.py",
    ROOT / "catalog_depth.py",
    ROOT / "catalog_synthesis.py",
    ROOT / "pipeline.py",
    ROOT.parent / "mathia_corpus" / "interchange.py",
)

REVIEW_CONTENT_RELEASE_FILES = (
    "acquisition_history.json",
    "acquisition_snapshot.json",
    "baseline_quality_audit.json",
    "calibration_audit.json",
    "coverage_audit.json",
    "coverage_map.json",
    "qa_sample.json",
    "records.jsonl",
    "rendered_trainable.jsonl",
    "saturation_log.json",
    "sidecars.jsonl",
    "source_inventory.jsonl",
    "synthetic_mixed_dry_run.json",
    "trainable_manifest.json",
)


def source_tree_freeze_rows() -> list[dict[str, Any]]:
    return [
        {
            "path": str(path.relative_to(REPO_ROOT)),
            "sha256": sha256_file(path),
        }
        for path in SOURCE_TREE_PATHS
    ]


def review_content_paths() -> list[Path]:
    return [RELEASE_ROOT / name for name in REVIEW_CONTENT_RELEASE_FILES] + [
        path for path in sorted(COMMON_FIXTURE_ROOT.iterdir()) if path.is_file()
    ]


def build_review_content_freeze() -> dict[str, Any]:
    paths = review_content_paths()
    missing = [str(path.relative_to(REPO_ROOT)) for path in paths if not path.is_file()]
    if missing:
        raise ValueError(f"cannot freeze missing review content: {missing}")
    value = {
        "freeze_version": "agnostic-mathia-review-content-v1",
        "release_id": RELEASE_ID,
        "purpose": "exact corpus candidate inspected by fresh QA; excludes quality reviews, final report, and final freeze to avoid self-reference",
        "files": [
            {
                "path": str(path.relative_to(REPO_ROOT)),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in paths
        ],
        "source_tree": source_tree_freeze_rows(),
    }
    value["review_content_freeze_id"] = "review_content_" + sha256_text(
        canonical_json(value)
    )
    write_json(REVIEW_CONTENT_FREEZE_PATH, value)
    return value


def build_release() -> dict[str, Any]:
    RELEASE_ROOT.mkdir(parents=True, exist_ok=True)
    snapshot = acquisition_snapshot()
    records = build_records(snapshot)
    sidecars = build_sidecars()
    inventory = build_source_inventory(snapshot)
    manifest = {
        "interchange_version": INTERCHANGE_VERSION,
        "corpus_release": RELEASE_ID,
        "eligible_object_ids": sorted(
            record["object_id"] for record in records if record["training_eligible"]
        ),
    }
    write_json(RELEASE_ROOT / "coverage_map.json", coverage_map())
    write_jsonl(RELEASE_ROOT / "source_inventory.jsonl", inventory)
    write_jsonl(RELEASE_ROOT / "records.jsonl", records)
    write_jsonl(RELEASE_ROOT / "sidecars.jsonl", sidecars)
    write_json(RELEASE_ROOT / "trainable_manifest.json", manifest)
    write_json(RELEASE_ROOT / "calibration_audit.json", calibration_audit())
    write_json(RELEASE_ROOT / "acquisition_history.json", acquisition_history())
    write_json(RELEASE_ROOT / "coverage_audit.json", coverage_audit(records))
    write_json(RELEASE_ROOT / "saturation_log.json", saturation_log())
    write_json(RELEASE_ROOT / "qa_sample.json", qa_sample())

    by_id = {record["object_id"]: record for record in records}
    rendered = [
        {
            "object_id": object_id_value,
            "rendered_text": render_record(by_id[object_id_value], by_id),
            "rendered_sha256": sha256_text(render_record(by_id[object_id_value], by_id)),
        }
        for object_id_value in manifest["eligible_object_ids"]
    ]
    write_jsonl(RELEASE_ROOT / "rendered_trainable.jsonl", rendered)

    fixture_records, fixture_sidecars, fixture_manifest = representative_fixture()
    COMMON_FIXTURE_ROOT.mkdir(parents=True, exist_ok=True)
    write_jsonl(COMMON_FIXTURE_ROOT / "records.jsonl", fixture_records)
    write_jsonl(COMMON_FIXTURE_ROOT / "sidecars.jsonl", fixture_sidecars)
    write_json(COMMON_FIXTURE_ROOT / "trainable_manifest.json", fixture_manifest)
    write_json(
        COMMON_FIXTURE_ROOT / "README.json",
        {
            "purpose": "representative issue #42 compatibility fixture allowed by issue #44 while corpus-scale issue #42 extraction remains underway",
            "not_a_replacement_for_issue_42_release": True,
        },
    )
    mixed = materialize_mixed_manifest([records, fixture_records], per_release=4)
    write_json(RELEASE_ROOT / "synthetic_mixed_dry_run.json", mixed)

    review_content_freeze = build_review_content_freeze()
    reviews = load_quality_reviews()
    report_value = report(
        records,
        inventory,
        sidecars,
        reviews,
        review_content_freeze["review_content_freeze_id"],
    )
    write_json(RELEASE_ROOT / "corpus_report.json", report_value)

    freeze_paths = [
        path
        for path in sorted(RELEASE_ROOT.iterdir())
        if path.is_file() and path.name != "freeze.json"
    ] + [
        path
        for path in sorted(COMMON_FIXTURE_ROOT.iterdir())
        if path.is_file()
    ]
    freeze_files = [
        {
            "path": str(path.relative_to(REPO_ROOT)),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
        for path in freeze_paths
    ]
    freeze = {
        "freeze_version": "agnostic-mathia-freeze-v1",
        "release_id": RELEASE_ID,
        "created_at": "2026-08-19",
        "implementation_base_revision": "e1738d3aa186b5a10a06fa8369fec79b0459037a",
        "source_tree": source_tree_freeze_rows(),
        "review_content_freeze_id": review_content_freeze[
            "review_content_freeze_id"
        ],
        "published_revision_policy": "the immutable Git commit and PR head are recorded by the GitHub publication handoff; source_tree hashes bind the pre-commit inputs without a self-referential commit hash",
        "files": freeze_files,
        "training_or_gpu_work_performed": False,
    }
    freeze["freeze_id"] = "freeze_" + sha256_text(canonical_json(freeze))
    write_json(RELEASE_ROOT / "freeze.json", freeze)
    return {
        "release_id": RELEASE_ID,
        "freeze_id": freeze["freeze_id"],
        "record_count": len(records),
        "eligible_count": len(manifest["eligible_object_ids"]),
        "source_unit_count": len(UNIT_SPECS),
        "final_decision": report_value["final_decision"],
    }


def validate_artifacts(artifact_root: Path) -> list[str]:
    errors = []
    snapshot = acquisition_snapshot()
    acquired_ids = {row["source_id"] for row in snapshot.get("artifacts", [])}
    used_ids = {spec["source_id"] for spec in UNIT_SPECS}
    for source_id in sorted(used_ids - acquired_ids):
        errors.append(f"used source lacks hash-bound artifact: {source_id}")
    for row in snapshot.get("artifacts", []):
        path = artifact_root / row["artifact_filename"]
        if not path.is_file():
            errors.append(f'missing source artifact: {row["source_id"]}: {path}')
            continue
        if path.stat().st_size != row["artifact_bytes"]:
            errors.append(f'artifact size mismatch: {row["source_id"]}')
        if sha256_file(path) != row["artifact_sha256"]:
            errors.append(f'artifact hash mismatch: {row["source_id"]}')
    return errors


def validate_committed_release(*, artifact_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    required = [
        "coverage_map.json",
        "source_inventory.jsonl",
        "records.jsonl",
        "sidecars.jsonl",
        "trainable_manifest.json",
        "calibration_audit.json",
        "acquisition_history.json",
        "coverage_audit.json",
        "saturation_log.json",
        "qa_sample.json",
        "quality_reviews.jsonl",
        "review_content_freeze.json",
        "corpus_report.json",
        "rendered_trainable.jsonl",
        "synthetic_mixed_dry_run.json",
        "freeze.json",
        "acquisition_snapshot.json",
    ]
    for name in required:
        if not (RELEASE_ROOT / name).is_file():
            errors.append(f"missing release file: {name}")
    if errors:
        return errors

    records = load_jsonl(RELEASE_ROOT / "records.jsonl")
    sidecars = load_jsonl(RELEASE_ROOT / "sidecars.jsonl")
    manifest = read_json(RELEASE_ROOT / "trainable_manifest.json")
    errors.extend(validate_release(records, sidecars, manifest, root=ROOT))
    fixture_records = load_jsonl(COMMON_FIXTURE_ROOT / "records.jsonl")
    fixture_sidecars = load_jsonl(COMMON_FIXTURE_ROOT / "sidecars.jsonl")
    fixture_manifest = read_json(COMMON_FIXTURE_ROOT / "trainable_manifest.json")
    errors.extend(validate_release(fixture_records, fixture_sidecars, fixture_manifest))

    coverage = read_json(RELEASE_ROOT / "coverage_map.json")
    if not 20 <= len(coverage.get("ecosystems", [])) <= 30:
        errors.append("coverage map must contain roughly 20–30 ecosystems")
    for ecosystem in coverage.get("ecosystems", []):
        seeds = ecosystem.get("seed_source_ids", [])
        if len(seeds) < 3:
            errors.append(f'ecosystem has fewer than three seeds: {ecosystem.get("ecosystem_id")}')
        unknown = set(seeds) - set(SOURCE_BY_ID)
        if unknown:
            errors.append(f'ecosystem has unknown seed sources: {ecosystem.get("ecosystem_id")}: {sorted(unknown)}')

    unit_counts = Counter(spec["ecosystem_id"] for spec in UNIT_SPECS)
    if set(unit_counts) != set(ECOSYSTEM_BY_ID):
        errors.append("source units do not cover every ecosystem")
    if any(count < 3 for count in unit_counts.values()):
        errors.append("every ecosystem must have at least three source units")
    if len(UNIT_SPECS) != 72:
        errors.append("v1 must freeze exactly 72 semantic source units")
    if len({spec["unit_id"] for spec in UNIT_SPECS}) != len(UNIT_SPECS):
        errors.append("duplicate semantic unit ids")
    for spec in UNIT_SPECS:
        if spec["source_id"] not in SOURCE_BY_ID:
            errors.append(f'unknown source id in unit: {spec["unit_id"]}')
        if spec["depth_tier"] == "proof_or_worked_development" and len(
            spec["source_math"].split()
        ) < 100:
            errors.append(f'deep unit is too short for its tier: {spec["unit_id"]}')
    for ecosystem_id in ECOSYSTEM_BY_ID:
        if not any(
            spec["ecosystem_id"] == ecosystem_id
            and spec["depth_tier"] == "proof_or_worked_development"
            for spec in UNIT_SPECS
        ):
            errors.append(f"ecosystem lacks proof/worked depth: {ecosystem_id}")

    calibration = read_json(RELEASE_ROOT / "calibration_audit.json")
    if calibration.get("status") != "passed_before_adaptive_expansion":
        errors.append("heterogeneous calibration did not pass before expansion")
    if calibration.get("distinct_ecosystem_count", 0) < 8:
        errors.append("calibration spans fewer than eight ecosystems")
    if any(row.get("result") != "pass" for row in calibration.get("requirements", [])):
        errors.append("calibration requirement failed")

    report_value = read_json(RELEASE_ROOT / "corpus_report.json")
    reviews = load_jsonl(RELEASE_ROOT / "quality_reviews.jsonl")
    review_content_freeze = read_json(REVIEW_CONTENT_FREEZE_PATH)
    review_content_without_id = {
        key: value
        for key, value in review_content_freeze.items()
        if key != "review_content_freeze_id"
    }
    expected_review_content_id = "review_content_" + sha256_text(
        canonical_json(review_content_without_id)
    )
    if (
        review_content_freeze.get("review_content_freeze_id")
        != expected_review_content_id
    ):
        errors.append("review content freeze id mismatch")
    expected_review_paths = {
        str(path.relative_to(REPO_ROOT)) for path in review_content_paths()
    }
    declared_review_paths = {
        row.get("path") for row in review_content_freeze.get("files", [])
    }
    if declared_review_paths != expected_review_paths:
        errors.append("review content freeze file set mismatch")
    for row in review_content_freeze.get("files", []):
        path = REPO_ROOT / row["path"]
        if not path.is_file():
            errors.append(f'missing review-frozen file: {row["path"]}')
        elif path.stat().st_size != row["bytes"] or sha256_file(path) != row["sha256"]:
            errors.append(f'review-frozen file drift: {row["path"]}')
    if review_content_freeze.get("source_tree") != source_tree_freeze_rows():
        errors.append("review content source tree drift")
    if len(reviews) != len(QA_CRITERIA):
        errors.append("quality review must contain exactly one row per fixed criterion")
    review_criteria = [review.get("criterion") for review in reviews]
    if set(review_criteria) != set(QA_CRITERIA) or len(review_criteria) != len(
        set(review_criteria)
    ):
        errors.append("quality review criteria are missing or duplicated")
    for review in reviews:
        criterion = review.get("criterion", "unknown")
        if review.get("verdict") != "pass":
            errors.append(f"quality criterion did not pass: {criterion}")
        if review.get("fresh_subagent") is not True:
            errors.append(f"quality criterion lacks fresh-subagent evidence: {criterion}")
        if review.get("reviewer_agent") != "/root/expanded_corpus_qa":
            errors.append(f"quality criterion has unexpected reviewer: {criterion}")
        if review.get("candidate") != "expanded_72_unit_release":
            errors.append(f"quality criterion has unexpected candidate: {criterion}")
        if review.get("review_content_freeze_id") != expected_review_content_id:
            errors.append(
                f"quality criterion is not bound to reviewed content: {criterion}"
            )
        if not review.get("summary") or not review.get("evidence"):
            errors.append(f"quality criterion lacks concrete evidence: {criterion}")
    if report_value.get("final_decision") != "AGNOSTIC_MATHIA_CORPUS_READY":
        errors.append("unexpected final decision")
    if report_value["quality_audit"]["fresh_review_count"] < 1:
        errors.append("fresh corpus-scale quality review is missing")
    if report_value["quality_audit"]["unresolved_material_failure_count"]:
        errors.append("fresh corpus-scale quality review has unresolved material failures")
    if not report_value["quality_audit"].get("complete_criterion_coverage"):
        errors.append("fresh corpus-scale quality review does not cover every fixed criterion")
    if (
        report_value["quality_audit"].get("review_content_freeze_id")
        != expected_review_content_id
    ):
        errors.append("report does not reference reviewed content freeze")

    snapshot_ids = {
        row["source_id"]
        for row in read_json(RELEASE_ROOT / "acquisition_snapshot.json").get(
            "artifacts", []
        )
    }
    used_source_ids = {spec["source_id"] for spec in UNIT_SPECS}
    if used_source_ids - snapshot_ids:
        errors.append(
            "used sources lack frozen artifacts: "
            + ", ".join(sorted(used_source_ids - snapshot_ids))
        )

    mixed = read_json(RELEASE_ROOT / "synthetic_mixed_dry_run.json")
    origins = {row["private_analysis"]["corpus_origin"] for row in mixed.get("records", [])}
    if origins != {"agnostic", "riemann"}:
        errors.append("synthetic mixed dry run does not contain both corpus origins")
    if not mixed.get("duplicate_groups"):
        errors.append("cross-corpus duplicate detector did not identify the shared fixture source")
    for row in mixed.get("records", []):
        folded = row["rendered_text"].casefold()
        if "agnostic" in folded or "riemann" in folded:
            errors.append(f'mixed rendering leaks corpus origin: {row["object_id"]}')

    rendered = load_jsonl(RELEASE_ROOT / "rendered_trainable.jsonl")
    if len(rendered) != len(manifest["eligible_object_ids"]):
        errors.append("rendered trainable count does not match manifest")
    if {row["object_id"] for row in rendered} != set(manifest["eligible_object_ids"]):
        errors.append("rendered trainable ids do not match manifest")

    freeze = read_json(RELEASE_ROOT / "freeze.json")
    freeze_without_id = {key: value for key, value in freeze.items() if key != "freeze_id"}
    expected_freeze_id = "freeze_" + sha256_text(canonical_json(freeze_without_id))
    if freeze.get("freeze_id") != expected_freeze_id:
        errors.append("freeze id mismatch")
    if freeze.get("review_content_freeze_id") != expected_review_content_id:
        errors.append("final freeze does not reference reviewed content freeze")
    for row in freeze.get("files", []):
        path = REPO_ROOT / row["path"]
        if not path.is_file():
            errors.append(f'missing frozen file: {row["path"]}')
        elif path.stat().st_size != row["bytes"] or sha256_file(path) != row["sha256"]:
            errors.append(f'frozen file drift: {row["path"]}')

    if artifact_root is not None:
        errors.extend(validate_artifacts(artifact_root))
    return errors


def summary() -> dict[str, Any]:
    report_value = read_json(RELEASE_ROOT / "corpus_report.json")
    freeze = read_json(RELEASE_ROOT / "freeze.json")
    return {
        "valid": True,
        "release_id": report_value["release_id"],
        "freeze_id": freeze["freeze_id"],
        "final_decision": report_value["final_decision"],
        "counts": report_value["counts"],
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build and validate the issue #44 corpus")
    parser.add_argument("--artifact-root", type=Path, default=DEFAULT_ARTIFACT_ROOT)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("acquire")
    subparsers.add_parser("build")
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--require-artifacts", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "acquire":
        value = acquire_sources(args.artifact_root)
        print(json.dumps(value, indent=2, sort_keys=True))
        return 0
    if args.command == "build":
        print(json.dumps(build_release(), indent=2, sort_keys=True))
        return 0
    errors = validate_committed_release(
        artifact_root=args.artifact_root if args.require_artifacts else None
    )
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2, sort_keys=True))
        return 1
    print(json.dumps(summary(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
