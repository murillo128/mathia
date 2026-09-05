# MI-014 — Target-relative spectral fidelity is projection geometry unless the coefficient metric is source-canonical

**Evidence level:** supported through AF-136 by exact whitening, Moore--Penrose projection identities, and complete fixed-target congruence invariants

## Core intuition

A source Gram matrix does not carry an intrinsic hierarchy of spectral magnitudes under arbitrary changes of generator coordinates. Once the source representation is whitened, the information relevant to a declared target is simply how much of each target direction lies in the retained source subspace. The stable invariant is therefore projection/principal-angle geometry, not the raw eigenvalue scale of a coordinate-dependent Gram matrix.

Spectral truncation becomes meaningful only after the source supplies an independent coefficient Hilbert structure, restricted gauge, or other normalization that makes singular values physically or mathematically comparable. Without that extra geometry, keeping the “largest eigenmodes” is a coordinate choice rather than an intrinsic fidelity statement.

## Strongest justified principle

AF-135 considers a target vector `k` against a retained source system with Gram matrix `G` and cross-coordinate vector `b`. The exact squared residual after optimal reconstruction is

`dist(k,ran A)^2 = kappa - b^* G^dagger b`.

After whitening, this is exactly the norm of the target component orthogonal to the retained source span. The corresponding sensitivity is controlled by the whitened coordinate `G^{dagger/2} b`; source eigenvalues matter only through the declared coefficient metric used to define the whitening.

AF-136 treats a whole target family. If `C` records source--target pairings, then

`Q=C^* G^dagger C`

is the target projection Gram, equivalently `U^* P_M U` after whitening. Under the full invertible generator gauge, `(rank G,Q)` is a complete fixed-target invariant. The positive eigenvalue magnitudes of `G` can be altered by congruence without changing the represented source subspace or `Q`.

The best rank-`s` target approximation is correspondingly governed by the eigenvalues/principal angles of the target projection geometry; for the scoped result the optimal residual threshold is `lambda_{s+1}(Q)`. This is target-relative information, not a canonical ordering of the source coordinates themselves.

## What remains possible

A genuine spectral-fidelity theorem may still use singular values when the source construction provides a canonical coefficient metric, energy, probability law, operator ideal, or restricted transformation group. That additional structure must be stated and defended before a spectral cutoff is interpreted as information loss.

For Mathia carriers without such a metric, formulate fidelity in terms of subspace projection, principal angles, or the target projection Gram. If a proposed spectral scale changes under an admissible generator reparameterization while the target projection does not, the scale is representation metadata rather than intrinsic evidence.

## Status / novelty

Gram matrices, pseudoinverses, whitening, congruence, principal angles, and projection Grams are classical linear algebra. The persisted synthesis is the category boundary: **fixed-target spectral fidelity is intrinsically projection geometry; raw source spectral magnitudes require an independently justified coefficient geometry before they can carry mathematical meaning**.

## Falsification criterion

Find two full-generator-gauge-equivalent source representations with the same target projection Gram but different fixed-target recoverability, or produce an intrinsic source spectral ordering invariant under the admitted full congruence gauge without adding extra coefficient geometry.

## Lean-formalizable core

- Pseudoinverse projection identity `C^*G^dagger C=U^*P_MU`.
- Congruence invariance of the target projection Gram.
- Completeness of `(rank G,Q)` for the fixed-target gauge.
- Principal-angle/rank-`s` approximation characterization.
