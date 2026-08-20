import json
import os
import re
import sqlite3
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from experiments.openalex_discovery import pipeline


class OpenAlexDiscoveryTests(unittest.TestCase):
    def test_committed_seed_inventory_is_broad_and_exact(self) -> None:
        seeds = pipeline.build_seed_records()
        self.assertEqual(len(seeds), 393)
        self.assertEqual(sum(bool(row["openalex_id"]) for row in seeds), 381)
        self.assertEqual(len({row["source_id"] for row in seeds}), 393)
        self.assertTrue(all(row["title_normalized"] for row in seeds))

    def test_identifier_normalization(self) -> None:
        self.assertEqual(
            pipeline.normalized_openalex_id("https://openalex.org/w123"),
            "https://openalex.org/W123",
        )
        self.assertEqual(
            pipeline.normalized_doi("https://doi.org/10.1/ABC."), "10.1/abc"
        )
        self.assertIsNone(pipeline.normalized_openalex_id("not-a-work"))

    def test_agnostic_seed_release_is_exact_and_bounded(self) -> None:
        seeds = pipeline.build_agnostic_seed_records()
        coverage = json.loads(
            (pipeline.AGNOSTIC_RELEASE / "coverage_map.json").read_text()
        )
        ecosystem_ids = {row["ecosystem_id"] for row in coverage["ecosystems"]}
        self.assertEqual(len(seeds), 28)
        self.assertEqual(len({row["source_id"] for row in seeds}), 28)
        self.assertTrue(all(row["ecosystem_ids"] for row in seeds))
        self.assertEqual(set(pipeline.AGNOSTIC_LENS_PATTERNS), ecosystem_ids)
        self.assertTrue(
            all(
                set(rule[1]) <= ecosystem_ids for rule in pipeline.AGNOSTIC_FAMILY_RULES
            )
        )
        self.assertEqual(pipeline._verify_agnostic_release(), [])

    def test_seed_mapping_prefers_identifiers_then_title_author(self) -> None:
        exact = {
            "id": "https://openalex.org/W1",
            "title": "Generic title",
            "authors": ["Different Author"],
            "publication_year": 2020,
        }
        by_oa = {"https://openalex.org/W1": [exact]}
        status, candidates = pipeline._map_seed_candidates(
            {
                "openalex_id": "https://openalex.org/W1",
                "doi": None,
                "title_normalized": "generic title",
                "authors": ["Seed Author"],
                "year": 2020,
            },
            by_oa,
            {},
            {"generic title": [exact]},
        )
        self.assertEqual(status, "resolved")
        self.assertEqual(candidates[0]["match_methods"], ["openalex_id"])

        right = {
            "id": "https://openalex.org/W2",
            "title": "Generic title",
            "authors": ["Ada Lovelace"],
            "publication_year": 2021,
        }
        wrong = {
            "id": "https://openalex.org/W3",
            "title": "Generic title",
            "authors": ["Emmy Noether"],
            "publication_year": 2021,
        }
        status, candidates = pipeline._map_seed_candidates(
            {
                "openalex_id": None,
                "doi": None,
                "title_normalized": "generic title",
                "authors": ["Ada Lovelace"],
                "year": 2021,
            },
            {},
            {},
            {"generic title": [wrong, right]},
        )
        self.assertEqual(status, "resolved")
        self.assertEqual(candidates[0]["openalex_id"], right["id"])
        self.assertEqual(candidates[0]["match_methods"], ["title_author_year"])

    def test_unresolved_title_candidates_remain_auditable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            pipeline._write_seed_mapping(
                [
                    {
                        "source_id": "seed",
                        "title": "The Riemann Hypothesis",
                        "title_normalized": "the riemann hypothesis",
                        "authors": ["Leonhard Euler"],
                        "openalex_id": None,
                        "doi": None,
                        "year": 2000,
                    }
                ],
                [
                    {
                        "id": "https://openalex.org/W9",
                        "doi": None,
                        "title": "The Riemann Hypothesis",
                        "authors": ["Carl Gauss"],
                        "publication_year": 2000,
                        "snapshot_object": "part",
                        "snapshot_object_etag": "etag",
                    }
                ],
                output,
            )
            mapping = pipeline.load_jsonl(output / "seed_mapping.jsonl")[0]
            self.assertEqual(mapping["status"], "unresolved")
            self.assertEqual(mapping["candidates"], [])
            self.assertEqual(
                mapping["unselected_title_evidence"][0]["openalex_id"],
                "https://openalex.org/W9",
            )

    def test_relevance_rules_accept_core_mechanisms(self) -> None:
        accepted = (
            "The Riemann hypothesis",
            "Zeros of the Riemann zeta function on the critical line",
            "A new lower bound for the de Bruijn-Newman constant",
            "The Nyman-Beurling criterion for the Riemann hypothesis",
            "Pair correlation of zeros of the zeta function",
        )
        for title in accepted:
            with self.subTest(title=title):
                result = pipeline.text_relevance(title)
                self.assertGreater(result["score"], 0)
                self.assertIsNone(result["exclusion"])

    def test_relevance_rules_preserve_known_false_positive_boundaries(self) -> None:
        rejected = (
            "The moduli space of Riemann surfaces",
            "The Riemann-Hilbert correspondence",
            "Riemann-Liouville fractional derivatives",
            "Convergence of the Riemann sum",
            "The Selberg zeta function on a compact Riemann surface",
        )
        for title in rejected:
            with self.subTest(title=title):
                result = pipeline.text_relevance(title)
                self.assertEqual(result["decision"], "rejected_false_positive")

    def test_extended_riemann_mechanism_titles_stay_anchored(self) -> None:
        accepted = (
            "Random Matrix Theory and the Riemann Zeta Function",
            "Computational Verification of Zeros of the Riemann Zeta Function",
            "Equivalent Criteria for the Riemann Hypothesis",
            "Quantum Chaos and Zeta Zeros",
        )
        for title in accepted:
            with self.subTest(title=title):
                self.assertIsNotNone(
                    re.search(pipeline.RIEMANN_MECHANISM_TITLE_PATTERN, title.lower())
                )
        rejected = (
            "Random Matrices in Wireless Communications",
            "A History of Riemann Surfaces",
            "Computational Spectral Geometry",
        )
        for title in rejected:
            with self.subTest(title=title):
                self.assertIsNone(
                    re.search(pipeline.RIEMANN_MECHANISM_TITLE_PATTERN, title.lower())
                )

    def test_candidate_url_order_prefers_direct_oa_pdf(self) -> None:
        record = {
            "best_oa_location": {"pdf_url": "https://example.org/a.pdf"},
            "open_access": {"oa_url": "https://repo.example/a"},
            "primary_location": {"pdf_url": "https://other.example/a.pdf"},
            "locations": [{"pdf_url": "https://example.org/a.pdf"}],
            "ids": {"arxiv": "https://arxiv.org/abs/2401.00001"},
        }
        self.assertEqual(
            pipeline.candidate_urls(record),
            [
                "https://example.org/a.pdf",
                "https://repo.example/a",
                "https://other.example/a.pdf",
                "https://arxiv.org/pdf/2401.00001",
            ],
        )

    def test_robots_access_boundaries_are_conservative(self) -> None:
        forbidden = SimpleNamespace(status_code=403, text="")
        with mock.patch("requests.get", return_value=forbidden):
            self.assertFalse(
                pipeline._robots_allowed(
                    "https://example.org/paper.pdf", "MathiaTest", {}
                )
            )
        missing = SimpleNamespace(status_code=404, text="")
        with mock.patch("requests.get", return_value=missing):
            self.assertTrue(
                pipeline._robots_allowed(
                    "https://example.org/paper.pdf", "MathiaTest", {}
                )
            )
        rate_limited = SimpleNamespace(status_code=429, text="")
        with mock.patch("requests.get", return_value=rate_limited):
            self.assertFalse(
                pipeline._robots_allowed(
                    "https://example.org/paper.pdf", "MathiaTest", {}
                )
            )

    def test_fulltext_redirect_rechecks_destination_robots_policy(self) -> None:
        class RedirectResponse:
            status_code = 302
            headers = {"Location": "https://other.example/paper.pdf"}
            url = "https://example.org/redirect"

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "paper.pdf"
            with (
                mock.patch.object(
                    pipeline, "_robots_allowed", side_effect=[True, False]
                ) as robots,
                mock.patch("requests.get", return_value=RedirectResponse()),
            ):
                with self.assertRaisesRegex(
                    pipeline.PipelineError, "robots_disallowed"
                ):
                    pipeline._download_url(
                        "https://example.org/redirect",
                        target,
                        user_agent="MathiaTest",
                        robots_cache={},
                    )
            self.assertEqual(robots.call_count, 2)
            self.assertFalse(target.exists())

    def test_partial_fulltext_download_is_removed_after_stream_failure(self) -> None:
        class BrokenResponse:
            status_code = 200
            headers = {"Content-Type": "application/pdf"}
            url = "https://example.org/paper.pdf"

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def iter_content(self, **_kwargs):
                yield b"partial bytes"
                raise OSError("stream failed")

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "paper.pdf"
            with (
                mock.patch.object(pipeline, "_robots_allowed", return_value=True),
                mock.patch("requests.get", return_value=BrokenResponse()),
            ):
                with self.assertRaises(OSError) as caught:
                    pipeline._download_url(
                        "https://example.org/paper.pdf",
                        target,
                        user_agent="MathiaTest",
                        robots_cache={},
                    )
            self.assertEqual(caught.exception.downloaded_bytes, len(b"partial bytes"))
            self.assertFalse(target.with_suffix(".pdf.part").exists())

    def test_agnostic_acquisition_uses_its_own_duplicate_groups(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            layout = pipeline.Layout.from_root(root, root / "openalex")
            layout.create()
            pipeline.write_jsonl(layout.agnostic / "seeds.jsonl", [])
            pipeline.write_json(
                layout.agnostic / "seed_summary.json",
                {
                    "release_id": "release",
                    "freeze_id": "freeze",
                    "freeze_sha256": "freeze-sha",
                    "coverage_map_id": "coverage",
                    "coverage_map_sha256": "coverage-sha",
                },
            )
            duplicates = layout.agnostic / "graph_v1" / "duplicate_groups.parquet"
            duplicates.parent.mkdir(parents=True)
            duplicates.touch()
            seen_queries = []

            def export_candidates(_duckdb, _parquet, path):
                pipeline.write_jsonl(path, [])

            def run(_command, *, input_text=None, **_kwargs):
                seen_queries.append(input_text)
                duplicate_json = (
                    layout.agnostic / "acquisition_v1" / "duplicate_groups.jsonl"
                )
                pipeline.write_jsonl(duplicate_json, [])
                return SimpleNamespace(returncode=0, stderr="", stdout="")

            with (
                mock.patch.object(
                    pipeline, "_export_candidates_json", side_effect=export_candidates
                ),
                mock.patch.object(pipeline, "_run", side_effect=run),
            ):
                result = pipeline.acquire_fulltext(
                    layout,
                    Path("/unused/duckdb"),
                    max_candidates=0,
                    max_successes=0,
                    stream="agnostic_mathia",
                )

            self.assertEqual(result["stream"], "agnostic_mathia")
            self.assertEqual(len(seen_queries), 1)
            self.assertIn(str(duplicates), seen_queries[0])

    def test_html_normalization_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "source.html"
            normalized = root / "source.txt"
            raw.write_text(
                "<html><script>bad()</script><h1>Riemann</h1><p>Mathematical text "
                + "with alphabetic content and structural mathematical explanation. "
                * 500
                + "</p></html>",
                encoding="utf-8",
            )
            result = pipeline.normalize_artifact(raw, normalized, "text/html")
            text = normalized.read_text()
            self.assertNotIn("bad()", text)
            self.assertIn("Riemann", text)
            self.assertGreater(result["quality"]["bytes"], 2000)

    def test_free_space_check_includes_temporary_requirement(self) -> None:
        layout = pipeline.Layout.from_root(Path("/mnt/fake"))
        evidence = {"available_bytes": 500, "free_bytes_floor": 200}
        with mock.patch.object(pipeline, "volume_evidence", return_value=evidence):
            self.assertEqual(pipeline.assert_free_space(layout, 100), evidence)
            with self.assertRaises(pipeline.PipelineError):
                pipeline.assert_free_space(layout, 301)

    def test_scan_state_migrates_legacy_network_accounting_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scan.sqlite3"
            connection = sqlite3.connect(path)
            connection.execute(
                """CREATE TABLE shards(
                object_key TEXT PRIMARY KEY,reduction_id TEXT,object_etag TEXT NOT NULL,
                input_bytes INTEGER NOT NULL,expected_records INTEGER NOT NULL,
                output_path TEXT,output_bytes INTEGER,output_sha256 TEXT,
                output_records INTEGER,network_bytes INTEGER NOT NULL DEFAULT 0,
                free_bytes_before INTEGER,peak_observed_used_bytes INTEGER,
                status TEXT NOT NULL,started_at TEXT,completed_at TEXT,error TEXT)"""
            )
            connection.execute(
                "INSERT INTO shards(object_key,reduction_id,object_etag,input_bytes,"
                "expected_records,network_bytes,status) VALUES "
                "('done','v3','a',100,1,100,'complete'),"
                "('interrupted','v3','b',200,1,0,'running')"
            )
            connection.commit()
            connection.close()
            migrated = pipeline._state_connection(path)
            self.assertEqual(
                migrated.execute("SELECT sum(bytes) FROM download_events").fetchone()[
                    0
                ],
                100,
            )
            self.assertEqual(
                migrated.execute(
                    "SELECT value FROM state_metadata WHERE "
                    "key='legacy_untracked_interrupted_upper_bound_bytes'"
                ).fetchone()[0],
                "200",
            )
            migrated.close()
            reopened = pipeline._state_connection(path)
            self.assertEqual(
                reopened.execute("SELECT count(*) FROM download_events").fetchone()[0],
                1,
            )
            reopened.close()

    def test_reduction_sql_uses_real_taxonomy_and_object_provenance(self) -> None:
        sql = pipeline.shard_reduction_sql(
            Path("/mnt/openalex/openalex/tmp/part.parquet"),
            Path("/mnt/openalex/openalex/reduced/works_parts/part_0001.parquet"),
            {"snapshot_date": "2026-06-26"},
            {"key": "data/parquet/works/test.parquet", "etag": "abc123"},
            ["https://openalex.org/W1"],
            ["10.1/example"],
            ["the riemann hypothesis"],
        )
        self.assertIn("primary_topic.field.display_name = 'Mathematics'", sql)
        self.assertIn("regexp_matches(title_norm", sql)
        self.assertIn("data/parquet/works/test.parquet", sql)
        self.assertIn("abc123", sql)
        self.assertIn("/mnt/openalex/openalex/tmp/duckdb_spill", sql)
        self.assertIn("seed_oa_match OR seed_doi_match AS seed_match", sql)
        self.assertIn("WHEN seed_title_match THEN 'seed_title_candidate'", sql)
        self.assertIn("FROM classified", sql)

    def test_handoff_verifier_detects_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "raw.pdf"
            normalized = root / "normalized.txt"
            raw.write_bytes(b"%PDF-test")
            normalized.write_text("usable text")
            manifest = root / "manifest.jsonl"
            row = {
                "source_id": "test",
                "raw_path": str(raw),
                "raw_sha256": pipeline.sha256_file(raw),
                "normalized_path": str(normalized),
                "normalized_sha256": pipeline.sha256_file(normalized),
            }
            manifest.write_text(json.dumps(row) + "\n")
            freeze = {
                "files": [
                    {
                        "path": "manifest.jsonl",
                        "bytes": manifest.stat().st_size,
                        "sha256": pipeline.sha256_file(manifest),
                    }
                ]
            }
            (root / "freeze.json").write_text(json.dumps(freeze))
            self.assertEqual(pipeline.verify_handoff(root), [])
            normalized.write_text("tampered")
            self.assertTrue(pipeline.verify_handoff(root))

    def test_handoff_freeze_is_atomically_published_with_final_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            layout = pipeline.Layout.from_root(root, root / "openalex")
            layout.create()
            acquisition = layout.riemann / "acquisition_v1"
            raw = acquisition / "raw" / "w1.pdf"
            normalized = acquisition / "normalized" / "w1.txt"
            raw.parent.mkdir(parents=True)
            normalized.parent.mkdir(parents=True)
            raw.write_bytes(b"%PDF-test artifact")
            normalized.write_text("usable normalized mathematical text")
            pipeline.write_jsonl(
                acquisition / "acquired.jsonl",
                [
                    {
                        "source_id": "test",
                        "raw_path": str(raw),
                        "raw_sha256": pipeline.sha256_file(raw),
                        "normalized_path": str(normalized),
                        "normalized_sha256": pipeline.sha256_file(normalized),
                    }
                ],
            )

            frozen = pipeline.freeze_handoff(layout, "test_v1")
            target = layout.handoffs / "test_v1"
            manifest_row = pipeline.load_jsonl(target / "manifest.jsonl")[0]
            self.assertEqual(frozen["source_count"], 1)
            self.assertTrue(target.is_dir())
            self.assertFalse((layout.handoffs / ".test_v1.partial").exists())
            self.assertTrue(manifest_row["raw_path"].startswith(str(target)))
            self.assertEqual(pipeline.verify_handoff(target), [])

            for path in target.rglob("*"):
                os.chmod(path, 0o755 if path.is_dir() else 0o644)
            os.chmod(target, 0o755)


if __name__ == "__main__":
    unittest.main()
