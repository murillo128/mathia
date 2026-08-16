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
    subsets = {
        1: [8, 11, 14, 5],
        2: [3, 6, 9, 12],
        3: [5, 8, 11, 14],
        4: [3, 4, 11, 12],
        5: [7, 10, 13, 16],
        6: [3, 4, 5, 6],
        7: [3, 6, 9, 12],
        8: [3, 4, 5, 6],
    }
    starts = {1: 7, 2: 11, 3: 15, 4: 3, 5: 7, 6: 6, 7: 31, 8: 5}
    candidate_sets = {
        1: [1, 4, 7, 10],
        2: [2, 5, 8, 11],
        3: [3, 6, 9, 12],
        4: [3, 7, 11, 15],
        5: [1, 5, 9, 13],
        6: [2, 5, 8, 11],
        7: [4, 9, 14, 19],
        8: [6, 13, 20, 27, 34],
    }
    targets = {1: 11, 2: 3, 3: 9, 4: 2, 5: 18, 6: 4, 7: 18, 8: 25}
    recovery_inputs = {1: 11, 3: 7, 5: 14, 7: 12}

    for i, n, a in specs:
        unit = math.gcd(a, n) == 1
        target = targets[i]
        subset = subsets[i]
        candidates = candidate_sets[i]
        start = starts[i]
        subset_text = "{" + ",".join(str(x) for x in subset) + "}"
        candidate_text = "{" + ",".join(str(x) for x in candidates) + "}"
        tasks = [
            _task("T1", "restricted-preimage", "near", f"Among candidate residues C={candidate_text}, how many x solve {a}x ≡ {target} (mod {n})?", "int"),
            _task("T2", "subset-image-aggregate", "medium", f"Let S={subset_text}. Add the distinct residues in {{{a}x mod {n} : x in S}} as ordinary integers. What is the sum?", "int"),
            _task("T3", "dynamics-transfer", "far", f"Start at x={start} and repeatedly apply x -> {a}x mod {n}. How many distinct residues are visited before the first repeated value appears?", "int"),
        ]
        if unit:
            hidden_x = recovery_inputs[i]
            y = (a * hidden_x) % n
            tasks.append(
                _task("T4", "inverse-reconstruction", "far", f"A hidden residue x in [0,{n-1}] produced output {y} under x -> {a}x mod {n}. Recover x.", "int")
            )
        else:
            tasks.append(
                _task("T4", "counterexample", "far", f"Give two distinct residues [x,y] modulo {n} with {a}x ≡ {a}y (mod {n}).", "mul_collision_pair")
            )
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
