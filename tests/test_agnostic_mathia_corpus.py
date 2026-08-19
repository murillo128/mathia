from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path

from experiments.agnostic_mathia_corpus import RELEASE_ID, pipeline
from experiments.agnostic_mathia_corpus.catalog_ecosystems import ECOSYSTEMS
from experiments.agnostic_mathia_corpus.catalog_sources import SOURCE_BY_ID
from experiments.agnostic_mathia_corpus.catalog_units import UNIT_SPECS
from experiments.mathia_corpus import interchange
from experiments.riemann_corpus import full_corpus as riemann_full


class AgnosticMathiaCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.records = pipeline.load_jsonl(pipeline.RELEASE_ROOT / "records.jsonl")
        cls.sidecars = pipeline.load_jsonl(pipeline.RELEASE_ROOT / "sidecars.jsonl")
        cls.manifest = pipeline.read_json(
            pipeline.RELEASE_ROOT / "trainable_manifest.json"
        )
        cls.by_id = {record["object_id"]: record for record in cls.records}

    def test_committed_release_validates_without_external_artifacts(self) -> None:
        self.assertEqual(pipeline.validate_committed_release(), [])

    def test_release_uses_the_canonical_shared_contract(self) -> None:
        self.assertEqual(self.manifest["contract_version"], "mathia-interchange-v1")
        self.assertEqual(self.manifest["corpus_release_id"], RELEASE_ID)
        self.assertEqual(
            {record["contract_version"] for record in self.records},
            {interchange.CONTRACT_VERSION},
        )
        self.assertEqual(
            interchange.validate_release(
                self.records, lambda record: str(record["content"])
            ),
            [],
        )

    def test_coverage_map_is_broad_editable_and_owner_revised(self) -> None:
        coverage = pipeline.read_json(pipeline.RELEASE_ROOT / "coverage_map.json")
        self.assertEqual(len(coverage["ecosystems"]), 28)
        self.assertEqual(coverage["status"], "working_search_instrument_not_ontology")
        self.assertEqual(
            [row["ecosystem_count"] for row in coverage["revision_history"]],
            [22, 24, 28],
        )
        for ecosystem in coverage["ecosystems"]:
            with self.subTest(ecosystem=ecosystem["ecosystem_id"]):
                self.assertGreaterEqual(len(ecosystem["seed_source_ids"]), 3)
                self.assertLessEqual(
                    set(ecosystem["seed_source_ids"]), set(SOURCE_BY_ID)
                )
                self.assertEqual(
                    ecosystem["map_status"], "working_search_instrument_not_ontology"
                )

    def test_every_ecosystem_has_at_least_three_units_and_proof_depth(self) -> None:
        counts = Counter(spec["ecosystem_id"] for spec in UNIT_SPECS)
        self.assertEqual(len(UNIT_SPECS), 98)
        self.assertEqual(set(counts), {item["ecosystem_id"] for item in ECOSYSTEMS})
        self.assertEqual(set(counts.values()), {3, 4})
        self.assertEqual(len({spec["unit_id"] for spec in UNIT_SPECS}), 98)
        self.assertEqual(
            sum(
                spec["depth_tier"] == "proof_or_worked_development"
                for spec in UNIT_SPECS
            ),
            50,
        )
        for ecosystem in ECOSYSTEMS:
            deep = [
                spec
                for spec in UNIT_SPECS
                if spec["ecosystem_id"] == ecosystem["ecosystem_id"]
                and spec["depth_tier"] == "proof_or_worked_development"
            ]
            self.assertGreaterEqual(len(deep), 1)
            self.assertTrue(
                all(len(spec["source_math"].split()) >= 100 for spec in deep)
            )

    def test_calibration_passes_all_required_heterogeneous_cases(self) -> None:
        audit = pipeline.read_json(pipeline.RELEASE_ROOT / "calibration_audit.json")
        self.assertEqual(audit["status"], "passed_before_adaptive_expansion")
        self.assertGreaterEqual(audit["distinct_ecosystem_count"], 8)
        self.assertEqual({row["result"] for row in audit["requirements"]}, {"pass"})
        evidence = " ".join(row["requirement"] for row in audit["requirements"])
        for marker in (
            "geometric reformulation",
            "geometric analogy",
            "universal-property",
            "probabilistic",
            "combinatorial",
            "two different proofs",
        ):
            self.assertIn(marker, evidence)

    def test_owner_named_gaps_are_closed_by_explicit_probe_evidence(self) -> None:
        saturation = pipeline.read_json(pipeline.RELEASE_ROOT / "saturation_log.json")
        self.assertEqual(len(saturation["ecosystems"]), 28)
        self.assertEqual(saturation["represented_with_named_future_extension_count"], 0)
        self.assertEqual(saturation["bounded_v1_stop_ecosystem_count"], 28)
        for row in saturation["ecosystems"]:
            with self.subTest(ecosystem=row["ecosystem_id"]):
                self.assertEqual(
                    row["candidate_disposition"], "repeat_represented_mechanism"
                )
                self.assertTrue(row["post_expansion_candidate"])
                self.assertGreaterEqual(len(row["disposition_evidence"].split()), 12)
                self.assertTrue(row["recent_expansion_mostly_duplication"])

    def test_acceptance_semantics_exclude_every_negative_and_probe(self) -> None:
        manifest_ids = set(self.manifest["eligible_object_ids"])
        states = Counter(record["quality_state"] for record in self.records)
        self.assertEqual(
            states,
            Counter(
                {
                    "accepted": 214,
                    "rejected": 4,
                    "quarantined": 2,
                    "evaluation_only": 2,
                }
            ),
        )
        for record in self.records:
            with self.subTest(object_id=record["object_id"]):
                self.assertEqual(
                    record["object_id"] in manifest_ids,
                    record["quality_state"] == "accepted",
                )
                self.assertEqual(
                    record["training_eligibility"] == "eligible",
                    record["quality_state"] == "accepted",
                )
                if record["quality_state"] != "accepted":
                    self.assertTrue(record["exclusion_reason"])

    def test_renderer_never_exposes_private_corpus_metadata(self) -> None:
        rendered_rows = pipeline.load_jsonl(
            pipeline.RELEASE_ROOT / "rendered_trainable.jsonl"
        )
        self.assertEqual(
            {row["object_id"] for row in rendered_rows},
            set(self.manifest["eligible_object_ids"]),
        )
        for row in rendered_rows:
            text = row["rendered_text"].casefold()
            record = self.by_id[row["object_id"]]
            with self.subTest(object_id=row["object_id"]):
                self.assertIsNone(
                    re.search(r"(?<![a-z0-9_])agnostic(?![a-z0-9_])", text)
                )
                self.assertNotIn("corpus origin", text)
                self.assertNotIn("quality_state", text)
                self.assertNotIn("teacher_provenance", text)
                self.assertNotIn(row["object_id"].casefold(), text)
                self.assertEqual(
                    hashlib.sha256(row["rendered_text"].encode()).hexdigest(),
                    row["rendered_sha256"],
                )
                self.assertEqual(
                    interchange.render_training_example(
                        record,
                        self.by_id,
                        lambda item: str(item["content"]),
                    ),
                    row["rendered_text"],
                )

    def test_renderer_is_invariant_to_private_origin_metadata(self) -> None:
        record = next(
            item
            for item in self.records
            if item["object_role"] == "interpretation"
            and item["training_eligibility"] == "eligible"
        )
        changed = copy.deepcopy(record)
        changed["corpus_origin"] = "counterfactual-private-origin"
        changed["corpus_release_id"] = "counterfactual-private-release"
        original_text = interchange.render_training_example(
            record, self.by_id, lambda item: str(item["content"])
        )
        changed_text = interchange.render_training_example(
            changed, self.by_id, lambda item: str(item["content"])
        )
        self.assertEqual(original_text, changed_text)

    def test_source_lineage_and_content_hashes_are_exact(self) -> None:
        acquisition = {
            row["source_id"]: row
            for row in pipeline.read_json(
                pipeline.RELEASE_ROOT / "acquisition_snapshot.json"
            )["artifacts"]
        }
        used_sources = {spec["source_id"] for spec in UNIT_SPECS}
        self.assertEqual(set(acquisition), used_sources)
        self.assertEqual(len(acquisition), 25)
        for record in self.records:
            with self.subTest(object_id=record["object_id"]):
                self.assertEqual(
                    hashlib.sha256(record["content"].encode()).hexdigest(),
                    record["content_sha256"],
                )
                self.assertTrue(record["span_lineage"])
                if record["object_role"] == "source":
                    self.assertEqual(
                        record["teacher_provenance"]["kind"],
                        "Codex-authored source-grounded mathematical restatement",
                    )
                    self.assertFalse(
                        record["teacher_provenance"]["verbatim_source_text"]
                    )
                for lineage in record["span_lineage"]:
                    self.assertTrue(lineage["exact_span"])
                    self.assertTrue(lineage["source_url"])
                    self.assertEqual(
                        lineage["artifact_sha256"],
                        acquisition[lineage["source_id"]]["artifact_sha256"],
                    )

    def test_geometry_is_primary_and_sidecars_resolve(self) -> None:
        report = pipeline.read_json(pipeline.RELEASE_ROOT / "corpus_report.json")
        geometry = report["geometry_audit"]
        self.assertEqual(geometry["status"], "pass")
        self.assertGreaterEqual(geometry["primary_source_unit_count"], 45)
        self.assertGreaterEqual(len(geometry["represented_modes"]), 8)
        self.assertEqual(len(self.sidecars), 4)
        self.assertEqual(
            pipeline.validate_sidecar_manifest(self.records, self.sidecars), []
        )
        for sidecar in self.sidecars:
            with self.subTest(sidecar=sidecar["sidecar_id"]):
                path = pipeline.ROOT / sidecar["path"]
                self.assertTrue(path.is_file())
                self.assertEqual(pipeline.sha256_file(path), sidecar["sha256"])
                source_object = self.by_id[sidecar["source_object_id"]]
                self.assertEqual(source_object["object_role"], "source")
                self.assertIn(
                    sidecar["source_unit_id"], source_object["source_unit_ids"]
                )
                self.assertEqual(sidecar["necessity"], "helpful")
                self.assertEqual(
                    sidecar["representation_type"], "svg_editorial_reconstruction"
                )

        changed_sidecars = copy.deepcopy(self.sidecars)
        changed_sidecars[0]["source_object_id"] = (
            "mathia:agnostic:v1:source:qf_surface_identification"
        )
        errors = pipeline.validate_sidecar_manifest(self.records, changed_sidecars)
        self.assertTrue(
            any("unresolved canonical source object" in error for error in errors)
        )

        changed_records = copy.deepcopy(self.records)
        record_with_sidecar = next(
            record for record in changed_records if record["representation_dependencies"]
        )
        record_with_sidecar["representation_dependencies"][0]["content_sha256"] = (
            "0" * 64
        )
        errors = pipeline.validate_sidecar_manifest(changed_records, self.sidecars)
        self.assertTrue(
            any("descriptor disagrees with manifest" in error for error in errors)
        )

    def test_cross_corpus_dry_run_uses_actual_full_releases(self) -> None:
        mixed = pipeline.read_json(
            pipeline.RELEASE_ROOT / "synthetic_mixed_dry_run.json"
        )
        riemann_records = pipeline.load_jsonl(riemann_full.OBJECTS_PATH)
        self.assertEqual(mixed["contract_version"], interchange.CONTRACT_VERSION)
        expected_eligible = sum(
            record["training_eligibility"] == "eligible"
            for record in self.records + riemann_records
        )
        self.assertEqual(len(mixed["selections"]), expected_eligible)
        self.assertEqual(
            {row["corpus_release_id"] for row in mixed["selections"]},
            {RELEASE_ID, riemann_full.RELEASE_ID},
        )
        for release_id in (RELEASE_ID, riemann_full.RELEASE_ID):
            self.assertEqual(
                {
                    row["object_role"]
                    for row in mixed["selections"]
                    if row["corpus_release_id"] == release_id
                },
                {"source", "interpretation", "synthesis"},
            )
        self.assertEqual(
            mixed["duplicate_groups"],
            interchange.duplicate_groups([self.records, riemann_records]),
        )
        self.assertEqual(interchange.validate_release(riemann_records, None), [])

    def test_validator_rejects_eligibility_hash_and_source_parent_drift(self) -> None:
        changed = copy.deepcopy(self.records)
        rejected = next(
            record for record in changed if record["quality_state"] == "rejected"
        )
        rejected["training_eligibility"] = "eligible"
        errors = interchange.validate_release(
            changed, lambda record: str(record["content"])
        )
        self.assertTrue(any("only accepted records may be eligible" in error for error in errors))

        changed = copy.deepcopy(self.records)
        changed[0]["content"] += " drift"
        errors = interchange.validate_release(
            changed, lambda record: str(record["content"])
        )
        self.assertTrue(any("content hash mismatch" in error for error in errors))

        changed = copy.deepcopy(self.records)
        source = next(record for record in changed if record["object_role"] == "source")
        source["parent_ids"] = [changed[1]["object_id"]]
        errors = interchange.validate_release(
            changed, lambda record: str(record["content"])
        )
        self.assertTrue(any("source object cannot have parents" in error for error in errors))

    def test_external_artifact_verifier_is_explicit(self) -> None:
        errors = pipeline.validate_artifacts(Path("/definitely/missing"))
        self.assertEqual(len(errors), 25)
        self.assertTrue(all("missing source artifact" in error for error in errors))

    def test_report_exposes_depth_bias_and_style_measurements(self) -> None:
        report = pipeline.read_json(pipeline.RELEASE_ROOT / "corpus_report.json")
        self.assertTrue(report["depth"]["all_ecosystems_have_three_units"])
        self.assertTrue(
            report["depth"]["all_ecosystems_have_proof_or_worked_development"]
        )
        self.assertEqual(report["depth"]["proof_or_worked_development_count"], 50)
        self.assertEqual(report["depth"]["unresolved_distinct_depth_gap_count"], 0)
        self.assertGreaterEqual(
            report["depth"]["source_unit_word_count"]["proof_or_worked_minimum"],
            100,
        )
        self.assertIn("semantic_units_by_source_type", report["counts"])
        self.assertIn("semantic_units_by_primary_domain", report["counts"])
        self.assertGreater(report["counts"]["rendered_trainable_words"], 34000)
        self.assertLess(
            report["teacher_style_audit"]["exactly_four_sentence_fraction"], 0.3
        )

    def test_final_report_is_bounded_and_has_fresh_qa(self) -> None:
        report = pipeline.read_json(pipeline.RELEASE_ROOT / "corpus_report.json")
        self.assertEqual(report["final_decision"], "AGNOSTIC_MATHIA_CORPUS_READY")
        self.assertFalse(report["quality_audit"]["unresolved_material_failure_count"])
        self.assertGreater(report["quality_audit"]["fresh_review_count"], 0)
        self.assertTrue(report["quality_audit"]["complete_criterion_coverage"])
        self.assertIn(
            "not mathematically or bibliographically exhaustive",
            report["depth"]["warning"],
        )
        self.assertIn("no model training", " ".join(report["prohibited_implications"]))

    def test_fresh_qa_is_bound_to_recomputable_review_content(self) -> None:
        review_freeze = pipeline.read_json(pipeline.REVIEW_CONTENT_FREEZE_PATH)
        without_id = {
            key: value
            for key, value in review_freeze.items()
            if key != "review_content_freeze_id"
        }
        expected_id = "review_content_" + pipeline.sha256_text(
            pipeline.canonical_json(without_id)
        )
        self.assertEqual(review_freeze["review_content_freeze_id"], expected_id)
        frozen_paths = {row["path"] for row in review_freeze["files"]}
        self.assertIn(
            str(riemann_full.OBJECTS_PATH.relative_to(pipeline.REPO_ROOT)),
            frozen_paths,
        )
        self.assertIn(
            str(riemann_full.FREEZE_PATH.relative_to(pipeline.REPO_ROOT)),
            frozen_paths,
        )
        for relative_path in pipeline.SIDECAR_PATHS.values():
            self.assertIn(
                str((pipeline.ROOT / relative_path).relative_to(pipeline.REPO_ROOT)),
                frozen_paths,
            )
        for row in review_freeze["files"]:
            path = pipeline.REPO_ROOT / row["path"]
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(pipeline.sha256_file(path), row["sha256"])
        reviews = pipeline.load_jsonl(pipeline.QUALITY_REVIEWS_PATH)
        self.assertEqual(
            {review["review_content_freeze_id"] for review in reviews},
            {expected_id},
        )
        report = pipeline.read_json(pipeline.RELEASE_ROOT / "corpus_report.json")
        final_freeze = pipeline.read_json(pipeline.RELEASE_ROOT / "freeze.json")
        self.assertEqual(
            report["quality_audit"]["review_content_freeze_id"], expected_id
        )
        self.assertEqual(final_freeze["review_content_freeze_id"], expected_id)

    def test_cli_reports_valid_frozen_release(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "experiments.agnostic_mathia_corpus", "validate"],
            cwd=pipeline.REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        value = json.loads(completed.stdout)
        self.assertTrue(value["valid"])
        self.assertEqual(value["final_decision"], "AGNOSTIC_MATHIA_CORPUS_READY")
        self.assertEqual(value["counts"]["semantic_source_units"], 98)


if __name__ == "__main__":
    unittest.main()
