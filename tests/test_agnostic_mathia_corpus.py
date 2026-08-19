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

from experiments.agnostic_mathia_corpus import pipeline
from experiments.agnostic_mathia_corpus.catalog_ecosystems import ECOSYSTEMS
from experiments.agnostic_mathia_corpus.catalog_sources import SOURCE_BY_ID
from experiments.agnostic_mathia_corpus.catalog_units import UNIT_SPECS
from experiments.mathia_corpus.interchange import (
    materialize_mixed_manifest,
    validate_release,
)


class AgnosticMathiaCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.records = pipeline.load_jsonl(pipeline.RELEASE_ROOT / "records.jsonl")
        cls.sidecars = pipeline.load_jsonl(pipeline.RELEASE_ROOT / "sidecars.jsonl")
        cls.manifest = pipeline.read_json(
            pipeline.RELEASE_ROOT / "trainable_manifest.json"
        )

    def test_committed_release_validates_without_external_artifacts(self) -> None:
        self.assertEqual(pipeline.validate_committed_release(), [])

    def test_coverage_map_is_broad_editable_and_seeded(self) -> None:
        coverage = pipeline.read_json(pipeline.RELEASE_ROOT / "coverage_map.json")
        self.assertEqual(len(coverage["ecosystems"]), 24)
        self.assertEqual(coverage["status"], "working_search_instrument_not_ontology")
        self.assertEqual(coverage["revision_history"][0]["ecosystem_count"], 22)
        self.assertEqual(coverage["revision_history"][-1]["ecosystem_count"], 24)
        for ecosystem in coverage["ecosystems"]:
            with self.subTest(ecosystem=ecosystem["ecosystem_id"]):
                self.assertGreaterEqual(len(ecosystem["seed_source_ids"]), 3)
                self.assertLessEqual(
                    set(ecosystem["seed_source_ids"]), set(SOURCE_BY_ID)
                )
                self.assertEqual(
                    ecosystem["map_status"], "working_search_instrument_not_ontology"
                )

    def test_every_ecosystem_has_three_units_and_proof_depth(self) -> None:
        counts = Counter(spec["ecosystem_id"] for spec in UNIT_SPECS)
        self.assertEqual(len(UNIT_SPECS), 72)
        self.assertEqual(set(counts), {item["ecosystem_id"] for item in ECOSYSTEMS})
        self.assertEqual(set(counts.values()), {3})
        self.assertEqual(len({spec["unit_id"] for spec in UNIT_SPECS}), 72)
        for ecosystem in ECOSYSTEMS:
            deep = [
                spec
                for spec in UNIT_SPECS
                if spec["ecosystem_id"] == ecosystem["ecosystem_id"]
                and spec["depth_tier"] == "proof_or_worked_development"
            ]
            self.assertEqual(len(deep), 1)
            self.assertGreaterEqual(len(deep[0]["source_math"].split()), 100)

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

    def test_acceptance_semantics_exclude_every_negative_and_probe(self) -> None:
        manifest_ids = set(self.manifest["eligible_object_ids"])
        states = Counter(record["acceptance_state"] for record in self.records)
        self.assertEqual(
            states,
            Counter(
                {
                    "accepted": 158,
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
                    record["acceptance_state"] == "accepted",
                )
                if record["acceptance_state"] != "accepted":
                    self.assertTrue(record["exclusion_reason"])

    def test_renderer_never_exposes_private_corpus_or_review_metadata(self) -> None:
        by_id = {record["object_id"]: record for record in self.records}
        rendered_rows = pipeline.load_jsonl(
            pipeline.RELEASE_ROOT / "rendered_trainable.jsonl"
        )
        self.assertEqual(
            {row["object_id"] for row in rendered_rows},
            set(self.manifest["eligible_object_ids"]),
        )
        for row in rendered_rows:
            text = row["rendered_text"].casefold()
            with self.subTest(object_id=row["object_id"]):
                self.assertIsNone(
                    re.search(r"(?<![a-z0-9_])agnostic(?![a-z0-9_])", text)
                )
                self.assertNotIn("corpus origin", text)
                self.assertNotIn("acceptance_state", text)
                self.assertNotIn("teacher_provenance", text)
                self.assertNotIn(row["object_id"].casefold(), text)
                self.assertEqual(
                    hashlib.sha256(row["rendered_text"].encode()).hexdigest(),
                    row["rendered_sha256"],
                )
                self.assertEqual(
                    pipeline.render_record(by_id[row["object_id"]], by_id),
                    row["rendered_text"],
                )

    def test_origin_leak_check_uses_tokens_not_substrings(self) -> None:
        errors = validate_release(
            self.records, self.sidecars, self.manifest, root=pipeline.ROOT
        )
        self.assertFalse(any("origin leaked" in error for error in errors))
        changed = copy.deepcopy(self.records)
        interpretation = next(
            record
            for record in changed
            if record["object_role"] == "interpretation"
            and record["training_eligible"]
        )
        interpretation["content"] += " This sentence reveals agnostic origin."
        interpretation["content_sha256"] = hashlib.sha256(
            interpretation["content"].encode()
        ).hexdigest()
        errors = validate_release(
            changed, self.sidecars, self.manifest, root=pipeline.ROOT
        )
        self.assertTrue(any("origin leaked" in error for error in errors))

    def test_source_lineage_and_content_hashes_are_exact(self) -> None:
        acquisition = {
            row["source_id"]: row
            for row in pipeline.read_json(
                pipeline.RELEASE_ROOT / "acquisition_snapshot.json"
            )["artifacts"]
        }
        self.assertEqual(
            set(acquisition), {spec["source_id"] for spec in UNIT_SPECS}
        )
        self.assertEqual(len(acquisition), 19)
        for record in self.records:
            with self.subTest(object_id=record["object_id"]):
                self.assertEqual(
                    hashlib.sha256(record["content"].encode()).hexdigest(),
                    record["content_sha256"],
                )
                self.assertTrue(record["lineage"])
                if record["object_role"] == "source":
                    self.assertEqual(
                        record["extractor_provenance"]["kind"],
                        "Codex-authored source-grounded mathematical restatement",
                    )
                    self.assertFalse(
                        record["extractor_provenance"]["verbatim_source_text"]
                    )
                for lineage in record["lineage"]:
                    self.assertTrue(lineage["exact_span"])
                    self.assertTrue(lineage["source_url"])
                    if lineage["source_id"] in acquisition:
                        self.assertEqual(
                            lineage["artifact_sha256"],
                            acquisition[lineage["source_id"]]["artifact_sha256"],
                        )

    def test_geometry_is_primary_and_sidecars_resolve(self) -> None:
        report = pipeline.read_json(pipeline.RELEASE_ROOT / "corpus_report.json")
        geometry = report["geometry_audit"]
        self.assertEqual(geometry["status"], "pass")
        self.assertGreaterEqual(geometry["primary_source_unit_count"], 20)
        self.assertGreaterEqual(len(geometry["represented_modes"]), 8)
        self.assertEqual(len(self.sidecars), 4)
        for sidecar in self.sidecars:
            with self.subTest(sidecar=sidecar["sidecar_id"]):
                path = pipeline.ROOT / sidecar["path"]
                self.assertTrue(path.is_file())
                self.assertEqual(pipeline.sha256_file(path), sidecar["sha256"])
                self.assertEqual(sidecar["necessity"], "helpful")
                self.assertEqual(
                    sidecar["representation_type"], "svg_editorial_reconstruction"
                )

    def test_cross_corpus_mixer_uses_one_renderer_and_detects_duplicate(self) -> None:
        fixture_records = pipeline.load_jsonl(
            pipeline.COMMON_FIXTURE_ROOT / "records.jsonl"
        )
        mixed = materialize_mixed_manifest(
            [self.records, fixture_records], per_release=4
        )
        self.assertEqual(
            {row["private_analysis"]["corpus_origin"] for row in mixed["records"]},
            {"agnostic", "riemann"},
        )
        self.assertTrue(mixed["duplicate_groups"])
        duplicate = mixed["duplicate_groups"][0]
        self.assertEqual(duplicate["object_role"], "source")
        self.assertEqual(duplicate["corpus_origins"], ["agnostic", "riemann"])
        for row in mixed["records"]:
            folded = row["rendered_text"].casefold()
            self.assertIsNone(
                re.search(r"(?<![a-z0-9_])agnostic(?![a-z0-9_])", folded)
            )
            self.assertIsNone(
                re.search(r"(?<![a-z0-9_])riemann(?![a-z0-9_])", folded)
            )

    def test_validator_rejects_eligibility_and_hash_drift(self) -> None:
        changed = copy.deepcopy(self.records)
        rejected = next(
            record for record in changed if record["acceptance_state"] == "rejected"
        )
        rejected["training_eligible"] = True
        errors = validate_release(changed, self.sidecars, self.manifest, root=pipeline.ROOT)
        self.assertTrue(any("acceptance/eligibility mismatch" in error for error in errors))

        changed = copy.deepcopy(self.records)
        changed[0]["content"] += " drift"
        errors = validate_release(changed, self.sidecars, self.manifest, root=pipeline.ROOT)
        self.assertTrue(any("content hash mismatch" in error for error in errors))

        changed = copy.deepcopy(self.records)
        source = next(
            record for record in changed if record["object_role"] == "source"
        )
        source["extractor_provenance"] = None
        errors = validate_release(changed, self.sidecars, self.manifest, root=pipeline.ROOT)
        self.assertTrue(
            any("lacks extractor provenance" in error for error in errors)
        )

    def test_external_artifact_verifier_is_explicit(self) -> None:
        errors = pipeline.validate_artifacts(Path("/definitely/missing"))
        self.assertEqual(len(errors), 19)
        self.assertTrue(all("missing source artifact" in error for error in errors))

    def test_report_exposes_depth_bias_and_style_measurements(self) -> None:
        report = pipeline.read_json(pipeline.RELEASE_ROOT / "corpus_report.json")
        self.assertTrue(report["depth"]["all_ecosystems_have_three_units"])
        self.assertTrue(
            report["depth"]["all_ecosystems_have_proof_or_worked_development"]
        )
        self.assertEqual(report["depth"]["proof_or_worked_development_count"], 24)
        self.assertGreaterEqual(report["depth"]["source_unit_word_count"]["proof_or_worked_minimum"], 100)
        self.assertIn("semantic_units_by_source_type", report["counts"])
        self.assertIn("semantic_units_by_primary_domain", report["counts"])
        self.assertGreater(report["counts"]["rendered_trainable_words"], 19000)
        self.assertLess(
            report["teacher_style_audit"]["exactly_four_sentence_fraction"], 0.4
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
        self.assertEqual(value["counts"]["semantic_source_units"], 72)


if __name__ == "__main__":
    unittest.main()
