# Gold set v0: pre-RL conceptual-context experiment

This directory contains a deliberately small, hand-designed **experimental fixture**, not a permanent Mathia dataset schema.

Its purpose is to test one causal question before any Mathia post-training:

> Does giving a fixed solver a structurally useful way of seeing a mathematical situation improve performance on hidden interventions more than factual, procedural, rhetorically polished, wrong, or mismatched context?

## Contents

- `public_fixtures.py` defines 20 visible situations, five candidate context types, a deterministic source for a shuffled structural control, and 80 hidden-task prompts **without answers**.
- `private_truth.py` computes exact answers by finite enumeration and integer arithmetic and is never part of model-visible prompts.
- `materialize.py` writes `public.json` and `ground_truth.json` when a concrete run needs serialized artifacts.
- `validate.py` checks the 20/80 fixture shape, context controls, shuffled-cluster separation, public/private boundary, and answer coverage.
- `AUDIT.md` records intended discriminations, known weaknesses, leakage criteria, and pre-registered directional expectations.

## Context conditions

The runner should derive these conditions without showing the condition label to the model:

1. `none`: no added context.
2. `factual`: a neutral summary of the visible evidence.
3. `procedural`: a local recipe for checking/solving instances.
4. `structural`: a compact representation of the mechanism believed to matter.
5. `sterile`: fluent mathematical prose that sounds conceptual but carries little operational structure.
6. `wrong`: a plausible but systematically misleading conceptualization.
7. `shuffled`: use the `structural` text from `shuffled_structural_from`, which always comes from another mechanism cluster.

The labels above are experiment metadata and must not appear in solver prompts.

## Mathematical clusters

The 20 situations are balanced across four small clusters:

- 8 × modular reversibility / cancellation / congruence solution structure;
- 4 × gcd-preserving transformations;
- 4 × CRT-style residue-coordinate decomposition, including a non-coprime near miss;
- 4 × composition and affine-map reversibility.

This is intentionally broader than a single theorem family but still small enough to audit line by line.

## Hidden interventions

The 80 tasks include prediction, transfer, counterfactual assumption changes, reconstruction, composition, diagnosis, functional-graph representation changes, and witness/counterexample generation.

The set intentionally includes near and far interventions. The main signal of interest is **not** whether structural context improves every task. Procedural context may be superior for local calculation. The hypothesis predicts a relative advantage for structural context particularly when a task requires reusable representation, transfer, diagnosis, or a change of viewpoint.

## Validation

Run from this directory:

```bash
python validate.py
python materialize.py
```

Expected validator result:

```text
validated 20 situations / 80 hidden tasks
```

This validates deterministic fixture invariants. It does **not** establish that the benchmark measures conceptual understanding; that requires the paired context experiment and leakage/ceiling audit in issue #8.

## Freeze rule

Once the first Qwen3-8B run begins, do not edit v0 in response to model results. A genuine mathematical or leakage defect creates a new named version while preserving the original evidence.
