# First mathematical world: modular structure and reversibility

This note makes the first Mathia experiment concrete enough to inspect and implement without turning it into a fixed dataset schema or training architecture.

The purpose is **not** yet to train Mathia. The purpose is to test whether a conceptual representation can have a measurable causal effect on later mathematical work.

The first world is deliberately small:

```text
divisibility
<-> gcd
<-> congruence
<-> residue classes
<-> units / invertibility
<-> permutations and cycles
<-> finite group structure
```

It is attractive because many claims can be checked exactly by exhaustive computation on small integers, while the world still contains genuine conceptual moves: invariants, forgetting information, reversibility, weakening assumptions, changing representation, decomposition, and bridges from arithmetic to algebra.

## 1. First question to answer

Before RL, ask a narrower causal question:

> If two mathematically different conceptual representations are inserted before the same unseen downstream tasks, do some representations systematically improve performance on those tasks?

This is stronger than asking whether a model can write an insightful explanation.

A useful conceptualization should change what can be done next.

## 2. Do not let the first experiment collapse into self-generated scratchpad

A simple protocol would be confounded:

```text
model writes conceptualization
        ->
same model keeps reasoning
        ->
model solves hidden task
```

Any gain could come from extra tokens, self-consistency, or ordinary chain-of-thought rather than from a better representation.

The initial signal-validation study should therefore treat the conceptualization as an **intervention**.

For each mathematical situation:

1. create several candidate conceptualizations independently;
2. freeze them before hidden tasks are selected;
3. give each candidate, in randomized order, to fixed solver/evaluator instances;
4. ask those solvers to answer the same held-out tasks;
5. score the answers mechanically where possible;
6. estimate the uplift caused by each conceptualization relative to controls.

Conceptually:

```text
same visible mathematics
       |
       +--> C1 --------+
       +--> C2 --------+--> same hidden task family --> exact score
       +--> C3 --------+
       +--> controls ---+
```

The object of interest is not whether `C1` sounds deeper than `C2`, but whether conditioning on `C1` improves mathematically relevant behavior.

## 3. Essential controls

Each hidden task should be tested under several context conditions with approximately matched token budgets where practical.

### No conceptual context

The solver receives the mathematical situation and hidden task only.

This measures ordinary solver competence.

### Factual summary

A correct but non-structural restatement of the visible facts.

This controls for simply receiving more relevant tokens.

### Procedural note

A useful solution recipe or local trick that does not claim to expose a reusable mechanism.

This is a strong adversarial control: perhaps procedures outperform conceptual abstraction.

### Structural conceptualization

A candidate explanation of the mechanism: invariant, reversibility, quotient, decomposition, etc.

### Fluent but sterile conceptualization

Mathematically plausible prose that uses the rhetoric of depth but makes weak predictions.

Example:

> "At heart this phenomenon reflects a deep harmony between arithmetic structure and symmetry."

This checks whether evaluators or models merely reward style.

### Wrong-but-plausible conceptualization

A near-miss designed to make a specific false prediction.

This tests whether hidden interventions can actually falsify representations rather than merely decorate solutions.

### Shuffled conceptualization

A good conceptualization from another situation in the same world.

This checks whether any mathematical-sounding context helps regardless of relevance.

## 4. Hidden task families

The conceptualization is committed before the exact downstream family is revealed.

### Prediction

Infer a consequence not shown in the visible material.

### Counterfactual / assumption change

Change an assumption and predict what survives, what fails, and why.

### Counterexample

Find or select a small case that breaks an over-general interpretation.

### Transfer

Recognize the same mechanism under different notation or in a neighboring domain.

### Simplification

Choose or construct a representation that reduces the work required.

### Generalization

Propose the smallest stronger statement suggested by the mechanism.

### Composition / bridge construction

Move the problem into a different mathematical language when that language exposes useful structure.

### Diagnosis

Given a failed conjecture or failed analogy, identify which part of the conceptual model was wrong.

The first study does not need every situation to support every task family.

## 5. Seed situation A: Euclidean invariance

### Visible material

Show several chains such as

```text
gcd(84, 30) = 6
gcd(30, 24) = 6
gcd(24, 6)  = 6
```

with the transformations

```text
(84, 30) -> (30, 84 - 2*30) = (30, 24)
(30, 24) -> (24, 30 - 24)   = (24, 6)
```

and analogous examples with different integers.

Do not initially state the general identity.

### Structural candidate

> Replacing one number by itself minus an integer multiple of the other changes the description of the pair but preserves the set of common divisors. We can simplify aggressively while preserving exactly the invariant relevant to gcd.

### Procedural candidate

> Repeatedly divide the larger number by the smaller one and keep the remainder until the remainder is zero.

Both are useful, but they encode different kinds of knowledge.

### Hidden interventions

- predict whether `gcd(a,b) = gcd(b,a-qb)` should hold for arbitrary integer `q`;
- choose which transformations preserve gcd among several candidates;
- transfer the idea to a deliberately unfamiliar pair-reduction problem where an invariant, not the Euclidean algorithm itself, is what matters;
- diagnose why replacing `a-qb` by an unrelated smaller number can make the procedure faster yet invalid;
- ask whether the conceptual note or procedural note better supports a new proof that two different algorithms preserve the same gcd.

### Exact verification

Exhaustive integer tests over bounded ranges plus symbolic ground truth for the standard identity.

## 6. Seed situation B: multiplication modulo n as reversible action

### Visible material

For several moduli, show maps on residue classes.

For example modulo 10:

```text
x -> 3x mod 10   is a permutation
x -> 7x mod 10   is a permutation
x -> 2x mod 10   collapses residues
x -> 5x mod 10   collapses residues
```

Include prime and composite moduli so that "the modulus must be prime" is an attractive but false explanation.

### Structural candidate

> The decisive property is reversibility. Multiplication by `a` permutes residue classes exactly when `a` has a multiplicative inverse modulo `n`; primality of `n` is only one way to make many nonzero elements invertible.

### Plausible near-miss

> Nonzero multipliers permute nonzero residue classes.

This is true over a prime modulus and false in general.

### Hidden interventions

- classify unseen `(a,n)` pairs as bijective or non-bijective;
- infer that coprimality, not primality, is the relevant condition;
- predict when cancellation `ax = ay (mod n) => x = y (mod n)` is valid;
- transfer from multiplication to affine maps `x -> ax+b (mod n)`;
- predict whether iteration has only cycles or can contain tails/collapse;
- construct the smallest counterexample to the nonzero-multiplier near-miss.

### Exact verification

Enumerate residue maps and compare with `gcd(a,n) = 1`.

## 7. Seed situation C: cancellation is the same reversibility question

### Visible material

Give examples such as

```text
3x = 3y (mod 8)  -> x = y (mod 8)
2x = 2y (mod 8)  does not force x = y (mod 8)
```

and several other moduli.

### Structural candidate

> Cancellation is not a separate modular trick. It is exactly the question of whether multiplication by the coefficient is injective, hence reversible, on residue classes.

### Hidden interventions

- predict the exact condition for cancellation modulo `n`;
- recognize that this is the same mechanism as the permutation situation despite a different surface question;
- transfer the idea to solving `ax = b (mod n)`;
- distinguish "coefficient nonzero" from "coefficient invertible".

This situation is useful for testing **compression and transfer inside one domain**: two theorem families should become one mechanism.

## 8. Seed situation D: solving ax = b modulo n as image/kernel structure

### Visible material

Show examples where `ax = b (mod n)` has zero, one, or multiple residue-class solutions.

For example modulo 12:

```text
5x = 7  has one solution
4x = 8  has four solutions
4x = 6  has no solution
```

### Structural candidate

> Multiplication by `a` is a map on the finite residue space. Its kernel measures how much information the map collapses; its image determines which right-hand sides are reachable. Non-invertibility does not merely mean "failure": it predicts both repeated solutions and unreachable values.

This deliberately anticipates later linear-algebra language without requiring it as the initial formalism.

### Hidden interventions

- infer the solvability condition `gcd(a,n) | b` from examples;
- predict the number of solutions when solvable;
- connect multiple solutions and missing outputs to the same collapse mechanism;
- transfer to a small finite abelian group presented without modular notation;
- later compare whether a model trained on this idea transfers more naturally to kernels/images of linear maps.

### Exact verification

Enumerate all residues and count preimages.

## 9. Seed situation E: congruence as deliberate forgetting

### Visible material

Show integers partitioned into classes modulo several moduli and examples where addition and multiplication can be performed using representatives.

### Structural candidate

> Passing modulo `n` intentionally forgets differences by multiples of `n`. The quotient is useful because the operations we care about respect that loss of information: changing representatives does not change the resulting class.

### Hidden interventions

- decide whether a proposed equivalence relation supports a well-defined induced operation;
- explain why representative choice is irrelevant in valid quotient operations;
- distinguish a relation that is an equivalence relation from one that is also compatible with the operation;
- transfer the idea to a toy quotient of an additive group;
- diagnose a deliberately invalid quotient-like construction.

Some of these checks may initially be generated from finite tables so well-definedness can be verified exhaustively.

## 10. Seed situation F: finite dynamics — cycles versus collapse

### Visible material

Show repeated iteration of maps such as

```text
x -> ax mod n
```

for both units and non-units.

For units, every state lies on a cycle because the map is a permutation. For non-units, different states can merge and transient tails can appear.

### Structural candidate

> In a finite state space, reversibility rules out merging. A reversible deterministic map decomposes the space entirely into cycles; once information can be lost, tails and collapsed trajectories become possible.

### Hidden interventions

- predict qualitative orbit structure from `gcd(a,n)` without tracing every orbit;
- transfer the cycle argument to an arbitrary finite permutation written with unfamiliar labels;
- distinguish periodicity caused by finiteness from pure-cycle behavior caused by bijectivity;
- compose the modular arithmetic view with permutation/group language.

### Exact verification

Enumerate functional graphs for small moduli.

## 11. Seed situation G: Chinese-remainder decomposition

This introduces a second major motif so that the world does not collapse into "everything is reversibility".

### Visible material

Show examples where a residue modulo `mn` is completely determined by its residues modulo `m` and `n`, and examples where naive decomposition loses information.

### Structural candidate

> When the moduli are coprime, two local views carry independent information and together reconstruct the global residue. The hard arithmetic problem can be decomposed into smaller components and recombined.

### Plausible near-miss

> Residues modulo `m` and `n` always determine the residue modulo `mn`.

### Hidden interventions

- distinguish coprime from non-coprime decompositions;
- find collisions when the pair of local views loses information;
- transfer the idea from residue arithmetic to a product representation of a finite structure;
- solve a problem more cheaply by splitting it into components;
- compare the conceptual motif of **decomposition** against the earlier motif of **reversible transformation**.

### Exact verification

Enumerate the map

```text
x mod mn -> (x mod m, x mod n)
```

and test injectivity/surjectivity.

## 12. Seed situation H: from arithmetic to group language

### Visible material

Present the invertible residues modulo `n` only through arithmetic examples: closure under multiplication, an identity, inverses, and repeated powers.

Do not initially label the structure a group.

### Structural candidate

> The invertible residue classes form a closed system of reversible composable transformations. Group language is not merely a relabeling: it packages exactly the structure needed to reason about repeated multiplication, orders, cycles, and symmetry.

### Hidden interventions

- identify which arithmetic facts become immediate from finite-group structure;
- infer that powers of a unit eventually return to the identity;
- transfer an argument about cycles/orders to a permutation group with no arithmetic notation;
- decide when moving to group language simplifies the problem and when it adds abstraction without benefit;
- compare an arithmetic proof and a group-theoretic proof for reuse/generalization.

This is the first explicit test of **bridge construction and perspective selection**.

## 13. What the first hand-designed set should contain

Do not immediately generate thousands of instances.

Start with roughly 20–50 carefully inspected situations drawn from the motifs above, with multiple hidden interventions per situation.

The set should intentionally contain:

- structurally similar problems with very different notation;
- superficially similar problems with different mechanisms;
- prime/composite contrasts;
- reversible/non-reversible contrasts;
- valid and invalid quotient-like constructions;
- good abstractions and over-general abstractions;
- cases where a procedural recipe is better than an abstract viewpoint;
- cases where the abstract viewpoint produces transfer or generalization that the recipe does not.

The goal is discrimination, not coverage.

## 14. First pre-RL experiment

For each hand-designed situation:

1. produce 4–8 candidate contexts spanning the control types above;
2. have independent teacher models critique them but do not collapse them to one gold answer;
3. commit the contexts;
4. sample held-out interventions not shown to the context generator;
5. evaluate each context on the same intervention set using one or more fixed solver models;
6. use exact computation to score objective outputs;
7. separately collect AI/human judgments of elegance, naturalness, compression, and explanatory quality;
8. compare subjective quality with downstream mathematical uplift.

The key quantity is a causal-style paired difference such as

```text
score(hidden tasks | structural context)
-
score(hidden tasks | matched control context)
```

not the absolute solver score.

## 15. Important failure modes to look for immediately

### Extra-token effect

Any coherent mathematical context improves performance equally.

If so, the signal is not conceptual.

### Solution leakage

The best conceptualization simply contains the answer pattern for the hidden tasks.

If so, hidden-task generation or commitment boundaries are weak.

### Judge-style bias

AI judges prefer elegant prose that does not improve objective tasks.

This is expected to some extent and should be measured rather than hidden.

### Universal-cliche collapse

The same phrase — "reversibility", "symmetry", "quotient", "invariant" — is rewarded across unrelated situations.

Near-miss and shuffled controls should punish this.

### Base-model ceiling

All hidden tasks are already trivial for the solver, leaving no room for conceptual context to help.

Tasks then need to be harder, more compositional, more transfer-heavy, or more synthetically re-represented — not merely numerically larger.

### Context-overfitting

A conceptualization helps only tasks whose wording resembles the visible material.

Cross-notation and cross-domain transfer tests should expose this.

### Abstraction tax

A beautiful high-level representation performs worse than a local procedural rule on some tasks.

This is not necessarily failure. A good mathematical reasoner should learn when abstraction pays for itself and when it does not.

## 16. What would count as a promising signal

Before training, evidence would be encouraging if:

- structural conceptualizations consistently beat token-matched factual summaries on some held-out task families;
- the gains are largest on transfer, assumption changes, composition, or generalization rather than simple arithmetic recall;
- irrelevant or wrong-but-plausible conceptualizations measurably hurt;
- procedural notes win where procedure is genuinely the best representation, rather than structural prose winning by default;
- conceptual quality judgments correlate imperfectly but meaningfully with downstream fertility;
- at least some useful representations outperform the teacher's initially preferred explanation.

The last point matters because it demonstrates that teacher preference is not the ceiling of the experiment.

## 17. What comes after signal validation

Only if this first environment discriminates useful representations should the project commit to a cold-start format and RL implementation.

At that point the natural next experiment is to train a model to **choose or construct contexts that maximize future hidden-task reward**, while keeping the exact future intervention unknown at commitment time.

Qwen-lean is not required for this world. Later it can extend the reward from exhaustive finite checks to formally verified theorem weakening, generalization, lemma generation, and proof assistance.

## 18. Current status

This document is a hand-designed experimental hypothesis, not a final dataset specification.

The immediate engineering task, if we choose to proceed, is small:

> implement enough of this world to generate and exactly verify the seed situations and hidden interventions, then run the pre-RL causal-context study on existing models before training anything.
