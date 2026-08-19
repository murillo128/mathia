import copy
import unittest
from pathlib import Path

from experiments.mathia_corpus import interchange


FIXTURE = (
    Path(__file__).resolve().parents[1]
    / "experiments"
    / "mathia_corpus"
    / "fixtures"
    / "agnostic_release.jsonl"
)


class MathiaCorpusInterchangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.records = interchange.load_jsonl(FIXTURE)
        cls.by_id = {record["object_id"]: record for record in cls.records}
        cls.loader = lambda record: record["content"]

    def test_pdf_control_bytes_are_rendered_as_explicit_loss(self) -> None:
        self.assertEqual(
            interchange.normalize_visible_text("a\x02b\f c"),
            "a\ufffdb\n c",
        )

    def test_representative_agnostic_fixture_is_valid(self) -> None:
        self.assertEqual(interchange.validate_release(self.records, self.loader), [])
        self.assertEqual(
            {record["object_role"] for record in self.records},
            {"source", "interpretation", "synthesis"},
        )

    def test_renderer_hides_private_metadata(self) -> None:
        for record in self.records:
            rendered = interchange.render_training_example(record, self.by_id, self.loader)
            changed = copy.deepcopy(record)
            changed["corpus_origin"] = "private-counterfactual-origin"
            changed["corpus_release_id"] = "private-counterfactual-release"
            self.assertEqual(
                rendered,
                interchange.render_training_example(changed, self.by_id, self.loader),
            )
            self.assertNotIn(record["corpus_release_id"], rendered)
            self.assertNotIn(record["object_id"], rendered)

    def test_rejected_and_evaluation_only_records_cannot_render(self) -> None:
        record = copy.deepcopy(self.records[0])
        for state in ("rejected", "quarantined", "evaluation_only"):
            with self.subTest(state=state):
                record["quality_state"] = state
                record["training_eligibility"] = "ineligible"
                record["exclusion_reason"] = "test exclusion"
                with self.assertRaises(ValueError):
                    interchange.render_training_example(record, self.by_id, self.loader)

    def test_missing_essential_sidecar_blocks_eligibility(self) -> None:
        record = copy.deepcopy(self.records[0])
        record["representation_dependencies"] = [
            {
                "asset_id": "missing-figure",
                "relationship": "essential",
                "availability": "unavailable",
                "content_ref": None,
                "content_sha256": None,
            }
        ]
        errors = interchange.validate_release([record], self.loader)
        self.assertTrue(any("missing essential representation" in error for error in errors))

    def test_mixed_manifest_uses_both_releases_without_conversion(self) -> None:
        second = copy.deepcopy(self.records)
        for record in second:
            record["corpus_release_id"] = "second-compatible-release"
            record["corpus_origin"] = "riemann"
        manifest = interchange.materialize_mixed_manifest(
            [self.records, second], [self.loader, self.loader], per_release=2
        )
        self.assertEqual(manifest["contract_version"], interchange.CONTRACT_VERSION)
        self.assertGreaterEqual(len(manifest["selections"]), 2)
        self.assertEqual(
            {selection["corpus_release_id"] for selection in manifest["selections"]},
            {"mathia-agnostic-representative-v1", "second-compatible-release"},
        )
        self.assertTrue(manifest["duplicate_groups"])
        self.assertTrue(
            all(len({member["corpus_release_id"] for member in group["members"]}) > 1
                for group in manifest["duplicate_groups"])
        )
        self.assertIn("compatibility dry run only", manifest["purpose"])


if __name__ == "__main__":
    unittest.main()
