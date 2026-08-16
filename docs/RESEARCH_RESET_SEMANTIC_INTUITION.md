# Research reset: semantic intuition before mathematical execution

## Status

This document records an **accepted reset of the first Mathia experimental line**.

It does not settle a final architecture, ontology, training algorithm, mathematical curriculum, or relationship to Lean. It does settle what the next experiment is trying to isolate and which parts of the previous experiment are no longer active.

The active epic is GitHub issue `#29`.

## The decision

Mathia's first experiment will no longer ask whether a conceptual explanation helps a general-purpose solver perform concrete arithmetic tasks better.

The new target is more fundamental:

> **Can a model represent and use the meaning of mathematical operations, relations, transformations, and structural mechanisms without relying on concrete numerical instances or arithmetic execution?**

The previous `gold-set-v0` experiment is therefore retired before target-model inference. Its code, fixtures, runner, audits, and documentation remain recoverable through Git history and closed issues/PRs, but they are removed from the active tree so they cannot silently constrain the new design.

This is a conceptual reset with technical continuity: reuse the laboratory discipline, not the old experiment.

## Why the old experiment was no longer the right first test

The previous line asked a legitimate causal question:

```text
mathematical situation
        |
structural / control context
        |
concrete hidden task
        |
solver answer
        |
exact score
```

That design successfully forced us to think about controls, hidden interventions, deterministic scoring, public/private boundaries, auditability, and pre-registration.

However, many hidden tasks still required ordinary execution: computing a concrete result, iterating a finite map, reconstructing a state, evaluating a gcd-like relation, or otherwise carrying out the operation on an instance.

That mixes two capabilities:

```text
understanding what a mathematical operation means
                    +
being able to execute that operation on an instance
```

Mathia is now intended to isolate the first capability before optimizing the second.

Simply replacing concrete numerals with variable names would not solve the problem. A symbolic task can still be an execution task. The reset therefore changes the **semantic demand** of the benchmark, not merely its surface syntax.

## The semantic / execution boundary

The current working decomposition is:

```text
SEMANTICS
What does this operation, relation, or construction mean?
        |
        v
REPRESENTATIONS
In what different ways can the same structure be seen?
        |
        v
INTUITION
What compact mechanism seems to govern the situation?
        |
        v
EXPECTATIONS
What should follow, survive, fail, or transfer if the intuition is right?
        |
        v
FERTILITY
Does the intuition improve unseen structural reasoning?

-------------------------------------------------------

EXECUTION / EXPERIMENT / FORMAL REALITY
Instantiate, compute, search, falsify, formalize, prove, or refute.
```

Mathia's first primary benchmark lives above the line.

Computation, concrete examples, exhaustive search, Python, Lean, or another prover may still be used **behind the experimental boundary** to construct or validate tasks. They are instruments of reality checking, not the conceptual substrate that Mathia is asked to depend on.

## No concrete numeral instances in primary Mathia-visible mathematics

For the active research line, model-visible primary mathematical situations, contexts, tasks, and intended conceptual reasoning should be generic.

Use objects and roles such as:

```text
objects:          A, B, X, Y
maps:             f, g, T
relations:        R, ~
operations:       ⊗, ⊕, ∘
identity role:    e
inverse role:     inv(x)
quotient-like map: q
```

The exact notation is not important and should vary. The important property is that the mathematical content does not depend on a concrete instance value.

This rule is not based on a belief that numerals are mathematically illegitimate. It is an experimental isolation device: concrete values carry accidental information and invite execution strategies that can obscure whether the model understands the underlying construction.

The base model already contains arithmetic knowledge from pretraining. We are not trying to erase it. We must construct tasks where using that knowledge provides no material advantage.

## A stronger test than numeral removal

Every primary task should pass an **execution firewall**:

> Imagine a model that understands mathematical language and structure but cannot evaluate concrete arithmetic. Could it still solve this task perfectly?

If not, the task is probably outside the first Mathia benchmark.

It should also pass a **genericity test**:

> If all objects and operations are renamed consistently, does the target mathematical answer remain the same?

And, where possible, a **representation test**:

> If the same mechanism is presented through another mathematical realization, does the underlying intuition transfer?

These tests are more important than any particular notation rule.

## What it means to understand an operation

Mathia should not be trained to associate one operation with one canonical verbal definition.

A mathematical operation may have several useful representations. The conceptual content lies partly in the relationships among them and in the structure that survives the change of viewpoint.

For example, a product-like construction may be represented as:

```text
independent combination of choices
        <->
rectangular / two-directional composition
        <->
product object built from two components
        <->
scaling-like interaction
```

The target question is not to evaluate the product. Interesting semantic questions include:

- what information from each component is retained;
- what happens when one component decomposes;
- why a decomposition can induce a distributive-looking law;
- which properties are symmetric between the components;
- when another construction is genuinely analogous rather than superficially similar.

Similarly, quotient-like constructions can be understood through:

```text
identify equivalent objects
        <->
forget distinctions declared irrelevant
        <->
retain only information constant on equivalence classes
        <->
factor a description through a coarser representation
```

Again, the benchmark should test consequences of that meaning, not the execution of a quotient algorithm on concrete values.

## Operational notion of intuition

"Intuition" is deliberately not defined as a poetic explanation.

For the next experiments, treat an intuition as:

> **a compact hypothesis about the structural mechanism governing a situation that produces new, falsifiable expectations.**

A fertile intuition might imply that:

- a transformation should preserve some relation;
- an apparent hypothesis can be weakened to a reversibility condition;
- a map loses exactly a certain kind of distinction;
- a property should factor through an equivalence relation;
- an analogy should break when one structural condition is removed;
- another representation should expose the same mechanism;
- a generalization should exist because the original statement used an accidental presentation.

A sterile statement can be mathematically correct yet predict nothing new. A wrong intuition can sound elegant yet make a specific false prediction. The benchmark must distinguish these cases.

## Hidden interventions remain central

One major idea from the retired experiment survives intact: **commit before the hidden test**.

```text
generic mathematical situation
          |
          v
candidate intuition / representation
          |
       commit
          |
          v
unseen structural intervention
          |
          v
measure what the intuition enables
```

This helps distinguish reusable understanding from a response tailored to a known question.

Candidate hidden interventions include:

- structural prediction;
- representation transfer;
- counterfactual assumption change;
- diagnosis of a failed analogy;
- generalization;
- representation selection;
- falsification design;
- bridge construction between descriptions.

The new benchmark should make these tasks answerable without arithmetic execution.

## What we keep from the previous line

The reset preserves methodological lessons that do not depend on the old mathematical content:

- conceptual candidates should be committed before downstream evaluation;
- structural context needs strong factual/local/sterile/wrong/shuffled controls;
- mathematical correctness and AI preference are different signals;
- public model-visible content must be separated from private truth/verifier data;
- prompt identity and provenance should be deterministic once a benchmark is accepted;
- parse failure and mathematical failure should remain distinguishable;
- experiments should be frozen before target-model results;
- independent adversarial review should try to falsify the design before expensive inference;
- negative results are scientifically useful;
- exact instances may be used privately for checking even when they are excluded from conceptual input.

Issue `#12` is explicitly preserved as a completed engineering result for the old experiment. Its runner is retired from the active tree because compatibility with the new task would be a liability, not an asset.

## What we retire

The active repository no longer treats the following as current experimental contracts:

- `gold-set-v0`;
- its concrete arithmetic fixtures;
- its answer kinds and fixed prompt cardinality;
- the old pre-RL runner implementation;
- the old GPU run/freeze plan;
- the previous first-mathematical-world document;
- the previous pre-RL-signal-study document.

They remain available in Git history and closed issues/PRs.

The retirement happened **before the intended local-Qwen experimental run**, so there is no model result being discarded or reinterpreted.

## Implications for cold start and later training

The reset makes the possible future cold-start objective clearer.

A cold start should not primarily teach explanations such as "the key idea is symmetry." It should teach the *activity* of mathematical intuition formation:

```text
partial structural evidence
        |
        v
candidate mechanism
        |
        v
new expectations
        |
        v
falsification / competing viewpoint
```

A later fertility-based training stage could then prefer intuitions because of what they enable on unseen interventions, not because a teacher likes their prose.

This is only a downstream hypothesis. The first job is to establish that a clean semantic-intuition signal exists at all.

## Implications for the three-layer research hypothesis

The three-layer idea becomes cleaner under this separation:

```text
frontier research director
        |
        +--------------------+
        |                    |
        v                    v
Mathia conceptual       formal specialist
meaning / intuition     formalize / prove / refute
        |                    |
        +---------+----------+
                  |
          checked evidence
                  |
          conceptual revision
```

Mathia need not be the component that performs every calculation. A future system may use separate computation or formal tools when instantiation is useful.

The research question is whether Mathia contributes **better conceptual moves per unit of local compute**, not whether it becomes a universal calculator or outperforms the frontier director in isolation.

## Hardware and model scaling

The reset does not assume the first local model is large enough.

Start with the existing common Qwen base because it gives a controlled, affordable diagnostic. If the benchmark is credible but the model shows a clear capacity limitation, scale the model or hardware **after identifying that bottleneck**.

A larger GPU should not be used to rescue a benchmark that is actually measuring the wrong thing.

## Active plan

The active path is intentionally short:

- `#29` — semantic-intuition epic;
- `#30` — current gate: design and adversarially audit a small computation-free benchmark;
- `#31` — later: build minimal benchmark-specific plumbing;
- `#32` — later: freeze, run, and interpret the first local base-model diagnostic.

No SFT/RL or three-layer orchestration issue should be opened merely because the reset sounds promising. Those become justified only if the diagnostic supplies evidence.

## Open research questions

Several important questions remain deliberately unresolved:

- How abstract can a task become before it tests verbal analogy rather than mathematics?
- Which semantic concepts admit exact hidden interventions without concrete execution?
- Can multiple representations be generated without leaking the intended structural answer?
- How should naturalness and explanatory compression be evaluated when exact correctness is unavailable?
- Can a local base model use structural intuition at all without specialized training?
- If the signal exists, is the best training object an intuition, a representation, a proposed next experiment, or something else?
- How should long-horizon research fertility eventually assign credit to an early mathematical idea?

The purpose of the reset is not to answer these by declaration. It is to make the next experiment discriminate among them more cleanly.
