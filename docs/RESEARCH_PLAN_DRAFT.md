# Draft research plan: semantic mathematical intuition

## Status

This is Mathia's current **draft research plan** after retiring the first execution-oriented pre-RL experiment.

It is intentionally narrower than a full architecture roadmap. The immediate purpose is to create a falsifiable experimental path from **semantic mathematical meaning** to a possible later **intuition/fertility training signal**.

The active operational plan is tracked by epic `#29` and issues `#30`–`#32`.

## Central research question

> **Can a language model form and use generic mathematical intuitions about operations, relations, transformations, and representations in a way that improves unseen structural reasoning without requiring concrete arithmetic execution?**

The project should answer this before committing to a training algorithm or large-scale corpus.

## Research decomposition

The current conceptual stack is:

```text
semantic meaning
      |
      v
multiple representations
      |
      v
mechanism / intuition
      |
      v
structural expectations
      |
      v
hidden interventions
      |
      v
measured fertility
```

Execution and formal verification are intentionally downstream:

```text
private instantiation / computation / formalization / proof
```

They may provide exact evidence without defining the conceptual representation Mathia must use.

## What the first benchmark must isolate

The first benchmark should measure whether a structural interpretation changes downstream mathematical behavior **because it captures a mechanism**, not because it:

- adds more tokens;
- states the hidden answer;
- gives a procedural recipe;
- contains concrete values that can be calculated;
- uses recognizable rhetoric;
- shares vocabulary with the task;
- exposes experimental metadata.

This is why strong controls and genericity tests are central.

## Experimental boundary: no arithmetic execution

For the active line, primary model-visible tasks should not require:

- concrete arithmetic evaluation;
- explicit numeral-based examples as evidence;
- gcd/residue calculation;
- finite numerical enumeration;
- repeated numerical state updates;
- reconstruction of concrete values;
- any other operation whose success can be explained mainly by ordinary arithmetic competence.

The base model already knows such skills. The benchmark isolates semantics by making them unnecessary rather than by pretending they are absent.

Concrete instances may still be used privately by exact verifiers or generators.

## Genericity and representation robustness

The benchmark should be designed so that the intended mathematical relation survives:

- alpha-renaming of objects and operations;
- notation changes;
- reordering of irrelevant presentation details;
- alternative realizations of the same structural mechanism;
- where appropriate, transfer across mathematical domains.

A representation-sensitive benchmark should intentionally include transformations that preserve the mechanism but change surface cues.

## Candidate semantic mechanisms

The following mechanisms are promising sources for hand-designed situations. They are not a fixed taxonomy.

### Reversibility and information preservation

Questions such as:

- when can a transformation be undone?;
- what information must be preserved for reconstruction?;
- what structural conclusions follow from having an inverse role?;
- what breaks when information is merged?

### Equivalence and quotienting

Questions such as:

- what distinctions are being declared irrelevant?;
- which properties depend only on the equivalence class?;
- when should a construction factor through the quotient-like representation?;
- what information survives after identification?

### Product / independent combination

Use multiple representations of a product-like structure to ask:

- what independence means;
- how decomposition of one component affects the whole;
- why a distributive-looking law should arise;
- which properties are symmetric or componentwise.

### Invariance

Ask what remains unchanged under a family of transformations and which conclusions depend only on the invariant rather than on the original presentation.

### Factorization and sufficient representation

Ask whether a property or transformation depends only on a coarser description, and what must be true for a factorization through that description to exist.

### Composition

Ask how structural properties such as reversibility or information loss behave under composition and what can be inferred without executing the composed transformation on instances.

## Candidate hidden interventions

The intuition/context is fixed before revealing one of these interventions.

### Structural prediction

Infer what must be preserved, forgotten, reversible, or invariant if the mechanism is correct.

### Counterfactual

Change a structural assumption and predict which conclusion survives.

### Representation transfer

Present the same mechanism in a different realization and test recognition/transfer.

### Diagnosis

Present a plausible analogy or conjecture that fails and identify the missing structural condition.

### Generalization

Ask what weaker or more natural condition the mechanism suggests.

### Representation selection

Offer several valid viewpoints and ask which one makes a target relation natural and why.

### Falsification design

Ask what kind of structural observation would refute the proposed intuition, without requiring Mathia to enumerate a concrete numerical counterexample.

### Bridge construction

Ask whether an intermediate object/representation can translate between two descriptions.

## Control conditions

The first benchmark should likely preserve a paired-context design, but issue `#30` owns the exact final control set.

Candidate controls:

- **none** — no added interpretation;
- **factual** — correct surface restatement;
- **local rule** — correct immediate relation without reusable mechanism;
- **structural** — mechanism-level intuition;
- **sterile** — fluent conceptual rhetoric with few consequences;
- **wrong** — plausible mechanism that makes a specific false prediction;
- **shuffled** — a good intuition from another situation.

The strongest evidence would be a **context × intervention interaction**, not a universal structural win.

## Scoring

The first benchmark should prefer compact auditable targets over free-form explanation scoring.

Possible answer forms include:

- which relation is guaranteed;
- which structural condition is required;
- which transformation preserves a stated property;
- whether a proposed transfer is valid;
- a canonical symbolic relation;
- which representation is appropriate among semantically distinct alternatives.

AI judges may be used for auxiliary dimensions such as whether two viewpoints are genuinely distinct or whether prose is sterile. They should not silently become the correctness oracle.

## Stage A: benchmark design before implementation

Issue `#30` owns the first stage.

Start with a small number of hand-designed cases. Iterate design and adversarial independent review until the benchmark is credible or blocked.

Important attack questions:

- Can a verbal heuristic solve it without mathematics?
- Does structural context leak the answer?
- Does the wrong/sterile control differ stylistically rather than mathematically?
- Does renaming break the task?
- Does the task still secretly require execution?
- Is the ground truth really exact?
- Can the benchmark produce evidence against the hypothesis?

Do not scale the corpus before these questions have good answers.

## Stage B: minimal plumbing only after semantics settle

Issue `#31` owns implementation after `#30` passes.

Reuse only general lessons from the retired runner:

- deterministic identity/hashing;
- provider-neutral import;
- strict parsing;
- public/private separation;
- provenance;
- independent technical review.

Do not inherit the old runner's code/format/cardinality by default. The new semantic task should determine the smallest implementation required.

## Stage C: frozen base-model diagnostic

Issue `#32` freezes the exact benchmark, model identity, generation settings, execution order, and primary analysis **before target-model results**.

The first intended model remains the exact Qwen base shared with qwen-lean for comparability, subject to an explicit capacity/runtime return if it cannot run the accepted task credibly.

The main questions are:

- Does structural intuition causally help?
- Does it help selectively where the mechanism predicts?
- Do sterile/shuffled controls fail to reproduce it?
- Does a wrong mechanism cause predictable degradation?
- Does the signal survive generic renaming/representation changes?

Possible outcomes:

```text
PROCEED_TO_INTUITION_TRAINING_DESIGN
REVISE_SEMANTIC_BENCHMARK
NO_DISTINCT_SIGNAL_YET
CAPACITY_OR_RUNTIME_BLOCKER
```

## Only after a positive signal: cold start

If the diagnostic is convincing, a small cold start may teach the model what kind of activity is expected.

The target pattern is not "write an insightful explanation." It is closer to:

```text
structural evidence
    -> candidate mechanism
    -> competing alternative
    -> predicted consequences
    -> falsification condition
```

The cold start should remain small enough that it does not define a rigid canonical language for mathematical intuition.

Frontier models can generate diverse candidates, critics, and adversarial examples, but teacher preference should not define the final reward.

## Only after a positive signal: fertility-based optimization

A later training hypothesis is to select or reinforce conceptual outputs by what they enable on hidden downstream tasks.

Conceptually:

```text
mathematical situation
      |
Mathia proposes intuition I
      |
I is frozen
      |
unseen intervention(s)
      |
measured mathematical success
      |
credit assigned back to I
```

This differs from ordinary math RL where reward is attached directly to solving the visible problem.

The exact optimization method is deliberately undecided. RL may or may not be the best mechanism once the signal is understood.

## Later: long-horizon research fertility

In a future three-layer research system, an intuition may be valuable because it generates useful mathematical work many steps later.

Possible downstream evidence includes:

- a formally verified intermediate lemma;
- elimination of a false branch;
- a useful reformulation;
- convergence of independent lines of attack;
- a generalization that survives testing;
- reduced formal proof/search cost;
- repeated reuse by later reasoning.

This creates a difficult long-horizon credit-assignment problem. It should not be conflated with the first semantic benchmark.

## Relationship to qwen-lean and formal verification

Preserve the same base ancestor so future comparisons remain meaningful.

Potential later questions include:

- Does conceptual training improve formal lemma generation or proof search?
- Does formal training improve conceptual precision?
- Are two cooperating specialists better than one joint model?
- Can formal feedback teach Mathia to revise intuitions without forcing it to think in Lean syntax?

Formal systems provide exact checks but have asymmetric evidence semantics:

```text
verified proof          -> strong positive evidence
verified counterexample -> strong negative evidence
formalization success   -> precision, not truth
proof-search failure    -> ambiguous
formalization failure   -> ambiguous
```

## External validation

Mathia-specific benchmarks can establish the intended training signal but are not sufficient evidence of broad mathematical improvement.

Later evaluation should use independently designed external tasks, kept isolated from training decisions where practical, and compare:

- the exact base model;
- Mathia-trained variants;
- compute-matched ordinary solver training;
- stronger contemporary models as capability references.

The pattern of gains matters more than one aggregate score.

## Compute scaling

Do not treat small-model failure as automatic evidence that more hardware is required.

First diagnose whether the bottleneck is:

- benchmark validity;
- semantic-model capacity;
- inference throughput;
- formal specialist capacity;
- orchestration/knowledge-management design.

If a credible benchmark exposes a clear capacity floor, increasing model size or GPU resources is a valid next experiment while preserving the same conceptual process.

## Success criterion for the current plan

The first milestone is deliberately modest:

> **A generic structural intuition, committed before an unseen semantic intervention, produces measurable and interpretable downstream mathematical benefit relative to strong controls, without relying on arithmetic execution.**

That would justify asking how to train the capability.

Failure to establish this signal should change the operational hypothesis before scaling data or compute.
