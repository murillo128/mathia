import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from experiments.mathia_corpus import interchange
from experiments.riemann_corpus import full_corpus_v2


ROOT = Path(__file__).resolve().parents[1]


def _write_synthetic_handoff(
    parent: Path,
    handoff_id: str,
    stream: str,
    source_count: int = 1,
    work_id_start: int = 100,
) -> Path:
    bundle = parent / handoff_id
    (bundle / "raw").mkdir(parents=True)
    (bundle / "normalized").mkdir()
    rows = []
    for offset in range(source_count):
        work_id = work_id_start + offset
        raw = bundle / "raw" / f"w{work_id}.pdf"
        normalized = bundle / "normalized" / f"w{work_id}.txt"
        raw.write_bytes(f"%PDF synthetic {work_id}\n".encode())
        normalized.write_text(f"Synthetic mathematical source {work_id}.\n", encoding="utf-8")
        rows.append(
            {
                "access_boundary": "publicly accessible; redistribution rights not inferred",
                "acquisition_route": "synthetic-test",
                "authors": ["Test Author"],
                "candidate_public_locations": [],
                "doi": f"10.0000/{work_id}",
                "duplicate_relationships": [],
                "effective_url": f"https://example.test/{work_id}.pdf",
                "handoff_version": handoff_id,
                "ids": {"openalex": f"https://openalex.org/W{work_id}"},
                "license": None,
                "normalization": {
                    "media_type": "application/pdf",
                    "warnings": ["synthetic fixture"],
                },
                "normalized_bytes": normalized.stat().st_size,
                "normalized_lines": 1,
                "normalized_path": str(normalized),
                "normalized_sha256": full_corpus_v2.sha256_file(normalized),
                "open_access": {"is_oa": True},
                "openalex_id": f"https://openalex.org/W{work_id}",
                "priority": 1.0,
                "raw_bytes": raw.stat().st_size,
                "raw_path": str(raw),
                "raw_sha256": full_corpus_v2.sha256_file(raw),
                "relevance": {"mechanism_tags": ["synthetic"]},
                "snapshot": {"date": "2026-08-20"},
                "source_id": (
                    f"openalex_riemann_w{work_id}"
                    if stream == "riemann"
                    else f"openalex_agnostic_mathia_w{work_id}"
                ),
                "source_version": "publishedVersion",
                "title": f"Synthetic source {work_id}",
                "type": "article",
                "year": 2026,
            }
        )
    manifest = bundle / "manifest.jsonl"
    full_corpus_v2.write_jsonl(manifest, rows)
    files = []
    for path in [manifest, *sorted((bundle / "normalized").iterdir()), *sorted((bundle / "raw").iterdir())]:
        files.append(
            {
                "path": path.relative_to(bundle).as_posix(),
                "sha256": full_corpus_v2.sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )
    full_corpus_v2.write_json(
        bundle / "freeze.json",
        {
            "consumer_contract": "synthetic offline consumer contract",
            "files": files,
            "freeze_id": full_corpus_v2.OPENALEX_HANDOFF_SPECS[handoff_id][
                "freeze_id"
            ],
            "frozen_at": "2026-08-20T00:00:00+00:00",
            "handoff_version": handoff_id,
            "immutable": True,
            "manifest_sha256": full_corpus_v2.sha256_file(manifest),
            "pipeline_version": "openalex-offline-discovery-v1",
            "source_count": source_count,
            "stream": stream,
        },
    )
    return bundle


class RiemannCorpusV2Tests(unittest.TestCase):
    def test_audit_reuses_only_exact_pre_openalex_object_decisions(self) -> None:
        sample = full_corpus_v2.load_jsonl(full_corpus_v2.AUDIT_SAMPLE_PATH)
        carried = full_corpus_v2.load_jsonl(full_corpus_v2.AUDIT_CARRIED_PATH)
        prior = {
            row["object_id"]: row
            for row in full_corpus_v2.load_jsonl(
                full_corpus_v2.PRE_OPENALEX_AUDIT_FINAL_PATH
            )
        }
        current_ids = {
            row["object_id"] for row in full_corpus_v2.load_jsonl(full_corpus_v2.OBJECTS_PATH)
        }
        sample_ids = [row["object_id"] for row in sample]
        carried_ids = [row["object_id"] for row in carried]
        self.assertTrue(carried_ids)
        self.assertEqual(
            carried,
            [prior[object_id] for object_id in sample_ids if object_id in prior],
        )
        self.assertTrue(set(carried_ids).issubset(current_ids))

        assigned_ids = []
        for path in sorted(full_corpus_v2.AUDIT_ASSIGNMENT_ROOT.glob("*.json")):
            assignment = full_corpus_v2.load_json(path)
            assigned_ids.extend(row["object_id"] for row in assignment["items"])
        self.assertFalse(set(carried_ids) & set(assigned_ids))
        self.assertEqual(set(sample_ids), set(carried_ids) | set(assigned_ids))

    def test_openalex_handoff_sources_have_explicit_cross_panel_routing(self) -> None:
        routed = [
            source_id
            for source_ids in full_corpus_v2.CROSS_PANEL_SOURCE_OVERRIDES.values()
            for source_id in source_ids
        ]
        self.assertEqual(len(routed), 15)
        self.assertEqual(len(routed), len(set(routed)))
        self.assertTrue(all(source_id.startswith("openalex_w") for source_id in routed))
        self.assertTrue(
            set(full_corpus_v2.CROSS_PANEL_SOURCE_OVERRIDES).issubset(
                full_corpus_v2.CROSS_PANELS
            )
        )

    def test_v2_reuses_canonical_interchange(self) -> None:
        self.assertIs(full_corpus_v2.interchange, interchange)
        self.assertEqual(interchange.CONTRACT_VERSION, "mathia-interchange-v1")

    def test_v2_parent_is_exact_immutable_v1(self) -> None:
        parent = json.loads(full_corpus_v2.PARENT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(parent["parent_release_id"], "riemann-mathia-full-v1")
        self.assertEqual(parent["parent_freeze_id"], full_corpus_v2.V1_FREEZE_ID)
        self.assertEqual(
            parent["v1_counts"],
            {
                "relevant_inventory_records": 393,
                "usable_sources": 86,
                "sources_needing_usable_full_text": 307,
                "semantic_units": 274,
                "objects": 568,
            },
        )
        for binding in parent["bindings"]:
            path = full_corpus_v2.HERE / binding["path"]
            self.assertEqual(path.stat().st_size, binding["bytes"])
            self.assertEqual(full_corpus_v2.sha256_file(path), binding["sha256"])

    def test_v2_acquisition_overlay_validates_without_external_artifacts(self) -> None:
        self.assertEqual(
            full_corpus_v2.validate_acquisition(full_corpus_v2.DEFAULT_ARTIFACT_ROOT, False),
            [],
        )

    def test_v2_acquisition_expands_breadth_and_preserves_marginal_yield(self) -> None:
        summary = json.loads(full_corpus_v2.ACQUISITION_SUMMARY_PATH.read_text(encoding="utf-8"))
        self.assertEqual(summary["updated_relevant_inventory_records"], 423)
        self.assertGreaterEqual(summary["formerly_unusable_recovered"], 41)
        self.assertGreaterEqual(summary["total_usable_sources_after_round"], 143)
        self.assertGreaterEqual(summary["curated_long_form_sources"], 17)
        saturation = [
            entry
            for entry in full_corpus_v2.load_jsonl(full_corpus_v2.SATURATION_LOG_PATH)
            if entry.get("axis") == "acquisition"
        ]
        self.assertTrue(saturation)
        self.assertTrue(
            all(
                {"attempts", "recovered_sources", "marginal_yield", "outcomes", "routes"}
                <= set(entry)
                for entry in saturation
            )
        )
        retry_state = json.loads(
            full_corpus_v2.ACQUISITION_RETRY_STATE_PATH.read_text(encoding="utf-8")
        )
        self.assertEqual(
            retry_state["state_version"], "riemann-v2-acquisition-retry-state-v1"
        )
        self.assertEqual(retry_state["policy"]["host_concurrency"], 1)
        self.assertFalse(retry_state["policy"]["global_sleep"])
        unresolved = {
            source_id: source["disposition"]
            for source_id, source in retry_state["sources"].items()
            if source["disposition"] not in {"usable", "lawful-routes-exhausted"}
        }
        if full_corpus_v2.ACQUISITION_FRONTIER_PATH.is_file():
            self.assertFalse(unresolved)
            frontier = json.loads(
                full_corpus_v2.ACQUISITION_FRONTIER_PATH.read_text(encoding="utf-8")
            )
            self.assertEqual(frontier["attempts"], 0)
            self.assertEqual(frontier["marginal_yield"], 0.0)
            self.assertEqual(
                frontier["outcomes"], {"no-unattempted-lawful-candidates": 1}
            )
        else:
            self.assertTrue(unresolved)

    def test_v2_acquisition_retry_classes_are_explicit(self) -> None:
        self.assertEqual(
            full_corpus_v2._outcome_status_class("blocked-http-429"),
            "temporary-retryable",
        )
        self.assertEqual(
            full_corpus_v2._outcome_status_class("blocked-http-403"),
            "route-specific-failure",
        )
        self.assertEqual(
            full_corpus_v2._outcome_status_class("blocked-http-404"),
            "terminal-for-route",
        )
        self.assertEqual(
            full_corpus_v2._outcome_status_class("acquired-and-normalized"), "success"
        )

    def test_v2_alternate_match_rejects_a_later_sequel(self) -> None:
        row = {
            "title": "On the zeros of the Riemann zeta function in the critical strip",
            "authors": ["Richard P. Brent"],
            "year": 1979,
        }
        sequel = {
            "id": "https://openalex.org/W2116781013",
            "display_name": "On the zeros of the Riemann zeta function in the critical strip. II",
            "publication_year": 1982,
            "authorships": [
                {"author": {"display_name": "Richard P. Brent"}},
                {"author": {"display_name": "J. van de Lune"}},
            ],
        }
        self.assertIsNone(full_corpus_v2._alternate_work_match(row, sequel))

    def test_lehmer_paper_identity_routes_are_distinct(self) -> None:
        curated = {
            row["source_id"]: row
            for row in json.loads(
                full_corpus_v2.V2_CURATED_PATH.read_text(encoding="utf-8")
            )
        }
        short_note = curated["openalex_w1224069186"]
        long_paper = curated["openalex_w2080252578"]
        self.assertIn("pp104-111.pdf", short_note["acquisition_url"])
        self.assertIn("paper_206.pdf", long_paper["acquisition_url"])
        self.assertNotEqual(short_note["authors"], long_paper["authors"])
        self.assertIn("1993 ETNA", long_paper["known_difference"])
        quarantine = json.loads(
            full_corpus_v2.V2_ACQUISITION_QUARANTINE_PATH.read_text(
                encoding="utf-8"
            )
        )
        finding = next(
            row
            for row in quarantine
            if row["source_id"] == "openalex_w1224069186"
        )
        self.assertIn(
            "v2_candidate_486500ee7daff94e6fd70a603e7d538cc67ec6624166be389175c3fa0e8cd51d",
            finding["candidate_ids"],
        )

    def test_orphaned_raw_analysis_is_preserved_before_deactivation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            batches = root / "batches"
            batches.mkdir()
            output = batches / "pass12_batch_01.jsonl"
            records = [
                {"unit_id": "stale", "spontaneous": {}, "directed": {}},
                {"unit_id": "live", "spontaneous": {}, "directed": {}},
            ]
            full_corpus_v2.write_jsonl(output, records)
            quarantine = root / "identity_quarantine.jsonl"
            with (
                mock.patch.object(full_corpus_v2, "HERE", root),
                mock.patch.object(full_corpus_v2, "ANALYSIS_BATCH_ROOT", batches),
                mock.patch.object(
                    full_corpus_v2, "ANALYSIS_IDENTITY_QUARANTINE_PATH", quarantine
                ),
            ):
                full_corpus_v2._quarantine_orphaned_raw_analysis({"live"})
            self.assertEqual(
                [row["unit_id"] for row in full_corpus_v2.load_jsonl(output)],
                ["live"],
            )
            preserved = full_corpus_v2.load_jsonl(quarantine)
            self.assertEqual(len(preserved), 1)
            self.assertEqual(preserved[0]["unit_id"], "stale")
            self.assertEqual(preserved[0]["original_record_index"], 0)
            self.assertEqual(preserved[0]["record"], records[0])

    def test_completed_depth_plans_are_exactly_valid(self) -> None:
        self.assertEqual(full_corpus_v2.validate_depth_plans(require_complete=False), [])

    def test_execution_context_is_compact_bound_and_non_authoritative(self) -> None:
        self.assertEqual(full_corpus_v2.validate_execution_context(), [])
        dossiers = full_corpus_v2.load_jsonl(full_corpus_v2.SOURCE_DOSSIERS_PATH)
        inventory = full_corpus_v2.load_jsonl(full_corpus_v2.DEPTH_INVENTORY_PATH)
        self.assertEqual(
            [row["source_id"] for row in dossiers],
            [row["source_id"] for row in inventory],
        )
        self.assertTrue(
            all(row["cache_role"] == "non-authoritative-execution-cache" for row in dossiers)
        )
        brief = full_corpus_v2.EXECUTION_BRIEF_PATH.read_text(encoding="utf-8")
        self.assertIn(
            "Consumed issue #46 Riemann handoff IDs: **riemann_fulltext_v1**",
            brief,
        )
        self.assertIn(
            "Consumed issue #46 agnostic Mathia handoff IDs: **agnostic_mathia_fulltext_v1**",
            brief,
        )
        self.assertIn("Do not read the full issue history", brief)

    def test_dual_openalex_state_binds_merged_agnostic_parent(self) -> None:
        self.assertEqual(full_corpus_v2.validate_openalex_handoff_state(False), [])
        self.assertEqual(full_corpus_v2.validate_openalex_handoff_state(True), [])
        state = full_corpus_v2.load_json(full_corpus_v2.OPENALEX_HANDOFF_STATE_PATH)
        self.assertEqual(set(state["streams"]), {"riemann", "agnostic_mathia"})
        self.assertEqual(state["network_requests_performed_by_42_for_handoffs"], 0)
        self.assertEqual(state["processing_cutoff"]["status"], "frozen")
        self.assertTrue(state["finalization_allowed"])
        self.assertTrue(
            all(
                row["processing_status"] == "complete"
                for stream in state["streams"].values()
                for row in stream["consumed"]
            )
        )
        parent = full_corpus_v2.load_json(
            full_corpus_v2.AGNOSTIC_SUPPLEMENT_PARENT_PATH
        )
        self.assertEqual(parent["parent_release_id"], "agnostic-mathia-full-v1")
        self.assertEqual(parent["parent_freeze_id"], full_corpus_v2.AGNOSTIC_V1_FREEZE_ID)
        self.assertEqual(parent["contract_version"], "mathia-interchange-v1")

    def test_dual_openalex_cutoff_rejects_duplicate_dispositions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            artifact_root = root / "artifacts"
            artifact_root.mkdir()
            manifest_path = root / "manifest.json"
            manifest_path.write_text("{}\n", encoding="utf-8")
            state = full_corpus_v2.load_json(
                full_corpus_v2.OPENALEX_HANDOFF_STATE_PATH
            )
            state["processing_cutoff"] = {
                "status": "frozen",
                "cutoff_id": "cutoff-test",
                "published_handoff_ids_through_cutoff": ["riemann_fulltext_v1"],
                "observed_issue_46_through": "test",
            }
            state["finalization_allowed"] = True
            state["streams"]["riemann"]["consumed"] = [
                {
                    "handoff_id": "riemann_fulltext_v1",
                    "handoff_version": 1,
                    "manifest_path": str(manifest_path),
                    "manifest_sha256": full_corpus_v2.sha256_file(manifest_path),
                    "local_artifact_root": str(artifact_root),
                    "processing_cutoff": "cutoff-test",
                }
            ]
            state["streams"]["riemann"][
                "deduplicated_or_already_represented"
            ] = [{"handoff_id": "riemann_fulltext_v1", "reason": "duplicate"}]
            state_path = root / "handoff-state.json"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            with mock.patch.object(
                full_corpus_v2, "OPENALEX_HANDOFF_STATE_PATH", state_path
            ):
                self.assertIn(
                    "not every #46 handoff through the cutoff has exactly one disposition",
                    full_corpus_v2.validate_openalex_handoff_state(True),
                )

    def test_verified_handoff_copy_is_idempotent_and_detects_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = _write_synthetic_handoff(
                root / "published", "riemann_fulltext_v1", "riemann"
            )
            retained_parent = root / "retained"
            first = full_corpus_v2._copy_verified_handoff(
                source, retained_parent, "riemann_fulltext_v1", "riemann"
            )
            second = full_corpus_v2._copy_verified_handoff(
                source, retained_parent, "riemann_fulltext_v1", "riemann"
            )
            self.assertEqual(first["freeze_sha256"], second["freeze_sha256"])
            self.assertEqual(second["root"], retained_parent / "riemann_fulltext_v1")
            self.assertFalse(
                any(path.name.startswith(".riemann_fulltext_v1.staging-") for path in retained_parent.iterdir())
            )
            retained_text = second["root"] / "normalized" / "w100.txt"
            retained_text.write_text("drift\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "frozen file drift"):
                full_corpus_v2._copy_verified_handoff(
                    source, retained_parent, "riemann_fulltext_v1", "riemann"
                )

    def test_handoff_validation_rejects_unsafe_paths_and_extra_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bundle = _write_synthetic_handoff(
                root, "riemann_fulltext_v1", "riemann"
            )
            freeze = full_corpus_v2.load_json(bundle / "freeze.json")
            freeze["files"].append(
                {"path": "../escape", "sha256": "0" * 64, "bytes": 0}
            )
            full_corpus_v2.write_json(bundle / "freeze.json", freeze)
            with self.assertRaisesRegex(ValueError, "unsafe handoff-relative path"):
                full_corpus_v2._validate_openalex_handoff_bundle(
                    bundle, "riemann_fulltext_v1", "riemann"
                )
            bundle = _write_synthetic_handoff(
                root / "second", "agnostic_mathia_fulltext_v1", "agnostic_mathia"
            )
            (bundle / "undeclared.txt").write_text("extra\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "descriptor coverage"):
                full_corpus_v2._validate_openalex_handoff_bundle(
                    bundle, "agnostic_mathia_fulltext_v1", "agnostic_mathia"
                )

    def test_handoff_source_classification_uses_canonical_work_ids(self) -> None:
        handoff_row = {
            "source_id": "openalex_riemann_w123",
            "openalex_id": "https://openalex.org/W123",
            "doi": "10.0000/123",
            "normalized_sha256": "1" * 64,
        }
        existing = [
            {
                "source_id": "openalex_w123",
                "identifiers": {},
                "selected_artifact": {},
            }
        ]
        represented = full_corpus_v2._classify_handoff_source(
            handoff_row,
            existing,
            {"openalex_w123"},
            "accepted_for_riemann_v2_processing",
        )
        self.assertEqual(
            represented["disposition"], "deduplicated_or_already_represented"
        )
        recoverable = full_corpus_v2._classify_handoff_source(
            handoff_row,
            existing,
            set(),
            "accepted_for_riemann_v2_processing",
        )
        self.assertEqual(
            recoverable["disposition"], "accepted_for_riemann_v2_processing"
        )
        self.assertEqual(recoverable["canonical_source_id"], "openalex_w123")

    def test_handoff_source_classification_deduplicates_identical_raw_artifact(self) -> None:
        digest = "a" * 64
        handoff_row = {
            "source_id": "openalex_riemann_w456",
            "openalex_id": "https://openalex.org/W456",
            "doi": "10.48550/arxiv.1234.5678",
            "raw_sha256": digest,
            "normalized_sha256": "b" * 64,
        }
        existing = [
            {
                "source_id": "legacy_named_source",
                "identifiers": {"arxiv": "1234.5678"},
                "v1_artifact_sha256": digest,
                "selected_artifact": None,
            }
        ]
        classified = full_corpus_v2._classify_handoff_source(
            handoff_row,
            existing,
            {"legacy_named_source"},
            "accepted_for_riemann_v2_processing",
        )
        self.assertEqual(
            classified["disposition"], "deduplicated_or_already_represented"
        )
        self.assertEqual(classified["canonical_source_id"], "legacy_named_source")

    def test_riemann_handoff_adapter_routes_only_unrepresented_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            published = _write_synthetic_handoff(
                root / "published",
                "riemann_fulltext_v1",
                "riemann",
                source_count=3,
                work_id_start=100,
            )
            artifact_root = root / "artifacts"
            bundle = full_corpus_v2._copy_verified_handoff(
                published,
                artifact_root / "openalex_handoffs",
                "riemann_fulltext_v1",
                "riemann",
            )
            acquisition_path = root / "acquisition.jsonl"
            depth_path = root / "depth.jsonl"
            base_rows = []
            for work_id in (100, 101):
                base_rows.append(
                    {
                        "source_id": f"openalex_w{work_id}",
                        "lineage": "v1-relevant",
                        "title": f"Existing {work_id}",
                        "authors": [],
                        "year": 2020,
                        "source_type": "article",
                        "identifiers": {},
                        "canonical_url": None,
                        "viewpoint_tags": [],
                        "v1_acquisition_status": "not-attempted",
                        "v1_usable": False,
                        "v1_artifact_sha256": None,
                        "v1_normalized_sha256": None,
                        "search_priority": "recovery",
                        "openalex_refresh_status": "not-yet-refreshed",
                        "openalex_refreshed_at": None,
                        "candidates": [],
                        "attempts": [],
                        "final_status": "recovery-search-pending",
                        "selected_candidate_id": None,
                        "selected_artifact": None,
                        "remaining_search_notes": [],
                    }
                )
            full_corpus_v2.write_jsonl(acquisition_path, base_rows)
            full_corpus_v2.write_jsonl(depth_path, [{"source_id": "openalex_w100"}])
            ledger = full_corpus_v2._adapt_riemann_handoff_acquisition(
                bundle, artifact_root, acquisition_path, depth_path
            )
            self.assertEqual(
                dict(
                    sorted(
                        Counter(row["disposition"] for row in ledger).items()
                    )
                ),
                {
                    "accepted_for_riemann_v2_processing": 2,
                    "deduplicated_or_already_represented": 1,
                },
            )
            updated = {
                row["source_id"]: row for row in full_corpus_v2.load_jsonl(acquisition_path)
            }
            self.assertEqual(set(updated), {"openalex_w100", "openalex_w101", "openalex_w102"})
            self.assertEqual(updated["openalex_w100"]["attempts"], [])
            for source_id in ("openalex_w101", "openalex_w102"):
                self.assertEqual(updated[source_id]["final_status"], "recovered-usable-in-v2")
                self.assertIs(
                    updated[source_id]["attempts"][-1]["network_request_performed"],
                    False,
                )

    def test_explicit_cutoff_stays_blocked_until_processing_completes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            state_path = Path(temporary_directory) / "state.json"
            state = full_corpus_v2.load_json(
                full_corpus_v2.OPENALEX_HANDOFF_STATE_PATH
            )
            for handoff_id, spec in full_corpus_v2.OPENALEX_HANDOFF_SPECS.items():
                state["streams"][spec["stream"]]["consumed"] = [
                    {
                        "handoff_id": handoff_id,
                        "stream": spec["stream"],
                        "freeze_id": spec["freeze_id"],
                        "freeze_sha256": "1" * 64,
                        "manifest_sha256": "2" * 64,
                        "processing_status": "copied_pending_analysis",
                    }
                ]
            full_corpus_v2.write_json(state_path, state)
            with mock.patch.object(
                full_corpus_v2, "OPENALEX_HANDOFF_STATE_PATH", state_path
            ):
                with self.assertRaisesRegex(ValueError, "exactly the authorized IDs"):
                    full_corpus_v2.freeze_openalex_handoff_cutoff(
                        ["riemann_fulltext_v1"], "https://example.test/issue-46"
                    )
                first = full_corpus_v2.freeze_openalex_handoff_cutoff(
                    list(full_corpus_v2.OPENALEX_HANDOFF_SPECS),
                    "https://example.test/issue-46",
                )
                second = full_corpus_v2.freeze_openalex_handoff_cutoff(
                    reversed(list(full_corpus_v2.OPENALEX_HANDOFF_SPECS)),
                    "https://example.test/issue-46",
                )
                self.assertEqual(first, second)
                frozen = full_corpus_v2.load_json(state_path)
                self.assertFalse(frozen["finalization_allowed"])
                self.assertFalse(full_corpus_v2._openalex_finalization_allowed(frozen))
                for stream in frozen["streams"].values():
                    for row in stream["consumed"]:
                        row["processing_status"] = "complete"
                self.assertTrue(full_corpus_v2._openalex_finalization_allowed(frozen))

    def test_new_analysis_packets_are_bounded_to_one_source(self) -> None:
        assignments = sorted(
            full_corpus_v2.ANALYSIS_ASSIGNMENT_ROOT.glob("pass*_source_*.json")
        )
        self.assertTrue(assignments)
        for path in assignments:
            assignment = full_corpus_v2.load_json(path)
            self.assertGreaterEqual(assignment["unit_count"], 1)
            self.assertLessEqual(
                assignment["unit_count"], full_corpus_v2.SOURCE_CONTEXT_MAX_UNITS
            )
            self.assertEqual(
                {row["source_id"] for row in assignment["units"]},
                {assignment["source_id"]},
            )
            assignment_brief_path = Path(assignment["execution_brief_path"])
            self.assertTrue(assignment_brief_path.is_file())
            self.assertEqual(
                assignment["execution_brief_sha256"],
                full_corpus_v2.sha256_file(assignment_brief_path),
            )
            for unit in assignment["units"]:
                self.assertIn("source_dossier_fragment", unit)
                self.assertIn("nearby_context", unit)
                for side in ("before", "after"):
                    packet = unit["nearby_context"][side]
                    self.assertEqual(
                        packet["sha256"], full_corpus_v2.sha256_text(packet["text"])
                    )

    def test_compromised_critic_is_preserved_outside_live_coverage(self) -> None:
        findings = full_corpus_v2.load_jsonl(
            full_corpus_v2.ANALYSIS_CONTEXT_QUARANTINE_PATH
        )
        finding = next(
            row
            for row in findings
            if row["quarantine_key"]
            == "pass3:batch_39:accidental-unrelated-v1-critic-context"
        )
        archived = full_corpus_v2.V2_ROOT / finding["archived_output_relpath"]
        self.assertTrue(archived.is_file())
        self.assertFalse(finding["trainable"])
        self.assertEqual(full_corpus_v2.sha256_file(archived), finding["original_output_sha256"])
        self.assertFalse(
            (
                full_corpus_v2.ANALYSIS_BATCH_ROOT / "pass3_batch_39.jsonl"
            ).exists()
        )

    def test_non_revision_critic_has_deterministic_final_mapping(self) -> None:
        candidate = {
            "directed": {
                "source_grounded_mathematics": "Exact mechanism.",
                "conceptual_reading": "Conceptual interpretation.",
                "representation_or_bridge": "Representation change.",
                "boundary_or_failure": "Bounded failure.",
                "uncertainty": "No formula reconstruction.",
            }
        }
        critic = {
            "critic_decision": "accept_as_is",
            "supported": ["Supported."],
            "inference": ["Inference labeled."],
            "unsupported_or_imported": [],
            "paraphrase_or_style_risk": [],
            "context_or_ocr_risk": [],
        }
        record = full_corpus_v2._deterministic_final_record("u", candidate, critic)
        self.assertEqual(record["decision"], "accepted")
        self.assertEqual(record["interpretation"], "Conceptual interpretation.")
        self.assertIn("Supported.", record["quality_reason"])

    def test_even_selection_handles_a_single_requested_sample(self) -> None:
        values = [{"value": value} for value in range(5)]
        self.assertEqual(full_corpus_v2._evenly_select(values, 1), [{"value": 2}])

    def test_selected_artifact_warnings_allow_a_null_artifact(self) -> None:
        self.assertEqual(
            full_corpus_v2._selected_artifact_warnings({"selected_artifact": None}),
            [],
        )
        self.assertEqual(
            full_corpus_v2._selected_artifact_warnings(
                {"selected_artifact": {"warnings": ["ocr"]}}
            ),
            ["ocr"],
        )

    def test_independent_audit_assignments_bind_exact_parent_artifacts(self) -> None:
        assignments = sorted(full_corpus_v2.AUDIT_ASSIGNMENT_ROOT.glob("*.json"))
        self.assertTrue(assignments)
        for path in assignments:
            assignment = full_corpus_v2.load_json(path)
            for item in assignment["items"]:
                for parent in item["parent_sources"]:
                    artifact = Path(parent["content_abspath"])
                    self.assertEqual(artifact.stat().st_size, parent["artifact_bytes"])
                    self.assertEqual(
                        full_corpus_v2.sha256_file(artifact), parent["artifact_sha256"]
                    )
                    visible = interchange.normalize_visible_text(
                        artifact.read_text(encoding="utf-8")
                    )
                    self.assertEqual(
                        interchange.sha256_text(visible), parent["content_sha256"]
                    )

    def test_v1_release_tree_is_not_nested_under_v2(self) -> None:
        self.assertFalse((full_corpus_v2.V2_ROOT / "full_corpus_v1").exists())
        self.assertTrue((ROOT / "experiments/riemann_corpus/full_corpus_v1/freeze.json").is_file())


if __name__ == "__main__":
    unittest.main()
