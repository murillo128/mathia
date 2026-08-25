from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from experiments.frontier_assisted_intuition_corpus_v1 import core


class FakeTokenizer:
    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        if add_special_tokens:
            raise AssertionError("issue #59 must not add special tokens")
        return list(range(len(text.split())))


def source_row(**updates: object) -> dict[str, object]:
    declaration = "theorem sample (P : Prop) (h : P) : P"
    context = "import Mathlib"
    row: dict[str, object] = {
        "schema_version": core.SOURCE_SCHEMA_VERSION,
        "workload": "minif2f-valid-clean-v2",
        "task_id": "sample",
        "declaration_name": "sample",
        "declaration": declaration,
        "public_context": context,
        "model_visible_theorem_sha256": core.sha256_text(
            core.render_model_visible_theorem(public_context=context, declaration=declaration)
        ),
        "upstream": {
            "repository": core.QWEN_REPOSITORY,
            "accepted_commit": core.QWEN_ACCEPTED_COMMIT,
            "membership_evidence_commit": core.QWEN_MEMBERSHIP_EVIDENCE_COMMIT,
            "source_path": core.MINIF2F_PATH,
            "source_file_sha256": core.UPSTREAM_FILE_SHA256[core.MINIF2F_PATH],
        },
        "projection_provenance": {
            "source_issue": core.PRIOR_ISSUE,
            "source_snapshot_path": "experiments/frontier_intuition_corpus_v1/source_tasks.jsonl",
            "source_snapshot_sha256": "0" * 64,
            "copied_fields": [],
            "prior_generation_outputs_copied": False,
        },
        **core.EVALUATION_MARKERS,
    }
    row.update(updates)
    return row


def valid_capture(message: str, *, tool: bool = False) -> dict[str, object]:
    events = [
        {"type": "thread.started", "thread_id": "thread-1"},
        {"type": "item.completed", "item": {"type": "reasoning"}},
    ]
    if tool:
        events.append({
            "type": "item.completed",
            "item": {
                "id": "search-1", "type": "web_search", "query": "site:example.org theorem",
                "action": {"type": "search"},
            },
        })
    events.append({"type": "item.completed", "item": {"type": "agent_message", "text": message}})
    transcript = "\n".join(json.dumps(row) for row in events)
    parsed = core.parse_codex_transcript(transcript, tools_allowed=True)
    return {
        "returncode": 0, "timed_out": False, "stdout_jsonl": transcript,
        "stdout_sha256": core.sha256_text(transcript), "stderr": "",
        "stderr_sha256": core.sha256_text(""), **parsed,
    }


class CoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = FakeTokenizer()

    def test_ordered_identity_matches_qwen_json_contract(self) -> None:
        self.assertEqual(core.ordered_ids_sha256(["a", "b"]), core.sha256_text('["a","b"]'))

    def test_calibration_is_exact_evenly_spaced_8_plus_16(self) -> None:
        self.assertEqual(core.calibration_indices(244, 8), [0, 34, 69, 104, 138, 173, 208, 243])
        self.assertEqual(core.calibration_indices(406, 16), list(range(0, 406, 27)))

    def test_prompt_is_theorem_only_and_retry_is_frozen(self) -> None:
        row = source_row()
        first = core.render_prompt(row, attempt_index=1)
        second = core.render_prompt(row, attempt_index=2)
        self.assertIn(core.INTUITION_REQUEST, first)
        self.assertNotIn(core.RETRY_REMINDER, first)
        self.assertIn(core.RETRY_REMINDER, second)
        self.assertNotIn("oracle_proof", first)

    def test_source_rejects_privileged_field(self) -> None:
        row = source_row(proof="secret")
        with self.assertRaisesRegex(ValueError, "theorem-only contract"):
            core.validate_source_row(row)

    def test_hard_gate_accepts_ordinary_mathematical_vocabulary(self) -> None:
        text = (
            "Lean aside, use induction and ring arithmetic conceptually: expose the invariant "
            "factorization, then view Real.sqrt as ordinary notation and reduce by symmetry."
        )
        result = core.hard_check(text, self.tokenizer)
        self.assertEqual(result["status"], "hard_pass")

    def test_hard_gate_rejects_unambiguous_lean_recipe(self) -> None:
        cases = (
            "```lean\ntheorem x : True := by simp\n```",
            "Use Nat.Prime.dvd_of_dvd_pow as the API recipe.",
            "apply h; rw [identity]; exact result",
            "have h : P := by\n  simpa",
        )
        for text in cases:
            with self.subTest(text=text):
                self.assertEqual(core.hard_check(text, self.tokenizer)["status"], "hard_reject")

    def test_generator_transcript_allows_and_records_web_use(self) -> None:
        capture = valid_capture("Use the invariant decomposition.", tool=True)
        self.assertTrue(capture["valid_capture"])
        self.assertEqual(capture["support_item_types"], {"web_search": 1})
        self.assertEqual(capture["source_domains"], ["example.org"])

    def test_semantic_reviewer_transcript_rejects_tool_use(self) -> None:
        capture = valid_capture('{"decision":"accepted_intuition"}', tool=True)
        replay = core.parse_codex_transcript(str(capture["stdout_jsonl"]), tools_allowed=False)
        self.assertFalse(replay["valid_capture"])

    def test_generator_selects_final_message_after_interim_web_message(self) -> None:
        events = (
            {"type": "thread.started", "thread_id": "thread-1"},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "I will check a public reference."}},
            {"type": "item.completed", "item": {"type": "web_search", "query": "site:example.org theorem"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Use the invariant decomposition."}},
        )
        transcript = "\n".join(json.dumps(row) for row in events)
        parsed = core.parse_codex_transcript(
            transcript, tools_allowed=True, allow_interim_agent_messages=True
        )
        self.assertTrue(parsed["valid_capture"])
        self.assertEqual(parsed["agent_message_count"], 2)
        self.assertEqual(parsed["interim_agent_message_count"], 1)
        self.assertEqual(parsed["final_message"], "Use the invariant decomposition.")
        strict = core.parse_codex_transcript(
            transcript, tools_allowed=True, allow_interim_agent_messages=False
        )
        self.assertFalse(strict["valid_capture"])

    def test_revised_semantic_rubric_rejects_compact_complete_derivations(self) -> None:
        rubric = core.SEMANTIC_REVIEW_INSTRUCTION
        self.assertIn("even to a concise one-paragraph derivation", rubric)
        self.assertIn("one-step elementary identity", rubric)
        self.assertIn("evaluates both theorem-specific sums", rubric)
        self.assertIn("evaluates the theorem's percentages", rubric)
        self.assertIn("Cosmetic omission of an explicit final result", rubric)
        self.assertIn("decisive justification for every clause", rubric)
        fixtures = json.loads(
            (Path(__file__).parent / "semantic_boundary_revision_fixtures.json").read_text(encoding="utf-8")
        )
        self.assertEqual(len(fixtures), 7)
        self.assertTrue(all(row["expected_decision"] == "rejected_near_complete_proof" for row in fixtures))
        self.assertTrue(all(row["candidate"] not in core.INTUITION_REQUEST for row in fixtures))

    def test_semantic_decision_schema(self) -> None:
        message = json.dumps({
            "decision": "accepted_intuition", "semantic_truncation_detected": False,
            "boundary_basis": "Compact mechanism rather than an implementation.",
        })
        capture = valid_capture(message)
        decision = core._parse_semantic_decision(capture)
        self.assertEqual(decision["status"], "review_valid")
        self.assertEqual(decision["decision"], "accepted_intuition")

    def test_attempt_eligibility_combines_layers_and_cap(self) -> None:
        text = "Use symmetry to expose the shared invariant."
        attempt = {
            "generation_capture": valid_capture(text, tool=True),
            "hard_check": core.hard_check(text, self.tokenizer),
            "semantic_boundary_review": {
                "status": "review_valid", "decision": "accepted_intuition",
                "semantic_truncation_detected": False,
            },
        }
        self.assertTrue(core.attempt_eligibility(attempt, maximum_tokens=128)["eligible"])
        self.assertFalse(core.attempt_eligibility(attempt, maximum_tokens=3)["eligible"])

    def test_circuit_breakers(self) -> None:
        missing = {
            "workload": "w", "task_id": "t", "accepted": False,
            "runtime_missing": False,
        }
        accepted = {**missing, "accepted": True}
        self.assertEqual(core._circuit_breaker([missing] * 12)["rule"], "consecutive_missing")
        early = [accepted] * 17 + [missing] * 7
        self.assertEqual(core._circuit_breaker(early)["rule"], "early_24_acceptance")
        rolling = [accepted] * 24 + [accepted] * 23 + [missing] * 9
        self.assertEqual(core._circuit_breaker(rolling)["rule"], "rolling_32_acceptance")

    def test_write_once_refuses_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact.json"
            core.write_json_once(path, {"a": 1})
            with self.assertRaisesRegex(RuntimeError, "write-once"):
                core.write_json_once(path, {"a": 2})


if __name__ == "__main__":
    unittest.main()
