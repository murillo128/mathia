import unittest
from collections import Counter
from pathlib import Path

from experiments.riemann_corpus import full_corpus


class RiemannFullCorpusTests(unittest.TestCase):
    def test_source_inspection_covers_every_candidate_input(self) -> None:
        inspections = full_corpus.load_jsonl(full_corpus.SOURCE_INSPECTION_PATH)
        self.assertEqual(len(inspections), 94)
        self.assertEqual(
            Counter(record["inspection_decision"] for record in inspections),
            Counter({"usable": 79, "usable_with_limits": 7, "excluded": 8}),
        )

    def test_nonquota_expansion_is_variable_and_lineage_complete(self) -> None:
        expansion = [
            record
            for path in sorted(full_corpus.SEGMENT_EXPANSION_PLAN_ROOT.glob("batch_*.jsonl"))
            for record in full_corpus.load_jsonl(path)
        ]
        self.assertEqual(len(expansion), 74)
        self.assertEqual(
            Counter(len(record["additional_units"]) for record in expansion),
            Counter({0: 5, 1: 10, 2: 25, 3: 20, 4: 14}),
        )
        units = full_corpus.load_jsonl(full_corpus.UNITS_PATH)
        self.assertEqual(len(units), 274)
        self.assertEqual(len({unit["source_id"] for unit in units}), 86)
        per_source = Counter(unit["source_id"] for unit in units)
        self.assertGreater(len(set(per_source.values())), 1)

    def test_units_and_four_pass_lineage_validate_without_artifacts(self) -> None:
        self.assertEqual(full_corpus.validate_units(Path("/does-not-exist"), False), [])
        self.assertEqual(full_corpus.validate_analysis(), [])
        revised = full_corpus.load_jsonl(full_corpus.PASS_FILES["revised"])
        self.assertEqual(
            Counter(record["output"]["decision"] for record in revised),
            Counter({"accepted": 267, "quarantined": 6, "rejected": 1}),
        )

    def test_synthesis_and_shared_interchange_release_are_consistent(self) -> None:
        self.assertEqual(full_corpus.validate_synthesis(), [])
        syntheses = full_corpus.load_jsonl(full_corpus.SYNTHESIS_ROOT / "final.jsonl")
        self.assertEqual(
            Counter(record["decision"] for record in syntheses),
            Counter({"accepted": 16, "quarantined": 1, "rejected": 3}),
        )
        self.assertEqual(
            full_corpus.validate_objects(Path("/does-not-exist"), False),
            [],
        )
        manifest = full_corpus.load_json(full_corpus.TRAINABLE_MANIFEST_PATH)
        self.assertEqual(
            manifest["object_counts"],
            {"source": 274, "interpretation": 267, "synthesis": 16},
        )
        self.assertEqual(len(manifest["eligible_object_ids"]), 557)
        mixed = full_corpus.load_json(full_corpus.MIXED_MANIFEST_PATH)
        self.assertEqual(
            {selection["corpus_release_id"] for selection in mixed["selections"]},
            {"riemann-mathia-full-v1", "mathia-agnostic-representative-v1"},
        )

    def test_blinded_independent_audit_and_reconciliation_validate(self) -> None:
        assignment = full_corpus.load_json(full_corpus.AUDIT_ROOT / "assignment.json")
        self.assertEqual(len(assignment["interpretations"]), 64)
        self.assertEqual(len(assignment["syntheses"]), 20)
        self.assertTrue(
            all("current_quality_state" not in record for record in assignment["interpretations"])
        )
        self.assertTrue(
            all("current_quality_state" not in record for record in assignment["syntheses"])
        )
        audit = full_corpus.load_jsonl(full_corpus.AUDIT_ROOT / "independent_review.jsonl")
        self.assertEqual(
            Counter(record["decision"] for record in audit),
            Counter({"accept": 73, "quarantine": 6, "reject": 5}),
        )
        self.assertEqual(full_corpus.validate_audit(), [])


if __name__ == "__main__":
    unittest.main()
