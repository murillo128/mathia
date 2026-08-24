from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from experiments.frontier_intuition_corpus_v1 import core


class FakeTokenizer:
    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        if add_special_tokens:
            raise AssertionError("issue #57 must not add special tokens")
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
        **core.EVALUATION_MARKERS,
    }
    row.update(updates)
    return row


class CoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = FakeTokenizer()

    def classify(self, text: str | None, *, valid: bool = True) -> dict[str, object]:
        return core.classify_text(
            raw_text=text,
            valid_tool_free_capture=valid,
            declaration_name="sample",
            tokenizer=self.tokenizer,
        )

    def test_ordered_identity_matches_qwen_json_contract(self) -> None:
        self.assertEqual(
            core.ordered_ids_sha256(["a", "b"]),
            core.sha256_text('["a","b"]'),
        )

    def test_prompt_uses_exact_request_and_source_only(self) -> None:
        row = source_row()
        prompt = core.render_prompt(row)
        self.assertIn(core.INTUITION_REQUEST, prompt)
        self.assertIn(str(row["declaration"]), prompt)
        self.assertNotIn("proof_variants", prompt)
        self.assertTrue(prompt.endswith("\n\nStrategy:\n"))

    def test_source_rejects_forbidden_field(self) -> None:
        row = source_row(proof="secret")
        with self.assertRaisesRegex(ValueError, "theorem-only schema"):
            core.validate_source_row(row)

    def test_evaluation_markers_are_required(self) -> None:
        row = source_row(training_eligible=True)
        with self.assertRaisesRegex(ValueError, "training_eligible"):
            core.validate_source_row(row)

    def test_accepted_gate(self) -> None:
        decision = self.classify(
            "View both sides as the same invariant decomposition. Isolate the shared component, "
            "then compare the complementary pieces through symmetry."
        )
        self.assertEqual(decision["status"], "accepted")
        self.assertTrue(decision["eligible"])

    def test_generation_failure_precedes_other_reasons(self) -> None:
        decision = self.classify("```lean\nby simp\n```", valid=False)
        self.assertEqual(decision["status"], "generation_failure")

    def test_lean_syntax_gate(self) -> None:
        decision = self.classify("Use the identity.\nby\n  simp")
        self.assertEqual(decision["status"], "rejected_lean_syntax")

    def test_natural_by_and_show_language_is_allowed(self) -> None:
        decision = self.classify(
            "By symmetry, reduce to one component. Show that its invariant controls x_i; "
            "e.g. compare the two complementary representations."
        )
        self.assertEqual(decision["status"], "accepted")

    def test_formal_identifier_gate(self) -> None:
        decision = self.classify("Apply Finset.sum to reorganize the expression.")
        self.assertEqual(decision["status"], "rejected_formal_identifier")

    def test_copied_declaration_name_gate(self) -> None:
        decision = self.classify("Reinterpret sample through symmetry.")
        self.assertEqual(decision["status"], "rejected_formal_identifier")

    def test_proof_like_gate(self) -> None:
        decision = self.classify("We now prove the claim by exhausting every case.")
        self.assertEqual(decision["status"], "rejected_proof_like")

    def test_over_budget_gate(self) -> None:
        decision = self.classify("word " * 97)
        self.assertEqual(decision["status"], "rejected_over_budget")
        self.assertEqual(decision["post_render"]["token_count"], 97)  # type: ignore[index]

    def test_comment_escape_is_counted_and_preserved(self) -> None:
        decision = self.classify("View /- the obstruction -/ conceptually.")
        self.assertEqual(decision["status"], "rejected_lean_syntax")
        self.assertEqual(
            decision["downstream_visible_text"],
            "View / - the obstruction - / conceptually.",
        )

    def test_transcript_accepts_only_one_tool_free_message(self) -> None:
        transcript = "\n".join(
            (
                json.dumps({"type": "thread.started", "thread_id": "thread-1"}),
                json.dumps({"type": "item.completed", "item": {"type": "reasoning"}}),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "agent_message", "text": "strategy"},
                    }
                ),
            )
        )
        parsed = core.parse_codex_transcript(transcript)
        self.assertTrue(parsed["valid_tool_free_capture"])
        self.assertEqual(parsed["final_message"], "strategy")

    def test_transcript_rejects_tool_item(self) -> None:
        transcript = "\n".join(
            (
                json.dumps({"type": "thread.started", "thread_id": "thread-1"}),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "command_execution", "command": "pwd"},
                    }
                ),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {"type": "agent_message", "text": "strategy"},
                    }
                ),
            )
        )
        parsed = core.parse_codex_transcript(transcript)
        self.assertFalse(parsed["valid_tool_free_capture"])
        self.assertEqual(parsed["unexpected_item_types"], ["command_execution"])

    def test_write_once_refuses_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact.json"
            core.write_json_once(path, {"a": 1})
            with self.assertRaisesRegex(RuntimeError, "write-once"):
                core.write_json_once(path, {"a": 2})

    def test_accepted_projection_selects_first_eligible(self) -> None:
        source = source_row()
        failed = {
            "workload": source["workload"],
            "task_id": source["task_id"],
            "attempt_id": "attempt-1",
            "attempt_index": 1,
            "eligibility": self.classify("```lean\nby simp\n```"),
        }
        success = {
            "workload": source["workload"],
            "task_id": source["task_id"],
            "attempt_id": "attempt-2",
            "attempt_index": 2,
            "eligibility": self.classify("Use symmetry to compare the two invariant pieces."),
        }
        accepted, leakage = core._accepted_projection([source], [failed, success])
        self.assertEqual(accepted[0]["accepted_attempt_id"], "attempt-2")
        self.assertEqual(leakage[0]["task_status"], "accepted")
        for key, expected in core.EVALUATION_MARKERS.items():
            self.assertEqual(accepted[0][key], expected)


if __name__ == "__main__":
    unittest.main()
