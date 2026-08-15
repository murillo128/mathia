# Pre-RL signal study

This document specifies the first executable research study for Mathia. It is intentionally narrow: **do not train a new model yet**. First test whether conceptual mathematical representations produce measurable downstream benefit under controlled conditions.

It operationalizes the design in `docs/FIRST_MATHEMATICAL_WORLD.md`.

## Research question

> Does conditioning a fixed mathematical solver on a structural conceptual representation improve performance on unseen mathematical interventions, relative to token-matched controls, when the representation was fixed before the intervention was selected?

A positive result would justify moving toward cold-start data and reinforcement learning. A negative or ambiguous result should cause the environment or hypothesis to be revised before training.

## Core comparison

For one visible mathematical situation, construct several frozen contexts:

- no extra context;
- factual summary;
- procedural/local recipe;
- structural conceptualization;
- fluent but sterile conceptualization;
- wrong-but-plausible conceptualization;
- shuffled good conceptualization from another situation.

Then evaluate the same hidden tasks under all applicable contexts with fixed solver settings.

The primary object is paired uplift, not absolute accuracy:

```text
score(task | candidate context) - score(task | matched control)
```

## First mathematical scope

Use only exactly checkable finite arithmetic initially:

- gcd-preserving transformations;
- multiplication modulo `n`;
- cancellation modulo `n`;
- linear congruences `ax = b (mod n)`;
- congruence / quotient compatibility;
- finite orbit structure of `x -> ax mod n`;
- Chinese-remainder decomposition;
- invertible residues as finite group structure.

Avoid importing Lean, theorem-proving infrastructure, or large external mathematical datasets into this first study.

## Required hidden-task families

The initial implementation should cover at least:

1. **prediction** — classify or compute an unseen consequence;
2. **counterfactual** — modify an assumption and predict what survives;
3. **counterexample** — produce or select a small falsifying case;
4. **transfer** — present the same mechanism under changed notation or representation;
5. **simplification / perspective choice** — choose which representation or method is appropriate;
6. **diagnosis** — identify why a plausible conceptualization fails.

Generalization and cross-field composition are desirable but can remain partly teacher/judge-scored until a clean exact verifier is available.

## Mechanical verification

Prefer exhaustive checking over small domains rather than model-based correctness judgments.

Examples:

- `gcd(a,n) = 1` versus whether `x -> ax mod n` is a permutation;
- brute-force cancellation validity;
- enumeration of solution sets for `ax = b mod n`;
- functional-graph analysis for cycles/tails;
- injectivity/surjectivity of CRT maps;
- operation well-definedness on finite quotient tables.

Every generated objective task should carry enough hidden ground truth for deterministic scoring.

## Context-generation discipline

Candidate contexts may initially be hand-written or teacher-generated, but generation and evaluation must be separated.

A context generator must not see the exact held-out task instances used to score that context.

Teacher models may:

- generate alternative perspectives;
- generate matched procedural/factual controls;
- generate plausible near-misses;
- critique contexts for leakage;
- suggest harder interventions.

Teacher preference must not replace objective scoring.

## Solver discipline

Use fixed solver models/configurations within each comparison.

For each hidden task and context condition:

- keep prompt framing stable apart from the context intervention;
- use repeated samples if stochastic decoding is used;
- randomize context order/identifiers so labels such as "structural" are never exposed;
- retain raw answers and exact scores;
- avoid giving the solver the context category or expected mechanism.

The first study may use one strong model for fast iteration, but a promising signal should later reproduce across more than one solver family or checkpoint.

## Leakage controls

A conceptualization fails the experimental contract if it directly states the answer to the hidden test rather than representing the visible situation.

Audit for:

- explicit hidden theorem statements;
- lists of all future cases;
- procedural instructions tailored to one known intervention;
- numerical answers reused by hidden tasks;
- metadata revealing the intended context category.

The commitment boundary should be enforced at data-generation time, not merely by prompt wording.

## First analysis

At minimum report:

- accuracy / exact-score by task family and context condition;
- paired uplift over no-context and factual-summary controls;
- effect of wrong and shuffled contexts;
- procedural-versus-structural comparison;
- task difficulty / ceiling effects;
- context length and token-count differences;
- examples where subjective elegance and objective usefulness disagree.

Do not collapse everything immediately into one scalar "understanding score". The profile across task families is part of the result.

## Evidence that would justify RL

Proceed toward a cold-start + RL experiment only if the study shows at least some robust pattern such as:

- structural contexts outperform factual summaries on held-out transfer, counterfactual, diagnosis, or simplification tasks;
- wrong-but-plausible contexts hurt in mechanism-specific ways;
- shuffled good contexts do not provide the same gain;
- procedural notes dominate on some local tasks while structural notes dominate on broader transfer/generalization tasks;
- the effect survives token/length controls and is not explained by hidden-answer leakage;
- useful contexts are not perfectly predicted by teacher preference alone.

The point is not to demand that structural abstraction always win. A mathematically competent model should learn when abstraction is useful and when a direct procedure is better.

## Negative results that should stop or redirect the project

Do not start RL merely because the infrastructure exists if:

- any extra mathematical prose gives the same uplift;
- the solver is at ceiling on almost all tasks;
- conceptual contexts only help tasks whose wording closely matches them;
- good and wrong contexts perform similarly;
- the structural advantage disappears under matched token budgets;
- gains come mainly from explicit solution leakage;
- subjective "depth" ratings correlate with style but not mathematical consequences.

These would indicate that the current operationalization is not yet measuring the Mathia hypothesis.

## Relationship to issue #2

This study is the first concrete attempt to resolve the umbrella question tracked in issue #2: whether conceptual mathematical reasoning provides a trainable signal distinct from ordinary solver competence and explanation style.
