# MI-001 — Anchoring is necessary, but same-shell pointing and linear refinement still classicalize

**Evidence level:** supported by exact and literature-backed negative results

## Core intuition

Breaking rotational symmetry by naming a vertex or retaining a local matrix is necessary to avoid the coarsest Prime-Circle quotients, but it is not sufficient. The newer evidence shows that several apparently stronger ways of preserving a mark — local spectral measures, Schur complements, divisor-level Kron refinement, and even a joint metric/chiral same-level algebra — still reduce to classical shell data or to a low-rank interaction through already-existing vertices.

## Strongest justified principle

The one-shell obstruction is now substantially sharper than “unmarked spectra forget the anchor.”

- PC-038 proves that on a vertex-transitive circulant shell the pointed local spectral measure is the global spectral measure divided by the shell size, while vertex-deleted determinants and Schur self-energies are characteristic-polynomial derivatives. Pointing before diagonalization therefore does not create new local arithmetic data when the underlying operator remains translation invariant.
- PC-039 shows that the canonical inverse-square divisor refinement by Kron/Schur reduction is path independent. Eliminating intermediate divisor shells creates no refinement holonomy or order-sensitive memory.
- PC-044 and PC-045 show that the first square-free primitive metric and oriented/chiral blocks reduce exactly to finite Dirichlet-character packages at fixed special values `L(-1,chi)` and `L(0,chi)`.
- PC-046 shows that the natural same-level metric/chiral pair is not an independent bulk noncommutative system: its polynomial relation fails after primitive compression only through a defect factoring through old vertices, with correspondingly low-rank commutator control.

Together these findings shift the live variable from “a pointed shell” to **how genuinely new vertices couple to previously existing levels before those old degrees of freedom are eliminated**.

## What remains possible

This does not rule out every cross-level construction. A simultaneous operator on several labeled shells can retain old/new couplings that a Schur reduction removes; a shell-dependent kernel can break the full circulant commutant; and a nonlinear response can amplify a low-rank old-vertex defect. The surviving mechanism must use one of those extra structures intrinsically rather than merely rename a one-shell cofactor, character sum, or staged Schur complement.

## Status / novelty

The classicalization identities and low-rank factorization are persisted findings. The synthesis is a supported design constraint for future Prime-Circle operators, not a theorem about all multilevel constructions.

## Falsification criterion

Construct a canonical same-shell or path-independent linear refinement observable built only from the audited translation-invariant shell operators whose value is not determined by the corresponding full-shell spectral/Dirichlet data and old-vertex coupling. Conversely, a genuinely simultaneous multilevel construction would evade this intuition only if the old/new interaction remains an active state rather than being compressed away.

## Lean-formalizable core

- Cofactor/characteristic-polynomial derivative identities for circulant matrices.
- Associativity/quotient identity for staged Schur complements.
- Polynomial relation and old-vertex factorization in the metric/chiral pair.
- Rank bounds under compression through an old-vertex subspace.
