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
    assert set(SHUFFLED_POOL) == {"S1"}

    situations = public["situations"]
    answers = private["answers"]
    assert len(situations) == 20
    assert len({s["id"] for s in situations}) == 20

    total = 0
    witness_tasks = 0
    coordinate_pair_tasks = 0
    clustered_tasks: dict[tuple[str, str], list[tuple[dict[str, object], object]]] = {}

    for situation in situations:
        sid = situation["id"]
        tasks = situation["hidden_tasks"]
        total += len(tasks)
        assert len(tasks) == 4
        assert len({task["type"] for task in tasks}) == 4
        assert set(situation["contexts"]) == EXPECTED_CONTEXTS
        assert situation["shuffled_context_id"] == "S1"

        public_text = json.dumps(situation).lower()
        assert "ground_truth" not in public_text and "correct_answer" not in public_text
        assert {task["id"] for task in tasks} == set(answers[sid])

        lengths = [len(text.split()) for text in situation["contexts"].values()]
        assert max(lengths) <= 1.8 * min(lengths)

        for task in tasks:
            tid = task["id"]
            canonical = answers[sid][tid]["value"]
            assert score_answer(sid, tid, canonical)
            clustered_tasks.setdefault((situation["cluster"], tid), []).append((task, canonical))
            if task["answer_kind"] in {"mul_collision_pair", "crt_collision_pair"}:
                witness_tasks += 1
            if task["answer_kind"] == "int_pair":
                coordinate_pair_tasks += 1

    assert total == 80
    assert witness_tasks == 5
    assert coordinate_pair_tasks == 4

    # Numeric task families need real instance variation, not constant templates.
    # No two scalar families inside a mechanism cluster may have the same answer
    # vector; this catches exact normalized duplicates such as the blocked R T1/T2.
    by_cluster: dict[str, dict[str, list[object]]] = {}
    for (cluster, tid), tasks_and_values in clustered_tasks.items():
        values = [item[1] for item in tasks_and_values]
        by_cluster.setdefault(cluster, {})[tid] = values
        if all(isinstance(value, int) and not isinstance(value, bool) for value in values):
            assert len(set(values)) >= min(3, len(values))

    for cluster, vectors in by_cluster.items():
        scalar_vectors = {
            tid: values
            for tid, values in vectors.items()
            if all(isinstance(value, (int, bool)) for value in values)
        }
        tids = sorted(scalar_vectors)
        for index, left in enumerate(tids):
            for right in tids[index + 1:]:
                assert scalar_vectors[left] != scalar_vectors[right], (cluster, left, right)
                left_values = scalar_vectors[left]
                right_values = scalar_vectors[right]
                if all(isinstance(value, int) and not isinstance(value, bool) for value in left_values) and all(isinstance(value, bool) for value in right_values):
                    assert [value == 1 for value in left_values] != right_values
                if all(isinstance(value, bool) for value in left_values) and all(isinstance(value, int) and not isinstance(value, bool) for value in right_values):
                    assert left_values != [value == 1 for value in right_values]

    # Design-reopen invariants: the three blocked families now probe genuinely
    # different consequences instead of reformatting one theorem.
    for situation in situations:
        task_by_id = {task["id"]: task for task in situation["hidden_tasks"]}
        sid = situation["id"]
        if sid.startswith("R"):
            assert task_by_id["T1"]["type"] == "preimage-count"
            assert task_by_id["T2"]["type"] == "subset-transfer"
            assert task_by_id["T3"]["type"] == "dynamics-transfer"
        if sid.startswith("C"):
            assert task_by_id["T2"]["type"] == "coordinate-operation"
            assert task_by_id["T2"]["answer_kind"] == "int_pair"
            assert task_by_id["T4"]["type"] in {"counterfactual-representation", "coupled-coordinate"}
        if sid.startswith("M"):
            assert task_by_id["T1"]["type"] == "image-size"
            assert task_by_id["T2"]["type"] == "dynamics-diagnosis"
            assert task_by_id["T3"]["type"] == "composition"
            assert task_by_id["T4"]["type"] == "composition-dynamics"

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

    noncanonical = {
        ("R02", "T4"): [16, 19],
        ("R04", "T4"): [17, 25],
        ("R06", "T4"): [22, 25],
        ("R08", "T4"): [36, 43],
        ("C16", "T3"): [25, 37],
    }
    for key, answer in noncanonical.items():
        assert score_answer(*key, answer)

    # Coordinate-pair outputs are canonical ordered coordinates, not an
    # unordered witness; reject swapped values and Boolean/int ambiguity.
    for sid in ("C13", "C14", "C15", "C16"):
        pair = answers[sid]["T2"]["value"]
        assert score_answer(sid, "T2", pair)
        assert not score_answer(sid, "T2", [True, pair[1]])
        if pair[0] != pair[1]:
            assert not score_answer(sid, "T2", list(reversed(pair)))

    print("validated redesigned gold-set-v0: 20 situations / 80 nonredundant hidden tasks / semantic scoring")


if __name__ == "__main__":
    main()
