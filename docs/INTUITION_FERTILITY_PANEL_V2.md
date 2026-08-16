# Intuition-fertility theorem panel v2

## Status

**Current revised exact theorem-panel target for Mathia issue #30.** This document responds to the independent `REVISE` verdict on `INTUITION_FERTILITY_PANEL_V1.md` at branch head `818793ba4ec2d7d0a7db718c0c8deacf366ea83b`.

`PANEL_V1` remains immutable review provenance. Canonical theorem identity is now separated from artifact metadata in `INTUITION_FERTILITY_TARGET_IDENTITY_AUDIT_V1.md`.

The panel tests whether theorem-specific strategic guidance changes verified whole-proof generation. It does **not** behaviorally validate the proposed concept families or conceptual-move labels.

## Common intuition request

Every Mathia-visible theorem presentation receives exactly this semantic request:

> Propose one compact mathematical strategy for why the result should hold and how a proof might be organized. Identify the main mechanism or representation and a small number of useful intermediate mathematical goals if needed. Mention an obstruction or essential assumption only if it materially guides the route. Do not write the proof.

The generator must not receive the canonical/private declaration name, source file, retained proof, neighboring source lemmas, audit-only mechanism note, qwen-lean output, or private formal metadata.

Disallowed primary outputs include Lean code, tactic names, library identifiers, source names, line-by-line derivations, or an informal proof so complete that the downstream prover is left mainly with transcription.

## Leakage classification — frozen operational contract

Classification exists only to prevent proof transmission from masquerading as intuition. It is **not** a quality, elegance, correctness, or truth score.

A classifier sees only:

- the same Mathia-visible theorem statement seen by the intuition generator;
- the candidate guidance text.

It must not see:

- generator/model identity;
- canonical declaration name or source path;
- retained/source proof;
- audit-only mechanism note;
- qwen-lean generations, pass/fail outcomes, logits, or ranks;
- other candidate guidance for comparative ranking.

Labels:

- `strategic` — gives a mechanism, representation, obstruction, or a small number of subgoals while leaving substantial local mathematical and formal proof work unresolved;
- `borderline` — gives an ordered local derivation or implementation skeleton that resolves a major proof subproblem enough to make causal interpretation unsafe;
- `proof_like` — supplies a near-complete proof route, detailed induction/case structure, exact coefficient/constructor derivation, exact lemma chain, Lean code, tactics, or equivalent transcription-ready content.

Only `strategic` enters primary fertility scoring. Any disagreement or uncertainty is conservatively treated as `borderline` and excluded from the primary score. AI assistance is permitted for this leakage-only classification, but it must use this frozen rubric and may not score mathematical correctness or similarity to the audit note. Labels freeze before corresponding formal-worker outcomes exist. Never sanitize or shorten a leaky sample after seeing qwen-lean outcomes.

## Guidance length and comment-channel control

All **generated strategy-bearing guidance** used in a formal-worker condition (`adjacent_cross`, `distant_mismatch`, `qwen_base_intuition`, `codex_reference_intuition`, future `mathia_intuition`) is produced under the same intuition request and a common hard maximum of **96 qwen-lean-tokenizer tokens before Lean-comment delimiters**.

- Over-budget samples are rejected before any qwen-lean outcome exists.
- Do not truncate or pad semantic text after generation.
- Record the exact serialized guidance-token count for every cell.
- The main content-specific causal comparison requires relevant guidance to beat a **same-generator distant mismatched strategy** under the same comment wrapper.
- For a relevant-vs-distant cell to support a content-specific claim, their serialized guidance lengths must differ by no more than **20% of the longer text**. If they do, report the cell but do not use it for the content-specific causal claim.

`factual_control` and `generic_strategy_control` remain additional triangulation controls; exact token equality with them is not required because the distant mismatch now supplies the strategy-shaped/context-matched negative. All guidance conditions use the same bounded natural-language Lean-comment wrapper. `no_guidance` remains the only no-comment condition.

## Generic strategy control

Use the same theorem-independent content for every target:

> Search for a structural viewpoint that makes the conclusion natural. Identify one useful representation, decomposition, invariant, or intermediate object and a small number of subgoals suggested by it. Prefer a viewpoint that removes irrelevant detail. Do not write the proof.

This measures generic `think structurally` priming. It may genuinely help some targets; relevant guidance must therefore beat it where a theorem-specific claim is made.

---

## Primary A — analytic local-to-global identity

**Canonical private formal target:** `AnalyticOnNhd.eqOn_zero_of_preconnected_of_eventuallyEq_zero_aux`

**Record:** `b02d73078afb5b4319abc67810e0ae8efa2ce6960dea2d4a8445f6f422d9437b`

**Private source:** `Mathlib/Analysis/Analytic/Uniqueness.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `𝕜` be a nontrivially normed field, and let `E` and `F` be normed spaces over the same field `𝕜`, with `F` complete. Let `U` be a preconnected subset of `E` and let `f : E → F` be analytic in a neighborhood of every point of `U`. Assume there is a point of `U` near which `f` agrees with the constant zero function. Show that `f` agrees with the constant zero function throughout `U`.

### Factual control

`E` and `F` are normed over the same nontrivially normed field, `F` is complete, `U` is preconnected, `f` is analytic near every point of `U`, and near one point of `U` it agrees with the constant zero function. The target is equality with that function on all of `U`.

### Audit-only mechanism boundary

Think of local vanishing as a property that should propagate through a preconnected region because analytic uniqueness prevents propagation from stopping at an interior boundary.

### Intended move annotations

`stress-test`, `abstract/compress`, local-to-global transfer. These are descriptive annotations only, not validated latent dimensions.

### Leakage boundary

Constructing the exact open/closed set used by the source, giving the analytic power-series continuation argument, or naming the exact source lemma chain is `proof_like`. The propagation viewpoint itself can remain `strategic`.

### Exact genericity variant

Let `K` be a nontrivially normed field and let `X` and `Y` be normed spaces over `K`, with `Y` complete. Let `V` be preconnected and let `g : X → Y` be analytic near every point of `V`. Suppose some point of `V` has a neighborhood on which `g` is the constant zero function. Show that `g` is the constant zero function on all of `V`.

---

## Primary B — separation of generalized eigenspaces

**Canonical private formal target:** `Module.End.disjoint_genEigenspace`

**Record:** `9db61d80db52314e83addee2d556253ee17ad710d1a597725a0a6390d2009073`

**Private source:** `Mathlib/LinearAlgebra/Eigenspace/Basic.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `T` be an endomorphism of a torsion-free module over a domain, and let `λ` and `μ` be distinct scalars. For any generalized-eigenspace depths `k` and `l` in the extended natural numbers `ℕ∞` — including the unbounded depth — show that the generalized eigenspace of `T` for `λ` at depth `k` and the generalized eigenspace for `μ` at depth `l` have trivial intersection.

### Factual control

The same endomorphism `T` determines generalized eigenspaces for two distinct scalars `λ` and `μ`, at arbitrary depths in `ℕ∞`, possibly unbounded. The module is torsion-free over a domain. The target is that the two submodules have only the trivial intersection.

### Audit-only mechanism boundary

A common vector would exhibit two incompatible generalized shifted-operator behaviors; scalar distinctness together with the domain/torsion-free assumptions is the obstruction.

### Intended move annotations

`stress-test`, `decompose`, `select`. Descriptive only.

### Leakage boundary

Giving the exact polynomial identity, exponent manipulation, or source lemma sequence that derives the contradiction is `proof_like`. Identifying incompatible shifted-operator behavior and the role of scalar distinctness can remain `strategic`.

### Exact genericity variant

Let `S` be an endomorphism of a torsion-free module over a domain and let `α` and `β` be distinct scalars. Fix any depths `p` and `q` in `ℕ∞`, allowing the unbounded case. Consider the corresponding generalized eigenspaces for `α` and `β`. Show that they have trivial intersection.

---

## Primary C — independence across a disjoint index sum

**Canonical private formal target:** `linearIndependent_sum`

**Record:** `5751f369a1e80a5ebcf31574d28dd7a3b9b20c65d841fce0294f780562bd73e6`

**Private source:** `Mathlib/LinearAlgebra/LinearIndependent/Basic.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `v` be a family of vectors indexed by the disjoint sum of two index types. Show that the whole family is linearly independent if and only if the restriction to each side is linearly independent and the submodules spanned by the ranges of the two restrictions are disjoint.

### Factual control

The family has one restriction to each side of a disjoint index sum. The target is an equivalence between independence of the combined family and independence of both restrictions together with disjointness of their spans.

### Audit-only mechanism boundary

Split a global relation according to the two tags; local independence handles each side, while disjoint spans should rule out cancellation between the two contributions.

### Intended move annotations

`decompose`, `synthesize`, `abstract/compress`. Descriptive only.

### Leakage boundary

Writing the finite-support coefficient derivation in both directions is `proof_like`. The decomposition/cross-cancellation viewpoint alone can remain `strategic`.

### Exact genericity variant

Let `(a_i)` and `(b_j)` be two tagged families of vectors whose index sets are disjoint. Form the combined tagged family. Show that it is linearly independent exactly when each original family is linearly independent and the spans of the two families have trivial intersection.

**Interpretation note:** this statement already exposes the span-disjointness condition. C can measure proof-organization fertility, but it is weak evidence for *discovering* a hidden mechanism.

---

## Primary D — finite graph consistency to a global homomorphism

**Canonical private formal target:** `SimpleGraph.nonempty_hom_of_forall_finite_subgraph_hom`

**Previously reported artifact/shortlist name:** `SimpleGraph.Finsubgraph.nonempty_hom_of_forall_finite_subgraph_hom` (invalid as a canonical source name; retained only as provenance).

**Record:** `9a0191efa6271a14b1aa05a9b3d422d207d1193899daf8ef955cbe9a2e0440ae`

**Private source:** `Mathlib/Combinatorics/SimpleGraph/Finsubgraph.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `G` and `F` be graphs, with the vertex type of `F` finite. Assume that every subgraph of `G` having finitely many vertices admits a graph homomorphism into `F`. Show that there exists a graph homomorphism from all of `G` into `F`.

### Factual control

`F` has finitely many vertices. Every finite-vertex subgraph of `G` has at least one graph homomorphism into `F`. The target is existence of a graph homomorphism from `G` itself into `F`.

### Audit-only mechanism boundary

Reframe the finite homomorphisms as finite compatible constraints and look for a compactness/coherence principle that uses the finite target to obtain one global assignment.

### Intended move annotations

`abstract/compress`, `synthesize`, `reframe/bridge`, local-to-global transfer. Descriptive only.

### Leakage boundary

Naming the exact inverse-system objects, filters/ultrafilters, source compactness theorem, or the source assembly construction is `proof_like`. Finite satisfiability plus compactness/coherence can remain `strategic`.

### Exact genericity variant

Let `H` be a source graph and `K` a graph with finite vertex type. Suppose every finite-vertex subgraph of `H` admits a homomorphism into `K`. Show that the entire graph `H` admits a homomorphism into `K`.

---

## Primary E — local diamonds to global confluence

**Canonical private formal target:** `Relation.church_rosser`

**Previously reported artifact/shortlist name:** `Relation.ReflGen.SymmGen.ReflTransGen.TransGen.EqvGen.church_rosser` (invalid as a canonical source name; retained only as provenance).

**Record:** `92d6b286e0d3754888b472b5b8b3f488715970a8f1dca537c3f5bb10ed9934cc`

**Private source:** `Mathlib/Logic/Relation.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let `r` be a reduction relation. Assume that whenever one object makes two direct `r`-steps to two successors, the branches can be joined so that one successor needs at most one further `r`-step and the other needs only finitely many `r`-steps. Show that whenever two objects are each reachable from a common start by finitely many `r`-steps, the two endpoints have a common descendant reachable from each by finitely many `r`-steps. Zero-step reachability is allowed.

### Factual control

The premise gives a joinability condition for every direct fork of `r`. The target gives a joinability condition for endpoints of arbitrary finite reduction sequences from the same source, with empty paths allowed.

### Audit-only mechanism boundary

Try to lift the one-step joining property to finite paths by an induction compatible with reflexive-transitive closure.

### Intended move annotations

`transfer`, `synthesize`, `generalize/weaken`, local-to-global reasoning. Descriptive only.

### Leakage boundary

A complete induction with its ordered constructor/case derivation is `proof_like`. Naming induction/closure as the mechanism can remain `strategic`.

### Exact genericity variant

Let `→` be a relation. Suppose every pair of one-step paths from the same source can be joined, with one branch requiring no more than one additional step and the other a finite path. If `y` and `z` are reached from `x` by finite paths, allowing empty paths, show that `y` and `z` can each reach a common object by finite paths.

---

## Primary F — measurable events depend on countably many coordinates

**Canonical private formal target:** `MeasureTheory.MeasurableSet.eq_preimage_restrict_countable`

**Record:** `7ee0d231a646406fb0e6adea92cbca454ed339175fcd0d2c83bda918064cc795`

**Private source:** `Mathlib/MeasureTheory/Constructions/Cylinders.lean`

**Phase-2 status:** heldout, proof-bearing.

### Mathia-visible statement

Let a family of measurable spaces be indexed by an arbitrary type, and let `s` be a measurable subset of their product. Show that there is a countable set of coordinates `I` and a subset `t` of the product restricted to `I` such that `s` is exactly the preimage of `t` under the coordinate-restriction map. Thus membership in `s` depends only on the coordinates in `I`.

### Factual control

`s` is measurable in a product measurable space. The target is existence of a countable coordinate set and a restricted-product subset whose inverse image under coordinate restriction is exactly `s`.

### Audit-only mechanism boundary

Turn “depends on countably many coordinates” into a property that can be checked for the generators of the product measurable structure and is preserved by the relevant set-building operations.

### Intended move annotations

`abstract/compress`, `synthesize`, `generalize/weaken`. Descriptive only.

### Leakage boundary

Listing the exact measurable-space induction constructors and the corresponding set identities is `proof_like`. The closure-property reframing can remain `strategic`.

### Exact genericity variant

Let `(Y_j)` be measurable spaces indexed by a type `J`, and let `A` be a measurable subset of their product. Show that there is a countable subset `K` of `J` and a subset `B` of the product over `K` such that `A` is the inverse image of `B` under restriction to `K`. Equivalently, changing coordinates outside `K` cannot change membership in `A`.

---

## Calibration G — orbit/stabilizer cardinality

**Canonical private formal target:** `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`

**Record:** `60b1a7986f6f4b88449378e1d397c3e717b2e9d2e29d21efe11d73ff443a7c41`

**Private source:** `Mathlib/GroupTheory/GroupAction/Quotient.lean`

**Phase-2 status:** `CLEAN_HELDOUT`, but retained proof is short/wrapper-like.

### Mathia-visible statement

Let a finite group `G` act on a set and let `x` be a point. Show that the cardinality of the orbit of `x` multiplied by the cardinality of the stabilizer of `x` equals the cardinality of `G`.

### Factual control

The orbit contains the points reachable from `x` under the action, and the stabilizer contains the group elements that leave `x` fixed. The target relates their finite cardinalities to the cardinality of `G`.

### Audit-only mechanism boundary

View orbit positions as effective group motions modulo motions that fix `x`; the stabilizer measures the redundancy.

### Leakage boundary

Supplying the exact orbit/quotient equivalence and final cardinality rewrite is `proof_like`. The redundancy/quotient viewpoint can remain `strategic`.

### Exact genericity variant

Let a finite group `H` act on a set and choose a point `y`. Show that the size of the set of positions reachable from `y`, multiplied by the size of the subgroup fixing `y`, is the size of `H`.

G is only a positive-channel/easier-target diagnostic. If baseline is at ceiling it is uninformative; if G responds while all six proof-bearing primaries remain at floor, the panel/channel remains inconclusive rather than validating substantive fertility.

## Adjacent cross-theorem transfer probe

Retain the v1 pairings, but **do not treat them as a clean negative control**:

- A ↔ E — local-to-global propagation;
- B ↔ C — linear-algebraic separation;
- D ↔ F — global structure from restricted information.

For each direction, use the exact frozen strategic intuition generated for the partner target. If it helps, report transfer/generalization evidence. If it matches theorem-specific guidance, that weakens a theorem-specific interpretation rather than being relabeled after outcomes.

## Distant mismatched strategy control

This is the new strategy-shaped negative control required by the independent review. For each target, use the exact frozen **strategic** intuition generated by the same model/configuration for the fixed donor below:

| Receiving target | Distant donor |
|---|---|
| A analytic identity | C disjoint-sum linear independence |
| B generalized eigenspaces | D finite graph consistency |
| C disjoint-sum linear independence | E local confluence |
| D finite graph consistency | B generalized eigenspaces |
| E local confluence | C disjoint-sum linear independence |
| F countable coordinate dependence | B generalized eigenspaces |

The mapping is intentionally mechanism-distant and frozen before formal-worker outcomes. It is not a balance test and does not claim the donor strategy is mathematically false; it claims only that no specific transfer relation is being targeted by design.

If a supposedly distant hint proves unexpectedly useful, preserve the result. It is evidence that the control was not irrelevant for that cell; do not redefine the mapping after outcomes. Content-specific claims for that cell then require caution or become unavailable.

G has no cross or distant condition in the primary contract.

## Required conditions

For each primary target:

- `no_guidance`;
- theorem-specific `factual_control`;
- theorem-independent `generic_strategy_control`;
- `adjacent_cross_theorem_strategy`;
- `distant_mismatched_strategy`;
- `qwen_base_intuition`;
- `codex_reference_intuition`;
- later `mathia_intuition` under the same contract.

## Causal interpretation guardrails

A result supports **theorem-specific useful intuition** only when, on at least some non-ceiling primary targets, strategic theorem-specific guidance beats:

- `no_guidance`;
- `factual_control`;
- `generic_strategy_control`;
- the same-generator `distant_mismatched_strategy` under the length criterion;

without being `borderline`/`proof_like`.

Interpret other patterns explicitly:

- relevant ≈ adjacent cross > distant → evidence compatible with transferable abstraction rather than theorem-specificity;
- relevant ≈ generic > factual/no-guidance → generic structural priming is sufficient;
- relevant ≈ distant → style/context/OOD or broad strategy effects remain live; no content-specific claim;
- only `borderline`/`proof_like` guidance helps → proof leakage channel, not intuition fertility;
- uplift tracks guidance length or only appears in length-imbalanced cells → token/context confound; no content-specific claim;
- all primary targets floor/ceiling → panel/formal-worker instrument failure, not mathematical refutation;
- G alone responds → channel may carry natural-language information on an easy target, but substantive primary fertility remains unestablished.

## Genericity variants

Variants remain alpha-renaming/paraphrase stress tests only. They can reveal dependence on names or incidental notation; robustness under them is not evidence by itself for conceptual understanding or transfer.
