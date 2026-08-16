# Conceptual mathematics direction

## Status

This document records the current conceptual direction of Mathia. It is a research hypothesis, not an architecture specification or permanent ontology.

The most important recent refinement is the deliberate separation of **mathematical meaning and intuition** from **mathematical execution**.

## Central hypothesis

A substantial part of mathematical reasoning is not the ability to carry out an operation, but the ability to understand:

- what information an operation uses;
- what information it preserves or destroys;
- which relations are invariant under a transformation;
- which assumptions are essential and which are accidental;
- which representation makes a phenomenon simple;
- when two apparently different constructions share one mechanism;
- what should be true if a proposed mechanism is correct;
- what observation would force that mechanism to be revised.

Mathia explores whether language models can learn this layer explicitly enough that it produces measurable downstream mathematical value.

## Meaning is not execution

For the active research line, the project treats these as different capabilities:

```text
understand a product-like construction
        !=
evaluate a concrete product

understand reversibility
        !=
run an inverse algorithm on an instance

understand quotienting / forgetting distinctions
        !=
compute a representative of a concrete quotient class

understand invariance
        !=
check a finite list of concrete cases
```

A future integrated mathematical system may need both layers. The first Mathia experiment intentionally tries to isolate the semantic one.

The goal is not to make a model permanently incapable of arithmetic. The base model already contains such knowledge. The benchmark should simply not reward or require it.

## Concepts as families of representations

Mathia should not learn a mathematical concept as one sentence or one canonical notation.

A concept is often better understood through multiple representations connected by shared structure.

A product-like idea may appear as:

```text
independent combination
<-> two-directional geometric construction
<-> product object
<-> scaling interaction
```

A quotient-like idea may appear as:

```text
identify equivalent objects
<-> forget declared-irrelevant distinctions
<-> retain only class-invariant information
<-> factor through a coarser description
```

Reversibility may appear as:

```text
undo a transformation
<-> preserve enough information to reconstruct
<-> one-to-one correspondence
<-> existence of an inverse role
```

The research question is whether a model can recognize and use what is common across these views, and whether changing representation improves its ability to make new structural predictions.

## Mathematical intuition as a mechanism hypothesis

The project uses "intuition" provisionally in a falsifiable sense.

An intuition is not merely a compressed theorem statement or deep-sounding prose. It is a hypothesis such as:

- "this phenomenon is controlled by reversibility rather than by the original stronger assumption";
- "this construction forgets exactly the distinctions represented by an equivalence relation";
- "this quantity depends only on the coarser representation and should factor through it";
- "the apparent special case is one realization of a more general invariant".

A good intuition should generate expectations that were not explicitly supplied.

That gives a behavioral definition of fertility:

```text
intuition
   |
   +--> predicts a hidden structural consequence
   +--> transfers to another representation
   +--> suggests a useful weakening/generalization
   +--> identifies a falsifying condition
   +--> helps diagnose a failed analogy
```

The project should prefer this downstream behavior over a teacher's preference for eloquent explanations.

## Genericity as an experimental constraint

The active experiment uses generic model-visible mathematics rather than concrete numeral instances.

The reason is not aesthetic. Concrete instances provide accidental information and invite algorithmic strategies. We want to ask whether the structural relationship itself carries useful information.

A candidate task should survive:

- consistent renaming of objects;
- notation changes;
- a different realization of the same structure;
- a change of representation that preserves the underlying mechanism.

Failure under such transformations is evidence that the task or model is relying on surface form.

## Representation change may be the key capability

Many mathematical breakthroughs, at both elementary and advanced levels, can be described as finding a representation where the important structure becomes visible.

Candidate forms include:

- replacing an object by an equivalence class;
- moving from elements to transformations;
- moving from local rules to an invariant;
- replacing a process by its fixed structure;
- viewing an operation geometrically, combinatorially, algebraically, or categorically;
- finding an intermediate object that translates between two domains.

Mathia should therefore be evaluated not only on whether it knows concepts, but on whether it can **choose, construct, compare, and transfer between representations**.

## Compression and simplicity

Conceptual understanding often compresses many local facts into one mechanism.

This motivates, but does not prove, a connection between mathematical beauty and useful representation.

A representation may be attractive when it:

- removes accidental choices;
- exposes symmetry;
- reduces case splitting;
- weakens assumptions to the mechanism actually needed;
- explains several facts simultaneously;
- makes generalization natural;
- reduces later search or proof effort.

These are hypotheses to test empirically. "Elegant" is not a correctness label.

## Counterexamples and falsification

A conceptual model that cannot survive attempts to break it is not useful mathematics.

Mathia should learn to ask questions such as:

- what structural condition is carrying the conclusion?;
- what change would remove that condition?;
- what observation would distinguish two competing interpretations?;
- which part of an analogy is essential?;
- what is the weakest failure that would invalidate the proposed mechanism?

The active benchmark should prefer **falsification design** over requiring Mathia itself to enumerate concrete numerical counterexamples. Private tools may instantiate and test the suggested failure mode later.

## Composition of concepts

A mature conceptual reasoner should eventually combine ideas rather than select one label.

Examples of compositional questions include:

- how does quotienting interact with an operation?;
- when does reversibility survive composition?;
- how does information loss constrain later transformations?;
- can two representations be connected by a map preserving the relevant structure?;
- does a decomposition in one domain induce a decomposition in another?

This is a longer-term target. The first benchmark should not try to cover every form of conceptual composition at once.

## Relationship to formal mathematics

Formal theorem proving is complementary rather than identical.

The conceptual layer asks:

```text
What should we try to prove?
Why might it be true?
What is the real mechanism?
Which formulation is natural?
What assumption can be weakened?
What would falsify the idea?
```

A formal layer can later ask:

```text
Is the statement precise?
Does the implication actually hold?
Can it be proved?
Is there a verified counterexample?
```

Lean should not dictate Mathia's internal conceptual language merely because it can provide exact feedback later.

## Relationship to the three-layer research hypothesis

A plausible downstream system separates roles:

```text
frontier director
      |
      +--> Mathia: abundant conceptual exploration
      |
      +--> formal specialist: abundant formal checking
      |
      v
select / revise / redirect
```

Mathia can be useful even if the frontier director is individually stronger. The relevant question is whether Mathia produces **fertile conceptual proposals cheaply and persistently enough** to amplify scarce strong reasoning.

This remains a downstream hypothesis. First establish that a Mathia-specific semantic signal exists.

## Current experimental priority

The active priority is not training.

It is to construct a small benchmark where:

- concrete arithmetic execution is unnecessary;
- structural intuition makes hidden predictions;
- strong controls can falsify the claimed effect;
- alpha-renaming and representation changes challenge surface dependence;
- correctness can be audited without using stylistic judgment as truth.

Only after such a signal is demonstrated should the project design a cold start or fertility-based post-training objective.
