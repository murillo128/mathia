from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from experiments.intuition_fertility.checkpoint_a import (
    DEFAULT_CHECKPOINT_A_PATH,
    read_checkpoint_a,
    render_generator_prompt,
    render_leakage_review_prompt,
    validate_checkpoint_a,
)
from experiments.intuition_fertility.panel import get_public_target, get_target_identity


class CheckpointAFreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = json.loads(DEFAULT_CHECKPOINT_A_PATH.read_text(encoding="utf-8"))

    def test_committed_freeze_validates_and_keeps_later_checkpoints_unauthorized(
        self,
    ) -> None:
        freeze = read_checkpoint_a()
        self.assertTrue(freeze.freeze_id.startswith("checkpoint_a_"))
        self.assertFalse(freeze.protected_execution_authorized)
        self.assertIsNone(freeze.blocker_code)

    def test_validation_selected_phase5_worker_and_hub_revision_are_exact(self) -> None:
        worker = self.value["formal_worker_binding"]
        adapter = worker["resolved_identity"]["adapter"]
        source = worker["resolved_identity"]["qwen_lean_source"]
        self.assertEqual(worker["status"], "frozen_validation_selected_phase5_adapter")
        self.assertEqual(adapter["selected_optimizer_step"], 9962)
        self.assertEqual(
            adapter["qwen_lean_training_artifact_sha256"],
            "48d33bc2f276d6f8c22525a5cb30fafe8677da95e866dbf3f37116e78e8ae990",
        )
        self.assertEqual(
            adapter["hub_revision"],
            "5a5fadc8ecfd46b31c7c6c2f3b8c00f1bcea6af5",
        )
        self.assertFalse(adapter["hub_floating_revision_allowed"])
        self.assertEqual(source["commit"], "ef09f5e0f11a54a25fcb95b324d766f675be49a3")

    def test_phase5_worker_identity_drift_is_rejected(self) -> None:
        mutations = (
            ("selected_optimizer_step", 4981),
            ("hub_revision", "main"),
            ("hub_adapter_model_safetensors_sha256", "0" * 64),
        )
        for field, replacement in mutations:
            with self.subTest(field=field):
                changed = copy.deepcopy(self.value)
                changed["formal_worker_binding"]["resolved_identity"]["adapter"][
                    field
                ] = replacement
                with self.assertRaisesRegex(ValueError, "formal-worker adapter"):
                    validate_checkpoint_a(changed)

    def test_generator_prompt_contains_only_public_payload_serialization(self) -> None:
        for theorem_id in "ABCDEFG":
            prompt = render_generator_prompt(theorem_id)
            identity = get_target_identity(theorem_id)
            self.assertNotIn(identity.canonical_target, prompt)
            self.assertNotIn(identity.record_id, prompt)
            self.assertNotIn(identity.source_path, prompt)
            self.assertTrue(prompt.startswith("Theorem statement:\n"))
            self.assertTrue(prompt.endswith("\n\nStrategy:\n"))

    def test_budget_and_materialized_cell_counts_are_bounded(self) -> None:
        formal = self.value["formal_worker_generation"]
        conditions = self.value["condition_materialization"]
        self.assertEqual(
            formal["candidate_budget_per_eligible_cell"],
            len(formal["repeat_seeds"]) * formal["candidates_per_seed"],
        )
        total_cells = (
            conditions["primary_cell_count_before_ineligibility"]
            + conditions["calibration_cell_count_before_ineligibility"]
        )
        self.assertEqual(total_cells, 59)
        self.assertEqual(
            total_cells * formal["candidate_budget_per_eligible_cell"], 944
        )

    def test_leakage_prompt_contains_only_rubric_and_blinded_payload(self) -> None:
        statement = get_public_target("D").statement
        prompt = render_leakage_review_prompt(
            theorem_statement=statement, candidate_guidance="Use compactness."
        )
        identity = get_target_identity("D")
        self.assertIn(statement, prompt)
        self.assertIn("Use compactness.", prompt)
        self.assertNotIn(identity.canonical_target, prompt)
        self.assertNotIn(identity.record_id, prompt)
        self.assertNotIn(identity.source_path, prompt)

    def test_phase4_or_intermediate_phase5_cannot_be_enabled(self) -> None:
        for field in ("phase4_allowed", "intermediate_phase5_allowed"):
            changed = copy.deepcopy(self.value)
            changed["formal_worker_binding"][field] = True
            with self.assertRaisesRegex(ValueError, "prohibition"):
                validate_checkpoint_a(changed)

    def test_worker_budget_or_seed_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["formal_worker_generation"]["candidate_budget_per_eligible_cell"] = 8
        with self.assertRaisesRegex(ValueError, "candidate budget"):
            validate_checkpoint_a(changed)

        changed = copy.deepcopy(self.value)
        changed["formal_worker_generation"]["repeat_seeds"] = [0]
        with self.assertRaisesRegex(ValueError, "formal seeds"):
            validate_checkpoint_a(changed)

    def test_panel_generator_and_analysis_drift_is_rejected(self) -> None:
        mutations = (
            ("panel", "panel_id", "panel_changed"),
            ("generator_protocol", "intuition_request", "changed"),
            ("leakage_policy", "review_prompt_template", "changed"),
            ("analysis_contract", "primary_theorem_ids", ["A"]),
        )
        for section, field, replacement in mutations:
            with self.subTest(section=section, field=field):
                changed = copy.deepcopy(self.value)
                changed[section][field] = replacement
                with self.assertRaises(ValueError):
                    validate_checkpoint_a(changed)

    def test_protected_execution_cannot_be_authorized_by_the_artifact(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["gates"]["protected_formal_worker_execution_authorized"] = True
        with self.assertRaisesRegex(ValueError, "protected execution gate"):
            validate_checkpoint_a(changed)

    def test_unknown_top_level_fields_are_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["unexpected"] = True
        with self.assertRaisesRegex(ValueError, "unknown fields"):
            validate_checkpoint_a(changed)

    def test_any_unvalidated_evidence_drift_changes_the_content_id(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["evidence_basis"]["candidate_budget_rationale"] = "changed"
        with self.assertRaisesRegex(ValueError, "content id"):
            validate_checkpoint_a(changed)

    def test_cli_reports_valid_freeze_without_worker_blocker(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-m",
                "experiments.intuition_fertility",
                "checkpoint-a",
            ],
            cwd=Path(__file__).parents[3],
            check=True,
            capture_output=True,
            text=True,
        )
        summary = json.loads(completed.stdout)
        self.assertTrue(summary["valid"])
        self.assertFalse(summary["protected_formal_worker_execution_authorized"])
        self.assertIsNone(summary["blocker_code"])


if __name__ == "__main__":
    unittest.main()
