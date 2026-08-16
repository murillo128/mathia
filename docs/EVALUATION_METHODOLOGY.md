# Evaluation methodology: evidence for semantic mathematical capability

## Status

This document records Mathia's methodological stance for evaluation. It is not a fixed benchmark suite or execution schedule.

The current plan distinguishes **concept knowledge**, **conceptual dimensions**, **intuition generation**, and **downstream mathematical fertility** rather than collapsing them into one score.

## Keep capability layers separate

### Semantic / conceptual capability

Can the model understand what mathematical constructions mean, what information they preserve or forget, and how they relate across representations?

### Conceptual-move capability

Can it perform reusable operations such as structural transfer, decomposition, synthesis, abstraction, generalization, reframing, bridge construction, counterfactual reasoning, and perspective selection?

### Intuition generation

Can it produce a compact strategic hypothesis about how a theorem or problem should be seen and where a useful proof route, lemma, representation, or obstruction may come from?

### Execution capability

Can it correctly carry out calculations, algorithms, symbolic manipulations, or other instance-level procedures?

### Formal capability

Can it formalize a claim precisely and produce a kernel-verified proof or counterexample?

### Research capability

Can its ideas improve a longer mathematical investigation: generating useful lemmas, reformulations, falsifiers, reductions, or directions?

These capabilities may interact, but improvement in one is not automatic evidence of improvement in another.

## Evidence classes

### Development diagnostics

Small cheap checks for broken prompts, serialization, model loading, parsing, scoring, or obvious task defects. They should not become the scientific result.

### Concept and dimension diagnostics

Internal tests should separately probe whether Mathia understands concepts and can perform conceptual moves under alpha-renaming, notation change, and representation change.

These tests can guide development but are vulnerable to explanation-style confounds and should not be treated as sufficient evidence of intuition.

### Documented-theorem intuition calibration

Use a small panel of well-documented theorems to ask a model for the mechanism, representation, intermediate objects or lemmas, and proof route it would try, without asking for the complete proof.

Famous theorems are acceptable here because the immediate goal is **calibration of strategic behavior**, not clean measurement of novel mathematical discovery. Base-model pretraining exposure must still be acknowledged.

Useful comparisons include the exact Qwen base, later Mathia checkpoints, and a strong frontier reference such as Codex.

### Intuition-fertility evaluation

The strongest internal signal currently proposed is causal downstream utility for a fixed formal worker.

For theorem `T` and intuition `I`, freeze `I` before proof search and compare qwen-lean under matched budgets:

```text
T                     -> qwen-lean -> outcome_base
T + frozen intuition I -> qwen-lean -> outcome_I
```

Lean verifies any resulting proof. The target signal is the matched change in proof-search outcome, not the perceived quality of the prose.

Candidate metrics include:

- verified proof success;
- proof-search attempts, tokens, or cost to verified proof;
- verified useful intermediate lemmas;
- correct reductions that lower subsequent search cost;
- verified counterexamples that eliminate a branch.

A failed proof search is ambiguous and must not be labeled as mathematical refutation.

### External mathematical validation

Later, independently designed tasks should test whether trained capability transfers outside Mathia's own documented-theorem and qwen-lean environment.

Relevant families may include structural perturbation, falsification/counterexamples, mathematical construction, research-level reasoning, and formal theorem proving. The final suite should be chosen when trained checkpoints and contemporary baselines are known.

### Open-ended research evidence

A later three-layer system may work on research-style problems where no final answer is known. Evaluation should then track intermediate verified mathematical progress rather than plausible prose.

## Controls for intuition fertility

At minimum consider matched conditions such as:

- no intuition;
- irrelevant/shuffled intuition;
- Qwen-base intuition;
- Mathia intuition;
- Codex intuition as a strong reference;
- optionally a documented human strategy represented through the same interface.

The theorem, formal target, qwen-lean checkpoint, proof-search budget, runtime semantics, and verification rules should be fixed or explicitly balanced.

### Frontier-reference channel test

Before training Mathia against qwen-lean uplift, verify that a strong frontier intuition can produce measurable uplift at all.

If Codex guidance does not help qwen-lean, likely explanations include an unsuitable interface, a formal-worker bottleneck, ceiling effects, or a bad fertility metric. That is a reason to revisit measurement before post-training.

### Proof leakage

An intuition that contains a near-complete proof may improve qwen-lean for the wrong reason. The interface should target strategic compression: mechanism, representation, intermediate objects/lemmas, assumptions, and route, while leaving meaningful proof work to the formal specialist.

### Solver-specific prompt hacking

Mathia may learn text that exploits one qwen-lean checkpoint rather than a generally useful mathematical idea. Preserve provenance and later test transfer across notation, prompting, qwen-lean versions, or another solver where practical.

### Teacher-imitation confound

Similarity to Codex or documented human intuition is auxiliary evidence only. If similarity rises while qwen-lean utility does not, the model may be learning style or canonical exposition rather than useful strategy.

### Arithmetic execution confound

Primary Mathia-facing tasks should not depend on concrete calculation. A theorem or proof search may contain formal mathematics, but the conceptual guidance under study should remain generic rather than relying on numerical instances.

## Base-model pre-test

Before Mathia-specific post-training, run the exact common Qwen base on the documented-theorem intuition task.

This estimates how much strategic capability is already present. A model may know or even have memorized a theorem proof yet still fail to produce a compact strategy that causally helps another prover.

The pre-test should therefore report at least two different quantities:

1. quality/structure of the generated strategy under the accepted audit criteria;
2. downstream qwen-lean proof-search effect under the frozen fertility protocol.

The second quantity is the stronger behavioral signal.

## Later ablation logic

If the pre-test validates the measurement channel, later checkpoints may be compared conceptually as:

```text
M0 = exact base
MC = concept-trained
MD = concept + conceptual-dimension training
MI = MD + initial Codex intuition distillation
MF = MI + fertility-based optimization
```

These are experimental labels, not a commitment to a specific training implementation.

The useful question is **where the behavior changes**. For example, concept training may improve representation robustness, dimension training may improve reframing/transfer, distillation may improve plausible strategy generation, and fertility optimization may improve actual proof-search uplift.

## AI-judged evidence

AI judges can help with dimensions that are hard to formalize, such as whether two intuitions are genuinely distinct, whether an explanation is a paraphrase, or whether a proposed representation is natural.

These judgments are **soft evidence**. Where Codex is both teacher and judge, its preference must not be reported as independent validation of a student distilled from Codex.

## Formal verification evidence

Keep separate:

- informal-statement fidelity;
- formalization success;
- proof success;
- counterexample/refutation success;
- proof-search failure.

A Lean-checked proof is strong evidence for the exact formal proposition. Failed proof search is not evidence of falsehood. A compiling formalization may still encode the wrong informal claim.

## Contamination and theorem familiarity

For the documented-theorem pre-test, pretraining familiarity is a known limitation rather than an automatic exclusion criterion. The panel is being used to calibrate intuition generation and the qwen-lean measurement channel.

For claims of mathematical generalization, stronger isolation is required: lesser-known theorems, transformed presentations, protected items, or independent external evaluations should be used where practical.

Do not claim that success on familiar theorem intuition is evidence of rediscovery from first principles.

## Compare against the exact base and strong alternatives

The primary causal comparison for Mathia post-training should include the exact base checkpoint under matched inference conditions.

Additional baselines may include:

- explanation-only or teacher-distillation training;
- compute-matched ordinary math/solver post-training;
- generic local reasoning without Mathia specialization;
- Codex/frontier strategy as a reference ceiling;
- stronger contemporary models when protocols are comparable.

## Fair inference comparison

Record enough detail to distinguish model quality from test-time compute:

- model/checkpoint and tokenizer;
- theorem/prompt representation;
- output/reasoning budget;
- sampling policy;
- tools/retrieval/formal verifier;
- number of attempts;
- aggregation rule;
- qwen-lean checkpoint and proof-search budget;
- hardware/throughput when runtime matters.

## Negative results

Treat the following as evidence rather than engineering failures:

- Codex intuition does not improve qwen-lean;
- base Qwen already saturates the strategic task;
- concept/dimension training changes prose but not downstream utility;
- qwen-lean uplift appears only with proof leakage;
- solver-specific gains fail to transfer;
- teacher similarity rises without fertility gains;
- the formal worker is too noisy for stable intuition-level credit assignment.

Different failures imply different next steps. Do not automatically respond with more training or larger hardware.

## Current methodological priority

Before Mathia post-training, establish whether the proposed causal instrument is usable:

> **Can a frozen strategic intuition measurably improve qwen-lean's verified proof search under a matched budget, and does a strong frontier reference demonstrate enough headroom over Qwen base to make later specialization testable?**

Issue #30 scopes that contract, #31 implements the minimal harness, and #32 runs the frozen pre-test.
