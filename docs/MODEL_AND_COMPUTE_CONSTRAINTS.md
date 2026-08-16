# Model and compute constraints

## Status

This note records provisional compute/model constraints for the active concepts/dimensions/intuition-fertility experiment. They are execution choices for controlled comparison, not permanent architecture decisions.

## Preserve a common model ancestor

The first local Mathia diagnostic should continue to use the same exact base revision already preserved by qwen-lean unless an explicit pre-inference design return changes that choice:

```text
model:     Qwen/Qwen3-8B-Base
revision:  49e3418fbbbca6ecbdf9608b4d22e5a407081db4
tokenizer: Qwen/Qwen3-8B-Base
revision:  49e3418fbbbca6ecbdf9608b4d22e5a407081db4
```

The purpose is experimental comparability, not a belief that this model is large enough for the final Mathia system.

A shared ancestor preserves later comparisons such as:

```text
M0 = common base
MC = M0 + concept training
MD = MC + conceptual-dimension training
MI = MD + intuition distillation
MF = MI + fertility-based optimization

Qwen-Lean = formal specialist from the same broader base lineage
```

The exact later training topology is not fixed by these names.

## Current compute sequence

Issue `#30` is research/design work. It scopes the concept/dimension vocabulary, documented-theorem intuition task, qwen-lean conditioning interface, controls, and proof-search fertility metrics. It should not consume training or target-inference GPU budget.

Issue `#31` is primarily software/plumbing work. It implements only the accepted pre-test and fertility measurement harness.

Issue `#32` is the first GPU-backed diagnostic in the new plan. It should run a frozen comparison of at least:

- exact Qwen base intuition generation;
- Codex/frontier intuition as a strong reference;
- qwen-lean proof search under matched budgets with and without those intuitions.

The objective is to validate the measurement channel before Mathia post-training.

## qwen-lean identity must be frozen at execution time

The related qwen-lean project may evolve. Issue #32 must record the exact qwen-lean checkpoint, source revision, Lean/mathlib environment, inference settings, and proof-search budget used for the fertility experiment.

Do not infer or hard-code that identity now from memory. Resolve it from the qwen-lean repository/runtime when #32 is frozen.

## Shared Ada resource gate

Mathia shares an Ada-class GPU resource with qwen-lean.

Do not disrupt qwen-lean's active GPU work. Start the #32 pre-test only when the resource is available for a bounded experiment or when an explicitly approved alternative compute arrangement exists.

This is a scheduling constraint. qwen-lean is nevertheless now a scientific dependency of the **fertility measurement**, because its proof-search response is part of the proposed signal.

## What the first base-model pre-test is asking

The first diagnostic does not ask Qwen base to be a strong calculator or formal prover. It asks whether, given a documented theorem statement and appropriate generic context, the model can produce a compact strategic intuition: mechanism, representation, intermediate objects/lemmas, assumptions, or proof route.

The downstream question is whether that strategy changes qwen-lean's verified proof-search outcome.

A model may know the theorem or proof from pretraining. That is acceptable for this calibration as long as the result is not presented as novel discovery.

## Frontier reference is a channel diagnostic

Codex/frontier intuition is included not as a fair local-compute baseline but as a **strong reference for the interface**.

If qwen-lean cannot exploit a strong frontier strategy under the proposed conditioning channel, then Mathia training against qwen-lean uplift is poorly motivated. The likely bottleneck may be the interface, qwen-lean, the formal target, or the metric rather than Mathia capacity.

## Capacity failure must be distinguished from measurement failure

If base Qwen produces weak intuitions or qwen-lean shows little uplift, possible explanations include:

```text
intuition task is verbal / ambiguous / leaky
Qwen base lacks the strategic capability
Codex/reference strategy is not represented well
qwen-lean cannot exploit conceptual guidance
theorem panel is at ceiling/floor
proof-search budget is badly chosen
runtime implementation is broken
```

The Codex-reference condition is intended to separate some of these possibilities before training.

## No training compute before a usable fertility signal

Do not start concept SFT, dimension training, intuition distillation, QLoRA, RL, or large synthetic-data generation merely because the GPU becomes available.

The intended order is currently:

```text
credible concepts/dimensions/intuition measurement design
        |
minimal audited harness
        |
frozen Qwen-base + Codex-reference + qwen-lean pre-test
        |
informative proof-search fertility channel
        |
only then: design concept/dimension/distillation training
        |
only later: choose whether/how to optimize for fertility
```

## When scaling hardware/model is justified

Scaling is a valid next step only after identifying the bottleneck. Examples:

- a stronger intuition generator helps qwen-lean but Qwen base cannot approach it -> conceptual-model capacity may be limiting;
- strong intuitions exist but qwen-lean cannot use them -> formal-worker capacity/search may be limiting;
- both work but runtime is excessive -> throughput/hardware may be limiting;
- neither the task nor reward channel survives audit -> more hardware is not the answer.

The relevant question is what minimum specialist capacity makes the conceptual process useful, not whether the first model is sufficient forever.
