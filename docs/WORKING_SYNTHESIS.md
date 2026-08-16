# Working synthesis

## Status

This is the current research synthesis after the semantic-intuition reset. It deliberately separates **accepted experimental constraints**, **working hypotheses**, **observed evidence**, and **open questions**.

It is not a final theory of mathematical understanding.

## Accepted experimental constraints for the current line

These are decisions about the next experiment, not universal claims about all future Mathia systems.

### Separate semantic understanding from execution

The first benchmark should not require arithmetic execution, concrete numerical calculation, finite numerical enumeration, or algorithmic state reconstruction.

The target is the model's ability to reason about mathematical meaning and structure.

### Use generic Mathia-visible mathematics

Primary model-visible mathematical content should use generic objects, operations, relations, transformations, and structural roles rather than concrete numeral instances.

The important constraint is semantic, not cosmetic: replacing a value with a variable does not make an execution task conceptual.

### Permit private instantiation for verification

Private generators, computation, falsifiers, and formal systems may instantiate abstract claims when useful. Concrete instances belong on the experimental/verifier side of the boundary, not as the conceptual evidence Mathia relies on.

### Validate the signal before post-training

Do not begin Mathia-specific SFT/RL merely because a training story is plausible. First establish that structural intuitions causally improve unseen semantic tasks relative to strong controls.

### Preserve the retired experiment as provenance

The old `gold-set-v0` line is removed from the active tree but remains in Git history. Issue #12 remains a completed engineering result. We do not rewrite completed history to make it appear that the new hypothesis was always the plan.

## Working hypotheses

### Mathematical meaning can be learned independently enough to measure

It may be possible to construct tasks where a model benefits from understanding what an operation or relation *means* even though no concrete arithmetic execution is needed.

This is unproven. Issue #30 exists to determine whether such a benchmark can be made non-trivial and trustworthy.

### Concepts are better represented as relations among viewpoints than as definitions

A concept may be learned more robustly when the model sees several representations connected by one mechanism rather than one canonical verbal definition.

Examples of candidate mechanisms include:

- reversibility and information preservation;
- quotienting and forgetting distinctions;
- invariance;
- product as independent combination;
- decomposition/distributive structure;
- identity and inverse roles;
- factorization through a representation.

These are candidate sources of examples, not a frozen curriculum.

### Intuition is predictive, not stylistic

A useful operational definition is:

> an intuition is a compact mechanism hypothesis that generates new structural expectations and possible falsifiers.

This implies that intuition quality should eventually be judged by downstream fertility rather than by whether a teacher finds the explanation profound.

### Representation change may be central

A model may display deeper mathematical competence when it can recognize one mechanism across substantially different representations, construct a useful intermediate representation, or choose the representation that exposes the relevant invariant.

### Good mathematical ideas have long-horizon value

In a future research loop, an idea may be valuable because it later produces useful lemmas, eliminations, reformulations, or proof directions. This suggests a future credit-assignment problem over **research fertility**, not merely immediate correctness.

This is far downstream of the current benchmark.

### Specialist cooperation may amplify scarce frontier reasoning

A plausible later system uses:

- a strong frontier director for strategic decisions;
- Mathia for abundant conceptual exploration;
- a formal specialist for exact checking.

Mathia need not outperform the frontier director individually. It would need to provide enough useful conceptual search per unit of cheap local compute to improve the overall research process.

## Evidence we actually have

At present, Mathia has **no target-model evidence** for the semantic-intuition hypothesis.

What the repository does have is process evidence from the retired experiment:

- a hand-designed mathematical benchmark was iteratively audited;
- the audit process exposed and repaired real benchmark defects;
- a deterministic model-agnostic runner was built and independently reviewed;
- the project learned that a seemingly conceptual experiment still relied materially on concrete mathematical execution;
- the experiment was retired before spending GPU on a now-misaligned target.

That last point is methodological progress, not evidence that the new semantic hypothesis is true.

## What a convincing first positive result would look like

A useful first result would not be "the model explains concepts beautifully."

It would look more like:

- structural intuition improves hidden semantic interventions over factual or local-rule context;
- sterile conceptual rhetoric does not reproduce the effect;
- a wrong mechanism predictably harms some downstream judgments;
- an irrelevant/shuffled good intuition does not help generically;
- the effect appears especially in representation transfer, counterfactual reasoning, diagnosis, generalization, or representation selection;
- performance survives alpha-renaming and meaningful representation changes;
- success does not depend on concrete numerical execution.

Even then, the result would establish only a trainable/evaluable signal, not human-like understanding.

## What would count against the hypothesis

Important negative outcomes include:

- the benchmark can be solved from verbal templates without mathematics;
- structural and sterile contexts perform similarly;
- alpha-renaming or notation changes break the effect;
- local-rule context explains all gains;
- the structural context simply leaks the hidden answer;
- generic tasks become so abstract that there is no trustworthy mathematical ground truth;
- the base model cannot exploit any proposed structural representation even when the benchmark is otherwise sound.

The last case could be a model-capacity limitation, but should not be assumed to be one without controls.

## The role of concrete examples

Concrete examples remain valuable scientific instruments.

They can be used privately to:

- falsify an abstract conjecture;
- construct an exact task;
- test whether a proposed invariant is real;
- discover missing assumptions;
- validate a formalization.

The current experimental constraint is only that Mathia's primary conceptual input should not depend on them.

This allows a future loop such as:

```text
Mathia proposes generic mechanism
        |
private computation / Lean instantiates or checks
        |
verified evidence
        |
Mathia revises generic intuition
```

## Cold start and RL remain hypotheses

If the signal exists, a small cold start may teach the *activity* of intuition formation:

```text
structural evidence
   -> competing mechanism hypotheses
   -> predictions
   -> falsification criteria
```

A later optimization stage could reward intuitions for downstream fertility.

But it is still unclear whether RL, rejection sampling, preference optimization, supervised contrastive data, or another method is best. The project should not choose the algorithm before the reward signal is demonstrated.

## Open questions

- What is the simplest genuinely mathematical semantic task that cannot be reduced to verbal analogy?
- How should abstract mathematical meaning be scored exactly without reverting to execution?
- Which concepts naturally admit multiple representations with the same hidden mechanism?
- How much mathematical formalism can appear before the task turns into theorem proving rather than semantic understanding?
- Should Mathia output an intuition, a representation, a next experiment, or a set of structural predictions?
- Can AI feedback reliably distinguish sterile from fertile explanations without becoming the truth oracle?
- Can a small local model exploit semantic context, or will the first credible benchmark immediately expose a capacity floor?
- If model size is the blocker, how does useful intuition scale with parameters and inference compute?
- How should later formal feedback be summarized so that it changes the conceptual model without forcing Lean-native thinking?

## Current action

The next action is not training. It is issue `#30`: design a small computation-free semantic-intuition benchmark and try aggressively to falsify its validity before implementing a runner or using GPU compute.
