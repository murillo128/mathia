from __future__ import annotations

import json

from contexts import SHUFFLED_POOL
from private_truth import build_private
from public_fixtures import build_public
from scoring import score_answer

EXPECTED_CONTEXTS = {"factual", "procedural", "structural", "sterile", "wrong"}


def main() -> None:
    public = build_public()
    private = build_private()
    assert public["version"] == private["version"] == "gold-set-v0"
    assert public["shuffled_pool"] == SHUFFLED_POOL

    situations = public["situations"]
    answers = private["answers"]
    assert len(situations) == 20
    ids = {s["id"] for s in situations}
    assert len(ids) == 20

    total = 0
    witness_tasks = 0
    clustered_tasks: dict[tuple[str, str], list[tuple[dict[str, object], object]]] = {}
    for situation in situations:
        sid = situation["id"]
        total += len(situation["hidden_tasks"])
        assert set(situation["contexts"]) == EXPECTED_CONTEXTS
        assert situation["shuffled_context_id"] in SHUFFLED_POOL

        public_text = json.dumps(situation).lower()
        assert "ground_truth" not in public_text and "correct_answer" not in public_text
        assert {t["id"] for t in situation["hidden_tasks"]} == set(answers[sid])

        lengths = [len(text.split()) for text in situation["contexts"].values()]
        assert max(lengths) <= 1.8 * min(lengths)

        for task in situation["hidden_tasks"]:
            tid = task["id"]
            canonical = answers[sid][tid]["value"]
            assert score_answer(sid, tid, canonical)
            clustered_tasks.setdefault((situation["cluster"], tid), []).append((task, canonical))
            if task["answer_kind"] in {"mul_collision_pair", "crt_collision_pair"}:
                witness_tasks += 1

    assert total == 80
    assert witness_tasks == 5

    # Repeated general prompts must not carry one deterministic answer, and
    # Boolean task templates must vary within a cluster. These checks prevent
    # the theorem-restatement/constant-answer ceiling defect found in cycle 1.
    for tasks_and_values in clustered_tasks.values():
        tasks = [item[0] for item in tasks_and_values]
        serialized_values = {json.dumps(item[1], sort_keys=True) for item in tasks_and_values}
        if len({task["prompt"] for task in tasks}) == 1:
            assert len(serialized_values) > 1
        if len(tasks) > 1 and all(task["answer_kind"] == "bool" for task in tasks):
            assert len(serialized_values) > 1

    old_direct_conclusions = (
        "requiring a nonnegative remainder",
        "changing only the translation term",
        "would uniqueness modulo the product still be guaranteed",
    )
    for situation in situations:
        for task in situation["hidden_tasks"]:
            prompt = task["prompt"].lower()
            assert not any(fragment in prompt for fragment in old_direct_conclusions)

    # Coprime CRT reconstruction targets must not all encode one recognizable
    # fixed offset such as x = mn - 2.
    crt_offsets = {
        situation["visible"]["domain_size"] - answers[situation["id"]]["T3"]["value"]
        for situation in situations
        if situation["id"] in {"C13", "C14", "C15"}
    }
    assert len(crt_offsets) == 3

    alternatives = {
        ("R02", "T4"): [1, 4],
        ("R04", "T4"): [1, 9],
        ("R06", "T4"): [1, 4],
        ("R08", "T4"): [1, 8],
        ("C16", "T3"): [1, 13],
    }
    for key, answer in alternatives.items():
        assert score_answer(*key, answer)
        assert score_answer(*key, list(reversed(answer)))
        assert not score_answer(*key, [True, answer[1]])
        assert not score_answer(*key, [answer[1], True])

    for key, answer in {
        ("R02", "T4"): [0, 3],
        ("R04", "T4"): [0, 8],
        ("R06", "T4"): [0, 3],
        ("R08", "T4"): [0, 7],
        ("C16", "T3"): [0, 12],
    }.items():
        assert not score_answer(*key, [False, answer[1]])
        assert not score_answer(*key, [answer[1], False])

    noncanonical = {
        ("R02", "T4"): [16, 19],  # [1,4] modulo 15
        ("R04", "T4"): [17, 25],  # [1,9] modulo 16
        ("R06", "T4"): [22, 25],  # [1,4] modulo 21
        ("R08", "T4"): [36, 43],  # [1,8] modulo 35
        ("C16", "T3"): [25, 37],  # [1,13] modulo 24
    }
    for key, answer in noncanonical.items():
        assert score_answer(*key, answer)

    for sid in ("M17", "M18", "M19", "M20"):
        value = answers[sid]["T3"]["value"]
        modulus = answers[sid]["T3"]["params"]["modulus"]
        assert score_answer(sid, "T3", value + modulus)
        assert score_answer(sid, "T3", value - modulus)
        assert not score_answer(sid, "T3", True)

    print("validated corrected gold-set-v0: 20 situations / 80 hidden tasks / semantic witness scoring")


if __name__ == "__main__":
    main()
