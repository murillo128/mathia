# MI-001 — Weil positivity needs a sign-producing global operation, not a positive-looking ingredient

**Evidence level:** supported by several decisive obstructions

## Core intuition

The Weil-positivity search has repeatedly found mathematically natural objects that are positive, self-dual, or Hilbert-geometric in some local sense. None of those properties survives as the required global sign theorem automatically. The missing mechanism is therefore not “find something positive near the primes”; it is a **canonical global operation whose own structure produces the correct sign after finite-prime, archimedean, polar, and cross-term contributions are assembled**.

## Strongest justified principle

Several independent routes now fail for different reasons.

- WP-008: Tate's adelic Fourier transform gives the correct completed self-duality and critical axis, but the even global Fourier involution has both `+1` and `-1` eigenspaces. Self-duality is not positivity.
- WP-010: orthogonal projections, Gram matrices, and Schur complements attached to the Nyman subspace are positive for universal Hilbert-space reasons. RH is hidden in a **vanishing/totality** condition, so converting the projection to a signed reflection merely repackages the hard statement.
- WP-013: the exact finite Prime-Lattice Mangoldt measure gives a genuinely positive Laplace/Hankel kernel, but the canonical pole subtraction already produces a negative diagonal and the full gamma/polar completion tends to `-infinity` on the real axis. The completed zeta object exits the same positive moment cone.
- WP-014: the exact Prime-Flute Schiffer coupling is pointwise positive, yet every nontrivial `2 x 2` kernel matrix is indefinite. Pointwise sign is not positive definiteness.

These examples remove four common shortcuts: symmetry, totality, positive local measure, and pointwise positive interaction. A viable Weil geometry must explain the sign of the **completed coupled form**, not inherit it from one component or manufacture it by a universal positive functional calculus.

## Evidence against overgeneralization

This does not imply that no Mathia-native positivity exists. It rules out only direct promotions of the audited objects. A quotient, cohomological/intersection pairing, boundary-response map, reflection-positive compression, or another global construction could change the sign structure nontrivially if its positivity theorem is independent of RH and its arithmetic normalization is forced.

Nor should the finite positive structures be discarded. WP-004 and WP-013 show that the finite Mangoldt weights already admit exact positive realizations. The unresolved issue is how to couple them to the archimedean/polar sector without either losing positivity or inserting the desired Weil functional by hand.

## Status / novelty

The individual sign obstructions are exact or literature-backed findings. The synthesis is a supported program-level constraint: **the sought theorem must generate positivity at the completed level rather than merely preserve positivity of a chosen component**.

## Falsification criterion

Refute this intuition by deriving the full required Weil-type positivity from one of the audited positive/self-dual ingredients using only a canonical operation already forced by that ingredient, while showing that no RH-equivalent totality, zero divisor, or hand-picked sign correction has been inserted.

## Lean-formalizable core

- A self-adjoint involution with both `+1` and `-1` eigenvectors is indefinite.
- Orthogonal-projection positivity and the equivalence `2P-I >= 0 <-> P=I`.
- One-point negative-diagonal obstruction to positive-semidefinite Hankel kernels.
- `2 x 2` determinant test distinguishing pointwise positive kernels from PSD kernels.
