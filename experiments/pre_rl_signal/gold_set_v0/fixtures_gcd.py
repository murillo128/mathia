from __future__ import annotations

from contexts import gcd_context, pool_id


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(9, 84, 30, 2), (10, 91, 26, -2), (11, 144, 54, 3), (12, 221, 52, 5)]
    deltas = {9: 1, 10: 2, 11: 3, 12: 5}
    for i, a, b, q in specs:
        c, d = b, a - q * b
        q2 = q + 2
        c2, d2 = b, a - q2 * b
        delta = deltas[i]
        bad_c, bad_d = b, a - q * b + delta
        situations.append({
            "id": f"G{i:02d}",
            "cluster": "gcd_invariance",
            "title": f"Preserving common-divisor information {i}",
            "visible": {
                "statement": f"Compare the pair ({a},{b}) with ({c},{d}), obtained by (a,b)->(b,a-qb) using q={q}.",
                "before_pair": [a, b],
                "after_pair": [c, d],
            },
            "contexts": gcd_context(),
            "shuffled_context_id": pool_id(i),
            "hidden_tasks": [
                _task("T1", "prediction", "medium", f"With q changed to {q2}, the transformed pair is ({c2},{d2}). What is its gcd?", "int"),
                _task("T2", "counterfactual", "medium", f"Perturb the rule by +{delta}, giving ({bad_c},{bad_d}). What is the gcd of this perturbed pair?", "int"),
                _task("T3", "diagnosis", "far", "Is requiring a nonnegative remainder smaller than |b| essential for the transformation (a,b)->(b,a-qb) to preserve gcd? Answer true/false.", "bool"),
                _task("T4", "transfer", "far", f"If the original pair is first swapped to ({b},{a}) and then transformed as (u,v)->(v,u-{q2}v), must the gcd still equal that of ({a},{b})? Answer true/false.", "bool"),
            ],
        })
    return situations
