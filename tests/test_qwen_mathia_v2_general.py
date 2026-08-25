from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any, Mapping, Sequence

from experiments.mathia_corpus import interchange
from experiments.qwen_mathia_v2_general.core import (
    ASSISTANT_END_TEXT,
    BASE_REVISION,
    EXPECTED_LORA_MODULE_COUNTS,
    IGNORE_INDEX,
    LORA_TARGET_REGEX,
    Candidate,
    DesignConfig,
    ParentRelease,
    canonical_json,
    sha256_file,
    sha256_text,
    tokenize_candidate,
)


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "experiments" / "qwen_mathia_v2_general"
CONFIG = PACKAGE / "config.json"
MANIFEST = PACKAGE / "training_manifest.json"
DEDUPE = PACKAGE / "evidence" / "dedupe_report.json"
ARCHITECTURE = PACKAGE / "evidence" / "architecture_audit.json"


class OfficialTemplateCharacterTokenizer:
    eos_token_id = 1
    pad_token_id = 1
    chat_template = "official-template-test-double"
    _end_id = 2

    def _render(self, messages: Sequence[Mapping[str, str]], add_generation_prompt: bool) -> str:
        rendered = ""
        for message in messages:
            if message["role"] == "user":
                rendered += f"<|im_start|>user\n{message['content']}<|im_end|>\n"
            elif message["role"] == "assistant":
                rendered += (
                    "<|im_start|>assistant\n<think>\n\n</think>\n\n"
                    + message["content"]
                    + ASSISTANT_END_TEXT
                )
            else:
                raise AssertionError("unexpected role")
        if add_generation_prompt:
            rendered += "<|im_start|>assistant\n<think>\n\n</think>\n\n"
        return rendered

    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        if add_special_tokens:
            raise AssertionError("special-token insertion must stay disabled")
        ids: list[int] = []
        index = 0
        while index < len(text):
            if text.startswith("<|im_end|>", index):
                ids.append(self._end_id)
                index += len("<|im_end|>")
            else:
                ids.append(ord(text[index]) + 1000)
                index += 1
        return ids

    def decode(
        self,
        ids: Sequence[int],
        *,
        skip_special_tokens: bool,
        clean_up_tokenization_spaces: bool,
    ) -> str:
        if skip_special_tokens or clean_up_tokenization_spaces:
            raise AssertionError("audit decode must preserve exact bytes")
        return "".join("<|im_end|>" if item == self._end_id else chr(item - 1000) for item in ids)

    def apply_chat_template(self, messages: Sequence[Mapping[str, str]], **kwargs: Any) -> Any:
        if kwargs.get("enable_thinking") is not False:
            raise AssertionError("thinking must be disabled deterministically")
        rendered = self._render(messages, bool(kwargs.get("add_generation_prompt")))
        if kwargs.get("tokenize"):
            return {"input_ids": self.encode(rendered, add_special_tokens=False)}
        return rendered

    def convert_tokens_to_ids(self, token: str) -> int:
        if token != "<|im_end|>":
            raise AssertionError("unexpected control token")
        return self._end_id


def _record(role: str, content: str, parents: list[str]) -> dict[str, Any]:
    content_hash = interchange.sha256_text(content)
    keys = ["source:test"]
    return {
        "contract_version": interchange.CONTRACT_VERSION,
        "corpus_release_id": "test-release",
        "object_id": interchange.stable_object_id(role, content_hash, keys, parents),
        "object_role": role,
        "corpus_origin": "agnostic",
        "source_ids": ["test-source"],
        "source_unit_ids": ["test-unit"],
        "span_lineage": [],
        "content_sha256": content_hash,
        "content": content,
        "parent_ids": parents,
        "derivation_ids": ["test"],
        "teacher_provenance": {"kind": "test"},
        "quality_state": "accepted",
        "training_eligibility": "eligible",
        "exclusion_reason": None,
        "licensing_boundary": "test-only",
        "representation_dependencies": [],
        "canonical_source_keys": keys,
    }


class QwenMathiaV2GeneralTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = DesignConfig.load(CONFIG)
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.dedupe = json.loads(DEDUPE.read_text(encoding="utf-8"))
        cls.architecture = json.loads(ARCHITECTURE.read_text(encoding="utf-8"))

    def test_parent_bindings_match_frozen_repository_files(self) -> None:
        for parent in self.config.corpus["parents"]:
            root = ROOT / parent["root"]
            for relative, wanted in parent["frozen_files"].items():
                self.assertEqual(sha256_file(root / relative), wanted)
        self.assertEqual(
            [parent["freeze_id"] for parent in self.config.corpus["parents"]],
            [
                "freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f",
                "agnostic_openalex_supplement_a1aa591df034db64d5ce0271df0da570e3aaf470ac49e5cc4014b66181bf0e33",
            ],
        )

    def test_g_v2_selection_is_general_only_and_target_only(self) -> None:
        audit = self.manifest["selection_audit"]
        self.assertEqual(audit["input_candidates"], 411)
        self.assertEqual(audit["selected_optimizer_targets"], 411)
        self.assertEqual(
            audit["selected_counts_by_parent_and_role"],
            {
                "agnostic-mathia-full-v1|interpretation": 98,
                "agnostic-mathia-full-v1|synthesis": 18,
                "agnostic-mathia-openalex-supplement-v1|interpretation": 295,
            },
        )
        self.assertEqual(audit["dedupe_dropped"], 0)
        self.assertEqual(audit["source_objects_selected_as_standalone_targets"], 0)
        self.assertEqual(audit["rejected_quarantined_or_evaluation_only_selected"], 0)
        self.assertEqual(audit["riemann_release_or_origin_objects_selected"], 0)
        rows = self.manifest["examples"]
        self.assertEqual(len(rows), 411)
        self.assertEqual(
            [row["object_id"] for row in rows],
            sorted(row["object_id"] for row in rows),
        )
        self.assertTrue(all(row["object_role"] in {"interpretation", "synthesis"} for row in rows))
        self.assertTrue(all(row["quality_state"] == "accepted" for row in rows))
        self.assertTrue(all(row["training_eligibility"] == "eligible" for row in rows))
        self.assertTrue(
            all(
                row["parent_release_id"]
                in {"agnostic-mathia-full-v1", "agnostic-mathia-openalex-supplement-v1"}
                for row in rows
            )
        )

    def test_dedupe_is_auditable_and_near_duplicates_do_not_delete(self) -> None:
        self.assertEqual(self.dedupe["input_candidate_count"], 411)
        self.assertEqual(self.dedupe["retained_count"], 411)
        self.assertEqual(self.dedupe["dropped"], [])
        self.assertEqual(self.dedupe["duplicate_identity_groups"], [])
        self.assertEqual(self.dedupe["duplicate_content_and_lineage_groups"], [])
        diagnostic = self.dedupe["near_duplicate_diagnostic"]
        self.assertFalse(diagnostic["automatic_deletion"])
        self.assertEqual(diagnostic["threshold"], 0.8)
        self.assertEqual(diagnostic["pair_count"], len(diagnostic["pairs"]))
        value = dict(self.dedupe)
        identifier = value.pop("dedupe_report_id")
        self.assertEqual(identifier, "g_v2_dedupe_" + sha256_text(canonical_json(value)))

    def test_official_template_boundary_masks_the_assistant_prefix(self) -> None:
        source = _record("source", "Let X be an object with a reversible map.", [])
        target = _record(
            "interpretation",
            "The key mechanism is reversibility rather than a coordinate choice.",
            [source["object_id"]],
        )
        records = {source["object_id"]: source, target["object_id"]: target}
        parent = ParentRelease(
            release_id="test-release",
            root=Path("."),
            records_path=Path("records.jsonl"),
            records=(source, target),
            by_id=records,
            loader=lambda record: str(record["content"]),
            rank=0,
        )
        candidate = Candidate(parent, target, "0" * 64)
        tokenizer = OfficialTemplateCharacterTokenizer()
        observed = tokenize_candidate(candidate, tokenizer, maximum_sequence_tokens=4096)
        self.assertTrue(observed.prompt_text.endswith("<think>\n\n</think>\n\n"))
        self.assertEqual(observed.supervised_text, target["content"] + ASSISTANT_END_TEXT)
        self.assertEqual(
            observed.labels[: observed.prompt_tokens],
            (IGNORE_INDEX,) * observed.prompt_tokens,
        )
        self.assertNotIn(IGNORE_INDEX, observed.labels[observed.prompt_tokens :])
        self.assertEqual(observed.assistant_end_tokens, 2)
        with self.assertRaisesRegex(ValueError, "truncation is forbidden"):
            tokenize_candidate(candidate, tokenizer, maximum_sequence_tokens=1)

    def test_token_audit_freezes_no_truncation_and_exact_exposure(self) -> None:
        bound = self.manifest["sequence_bound"]
        self.assertEqual(bound["true_maximum_sequence_tokens"], 9429)
        self.assertEqual(bound["smallest_clean_bound"], 9472)
        self.assertEqual(bound["configured_maximum_sequence_tokens"], 9472)
        self.assertEqual(bound["truncated_examples"], 0)
        totals = self.manifest["one_unique_corpus_pass"]
        self.assertEqual(totals["examples"], 411)
        self.assertEqual(totals["prompt_tokens"], 556227)
        self.assertEqual(totals["supervised_tokens"], 37957)
        self.assertEqual(totals["all_tokens"], 594184)
        exposure = self.manifest["exposure_plan"]
        self.assertEqual(exposure["optimizer_steps"], 52)
        self.assertEqual(exposure["final_partial_accumulation_microbatches"], 3)
        self.assertEqual(
            [(item["requested_epoch_fraction"], item["optimizer_step"]) for item in exposure["checkpoints"]],
            [(0.25, 13), (0.5, 26), (1.0, 52)],
        )
        self.assertEqual(exposure["checkpoints"][-1]["token_presentations"]["supervised_tokens"], 37957)
        for group in self.manifest["token_statistics"]["by_parent_and_role"].values():
            for metric in ("prompt_tokens", "supervised_tokens", "total_tokens"):
                self.assertLessEqual(group[metric]["p50"], group[metric]["p90"])
                self.assertLessEqual(group[metric]["p90"], group[metric]["p95"])
                self.assertLessEqual(group[metric]["p95"], group[metric]["p99"])
                self.assertLessEqual(group[metric]["p99"], group[metric]["maximum"])
                self.assertTrue(group[metric]["longest_object_ids"])

    def test_manifest_preserves_hash_lineage_without_restricted_source_text(self) -> None:
        for row in self.manifest["examples"]:
            self.assertNotIn("content", row)
            self.assertNotIn("rendered_text", row)
            self.assertRegex(row["original_record_sha256"], r"^[0-9a-f]{64}$")
            self.assertRegex(row["lineage_sha256"], r"^[0-9a-f]{64}$")
            self.assertTrue(row["source_ancestors"])
            self.assertEqual(row["assistant_end_tokens"], 2)
            self.assertEqual(row["loss_mask"]["masked_prompt_range"][1], row["prompt_tokens"])
            self.assertEqual(row["loss_mask"]["supervised_assistant_end_range"][1], row["total_tokens"])

    def test_qwen35_architecture_and_peft_boundary_are_exact(self) -> None:
        audit = self.architecture
        self.assertEqual(audit["model"]["model_revision"], BASE_REVISION)
        self.assertTrue(audit["model"]["text_only_training_path"])
        self.assertEqual(audit["model"]["vision_modules_present_in_training_model"], 0)
        self.assertEqual(audit["model"]["base_parameter_count"], 4_841_450_496)
        self.assertEqual(audit["model"]["peft_wrapped_total_parameter_count"], 4_873_915_392)
        lora = audit["lora"]
        self.assertEqual(lora["target_regex"], LORA_TARGET_REGEX)
        self.assertEqual(lora["matched_module_count"], 248)
        self.assertEqual(lora["module_counts_by_suffix"], EXPECTED_LORA_MODULE_COUNTS)
        self.assertEqual(lora["adapter_trainable_parameter_count"], 32_464_896)
        self.assertEqual(lora["adapter_parameter_tensor_count"], 496)
        self.assertEqual(lora["vision_modules_matched"], 0)
        pattern = re.compile(LORA_TARGET_REGEX)
        self.assertTrue(all(pattern.fullmatch(item["path"]) for item in lora["matched_modules"]))
        self.assertFalse(
            any(
                token in item["path"]
                for item in lora["matched_modules"]
                for token in ("vision", "visual", "embed", "norm", "lm_head")
            )
        )
        self.assertTrue(audit["compatibility"]["peft_adapter_attached"])
        self.assertTrue(audit["compatibility"]["bitsandbytes_nf4_config_constructed"])
        self.assertFalse(audit["compatibility"]["gpu_forward_backward_or_memory_claimed"])

    def test_freeze_ids_and_config_are_content_bound_and_secret_free(self) -> None:
        manifest = dict(self.manifest)
        freeze_id = manifest.pop("g_v2_freeze_id")
        self.assertEqual(freeze_id, "g_v2_" + sha256_text(canonical_json(manifest)))
        architecture = dict(self.architecture)
        architecture_id = architecture.pop("architecture_audit_id")
        self.assertEqual(
            architecture_id,
            "qwen35_4b_architecture_" + sha256_text(canonical_json(architecture)),
        )
        serialized = json.dumps(self.config.value, sort_keys=True).casefold()
        for forbidden in ("hf_token", "access_token", "/root", "/workspace/mathia-artifacts"):
            self.assertNotIn(forbidden, serialized)
        self.assertEqual(self.manifest["config_sha256"], self.config.config_sha256)
        self.assertEqual(self.architecture["config_sha256"], self.config.config_sha256)
        self.assertEqual(
            self.manifest["implementation"]["qwen_mathia_v2_general_core_sha256"],
            sha256_file(PACKAGE / "core.py"),
        )
        self.assertEqual(
            self.architecture["implementation_core_sha256"],
            sha256_file(PACKAGE / "core.py"),
        )

    def test_scope_stops_before_gpu_training_and_scientific_validation(self) -> None:
        self.assertEqual(self.config.value["exit_decision"], "QWEN_MATHIA_V2_GENERAL_DESIGN_READY")
        self.assertFalse(self.config.value["publication"]["scientific_capability_claim_authorized"])
        self.assertFalse(self.config.value["publication"]["publish_merged_weights"])
        self.assertFalse(self.config.value["downstream_handoff"]["executed_here"])
        self.assertEqual(self.config.value["downstream_handoff"]["riemann_specialization"], "out of scope")


if __name__ == "__main__":
    unittest.main()
