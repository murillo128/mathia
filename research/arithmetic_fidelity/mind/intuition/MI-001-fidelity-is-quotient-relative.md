# MI-001 — Fidelity is quotient-relative, and admissible information loss is irreversible

**Evidence level:** supported by exact deterministic, invariant, smooth, stochastic, statistical-sufficiency, and Riesz-profile factorization models

## Core intuition

A compression should be audited through the indistinguishability relation it imposes on the discriminator that matters. Recoverability is not a vague function of rank or dimension: the discriminator must factor through the retained statistic. Once conflicting states or models have been identified and no new admissible information is introduced, downstream processing cannot separate them again.

## Strongest justified principle

AF-001 gives the deterministic core: for `T:X->Y`, exact recovery of `d` through `T` is equivalent to `d` being constant on every `T`-fiber. AF-003 upgrades this to a constrained observable library: the joint map of all admissible observables is the maximal admissible quotient, so the right question is whether `d` factors through that quotient rather than whether one can invent an arbitrary faithful mark.

AF-012 and AF-013 give a stochastic version with an exact sufficient statistic. For a binary experiment the retained likelihood ratio is `E[L|Y]`; equality in any one strictly convex `f`-divergence is equivalent to statistical sufficiency and therefore to preservation of every convex `f`-divergence. For a finite family of models the full reference-relative likelihood-ratio vector plays the same role: one strictly convex multidistribution divergence has zero loss exactly when a single reverse channel recovers the whole experiment. Divergence losses are additive under further garbling, so a lost experiment cannot be reconstructed downstream without side information.

[AF-349](../../findings/AF-349-full-riesz-profile-is-exactly-recoverable-before-asymptotic-quotient.md) gives a sharp arithmetic instance of the same composition rule. For every fixed finite Riesz order `r`, the complete cutoff profile is injective because, with `F_r(X)=X^r R_r[a](X)`,

`D^(r+1) F_r = r! sum_n a_n delta_n`.

More strongly, the same jump structure gives an exact finite-horizon stability identity: the total variation of `D^r F_r[a-b]` is `r!` times the local coefficient `ell^1` distance. Thus the full Riesz representation is not merely injective; it is perfectly conditioned in this source-matched derivative-variation metric. The Mellin transform carries the same exact-fidelity conclusion through a nonzero beta factor.

Yet the AF-348 perfect-power control and dense unit mass stay only `O(1)` apart in raw profile amplitude once `r>=k-1`, while their local coefficient distance is `Theta(N)`. After the later quotient that discards bounded residual profiles they become identical. Hence fidelity and conditioning belong to the pair **(representation, destination topology)**: exact stability in a strong metric does not imply a useful inverse modulus in the weaker metric actually retained downstream.

The same quotient principle appears in other categories without becoming one category-free theorem. AF-007 gives a first-order smooth obstruction through the vertical rank of `dD|ker dT`; AF-009 identifies conditional variance as the exact `L2` prediction defect; AF-011 gives the zero-error analogue through support confusability.

## What remains possible

A lossy quotient can still be sufficient for one arithmetic predicate even when it does not reconstruct the full input. Conversely, a large or injective representation is not automatically meaningful if its extra coordinates are target-leaking, inaccessible to the terminal theorem, or controlled only in a topology stronger than the endpoint supplies. The live problem is to characterize the smallest **admissible** statistic on which the intended discriminator becomes well defined with the required stability in the actual destination metric.

AF-016 adds a necessary caution: symmetry breaking in one base realization is not generally a completeness theorem for intrinsic observability. In first-order settings, for example, automorphism invariance can be much weaker than definability unless one has an `omega`-categorical or Svenonius-type completeness argument.

## Status / novelty

The fiberwise, maximal-observable, smooth-rank, conditional-variance, support-confusability, statistical-sufficiency, and finite-order Riesz recovery/stability statements are persisted exact findings or standard-category consequences specialized here. Their organization as a reusable Mathia fidelity gate is a supported synthesis.

## Falsification criterion

Exhibit a pipeline in one of the audited categories where two conflicting states/models are indistinguishable under the complete admissible statistic entering the downstream construction, yet later processing recovers the discriminator without receiving new information. Or, for the quantitative version, exhibit a claimed terminal recovery theorem whose norm does not control the source-separating topology but nevertheless has a uniform inverse modulus on the stated source class.

## Lean-formalizable core

- Fiberwise factorization criterion and monotonicity under post-composition.
- Maximal admissible observable quotient.
- Likelihood-ratio conditional-expectation identity and strict-Jensen equality criterion.
- Support-confusability zero-error criterion.