---
id: CLUE-arithmetic-fidelity-beurling-arithmetic-equivalence-boundary
type: research-clue
status: proposed
origin: master-researcher
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/README.md
  - research/arithmetic_fidelity/findings/AF-001-fiberwise-recoverability-and-unconstrained-lifts.md
  - research/arithmetic_fidelity/findings/AF-013-finite-experiment-fidelity-is-vector-likelihood-ratio-sufficiency.md
  - research/master/STATE.md
---

# What remains of Arithmetic Fidelity beyond Beurling generalized primes and arithmetic equivalence?

## Observation

Arithmetic Fidelity increasingly treats rational-prime specificity as a survival problem under a declared compression or destination category: after quotienting, spectralization, positivity, averaging, or another map, the rational-prime object should remain distinguishable from matched non-prime controls at that same information layer. `AF-013` sharpens this by requiring fidelity to an entire control family rather than to one selected target statistic.

That motivation has a strong classical prior-art boundary. Beurling generalized primes were introduced precisely to separate consequences that follow from an abstract multiplicative prime system from consequences that require additional structure of the ordinary integers. Later generalized-prime constructions show that substantial prime/integer-counting behaviour can coexist with generalized zeta functions having zero distributions radically unlike the Riemann zeta function. In particular, Diamond--Montgomery--Vorhauer construct a Beurling system with `N_B(x)=kappa x+O(x^theta)`, `1/2<theta<1`, while the corresponding zeta function has infinitely many zeros on a curve tending to `Re(s)=1`.

Arithmetic equivalence supplies a second closely related boundary. Gassmann-equivalent, non-isomorphic number fields can have identical Dedekind zeta functions; Perlis proved the equivalence between arithmetic equivalence and equality of Dedekind zeta functions. Thus a highly structured canonical analytic invariant can be exactly identical while the upstream arithmetic objects remain non-isomorphic.

Therefore neither "compare ordinary primes with generalized-prime controls" nor "ask what upstream arithmetic structure a zeta/spectral invariant forgets" can by itself be treated as a new conceptual contribution of Arithmetic Fidelity.

## Research question

Can Arithmetic Fidelity isolate a theorem-level residual that is genuinely stronger than these classical precedents: a category-independent or explicitly category-indexed criterion that identifies the **minimal intrinsically admissible relational structure** which distinguishes the rational-prime system from the strongest matched generalized-prime/arithmetic-equivalence controls after a specified compression?

Concretely, for a destination map `T` and a control family `C`, can one derive from symmetry, locality, naturality, operator structure, or another independent constraint a maximal admissible quotient/lift class such that either:

1. the rational-prime discriminator factors through that admissible retained structure while the matched controls do not; or
2. one proves an exact no-go showing that every admissible retained structure in the declared category remains shared by some Beurling/generalized-prime or arithmetic-equivalent control?

The target is not another example of information loss. It is a reusable theorem that explains what additional structure beyond the classical Beurling/Gassmann boundaries must be present before a proposed RH mechanism can claim rational-prime specificity.

## Why it may matter

If this residual cannot be made precise, Arithmetic Fidelity risks becoming a reorganization of mature sufficiency, inverse-problem, generalized-prime, and arithmetic-equivalence theory. If it can, the line would gain a sharp novelty boundary and a practical stopping rule for the other Mathia branches: before investing in downstream positivity, spectra, determinants, or asymptotics, prove that the proposed carrier lies beyond the strongest classical matched-control equivalence at the exact destination category.

This could also distinguish two logically different claims that are often conflated: preserving arithmetic information versus preserving **rational-prime-specific** information. Beurling and arithmetic-equivalence examples show that substantial arithmetic structure can survive while the object is still not uniquely tied to the ordinary primes or a unique arithmetic source.

## Decisive test

Choose one concrete Mathia compression where a prime-specific claim is currently live and perform a three-way audit:

1. identify the exact rational-prime discriminator before compression;
2. construct the strongest literature-grounded matched controls from Beurling/generalized-prime or arithmetic-equivalence phenomena that inhabit the same destination category;
3. characterize the full post-compression indistinguishability relation and determine whether any intrinsically admissible relational lift separates the rational-prime object from those controls.

Kill this clue if the resulting criterion reduces entirely to an existing theorem from generalized-prime theory, statistical sufficiency, inverse problems, arithmetic equivalence, or another mature framework without leaving a Mathia-specific residual. Strengthen it only if the audit produces a reusable theorem or obstruction that is not already contained in those theories and that changes a concrete research line's admissible search space.

## Evidence boundary

The prior-art boundary should be audited at minimum against:

- A. Beurling, *Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I*, Acta Mathematica 68 (1937), 255--291.
- H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, *Beurling primes with large oscillation*, Mathematische Annalen 334 (2006), 1--36, DOI `10.1007/s00208-005-0638-2`.
- R. Perlis, *On the equation zeta_K(s)=zeta_K'(s)*, Journal of Number Theory 9 (1977), 342--360, DOI `10.1016/0022-314X(77)90070-1`, together with the Gassmann-equivalence antecedent.

These sources establish strong precedents for matched generalized-prime controls and for non-isomorphic arithmetic objects sharing a zeta invariant. They do **not** establish the proposed cross-category admissible-lift hierarchy, nor do they show that such a hierarchy exists or is novel. The clue is specifically to determine whether any theorem-level residual remains after these classical boundaries are incorporated as first-class prior art.
