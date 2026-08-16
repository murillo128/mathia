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
            if task["answer_kind"] in {"mul_collision_pair", "crt_collision_pair"}:
                witness_tasks += 1

    assert total == 80
    assert witness_tasks == 5

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

    print("validated corrected gold-set-v0: 20 situations / 80 hidden tasks / semantic witness scoring")


if __name__ == "__main__":
    main()
