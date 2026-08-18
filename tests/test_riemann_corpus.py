import json
import tempfile
import unittest
from pathlib import Path

from experiments.riemann_corpus import pipeline


class RiemannCorpusTests(unittest.TestCase):
    def test_committed_inventory_is_internally_valid(self) -> None:
        self.assertEqual(pipeline.validate_inventory(Path("/does-not-exist"), False), [])

    def test_citation_screen_rejects_generic_neighbors(self) -> None:
        self.assertFalse(
            pipeline.citation_is_relevant(
                {"display_name": "Universality for random matrices and quantum chaos"}
            )
        )
        self.assertTrue(
            pipeline.citation_is_relevant(
                {"display_name": "Random matrix theory and the Riemann zeta function"}
            )
        )

    def test_pilot_shape_and_hashes_without_external_artifacts(self) -> None:
        errors = pipeline.validate_pilot(Path("/does-not-exist"), False)
        missing_passes = [error for error in errors if error.startswith("missing analysis pass:")]
        self.assertEqual(errors, missing_passes)
        freeze = json.loads((pipeline.PILOT_ROOT / "freeze.json").read_text(encoding="utf-8"))
        units = pipeline.load_jsonl(pipeline.PILOT_ROOT / "units.jsonl")
        self.assertEqual(freeze["source_count"], 12)
        self.assertEqual(len(units), 24)
        per_source_counts = {
            sum(unit["source_id"] == source["source_id"] for unit in units)
            for source in freeze["sources"]
        }
        self.assertEqual(per_source_counts, {2})

    def test_artifact_verifier_reports_missing_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            errors = pipeline.verify_artifacts(Path(directory))
        self.assertTrue(errors)
        self.assertTrue(all("missing" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
