# Intuition-fertility theorem panel v0

## Status and use

This file instantiates the design in `INTUITION_FERTILITY_PRETEST_V0.md` on a small candidate panel. It is an audit artifact for issue #30, not training data and not the final frozen #32 prompt set.

The `Mathia-visible statement` and `factual control` fields below are candidates for the primary pre-test. The `audit-only strategic reference` is intentionally private from the intuition generator. It exists so reviewers can judge whether the task admits a compact strategy that is neither empty rhetoric nor a near-complete proof.

The actual Codex/reference intuitions in #32 must be freshly generated under the frozen protocol; they must not be copied from this file.

No candidate is finally accepted until its exact qwen-lean Phase-2 split/training exposure is resolved. A target used in qwen-lean optimizer training must be replaced under #30 rather than silently retained.

## Common intuition request

Each Mathia-visible statement is preceded by the same semantic request:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and at most one or two useful intermediate mathematical goals. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof, Lean code, tactic names, or library theorem names.

The theorem name and private formal target are not shown to the intuition generator.

---

## Candidate A — subgroup cardinality / quotient decomposition

**Private formal target:** `Subgroup.card_subgroup_dvd_card`

**Private source:** `Mathlib/GroupTheory/Coset/Card.lean`

**Role:** easy/floor channel calibration.

### Mathia-visible statement

Let `G` be a finite group and `H` a subgroup of `G`. Explain a strategy for showing that the cardinality of `H` divides the cardinality of `G`.

### Factual control

`H` is a subgroup of the finite group `G`. The target compares the cardinality of `H` with the cardinality of `G` through a divisibility relation.

### Audit-only strategic reference

Look for a representation of `G` as equally sized pieces determined by `H`. The subgroup acts as the repeated local piece, while a quotient-like set indexes how many such pieces occur. If these pieces exhaust `G` without overlap, the desired divisibility becomes a structural consequence of that decomposition rather than an arithmetic calculation.

### Dimension coverage

`decompose`, `reframe/bridge`, with quotient semantics.

### Main leakage risk

The strategy is standard enough that a long response can easily become the full coset proof. Keep it at the partition/indexing mechanism.

---

## Candidate B — rank, kernel, and surviving information

**Private formal target:** `LinearMap.rank_range_add_rank_ker`

**Private source:** `Mathlib/LinearAlgebra/Dimension/RankNullity.lean`

**Role:** medium representation-change calibration.

### Mathia-visible statement

Let `f : M → M'` be a linear map in a setting where the relevant module ranks and the ambient hypotheses of the result are available. Explain a strategy for showing that the rank of the range of `f`, together with the rank of the kernel of `f`, accounts for the rank of `M`.

### Factual control

The kernel and range are the two substructures associated with the same linear map `f`. The target relates their ranks to the rank of the domain `M`.

### Audit-only strategic reference

Interpret the kernel as exactly the distinctions in the domain that `f` cannot observe. Collapse those distinctions first. The resulting quotient should retain precisely the information that survives under `f`, so it should be naturally identifiable with the range. The rank statement can then be organized as the decomposition of the domain into forgotten information and surviving information.

### Dimension coverage

`abstract/compress`, `reframe/bridge`, `decompose`, with information-loss semantics.

### Main leakage risk

Naming the exact quotient-to-range library equivalence or giving the final rewrite chain would cross from strategy into implementation.

---

## Candidate C — orbit and stabilizer as redundancy

**Private formal target:** `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`

**Private source:** `Mathlib/GroupTheory/GroupAction/Quotient.lean`

**Role:** medium transfer test.

### Mathia-visible statement

Let a finite group `G` act on a set, and let `x` be a point. Explain a strategy for relating the cardinality of the orbit of `x` and the cardinality of the stabilizer of `x` to the cardinality of `G`.

### Factual control

The orbit of `x` contains the points reachable from `x` by the action of `G`. The stabilizer contains the elements of `G` that leave `x` fixed. The target relates the finite cardinalities of these objects and `G`.

### Audit-only strategic reference

View a group element only through what it does to `x`. Different elements become indistinguishable exactly when their difference is motion that fixes `x`. Thus the stabilizer measures redundancy in the map from group elements to orbit positions, and the orbit should be represented by the corresponding quotient. Counting the effective positions and the redundant motions gives the structural factorization.

### Dimension coverage

`transfer`, `reframe/bridge`, `decompose`, with symmetry/quotient semantics.

### Main leakage risk

Because the target follows from a standard quotient equivalence, a response that supplies the exact equivalence and cardinality rewrite is too implementation-like.

---

## Candidate D — two injections and a piecewise bijection

**Private formal target:** `Function.Embedding.schroeder_bernstein_of_rel`

**Private source:** `Mathlib/SetTheory/Cardinal/SchroederBernstein.lean`

**Role:** hard proof-bearing item.

### Mathia-visible statement

Let `f : A → B` and `g : B → A` be injective maps. Let `R` be a relation between `A` and `B` such that `R(a, f(a))` holds for every `a`, and `R(g(b), b)` holds for every `b`. Explain a strategy for constructing a bijection `h : A → B` for which `R(a, h(a))` holds for every `a`.

### Factual control

There is an injection in each direction between `A` and `B`. The relation `R` already holds along the pairs supplied by `f` and by `g`. The target asks for a bijection that also respects `R` pointwise.

### Audit-only strategic reference

A single global choice of the forward map or the inverse direction need not work. Search instead for a stable partition of `A`: on one region use `f`, and on the complementary region use the uniquely recoverable preimage supplied by injectivity of `g`. The key subproblem is to define the region so the two image pieces are disjoint and exhaustive; the relation condition is then inherited branchwise.

### Dimension coverage

`decompose`, `synthesize`, `reframe/bridge`, `stress-test`.

### Main leakage risk

Specifying the exact fixed-point operator, all set identities, or the piecewise bijection proof in detail would be a near-proof. The strategic object is the stable partition and two-branch construction.

---

## Candidate E — matching by slack versus tightness

**Private formal target:** `HallMarriageTheorem.hall_hard_inductive`

**Private source:** `Mathlib/Combinatorics/Hall/Finite.lean`

**Role:** hard proof-bearing item.

### Mathia-visible statement

A finite family assigns to each index a finite set of allowed representatives. Assume every subfamily collectively has at least as many available representatives as it has indices. Explain a strategy for constructing an injective choice that assigns each index an allowed representative.

### Factual control

Each index has a finite set of allowed representatives. Every subfamily satisfies the stated cardinality condition, and the target is an injective choice taking each index to one of its allowed representatives.

### Audit-only strategic reference

The Hall condition suggests testing whether it is ever tight. If some proper nonempty subfamily uses exactly all the capacity available to it, treat that block as a self-contained constrained problem and solve the complement with those representatives removed, then combine. If no such tight block exists, there is slack everywhere, which should let one commit a representative for one index and recurse after removing that choice.

### Dimension coverage

`stress-test`, `decompose`, `synthesize`, `generalize/weaken`.

### Main leakage risk

A complete induction with all cardinality inequalities is the proof. The intuition should stop at the tight-block/slack dichotomy and recursive organization.

---

## Candidate F — compactness transported through a map

**Private formal target:** `IsCompact.image_of_continuousOn`

**Private source:** `Mathlib/Topology/Compactness/Compact.lean`

**Role:** representation/domain diversity item.

### Mathia-visible statement

Let `s` be a compact subset of a topological space and let `f` be continuous on `s`. Explain a strategy for showing that the image of `s` under `f` is compact.

### Factual control

The set `s` is compact, the map `f` is continuous on `s`, and the target concerns compactness of the image of `s` under `f`.

### Audit-only strategic reference

Treat compactness through a characterization that can be transported along maps rather than by manipulating points individually. Pull the relevant cover/filter/cluster structure on the image back to the source, invoke compactness there, and use continuity to push the resulting finite or limiting witness forward. The useful representation is whichever compactness characterization makes this pullback/pushforward pattern direct.

### Dimension coverage

`transfer`, `reframe/bridge`, `select`, with preservation-under-map semantics.

### Main leakage risk

The reference deliberately leaves open which compactness characterization to use. Giving the exact filter construction from the library proof would overfit the formal implementation rather than the conceptual strategy.

---

## Cross-theorem strategy control

After the panel is frozen, use a deterministic derangement rather than randomly selecting an obviously unrelated hint. The initial pairing should stress conceptual overlap:

- subgroup-cardinality strategy ↔ orbit/stabilizer strategy;
- rank/kernel strategy ↔ compact-image transport strategy;
- two-injections strategy ↔ Hall matching strategy.

Each member receives the partner's frozen strategy in the `cross_theorem_strategy` condition. These are intentionally strong controls: some may help because the mechanisms genuinely transfer. Such an effect is reported as transfer rather than retroactively declaring the control invalid.

## Genericity variants

For intuition generation, each retained theorem should have at least one presentation variant that changes incidental notation or phrasing while preserving the mechanism. The variant must not alter the private formal target or the qwen-lean proof request. Examples include renaming maps and carrier types, swapping `kernel`/`range` prose for `forgotten`/`surviving` information while retaining definitions, or expressing orbit/stabilizer through action-equivalence language.

The purpose is not to create a large augmented benchmark. It is to detect dependence on theorem names and surface templates before interpreting strategic output as conceptual behavior.

## Panel acceptance checklist

Before #30 can freeze this file as the panel contract:

- resolve exact qwen-lean Phase-2 record identity and split for each private target;
- remove/replace any target exposed to optimizer training by the chosen qwen-lean checkpoint;
- verify that every Mathia-visible statement is faithful to the private target;
- verify that no Mathia-visible statement depends on concrete numeral instances;
- independently classify each audit-only reference as strategic rather than proof-like;
- check that factual controls do not add a useful representation or subgoal;
- audit the cross-theorem pairing for trivial topic/style cues;
- run a fresh-context adversarial review before implementation.
