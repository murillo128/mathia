from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter, defaultdict
from pathlib import Path

from experiments.intuition_fertility.checkpoint_a_v2 import (
    EXPECTED_CHECKPOINT_A_V2_ID,
)
from experiments.intuition_fertility.checkpoint_b_v2 import (
    EXPECTED_CHECKPOINT_B_V2_ID,
)
from experiments.intuition_fertility.checkpoint_c import (
    DEFAULT_CHECKPOINT_C_BUNDLE_PATH,
    DEFAULT_CHECKPOINT_C_PATH,
    EXPECTED_CHECKPOINT_C_ID,
    read_checkpoint_c,
    validate_checkpoint_c,
)
from experiments.intuition_fertility.conditions import Condition
from experiments.intuition_fertility.panel import ADJACENT_DONORS, DISTANT_DONORS


class CheckpointCFreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = json.loads(DEFAULT_CHECKPOINT_C_PATH.read_text(encoding="utf-8"))
        cls.freeze = read_checkpoint_c()
        cls.bundle = cls.freeze.bundle

    def test_committed_freeze_and_bundle_validate_without_results(self) -> None:
        self.assertEqual(self.freeze.freeze_id, EXPECTED_CHECKPOINT_C_ID)
        self.assertEqual(
            self.bundle.bundle_id,
            "bundle_5dcb4f97f22dadd8ba9b4135489ab2006d796dde9510ec518e44ab3a0fbbe600",
        )
        self.assertEqual(len(self.bundle.results), 0)
        self.assertEqual(
            self.bundle.runs[0].run_id,
            "run_15eb7b5d3d3ff8772f246bb882d8786ee3c0169d47bda4dfd4b46e2076829b13",
        )
        self.assertEqual(self.value["bundle"]["candidate_results_frozen"], 0)
        self.assertEqual(
            hashlib.sha256(DEFAULT_CHECKPOINT_C_BUNDLE_PATH.read_bytes()).hexdigest(),
            "8b8d863f0ef5a4f2751f5211a59218b272658125e30aadc0d7252592a67eb44b",
        )

    def test_exact_merged_a_v2_b_v2_and_panel_are_bound(self) -> None:
        source = self.value["source_contract"]
        self.assertEqual(
            source["mathia_main_commit"],
            "0f4da8f2a9520345c2aa450f756b9a9319d5ae8b",
        )
        self.assertEqual(
            source["checkpoint_a_v2"]["freeze_id"], EXPECTED_CHECKPOINT_A_V2_ID
        )
        self.assertEqual(
            source["checkpoint_b_v2"]["freeze_id"], EXPECTED_CHECKPOINT_B_V2_ID
        )
        self.assertEqual(len(self.bundle.samples), 14)
        self.assertEqual(len(self.bundle.decisions), 14)

    def test_exact_primary_and_calibration_cells_are_materialized(self) -> None:
        counts = Counter(cell.theorem_id for cell in self.bundle.cells)
        self.assertEqual(counts, Counter({**{item: 9 for item in "ABCDEF"}, "G": 5}))
        self.assertEqual(len(self.bundle.cells), 59)
        self.assertEqual(sum(cell.eligible for cell in self.bundle.cells), 58)
        self.assertEqual(len(self.bundle.prompts), 58)
        self.assertEqual(len(self.bundle.runs), 1)
        self.assertEqual(
            self.value["materialization"]["planned_candidate_slot_count"], 928
        )

    def test_donors_bind_exact_same_generator_samples_and_frozen_mappings(self) -> None:
        samples = {sample.sample_id: sample for sample in self.bundle.samples}
        donors = [
            cell
            for cell in self.bundle.cells
            if cell.condition
            in {
                Condition.ADJACENT_CROSS_THEOREM_STRATEGY.value,
                Condition.DISTANT_MISMATCHED_STRATEGY.value,
            }
        ]
        self.assertEqual(len(donors), 24)
        for cell in donors:
            anchor = samples[cell.anchor_sample_id]
            donor = samples[cell.guidance_sample_id]
            mapping = (
                ADJACENT_DONORS
                if cell.condition == Condition.ADJACENT_CROSS_THEOREM_STRATEGY.value
                else DISTANT_DONORS
            )
            self.assertEqual(anchor.theorem_id, cell.theorem_id)
            self.assertEqual(donor.theorem_id, mapping[cell.theorem_id])
            self.assertEqual(donor.generator_role, anchor.generator_role)
            self.assertEqual(donor.generator_config_id, anchor.generator_config_id)
            self.assertEqual(donor.presentation, anchor.presentation)
            self.assertEqual(cell.guidance_sample_id, donor.sample_id)
            self.assertEqual(cell.guidance_text, donor.raw_text)

    def test_codex_g_is_the_only_ineligible_cell_and_has_no_prompt_or_slot(
        self,
    ) -> None:
        ineligible = [cell for cell in self.bundle.cells if not cell.eligible]
        self.assertEqual(len(ineligible), 1)
        cell = ineligible[0]
        self.assertEqual(cell.theorem_id, "G")
        self.assertEqual(cell.condition, Condition.CODEX_REFERENCE_INTUITION.value)
        self.assertEqual(cell.ineligibility_reasons, ("leakage_label_borderline",))
        self.assertNotIn(
            cell.cell_id,
            {prompt.condition_cell_id for prompt in self.bundle.prompts},
        )
        self.assertNotIn(
            cell.cell_id,
            {
                row["condition_cell_id"]
                for row in self.value["execution_plan"]["eligible_cells"]
            },
        )
        self.assertEqual(
            self.value["materialization"]["codex_reference_g"]["disposition"],
            "preserved_ineligible_not_rendered_not_scheduled",
        )

    def test_worker_is_exact_selected_phase5_and_never_phase4(self) -> None:
        run = self.bundle.runs[0].to_dict()
        worker = run["qwen_lean_identity"]
        adapter = worker["adapter"]
        self.assertEqual(
            worker["qwen_lean_source"]["commit"],
            "ef09f5e0f11a54a25fcb95b324d766f675be49a3",
        )
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
        self.assertEqual(
            worker["formal_worker_tokenizer"],
            {
                "tokenizer_id": "Qwen/Qwen3-8B-Base",
                "revision": "49e3418fbbbca6ecbdf9608b4d22e5a407081db4",
                "chat_template": None,
                "add_special_tokens": False,
            },
        )
        self.assertEqual(
            {sample.tokenizer_id for sample in self.bundle.samples},
            {run["tokenizer_identity_id"]},
        )
        self.assertEqual(
            {
                cell.tokenizer_id
                for cell in self.bundle.cells
                if cell.tokenizer_id is not None
            },
            {run["tokenizer_identity_id"]},
        )
        self.assertEqual(run["lean_version"], "v4.32.0")
        self.assertFalse(self.value["gates"]["phase4_checkpoint_used"])
        self.assertFalse(self.value["gates"]["intermediate_phase5_checkpoint_used"])

    def test_run_budget_seeds_sampling_and_submission_order_are_exact(self) -> None:
        run = self.bundle.runs[0]
        settings = run.to_dict()["generation_settings"]
        self.assertEqual(run.seeds, (1, 2, 3, 4))
        self.assertEqual(run.candidate_budget, 16)
        self.assertEqual(settings["candidates_per_seed"], 4)
        self.assertTrue(settings["do_sample"])
        self.assertEqual(settings["temperature"], 0.8)
        self.assertEqual(settings["top_p"], 0.95)
        self.assertEqual(settings["top_k"], -1)
        self.assertEqual(settings["max_new_tokens"], 1024)
        self.assertEqual(settings["max_model_len"], 2048)
        slots = self.value["execution_plan"]["candidate_slot_mapping"]
        self.assertEqual([row["candidate_index"] for row in slots], list(range(16)))
        self.assertEqual([row["candidate_order"] for row in slots], list(range(1, 17)))
        self.assertEqual(
            [row["seed"] for row in slots], [1] * 4 + [2] * 4 + [3] * 4 + [4] * 4
        )
        by_theorem: dict[str, list[str]] = defaultdict(list)
        for row in self.value["execution_plan"]["eligible_cells"]:
            by_theorem[row["theorem_id"]].append(row["logical_condition"])
        expected_primary = self.value["execution_plan"]["logical_condition_order"]
        for theorem_id in "ABCDEF":
            self.assertEqual(by_theorem[theorem_id], expected_primary)
        self.assertEqual(
            by_theorem["G"],
            [
                "no_guidance",
                "factual_control",
                "generic_strategy_control",
                "qwen_base_intuition",
            ],
        )

    def test_every_eligible_prompt_has_exact_parity_and_context_headroom(self) -> None:
        cells = {cell.cell_id: cell for cell in self.bundle.cells}
        prompt_rows = {
            row["condition_cell_id"]: row for row in self.value["prompt_manifest"]
        }
        baseline_by_theorem: dict[str, set[str]] = defaultdict(set)
        for prompt in self.bundle.prompts:
            cell = cells[prompt.condition_cell_id]
            row = prompt_rows[cell.cell_id]
            self.assertTrue(row["non_intervention_bytes_identical"])
            self.assertTrue(row["context_eligible"])
            self.assertLessEqual(row["prompt_token_count"], 1024)
            self.assertEqual(row["prompt_id"], prompt.prompt_id)
            self.assertEqual(row["prompt_hash"], prompt.prompt_hash)
            baseline_by_theorem[cell.theorem_id].add(prompt.baseline_hash)
        self.assertEqual(set(baseline_by_theorem), set("ABCDEFG"))
        self.assertTrue(
            all(len(hashes) == 1 for hashes in baseline_by_theorem.values())
        )
        self.assertEqual(
            min(
                row["prompt_token_count"]
                for row in prompt_rows.values()
                if row["eligible"]
            ),
            81,
        )
        self.assertEqual(
            max(
                row["prompt_token_count"]
                for row in prompt_rows.values()
                if row["eligible"]
            ),
            216,
        )

    def test_baseline_uses_exact_phase5_sft_prompt_without_source_preamble(
        self,
    ) -> None:
        instruction = (
            "/- Complete the proof below.\n"
            "Return only Lean code continuing after `by`; do not use `sorry` or `admit`. -/\n"
        )
        for prompt in self.bundle.prompts:
            baseline = prompt.baseline_bytes.decode("utf-8")
            self.assertTrue(baseline.startswith(instruction))
            self.assertFalse(baseline.startswith("\n"))
            self.assertEqual(baseline.count(instruction), 1)

    def test_scope_gates_forbid_execution_verification_progression_and_merge(
        self,
    ) -> None:
        gates = self.value["gates"]
        self.assertTrue(gates["checkpoint_c_complete"])
        for field in (
            "qwen_lean_inference_performed",
            "lean_verification_performed",
            "gpu_work_performed",
            "historical_B_seed0_draws_opened",
            "candidate_outputs_or_item_level_results_exist",
            "protected_formal_worker_execution_authorized",
            "checkpoint_d_authorized",
            "merge_or_auto_merge_authorized",
        ):
            self.assertFalse(gates[field])

    def test_freeze_and_bundle_tampering_are_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["frozen_at_utc"] = "changed"
        with self.assertRaisesRegex(ValueError, "content id"):
            validate_checkpoint_c(changed)

        changed = copy.deepcopy(self.value)
        changed["gates"]["checkpoint_d_authorized"] = True
        with self.assertRaisesRegex(ValueError, "checkpoint_d_authorized"):
            validate_checkpoint_c(changed)

        bundle_value = json.loads(
            DEFAULT_CHECKPOINT_C_BUNDLE_PATH.read_text(encoding="utf-8")
        )
        bundle_value["candidate_results"].append({})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bundle.json"
            path.write_text(json.dumps(bundle_value), encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_checkpoint_c(self.value, bundle_path=path)

    def test_cli_reports_ready_freeze_but_no_checkpoint_d_authority(self) -> None:
        root = Path(__file__).parents[3]
        result = subprocess.run(
            [sys.executable, "-m", "experiments.intuition_fertility", "checkpoint-c"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        summary = json.loads(result.stdout)
        self.assertEqual(summary["freeze_id"], EXPECTED_CHECKPOINT_C_ID)
        self.assertEqual(summary["condition_cell_count"], 59)
        self.assertEqual(summary["rendered_prompt_count"], 58)
        self.assertEqual(summary["candidate_result_count"], 0)
        self.assertFalse(summary["protected_formal_worker_execution_authorized"])
        self.assertFalse(summary["checkpoint_d_authorized"])


if __name__ == "__main__":
    unittest.main()
