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
    for i, m, n in specs:
        coprime = math.gcd(m, n) == 1
        modulus = m * n
        x0 = modulus - 2
        rm, rn = x0 % m, x0 % n
        tasks = [
            _task("T1", "prediction", "near", f"How many distinct coordinate pairs (x mod {m}, x mod {n}) occur as x ranges modulo {modulus}?", "int"),
            _task("T2", "reconstruction", "medium", f"How many x modulo {modulus} satisfy x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n})?", "int"),
        ]
        if coprime:
            tasks.extend([
                _task("T3", "transfer", "far", f"Give the unique residue x in [0,{modulus-1}] with x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n}).", "int"),
                _task("T4", "counterfactual", "far", "If one modulus were replaced so the two moduli shared a nontrivial factor, would uniqueness modulo the product still be guaranteed for every residue pair? Answer true/false.", "bool"),
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
