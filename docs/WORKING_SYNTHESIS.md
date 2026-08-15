# Working synthesis: conceptual mathematical reasoning

This note captures the current working synthesis of the Mathia brainstorming. It is deliberately exploratory. It is **not** a roadmap, architecture, dataset schema, training recipe, or settled theory of mathematics. Its purpose is to preserve the research hypothesis clearly enough that the next discussion can ask a different question: **how could we actually build and test this?**

## 1. The motivating distinction: understanding what is happening versus proving how it happens

A formal proof establishes that a conclusion follows from definitions, assumptions, and valid inference steps. This answers an indispensable question:

> How does the theorem follow?

But mathematical understanding often feels like a different achievement:

> What is really happening here, and why does this result become natural from the right point of view?

A student can follow or reproduce a proof while still not understanding the phenomenon. Conversely, after finding the right representation, a theorem can suddenly feel almost inevitable even before every formal step has been written down.

For example, rank-nullity can be proved by choosing a basis of the kernel, extending it to a basis of the domain, and analyzing its image. But the conceptual picture is smaller: a linear map partitions the information in the domain into information that disappears and information that remains observable. The kernel measures what is lost; the image measures what survives. In finite dimension, the original dimension must split between the two.

This distinction suggests that formal derivation and conceptual understanding are related but not identical mathematical capabilities.

## 2. A working philosophical picture of mathematics

One intuition behind Mathia is that mathematical objects and theories can often be understood as representations built to capture recurring relationships.

We choose definitions, representations, equivalence relations, axioms, notation, and the particular statements we elevate into named theorems. In that sense, much of mathematical formalism is constructed. But once a representation and its rules are fixed, their consequences are not freely chosen: there remains a genuine discovery problem inside the structure.

A useful working picture is therefore:

```text
notice a pattern or relationship
        |
        v
choose what information matters
        |
        v
construct a representation / abstraction
        |
        v
explore its consequences
        |
        v
discover new relationships among those consequences
        |
        v
abstract or re-represent again
```

Mathematics then becomes, in part, a recursive process of turning relationships into objects, studying relationships between those objects, and constructing higher abstractions that compress the repeated structure.

This is not intended as a final philosophical position about what mathematics *is*. It is a productive research hypothesis about the kind of mathematical competence an AI might learn.

## 3. Mathematical understanding as finding the right representation

A recurring theme in the discussion is that deep mathematical reasoning may be less about executing longer chains of deductions and more about changing the space in which the problem is being considered.

Examples of such moves include:

- realizing that only a residue class matters, not the original integer;
- replacing individual elements by orbits or equivalence classes;
- seeing coprimality as a reversibility condition;
- quotienting out exactly the information a map cannot observe;
- choosing coordinates or a basis in which a transformation reveals its structure;
- interpreting a recurrence as iteration of a linear transformation;
- turning an arithmetic problem into a group-theoretic one;
- turning a complicated calculation into an invariant argument.

A compact formulation of the hypothesis is:

> A substantial part of mathematical intelligence may consist of finding a representation that forgets accidental information while preserving the structure relevant to the question.

This is closely related to the mathematical role of invariants, quotients, homomorphisms, canonical forms, coordinates, equivalence relations, universal properties, and abstraction more generally.

## 4. Two complementary layers

The current conceptual picture has two distinct but interacting mathematical roles.

### Conceptual layer — Mathia

This layer should ask questions such as:

- What is actually happening?
- Which information is essential and which is accidental?
- What is invariant?
- What can safely be forgotten?
- Which representation makes the phenomenon simple?
- Is the current assumption stronger than necessary?
- Is the same mechanism appearing somewhere else?
- Can ideas from different domains be composed?
- Is there a more natural or canonical construction?
- What conjecture should be true if this interpretation is correct?

### Formal layer — for example qwen-lean / Lean

This layer can ask:

- Can the idea be stated precisely?
- Does the conclusion really follow from the assumptions?
- Can a valid formal proof be constructed?
- Does a proposed weakening or generalization survive exact checking?
- Is a failure caused by a false conjecture, a bad formalization, or prover weakness?

A useful caricature is:

```text
Mathia:    what should be true, what is the right way to see it, and why?
Formal:    is it actually true, under exactly which assumptions, and how does it follow?
```

The relationship should not be one-way. Formal reasoning can expose hidden conditions, counterexamples, missing structure, or surprising consequences and therefore force the conceptual layer to revise its understanding.

The intended relationship is closer to:

```text
conceptual interpretation
        <->
formalization / derivation / verification
        <->
new evidence and surprises
        <->
revised conceptual interpretation
```

The formal layer should not prematurely dictate the representation used by the conceptual layer. Equally, the conceptual layer should not treat formal work as mere bureaucracy: exact derivation can itself generate new mathematical insight.

## 5. A hypothesis about training order, not yet a decision

One particularly interesting possibility is to train or post-train the conceptual model on top of a model that already has strong formal mathematical competence.

The optimistic hypothesis is that formal training supplies a dense substrate of mathematical facts, dependency structure, assumption sensitivity, definitions, and valid transformations, after which conceptual training teaches the model to compress this competence into higher-level representations.

Informally:

```text
formal competence
      ->
conceptual compression / abstraction
```

There is an important competing hypothesis: strong formal-first training might bias the model toward seeing every mathematical problem as a theorem-proving search problem — goals, lemmas, rewrites, tactics — and make it harder to question the representation itself.

This tension should remain empirical. Mathia should not silently assume that formal-first is necessarily the best ordering simply because a formal model already exists.

## 6. The target is not theorem explanation but conceptual mathematical action

A major refinement of the initial corpus idea is that **mathematical meta-description may be only the observable surface of the desired capability**.

The real target may be mathematical moves such as:

```text
recognize an invariant
identify what information can be discarded
find a reversible transformation
change representation
weaken an assumption
find the common mechanism behind several results
construct a bridge into another mathematical domain
compose two different ideas
propose a generalization
search for a counterexample
repair a failed conjecture
choose between competing viewpoints
find a more natural construction
```

This distinction matters because a model can learn to produce polished conceptual prose without learning to perform any of these operations.

A Wikipedia-style explanation tells us what an existing concept or theorem means. The Mathia hypothesis is stronger: a model should use conceptual representations to **do new mathematical work**.

## 7. Candidate dimensions of mathematical understanding

The discussion has produced a working set of behaviors that may help operationalize "understanding" without pretending that they form a final taxonomy.

### Compression

Explain many facts through a small number of ideas or mechanisms.

```text
many local results -> one structural explanation
```

### Prediction

Use a conceptual interpretation to anticipate consequences that were not explicitly supplied.

A description that cannot support any new prediction may be exposition rather than understanding.

### Transfer

Recognize the same mechanism when its superficial mathematical representation changes.

For example, reversibility or quotienting may appear in number theory, group theory, and linear algebra under very different notation.

### Counterfactual reasoning

Predict what should change when an assumption, object, or representation is modified.

The interesting question is not merely "which assumptions occur in the theorem?" but "what role does this assumption play, and what is the first thing that breaks when it is removed?"

### Generation

Suggest useful generalizations, intermediate lemmas, new questions, examples, counterexamples, or conjectures.

### Simplification

Find a representation from which a problem requires substantially less work.

This may be one of the clearest manifestations of "seeing beyond" the original formulation.

### Composition / synthesis

Combine distinct mathematical ideas or domains when neither one alone provides the right viewpoint.

For example, an arithmetic problem may become natural after constructing a group; a recurrence may become linear algebra; a group may be studied through a linear representation.

### Bridge construction

Invent or identify an intermediate object that translates a problem into a domain with better tools.

This is stronger than noticing an analogy. It constructs a mathematically useful connection.

### Reframing / multiple perspectives

Find genuinely different interpretations of the same mathematical phenomenon rather than merely paraphrasing the same explanation.

For example, rank-nullity can be viewed through bases, through lost versus surviving information, or through the quotient `V / ker(T) ≅ im(T)`. Different views make different questions easy.

### Perspective selection

Given several legitimate representations, choose the one that best serves the current goal.

Mathematical understanding is not simply owning many viewpoints; it includes knowing when each viewpoint is useful.

### Naturalness / canonicality

Distinguish constructions that arise intrinsically from the structure of the problem from constructions that depend on arbitrary proof choices.

For a map `T`, the equivalence relation "two inputs are equivalent when `T` cannot distinguish them" is not an arbitrary trick. It is induced by the question itself and leads naturally to quotienting by the kernel.

### Fertility

A good conceptual representation should *do work*. It should make some combination of prediction, transfer, simplification, generalization, composition, counterexample discovery, or proof easier.

Fertility may be more useful than eloquence as a criterion for conceptual quality.

## 8. Simplicity and mathematical beauty may carry information

Mathematicians often treat elegance as evidence that the correct structure has been found. A cumbersome proof can create the feeling that the theorem has been established without yet exposing the reason it is true. A later proof may remove cases, arbitrary choices, or local tricks and make the result appear inevitable.

Beauty here should **not** be reduced to proof length. A short proof can hide all of its content inside a powerful black-box theorem, while a longer proof can be much more explanatory.

The relevant aesthetic signals seem closer to:

- economy: few ideas explain many consequences;
- inevitability: once the viewpoint is found, the result looks structurally forced;
- symmetry: no unnecessary cases or privileged choices;
- naturalness: the objects introduced are demanded by the problem rather than invented ad hoc;
- minimal assumptions: the theorem says no more and assumes no more than the mechanism requires;
- unity: different parts of the argument are manifestations of one idea;
- surprising connection followed by explanation: previously separate phenomena become instances of the same structure.

A useful hypothesis is that mathematical beauty is sometimes the subjective signal of having found a highly compressed, fertile representation.

But this must remain a heuristic, not a correctness criterion. Some mathematics may be intrinsically complicated; some simple conceptual ideas require long formal implementations; and human aesthetic preferences can be culturally or historically contingent.

For Mathia, the interesting question is therefore not "can a model rate elegance?" but:

> Can a model prefer representations or proofs whose structural simplicity leads to more transfer, prediction, generalization, and reuse?

## 9. Examples of the kind of conceptual connection we care about

### Quotient as forgetting exactly the invisible information

For a linear map `T : V -> W`,

```text
T(v1) = T(v2)  <=>  v1 - v2 is in ker(T).
```

The kernel therefore captures exactly the distinctions that `T` cannot observe. Quotienting by the kernel removes precisely that invisible information, making

```text
V / ker(T) ≅ im(T)
```

conceptually natural rather than an isolated theorem.

The same high-level pattern appears in congruence classes and quotient groups, although the structures and compatibility conditions differ.

### Reversible simplification

The Euclidean algorithm repeatedly replaces a complicated pair of integers by a simpler pair while preserving the gcd. Gaussian elimination repeatedly replaces a system or matrix representation by a simpler one through controlled transformations while preserving the relevant solution structure.

The point is not that these algorithms are "the same". The transferable idea is:

> simplify the representation aggressively while preserving the invariant that answers the question.

### Moving a problem into another field

Fermat's little theorem can be approached as a statement about modular arithmetic, but the nonzero residue classes modulo a prime also form a finite multiplicative group. The group representation makes a broader structural mechanism visible.

Likewise a recurrence can be encoded as repeated application of a matrix, allowing eigenvalues and invariant subspaces to become relevant.

The conceptual move is not just analogy but changing mathematical language because another language makes the phenomenon simpler.

## 10. Understanding should be tested by consequences, not prose alone

A central danger is producing a model that sounds like a mathematician who understands deeply while merely reproducing the rhetoric of understanding.

Phrases such as

- "the quotient forgets irrelevant information";
- "this is really about symmetry";
- "the right invariant is...";
- "the theorem is natural from this viewpoint";

can themselves become stylistic clichés.

A stronger operational test is:

> After adopting this conceptual description, what mathematical question should the model now answer better that was not already answered literally in the description?

A useful representation should generate observable consequences. It may allow the model to:

- predict a theorem;
- weaken an assumption correctly;
- find a counterexample when the mechanism fails;
- transfer an idea to another domain;
- choose a shorter or more natural proof strategy;
- invent a useful intermediate construction;
- connect two previously separate topics;
- formalize a valid generalization.

This creates a potential bridge between subjective conceptual judgment and objective mathematical evidence.

## 11. AI feedback and formal feedback should remain different signals

Conceptual quality cannot currently be machine-verified in the same way as a Lean theorem. AI feedback may nevertheless be extremely useful for comparing candidate interpretations, criticizing shallow paraphrases, identifying promising conjectures, or ranking alternative viewpoints.

But an AI judge saying that an explanation is "deep" is not mathematical verification.

One promising principle is to prefer conceptual interpretations not only because a teacher likes their prose, but because they prove **fertile under intervention**: they generate correct predictions, useful generalizations, successful transfers, simplifications, or formally valid consequences.

Formal verification can therefore act as reality against which conceptual interpretations are tested without forcing the conceptual layer to think in a formal-language representation.

## 12. A mathematics-specialist model

The project is interested in a model whose intellectual task is essentially mathematics.

That does not necessarily imply pretraining from scratch on mathematics only. General language, code, science, and broad-world pretraining may provide useful representational priors for analogy, transformation, objects, causality, composition, and communication.

A more plausible working interpretation of "a model that only knows mathematics" is:

> retain a strong general pretrained substrate, but make the model's specialization and post-training world overwhelmingly mathematical.

Its experience could consist primarily of mathematical objects, problems, proofs, counterexamples, conceptual interpretations, alternative representations, conjectures, failed attempts, critiques, cross-domain connections, and formal feedback.

This too remains a hypothesis rather than a settled training choice.

## 13. Open tensions that should remain visible

The current synthesis leaves several important questions unresolved:

- Does strong formal training provide the best substrate for conceptual abstraction, or does it bias the model toward theorem-search representations?
- Can teacher-generated conceptual data teach genuine mathematical capability rather than a recognizable "deep explanation" style?
- How much of mathematical understanding can be externalized in natural language, and how much depends on latent internal representation?
- Can mathematical beauty, simplicity, or naturalness be used as training signals without rewarding fashionable rhetoric?
- How should competing conceptual interpretations be compared when several are valid for different purposes?
- How should the system value conjectures that are conceptually fruitful but not yet proved?
- How do we distinguish a false conjecture from failed formalization or prover weakness?
- How can we test cross-domain synthesis rather than merely memorized analogies?
- How can we measure whether a representation actually lowers mathematical problem complexity?
- How much should the formal and conceptual models share parameters, training history, or representations, if at all?

These are research questions, not missing implementation details.

## 14. Current synthesis in one sentence

A stronger formulation of the Mathia hypothesis is:

> **Deep mathematical reasoning may consist substantially of searching for, constructing, composing, and selecting representations in which many apparently different facts become simple manifestations of a small number of relationships; formal proof then tests and propagates the consequences of those representations, while feeding surprises back into conceptual understanding.**

Under this view, the unit we ultimately want to teach may not be the theorem, proof, or even the named concept. It may be a **way of seeing a mathematical situation**.

## 15. The next question

The next project discussion should move from *what capability are we trying to study?* to:

> **How could we construct a small experiment or training substrate that genuinely teaches and tests these capabilities?**

That discussion can consider source material, teacher generation, theorem neighborhoods, examples and counterexamples, alternative viewpoints, AI feedback, interaction with qwen-lean / Lean, and evaluation design.

It should still resist prematurely fixing a global architecture, rigid dataset schema, training pipeline, or project roadmap. The immediate goal is to discover what kind of concrete construction would distinguish **mathematical understanding** from explanation style and formal proof search.