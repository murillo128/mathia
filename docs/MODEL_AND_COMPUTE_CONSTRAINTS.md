# Model and compute constraints

## Status

This note records provisional compute/model constraints for the active semantic-intuition experiment. They are execution choices for controlled comparison, not permanent architecture decisions.

## Preserve a common model ancestor

The first local Mathia diagnostic should continue to use the same exact base revision already preserved by qwen-lean unless an explicit pre-inference design return changes that choice:

```text
model:     Qwen/Qwen3-8B-Base
revision:  49e3418fbbbca6ecbdf9608b4d22e5a407081db4
tokenizer: Qwen/Qwen3-8B-Base
revision:  49e3418fbbbca6ecbdf9608b4d22e5a407081db4
```

The purpose is experimental comparability, not a belief that this model is large enough for the final Mathia system.

A shared ancestor preserves later questions such as:

```text
M0 = common base

MC = M0 + conceptual / intuition post-training
MF = M0 + formal / Lean post-training
```

and comparisons among independent specialists, sequential training, joint training, or other combinations.

## The semantic reset reduces immediate GPU pressure

The current gate is benchmark design, not inference.

Issue `#30` is CPU/research work: create and adversarially audit generic computation-free tasks before implementing a model runner.

Issue `#31` is also primarily CPU/software work: build minimal deterministic plumbing only around the accepted benchmark.

GPU work begins at `#32`, after the semantic contract and implementation have both passed independent review.

This is intentional. The project should not use expensive inference to discover that the benchmark is asking the wrong question.

## Shared Ada resource gate

Mathia currently shares an Ada-class GPU resource with qwen-lean.

Do not disrupt qwen-lean's active GPU work for Mathia's first diagnostic. Start the #32 local-model run only when the GPU is available for a bounded Mathia experiment.

This is a scheduling constraint, not a conceptual dependency between the projects.

## What the first model is being asked to do

The first local diagnostic does **not** require the model to be a strong calculator.

The benchmark should test whether the unchanged base model can use generic structural context to answer semantic interventions involving mechanisms such as:

- reversibility;
- information loss;
- invariance;
- quotienting;
- representation transfer;
- structural counterfactuals;
- generalization/diagnosis.

The model's existing arithmetic knowledge may still be present internally, but benchmark success should not depend on executing it.

## Capacity failure must be distinguished from benchmark failure

If Qwen3-8B performs poorly, do not immediately conclude that the experiment needs a larger GPU.

Possible explanations include:

```text
benchmark is verbal / ambiguous / leaky
semantic context contains no useful signal
model cannot exploit the signal at this capacity
inference budget is insufficient
runtime implementation is broken
```

The experiment should preserve enough controls to separate these where possible.

A stronger frontier/API model may later be used as a **ceiling/solvability probe**, but it should not be allowed to tune the protected benchmark item by item after the target protocol is frozen.

## When scaling hardware/model is justified

Scaling is a valid next step when evidence looks like:

- benchmark design survives independent audit;
- strong models can use the intended semantic signal;
- the local model fails in a way consistent with capacity rather than task invalidity;
- throughput, context length, or model capacity is the demonstrated bottleneck.

At that point the system can move to a larger local model and/or more capable GPU without changing the conceptual process being tested.

The relevant question is not whether the first small model is sufficient forever. It is **what minimum specialist capacity makes the conceptual process useful**.

## Three-layer scaling is component-specific

In a later research system, different bottlenecks should scale independently:

```text
Mathia weak conceptually
    -> scale conceptual model

formal specialist cannot formalize/prove useful claims
    -> scale formal model/search

research state is lost/repeated
    -> improve coordination/memory, not GPU first

all components work but are too slow
    -> scale throughput/hardware
```

Do not interpret every system failure as a need to scale all models simultaneously.

## No training compute before a signal

Do not start conceptual SFT, QLoRA, RL, or large synthetic-data generation merely because the GPU becomes available.

The intended order remains:

```text
credible generic semantic benchmark
        |
minimal audited plumbing
        |
frozen unchanged-base diagnostic
        |
interpretable evidence
        |
only then: design post-training if justified
```

This gate is more important than maximizing GPU utilization.
