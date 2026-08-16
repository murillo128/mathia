from __future__ import annotations

import math

from contexts import crt_context, pool_id


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def _sample_crt(m: int, n: int) -> list[list[object]]:
    return [[x, [x % m, x % n]] for x in range(min(m * n, 4))]


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(13, 3, 5), (14, 4, 9), (15, 5, 8), (16, 4, 6)]
    coordinate_subsets = {
        13: ([0], [1, 4]),
        14: ([0, 2], [1, 4, 7]),
        15: ([0, 1, 3], [1, 2, 5, 7]),
        16: ([0, 1, 2], [0, 1, 4]),
    }
    reconstruction_targets = {13: 7, 14: 23, 15: 17, 16: 10}
    replacement_moduli = {13: 6, 14: 6, 15: 10}
    for i, m, n in specs:
        coprime = math.gcd(m, n) == 1
        modulus = m * n
        x0 = reconstruction_targets[i]
        rm, rn = x0 % m, x0 % n
        residues_m, residues_n = coordinate_subsets[i]
        set_m = "{" + ",".join(str(value) for value in residues_m) + "}"
        set_n = "{" + ",".join(str(value) for value in residues_n) + "}"
        tasks = [
            _task("T1", "prediction", "near", f"How many distinct coordinate pairs (x mod {m}, x mod {n}) occur as x ranges modulo {modulus}?", "int"),
            _task("T2", "set-transfer", "medium", f"How many residues x modulo {modulus} have x mod {m} in {set_m} and x mod {n} in {set_n}?", "int"),
        ]
        if coprime:
            replacement_n = replacement_moduli[i]
            tasks.extend([
                _task("T3", "transfer", "far", f"Give the unique residue x in [0,{modulus-1}] with x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n}).", "int"),
                _task("T4", "counterfactual", "far", f"Replace modulus {n} by {replacement_n}. How many distinct coordinate pairs (x mod {m}, x mod {replacement_n}) occur as x ranges modulo {m * replacement_n}?", "int"),
            ])
        else:
            tasks.extend([
                _task("T3", "counterexample", "far", f"Give two distinct residues [x,y] modulo {modulus} with the same pair of residues modulo {m} and modulo {n}.", "crt_collision_pair"),
                _task("T4", "diagnosis", "far", f"How many solutions modulo {modulus} satisfy x ≡ 0 (mod {m}) and x ≡ 1 (mod {n})?", "int"),
            ])
        situations.append({
            "id": f"C{i:02d}",
            "cluster": "crt_decomposition",
            "title": f"Residue-coordinate decomposition mod {m} and {n}",
            "visible": {
                "statement": f"Encode x modulo {modulus} by the pair (x mod {m}, x mod {n}).",
                "moduli": [m, n],
                "sample_pairs": _sample_crt(m, n),
                "domain_size": modulus,
            },
            "contexts": crt_context(coprime),
            "shuffled_context_id": pool_id(i),
            "hidden_tasks": tasks,
        })
    return situations
