from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from experiments.qwen_mathia_v1.core import (
    IGNORE_INDEX,
    QwenMathiaConfig,
    load_selected_records,
    split_canonical_rendering,
    tokenize_record,
    verify_frozen_release,
)
from experiments.qwen_mathia_v1.runtime import _license_audit


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "experiments" / "qwen_mathia_v1" / "config.json"


class CharacterTokenizer:
    eos_token_id = 0
    pad_token_id = 0
    name_or_path = "character-tokenizer-test-double"

    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        if add_special_tokens:
            raise AssertionError("special tokens must remain disabled")
        return [ord(character) + 1 for character in text]

    def decode(
        self,
        ids: list[int],
        *,
        skip_special_tokens: bool,
        clean_up_tokenization_spaces: bool,
    ) -> str:
        return "".join(chr(item - 1) for item in ids)


class QwenMathiaV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = QwenMathiaConfig.load(CONFIG)
        cls.records, cls.by_id, cls.audit = load_selected_records(cls.config)

    def test_frozen_release_and_config_match_issue_47(self) -> None:
        identity = verify_frozen_release(self.config)
        self.assertEqual(identity["release_id"], "agnostic-mathia-full-v1")
        self.assertEqual(
            identity["freeze_id"],
            "freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f",
        )
        self.assertEqual(self.config.training["maximum_sequence_tokens"], 768)
        self.assertFalse(self.config.training["truncation"])

    def test_optimizer_workload_contains_only_conceptual_derivatives(self) -> None:
        counts = self.audit["selected_role_counts"]
        self.assertEqual(counts, {"interpretation": 98, "synthesis": 18})
        self.assertEqual(len(self.records), 116)
        self.assertEqual(self.audit["excluded_or_evaluation_objects_selected"], 0)
        self.assertEqual(self.audit["source_objects_selected_as_standalone_targets"], 0)
        self.assertEqual(self.audit["riemann_objects_selected"], 0)
        self.assertEqual(
            [record["object_id"] for record in self.records],
            sorted(record["object_id"] for record in self.records),
        )

    def test_boundary_reuses_canonical_renderer_and_masks_only_prompt(self) -> None:
        record = self.records[0]
        prompt, response, rendered = split_canonical_rendering(record, self.by_id)
        self.assertEqual(prompt + response, rendered)
        self.assertTrue(prompt.endswith("## Response\n\n"))
        example = tokenize_record(
            record,
            self.by_id,
            CharacterTokenizer(),
            maximum_sequence_tokens=len(rendered) + 1,
        )
        self.assertEqual(
            example.labels[: example.prompt_tokens],
            (IGNORE_INDEX,) * example.prompt_tokens,
        )
        self.assertNotIn(IGNORE_INDEX, example.labels[example.prompt_tokens :])
        self.assertEqual(example.labels[-1], CharacterTokenizer.eos_token_id)
        self.assertEqual(example.total_tokens, len(rendered) + 1)

    def test_truncation_is_a_hard_failure(self) -> None:
        record = self.records[0]
        with self.assertRaisesRegex(ValueError, "truncation is forbidden"):
            tokenize_record(record, self.by_id, CharacterTokenizer(), 1)

    def test_private_provenance_and_quality_audit_do_not_change_visible_bytes(
        self,
    ) -> None:
        record = next(
            item for item in self.records if item["object_role"] == "interpretation"
        )
        original = split_canonical_rendering(record, self.by_id)[2]
        changed = copy.deepcopy(record)
        changed["teacher_provenance"] = {"kind": "private-counterfactual"}
        changed["span_lineage"] = [{"private": "counterfactual"}]
        changed["derivation_ids"] = ["private-counterfactual"]
        changed["licensing_boundary"] = "private-counterfactual"
        changed["corpus_local_audit"] = {"quality": "private-counterfactual"}
        changed["corpus_origin"] = "private-counterfactual"
        changed["corpus_release_id"] = "private-counterfactual"
        observed = split_canonical_rendering(changed, self.by_id)[2]
        self.assertEqual(original.encode("utf-8"), observed.encode("utf-8"))

    def test_config_is_canonical_json_serializable_without_secrets(self) -> None:
        rendered = json.dumps(self.config.value, sort_keys=True)
        self.assertNotIn("hf_token", rendered.casefold())
        self.assertNotIn("access_token", rendered.casefold())
        self.assertNotIn("/root", rendered)

    def test_publication_license_does_not_overclaim_apache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            model_card = Path(directory) / "README.md"
            model_card.write_text("---\nlicense: apache-2.0\n---\n", encoding="utf-8")
            audit = _license_audit(self.config, model_card)
        self.assertEqual(audit["upstream_base"]["reported_license"], "apache-2.0")
        self.assertEqual(audit["hub_license_field"], "other")
        self.assertFalse(audit["global_corpus_license_granted"])
        self.assertIn("CC-BY-NC-SA-4.0", audit["source_license_identifiers"])
        self.assertIn(
            "source-linked-original-analysis-no-license-grant",
            audit["source_license_identifiers"],
        )


if __name__ == "__main__":
    unittest.main()
