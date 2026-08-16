from __future__ import annotations

from contexts import composition_context, pool_id


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(17, 12, 5, 2, 7, 0), (18, 15, 6, 5, 4, 1), (19, 20, 3, 0, 7, 0), (20, 18, 5, 1, 6, 4)]
    alternate_multipliers = {17: 6, 18: 5, 19: 4, 20: 3}
    for i, n, a, b, c, d in specs:
        alternate_a = alternate_multipliers[i]
        situations.append({
            "id": f"M{i:02d}",
            "cluster": "composition",
            "title": f"Composition and affine information loss mod {n}",
            "visible": {
                "statement": f"On residues modulo {n}, compare f(x)={a}x+{b} and g(x)={c}x+{d}.",
            },
            "contexts": composition_context(),
            "shuffled_context_id": pool_id(i),
            "hidden_tasks": [
                _task("T1", "prediction", "near", "How many distinct outputs does f have over all residue classes?", "int"),
                _task("T2", "transfer", "medium", "How many distinct outputs does g have over all residue classes?", "int"),
                _task("T3", "composition", "medium", f"What is the coefficient of x in the affine formula for g∘f modulo {n}?", "mod_int"),
                _task("T4", "counterfactual", "far", f"If f's multiplier were replaced by {alternate_a} while its translation stayed {b}, how many distinct outputs would g∘f have over all residue classes modulo {n}?", "int"),
            ],
        })
    return situations
