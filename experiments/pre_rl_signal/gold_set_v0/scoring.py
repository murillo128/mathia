from __future__ import annotations

from typing import Any

from private_truth import build_private
from public_fixtures import build_public


def _task_index() -> dict[tuple[str, str], dict[str, Any]]:
    index: dict[tuple[str, str], dict[str, Any]] = {}
    for situation in build_public()["situations"]:
        for task in situation["hidden_tasks"]:
            index[(situation["id"], task["id"])] = task
    return index


def score_answer(situation_id: str, task_id: str, answer: Any) -> bool:
    task = _task_index()[(situation_id, task_id)]
    truth = build_private()["answers"][situation_id][task_id]
    kind = task["answer_kind"]
    value = truth["value"]
    params = truth["params"]

    if kind == "bool":
        return isinstance(answer, bool) and answer is value
    if kind == "int":
        return isinstance(answer, int) and not isinstance(answer, bool) and answer == value
    if kind == "int_pair":
        return (
            isinstance(answer, (list, tuple))
            and len(answer) == 2
            and all(isinstance(item, int) and not isinstance(item, bool) for item in answer)
            and list(answer) == value
        )
    if kind == "mod_int":
        return (
            isinstance(answer, int)
            and not isinstance(answer, bool)
            and (answer - value) % params["modulus"] == 0
        )
    if kind == "mul_collision_pair":
        if not (isinstance(answer, (list, tuple)) and len(answer) == 2):
            return False
        x, y = answer
        if not (
            isinstance(x, int)
            and not isinstance(x, bool)
            and isinstance(y, int)
            and not isinstance(y, bool)
        ):
            return False
        a, n = params["a"], params["n"]
        return x % n != y % n and (a * x - a * y) % n == 0
    if kind == "crt_collision_pair":
        if not (isinstance(answer, (list, tuple)) and len(answer) == 2):
            return False
        x, y = answer
        if not (
            isinstance(x, int)
            and not isinstance(x, bool)
            and isinstance(y, int)
            and not isinstance(y, bool)
        ):
            return False
        m, n = params["m"], params["n"]
        modulus = m * n
        return x % modulus != y % modulus and x % m == y % m and x % n == y % n
    raise ValueError(f"unsupported answer kind: {kind}")
