import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from experiments import execution_provenance
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


def _write_unresolved_acquisition_state(root: Path) -> dict:
    rows = [
        {
            "source_id": "unresolved_test_source",
            "lineage": "v1-relevant",
            "v1_usable": False,
            "final_status": "alternate-version-search-pending",
            "alternate_work_search_status": None,
            "candidates": [
                {
                    "candidate_id": "unresolved_test_candidate",
                    "route": "synthetic-test",
                    "route_rank": 0,
                    "url": "https://example.test/unresolved.pdf",
                    "host": "example.test",
                }
            ],
            "attempts": [],
        }
    ]
    full_corpus_v2.write_jsonl(root / "acquisition_search.jsonl", rows)
    state = full_corpus_v2._build_acquisition_retry_state(
        rows, full_corpus_v2.DEFAULT_MAX_ROUTE_ATTEMPTS
    )
    full_corpus_v2.write_json(root / "acquisition_retry_state.json", state)
    return state


def _write_minimal_frozen_release(root: Path, decision: str) -> None:
    identity = {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": full_corpus_v2.V2_RELEASE_ID,
        "parent_release_id": full_corpus_v2.V1_RELEASE_ID,
        "parent_freeze_id": full_corpus_v2.V1_FREEZE_ID,
        "final_decision": decision,
        "files": [],
    }
    freeze_id = "riemann_mathia_v2_" + full_corpus_v2.sha256_text(
        full_corpus_v2.canonical_json(identity)
    )
    full_corpus_v2.write_json(
        root / "freeze.json",
        {**identity, "freeze_id": freeze_id, "frozen_at": "2026-08-21T00:00:00+00:00"},
    )
    (root / "REPORT.md").write_text(decision + "\n", encoding="utf-8")
    full_corpus_v2.write_jsonl(root / "objects.jsonl", [])
    manifest_identity = {"freeze_id": freeze_id, "files": []}
    full_corpus_v2.write_json(
        root / "release_manifest.json",
        {
            **manifest_identity,
            "manifest_id": "riemann_mathia_v2_manifest_"
            + full_corpus_v2.sha256_text(full_corpus_v2.canonical_json(manifest_identity)),
        },
    )


def _synthetic_execution_row(
    release_root: Path,
    assignment_path: Path,
    output_path: Path,
    *,
    ledger_id: str,
    stage: str,
    task_path: str,
    status: str,
    requires_rerun: bool,
) -> dict:
    row = execution_provenance.base_execution_row()
    row.update(
        {
            "schema_version": 1,
            "ledger_kind": "synthetic-test-execution",
            "ledger_id": ledger_id,
            "release_id": full_corpus_v2.V2_RELEASE_ID,
            "stage": stage,
            "status": status,
            "requires_rerun": requires_rerun,
            "rerun_reason": "synthetic-isolation" if requires_rerun else None,
            "assignment_relpath": full_corpus_v2._execution_ledger_relpath(
                release_root, assignment_path
            ),
            "assignment_sha256": full_corpus_v2.sha256_file(assignment_path),
            "prompt_recovery_status": "encrypted-local-only",
            "agent_task_path": task_path,
            "output_relpath": full_corpus_v2._execution_ledger_relpath(
                release_root, output_path
            ),
            "output_sha256": full_corpus_v2.sha256_file(output_path),
            "output_records": len(full_corpus_v2.load_jsonl(output_path)),
            "recovery_quality": "synthetic-exact",
        }
    )
    execution_provenance.validate_execution_rows([row])
    return row


class RiemannCorpusV2Tests(unittest.TestCase):
    def test_audit_reuses_only_exact_pre_openalex_object_decisions(self) -> None:
        self.assertEqual(full_corpus_v2.validate_source_isolation_archive(), [])
        archived_audit_root = (
            full_corpus_v2.ISOLATION_ARCHIVE_ROOT
            / "reconciliation/artifacts/audit"
        )
        archived_objects_path = (
            full_corpus_v2.ISOLATION_ARCHIVE_ROOT
            / "non_authoritative/artifacts/objects.jsonl"
        )
        sample = full_corpus_v2.load_jsonl(archived_audit_root / "sample.jsonl")
        carried = full_corpus_v2.load_jsonl(
            archived_audit_root / "carried_pre_openalex.jsonl"
        )
        prior_reviews = full_corpus_v2.load_jsonl(
            full_corpus_v2.PRE_OPENALEX_AUDIT_FINAL_PATH
        )
        prior_sample = full_corpus_v2.load_jsonl(
            full_corpus_v2.PRE_OPENALEX_AUDIT_SAMPLE_PATH
        )
        current_ids = {
            row["object_id"]
            for row in full_corpus_v2.load_jsonl(archived_objects_path)
        }
        sample_ids = [row["object_id"] for row in sample]
        carried_ids = [row["object_id"] for row in carried]
        self.assertTrue(carried_ids)
        self.assertEqual(
            carried,
            full_corpus_v2.exact_audit_carry(sample, prior_sample, prior_reviews),
        )
        self.assertTrue(set(carried_ids).issubset(current_ids))

        assigned_ids = []
        for path in sorted((archived_audit_root / "assignments").glob("*.json")):
            assignment = full_corpus_v2.load_json(path)
            assigned_ids.extend(row["object_id"] for row in assignment["items"])
        self.assertFalse(set(carried_ids) & set(assigned_ids))
        self.assertEqual(set(sample_ids), set(carried_ids) | set(assigned_ids))

        changed = [dict(row) for row in sample]
        carried_id = carried_ids[0]
        changed_item = next(row for row in changed if row["object_id"] == carried_id)
        changed_item["proposed_content"] += " changed"
        self.assertNotIn(
            carried_id,
            {
                row["object_id"]
                for row in full_corpus_v2.exact_audit_carry(
                    changed, prior_sample, prior_reviews
                )
            },
        )

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

    def test_ready_freeze_rejects_open_acquisition_frontier(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _write_unresolved_acquisition_state(root)
            open_frontier = {
                "axis": "acquisition",
                "round_id": "open-test-round",
                "frontier_status": "open",
                "attempts": 0,
                "recovered_sources": 0,
                "marginal_yield": 0.0,
                "routes": {},
                "outcomes": {"no-unattempted-lawful-candidates": 1},
            }
            full_corpus_v2.write_json(root / "acquisition_frontier.json", open_frontier)
            full_corpus_v2.write_jsonl(root / "saturation_log.jsonl", [open_frontier])
            with mock.patch.multiple(
                full_corpus_v2,
                ACQUISITION_SEARCH_PATH=root / "acquisition_search.jsonl",
                ACQUISITION_RETRY_STATE_PATH=root / "acquisition_retry_state.json",
                ACQUISITION_FRONTIER_PATH=root / "acquisition_frontier.json",
                SATURATION_LOG_PATH=root / "saturation_log.jsonl",
            ), mock.patch.object(
                full_corpus_v2, "validate_execution_ledger_receipts", return_value=[]
            ), mock.patch.object(
                full_corpus_v2, "validate_exact_audit_carry", return_value=[]
            ):
                with self.assertRaisesRegex(ValueError, "unresolved source dispositions"):
                    full_corpus_v2.freeze_release("RIEMANN_MATHIA_CORPUS_V2_READY")

    def test_ready_freeze_accepts_terminal_acquisition_frontier(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rows = [
                {
                    "source_id": "terminal_test_source",
                    "lineage": "v1-relevant",
                    "v1_usable": False,
                    "final_status": "lawful-routes-exhausted-after-persistent-policy",
                    "alternate_work_search_status": "searched",
                    "candidates": [
                        {
                            "candidate_id": "terminal_test_candidate",
                            "route": "synthetic-test",
                            "route_rank": 0,
                            "url": "https://example.test/terminal.pdf",
                            "host": "example.test",
                        }
                    ],
                    "attempts": [
                        {
                            "attempt_id": "terminal_test_attempt",
                            "candidate_id": "terminal_test_candidate",
                            "round_id": "terminal-route-round",
                            "route": "synthetic-test",
                            "requested_url": "https://example.test/terminal.pdf",
                            "host": "example.test",
                            "attempted_at": "2026-08-20T00:00:00+00:00",
                            "result": "blocked-http-404",
                            "status_class": "terminal-for-route",
                        }
                    ],
                }
            ]
            full_corpus_v2.write_jsonl(root / "acquisition_search.jsonl", rows)
            with mock.patch.multiple(
                full_corpus_v2,
                V2_ROOT=root,
                FREEZE_PATH=root / "freeze.json",
                RELEASE_MANIFEST_PATH=root / "release_manifest.json",
                ACQUISITION_SEARCH_PATH=root / "acquisition_search.jsonl",
                ACQUISITION_RETRY_STATE_PATH=root / "acquisition_retry_state.json",
                ACQUISITION_FRONTIER_PATH=root / "acquisition_frontier.json",
                SATURATION_LOG_PATH=root / "saturation_log.jsonl",
            ), mock.patch.object(
                full_corpus_v2, "validate_openalex_handoff_state", return_value=[]
            ), mock.patch.object(
                full_corpus_v2, "validate_execution_ledger_receipts", return_value=[]
            ), mock.patch.object(
                full_corpus_v2, "validate_exact_audit_carry", return_value=[]
            ):
                full_corpus_v2.record_acquisition_frontier("terminal-frontier-round")
                full_corpus_v2.freeze_release("RIEMANN_MATHIA_CORPUS_V2_READY")
                self.assertEqual(
                    full_corpus_v2.load_json(root / "freeze.json")["final_decision"],
                    "RIEMANN_MATHIA_CORPUS_V2_READY",
                )

    def test_ready_frozen_validation_rejects_absent_acquisition_frontier(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _write_unresolved_acquisition_state(root)
            _write_minimal_frozen_release(root, "RIEMANN_MATHIA_CORPUS_V2_READY")
            errors = self._validate_minimal_frozen_release(root)
            self.assertIn(
                "READY requires a terminal acquisition_frontier.json record", errors
            )

    def test_nonready_frozen_validation_accepts_unresolved_acquisition(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _write_unresolved_acquisition_state(root)
            _write_minimal_frozen_release(root, "MORE_ACQUISITION_NEEDED")
            self.assertEqual(self._validate_minimal_frozen_release(root), [])

    def _validate_minimal_frozen_release(self, root: Path) -> list[str]:
        with mock.patch.multiple(
            full_corpus_v2,
            V2_ROOT=root,
            FREEZE_PATH=root / "freeze.json",
            RELEASE_MANIFEST_PATH=root / "release_manifest.json",
            OBJECTS_PATH=root / "objects.jsonl",
            ACQUISITION_SEARCH_PATH=root / "acquisition_search.jsonl",
            ACQUISITION_RETRY_STATE_PATH=root / "acquisition_retry_state.json",
            ACQUISITION_FRONTIER_PATH=root / "acquisition_frontier.json",
            SATURATION_LOG_PATH=root / "saturation_log.jsonl",
        ), mock.patch.object(
            full_corpus_v2, "validate_acquisition", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_depth_plans", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_depth_units", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_execution_context", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_execution_ledger_receipts", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_exact_audit_carry", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_openalex_handoff_state", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_analysis", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_within_source_synthesis", return_value=[]
        ), mock.patch.object(
            full_corpus_v2, "validate_mixed_manifest_status", return_value=[]
        ), mock.patch.object(interchange, "validate_release", return_value=[]):
            return full_corpus_v2.validate_frozen_release(root)

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
        self.assertEqual(
            full_corpus_v2.validate_depth_plans(require_complete=False), []
        )
        assignments = sorted(full_corpus_v2.DEPTH_ASSIGNMENT_ROOT.glob("*.json"))
        self.assertTrue(assignments)
        self.assertTrue(
            all(
                len(full_corpus_v2.load_json(path).get("sources") or []) == 1
                for path in assignments
            )
        )
        self.assertEqual(full_corpus_v2.validate_source_isolation_archive(), [])
        archived_rows = full_corpus_v2._archive_manifest_rows(
            full_corpus_v2.ISOLATION_ARCHIVE_MANIFEST_PATH
        )
        self.assertTrue(
            any(row.get("category") == "mixed-depth-assignment" for row in archived_rows)
        )
        self.assertTrue(
            any(row.get("category") == "mixed-depth-output" for row in archived_rows)
        )

    def test_source_isolation_prepare_preserves_ledgers_and_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "release"
            depth_assignment_path = root / "depth/assignments/batch_01.json"
            depth_output_path = root / "depth/plans/batch_01.jsonl"
            depth_assignment = full_corpus_v2._bind_model_visible_packet(
                {
                    "stage": "whole-source-depth",
                    "sources": [{"source_id": "s1"}, {"source_id": "s2"}],
                    "output_path": str(depth_output_path),
                }
            )
            full_corpus_v2.write_json(depth_assignment_path, depth_assignment)
            full_corpus_v2.write_jsonl(
                depth_output_path,
                [{"source_id": "s1"}, {"source_id": "s2"}],
            )
            full_corpus_v2.write_jsonl(
                root / "depth/units.jsonl",
                [
                    {"unit_id": "u1", "source_id": "s1"},
                    {"unit_id": "u2", "source_id": "s2"},
                ],
            )

            audit_assignment_path = root / "audit/assignments/audit_01.json"
            audit_output_path = root / "audit/batches/audit_01.jsonl"
            audit_assignment = full_corpus_v2._bind_model_visible_packet(
                {
                    "stage": "audit",
                    "items": [{"object_id": "o1", "source_id": "s1"}],
                    "output_path": str(audit_output_path),
                }
            )
            full_corpus_v2.write_json(audit_assignment_path, audit_assignment)
            full_corpus_v2.write_jsonl(audit_output_path, [{"object_id": "o1"}])
            legacy_row = _synthetic_execution_row(
                root,
                depth_assignment_path,
                depth_output_path,
                ledger_id="legacy_synthetic",
                stage="whole-source-depth",
                task_path="/root/synthetic-mixed-depth",
                status="isolation-invalid",
                requires_rerun=True,
            )
            audit_row = _synthetic_execution_row(
                root,
                audit_assignment_path,
                audit_output_path,
                ledger_id="audit_synthetic",
                stage="audit",
                task_path="/root/synthetic-audit",
                status="authoritative",
                requires_rerun=False,
            )
            full_corpus_v2.write_jsonl(
                root / "execution/legacy_context_recovery.jsonl", [legacy_row]
            )
            full_corpus_v2.write_jsonl(
                root / "execution/ai_execution_ledger.jsonl", [audit_row]
            )
            full_corpus_v2.write_jsonl(
                root / "audit/decision_execution_map.jsonl",
                [
                    {
                        "schema_version": 1,
                        "ledger_kind": "riemann-audit-decision-map",
                        "release_id": full_corpus_v2.V2_RELEASE_ID,
                        "object_id": "o1",
                        "state": "active-fresh",
                        "execution_ledger_id": "audit_synthetic",
                        "assignment_sha256": audit_row["assignment_sha256"],
                        "output_sha256": audit_row["output_sha256"],
                        "decision_canonical_sha256": "0" * 64,
                    }
                ],
            )
            full_corpus_v2.write_json(root / "freeze.json", {"candidate": "old"})

            first = full_corpus_v2.prepare_source_isolation_rerun(root)
            summary_path = (
                root
                / full_corpus_v2.ISOLATION_ARCHIVE_ROOT.name
                / "summary.json"
            )
            interrupted = dict(first)
            interrupted["status"] = "in_progress"
            full_corpus_v2.write_json(summary_path, interrupted)
            resumed = full_corpus_v2.prepare_source_isolation_rerun(root)
            second = full_corpus_v2.prepare_source_isolation_rerun(root)
            self.assertEqual(resumed, second)
            self.assertEqual(first, second)
            self.assertEqual(first["status"], "complete")
            self.assertTrue(first["prior_candidate_freeze_preserved"])
            self.assertEqual(
                full_corpus_v2.validate_source_isolation_archive(
                    root, root / full_corpus_v2.ISOLATION_ARCHIVE_ROOT.name
                ),
                [],
            )
            restated_audit = full_corpus_v2.load_jsonl(
                root / "execution/ai_execution_ledger.jsonl"
            )
            self.assertEqual(restated_audit[0]["status"], "reconciliation-pending")
            self.assertEqual(
                full_corpus_v2.load_jsonl(
                    root / "audit/decision_execution_map.jsonl"
                )[0]["state"],
                "reconciliation-pending",
            )

    def test_corrective_isolation_archives_only_reused_legacy_contexts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "release"
            specifications = (
                ("pass12", "keep", "/root/keep-teacher"),
                ("pass3", "keep", "/root/keep-critic"),
                ("pass4", "keep", "/root/keep-reviser"),
                ("pass12", "source_a", "/root/reused-teacher-critic"),
                ("pass12", "source_b", "/root/reused-teacher-critic"),
                ("pass3", "source_a", "/root/reused-teacher-critic"),
                ("pass3", "source_c", "/root/reused-reviser"),
                ("pass4", "source_c", "/root/reused-reviser"),
            )
            ledger_rows = []
            provenance_rows = []
            for index, (stage, source_id, task_path) in enumerate(specifications):
                assignment_path = (
                    root / "analyses/assignments" / f"{stage}_{index:02d}.json"
                )
                output_path = (
                    root / "analyses/batches" / f"{stage}_{index:02d}.jsonl"
                )
                assignment = full_corpus_v2._bind_model_visible_packet(
                    {
                        "stage": stage,
                        "units": [
                            {"unit_id": f"{source_id}_{stage}", "source_id": source_id}
                        ],
                        "output_path": str(output_path),
                    }
                )
                full_corpus_v2.write_json(assignment_path, assignment)
                full_corpus_v2.write_jsonl(
                    output_path, [{"unit_id": f"{source_id}_{stage}"}]
                )
                ledger_rows.append(
                    _synthetic_execution_row(
                        root,
                        assignment_path,
                        output_path,
                        ledger_id=f"corrective_{index}",
                        stage=stage,
                        task_path=task_path,
                        status="historical-recovered",
                        requires_rerun=False,
                    )
                )
                provenance_rows.append(
                    {
                        "assignment_relpath": assignment_path.relative_to(root).as_posix(),
                        "assignment_sha256": full_corpus_v2.sha256_file(assignment_path),
                        "agent_task_path": task_path,
                        "stage": stage,
                    }
                )
            full_corpus_v2.write_jsonl(
                root / "execution/legacy_context_recovery.jsonl", ledger_rows
            )
            full_corpus_v2.write_jsonl(
                root / "execution/ai_execution_ledger.jsonl", []
            )
            full_corpus_v2.write_jsonl(
                root / "analyses/generation_provenance.jsonl", provenance_rows
            )

            discovery = full_corpus_v2.discover_reused_legacy_analysis_contexts(root)
            self.assertEqual(discovery["affected_context_count"], 5)
            self.assertEqual(len(discovery["retained_assignment_relpaths"]), 3)
            self.assertEqual(
                discovery["teacher_critic_collision_paths"],
                ["/root/reused-teacher-critic"],
            )

            archive = root / full_corpus_v2.CORRECTIVE_ISOLATION_ARCHIVE_ROOT.name
            in_progress = {
                **discovery,
                "phase": "riemann-source-isolation-correction-v2",
                "status": "in_progress",
                "reason": "synthetic interruption",
                "authoritative": False,
                "trainable": False,
            }
            full_corpus_v2._write_json_atomic(archive / "summary.json", in_progress)
            first_affected = root / discovery["affected_assignment_relpaths"][0]
            first_output = Path(
                full_corpus_v2.load_json(first_affected)["output_path"]
            )
            for path, category in (
                (first_output, "reused-legacy-analysis-output"),
                (first_affected, "reused-legacy-analysis-assignment"),
            ):
                full_corpus_v2._archive_file_for_isolation(
                    root,
                    archive,
                    path,
                    pool="non_authoritative",
                    category=category,
                    reason="synthetic interrupted correction",
                )

            first = full_corpus_v2.prepare_corrective_source_isolation_rerun(root)
            self.assertEqual(first["status"], "complete")
            self.assertEqual(first["affected_context_count"], 5)
            self.assertEqual(first["archived_file_count"], 12)
            self.assertEqual(
                full_corpus_v2.validate_source_isolation_archive(root, archive), []
            )
            self.assertTrue(
                all(
                    row["authoritative"] is False and row["trainable"] is False
                    for row in full_corpus_v2.load_jsonl(archive / "manifest.jsonl")
                )
            )
            self.assertEqual(
                full_corpus_v2.validate_execution_ledger_receipts(root), []
            )
            self.assertTrue(
                all(
                    not (root / relative).exists()
                    for relative in discovery["affected_assignment_relpaths"]
                )
            )
            self.assertTrue(
                all(
                    (root / relative).is_file()
                    for relative in discovery["retained_assignment_relpaths"]
                )
            )
            self.assertEqual(
                len(
                    full_corpus_v2.load_jsonl(
                        root / "analyses/generation_provenance.jsonl"
                    )
                ),
                3,
            )
            restated = full_corpus_v2.load_jsonl(
                root / "execution/legacy_context_recovery.jsonl"
            )
            self.assertEqual(
                Counter(row["status"] for row in restated),
                Counter({"isolation-invalid": 5, "historical-recovered": 3}),
            )
            self.assertTrue(
                all(
                    row["requires_rerun"]
                    for row in restated
                    if row["status"] == "isolation-invalid"
                )
            )

            pending_assignment = full_corpus_v2._bind_model_visible_packet(
                {
                    "stage": "pass12",
                    "units": [{"unit_id": "fresh", "source_id": "fresh_source"}],
                    "output_path": str(root / "analyses/batches/fresh.jsonl"),
                }
            )
            full_corpus_v2.write_json(
                root / "analyses/assignments/fresh.json", pending_assignment
            )
            self.assertEqual(
                full_corpus_v2.validate_execution_ledger_receipts(
                    root, allow_fresh_pending=True
                ),
                [],
            )
            self.assertTrue(full_corpus_v2.validate_execution_ledger_receipts(root))
            second = full_corpus_v2.prepare_corrective_source_isolation_rerun(root)
            self.assertEqual(first, second)
            self.assertEqual(
                first["manifest_sha256"],
                full_corpus_v2.sha256_file(archive / "manifest.jsonl"),
            )

    def test_corrective_isolation_has_a_distinct_cli_phase(self) -> None:
        summary = {"status": "complete", "phase": "synthetic"}
        with mock.patch.object(
            full_corpus_v2,
            "prepare_corrective_source_isolation_rerun",
            return_value=summary,
        ) as prepare, mock.patch("builtins.print") as output:
            self.assertEqual(
                full_corpus_v2.main(["prepare-source-isolation-correction-v2"]),
                0,
            )
        prepare.assert_called_once_with()
        output.assert_called_once_with(json.dumps(summary, sort_keys=True))

    def test_all_release_enumerations_exclude_both_isolation_archives(self) -> None:
        self.assertTrue(
            full_corpus_v2._is_source_isolation_archive_path(
                full_corpus_v2.ISOLATION_ARCHIVE_ROOT / "manifest.jsonl"
            )
        )
        self.assertTrue(
            full_corpus_v2._is_source_isolation_archive_path(
                full_corpus_v2.CORRECTIVE_ISOLATION_ARCHIVE_ROOT / "manifest.jsonl"
            )
        )
        self.assertFalse(
            full_corpus_v2._is_source_isolation_archive_path(
                full_corpus_v2.V2_ROOT / "execution/ai_execution_ledger.jsonl"
            )
        )

    def test_selective_reconciliation_requires_an_exact_packet_and_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "release"
            archive = root / "non_authoritative_source_isolation_run"
            assignment_path = root / "analyses/assignments/pass3_source.json"
            output_path = root / "analyses/batches/pass3_source.jsonl"
            assignment = full_corpus_v2._bind_model_visible_packet(
                {
                    "stage": "pass3",
                    "source_id": "s1",
                    "units": [{"unit_id": "u1", "source_id": "s1"}],
                    "output_path": str(output_path),
                }
            )
            full_corpus_v2.write_json(assignment_path, assignment)
            full_corpus_v2.write_jsonl(output_path, [{"unit_id": "u1"}])
            receipt = {
                "stage": "pass3",
                "agent_task_path": "/root/synthetic-source-critic",
                "assignment_sha256": full_corpus_v2.sha256_file(assignment_path),
                "raw_output_sha256": full_corpus_v2.sha256_file(output_path),
                "model_visible_packet_sha256": full_corpus_v2.model_visible_packet_sha256(
                    assignment
                ),
            }
            full_corpus_v2._archive_file_for_isolation(
                root,
                archive,
                output_path,
                pool="reconciliation",
                category="test-output",
                reason="synthetic test",
                reconciliation_eligible=True,
            )
            full_corpus_v2._archive_file_for_isolation(
                root,
                archive,
                assignment_path,
                pool="reconciliation",
                category="test-assignment",
                reason="synthetic test",
                reconciliation_eligible=True,
            )
            full_corpus_v2.write_json(assignment_path, assignment)
            self.assertTrue(
                full_corpus_v2.reconcile_archived_assignment(
                    assignment_path, root, archive, receipt
                )
            )
            output_path.unlink()
            changed = dict(assignment)
            changed["units"] = [{"unit_id": "u1", "source_id": "s1", "changed": True}]
            changed = full_corpus_v2._bind_model_visible_packet(changed)
            full_corpus_v2.write_json(assignment_path, changed)
            self.assertFalse(
                full_corpus_v2.reconcile_archived_assignment(
                    assignment_path, root, archive, receipt
                )
            )

    def test_execution_receipts_enforce_unique_disjoint_paths_and_explicit_panels(self) -> None:
        generation = full_corpus_v2._bind_model_visible_packet(
            {
                "stage": "pass12",
                "units": [{"unit_id": "u1", "source_id": "s1"}],
            }
        )
        critic = full_corpus_v2._bind_model_visible_packet(
            {
                "stage": "pass3",
                "units": [{"unit_id": "u1", "source_id": "s1"}],
            }
        )
        reused_path = "/root/reused-teacher-critic"
        errors = full_corpus_v2.validate_execution_receipts(
            [
                (
                    "generation",
                    generation,
                    {
                        "stage": "pass12",
                        "agent_task_path": reused_path,
                        "model_visible_packet_sha256": full_corpus_v2.model_visible_packet_sha256(generation),
                    },
                ),
                (
                    "critic",
                    critic,
                    {
                        "stage": "pass3",
                        "agent_task_path": reused_path,
                        "model_visible_packet_sha256": full_corpus_v2.model_visible_packet_sha256(critic),
                    },
                ),
            ]
        )
        self.assertTrue(any("task path reused" in error for error in errors))
        self.assertTrue(any("teacher/critic" in error for error in errors))

        panel = full_corpus_v2._bind_model_visible_packet(
            {
                "stage": "cross-source-audit",
                "items": [
                    {"source_id": "s1", "object_id": "o1"},
                    {"source_id": "s2", "object_id": "o2"},
                ],
            }
        )
        self.assertEqual(
            full_corpus_v2.validate_execution_receipts(
                [
                    (
                        "panel",
                        panel,
                        {
                            "stage": "cross-source-audit",
                            "agent_task_path": "/root/explicit-cross-panel",
                            "model_visible_packet_sha256": full_corpus_v2.model_visible_packet_sha256(panel),
                        },
                    )
                ],
                cross_source_stages={"cross-source-audit"},
            ),
            [],
        )

    def test_execution_context_is_compact_bound_and_non_authoritative(self) -> None:
        self.assertEqual(full_corpus_v2.validate_execution_context(), [])
        self.assertEqual(full_corpus_v2.validate_source_isolation_archive(), [])
        summary = full_corpus_v2.load_json(full_corpus_v2.ISOLATION_ARCHIVE_SUMMARY_PATH)
        self.assertFalse(summary["authoritative"])
        self.assertFalse(summary["trainable"])
        archived_execution_root = (
            full_corpus_v2.ISOLATION_ARCHIVE_ROOT
            / "non_authoritative/artifacts/execution"
        )
        dossiers_path = archived_execution_root / "source_dossiers.jsonl"
        dossiers = full_corpus_v2.load_jsonl(dossiers_path)
        inventory = full_corpus_v2.load_jsonl(full_corpus_v2.DEPTH_INVENTORY_PATH)
        self.assertEqual(
            [row["source_id"] for row in dossiers],
            [row["source_id"] for row in inventory],
        )
        self.assertTrue(
            all(row["cache_role"] == "non-authoritative-execution-cache" for row in dossiers)
        )
        manifest = full_corpus_v2.load_json(archived_execution_root / "manifest.json")
        for key, path in (
            ("source_dossiers", dossiers_path),
            ("efficiency_metrics", archived_execution_root / "efficiency_metrics.json"),
        ):
            descriptor = manifest[key]
            self.assertEqual(full_corpus_v2.sha256_file(path), descriptor["sha256"])
            self.assertEqual(path.stat().st_size, descriptor["bytes"])
        archived_brief = archived_execution_root / "RUN_BRIEF.md"
        archived_brief_descriptor = manifest["run_brief"]
        self.assertEqual(
            full_corpus_v2.sha256_file(archived_brief),
            archived_brief_descriptor["sha256"],
        )
        self.assertEqual(archived_brief.stat().st_size, archived_brief_descriptor["bytes"])
        brief = full_corpus_v2.EXECUTION_BRIEF_PATH.read_text(encoding="utf-8")
        self.assertIn(
            "Consumed issue #46 Riemann handoff IDs: **riemann_fulltext_v2**",
            brief,
        )
        self.assertIn(
            "Consumed issue #46 agnostic Mathia handoff IDs: **agnostic_mathia_fulltext_v2**",
            brief,
        )
        self.assertIn("Do not read the full issue history", brief)

    def test_dual_openalex_state_binds_merged_agnostic_parent(self) -> None:
        self.assertEqual(full_corpus_v2.validate_openalex_handoff_state(False), [])
        self.assertIn(
            "#46 handoff processing is incomplete despite the frozen cutoff",
            full_corpus_v2.validate_openalex_handoff_state(True),
        )
        state = full_corpus_v2.load_json(full_corpus_v2.OPENALEX_HANDOFF_STATE_PATH)
        self.assertEqual(set(state["streams"]), {"riemann", "agnostic_mathia"})
        self.assertEqual(state["network_requests_performed_by_42_for_handoffs"], 0)
        self.assertEqual(state["processing_cutoff"]["status"], "frozen")
        self.assertFalse(state["finalization_allowed"])
        self.assertEqual(
            {
                row["handoff_id"]
                for stream in state["streams"].values()
                for row in stream["consumed"]
            },
            {"riemann_fulltext_v2", "agnostic_mathia_fulltext_v2"},
        )
        self.assertEqual(
            {
                row["handoff_id"]
                for stream in state["streams"].values()
                for row in stream["superseded"]
            },
            {"riemann_fulltext_v1", "agnostic_mathia_fulltext_v1"},
        )
        parent = full_corpus_v2.load_json(
            full_corpus_v2.AGNOSTIC_SUPPLEMENT_PARENT_PATH
        )
        self.assertEqual(parent["parent_release_id"], "agnostic-mathia-full-v1")
        self.assertEqual(parent["parent_freeze_id"], full_corpus_v2.AGNOSTIC_V1_FREEZE_ID)
        self.assertEqual(
            parent["parent_review_content_freeze_id"],
            full_corpus_v2.AGNOSTIC_V1_REVIEW_CONTENT_FREEZE_ID,
        )
        self.assertEqual(parent["contract_version"], "mathia-interchange-v1")
        concrete = parent["concrete_artifact_binding"]
        self.assertEqual(
            concrete["controlling_comment"],
            full_corpus_v2.ISSUE42_CONCRETE_ARTIFACT_BINDING_COMMENT,
        )
        self.assertEqual(concrete["handoff_id"], "agnostic_mathia_fulltext_v2")
        self.assertEqual(
            concrete["handoff_freeze_id"],
            full_corpus_v2.OPENALEX_HANDOFF_SPECS[
                "agnostic_mathia_fulltext_v2"
            ]["freeze_id"],
        )
        self.assertEqual(
            concrete["handoff_manifest_sha256"],
            full_corpus_v2.AGNOSTIC_HANDOFF_V2_MANIFEST_SHA256,
        )
        self.assertEqual(
            state["concrete_artifact_binding"],
            concrete,
        )
        self.assertEqual(
            {row["path"] for row in parent["bindings"]},
            {
                path.relative_to(full_corpus_v2.REPO_ROOT).as_posix()
                for path in full_corpus_v2.AGNOSTIC_V1_BINDING_PATHS
            },
        )
        self.assertEqual(
            {row["path"] for row in concrete["repo_evidence"]},
            {
                path.relative_to(full_corpus_v2.REPO_ROOT).as_posix()
                for path in full_corpus_v2.AGNOSTIC_HANDOFF_V2_REPO_EVIDENCE_PATHS
            },
        )

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

    def test_superseding_handoff_carries_decisions_only_for_identical_bytes(self) -> None:
        hashes = {
            "raw_sha256": "a" * 64,
            "raw_bytes": 10,
            "normalized_sha256": "b" * 64,
            "normalized_bytes": 9,
        }
        prior = {"rows": [{"source_id": "source-1", **hashes}]}
        authoritative = {"rows": [{"source_id": "source-1", **hashes}]}
        ledger = [
            {
                "canonical_source_id": "canonical-1",
                "handoff_source_id": "source-1",
                "disposition": "accepted_for_riemann_v2_processing",
                "reason": "frozen prior decision",
                "identity_keys": ["openalex:source-1"],
                "matched_source_ids": [],
                **hashes,
            }
        ]
        carried = full_corpus_v2._superseding_handoff_classifications(
            prior, authoritative, ledger
        )
        self.assertEqual(
            carried["source-1"]["disposition"],
            "accepted_for_riemann_v2_processing",
        )
        authoritative["rows"][0]["normalized_sha256"] = "c" * 64
        with self.assertRaisesRegex(ValueError, "changed source bytes"):
            full_corpus_v2._superseding_handoff_classifications(
                prior, authoritative, ledger
            )

    def test_route_corrected_handoffs_bind_nine_versions_and_affected_licenses(self) -> None:
        self.assertEqual(full_corpus_v2.validate_source_isolation_archive(), [])
        archived_objects_path = (
            full_corpus_v2.ISOLATION_ARCHIVE_ROOT
            / "non_authoritative/artifacts/objects.jsonl"
        )
        riemann = {
            row["handoff_source_id"]: row
            for row in full_corpus_v2.load_jsonl(
                full_corpus_v2.RIEMANN_HANDOFF_SOURCE_LEDGER_PATH
            )
        }
        agnostic = {
            row["handoff_source_id"]: row
            for row in full_corpus_v2.load_jsonl(
                full_corpus_v2.AGNOSTIC_HANDOFF_SOURCE_LEDGER_PATH
            )
        }
        corrected_riemann = {
            "openalex_riemann_w2141932395",
            "openalex_riemann_w2237579816",
            "openalex_riemann_w2278237719",
            "openalex_w1647755162",
            "openalex_w2042837137",
        }
        corrected_agnostic = {
            "openalex_agnostic_mathia_w1968388660",
            "openalex_agnostic_mathia_w2020332468",
            "openalex_agnostic_mathia_w2090467627",
            "openalex_agnostic_mathia_w3098455240",
        }
        self.assertEqual(
            {riemann[source_id]["source_version"] for source_id in corrected_riemann},
            {"submittedVersion"},
        )
        self.assertEqual(
            {agnostic[source_id]["source_version"] for source_id in corrected_agnostic},
            {"submittedVersion"},
        )
        self.assertIsNone(riemann["openalex_riemann_w2141932395"]["license"])
        self.assertIsNone(
            agnostic["openalex_agnostic_mathia_w3098455240"]["license"]
        )
        self.assertEqual({row["handoff_id"] for row in riemann.values()}, {"riemann_fulltext_v2"})
        self.assertEqual(
            {row["handoff_id"] for row in agnostic.values()},
            {"agnostic_mathia_fulltext_v2"},
        )

        riemann_objects = [
            row
            for row in full_corpus_v2.load_jsonl(archived_objects_path)
            if row.get("object_role") == "source"
            and row.get("source_ids") == ["openalex_w2141932395"]
        ]
        self.assertEqual(len(riemann_objects), 29)
        self.assertTrue(
            all("reported license=None" in row["licensing_boundary"] for row in riemann_objects)
        )
        self.assertEqual(
            {
                row["corpus_local_audit"]["issue_46_handoff_provenance"]["handoff_id"]
                for row in riemann_objects
            },
            {"riemann_fulltext_v2"},
        )
        unaffected = next(
            row
            for row in full_corpus_v2.load_jsonl(archived_objects_path)
            if row.get("source_unit_ids") == ["aim2004_resource_v2u01"]
        )
        self.assertEqual(
            unaffected["object_id"],
            "mathia_source_80d75f2dba6b8580218769b106ad683d7093c91e48791245787f81a7731abe71",
        )
        self.assertNotIn(
            "issue_46_handoff_provenance", unaffected["corpus_local_audit"]
        )
        self.assertEqual(
            unaffected["licensing_boundary"],
            "source text external-local-not-git; reported access boundary: no "
            "redistribution grant located; metadata and derived teacher interpretation "
            "are repository-retained",
        )

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
        self.assertEqual(full_corpus_v2.validate_source_isolation_archive(), [])
        assignments = sorted(
            (
                full_corpus_v2.ISOLATION_ARCHIVE_ROOT
                / "reconciliation/artifacts/audit/assignments"
            ).glob("*.json")
        )
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
