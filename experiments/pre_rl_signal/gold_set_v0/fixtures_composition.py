from __future__ import annotations

from contexts import composition_context, pool_id


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(17, 12, 5, 2, 6, 0), (18, 15, 6, 5, 10, 1), (19, 20, 3, 0, 7, 1), (20, 18, 5, 1, 9, 1)]
    for i, n, a, b, c, d in specs:
        situations.append({
            "id": f"M{i:02d}",
            "cluster": "composition",
            "title": f"Composition, information loss, and dynamics mod {n}",
            "visible": {
                "statement": f"On residues modulo {n}, compare f(x)={a}x+{b} and g(x)={c}x+{d}.",
            },
            "contexts": composition_context(),
            "shuffled_context_id": pool_id(i),
            "hidden_tasks": [
                _task("T1", "image-size", "near", "How many distinct outputs does f have over all residue classes?", "int"),
                _task("T2", "dynamics-diagnosis", "medium", "How many fixed points does f have modulo the given modulus?", "int"),
                _task("T3", "composition", "medium", "How many distinct outputs does g∘f have over all residue classes?", "int"),
                _task("T4", "composition-dynamics", "far", "How many fixed points does g∘f have modulo the given modulus?", "int"),
            ],
        })
    return situations
