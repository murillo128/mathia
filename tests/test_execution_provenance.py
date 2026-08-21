import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory

from experiments import execution_provenance as provenance


class ExecutionProvenanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = provenance.jsonl_rows(provenance.RIEMANN_AUDIT_LEDGER)
        cls.decisions = provenance.jsonl_rows(provenance.RIEMANN_DECISION_MAP)
        cls.legacy = provenance.jsonl_rows(provenance.LEGACY_CONTEXT_LEDGER)
        cls.agnostic = provenance.jsonl_rows(provenance.AGNOSTIC_EXECUTION_LEDGER)

    def _write_recovery_fixture(
        self,
        root: Path,
        *,
        include_prompt_bindings: bool,
        duplicate_write: bool = False,
    ) -> tuple[Path, Path, Path, str]:
        fixture = root / "fixture"
        sessions = root / "sessions"
        fixture.mkdir(parents=True)
        sessions.mkdir()
        output = fixture / "output.jsonl"
        output.write_text('{"ok":true}\n', encoding="utf-8")
        assignment = {
            "stage": "generation",
            "output_path": str(output),
        }
        if include_prompt_bindings:
            prompt = fixture / "prompt.md"
            brief = fixture / "brief.md"
            prompt.write_text("fixture prompt body\n", encoding="utf-8")
            brief.write_text("fixture brief body\n", encoding="utf-8")
            assignment.update(
                {
                    "prompt_path": str(prompt),
                    "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
                    "execution_brief_path": str(brief),
                    "execution_brief_sha256": hashlib.sha256(
                        brief.read_bytes()
                    ).hexdigest(),
                }
            )
        assignment_path = fixture / "assignment.json"
        assignment_path.write_text(
            json.dumps(assignment, sort_keys=True) + "\n", encoding="utf-8"
        )
        ledger = fixture / "ledger.jsonl"
        ledger.write_text(
            json.dumps(self.agnostic[0], sort_keys=True) + "\n", encoding="utf-8"
        )
        task_path = "/root/fixture_unique_generation"
        thread_id = "00000000-0000-4000-8000-000000000101"
        turn_id = "00000000-0000-4000-8000-000000000102"
        metadata = {"turn_id": turn_id}
        events = [
            {
                "type": "session_meta",
                "payload": {
                    "id": thread_id,
                    "parent_thread_id": "00000000-0000-4000-8000-000000000103",
                    "agent_path": task_path,
                    "timestamp": "2026-08-21T12:00:00Z",
                    "cli_version": "0.149.0",
                    "originator": "codex-tui",
                    "model_provider": "openai",
                    "cwd": str(root),
                },
            },
            {
                "type": "turn_context",
                "payload": {
                    "turn_id": turn_id,
                    "model": "gpt-5.6-sol",
                    "effort": "xhigh",
                    "comp_hash": "3000",
                    "approval_policy": "never",
                    "sandbox_policy": {"type": "danger-full-access"},
                    "cwd": str(root),
                },
            },
            {
                "type": "response_item",
                "timestamp": "2026-08-21T12:00:01Z",
                "payload": {
                    "type": "agent_message",
                    "recipient": task_path,
                    "content": [
                        {
                            "type": "encrypted_content",
                            "encrypted_content": "fixture encrypted envelope",
                        }
                    ],
                    "internal_chat_message_metadata_passthrough": metadata,
                },
            },
            {
                "type": "response_item",
                "timestamp": "2026-08-21T12:00:02Z",
                "payload": {
                    "type": "custom_tool_call",
                    "call_id": "fixture-call-1",
                    "input": "*** Add File: fixture/output.jsonl\n+fixture",
                    "internal_chat_message_metadata_passthrough": metadata,
                },
            },
        ]
        if duplicate_write:
            events.append(
                {
                    "type": "response_item",
                    "timestamp": "2026-08-21T12:00:03Z",
                    "payload": {
                        "type": "custom_tool_call",
                        "call_id": "fixture-call-2",
                        "input": "*** Update File: fixture/output.jsonl\n+fixture",
                        "internal_chat_message_metadata_passthrough": metadata,
                    },
                }
            )
        (sessions / "rollout.jsonl").write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
            encoding="utf-8",
        )
        return assignment_path, ledger, sessions, task_path

    def test_exact_coverage_and_security_validation(self) -> None:
        summary = provenance.load_and_validate_existing()
        audit_fresh = sum(row["status"] == "authoritative" and row["stage"] == "active-fresh-audit" for row in self.audit)
        legacy_fresh = sum(row["status"] == "authoritative" for row in self.legacy)
        agnostic_fresh = sum(row["status"] == "authoritative" for row in self.agnostic)
        fresh_bindings = sum(
            row[field] is not None
            for row in self.audit + self.legacy + self.agnostic
            if row["status"] == "authoritative"
            and (
                row in self.legacy
                or row in self.agnostic
                or row["stage"] == "active-fresh-audit"
            )
            for field in (
                "assignment_sha256",
                "prompt_sha256",
                "execution_brief_sha256",
                "output_sha256",
            )
        )
        self.assertEqual(
            summary,
            {
                "agnostic_fresh_authoritative_rows": agnostic_fresh,
                "agnostic_requires_rerun": 102,
                "agnostic_rows": 102 + agnostic_fresh,
                "archived_artifact_bindings": 840,
                "legacy_fresh_authoritative_rows": legacy_fresh,
                "legacy_context_rows": 290 + legacy_fresh,
                "legacy_requires_rerun": 263,
                "live_artifact_bindings": 1027 + fresh_bindings,
                "riemann_audit_requires_rerun": 32,
                "riemann_audit_rows": 199 + audit_fresh,
                "riemann_decision_rows": 1864,
                "riemann_decisions_reconciliation_pending": 1004,
                "riemann_fresh_authoritative_rows": audit_fresh,
            },
        )

    def test_riemann_active_decisions_have_exact_execution_edges(self) -> None:
        states = Counter(row["state"] for row in self.decisions)
        self.assertEqual(
            states,
            Counter({"predecessor": 860, "reconciliation-pending": 1004}),
        )
        execution_ids = {row["ledger_id"] for row in self.audit}
        self.assertTrue(
            all(row["execution_ledger_id"] in execution_ids for row in self.decisions)
        )

    def test_agnostic_plaintext_prompt_gap_is_not_overclaimed(self) -> None:
        historical = [row for row in self.agnostic if row["status"] != "authoritative"]
        fresh = [row for row in self.agnostic if row["status"] == "authoritative"]
        self.assertEqual(
            Counter(row["stage"] for row in historical),
            Counter({"generation": 27, "critic": 27, "revision": 22, "audit": 26}),
        )
        self.assertTrue(fresh)
        self.assertTrue(
            {row["stage"] for row in fresh}.issubset(
                {"generation", "critic", "revision", "audit"}
            )
        )
        for row in self.agnostic:
            self.assertEqual(row["prompt_recovery_status"], "encrypted-local-only")
            self.assertIsNone(row["prompt_relpath"])
            self.assertIsNone(row["prompt_sha256"])
            self.assertIsNotNone(row["task_envelope_ciphertext_sha256"])
            self.assertIsNone(row["service_checkpoint_id"])
        generation = [
            row
            for row in self.agnostic
            if row["stage"] == "generation" and row["status"] == "isolation-invalid"
        ]
        self.assertEqual(len({row["thread_id"] for row in generation}), 2)
        self.assertEqual(len({row["turn_id"] for row in generation}), 27)
        self.assertTrue(
            all(
                row["requires_rerun"]
                for row in self.agnostic
                if row["status"] != "authoritative"
            )
        )
        self.assertTrue(
            all(
                row["requires_rerun"] is False
                for row in self.agnostic
                if row["status"] == "authoritative"
            )
        )
        self.assertEqual(
            Counter(row["status"] for row in self.agnostic),
            Counter(
                {
                    "isolation-invalid": 27,
                    "reconciliation-pending": 75,
                    "authoritative": len(fresh),
                }
            ),
        )

    def test_legacy_post_isolation_context_counts(self) -> None:
        mixed = Counter(
            row["stage"] for row in self.legacy if row["requires_rerun"]
        )
        self.assertEqual(
            mixed,
            Counter(
                {
                    "whole-source-depth": 37,
                    "missing-source-depth-repair": 3,
                    "pass12": 56,
                    "pass3": 58,
                    "pass4": 109,
                }
            ),
        )
        self.assertEqual(
            Counter(row["status"] for row in self.legacy),
            Counter(
                {
                    "historical-recovered": 27,
                    "isolation-invalid": 179,
                    "reconciliation-pending": 84,
                    "authoritative": sum(
                        row["status"] == "authoritative" for row in self.legacy
                    ),
                }
            ),
        )
        self.assertEqual(
            sum(row["recovery_quality"] == "path-and-hashes-only" for row in self.legacy),
            16,
        )

    def test_current_artifact_hashes(self) -> None:
        locations: Counter[str] = Counter()
        for row in self.audit + self.legacy + self.agnostic:
            bindings = (
                ("assignment_relpath", "assignment_sha256"),
                ("prompt_relpath", "prompt_sha256"),
                ("execution_brief_relpath", "execution_brief_sha256"),
                ("output_relpath", "output_sha256"),
            )
            for path_field, hash_field in bindings:
                if row[hash_field] is None:
                    continue
                artifact, location = provenance.resolve_ledger_artifact(
                    row[path_field], row[hash_field]
                )
                locations[location] += 1
                self.assertEqual(
                    hashlib.sha256(artifact.read_bytes()).hexdigest(),
                    row[hash_field],
                )
        fresh_bindings = sum(
            row[field] is not None
            for row in self.audit + self.legacy + self.agnostic
            if row["status"] == "authoritative"
            and (
                row in self.legacy
                or row in self.agnostic
                or row["stage"] == "active-fresh-audit"
            )
            for field in (
                "assignment_sha256",
                "prompt_sha256",
                "execution_brief_sha256",
                "output_sha256",
            )
        )
        self.assertEqual(
            locations, Counter({"live": 1027 + fresh_bindings, "archive": 840})
        )

    def test_live_then_archived_exact_artifact_resolution(self) -> None:
        with TemporaryDirectory() as directory:
            repo_root = Path(directory)
            artifact_root = repo_root / "release"
            live_path = artifact_root / "assignment.json"
            live_path.parent.mkdir(parents=True)
            live_path.write_text("{}\n", encoding="utf-8")
            digest = hashlib.sha256(live_path.read_bytes()).hexdigest()
            resolved, location = provenance.resolve_ledger_artifact(
                "release/assignment.json",
                digest,
                repo_root=repo_root,
                archive_roots=(artifact_root,),
            )
            self.assertEqual((resolved, location), (live_path.resolve(), "live"))

            archive_root = artifact_root / provenance.ISOLATION_ARCHIVE_NAME
            archived_path = (
                archive_root / "non_authoritative" / "artifacts" / "assignment.json"
            )
            archived_path.parent.mkdir(parents=True)
            live_path.replace(archived_path)
            manifest = {
                "archive_relpath": "non_authoritative/artifacts/assignment.json",
                "authoritative": False,
                "bytes": archived_path.stat().st_size,
                "category": "fixture",
                "original_relpath": "assignment.json",
                "pool": "non_authoritative",
                "reason": "fixture",
                "reconciliation_eligible": False,
                "replacement_required": True,
                "sha256": digest,
                "trainable": False,
            }
            (archive_root / "manifest.jsonl").write_text(
                json.dumps(manifest, sort_keys=True) + "\n", encoding="utf-8"
            )
            resolved, location = provenance.resolve_ledger_artifact(
                "release/assignment.json",
                digest,
                repo_root=repo_root,
                archive_roots=(artifact_root,),
            )
            self.assertEqual((resolved, location), (archived_path.resolve(), "archive"))

    def test_append_fresh_authoritative_row_checks_live_context(self) -> None:
        with TemporaryDirectory() as directory:
            repo_root = Path(directory)
            assignment = repo_root / "fixture" / "assignment.json"
            output = repo_root / "fixture" / "output.jsonl"
            ledger = repo_root / "fixture" / "ledger.jsonl"
            assignment.parent.mkdir(parents=True)
            assignment.write_text("{}\n", encoding="utf-8")
            output.write_text('{"ok":true}\n', encoding="utf-8")
            row = dict(self.agnostic[0])
            row.update(
                {
                    "ledger_id": "fixture_fresh_authoritative",
                    "stage": "generation",
                    "status": "authoritative",
                    "requires_rerun": False,
                    "rerun_reason": None,
                    "assignment_relpath": "fixture/assignment.json",
                    "assignment_sha256": hashlib.sha256(
                        assignment.read_bytes()
                    ).hexdigest(),
                    "agent_task_path": "/root/fixture_fresh_authoritative",
                    "thread_id": "00000000-0000-4000-8000-000000000001",
                    "turn_id": "00000000-0000-4000-8000-000000000002",
                    "output_relpath": "fixture/output.jsonl",
                    "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                    "output_records": 1,
                }
            )
            provenance.append_authoritative_execution_row(
                ledger, row, repo_root=repo_root
            )
            self.assertEqual(provenance.jsonl_rows(ledger), [row])
            with self.assertRaisesRegex(ValueError, "agent task path was already used"):
                provenance.append_authoritative_execution_row(
                    ledger, {**row, "ledger_id": "fixture_duplicate"}, repo_root=repo_root
                )

    def test_recover_and_append_unique_local_assignment_write(self) -> None:
        with TemporaryDirectory() as directory:
            repo_root = Path(directory)
            assignment, ledger, sessions, task_path = self._write_recovery_fixture(
                repo_root, include_prompt_bindings=True
            )
            row = provenance.recover_and_append_authoritative_assignment(
                assignment,
                ledger,
                expected_stage="generation",
                release_id="agnostic-mathia-openalex-supplement-v1",
                agent_task_path=task_path,
                session_roots=(sessions,),
                repo_root=repo_root,
            )
            self.assertEqual(row["status"], "authoritative")
            self.assertFalse(row["requires_rerun"])
            self.assertEqual(row["prompt_recovery_status"], "verified-file")
            self.assertEqual(row["output_records"], 1)
            self.assertEqual(row["agent_task_path"], task_path)
            self.assertIsNone(row["service_checkpoint_id"])
            self.assertEqual(len(provenance.jsonl_rows(ledger)), 2)
            serialized = json.dumps(row, sort_keys=True)
            self.assertNotIn("fixture encrypted envelope", serialized)
            self.assertNotIn("fixture prompt body", serialized)

    def test_recovery_marks_unavailable_plaintext_prompt_encrypted_only(self) -> None:
        with TemporaryDirectory() as directory:
            repo_root = Path(directory)
            assignment, ledger, sessions, task_path = self._write_recovery_fixture(
                repo_root, include_prompt_bindings=False
            )
            row = provenance.recover_authoritative_execution_row(
                assignment,
                ledger,
                expected_stage="generation",
                release_id="agnostic-mathia-openalex-supplement-v1",
                agent_task_path=task_path,
                session_roots=(sessions,),
                repo_root=repo_root,
            )
            self.assertEqual(row["prompt_recovery_status"], "encrypted-local-only")
            self.assertIsNone(row["prompt_relpath"])
            self.assertIsNone(row["prompt_sha256"])
            self.assertRegex(row["task_envelope_ciphertext_sha256"], r"^[0-9a-f]{64}$")

    def test_recovery_rejects_ambiguous_or_mismatched_context(self) -> None:
        with TemporaryDirectory() as directory:
            repo_root = Path(directory)
            assignment, ledger, sessions, task_path = self._write_recovery_fixture(
                repo_root,
                include_prompt_bindings=False,
                duplicate_write=True,
            )
            kwargs = {
                "assignment_path": assignment,
                "ledger_path": ledger,
                "expected_stage": "generation",
                "release_id": "agnostic-mathia-openalex-supplement-v1",
                "agent_task_path": task_path,
                "session_roots": (sessions,),
                "repo_root": repo_root,
            }
            with self.assertRaisesRegex(ValueError, "found 2"):
                provenance.recover_authoritative_execution_row(**kwargs)
            with self.assertRaisesRegex(ValueError, "stage mismatch"):
                provenance.recover_authoritative_execution_row(
                    **{**kwargs, "expected_stage": "critic"}
                )
            with self.assertRaisesRegex(ValueError, "release_id mismatch"):
                provenance.recover_authoritative_execution_row(
                    **{**kwargs, "release_id": "wrong-release"}
                )
            with self.assertRaisesRegex(ValueError, "found 0"):
                provenance.recover_authoritative_execution_row(
                    **{**kwargs, "agent_task_path": "/root/wrong_task"}
                )

    def test_read_only_output_variable_is_not_a_write(self) -> None:
        call = provenance.ToolCall(
            index=1,
            call_id="read-only",
            turn_id="00000000-0000-4000-8000-000000000001",
            timestamp="2026-08-21T12:00:00Z",
            input_text="output='fixture/output.jsonl'; output.read_text()",
        )
        self.assertFalse(provenance.is_output_mutation(call, "output.jsonl"))

    def test_post_isolation_coverage_accepts_fresh_authoritative_rows(self) -> None:
        fresh = {
            **self.agnostic[0],
            "ledger_id": "fixture_post_isolation_authoritative",
            "status": "authoritative",
            "requires_rerun": False,
            "rerun_reason": None,
        }
        summary = provenance.validate_coverage(
            self.audit,
            self.decisions,
            self.legacy,
            [*self.agnostic, fresh],
        )
        current_fresh = sum(
            row["status"] == "authoritative" for row in self.agnostic
        )
        self.assertEqual(summary["agnostic_rows"], 103 + current_fresh)
        self.assertEqual(
            summary["agnostic_fresh_authoritative_rows"], current_fresh + 1
        )
        self.assertEqual(summary["agnostic_requires_rerun"], 102)

    def test_ledger_serialization_excludes_sensitive_rollout_content(self) -> None:
        paths = (
            provenance.RIEMANN_AUDIT_LEDGER,
            provenance.RIEMANN_DECISION_MAP,
            provenance.LEGACY_CONTEXT_LEDGER,
            provenance.AGNOSTIC_EXECUTION_LEDGER,
        )
        payload = "\n".join(path.read_text(encoding="utf-8") for path in paths).lower()
        for pattern in provenance.SENSITIVE_PATTERNS:
            self.assertNotIn(pattern.lower(), payload)
        self.assertNotIn("/root/.codex", payload)

    def test_secret_pattern_guard_rejects_unsafe_output(self) -> None:
        for pattern in provenance.SENSITIVE_PATTERNS:
            with self.subTest(pattern=pattern):
                with self.assertRaisesRegex(ValueError, "sensitive pattern rejected"):
                    provenance.reject_sensitive_content([{"unsafe": pattern}])


if __name__ == "__main__":
    unittest.main()
