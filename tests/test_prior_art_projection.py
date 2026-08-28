import unittest

from experiments import prior_art_projection


class PriorArtProjectionTests(unittest.TestCase):
    def test_catalog_and_rendered_notes_are_valid(self) -> None:
        catalog = prior_art_projection.load_json(prior_art_projection.CATALOG_PATH)
        self.assertEqual([], prior_art_projection.validate_catalog(catalog))
        self.assertEqual([], prior_art_projection.validate_rendered_notes(catalog))
        self.assertEqual([], prior_art_projection.validate_coverage(catalog))

    def test_review_census_covers_every_note(self) -> None:
        catalog = prior_art_projection.load_json(prior_art_projection.CATALOG_PATH)
        mandatory, remaining = prior_art_projection._review_cohorts(catalog)
        self.assertEqual(
            {node["id"] for node in catalog["nodes"]}, set(mandatory) | set(remaining)
        )
        self.assertEqual(
            remaining, catalog["coverage"]["independent_review_sample"]
        )

    def test_slug_folds_diacritics_and_punctuation(self) -> None:
        self.assertEqual(
            "hilbert-polya-program",
            prior_art_projection.canonical_slug("Hilbert–Pólya program"),
        )


if __name__ == "__main__":
    unittest.main()
