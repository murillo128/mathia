from __future__ import annotations

from contexts import gcd_context, pool_id


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(9, 84, 30, 2), (10, 91, 26, -2), (11, 144, 54, 3), (12, 221, 52, 5)]
    deltas = {9: 1, 10: 2, 11: 3, 12: 5}
    reconstruction_specs = {
        9: (71, 22, -3),
        10: (109, 31, 4),
        11: (137, 40, -2),
        12: (203, 47, 5),
    }
    two_step_specs = {
        9: (96, 37, 2, -1),
        10: (104, 34, 3, 2),
        11: (150, 57, 2, -2),
        12: (225, 55, 4, 3),
    }
    for i, a, b, q in specs:
        c, d = b, a - q * b
        q2 = q + 2
        c2, d2 = b, a - q2 * b
        delta = deltas[i]
        bad_c, bad_d = b, a - q * b + delta
        hidden_u, hidden_v, hidden_q = reconstruction_specs[i]
        hidden_c, hidden_d = hidden_v, hidden_u - hidden_q * hidden_v
        probe_u, probe_v, probe_q1, probe_q2 = two_step_specs[i]
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
                _task("T3", "representation-transfer", "far", f"An unseen pair (u,v) was transformed by (u,v)->(v,u-qv) with q={hidden_q}, producing ({hidden_c},{hidden_d}). What was u?", "int"),
                _task("T4", "two-step-state", "far", f"Starting from the unseen pair ({probe_u},{probe_v}), apply (u,v)->(v,u-qv) first with q={probe_q1} and then with q={probe_q2}. Return the final ordered pair [u,v].", "int_pair"),
            ],
        })
    return situations
