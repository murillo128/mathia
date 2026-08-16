# Conceptual mathematics direction

## Status

This document records the current conceptual direction of Mathia. It is a research hypothesis, not an architecture specification, permanent ontology, or fixed training curriculum.

The project currently separates four questions:

1. what mathematical concepts mean;
2. what reusable conceptual moves can be performed over them;
3. whether strategic intuition emerges from combining those resources;
4. whether such intuitions are mathematically fertile downstream.

## Central hypothesis

A substantial part of mathematical reasoning is not the ability to carry out an operation, but the ability to understand:

- what information an operation uses;
- what information it preserves or destroys;
- which relations are invariant under a transformation;
- which assumptions are essential and which are accidental;
- which representation makes a phenomenon simple;
- when two apparently different constructions share one mechanism;
- how a problem can be decomposed or recomposed;
- when a bridge to another domain changes the problem;
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

A future integrated mathematical system may need both layers. Mathia's conceptual training should not rely on arithmetic execution as a shortcut.

The goal is not to make a model incapable of arithmetic. The base model already contains such knowledge. The experimental task is to make that knowledge unnecessary for the conceptual behavior being measured.

## Concepts as families of representations

Mathia should not learn a mathematical concept as one sentence or one canonical notation.

A concept is often better understood through several representations connected by shared structure.

A product-like idea may appear as independent combination, a two-directional geometric construction, a product object, or a scaling-like interaction. A quotient-like idea may appear as identifying equivalent objects, forgetting declared-irrelevant distinctions, retaining only class-invariant information, or factoring a description through a coarser representation.

The research question is whether a model can recognize and use what is common across such views.

Candidate concept material includes:

- composition;
- identity and inverse;
- equivalence and quotienting;
- invariance and symmetry;
- reversibility and information preservation;
- decomposition;
- factorization through another representation;
- necessary and sufficient conditions;
- product-like independent combination;
- representation and change of representation.

This is a source list for experiments, not a final ontology.

## Conceptual dimensions: what the model does with concepts

The earlier Mathia exploration identified a different kind of capability: reusable **mathematical moves** that can be applied across concepts and domains.

Current candidates include:

### Structural similarity / transfer

Recognize that two superficially different problems share a mechanism and transfer expectations between them.

### Decomposition

Split an object, transformation, or problem into parts that reveal distinct roles or simpler substructures.

### Composition / synthesis

Combine concepts, transformations, representations, or domains when none alone provides the right viewpoint.

### Abstraction / compression

Replace many local facts by a smaller structural mechanism or representation.

### Generalization

Identify which parts of a statement are accidental and which support a broader claim.

### Counterfactual reasoning

Predict what changes when an assumption, operation, relation, or representation is modified.

### Simplification

Find a representation in which the same mathematical question requires less work or fewer cases.

### Bridge construction

Introduce or identify an intermediate object that translates between mathematical descriptions.

### Reframing / out-of-the-box movement

Leave the representation in which the problem was posed and formulate it in a substantially different space.

### Multiple perspectives and perspective selection

Generate genuinely different views of the same phenomenon and choose the one that best serves the current goal.

### Naturalness / canonicality

Distinguish constructions induced by the structure of the problem from arbitrary proof choices.

### Prediction and falsification

Use a representation to generate consequences that can support or break the proposed interpretation.

The goal is not to teach the names of these moves. A model could correctly define "reframing" while never reframing a problem. The target is behavioral transfer across mathematical settings.

## Intuition as a candidate emergent property

The current working hypothesis is that intuition may not need to be supervised as a fixed answer from the beginning.

If a model has learned rich concepts and can perform conceptual moves, it may begin to produce strategic statements such as:

- the real mechanism may be reversibility rather than the stronger stated hypothesis;
- this construction seems to ignore exactly one equivalence relation, so quotienting may be the natural representation;
- decomposing the object may expose independent components;
- a bridge into another domain may turn the target into a standard invariant problem.

Treat such outputs as **candidate intuitions**, not as automatically correct explanations.

A useful intuition should change what the model or another solver tries next. It may suggest a lemma, representation, reduction, generalization, or falsifying test.

## Intuition need not be immediately correct

A mathematical intuition can be valuable even when false. A failed mechanism can expose the exact missing condition, identify a counterexample, or eliminate a large branch of search.

Therefore:

```text
good intuition != always-true statement
```

The relevant notion of quality may be closer to **information gain or downstream fertility** than immediate correctness.

## Initial teacher distillation

A strong frontier model such as Codex can provide an initial distribution of strategic mathematical behavior on documented theorems. It may show how to identify mechanisms, representations, intermediate lemmas, assumptions, and proof routes.

This is distillation. It can be useful as a bootstrap without being treated as the final objective.

A Mathia output should not be considered better merely because it resembles Codex or a canonical human explanation. The stronger question is whether it produces useful mathematical consequences.

## Documented theorems as a laboratory

Well-known and well-explained theorems provide a useful calibration environment because their proof ideas can be inspected and several proof strategies may be available.

The base model may already know the theorem or proof from pretraining. For the first internal diagnostic that is acceptable: the question is whether the model can produce a **compact strategic representation that helps another prover**, not whether it rediscovered the theorem from scratch.

This means familiar theorems are appropriate for calibration but weak evidence of novel generalization. Later evaluation should use more independent material.

## Fertility through a separate formal worker

The current strongest behavioral proposal is to freeze a candidate intuition and measure its effect on qwen-lean under a matched proof-search budget.

Conceptually:

```text
theorem
   -> qwen-lean
   -> verified proof-search outcome

same theorem + Mathia intuition
   -> qwen-lean
   -> verified proof-search outcome
```

If the intuition increases verified proof success, reduces search cost, produces a useful verified intermediate lemma, or eliminates a false branch, it has demonstrated solver-conditional fertility.

That signal is stronger than an AI judge saying the intuition is elegant. It is still not a complete definition of mathematical intuition because qwen-lean has its own limitations and biases.

## Representation change may be central

Many mathematical advances can be described as finding a representation where the important structure becomes visible.

Candidate forms include:

- replacing objects by equivalence classes;
- moving from elements to transformations;
- moving from local rules to invariants;
- replacing a process by its fixed structure;
- viewing an operation geometrically, combinatorially, algebraically, or categorically;
- finding an intermediate object that translates between two domains.

Mathia should therefore be evaluated not only on whether it knows concepts, but on whether it can choose, construct, compare, and transfer between representations.

## Compression and simplicity

Conceptual understanding often compresses many local facts into one mechanism. A representation may be useful when it removes accidental choices, exposes symmetry, reduces case splitting, weakens assumptions to the mechanism actually needed, explains several facts simultaneously, or makes generalization natural.

These are hypotheses to test empirically. "Elegant" is not a correctness label.

## Counterexamples and falsification

A conceptual model that cannot survive attempts to break its ideas is not useful mathematics.

Mathia should learn to ask what structural condition carries a conclusion, what change would remove it, what observation distinguishes two competing interpretations, and what is the weakest failure that invalidates a proposed mechanism.

Private computation and formal tools may instantiate those failure modes later.

## Composition of concepts

A mature conceptual reasoner should combine ideas rather than select one label. Examples include asking how quotienting interacts with an operation, when reversibility survives composition, how information loss constrains later transformations, or whether a decomposition in one domain induces one in another.

This is one reason composition/synthesis is treated as a conceptual dimension rather than merely a mathematical concept.

## Relationship to formal mathematics

Formal theorem proving is complementary rather than identical.

The conceptual layer asks what should be tried, what the real mechanism is, which formulation is natural, what assumption can be weakened, what representation might help, and what would falsify the idea.

A formal layer asks whether the statement is precise, whether the implication actually holds, whether it can be proved, and whether there is a verified counterexample.

Lean and qwen-lean should not dictate Mathia's internal conceptual language merely because they provide exact downstream feedback.

## Relationship to the three-layer hypothesis

A plausible later system separates roles among a frontier teacher/director, Mathia as abundant conceptual explorer, and a formal specialist as abundant checker/prover.

The current plan uses part of this structure earlier: qwen-lean may act as a measurement instrument for intuition fertility before the full research system is built.

## Current experimental priority

The immediate priority is not training.

Issue #30 must first scope and adversarially audit:

- the provisional concept substrate;
- the conceptual dimensions;
- a documented-theorem intuition task;
- a proof-leakage boundary;
- a matched qwen-lean fertility measurement;
- strong reference and control conditions.

Then #31 can build minimal plumbing and #32 can test Qwen base and Codex-reference intuitions against qwen-lean before Mathia-specific post-training begins.
