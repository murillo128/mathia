# MI-003 — The Nyman obstruction is target/model-space data, not generator spectral geometry

**Evidence level:** proved for the structural separations; the residual discrete classification is open

## Core intuition

The prime-exponent semigroup already has a serious RH-equivalent Hilbert-space realization in Nyman--Beurling--Báez-Duarte theory. The difficult information is not hidden in a new spectrum of the commuting dilation generators. It lives in whether a **distinguished target** lies in the closed span, and in the model-space/divisibility defect that survives after the common arithmetic factors are accounted for.

## Strongest justified principle

PL-017 identifies the exact prime-exponent semigroup

\[
T_mT_n=T_{mn},\qquad T_m=\prod_pT_p^{v_p(m)},
\]

whose Mellin transform multiplies by `m^(1/2-s)`. On the critical boundary these are precisely the log-prime phases. Nevertheless RH is not an eigenvalue statement for `T_m`; it is the totality statement that the Nyman span contains the constant target.

PL-019 then identifies the residual integer-semigroup classification with Balazard's classical open problem: after imposing the zero-divisibility constraints, is the sparse integer-generated closed span exactly the expected invariant subspace? The continuous real-dilation analogue is classifiable, but the one-sided times `{log n}` leave a genuine discrete completeness problem.

PL-020 gives a decisive information-loss warning. If `B_Z` is the Blaschke product of hypothetical zeta zeros in `Re(s)>1/2` and `psi_n=B_Z phi_n`, then multiplication by the inner function is isometric, so every generator Gram matrix is unchanged:

\[
\langle\psi_m,\psi_n\rangle=\langle\phi_m,\phi_n\rangle.
\]

The finite approximation error instead splits orthogonally into a rigid model-space zero term plus a residual arithmetic approximation term. Thus eigenvalues, condition numbers, frame bounds, whitening, or any other **generator-Gram-only** statistic cannot detect precisely the off-line inner factor whose absence RH requires.

PL-021 supplies a useful contrast: moving the Möbius orientation to the native Bohr coefficient `H^2` makes it cyclic unconditionally wherever the vector belongs to that space. The RH-sensitive analytic continuation has been discarded rather than solved.

## What remains fertile

The remaining Nyman question must retain target-relative data: cross-correlations with the reproducing-kernel target, model-space projections, multiplicity-sensitive divisibility, Vasyunin dual information, or another invariant that is not preserved under common inner multiplication. A quantitative theorem about the de-Blaschke discrete span could be valuable, but it must address Balazard's known classification frontier rather than merely rediscovering the semigroup formulation.

## Status / novelty

The semigroup, totality criterion, Balazard problem, Hardy inner-factor identities, and Bohr cyclicity are prior art or exact derived consequences. The synthesis is a supported route discriminator: **generator spectral beauty is orthogonal to the actual RH obstruction unless the target/model-space relation is retained**.

## Falsification criterion

Refute the narrow principle by deriving the off-line Blaschke factor, or its triviality, from generator Gram data alone despite the exact inner-isometry identity above, without supplying target evaluations or any other non-Gram information.

## Lean-formalizable core

- Prime factorization of the dilation semigroup.
- Isometry of multiplication by an inner function and invariance of finite Gram matrices.
- Orthogonal decomposition of distance to `B_Z A_M` into model-space and de-Blaschke approximation terms.
- Abstract lemma distinguishing generator-only data from target-relative projection data.
