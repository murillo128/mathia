from __future__ import annotations

import math

from contexts import pool_id, rev_context


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def _sample_mul(a: int, n: int) -> list[list[int]]:
    return [[x, (a * x) % n] for x in (0, 1, 2)]


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(1, 15, 4), (2, 15, 5), (3, 16, 3), (4, 16, 6), (5, 21, 8), (6, 21, 7), (7, 35, 12), (8, 35, 10)]
    for i, n, a in specs:
        unit = math.gcd(a, n) == 1
        b = (i * 3 + 1) % n
        target = (i * 5 + 2) % n
        alt_a = (a + i + 1) % n or 1
        tasks = [
            _task("T1", "prediction", "near", f"How many residue classes x modulo {n} solve {a}x ≡ {target} (mod {n})?", "int"),
            _task("T2", "representation-transfer", "far", f"In the functional graph of x -> {a}x mod {n}, is every vertex already on a directed cycle, with no transient tail? Answer true/false.", "bool"),
            _task("T3", "counterfactual", "medium", f"How many distinct outputs does x -> {alt_a}x+{b} mod {n} have as x ranges over every residue class?", "int"),
        ]
        if unit:
            tasks.append(_task("T4", "transfer", "far", f"Give the multiplicative inverse of {a} modulo {n} as the unique residue in [0,{n-1}].", "int"))
        else:
            tasks.append(_task("T4", "counterexample", "far", f"Give two distinct residues [x,y] modulo {n} with {a}x ≡ {a}y (mod {n}).", "mul_collision_pair"))
        situations.append({
            "id": f"R{i:02d}",
            "cluster": "reversibility",
            "title": f"Information loss modulo {n} with multiplier {a}",
            "visible": {
                "statement": f"On residues modulo {n}, inspect the multiplication map x -> {a}x mod {n}.",
                "sample_mapping": _sample_mul(a, n),
            },
            "contexts": rev_context(n),
            "shuffled_context_id": pool_id(i),
            "hidden_tasks": tasks,
        })
    return situations
