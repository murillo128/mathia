# VIS-372 — commuting external Hermitian structure remains joint spectral filtering

## Claim

Let `G=X_0>=0` be the source-free Wang Gram on a finite-dimensional coefficient space, and let

`X_0=G, X_1, ..., X_m`

be a finite family of pairwise commuting Hermitian matrices. Let `F` assign a positive-definite Hermitian metric

`C=F(X_0,...,X_m)`

and assume simultaneous unitary-conjugation equivariance:

`F(U X_0 U^*,...,U X_m U^*) = U F(X_0,...,X_m) U^*`

for every unitary `U`.

Because the `X_j` commute, there is a joint orthogonal spectral decomposition

`X_j = sum_alpha lambda_(j,alpha) P_alpha`,

where `P_alpha` projects onto the common eigenspace associated with the attained joint eigenvalue tuple

`Lambda_alpha=(lambda_(0,alpha),...,lambda_(m,alpha))`.

Then there are positive scalars `c_alpha>0` such that

`C = sum_alpha c_alpha P_alpha`.

Consequently `C` commutes with every `X_j`, in particular

`[C,G]=0`.

Thus an additional Hermitian operator does **not** create a genuinely new orientation for a coordinate-free Wang metric merely by being external to the Gram. If all admitted external Hermitian inputs commute with the Gram and with one another, every simultaneous-unitary-equivariant positive metric rule is still only a joint spectral reweighting. Relative to the baseline Wang map, it remains inside the commuting-metric class of `VIS-370`.

A commuting external operator can refine a degenerate eigenspace of `G` and assign different weights to its joint spectral subspaces, so this result is strictly broader than the Gram-only conclusion of `VIS-371`; nevertheless it cannot mix distinct Gram eigenspaces or create cross-sector interference. A genuinely noncommuting positive-metric route therefore needs **noncommuting external structure**, source-dependent orientation, non-equivariant preferred coordinates, or a mechanism outside positive finite-dimensional Hilbert geometry.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL JOINT SPECTRAL REPRESENTATION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the normalized Chebyshev-theta remainder, the PNT remainder, zeta zeros, or RH.

## 1. Alternate representation: replace separate matrices by one joint spectral observable

The representation audit starts from the tuple `(X_0,...,X_m)` rather than from `G` alone. Pairwise commuting Hermitian matrices are simultaneously unitarily diagonalizable, so the tuple is equivalent to a finite joint spectral measure: the coefficient space decomposes orthogonally into common eigenspaces `E_alpha=ran(P_alpha)`, and each `X_j` acts on `E_alpha` by the scalar `lambda_(j,alpha)`.

This representation preserves exactly the information in the commuting family. It exposes what the extra operators actually add: they may split a repeated `G` eigenspace into smaller joint eigenspaces, but they do not supply an orientation coupling two different Gram eigenvalues.

The bridge back to the original Wang representation is exact. The first coordinate of each joint eigenvalue tuple is the Gram eigenvalue, so every joint projector lies inside one Gram eigenspace. Hence any operator scalar on the joint projectors automatically commutes with `G`.

## 2. Stabilizer equivariance forces scalar action on each joint eigenspace

Fix the commuting tuple. Its simultaneous stabilizer contains every unitary that acts arbitrarily inside one common eigenspace `E_alpha` and as the identity on the orthogonal complement. Equivariance therefore gives

`C = U C U^*`

for all such unitaries.

As in `VIS-371`, phase rotations on distinct joint eigenspaces kill off-diagonal blocks, while the full unitary group inside each `E_alpha` forces the surviving diagonal block to be scalar. Thus

`P_alpha C P_beta=0` for `alpha!=beta`,

and

`P_alpha C P_alpha=c_alpha P_alpha`.

Positivity of `C` gives `c_alpha>0`, yielding

`C=sum_alpha c_alpha P_alpha`.

No continuity, differentiability, polynomial ansatz, simple spectrum, or one-variable functional formula is required.

## 3. What the extra commuting operator can and cannot buy

`VIS-371` showed that a coordinate-free rule built from `G` alone must be scalar on every full eigenspace of `G`. The present result identifies the exact additional freedom obtained from commuting external structure.

Suppose `G` has a repeated eigenvalue `lambda` and an external Hermitian operator `H` commutes with `G` but has several eigenvalues inside that `lambda`-eigenspace. A joint-equivariant rule may assign different metric weights to those `H` sectors. This is genuinely more information than `G` alone contains, so it is not correct to collapse the rule to `f_G(G)`.

But every such sector remains inside the same `G` eigenspace. Therefore the resulting metric still commutes with `G`. Applying `VIS-370`, the modified Wang squared singular spectrum is obtained by multiplying the baseline Gram eigenvalues by the corresponding positive joint-sector weights. No new cross-Gram orientation, interference, or cancellation channel appears.

So the relevant dichotomy is sharper than “Gram versus external operator.” It is:

- **commuting external structure:** extra labels inside the existing spectral decomposition, still commuting preconditioning;
- **noncommuting external structure:** a genuinely new relative orientation, which must be justified and whose cost/information content must be propagated.

## 4. Wang consequence

The previous frontier said that a noncommuting metric must import something beyond the Gram. That statement is necessary but not sufficient: merely naming an additional physical or geometric Hermitian operator does not yet escape the spectral-filter audit.

For a proposed external operator `H`, first test `[H,G]`. If `H` belongs to a pairwise commuting Hermitian family with `G` and the metric constructor is simultaneous-unitary-equivariant, the present theorem reduces the constructor to joint spectral weights and `VIS-370` applies. The extra operator may justify how those weights are chosen, but it does not create a new orientation of the Wang singular geometry.

A positive-Hilbert continuation that genuinely aims to leave the commuting class must therefore exhibit an externally fixed operator or structure with nonzero commutator against the baseline Gram, or else use preferred coordinates/source data whose non-equivariance is itself an explicit resource. A nonzero commutator is not evidence of arithmetic gain; it is only the first structural gate showing that the candidate is not already joint spectral filtering.

## Prior-art audit

The mathematical representation is classical. A finite family of pairwise commuting Hermitian matrices is simultaneously unitarily diagonalizable. Mnacho Echenim, **Simultaneous diagonalization of pairwise commuting Hermitian matrices**, Archive of Formal Proofs (2022), gives a formalized statement and proof of the general finite-family theorem. Brian D. Sutton, **Simultaneous diagonalization of nearly commuting Hermitian matrices: do-one-then-do-the-other**, *IMA Journal of Numerical Analysis* 44 (2024), 1061–1089, DOI `10.1093/imanum/drad033`, uses the exact commuting theorem as the baseline for the nearly commuting problem.

For equivariant/isotropic tensor-valued functions with multiple symmetric inputs, the literature is substantially richer than in the one-input case. Ken Kamrin and Sanjay Govindjee, **Clarifying the representation of isotropic symmetric tensor-valued functions of two symmetric tensors**, *Mathematics and Mechanics of Solids* 31:1 (2026), 172–182, DOI `10.1177/10812865251340424`, reviews that representation problem and its historical lineage. The present commuting-family statement uses only the elementary stabilizer/commutant consequence after simultaneous diagonalization; it does not claim a new general multi-input isotropic representation theorem.

Standard matrix spectral background is also covered by Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2013). No novelty is claimed for simultaneous diagonalization, joint spectral projectors, commutants, or equivariant matrix-function representation.

The Mathia-specific contribution is the Wang accounting boundary: an “external operator” escapes `VIS-371` as an input source but still does not escape `VIS-370` when the full admitted Hermitian family is commuting. The first possible positive-Hilbert orientation escape therefore requires genuinely noncommuting additional structure, not merely additional commuting observables.

## Dependencies

- `VIS-369`: freely aligned degenerating positive metrics can prescribe the active singular spectrum.
- `VIS-370`: every positive metric commuting with the Wang Gram acts by sectorwise spectral reweighting.
- `VIS-371`: every unitary-equivariant positive metric rule built from the Gram alone is spectral on Gram eigenspaces.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue further narrowed by this result.

## Research consequence

The alternate joint-spectrum representation produces a real information gain over the one-Gram picture: it distinguishes **extra information that only refines Gram degeneracies** from **extra structure that changes relative orientation across Gram sectors**.

Accordingly, future positive-Hilbert Wang candidates should not be credited merely for depending on a second canonical Hermitian observable. If all inputs commute, a coordinate-free constructor remains joint spectral filtering and belongs to the already priced `VIS-370` class. A surviving orientation mechanism must identify and justify noncommuting external structure, source-dependent/non-equivariant information, or leave the finite-dimensional positive-Hilbert setting altogether.