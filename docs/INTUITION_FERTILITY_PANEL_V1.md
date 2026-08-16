# Intuition-fertility theorem panel v1

## Status

This is the **current exact theorem-panel design target for issue #30**, pending fresh-context independent adversarial review. It supersedes `INTUITION_FERTILITY_PANEL_V0.md`, whose original six candidates were rejected for the Phase-5 line after five were found in qwen-lean optimizer training.

All six primary v1 targets below were independently checked in the actual qwen-lean Phase-2 artifact as `heldout`, reconstruct correctly in pinned mathlib, and have Lean-accepted retained proofs. No qwen-lean/Qwen inference was used to choose them. `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` remains a separate clean heldout **calibration** target because its retained proof is short/wrapper-like.

The panel is designed to test whether theorem-specific strategic guidance changes verified whole-proof generation. The private proof mechanisms and audit references in this file must not be exposed to the intuition generator.

## Common intuition request

Each Mathia-visible theorem presentation receives the same request:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and a small number of useful intermediate mathematical goals if needed. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof.

The generator must not receive the private declaration name, source file, retained proof, neighboring source lemmas, audit-only strategy reference, or qwen-lean output.

Disallowed primary outputs include Lean code, tactic names, library identifiers, a line-by-line derivation, or an informal proof so complete that the downstream prover is left mainly with transcription.

## Generic strategy control

Use the same theorem-independent strategy-shaped control for every target:

> Look for a structural representation that makes the conclusion direct. Check whether a decomposition, invariant, reversible or quotient-like map, or equivalent formulation removes irrelevant detail. Prefer one mechanism and a small number of subgoals; do not write the proof.

This control exists to detect a generic `think structurally` / extra-deliberation effect. Exact comment escaping and token-budget normalization belong to #31/#32, but the semantic content above is frozen by #30.

## Primary A — analytic local-to-global identity

**Private formal target:** `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux`

**Record:** `b02d73078afb5b4319abc67810e0ae8efa2ce6960dea2d4a8445f6f422d9437b`

**Private source:** `Mathlib/Analysis/Analytic/Uniqueness.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `U` be a preconnected region and let `f` be a function that is analytic in a neighborhood of every point of `U`. Assume `f` agrees locally with the zero function near some point of `U`. Show that `f` agrees with the zero function throughout `U`.

The concrete formal setting includes the completeness assumptions required by the retained target, but the theorem name and source implementation are hidden.

### Factual control

`f` is analytic near every point of the same preconnected region `U`, and near one point of `U` it agrees with the zero function. The target asks for equality with the zero function on all of `U`.

### Audit-only strategic reference

Treat local vanishing as a property that can propagate through the connected region. Use analytic uniqueness to show that the region where the local zero behavior has propagated cannot stop at an interior boundary; organize the argument so preconnectedness turns the local agreement into global agreement.

### Intended move coverage

`stress-test`, `abstract/compress`, local-to-global transfer.

### Leakage boundary

A response that states the exact source lemma chain, constructs the exact open/closed sets used by the retained proof, or gives the full analytic continuation derivation is proof-like. The strategic content is the propagation mechanism and why connectedness prevents a boundary.

### Genericity variant

Rename the function, region, and distinguished point; phrase the premise as local agreement with the additive identity rather than using the canonical theorem vocabulary. Mathematical content must remain unchanged.

---

## Primary B — separation of generalized eigenspaces

**Private formal target:** `Module.End.disjoint_genEigenspace`

**Record:** `9db61d80db52314e83addee2d556253ee17ad710d1a597725a0a6390d2009073`

**Private source:** `Mathlib/LinearAlgebra/Eigenspace/Basic.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `T` be an endomorphism of a torsion-free module over a domain. Let `λ` and `μ` be distinct scalars. For arbitrary allowed generalized-eigenspace depths, show that the generalized eigenspaces of `T` associated with `λ` and `μ` are disjoint.

### Factual control

The same endomorphism `T` determines generalized eigenspaces for two distinct scalars `λ` and `μ`. The target is that the two specified generalized eigenspaces have only the trivial intersection.

### Audit-only strategic reference

Suppose a vector lies in both generalized eigenspaces and restrict attention to the common substructure it generates. On that common part, suitable powers of the two shifted operators behave nilpotently. Their difference is controlled by the nonzero scalar `μ - λ`; distinctness plus the domain/torsion-free assumptions should make the two nilpotence claims incompatible except for the trivial vector.

### Intended move coverage

`stress-test`, `decompose`, `select`.

### Leakage boundary

Naming the exact polynomial identity, exponent manipulation, or library lemmas that discharge the nilpotence contradiction is proof-like. A strategic intuition may identify incompatible shifted-operator behavior and the role of scalar distinctness.

### Genericity variant

Rename the endomorphism and the two scalars and swap their order. Replace `generalized eigenspace` by a short definition in terms of eventual annihilation by powers of the shifted endomorphism, without exposing the target name.

---

## Primary C — independence across a disjoint index sum

**Private formal target:** `linearIndependent_sum`

**Record:** `5751f369a1e80a5ebcf31574d28dd7a3b9b20c65d841fce0294f780562bd73e6`

**Private source:** `Mathlib/LinearAlgebra/LinearIndependent/Basic.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `v` be a family of vectors indexed by the disjoint sum of two index types. Characterize when the whole family is linearly independent using only the two restricted families and the relationship between the submodules spanned by their ranges.

### Factual control

The family has one restriction to each side of a disjoint index sum. The target is an equivalence between independence of the combined family and conditions involving independence of both restrictions together with disjointness of their spans.

### Audit-only strategic reference

A finite linear relation on the combined family splits canonically into a contribution from each side. If each side is independently rigid, the only remaining way the two contributions can cancel is through a common vector in the two spans. Disjointness of those spans removes that final cancellation channel; conversely, independence of the whole family forces both local independence and separation of the spans.

### Intended move coverage

`decompose`, `synthesize`, `abstract/compress`.

### Leakage boundary

Writing the complete finite-support coefficient argument in both directions is proof-like. The strategic object is the decomposition of a global relation into two independent pieces plus the identification of span intersection as the only cross-cancellation mechanism.

### Genericity variant

Swap the two index types and rename the injections/restrictions. Alternatively present the index set as two tagged disjoint families rather than using sum-type notation.

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

View a partial graph homomorphism as a finite constraint assignment. Every finite collection of constraints is satisfiable by assumption. Because the target choices live in a finite space, search for a compactness/coherence principle that selects assignments compatible across all finite restrictions and then assemble their common limit into one global homomorphism.

### Intended move coverage

`abstract/compress`, `synthesize`, `reframe/bridge`, local-to-global transfer.

### Leakage boundary

Specifying the exact inverse-system objects, filters, ultrafilters, or library compactness theorem used by mathlib is implementation-level. The strategy may identify finite satisfiability plus compactness/coherent-choice as the mechanism.

### Genericity variant

Phrase the hypothesis as “every finite restriction of the source graph is colorable/mappable into the same finite target graph” while preserving graph-homomorphism semantics rather than replacing the theorem by a different coloring statement.

---

## Primary E — local diamonds to global confluence

**Private formal target:** `Relation.ReflGen.SymmGen.ReflTransGen.TransGen.EqvGen.church_rosser`

**Record:** `92d6b286e0d3754888b472b5b8b3f488715970a8f1dca537c3f5bb10ed9934cc`

**Private source:** `Mathlib/Logic/Relation.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `r` be a reduction relation. Assume that whenever one object makes two direct `r`-steps to two successors, the two branches can be joined so that one successor needs at most one further `r`-step and the other needs only finitely many `r`-steps. Show that whenever two objects are each reachable from a common start by finitely many `r`-steps, those two endpoints have a common descendant reachable by finitely many `r`-steps.

Zero-step reachability is allowed in the reflexive-transitive closures used above.

### Factual control

The premise gives a joinability condition for every direct fork of the relation `r`. The target gives a joinability condition for endpoints of arbitrary finite reduction sequences starting at the same object.

### Audit-only strategic reference

Promote the direct-fork property along longer reduction paths. Isolate the first step of one path, use the local joining hypothesis against the competing path, and then apply an induction/closure argument to the remaining reductions. The conceptual move is to show that the local diamond property is stable under composition of reduction steps.

### Intended move coverage

`transfer`, `synthesize`, `generalize/weaken`, local-to-global reasoning.

### Leakage boundary

A complete induction with every constructor of the reflexive-transitive closure is proof-like. Strategic guidance may identify the induction direction and closure-under-composition mechanism without enumerating the formal cases.

### Genericity variant

Rename the relation and endpoints, reverse the names of the two branches, and phrase reachability as finite reduction paths rather than closure constructors.

---

## Primary F — measurable events depend on countably many coordinates

**Private formal target:** `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable`

**Record:** `7ee0d231a646406fb0e6adea92cbca454ed339175fcd0d2c83bda918064cc795`

**Private source:** `Mathlib/MeasureTheory/Constructions/Cylinders.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let a family of measurable spaces be indexed by an arbitrary type, and let `s` be a measurable subset of their product. Show that there is a countable set of coordinates `I` and a set `t` in the product restricted to `I` such that membership in `s` depends only on those coordinates; equivalently, `s` is the preimage of `t` under the coordinate-restriction map.

### Factual control

`s` is measurable in a product measurable space. The target is existence of a countable coordinate set and a restricted-space set whose inverse image under coordinate restriction is exactly `s`.

### Audit-only strategic reference

Consider the class of product subsets whose membership is determined by countably many coordinates. Show that this class is itself a sigma-algebra-like collection: the basic measurable cylinders lie in it, and dependence on countably many coordinates is preserved by the operations used to generate measurable sets. Then every measurable set inherits such a countable support.

### Intended move coverage

`abstract/compress`, `synthesize`, `generalize/weaken`.

### Leakage boundary

Listing the exact generating-measurable-space induction constructors and the corresponding set identities is proof-like. The strategic intuition is to turn “depends on countably many coordinates” into a property closed under the measurable-set generation operations.

### Genericity variant

Rename the index and coordinate spaces; phrase the conclusion as “there exists a countable support determining membership” before giving the equivalent restriction-map formulation.

---

## Calibration G — orbit/stabilizer cardinality

**Private formal target:** `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`

**Record:** `60b1a7986f6f4b88449378e1d397c3e717b2e9d2e29d21efe11d73ff443a7c41`

**Private source:** `Mathlib/GroupTheory/GroupAction/Quotient.lean`

**Phase-2 status:** `CLEAN_HELDOUT`, but retained proof is short/wrapper-like.

This target is not part of the six primary evidence cells. It is a positive-channel calibrator: if even a strong compact strategy cannot affect this easy formal target when baseline is below ceiling, the natural-language guidance interface may be ineffective. Conversely, success here alone is not evidence for substantive intuition fertility.

## Cross-theorem strategy mapping

Freeze these pairings before any qwen-lean outcomes:

- **A analytic identity ↔ E local-to-global confluence.** Both convert a local property into a global one, but through different mathematical structures.
- **B generalized eigenspaces ↔ C disjoint-sum linear independence.** Both are linear-algebraic separation problems, with distinct mechanisms.
- **D finite graph consistency ↔ F countable coordinate dependence.** Both assemble global structure from restricted information, using different closure/compactness principles.

For each direction, the condition receives the exact frozen strategic intuition generated for its partner. A cross hint may genuinely help; such a result is transfer evidence, not grounds for relabeling the control after results are seen.

## Why the other shortlist candidates were not selected

This is not a judgment that they are mathematically worse. The reasons are experimental.

- `Module.Relations.Solution.injective_fromQuotient_iff_ker_π_eq_span`: useful reserve, but a faithful standalone presentation requires substantial specialized definitions and the theorem statement itself already foregrounds the quotient/kernel mechanism.
- `existsUnique_zpow_near_of_one_lt`: order/exponent structure is interesting but introduces more literal arithmetic/order syntax into Mathia-visible material than needed for the first panel.
- `Real.cauSeq_converges`: strong reserve, but extremely canonical base-model knowledge may reduce headroom; the panel already has a difficult analysis item.
- `Polynomial.exists_prod_multiset_X_sub_C_mul`: the target formula itself largely advertises the factorization strategy.
- `BoundedContinuousFunction.exists_norm_eq_restrict_eq`: good reserve, but the extension setting requires more inherited topological context than the selected items.
- `ConvexOn.lipschitzOnWith_of_abs_le`: proof-bearing, but the quantitative bound introduces unnecessary numerical/formula-specific surface structure for this computation-free conceptual diagnostic.
- `Orthonormal.sum_inner_products_le`: mathematically clean but highly canonical and likely to cue the standard proof immediately; reserve for a later transfer panel.
- `LinearMap.image_closure_of_convex`: potentially valuable but has a large locally-convex/dual-space context burden that risks testing missing definitions rather than intuition.
- `MulAction.Subgroup.normalCore_eq_ker`: shares the same component/domain as the orbit-stabilizer calibrator and would overweight coset-action mechanisms.
- `BinaryTree.treesOfNumNodesEq_card_eq_catalan`: the named counting sequence/recursive tree definition can reveal much of the intended decomposition strategy.
- `Finset.Colex.UV.erdos_ko_rado`: excellent research-style item, but the exact extremal bound and theorem familiarity make the first anonymous/computation-free presentation more fragile.
- `MeasureTheory.Measure.exists_sum_smul_dirac`: good reserve, but selecting it together with the countable-coordinate theorem would overweight measure theory.
- `continuousSMul_iff_stabilizer_isOpen`: useful moderate reserve but overlaps the action/stabilizer calibration domain.
- `Quiver.Path.exists_notMem_mem_hom_path_path_of_notMem_mem`: conceptually clear but close to a first-boundary-crossing lemma; likely too direct for primary evidence.

## Final pre-implementation audit questions

A fresh reviewer must try to falsify the panel by asking:

- Do the Mathia-visible statements leak the audit-only mechanisms?
- Are A/E, B/C, or D/F so similar that cross guidance is effectively relevant guidance?
- Does one generic strategy control plausibly advantage some targets disproportionately?
- Are the primary targets understandable from the supplied statement without source-file context?
- Can each target admit a useful strategy that is still substantially shorter than a proof?
- Do any natural-language paraphrases alter the exact formal proposition materially?
- Would theorem-name removal actually matter, or does the statement uniquely identify a famous theorem? If so, record this as pretraining familiarity rather than redesigning after results.
- Can the experiment return a negative result without treating formal-worker failure as mathematical refutation?
