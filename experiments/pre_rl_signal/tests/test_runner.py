import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from experiments.pre_rl_signal.runner import (
    CONDITIONS,
    ManifestMismatchError,
    ResponseImportError,
    build_oracle_responses,
    build_prompt_records,
    manifest_sha256,
    parse_response,
    read_jsonl,
    render_prompt,
    run_oracle,
    score_imported_responses,
    serialize_jsonl,
    validate_manifest_records,
    write_prompt_manifest,
)


class RunnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = build_prompt_records()
        cls.by_id = {record["prompt_id"]: record for record in cls.records}

    def test_manifest_has_560_unique_ids_and_all_conditions(self):
        self.assertEqual(len(self.records), 560)
        self.assertEqual(len(self.by_id), 560)
        grouped = {}
        for record in self.records:
            key = (record["situation_id"], record["task_id"])
            grouped.setdefault(key, []).append(record["condition"])
        self.assertEqual(len(grouped), 80)
        for conditions in grouped.values():
            self.assertEqual(conditions, list(CONDITIONS))

    def test_none_omits_context_and_other_conditions_are_verbatim(self):
        none = self.by_id["gold-set-v0/R01/T1/none"]["prompt_text"]
        factual = self.by_id["gold-set-v0/R01/T1/factual"]["prompt_text"]
        shuffled = self.by_id["gold-set-v0/R01/T1/shuffled"]["prompt_text"]
        self.assertNotIn("Additional context:\n", none)
        self.assertIn(
            "Additional context:\nThe visible rows show a few values of "
            "multiplication modulo 15;",
            factual,
        )
        self.assertIn(
            "Additional context:\nFor similar triangles, corresponding lengths "
            "scale by one factor",
            shuffled,
        )
        self.assertNotIn("condition", none.lower())

    def test_prompt_uses_only_visible_context_and_task_inputs(self):
        # Exact reconstruction proves metadata labels/IDs/title/answer kind were
        # not added by the wrapper, even where those words occur mathematically.
        from experiments.pre_rl_signal.runner import build_public

        public = build_public()
        situations = {item["id"]: item for item in public["situations"]}
        for record in self.records:
            situation = situations[record["situation_id"]]
            task = next(
                item
                for item in situation["hidden_tasks"]
                if item["id"] == record["task_id"]
            )
            condition = record["condition"]
            context = None
            if condition == "shuffled":
                context = public["shuffled_pool"][situation["shuffled_context_id"]]
            elif condition != "none":
                context = situation["contexts"][condition]
            expected = render_prompt(situation["visible"], task["prompt"], context)
            self.assertEqual(record["prompt_text"], expected)

    def test_manifest_contains_no_private_material(self):
        serialized = serialize_jsonl(self.records).decode("utf-8")
        self.assertNotIn('"ground_truth"', serialized)
        self.assertNotIn('"correct_answer"', serialized)
        self.assertNotIn('"private_truth"', serialized)
        self.assertNotIn('"scorer_params"', serialized)
        self.assertNotIn('"params"', serialized)

    def test_prompts_differ_only_by_optional_context_block(self):
        from experiments.pre_rl_signal.runner import build_public

        public = build_public()
        situation = public["situations"][0]
        task = situation["hidden_tasks"][0]
        none = render_prompt(situation["visible"], task["prompt"])
        for condition in CONDITIONS[1:]:
            if condition == "shuffled":
                context = public["shuffled_pool"][situation["shuffled_context_id"]]
            else:
                context = situation["contexts"][condition]
            contextual = render_prompt(situation["visible"], task["prompt"], context)
            block = f"\n\nAdditional context:\n{context}"
            self.assertEqual(contextual.replace(block, "", 1), none)

    def test_materialization_is_deterministic_and_hashes_exact_text(self):
        rebuilt = build_prompt_records()
        self.assertEqual(serialize_jsonl(self.records), serialize_jsonl(rebuilt))
        self.assertEqual(manifest_sha256(self.records), manifest_sha256(rebuilt))
        for record in self.records:
            expected = hashlib.sha256(record["prompt_text"].encode("utf-8")).hexdigest()
            self.assertEqual(record["prompt_sha256"], expected)

    def test_manifest_validation_allows_reordering_but_rejects_mismatch(self):
        validate_manifest_records(list(reversed(self.records)))
        changed = [dict(record) for record in self.records]
        changed[0]["prompt_text"] += "leak"
        with self.assertRaises(ManifestMismatchError):
            validate_manifest_records(changed)
        private = [dict(record) for record in self.records]
        private[0]["ground_truth"] = 1
        with self.assertRaises(ManifestMismatchError):
            validate_manifest_records(private)

    def test_strict_parser_supported_shapes(self):
        accepted = [
            ("true", "bool", True),
            ("0", "int", 0),
            ("-3", "mod_int", -3),
            ("[1,2]", "int_pair", [1, 2]),
            ("[1,2]", "mul_collision_pair", [1, 2]),
            ("[1,2]", "crt_collision_pair", [1, 2]),
        ]
        for raw, kind, expected in accepted:
            self.assertEqual(parse_response(raw, kind), ("ok", expected))

        for raw, kind, status in [
            ("true", "int", "wrong_shape"),
            ("[true,2]", "int_pair", "wrong_shape"),
            ("[1]", "int_pair", "wrong_shape"),
            ("[1,2,3]", "int_pair", "wrong_shape"),
            ("(1,2)", "int_pair", "invalid_json"),
            ("```json\n1\n```", "int", "invalid_json"),
            ("answer: 1", "int", "invalid_json"),
            ("1 extra", "int", "invalid_json"),
            ("NaN", "int", "invalid_json"),
        ]:
            self.assertEqual(parse_response(raw, kind)[0], status)

    def test_semantic_noncanonical_witnesses_use_existing_scorer(self):
        responses = [
            {
                "prompt_id": "gold-set-v0/R02/T4/none",
                "raw_response": "[16,19]",
            },
            {
                "prompt_id": "gold-set-v0/C16/T3/none",
                "raw_response": "[25,37]",
            },
        ]
        results, summary = score_imported_responses(
            self.records,
            responses,
            model_id="test/model",
            generation_settings={},
            allow_partial=True,
            commit="test-commit",
        )
        self.assertEqual([result["correct"] for result in results], [True, True])
        self.assertEqual(summary["correct_answers"], 2)
        self.assertFalse(summary["complete"])

    def test_unknown_duplicate_missing_and_hash_mismatch_are_rejected(self):
        with self.assertRaises(ResponseImportError) as unknown:
            score_imported_responses(
                self.records,
                [{"prompt_id": "unknown", "raw_response": "1"}],
                model_id="test/model",
                generation_settings={},
                allow_partial=True,
            )
        self.assertEqual(unknown.exception.summary["unknown_prompt_ids"], 1)

        prompt_id = self.records[0]["prompt_id"]
        duplicate = [
            {"prompt_id": prompt_id, "raw_response": "1"},
            {"prompt_id": prompt_id, "raw_response": "1"},
        ]
        with self.assertRaises(ResponseImportError) as duplicate_error:
            score_imported_responses(
                self.records,
                duplicate,
                model_id="test/model",
                generation_settings={},
                allow_partial=True,
            )
        self.assertEqual(duplicate_error.exception.summary["duplicate_prompt_ids"], 1)

        with self.assertRaises(ResponseImportError) as missing:
            score_imported_responses(
                self.records,
                [{"prompt_id": prompt_id, "raw_response": "1"}],
                model_id="test/model",
                generation_settings={},
            )
        self.assertEqual(missing.exception.summary["missing_responses"], 559)

        with self.assertRaises(ResponseImportError) as mismatch:
            score_imported_responses(
                self.records,
                [
                    {
                        "prompt_id": prompt_id,
                        "raw_response": "1",
                        "prompt_sha256": "0" * 64,
                    }
                ],
                model_id="test/model",
                generation_settings={},
                allow_partial=True,
            )
        self.assertEqual(mismatch.exception.summary["manifest_mismatches"], 1)

        with self.assertRaises(ResponseImportError) as missing_raw:
            score_imported_responses(
                self.records,
                [{"prompt_id": prompt_id}],
                model_id="test/model",
                generation_settings={},
                allow_partial=True,
            )
        self.assertEqual(missing_raw.exception.summary["invalid_response_records"], 1)

    def test_complete_oracle_run_is_explicit_and_scores_560(self):
        results, summary = run_oracle(self.records, commit="test-commit")
        self.assertEqual(len(results), 560)
        self.assertEqual(summary["imported_responses"], 560)
        self.assertEqual(summary["parsed_successfully"], 560)
        self.assertEqual(summary["parse_failures"], 0)
        self.assertEqual(summary["correct_answers"], 560)
        self.assertTrue(summary["complete"])
        self.assertTrue(summary["synthetic_oracle"])
        self.assertTrue(all(result["model_id"] == "synthetic/oracle" for result in results))

    def test_mixed_import_separates_format_and_math_failures(self):
        oracle = {
            response["prompt_id"]: response
            for response in build_oracle_responses(self.records)
        }
        prompt_ids = [
            "gold-set-v0/R01/T1/none",
            "gold-set-v0/R01/T1/factual",
            "gold-set-v0/R01/T1/procedural",
            "gold-set-v0/R01/T1/structural",
        ]
        responses = [
            oracle[prompt_ids[0]],
            {"prompt_id": prompt_ids[1], "raw_response": "999999"},
            {"prompt_id": prompt_ids[2], "raw_response": "not JSON"},
            {"prompt_id": prompt_ids[3], "raw_response": "true"},
        ]
        results, summary = score_imported_responses(
            self.records,
            responses,
            model_id="test/model",
            model_revision="revision",
            generation_settings={"temperature": 0},
            allow_partial=True,
            commit="test-commit",
        )
        self.assertEqual(len(results), 4)
        self.assertEqual(summary["correct_answers"], 1)
        self.assertEqual(summary["incorrect_answers"], 3)
        self.assertEqual(summary["parse_failures"], 2)
        self.assertEqual(summary["invalid_json"], 1)
        self.assertEqual(summary["wrong_shape"], 1)
        self.assertEqual(results[-1]["parse_status"], "wrong_shape")
        self.assertNotIn("parsed_answer", results[-1])

    def test_import_metadata_and_run_provenance_are_retained(self):
        response = {
            "prompt_id": "gold-set-v0/R01/T1/none",
            "raw_response": "1",
            "provider": {"request_id": "abc"},
        }
        results, _ = score_imported_responses(
            self.records,
            [response],
            model_id="provider/model",
            model_revision="rev-1",
            generation_settings={"temperature": 0},
            allow_partial=True,
            commit="test-commit",
        )
        result = results[0]
        self.assertEqual(result["repository_commit"], "test-commit")
        self.assertEqual(result["manifest_sha256"], manifest_sha256(self.records))
        self.assertEqual(result["model_revision"], "rev-1")
        self.assertEqual(result["import_metadata"], {"provider": {"request_id": "abc"}})

    def test_prompt_manifest_file_has_sidecar_and_no_oracle_answers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "prompts.jsonl"
            metadata = write_prompt_manifest(path, self.records)
            loaded = read_jsonl(path)
            sidecar = json.loads(
                Path(str(path) + ".meta.json").read_text(encoding="utf-8")
            )
            self.assertEqual(loaded, self.records)
            self.assertEqual(metadata, sidecar)
            self.assertEqual(sidecar["prompt_count"], 560)
            self.assertEqual(sidecar["manifest_sha256"], manifest_sha256(self.records))
            self.assertNotIn("raw_response", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
