# Intuition-fertility theorem panel v1

## Status

This is the **current exact theorem-panel design target for issue #30**, pending fresh-context independent adversarial review. It supersedes `INTUITION_FERTILITY_PANEL_V0.md`, whose original six candidates were rejected for the Phase-5 line after five were found in qwen-lean optimizer training.

All six primary v1 targets below were checked in the actual qwen-lean Phase-2 artifact as `heldout`, reconstruct correctly in pinned mathlib, and have Lean-accepted retained proofs. No Qwen/qwen-lean inference was used to choose them. `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` remains a separate clean heldout **calibration** target because its retained proof is short/wrapper-like.

The panel tests whether theorem-specific strategic guidance changes verified whole-proof generation. Private proof mechanisms and audit references in this file must not be exposed to the intuition generator.

## Common intuition request

Every Mathia-visible theorem presentation receives exactly this semantic request:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and a small number of useful intermediate mathematical goals if needed. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof.

The generator must not receive the private declaration name, source file, retained proof, neighboring source lemmas, audit-only strategy reference, or qwen-lean output.

Disallowed primary outputs include Lean code, tactic names, library identifiers, a line-by-line derivation, or an informal proof so complete that the downstream prover is left mainly with transcription.

## Generic strategy control

Use the same theorem-independent strategy-shaped control for every target:

> Search for a structural viewpoint that makes the conclusion natural. Identify one useful representation, decomposition, invariant, or intermediate object and a small number of subgoals suggested by it. Prefer a viewpoint that removes irrelevant detail. Do not write the proof.

This controls a generic `think structurally` / extra-deliberation effect without naming a theorem-specific mechanism. Exact Lean-comment escaping and final token budget belong to #31/#32; the mathematical content above is frozen by #30.

## Primary A — analytic local-to-global identity

**Private formal target:** `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux`

**Record:** `b02d73078afb5b4319abc67810e0ae8efa2ce6960dea2d4a8445f6f422d9437b`

**Private source:** `Mathlib/Analysis/Analytic/Uniqueness.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `E` and `F` be normed spaces in a setting where analytic maps between them are defined, and assume `F` is complete. Let `U` be a preconnected subset of `E` and let `f : E → F` be analytic in a neighborhood of every point of `U`. Assume there is a point of `U` near which `f` agrees with the constant zero function. Show that `f` agrees with the constant zero function throughout `U`.

### Factual control

`F` is complete, `U` is preconnected, `f` is analytic near every point of `U`, and near one point of `U` it agrees with the constant zero function. The target is equality with that function on all of `U`.

### Audit-only strategic reference

Treat local vanishing as a property that can propagate through the connected region. Analytic uniqueness should prevent the region where vanishing has propagated from stopping at an interior boundary; organize the argument so preconnectedness converts local agreement into global agreement.

### Intended move coverage

`stress-test`, `abstract/compress`, local-to-global transfer.

### Leakage boundary

A response that states the exact source lemma chain, constructs the exact open/closed sets used by the retained proof, or gives the full analytic continuation derivation is proof-like. The strategic content is the propagation mechanism and why connectedness prevents a boundary.

### Exact genericity variant

Let `X` and `Y` be normed spaces in the same analytic setting, with `Y` complete. Let `V` be preconnected and let `g : X → Y` be analytic near every point of `V`. Suppose some point of `V` has a neighborhood on which `g` is the constant zero function. Show that `g` is the constant zero function on all of `V`.

---

## Primary B — separation of generalized eigenspaces

**Private formal target:** `Module.End.disjoint_genEigenspace`

**Record:** `9db61d80db52314e83addee2d556253ee17ad710d1a597725a0a6390d2009073`

**Private source:** `Mathlib/LinearAlgebra/Eigenspace/Basic.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `T` be an endomorphism of a torsion-free module over a domain, and let `λ` and `μ` be distinct scalars. For any allowed generalized-eigenspace depths `k` and `l`, show that the generalized eigenspace of `T` for `λ` at depth `k` and the generalized eigenspace for `μ` at depth `l` have trivial intersection.

### Factual control

The same endomorphism `T` determines generalized eigenspaces for two distinct scalars `λ` and `μ`, at arbitrary specified depths. The target is that the two submodules have only the trivial intersection.

### Audit-only strategic reference

Suppose a vector lies in both generalized eigenspaces and focus on the common substructure. Suitable powers of the two shifted operators then act nilpotently there. Their difference is controlled by the nonzero scalar `μ - λ`; distinctness together with the domain/torsion-free assumptions should make those two nilpotence behaviors incompatible except on the trivial vector.

### Intended move coverage

`stress-test`, `decompose`, `select`.

### Leakage boundary

Naming the exact polynomial identity, exponent manipulation, or library lemmas that discharge the nilpotence contradiction is proof-like. A strategic intuition may identify incompatible shifted-operator behavior and the role of scalar distinctness.

### Exact genericity variant

Let `S` be an endomorphism of a torsion-free module over a domain and let `α` and `β` be distinct scalars. Fix any permitted depths `p` and `q`. Consider vectors eventually annihilated by repeated application of `S - α` at depth `p`, and vectors eventually annihilated by repeated application of `S - β` at depth `q`. Show that the two resulting submodules have trivial intersection.

---

## Primary C — independence across a disjoint index sum

**Private formal target:** `linearIndependent_sum`

**Record:** `5751f369a1e80a5ebcf31574d28dd7a3b9b20c65d841fce0294f780562bd73e6`

**Private source:** `Mathlib/LinearAlgebra/LinearIndependent/Basic.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `v` be a family of vectors indexed by the disjoint sum of two index types. Show that the whole family is linearly independent if and only if the restriction to each side is linearly independent and the submodules spanned by the ranges of the two restrictions are disjoint.

### Factual control

The family has one restriction to each side of a disjoint index sum. The target is an equivalence between independence of the combined family and independence of both restrictions together with disjointness of their spans.

### Audit-only strategic reference

A finite linear relation on the combined family splits canonically into a contribution from each side. If each side is independently rigid, the only remaining way the contributions can cancel is through a common vector in the two spans. Disjointness removes that cross-cancellation channel; conversely, independence of the whole family forces both local independence and separation of the spans.

### Intended move coverage

`decompose`, `synthesize`, `abstract/compress`.

### Leakage boundary

Writing the complete finite-support coefficient argument in both directions is proof-like. The strategic object is decomposition of a global relation into two pieces plus identification of span intersection as the only cross-cancellation mechanism.

### Exact genericity variant

Let `(a_i)` and `(b_j)` be two tagged families of vectors whose index sets are disjoint. Form the combined tagged family. Show that it is linearly independent exactly when each original family is linearly independent and the spans of the two families have trivial intersection.

---

## Primary D — finite graph consistency to a global homomorphism

**Private formal target:** `SimpleGraph.Finsubgraph.nonempty_hom_of_forall_finite_subgraph_hom`

**Record:** `9a0191efa6271a14b1aa05a9b3d422d207d1193899daf8ef955cbe9a2e0440ae`

**Private source:** `Mathlib/Combinatorics/SimpleGraph/Finsubgraph.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `G` and `F` be graphs, with the vertex type of `F` finite. Assume that every subgraph of `G` having finitely many vertices admits a graph homomorphism into `F`. Show that there exists a graph homomorphism from all of `G` into `F`.

### Factual control

`F` has finitely many vertices. Every finite-vertex subgraph of `G` has at least one graph homomorphism into `F`. The target is existence of a graph homomorphism from `G` itself into `F`.

### Audit-only strategic reference

View a partial graph homomorphism as a finite constraint assignment. Every finite collection of constraints is satisfiable by assumption. Because target choices live in a finite space, search for a compactness/coherence principle that selects assignments compatible across all finite restrictions and assemble their common limit into one global homomorphism.

### Intended move coverage

`abstract/compress`, `synthesize`, `reframe/bridge`, local-to-global transfer.

### Leakage boundary

Specifying the exact inverse-system objects, filters, ultrafilters, or library compactness theorem used by mathlib is implementation-level. The strategy may identify finite satisfiability plus compactness/coherent choice as the mechanism.

### Exact genericity variant

Let `H` be a source graph and `K` a graph with finite vertex type. Suppose every finite-vertex subgraph of `H` admits a homomorphism into `K`. Show that the entire graph `H` admits a homomorphism into `K`.

---

## Primary E — local diamonds to global confluence

**Private formal target:** `Relation.ReflGen.SymmGen.ReflTransGen.TransGen.EqvGen.church_rosser`

**Record:** `92d6b286e0d3754888b472b5b8b3f488715970a8f1dca537c3f5bb10ed9934cc`

**Private source:** `Mathlib/Logic/Relation.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `r` be a reduction relation. Assume that whenever one object makes two direct `r`-steps to two successors, the branches can be joined so that one successor needs at most one further `r`-step and the other needs only finitely many `r`-steps. Show that whenever two objects are each reachable from a common start by finitely many `r`-steps, the two endpoints have a common descendant reachable from each by finitely many `r`-steps. Zero-step reachability is allowed.

### Factual control

The premise gives a joinability condition for every direct fork of the relation `r`. The target gives a joinability condition for endpoints of arbitrary finite reduction sequences starting at the same object.

### Audit-only strategic reference

Promote the direct-fork property along longer reduction paths. Isolate a first step, use the local joining hypothesis against the competing branch, and apply an induction/closure argument to the remaining reductions. The conceptual move is to show that the local diamond property is stable under composition of reduction steps.

### Intended move coverage

`transfer`, `synthesize`, `generalize/weaken`, local-to-global reasoning.

### Leakage boundary

A complete induction with every constructor of the reflexive-transitive closure is proof-like. Strategic guidance may identify the induction direction and closure-under-composition mechanism without enumerating formal cases.

### Exact genericity variant

Let `→` be a relation. Suppose every pair of one-step paths from the same source can be joined, with one branch requiring no more than one additional step and the other a finite path. If `y` and `z` are reached from `x` by finite paths, allowing empty paths, show that `y` and `z` can each reach a common object by finite paths.

---

## Primary F — measurable events depend on countably many coordinates

**Private formal target:** `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable`

**Record:** `7ee0d231a646406fb0e6adea92cbca454ed339175fcd0d2c83bda918064cc795`

**Private source:** `Mathlib/MeasureTheory/Constructions/Cylinders.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let a family of measurable spaces be indexed by an arbitrary type, and let `s` be a measurable subset of their product. Show that there is a countable set of coordinates `I` and a subset `t` of the product restricted to `I` such that `s` is exactly the preimage of `t` under the coordinate-restriction map. Thus membership in `s` depends only on the coordinates in `I`.

### Factual control

`s` is measurable in a product measurable space. The target is existence of a countable coordinate set and a restricted-product subset whose inverse image under coordinate restriction is exactly `s`.

### Audit-only strategic reference

Consider the class of product subsets whose membership is determined by countably many coordinates. Show that this class is closed under the operations used to generate the product measurable structure and contains the basic measurable cylinders. Then every measurable set inherits such a countable support.

### Intended move coverage

`abstract/compress`, `synthesize`, `generalize/weaken`.

### Leakage boundary

Listing the exact measurable-space induction constructors and corresponding set identities is proof-like. The strategic intuition is to turn “depends on countably many coordinates” into a property preserved by measurable-set generation.

### Exact genericity variant

Let `(Y_j)` be measurable spaces indexed by a type `J`, and let `A` be a measurable subset of their product. Show that there is a countable subset `K` of `J` and a subset `B` of the product over `K` such that `A` is the inverse image of `B` under restriction to `K`. Equivalently, changing coordinates outside `K` cannot change membership in `A`.

---

## Calibration G — orbit/stabilizer cardinality

**Private formal target:** `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`

**Record:** `60b1a7986f6f4b88449378e1d397c3e717b2e9d2e29d21efe11d73ff443a7c41`

**Private source:** `Mathlib/GroupTheory/GroupAction/Quotient.lean`

**Phase-2 status:** `CLEAN_HELDOUT`, but retained proof is short/wrapper-like.

### Mathia-visible statement

Let a finite group `G` act on a set and let `x` be a point. Show that the cardinality of the orbit of `x` multiplied by the cardinality of the stabilizer of `x` equals the cardinality of `G`.

### Factual control

The orbit contains the points reachable from `x` under the action, and the stabilizer contains the group elements that leave `x` fixed. The target relates their finite cardinalities to the cardinality of `G`.

### Audit-only strategic reference

View a group element only through its effect on `x`. Elements become indistinguishable exactly when they differ by motion that fixes `x`, so the stabilizer measures redundancy and the orbit is represented by the corresponding quotient. Counting effective positions and redundant motions yields the factorization.

### Leakage boundary

Supplying the exact orbit/quotient equivalence and final cardinality rewrite is proof-like. The intended calibration hint stops at the redundancy/quotient mechanism.

### Exact genericity variant

Let a finite group `H` act on a set and choose a point `y`. Show that the size of the set of positions reachable from `y`, multiplied by the size of the subgroup fixing `y`, is the size of `H`.

This target is not part of the six primary evidence cells. It is a positive-channel calibrator: if even strong compact guidance cannot affect this easier target when baseline is below ceiling, the natural-language guidance interface may be ineffective. Conversely, success here alone is not evidence for substantive intuition fertility.

## Cross-theorem strategy mapping

Freeze these pairings before any qwen-lean outcomes:

- **A analytic identity ↔ E local-to-global confluence.** Both convert a local property into a global one, but through different mathematical structures.
- **B generalized eigenspaces ↔ C disjoint-sum linear independence.** Both are linear-algebraic separation problems, with distinct mechanisms.
- **D finite graph consistency ↔ F countable coordinate dependence.** Both assemble global structure from restricted information, using different closure/compactness principles.

For each direction, the condition receives the exact frozen strategic intuition generated for its partner. A cross hint may genuinely help; such a result is transfer evidence, not grounds for relabeling the control after results are seen.

## Why the other shortlist candidates were not selected

This is not a judgment that they are mathematically worse. The reasons are experimental.

- `Module.Relations.Solution.injective_fromQuotient_iff_ker_π_eq_span`: useful reserve, but a faithful standalone presentation requires substantial specialized definitions and the theorem statement itself foregrounds the quotient/kernel mechanism.
- `existsUnique_zpow_near_of_one_lt`: interesting order/exponent structure, but it introduces more literal arithmetic/order surface syntax than needed for the first computation-free conceptual panel.
- `Real.cauSeq_converges`: strong reserve, but extremely canonical base-model knowledge may reduce headroom; the panel already has a difficult analysis item.
- `Polynomial.exists_prod_multiset_X_sub_C_mul`: the target formula itself advertises much of the factorization strategy.
- `BoundedContinuousFunction.exists_norm_eq_restrict_eq`: good reserve, but the extension setting requires more inherited topological context than the selected items.
- `ConvexOn.lipschitzOnWith_of_abs_le`: proof-bearing, but the quantitative bound introduces unnecessary formula-specific surface structure for the first diagnostic.
- `Orthonormal.sum_inner_products_le`: mathematically clean but highly canonical and likely to cue the standard proof immediately; reserve for a later transfer panel.
- `LinearMap.image_closure_of_convex`: potentially valuable but has a large locally-convex/dual-space context burden that risks testing missing definitions rather than intuition.
- `MulAction.Subgroup.normalCore_eq_ker`: shares the same component/domain as the orbit-stabilizer calibrator and would overweight coset-action mechanisms.
- `BinaryTree.treesOfNumNodesEq_card_eq_catalan`: the named counting sequence/recursive tree definition can reveal much of the intended decomposition strategy.
- `Finset.Colex.UV.erdos_ko_rado`: excellent research-style reserve, but its exact extremal bound and theorem familiarity make the first anonymous presentation more fragile.
- `MeasureTheory.Measure.exists_sum_smul_dirac`: good reserve, but selecting it with the countable-coordinate theorem would overweight measure theory.
- `continuousSMul_iff_stabilizer_isOpen`: useful moderate reserve but overlaps the action/stabilizer calibration domain.
- `Quiver.Path.exists_notMem_mem_hom_path_path_of_notMem_mem`: conceptually clear but close to a first-boundary-crossing lemma; likely too direct for primary evidence.

## Final pre-implementation audit questions

A fresh reviewer must try to falsify the panel by asking:

- Do the Mathia-visible statements leak the audit-only mechanisms?
- Are the natural-language statements and exact variants faithful to the private formal propositions?
- Are A/E, B/C, or D/F so similar that cross guidance is effectively relevant guidance rather than a control?
- Does the generic strategy control advantage some targets disproportionately?
- Are all primary targets understandable from the supplied statement without source-file context?
- Can each target admit useful strategic guidance substantially shorter than a proof?
- Does any statement uniquely identify a famous theorem? If so, record pretraining familiarity rather than changing the panel after outcomes.
- Can the experiment return a negative result without treating formal-worker failure as mathematical refutation?
