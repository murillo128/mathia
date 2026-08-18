import json
import tempfile
import unittest
from pathlib import Path

from experiments.riemann_corpus import pipeline


class RiemannCorpusTests(unittest.TestCase):
    def test_committed_inventory_is_internally_valid(self) -> None:
        self.assertEqual(pipeline.validate_inventory(Path("/does-not-exist"), False), [])

    def test_citation_screen_rejects_generic_neighbors(self) -> None:
        rejected = (
            "Universality for random matrices and quantum chaos",
            "Evaluating Rational Functions",
            "Handbook of Mathematical Functions",
            "A Treatise on the Theory of Bessel Functions",
            "Higher Transcendental Functions",
            "The moduli space of Riemann surfaces",
            "The Riemann-Hilbert correspondence and motivic Galois theory",
            "Computing Hilbert class polynomials with the Chinese remainder theorem",
            "The Hadamard factorization of the Selberg zeta function on a compact Riemann surface",
            "Rigorous high-precision computation of the Hurwitz zeta function",
        )
        for title in rejected:
            with self.subTest(title=title):
                self.assertFalse(pipeline.citation_is_relevant({"display_name": title}))
        self.assertTrue(
            pipeline.citation_is_relevant(
                {"display_name": "Random matrix theory and the Riemann zeta function"}
            )
        )
        self.assertTrue(
            pipeline.citation_is_relevant(
                {"display_name": "Zero-density estimates for L-functions"}
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

    def test_artifact_verifier_rejects_unledgered_retained_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            raw = Path(directory) / "raw"
            raw.mkdir()
            (raw / "unledgered.pdf").write_bytes(b"%PDF-test")
            errors = pipeline.verify_artifacts(Path(directory))
        self.assertTrue(any("unledgered retained artifact" in error for error in errors))

    def test_all_six_scans_have_hashes_and_flagged_ocr(self) -> None:
        inventory = {
            record["source_id"]: record for record in pipeline.load_jsonl(pipeline.INVENTORY_PATH)
        }
        expected = {
            "openalex_w1608183925": (
                "20f721d9cd2e37785ef5530c881e25840c5bdf454ef63f95f569ffd9f8a02db9",
                6,
            ),
            "openalex_w2050389282": (
                "9cbdc75c45ca572e102cdfdf39dfc72821384fb85b02f2adb1b4064f6b65b6a7",
                5,
            ),
            "openalex_w343820166": (
                "cbe2d1e7115717cf28f9ffaffdc1fe232958595b17c5c2ee59fc968e8ff0d5a1",
                5,
            ),
            "openalex_w40132115": (
                "667d425d8b1a686a2d85595383e8f5dc78a8f8ff9ae1f276d063e7edbf7844c0",
                8,
            ),
            "openalex_w981942693": (
                "fbd26dcd338bff3f2977b8ee8576f3cbe1c54ee23b96f2ccaa8b9ff00bd6d122",
                5,
            ),
            "openalex_w998105725": (
                "0bd9c359a25ae25520c6d1f2b3709a4b2cdd96d5eb8494666e2fd0c7beb5e554",
                3,
            ),
        }
        ocr_source_ids = {
            source_id
            for source_id, record in inventory.items()
            if record.get("scope_status") == "relevant"
            and any("OCR fallback used" in warning for warning in record["acquisition_warnings"])
        }
        self.assertEqual(ocr_source_ids, set(expected))
        for source_id, (raw_hash, page_count) in expected.items():
            with self.subTest(source_id=source_id):
                record = inventory[source_id]
                self.assertEqual(record["scope_status"], "relevant")
                self.assertEqual(record["acquisition_status"], "acquired-and-normalized")
                self.assertEqual(record["artifact_sha256"], raw_hash)
                self.assertEqual(record["normalized_page_count"], page_count)
                self.assertGreater(record["normalized_bytes"], 1000)
                self.assertEqual(len(record["normalized_sha256"]), 64)
                self.assertTrue(
                    any("OCR fallback used" in warning for warning in record["acquisition_warnings"])
                )

    def test_preprint_published_pairs_are_linked(self) -> None:
        inventory = {
            record["source_id"]: record for record in pipeline.load_jsonl(pipeline.INVENTORY_PATH)
        }
        expected = {
            "openalex_w2950102297": "openalex_w1964482233",
            "openalex_w2951993830": "openalex_w1988856634",
            "openalex_w2952163178": "openalex_w2016676915",
            "openalex_w3106435960": "openalex_w1913535681",
            "openalex_w1649284210": "openalex_w2090804474",
        }
        for preprint_id, published_id in expected.items():
            with self.subTest(preprint_id=preprint_id):
                preprint = inventory[preprint_id]
                published = inventory[published_id]
                self.assertEqual(preprint["scope_status"], "duplicate")
                self.assertEqual(preprint["duplicate_of"], published_id)
                self.assertEqual(preprint["version_relationship"], "preprint/published-version")
                self.assertIn(preprint_id, published["alternate_version_source_ids"])

    def test_same_author_series_papers_are_not_deduplicated(self) -> None:
        inventory = {
            record["source_id"]: record for record in pipeline.load_jsonl(pipeline.INVENTORY_PATH)
        }
        distinct_pairs = (
            ("openalex_w2095903919", "openalex_w4213378054"),
            ("openalex_w2105964741", "openalex_w4241483398"),
            ("openalex_w2042837137", "openalex_w2116781013"),
        )
        for first_id, second_id in distinct_pairs:
            with self.subTest(first_id=first_id, second_id=second_id):
                self.assertEqual(inventory[first_id]["scope_status"], "relevant")
                self.assertEqual(inventory[second_id]["scope_status"], "relevant")


if __name__ == "__main__":
    unittest.main()
