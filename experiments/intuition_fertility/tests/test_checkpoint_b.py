from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from experiments.intuition_fertility.checkpoint_a_v2 import (
    EXPECTED_CHECKPOINT_A_V2_ID,
)
from experiments.intuition_fertility.checkpoint_b import (
    DEFAULT_CHECKPOINT_B_PATH,
    EXPECTED_CHECKPOINT_B_ID,
    _parse_codex_transcript,
    read_checkpoint_b,
    validate_checkpoint_b,
)


class CheckpointBFreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = json.loads(DEFAULT_CHECKPOINT_B_PATH.read_text(encoding="utf-8"))

    def test_committed_freeze_validates_and_stops_before_checkpoint_c(self) -> None:
        freeze = read_checkpoint_b()
        self.assertEqual(freeze.freeze_id, EXPECTED_CHECKPOINT_B_ID)
        self.assertTrue(freeze.value["gates"]["checkpoint_b_complete"])
        self.assertFalse(freeze.value["gates"]["checkpoint_c_or_d_authorized"])
        self.assertFalse(
            freeze.value["gates"]["protected_formal_worker_execution_authorized"]
        )

    def test_exact_checkpoint_a_v2_and_protocol_are_inherited(self) -> None:
        self.assertEqual(
            self.value["source_contract"]["checkpoint_a_v2_id"],
            EXPECTED_CHECKPOINT_A_V2_ID,
        )
        protocol = self.value["protocol"]
        self.assertEqual(protocol["sample_policy"]["maximum_guidance_tokens"], 96)
        self.assertEqual(protocol["sample_policy"]["regeneration_attempts"], 0)
        self.assertFalse(
            protocol["sample_policy"]["post_generation_truncation_or_padding"]
        )
        self.assertEqual(protocol["leakage_policy"]["reviewer_count"], 2)
        self.assertTrue(protocol["leakage_policy"]["blind_to_generator_identity"])
        self.assertTrue(protocol["leakage_policy"]["blind_to_formal_worker_outcomes"])

    def test_exactly_one_sample_per_generator_and_theorem_is_frozen(self) -> None:
        samples = self.value["samples"]
        self.assertEqual(len(samples), 14)
        self.assertEqual(
            [(sample["theorem_id"], sample["generator_role"]) for sample in samples],
            [
                (theorem_id, role)
                for theorem_id in "ABCDEFG"
                for role in ("qwen_base", "codex_reference")
            ],
        )
        self.assertEqual({sample["sample_index"] for sample in samples}, {0})
        self.assertEqual({sample["presentation"] for sample in samples}, {"standard"})
        self.assertEqual(len({sample["sample_id"] for sample in samples}), 14)
        self.assertEqual(len({sample["text_hash"] for sample in samples}), 14)

    def test_post_escape_token_counts_preserve_every_over_budget_sample(self) -> None:
        eligibility = self.value["eligibility"]
        qwen = [row for row in eligibility if row["generator_role"] == "qwen_base"]
        codex = [
            row for row in eligibility if row["generator_role"] == "codex_reference"
        ]
        self.assertEqual([row["token_count"] for row in qwen], [96] * 7)
        self.assertTrue(all(row["eligible"] for row in qwen))
        self.assertTrue(all(row["token_count"] > 96 for row in codex))
        self.assertTrue(all(not row["eligible"] for row in codex))
        self.assertTrue(
            all("over_96_token_budget" in row["ineligibility_reasons"] for row in codex)
        )

    def test_leakage_resolution_preserves_labels_and_disputes(self) -> None:
        decisions = {
            (row["theorem_id"], row["generator_role"]): decision
            for row, decision in zip(
                self.value["eligibility"],
                self.value["leakage_decisions"],
                strict=True,
            )
        }
        self.assertEqual(self.value["summary"]["leakage_review_count"], 28)
        self.assertEqual(
            self.value["summary"]["leakage_labels"],
            {"strategic": 11, "borderline": 3, "proof_like": 0},
        )
        disputed = [key for key, decision in decisions.items() if decision["disputed"]]
        self.assertEqual(
            disputed,
            [
                ("D", "codex_reference"),
                ("F", "codex_reference"),
                ("G", "codex_reference"),
            ],
        )
        for key in disputed:
            self.assertEqual(decisions[key]["label"], "borderline")
            self.assertFalse(decisions[key]["uncertain"])

    def test_capture_and_review_transcripts_are_hash_bound_and_tool_free(self) -> None:
        captures = self.value["sample_capture_evidence"]
        codex_captures = [
            capture
            for capture in captures
            if capture["generator_role"] == "codex_reference"
        ]
        self.assertEqual(len(codex_captures), 7)
        self.assertTrue(all(capture["transcript_path"] for capture in codex_captures))
        reviews = self.value["leakage_reviews"]
        self.assertEqual(len(reviews), 28)
        self.assertTrue(
            all(review["status"] == "valid_model_review" for review in reviews)
        )
        self.assertTrue(all(review["model_invoked"] for review in reviews))
        self.assertTrue(all(review["transcript_path"] for review in reviews))

    def test_transcript_parser_rejects_a_tool_event(self) -> None:
        events = (
            '{"type":"item.completed","item":{"type":"command_execution"}}\n'
            '{"type":"item.completed","item":{"type":"agent_message","text":"x"}}\n'
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "transcript.jsonl"
            path.write_text(events, encoding="utf-8")
            final_message, disallowed = _parse_codex_transcript(path)
        self.assertEqual(final_message, "x")
        self.assertEqual(disallowed, ["command_execution"])

    def test_sample_policy_or_content_tampering_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["protocol"]["sample_policy"]["maximum_guidance_tokens"] = 97
        with self.assertRaisesRegex(ValueError, "inherited protocol"):
            validate_checkpoint_b(changed)

        changed = copy.deepcopy(self.value)
        changed["samples"][0]["raw_text"] += " changed"
        with self.assertRaisesRegex(ValueError, "text_hash"):
            validate_checkpoint_b(changed)

    def test_token_or_leakage_decision_tampering_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["sample_capture_evidence"][0]["post_escape_token_ids"].pop()
        with self.assertRaisesRegex(ValueError, "token list"):
            validate_checkpoint_b(changed)

        changed = copy.deepcopy(self.value)
        changed["leakage_decisions"][0]["label"] = "proof_like"
        with self.assertRaisesRegex(ValueError, "content or identity"):
            validate_checkpoint_b(changed)

    def test_execution_and_progression_gates_cannot_drift(self) -> None:
        for field in (
            "qwen_lean_inference_performed",
            "lean_verification_performed",
            "historical_B_seed0_draws_opened",
            "checkpoint_c_or_d_authorized",
            "protected_formal_worker_execution_authorized",
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.value)
                changed["gates"][field] = True
                with self.assertRaisesRegex(ValueError, f"gate {field}"):
                    validate_checkpoint_b(changed)

    def test_unknown_or_unvalidated_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["unexpected"] = True
        with self.assertRaisesRegex(ValueError, "unknown fields"):
            validate_checkpoint_b(changed)

        changed = copy.deepcopy(self.value)
        changed["frozen_at_utc"] = "changed"
        with self.assertRaisesRegex(ValueError, "content id"):
            validate_checkpoint_b(changed)

    def test_cli_reports_complete_checkpoint_b_without_progression_authority(
        self,
    ) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-m",
                "experiments.intuition_fertility",
                "checkpoint-b",
            ],
            cwd=Path(__file__).parents[3],
            check=True,
            capture_output=True,
            text=True,
        )
        summary = json.loads(completed.stdout)
        self.assertEqual(summary["freeze_id"], EXPECTED_CHECKPOINT_B_ID)
        self.assertEqual(summary["sample_count"], 14)
        self.assertEqual(summary["eligible_count"], 7)
        self.assertEqual(summary["ineligible_count"], 7)
        self.assertFalse(summary["checkpoint_c_or_d_authorized"])
        self.assertFalse(summary["protected_formal_worker_execution_authorized"])


if __name__ == "__main__":
    unittest.main()
