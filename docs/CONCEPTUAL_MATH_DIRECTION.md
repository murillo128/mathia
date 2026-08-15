# Conceptual mathematics direction

This document preserves the conceptual and philosophical motivation behind **Mathia**. It is intentionally exploratory: it is **not** a roadmap, implementation contract, accepted architecture, dataset specification, phase plan, or commitment to a particular model or training method.

The central research question is deliberately broad:

> Can an LLM learn to reason about mathematics primarily at a higher conceptual level—working with ideas, relationships, viewpoints, abstractions, analogies, generalizations, and conjectures—and use a separate formalization/proving layer when exact formal mathematics is needed?

## Motivation

A working hypothesis behind Mathia is that a large amount of formal mathematics is the precise implementation of ideas that can often be expressed much more compactly: cyclic behavior, divisibility, symmetry, invariance, decomposition, change of representation, equivalence, abstraction, generalization, and similar recurring patterns.

From this viewpoint, formal mathematics is indispensable for precision and verification, but it need not be the representation in which all mathematical reasoning happens. A useful analogy is software design versus implementation: the high-level model determines what matters and how the pieces relate; implementation makes that design exact and executable.

This is a research hypothesis, not a settled philosophical claim that mathematics is "only" syntax or that formal proof is unimportant. The interesting question is empirical: does training or operating at a more conceptual layer improve mathematical capability?

## Philosophical context behind the hypothesis

The discussion that motivated Mathia started from a deliberately non-Platonic intuition: mathematical objects can be viewed as human-built representations for recurring relationships rather than as entities that must literally exist independently of us.

Very simple ideas can generate large mathematical structures. Counting leads to arithmetic; asking whether one quantity divides another leads to divisibility, remainders, congruence classes, factorization, and number-theoretic structure. Repeated reversible transformations lead naturally to cycles, composition, inverses, symmetry, and group-like structure. The exact historical development is richer than any one lineage, but the recurring pattern is the important part here.

A relationship is formalized, then often **reified** into a new object that can itself be studied. Relations between those objects become further objects and abstractions. Conceptually:

```text
simple relation or pattern
          |
          v
formal definition / representation
          |
          v
new mathematical object
          |
          v
relations between those objects
          |
          v
higher abstraction
          |
          v
repeat
```

This recursive construction can produce a very deep formal tower whose connection to the original intuition becomes difficult to see. Under this working interpretation, much of pure mathematics can be viewed as exploring consequences of representational systems that were introduced because they compressed some useful pattern.

The fact that the same abstraction appears in many domains does not by itself require a Platonic interpretation. A group, graph, vector space, or similar structure can instead be thought of as an interface that intentionally preserves only a particular kind of relationship. It is then unsurprising that the same interface is useful wherever that relationship occurs.

For example, a group can be understood as a compact language for reversible actions and their composition. Cyclic behavior then captures repeated application and return; permutation groups, rotations, algebraic symmetries, and other domains may reuse the same abstraction because we have deliberately chosen to focus on the same kind of compositional behavior.

This does **not** mean mathematical consequences are arbitrary. We may choose a representation or axioms, but after doing so we do not freely choose their implications. There remains a genuine discovery problem inside a constructed formal system.

## Conceptual complexity versus formal complexity

A related intuition applies strongly to mathematical physics and other mathematical sciences. The conceptual content of an idea can be much smaller than the formal machinery required to state it precisely, calculate with it, and propagate all its consequences. A symmetry, stationary principle, conservation idea, or geometric picture may be easy to describe while its coordinate expressions, tensor manipulations, differential equations, or perturbative calculations are large.

This motivates distinguishing two kinds of complexity:

```text
semantic / conceptual complexity
- what objects or phenomena matter?
- what is the right viewpoint?
- what is invariant?
- which assumptions are essential?
- what should be conjectured?

mechanical / formal complexity
- expand expressions
- change coordinates or representations
- normalize terms
- apply lemmas
- manipulate symbols
- construct a fully checkable derivation
```

Mathematicians and theoretical scientists have historically needed to master both because much of the formal machinery has been executed by humans. One hypothesis worth exploring is whether an AI system can separate those roles more strongly: reason mainly in compact conceptual descriptions and delegate exact formalization and derivation to a lower layer when needed.

The software analogy is useful but intentionally imperfect:

```text
conceptual mathematical idea     software/system design
            |                              |
            v                              v
formal mathematical structure    implementation / IR
            |                              |
            v                              v
formal proof / derivation         executable implementation
            |                              |
            v                              v
formal verification              compiler/tests/runtime checks
```

Under this analogy, large amounts of local theorem search, rewriting, tactic selection, symbolic manipulation, or coordinate algebra are closer to implementation or compilation than to the highest level of mathematical understanding.

There are important limits to the analogy. Mathematics is not merely bureaucratic translation. Formalization can reveal consequences that intuition misses, expose contradictions in an apparently simple idea, or show that a proposed abstraction is insufficient. In physics, mathematical derivation also cannot prove that a model is empirically true of nature; it proves consequences conditional on the model, while experiment decides whether the model describes reality.

The formal layer is therefore not disposable. It can be both a correctness constraint and a cognitive tool that feeds surprising information back into the conceptual layer.

The useful research claim is narrower and empirical:

> Some mathematical capability may improve if an LLM is trained to operate explicitly on compact conceptual descriptions and conjectures before being asked to compile those ideas into exact formal mathematics.

## Desired conceptual layer

The tentative mental model is:

```text
mathematical material / problems / examples
                |
                v
    conceptual mathematical reasoning
                |
                v
      concepts, viewpoints, conjectures
                |
                v
   optional formalization / proving layer
                |
                v
       formal verification when useful
```

The upper layer should not merely predict tactics or perform longer theorem-search traces. Its role is closer to asking:

- What is this problem really about?
- Which details appear accidental and which structure matters?
- Is there a simpler representation or viewpoint?
- Does an invariant, symmetry, quotient, cycle, decomposition, or analogy explain the behavior?
- Is an assumption stronger than necessary?
- Can several concrete results be compressed into a more general conjecture?
- What conjecture would be worth attempting next?
- Which concepts connect a family of apparently different theorems?

A future formalization/proving layer may turn those ideas into exact statements and proofs, but that layer should not prematurely determine how the conceptual model must think.

## Representation: close to mathematical natural language

The conceptual layer should remain much closer to concise mathematical natural language than to a new formal DSL.

The goal is not to invent "Lean-lite", a conceptual type system, or another rigid formal language in which every early thought must already be precise. Useful mathematical exploration often contains provisional statements such as:

- "This looks cyclic."
- "The absolute value probably does not matter; only the residue does."
- "Try viewing this as a permutation of the residue classes."
- "Primality may be stronger than necessary; perhaps coprimality is what is actually used."
- "These examples seem to be instances of the same symmetry."
- "The theorem is stated for a very rich structure, but the proof may only use a small part of it."

Such statements may be deliberately less precise than formal mathematics while still being substantially more structured and mathematical than unrestricted conversational prose.

A future corpus might therefore use short **mathematical meta-descriptions**: compact explanations of the underlying concepts, useful viewpoint, possible generalization, conjecture, or reason a result should be true. The exact style and schema are deliberately open.

## A possible corpus direction

One possible experiment is to use ChatGPT, Codex, or another strong teacher system to generate these meta-descriptions from mathematical source material.

Possible source material includes:

- formal theorem statements and verified proofs from systems such as Lean/mathlib;
- groups or neighborhoods of related theorems rather than isolated proof strings;
- textbooks or worked mathematical exposition with suitable licensing;
- general mathematical definitions and examples;
- examples and counterexamples generated specifically for investigation.

The generated descriptions could try to capture things such as:

- the fundamental concept behind a theorem;
- how a concept relates to neighboring concepts;
- which family of theorems expresses a common idea;
- which theorem is a fundamental characterization versus a mechanical consequence;
- what information a representation deliberately forgets;
- which assumptions seem essential or accidental;
- a useful change of viewpoint;
- analogies with other mathematical structures;
- possible generalizations;
- conjectures suggested by examples or theorem families.

The goal would be to capture conceptual content rather than paraphrase an implementation or proof line by line.

This data would initially be synthetic or weakly supervised. A formal proof can verify an eventual formal statement, but it cannot certify that a natural-language conceptual explanation is insightful, faithful, or pedagogically useful. That distinction must remain explicit.

## Concepts, relationships, and theorem families

A useful working picture for corpus exploration is not merely:

```text
theorem -> explanation
```

but something closer to:

```text
concepts
   <-> relationships
   <-> theorem families
   <-> examples / counterexamples
```

For example, a cluster of gcd theorems may be better represented by the universal-property idea "the gcd divides both arguments and every common divisor divides the gcd" than by treating every theorem as an unrelated fact.

Likewise, congruence, quotienting, periodicity, and cyclic structure may form a conceptual chain in which each abstraction captures what information matters and what information is intentionally discarded.

A corpus that teaches these connections may be more interesting than one containing isolated dictionary-like explanations.

## Avoiding a Wikipedia-style corpus

A central risk is producing mathematically polished prose that does not teach stronger mathematical reasoning.

Useful meta-descriptions should ideally do more than define terminology. They should expose operations such as:

- identifying the small number of ideas that compress many results;
- distinguishing structural facts from representational accidents;
- recognizing when the same pattern occurs in superficially different settings;
- weakening unnecessary assumptions;
- changing representation to make a problem simpler;
- proposing and refining conjectures;
- recognizing counterexamples or limits of an analogy.

The eventual value of the corpus should be judged by downstream mathematical capability, not merely fluency or explanation style.

## AI-feedback training opportunity

This direction is a natural place to experiment with **AI feedback** because conceptual output is not directly machine-verifiable in the way a formal proof can be.

A teacher or judge model could, for example:

- generate multiple conceptual descriptions for the same mathematical material;
- rank descriptions by clarity, faithfulness, generality, or usefulness;
- identify when a description merely paraphrases a proof instead of extracting an idea;
- propose or rank conjectures;
- critique a conjecture after a counterexample or failed formalization;
- create chosen/rejected pairs for preference training.

This could support preference optimization or other AI-feedback post-training experiments.

The distinction between **AI-judged conceptual quality** and **formally verified correctness** must remain visible rather than treating them as the same signal.

A possible future feedback loop is:

```text
conceptual idea / conjecture
          |
          v
AI feedback / refinement
          |
          v
formalization and proof attempt
          |
          v
verified result, counterexample, or failure evidence
          |
          +------> refine the conceptual model
```

A failed proof attempt does not imply that a conjecture is false. Such a loop would need to distinguish prover weakness, formalization problems, and actual counterexamples.

## Possible training questions

A later experiment could ask whether training on conceptual/meta-description material improves mathematical behavior beyond training on formal theorem/proof pairs or ordinary mathematical text.

The training method is intentionally unspecified. The project should remain free to compare different base models, adapter-based or full-model training, preference methods, AI-feedback methods, or combinations with formal-mathematics training.

Possible comparisons might include:

```text
base model

vs.

conceptual/meta-description training

vs.

formal-mathematics training

vs.

conceptual + formal training
```

The interesting outcome is not merely whether a model writes nicer explanations. The stronger hypothesis is that conceptual training could improve abilities such as abstraction, generalization, conjecture formation, representation choice, assumption weakening, and ultimately successful mathematics.

## What would count as evidence

The eventual question is empirical: does adding this conceptual layer make a model better at mathematics?

Potential evidence could include improvements in some combination of:

- held-out mathematical problem solving;
- quality and usefulness of conjectures;
- ability to generalize a theorem or weaken unnecessary assumptions;
- ability to recognize common structure across superficially different problems;
- ability to choose useful representations or viewpoints;
- rate at which conceptual outputs can be turned into valid formal statements;
- downstream formal-proof success when a conceptual layer feeds a formalizer/prover;
- performance compared with an otherwise similar model trained primarily on theorem/proof data;
- robustness of conceptual judgments under independent teacher/judge review.

The exact evaluation protocol is intentionally open.

## Relationship to formal theorem proving

Mathia is conceptually separate from a formal theorem-proving project.

A formal backend such as Lean may later become useful as a formalizer, verifier, source of theorem neighborhoods, source of proof-state evidence, or downstream evaluator. But Mathia should not be designed as merely a wrapper around Lean or constrained to think in Lean-native representations.

For now, the durable idea preserved by this document is only:

> Explore whether training an LLM on compact, higher-level mathematical meta-descriptions, conceptual relationships, and conjecture-oriented reasoning can improve mathematical capability; treat formal mathematics as an optional downstream precision/verification layer and use the conceptual layer as a natural testbed for AI-feedback training.

## Deliberate non-decisions

This document intentionally does **not** decide:

- a project roadmap or phases;
- a dataset schema;
- exact mathematical domains;
- which source corpus to use;
- which model family to train;
- whether to use SFT, preference optimization, RL, full fine-tuning, adapters, or another method;
- how to score conceptual quality;
- which formal system, if any, should be integrated;
- how conceptual and formal models should be architecturally connected.

Those choices should be made only when a later project-design session has enough evidence and explicitly chooses to settle them.
