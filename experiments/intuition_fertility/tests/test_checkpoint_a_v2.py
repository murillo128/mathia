from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from experiments.intuition_fertility.checkpoint_a import (
    DEFAULT_CHECKPOINT_A_PATH,
    EXPECTED_CHECKPOINT_A_ID,
    read_checkpoint_a,
)
from experiments.intuition_fertility.checkpoint_a_v2 import (
    DEFAULT_CHECKPOINT_A_V2_PATH,
    EXPECTED_CHECKPOINT_A_V2_ID,
    derive_first_unused_seeds,
    read_checkpoint_a_v2,
    validate_checkpoint_a_v2,
)


class CheckpointAV2FreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = json.loads(DEFAULT_CHECKPOINT_A_V2_PATH.read_text(encoding="utf-8"))

    def test_committed_v2_validates_without_authorizing_later_work(self) -> None:
        freeze = read_checkpoint_a_v2()
        self.assertEqual(freeze.freeze_id, EXPECTED_CHECKPOINT_A_V2_ID)
        self.assertEqual(freeze.protected_seeds, [1, 2, 3, 4])
        self.assertFalse(freeze.protected_execution_authorized)
        self.assertFalse(freeze.value["gates"]["checkpoints_b_through_f_authorized"])

    def test_v1_blocker_artifact_is_preserved_exactly(self) -> None:
        v1 = read_checkpoint_a()
        self.assertEqual(v1.freeze_id, EXPECTED_CHECKPOINT_A_ID)
        self.assertEqual(
            hashlib.sha256(DEFAULT_CHECKPOINT_A_PATH.read_bytes()).hexdigest(),
            "a50372c672db60edd650aa5bdd36ef30af90c45b097d5dbd57de69e43db842f9",
        )
        self.assertEqual(v1.blocker_code, "PRE_FREEZE_TARGET_EXECUTION_CONTAMINATION")

    def test_materialized_contract_changes_only_reviewed_seed_field(self) -> None:
        v1 = read_checkpoint_a().value
        v2 = read_checkpoint_a_v2().materialized_scientific_contract()
        unchanged_sections = (
            "source_contract",
            "panel",
            "generator_protocol",
            "sample_policy",
            "leakage_policy",
            "condition_materialization",
            "formal_worker_binding",
            "prompt_contract",
            "analysis_contract",
        )
        for section in unchanged_sections:
            with self.subTest(section=section):
                self.assertEqual(v2[section], v1[section])

        generation = copy.deepcopy(v2["formal_worker_generation"])
        self.assertTrue(generation.pop("same_seed_set_across_theorems_A_to_G"))
        self.assertEqual(generation.pop("repeat_seeds"), [1, 2, 3, 4])
        expected = copy.deepcopy(v1["formal_worker_generation"])
        self.assertEqual(expected.pop("repeat_seeds"), [0, 1, 2, 3])
        self.assertEqual(generation, expected)

    def test_membership_audit_finds_only_B(self) -> None:
        memberships = self.value["historical_execution_audit"]["target_membership"]
        overlaps = [
            entry["theorem_id"]
            for entry in memberships
            if entry["candidate_generation_memberships"]
        ]
        self.assertEqual(overlaps, ["B"])
        b_membership = memberships[1]["candidate_generation_memberships"][0]
        self.assertEqual(b_membership["selected_record_index_zero_based"], 351)
        self.assertEqual(b_membership["seed"], 0)
        self.assertEqual(b_membership["candidate_indexes"], [0, 1, 2, 3])

    def test_all_found_draws_are_burned_sealed_and_excluded(self) -> None:
        draws = self.value["historical_execution_audit"]["historical_draws"]
        self.assertEqual(len(draws), 4)
        self.assertEqual([draw["candidate_index"] for draw in draws], [0, 1, 2, 3])
        for draw in draws:
            self.assertTrue(draw["burned"])
            self.assertTrue(draw["sealed"])
            self.assertTrue(draw["excluded"])

    def test_first_unused_rule_is_mechanical(self) -> None:
        draws = self.value["historical_execution_audit"]["historical_draws"]
        self.assertEqual(derive_first_unused_seeds(draws), [1, 2, 3, 4])
        additional = copy.deepcopy(draws)
        additional.append({"seed": 2})
        additional.append({"seed": 5})
        self.assertEqual(derive_first_unused_seeds(additional), [1, 3, 4, 6])

    def test_same_four_seeds_and_k16_are_frozen_for_all_cells(self) -> None:
        generation = self.value["formal_worker_generation"]
        self.assertEqual(generation["repeat_seeds"], [1, 2, 3, 4])
        self.assertEqual(generation["candidates_per_seed"], 4)
        self.assertEqual(generation["candidate_budget_per_eligible_cell"], 16)
        self.assertTrue(generation["same_seed_set_across_conditions"])
        self.assertTrue(generation["same_seed_set_across_theorems_A_to_G"])

    def test_outcome_blinding_and_non_execution_are_frozen(self) -> None:
        blinding = self.value["historical_execution_audit"]["outcome_blinding"]
        self.assertFalse(blinding["candidate_outputs_opened"])
        self.assertFalse(blinding["item_level_verification_results_opened"])
        self.assertFalse(blinding["aggregate_outcomes_used_for_draw_selection"])
        gates = self.value["gates"]
        for field in (
            "qwen_inference_performed",
            "codex_generation_performed",
            "qwen_lean_inference_performed",
            "gpu_work_performed",
            "candidate_outputs_or_item_level_results_inspected",
        ):
            self.assertFalse(gates[field])

    def test_seed_or_historical_disposition_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["formal_worker_generation"]["repeat_seeds"] = [0, 1, 2, 3]
        with self.assertRaisesRegex(ValueError, "formal-worker generation"):
            validate_checkpoint_a_v2(changed)

        changed = copy.deepcopy(self.value)
        changed["historical_execution_audit"]["historical_draws"][0]["excluded"] = False
        with self.assertRaisesRegex(ValueError, "excluded disposition"):
            validate_checkpoint_a_v2(changed)

    def test_panel_worker_prompt_leakage_or_metrics_base_drift_is_rejected(
        self,
    ) -> None:
        base = json.loads(DEFAULT_CHECKPOINT_A_PATH.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            for section in (
                "panel",
                "formal_worker_binding",
                "prompt_contract",
                "leakage_policy",
                "analysis_contract",
            ):
                with self.subTest(section=section):
                    changed = copy.deepcopy(base)
                    changed[section]["unexpected_drift"] = True
                    path = Path(directory) / f"{section}.json"
                    path.write_text(json.dumps(changed), encoding="utf-8")
                    with self.assertRaisesRegex(
                        ValueError, "historical v1 artifact hash"
                    ):
                        validate_checkpoint_a_v2(self.value, base_v1_path=path)

    def test_unknown_or_unvalidated_v2_drift_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["unexpected"] = True
        with self.assertRaisesRegex(ValueError, "unknown fields"):
            validate_checkpoint_a_v2(changed)

        changed = copy.deepcopy(self.value)
        changed["historical_execution_audit"]["scope"] = "changed"
        with self.assertRaisesRegex(ValueError, "content id"):
            validate_checkpoint_a_v2(changed)

    def test_cli_reports_the_frozen_v2_without_execution_authority(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-m",
                "experiments.intuition_fertility",
                "checkpoint-a-v2",
            ],
            cwd=Path(__file__).parents[3],
            check=True,
            capture_output=True,
            text=True,
        )
        summary = json.loads(completed.stdout)
        self.assertTrue(summary["valid"])
        self.assertEqual(summary["protected_seeds"], [1, 2, 3, 4])
        self.assertEqual(summary["historical_draw_count"], 4)
        self.assertFalse(summary["protected_formal_worker_execution_authorized"])
        self.assertFalse(summary["checkpoints_b_through_f_authorized"])


if __name__ == "__main__":
    unittest.main()
