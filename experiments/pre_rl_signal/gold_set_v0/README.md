# Gold set v0: pre-RL conceptual-context experiment

This directory contains a deliberately small, hand-designed **experimental fixture**, not a permanent Mathia dataset schema.

Its purpose is to test one causal question before any Mathia post-training:

> Does giving a fixed solver a structurally useful way of seeing a mathematical situation improve performance on hidden interventions more than factual, procedural, rhetorically polished, wrong, or mismatched context?

The first independent audit (`INDEPENDENT_AUDIT.md`) returned **REVISE** before any model run. The fixture has since been corrected in place, which is allowed by the pre-run freeze rule. `REMEDIATION.md` records those changes. It must pass a fresh independent re-audit before the evaluation manifest is frozen.

## Contents

- `public_fixtures.py` assembles 20 visible situations and 80 hidden-task prompts **without answers** from mechanism-specific fixture modules.
- `contexts.py` defines authored context controls plus a mechanism-orthogonal shuffled pool independent of answer subtype.
- `private_truth.py` computes exact answers and private semantic-scoring parameters by finite enumeration/integer arithmetic.
- `scoring.py` accepts exact scalar answers and any mathematically valid collision witness rather than one canonical pair.
- `materialize.py` writes `public.json` and `ground_truth.json` when a concrete run needs serialized artifacts.
- `validate.py` checks the 20/80 fixture shape, authored-context length balance, public/private boundary, answer coverage, and semantic alternative-witness scoring.
- `AUDIT.md` preserves intended discriminations and pre-registered directional expectations.
- `INDEPENDENT_AUDIT.md` preserves the original `REVISE` audit unchanged.
- `REMEDIATION.md` maps the audit findings to the corrected fixture.

## Context conditions

The runner should derive these conditions without showing the condition label to the model:

1. `none`: no added context.
2. `factual`: a neutral summary of the visible evidence.
3. `procedural`: a local recipe for checking/solving instances.
4. `structural`: a compact representation of the mechanism believed to matter.
5. `sterile`: fluent mathematical prose that sounds conceptual but carries little operational structure.
6. `wrong`: a plausible but systematically misleading conceptualization.
7. `shuffled`: use one text from the fixed `SHUFFLED_POOL`, selected by `shuffled_context_id`; the pool covers unrelated mechanisms rather than borrowing a nearby gold-set structural explanation.

The labels above are experiment metadata and must not appear in solver prompts.

## Mathematical clusters

The 20 situations are balanced across four small clusters:

- 8 × modular reversibility / congruence / functional-graph information loss;
- 4 × gcd-preserving transformations and deliberately perturbed near-misses;
- 4 × CRT-style residue-coordinate decomposition, including a non-coprime near miss;
- 4 × composition and affine-map information loss.

This is intentionally broader than a single theorem family but still small enough to audit line by line.

## Hidden interventions

The 80 tasks mix integer-valued predictions, transfer, counterfactual changes, reconstruction, composition, diagnosis, functional-graph representation change, inverses, and witness/counterexample generation. The correction deliberately reduces duplicated Boolean templates that created ceiling risk in the original fixture.

The main signal of interest is **not** whether structural context improves every task. Procedural context may be superior for local calculation. The hypothesis predicts a relative advantage for structural context particularly when a task requires reusable representation, transfer, diagnosis, or a change of viewpoint.

## Validation

Run from this directory:

```bash
python3 validate.py
python3 materialize.py
```

Expected validator result:

```text
validated corrected gold-set-v0: 20 situations / 80 hidden tasks / semantic witness scoring
```

This validates deterministic fixture invariants. It does **not** establish that the benchmark measures conceptual understanding; a fresh independent leakage/ceiling audit is still required before freeze.

## Freeze rule

No Qwen result has been produced yet, so the issue-8 corrections were allowed in `gold-set-v0`. Once the first Qwen3-8B run begins, do not edit v0 in response to model results. Any genuine mathematical or leakage defect discovered after that point creates a new named version while preserving the original evidence.
