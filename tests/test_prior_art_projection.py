import unittest

from experiments import prior_art_projection


class PriorArtProjectionTests(unittest.TestCase):
    def test_catalog_and_rendered_notes_are_valid(self) -> None:
        catalog = prior_art_projection.load_json(prior_art_projection.CATALOG_PATH)
        self.assertEqual([], prior_art_projection.validate_catalog(catalog))
        self.assertEqual([], prior_art_projection.validate_rendered_notes(catalog))

    def test_slug_folds_diacritics_and_punctuation(self) -> None:
        self.assertEqual(
            "hilbert-polya-program",
            prior_art_projection.canonical_slug("Hilbert–Pólya program"),
        )


if __name__ == "__main__":
    unittest.main()
