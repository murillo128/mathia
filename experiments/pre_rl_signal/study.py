from __future__ import annotations

import random
from dataclasses import dataclass
from math import gcd
from typing import Any

from .math_world import (
    affine_is_permutation,
    cancellation_counterexample,
    cancellation_is_valid,
    crt_collision,
    crt_map_is_bijection,
    functional_graph_all_vertices_on_cycles,
    gcd_reduction,
    gcd_reduction_preserves,
    linear_congruence_solutions,
    multiplication_is_permutation,
    mul_map,
)


@dataclass(frozen=True)
class HiddenTask:
    task_id: str
    theme: str
    task_type: str
    prompt: str
    answer_kind: str
    ground_truth: Any

    def public_view(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "theme": self.theme,
            "task_type": self.task_type,
            "prompt": self.prompt,
            "answer_kind": self.answer_kind,
        }

    def private_view(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "ground_truth": self.ground_truth,
        }


def generate_visible_situation(theme: str, seed: int) -> dict[str, Any]:
    """Generate only material that a context author may inspect."""
    rng = random.Random(seed)

    if theme == "reversibility":
        examples = []
        candidates = [(a, n) for n in range(6, 16) for a in range(2, n)]
        rng.shuffle(candidates)
        chosen_unit = next((a, n) for a, n in candidates if gcd(a, n) == 1)
        chosen_nonunit = next((a, n) for a, n in candidates if gcd(a, n) > 1)
        for a, n in (chosen_unit, chosen_nonunit):
            images = mul_map(a, n)
            examples.append(
                {
                    "modulus": n,
                    "multiplier": a,
                    "mapping": list(enumerate(images)),
                    "distinct_outputs": len(set(images)),
                }
            )
        return {
            "theme": theme,
            "description": "Compare multiplication maps on finite residue systems.",
            "examples": examples,
        }

    if theme == "gcd_invariance":
        examples = []
        for _ in range(3):
            a = rng.randint(20, 120)
            b = rng.randint(5, 50)
            q = rng.randint(-3, 4)
            c, d = gcd_reduction(a, b, q)
            examples.append(
                {
                    "before": [a, b],
                    "q": q,
                    "after": [c, d],
                    "gcd_before": gcd(a, b),
                    "gcd_after": gcd(c, d),
                }
            )
        return {
            "theme": theme,
            "description": "Observe pair transformations that keep the gcd unchanged.",
            "examples": examples,
        }

    if theme == "decomposition":
        pairs = [(3, 4), (4, 5), (4, 6), (6, 9), (5, 7)]
        rng.shuffle(pairs)
        examples = []
        for m, n in pairs[:3]:
            mapping = [(x, (x % m, x % n)) for x in range(m * n)]
            examples.append(
                {
                    "moduli": [m, n],
                    "mapping": mapping,
                    "distinct_pairs": len({pair for _, pair in mapping}),
                    "domain_size": m * n,
                }
            )
        return {
            "theme": theme,
            "description": "Compare global residues with pairs of local residues.",
            "examples": examples,
        }

    raise ValueError(f"unknown theme: {theme}")


def generate_hidden_tasks(theme: str, seed: int, count: int = 8) -> list[HiddenTask]:
    """Generate held-out tasks from a seed not needed by visible-situation generation."""
    rng = random.Random(seed)
    tasks: list[HiddenTask] = []

    if theme == "reversibility":
        task_builders = [
            _task_mul_permutation,
            _task_cancellation,
            _task_linear_solution_count,
            _task_affine_transfer,
            _task_cycle_structure,
            _task_cancellation_witness,
        ]
    elif theme == "gcd_invariance":
        task_builders = [_task_gcd_preservation, _task_gcd_diagnosis]
    elif theme == "decomposition":
        task_builders = [_task_crt_bijection, _task_crt_collision]
    else:
        raise ValueError(f"unknown theme: {theme}")

    for i in range(count):
        builder = task_builders[i % len(task_builders)]
        tasks.append(builder(rng, i))
    return tasks


def _task_mul_permutation(rng: random.Random, i: int) -> HiddenTask:
    n = rng.randint(6, 30)
    a = rng.randint(0, n - 1)
    return HiddenTask(
        f"perm-{i}", "reversibility", "prediction",
        f"Does x -> {a}x mod {n} permute all residue classes? Answer true or false.",
        "bool", multiplication_is_permutation(a, n),
    )


def _task_cancellation(rng: random.Random, i: int) -> HiddenTask:
    n = rng.randint(6, 30)
    a = rng.randint(0, n - 1)
    return HiddenTask(
        f"cancel-{i}", "reversibility", "transfer",
        f"For all residues modulo {n}, does {a}x ≡ {a}y imply x ≡ y? Answer true or false.",
        "bool", cancellation_is_valid(a, n),
    )


def _task_linear_solution_count(rng: random.Random, i: int) -> HiddenTask:
    n = rng.randint(6, 30)
    a = rng.randint(0, n - 1)
    b = rng.randint(0, n - 1)
    solutions = linear_congruence_solutions(a, b, n)
    return HiddenTask(
        f"linear-{i}", "reversibility", "counterfactual",
        f"How many residue classes x modulo {n} solve {a}x ≡ {b} (mod {n})?",
        "int", len(solutions),
    )


def _task_affine_transfer(rng: random.Random, i: int) -> HiddenTask:
    n = rng.randint(6, 30)
    a = rng.randint(0, n - 1)
    b = rng.randint(0, n - 1)
    return HiddenTask(
        f"affine-{i}", "reversibility", "transfer",
        f"Does x -> {a}x + {b} mod {n} permute all residue classes? Answer true or false.",
        "bool", affine_is_permutation(a, b, n),
    )


def _task_cycle_structure(rng: random.Random, i: int) -> HiddenTask:
    n = rng.randint(6, 24)
    a = rng.randint(0, n - 1)
    return HiddenTask(
        f"cycles-{i}", "reversibility", "prediction",
        f"Under repeated iteration of x -> {a}x mod {n}, is every residue already on a cycle (no transient tail)?",
        "bool", functional_graph_all_vertices_on_cycles(a, n),
    )


def _task_cancellation_witness(rng: random.Random, i: int) -> HiddenTask:
    while True:
        n = rng.randint(6, 30)
        a = rng.randint(0, n - 1)
        witness = cancellation_counterexample(a, n)
        if witness is not None:
            break
    return HiddenTask(
        f"witness-{i}", "reversibility", "counterexample",
        f"Give two distinct residues x,y modulo {n} such that {a}x ≡ {a}y (mod {n}). Return [x,y].",
        "collision_pair", {"a": a, "n": n},
    )


def _task_gcd_preservation(rng: random.Random, i: int) -> HiddenTask:
    a = rng.randint(10, 150)
    b = rng.randint(2, 70)
    q = rng.randint(-5, 6)
    return HiddenTask(
        f"gcd-{i}", "gcd_invariance", "prediction",
        f"Does replacing (a,b)=({a},{b}) by (b,a-qb) with q={q} preserve the gcd? Answer true or false.",
        "bool", gcd_reduction_preserves(a, b, q),
    )


def _task_gcd_diagnosis(rng: random.Random, i: int) -> HiddenTask:
    a = rng.randint(20, 120)
    b = rng.randint(5, 50)
    q = rng.randint(-3, 4)
    good = gcd_reduction_preserves(a, b, q)
    bad_pair = (b, a - q * b + 1)
    bad = gcd(a, b) == gcd(*bad_pair)
    return HiddenTask(
        f"gcd-diag-{i}", "gcd_invariance", "diagnosis",
        (
            f"For (a,b)=({a},{b}), transform A gives (b,a-{q}b); transform B gives "
            f"(b,a-{q}b+1). Which transforms preserve gcd? Return a sorted list containing 'A' and/or 'B'."
        ),
        "string_set", sorted((["A"] if good else []) + (["B"] if bad else [])),
    )


def _task_crt_bijection(rng: random.Random, i: int) -> HiddenTask:
    m = rng.randint(2, 10)
    n = rng.randint(2, 10)
    return HiddenTask(
        f"crt-{i}", "decomposition", "prediction",
        f"Is x mod {m*n} -> (x mod {m}, x mod {n}) a bijection onto all residue pairs? Answer true or false.",
        "bool", crt_map_is_bijection(m, n),
    )


def _task_crt_collision(rng: random.Random, i: int) -> HiddenTask:
    while True:
        m = rng.randint(2, 10)
        n = rng.randint(2, 10)
        witness = crt_collision(m, n)
        if witness is not None:
            break
    return HiddenTask(
        f"crt-collision-{i}", "decomposition", "counterexample",
        f"Give distinct x,y modulo {m*n} with the same residues modulo both {m} and {n}. Return [x,y].",
        "crt_collision_pair", {"m": m, "n": n},
    )


def score_answer(task: HiddenTask, answer: Any) -> bool:
    if task.answer_kind == "bool":
        return isinstance(answer, bool) and answer is task.ground_truth
    if task.answer_kind == "int":
        return isinstance(answer, int) and not isinstance(answer, bool) and answer == task.ground_truth
    if task.answer_kind == "string_set":
        return isinstance(answer, list) and sorted(answer) == task.ground_truth
    if task.answer_kind == "collision_pair":
        if not (isinstance(answer, (list, tuple)) and len(answer) == 2):
            return False
        x, y = answer
        if not (isinstance(x, int) and isinstance(y, int)):
            return False
        a = task.ground_truth["a"]
        n = task.ground_truth["n"]
        return x % n != y % n and (a * x - a * y) % n == 0
    if task.answer_kind == "crt_collision_pair":
        if not (isinstance(answer, (list, tuple)) and len(answer) == 2):
            return False
        x, y = answer
        if not (isinstance(x, int) and isinstance(y, int)):
            return False
        m = task.ground_truth["m"]
        n = task.ground_truth["n"]
        modulus = m * n
        return (
            x % modulus != y % modulus
            and x % m == y % m
            and x % n == y % n
        )
    raise ValueError(f"unsupported answer kind: {task.answer_kind}")
