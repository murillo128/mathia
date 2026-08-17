from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

from experiments.intuition_fertility.checkpoint_a import render_generator_prompt
from experiments.intuition_fertility.checkpoint_a_v2 import (
    EXPECTED_CHECKPOINT_A_V2_ID,
)
from experiments.intuition_fertility.checkpoint_b import (
    DEFAULT_CHECKPOINT_B_PATH,
    EXPECTED_CHECKPOINT_B_ID,
    read_checkpoint_b,
)
from experiments.intuition_fertility.checkpoint_b_v2 import (
    DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR,
    DEFAULT_CHECKPOINT_B_V2_PATH,
    EXPECTED_CHECKPOINT_B_V2_ID,
    read_checkpoint_b_v2,
    validate_checkpoint_b_v2,
)
from experiments.intuition_fertility.checkpoint_b_v2_runner import (
    BREVITY_INSTRUCTION,
    render_generator_prompt_v2,
)


class CheckpointBV2FreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = json.loads(DEFAULT_CHECKPOINT_B_V2_PATH.read_text(encoding="utf-8"))
        cls.v1_value = json.loads(DEFAULT_CHECKPOINT_B_PATH.read_text(encoding="utf-8"))

    def test_committed_freeze_validates_and_stops_before_checkpoint_c(self) -> None:
        freeze = read_checkpoint_b_v2()
        self.assertEqual(freeze.freeze_id, EXPECTED_CHECKPOINT_B_V2_ID)
        self.assertTrue(freeze.value["gates"]["checkpoint_b_v2_complete"])
        self.assertFalse(freeze.value["gates"]["checkpoint_c_authorized"])
        self.assertFalse(
            freeze.value["gates"]["protected_formal_worker_execution_authorized"]
        )

    def test_checkpoint_b_v1_is_exact_and_historical_only(self) -> None:
        self.assertEqual(read_checkpoint_b().freeze_id, EXPECTED_CHECKPOINT_B_ID)
        self.assertEqual(
            hashlib.sha256(DEFAULT_CHECKPOINT_B_PATH.read_bytes()).hexdigest(),
            "31bf0a493ef19560777c85936dba1362c6b6ebcd48df0a268b2276fadd789068",
        )
        historical = self.value["historical_checkpoint_b_v1"]
        self.assertEqual(historical["freeze_id"], EXPECTED_CHECKPOINT_B_ID)
        self.assertEqual(
            historical["disposition"],
            "preserved_historical_only_not_mixed_selected_or_substituted",
        )
        self.assertFalse(
            self.value["gates"]["checkpoint_b_v1_samples_mixed_selected_or_substituted"]
        )

    def test_prompt_changes_only_by_the_exact_common_brevity_sentence(self) -> None:
        amendment = self.value["protocol"]["prompt_amendment"]
        self.assertEqual(amendment["brevity_instruction"], BREVITY_INSTRUCTION)
        for theorem_id in "ABCDEFG":
            base = render_generator_prompt(theorem_id)
            amended = render_generator_prompt_v2(theorem_id)
            self.assertEqual(
                amended,
                base.removesuffix("\n\nStrategy:\n")
                + f"\n{BREVITY_INSTRUCTION}\n\nStrategy:\n",
            )
            self.assertEqual(amended.replace(f"\n{BREVITY_INSTRUCTION}", "", 1), base)
            self.assertEqual(amended.count(BREVITY_INSTRUCTION), 1)
            self.assertEqual(
                amendment["amended_prompt_sha256"][theorem_id],
                hashlib.sha256(amended.encode()).hexdigest(),
            )

    def test_all_other_generator_sample_and_leakage_policy_is_inherited(self) -> None:
        protocol = self.value["protocol"]
        self.assertEqual(
            protocol["inherited_checkpoint_a_generator_protocol"],
            self.v1_value["protocol"]["generator_protocol"],
        )
        self.assertEqual(
            protocol["sample_policy"], self.v1_value["protocol"]["sample_policy"]
        )
        self.assertEqual(
            protocol["leakage_policy"], self.v1_value["protocol"]["leakage_policy"]
        )
        self.assertEqual(
            self.value["source_contract"]["checkpoint_a_v2_id"],
            EXPECTED_CHECKPOINT_A_V2_ID,
        )

    def test_exactly_14_new_samples_are_frozen_without_v1_substitution(self) -> None:
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
        self.assertEqual(len({sample["sample_id"] for sample in samples}), 14)
        self.assertTrue(
            {sample["sample_id"] for sample in samples}.isdisjoint(
                {sample["sample_id"] for sample in self.v1_value["samples"]}
            )
        )
        self.assertTrue(
            {sample["capture_identity"] for sample in samples}.isdisjoint(
                {sample["capture_identity"] for sample in self.v1_value["samples"]}
            )
        )

    def test_96_token_gate_preserves_all_samples_and_one_leakage_ineligible(
        self,
    ) -> None:
        eligibility = self.value["eligibility"]
        self.assertEqual(
            [row["token_count"] for row in eligibility],
            [
                42,
                67,
                67,
                65,
                39,
                59,
                66,
                57,
                32,
                61,
                56,
                67,
                60,
                67,
            ],
        )
        self.assertTrue(all(not row["over_96_token_budget"] for row in eligibility))
        self.assertEqual(self.value["summary"]["over_budget_count"], 0)
        ineligible = [row for row in eligibility if not row["eligible"]]
        self.assertEqual(len(ineligible), 1)
        self.assertEqual(
            (ineligible[0]["theorem_id"], ineligible[0]["generator_role"]),
            ("G", "codex_reference"),
        )
        self.assertEqual(
            ineligible[0]["ineligibility_reasons"], ["leakage_label_borderline"]
        )

    def test_blind_leakage_resolution_preserves_the_single_dispute(self) -> None:
        self.assertEqual(self.value["summary"]["leakage_review_count"], 28)
        self.assertEqual(
            self.value["summary"]["leakage_labels"],
            {"strategic": 13, "borderline": 1, "proof_like": 0},
        )
        disputed = [
            decision
            for decision in self.value["leakage_decisions"]
            if decision["disputed"]
        ]
        self.assertEqual(len(disputed), 1)
        sample = next(
            sample
            for sample in self.value["samples"]
            if sample["sample_id"] == disputed[0]["sample_id"]
        )
        self.assertEqual(
            (sample["theorem_id"], sample["generator_role"]), ("G", "codex_reference")
        )
        self.assertEqual(disputed[0]["label"], "borderline")
        self.assertFalse(disputed[0]["uncertain"])
        raw_labels = [
            review["label"]
            for review in self.value["leakage_reviews"]
            if review["sample_id"] == sample["sample_id"]
        ]
        self.assertEqual(raw_labels, ["borderline", "proof_like"])

    def test_all_codex_sessions_are_unique_tool_free_and_hash_bound(self) -> None:
        transcripts = [
            capture["transcript_path"]
            for capture in self.value["sample_capture_evidence"]
            if capture["transcript_path"] is not None
        ] + [review["transcript_path"] for review in self.value["leakage_reviews"]]
        self.assertEqual(len(transcripts), 35)
        thread_ids: set[str] = set()
        for relative_path in transcripts:
            events = [
                json.loads(line)
                for line in (DEFAULT_CHECKPOINT_B_V2_EVIDENCE_DIR / relative_path)
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            started = [
                event for event in events if event.get("type") == "thread.started"
            ]
            self.assertEqual(len(started), 1)
            thread_ids.add(started[0]["thread_id"])
            completed_types = {
                event["item"]["type"]
                for event in events
                if event.get("type") == "item.completed"
            }
            self.assertLessEqual(completed_types, {"reasoning", "agent_message"})
        self.assertEqual(len(thread_ids), 35)
        self.assertEqual(len(self.value["evidence_manifest_sha256"]), 106)

    def test_execution_notes_record_zero_retries_and_pre_model_preflight(self) -> None:
        notes = self.value["execution_notes"]
        self.assertEqual(notes["qwen_actual_generation_batches"], 1)
        self.assertEqual(notes["codex_generation_sessions"], 7)
        self.assertEqual(notes["leakage_review_sessions"], 28)
        self.assertEqual(notes["retries"], 0)
        self.assertFalse(notes["system_python_preflight"]["sample_attempt_performed"])
        self.assertFalse(notes["system_python_preflight"]["capture_created"])
        self.assertFalse(notes["system_python_preflight"]["regeneration_attempt"])

    def test_protocol_sample_or_content_tampering_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["protocol"]["prompt_amendment"]["brevity_instruction"] = "changed"
        with self.assertRaisesRegex(ValueError, "inherited protocol"):
            validate_checkpoint_b_v2(changed)

        changed = copy.deepcopy(self.value)
        changed["samples"][0]["raw_text"] += " changed"
        with self.assertRaisesRegex(ValueError, "text_hash"):
            validate_checkpoint_b_v2(changed)

    def test_token_review_or_decision_tampering_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["sample_capture_evidence"][0]["post_escape_token_ids"].pop()
        with self.assertRaisesRegex(ValueError, "token list"):
            validate_checkpoint_b_v2(changed)

        changed = copy.deepcopy(self.value)
        changed["leakage_reviews"][0]["label"] = "proof_like"
        with self.assertRaisesRegex(ValueError, "review evidence summary"):
            validate_checkpoint_b_v2(changed)

        changed = copy.deepcopy(self.value)
        changed["leakage_decisions"][0]["label"] = "proof_like"
        with self.assertRaisesRegex(ValueError, "content or identity"):
            validate_checkpoint_b_v2(changed)

    def test_execution_and_progression_gates_cannot_drift(self) -> None:
        for field in (
            "checkpoint_b_v1_samples_mixed_selected_or_substituted",
            "qwen_lean_inference_performed",
            "lean_verification_performed",
            "historical_B_seed0_draws_opened",
            "checkpoint_c_authorized",
            "protected_formal_worker_execution_authorized",
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.value)
                changed["gates"][field] = True
                with self.assertRaisesRegex(ValueError, f"gate {field}"):
                    validate_checkpoint_b_v2(changed)

    def test_unknown_or_content_id_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["unexpected"] = True
        with self.assertRaisesRegex(ValueError, "unknown fields"):
            validate_checkpoint_b_v2(changed)

        changed = copy.deepcopy(self.value)
        changed["frozen_at_utc"] = "changed"
        with self.assertRaisesRegex(ValueError, "content id"):
            validate_checkpoint_b_v2(changed)

    def test_cli_reports_both_preserved_v1_and_complete_v2(self) -> None:
        root = Path(__file__).parents[3]
        v1 = subprocess.run(
            [sys.executable, "-m", "experiments.intuition_fertility", "checkpoint-b"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        v2 = subprocess.run(
            [
                sys.executable,
                "-m",
                "experiments.intuition_fertility",
                "checkpoint-b-v2",
            ],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(json.loads(v1.stdout)["freeze_id"], EXPECTED_CHECKPOINT_B_ID)
        summary = json.loads(v2.stdout)
        self.assertEqual(summary["freeze_id"], EXPECTED_CHECKPOINT_B_V2_ID)
        self.assertEqual(summary["sample_count"], 14)
        self.assertEqual(summary["eligible_count"], 13)
        self.assertEqual(summary["ineligible_count"], 1)
        self.assertFalse(summary["checkpoint_c_authorized"])
        self.assertFalse(summary["protected_formal_worker_execution_authorized"])


if __name__ == "__main__":
    unittest.main()
