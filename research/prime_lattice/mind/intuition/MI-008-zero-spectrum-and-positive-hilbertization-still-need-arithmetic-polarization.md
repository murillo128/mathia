# MI-008 — Native kernel positivity and completed zero-sensitive positivity are different gates

**Evidence level:** supported by exact literature-backed spectral, RKHS, screw, and explicit-formula constructions through PL-144

## Core intuition

The prime-exponent program now has several strong positive structures that might superficially look like RH mechanisms. The native Hedenmalm--Lindqvist--Seip zeta kernel is positive definite and even infinitely divisible under all positive kernel powers in its evaluation half-plane; exact global spectral realizations of the zeta divisor exist; and completed zeta data support canonical positive Hilbert/screw structures.

These facts do not compose automatically into zero localization. The decisive boundary is **global completion plus a zeta-specific sign/polarization on the zero-sensitive object**. Native Euler-coordinate positivity is unconditional and generic; after completion, the relevant positivity statements are already RH-equivalent.

## Strongest justified principle

PL-118--PL-120 give the classical spectral/polarization template. Deninger's mechanism would force the half-axis only after a positive arithmetic Hodge pairing makes the centered flow skew-adjoint. Meyer realizes every zeta zero spectrally, including hypothetical off-line zeros. Suzuki constructs positive completed zeta Hilbert structure without RH, while equality with the zero-sensitive Weil form remains the load-bearing statement.

PL-142 tests a natural RKHS upgrade of the native Bohr geometry. The standard zeta reproducing kernel `K(s,u)=zeta(s+conj(u))` is not complete Pick: the reciprocal coefficient at every two-prime square-free point is `mu(pq)=+1`, violating the McCarthy--Shalit sign criterion. The obstruction is finite, algebraic, and unaffected by ordinary coefficient damping. Canonical complete-Pick repairs change the lattice weights to Drury--Arveson path-counting weights and become universal under mere rational independence of the logarithmic generators.

PL-143 shows that weakening complete Pick to kernel-power positivity does not help. For every `tau>0`, `K^tau` is positive definite, and `log K` is itself positive definite with feature support only on prime-power rays `r e_p`. Vertical slices are classical compound-Poisson laws with jumps `-r log p`. The same construction works for generic independent Euler energies, so this native infinite divisibility is not rational-prime rigidity and never crosses the Euler-product boundary.

After global completion the situation changes qualitatively. Nakamura--Suzuki's completed explicit-formula exponent has an infinitely divisible characteristic function exactly under RH, with zero ordinates as real Lévy jumps. PL-144 then identifies this with Suzuki's screw positivity through the classical Schoenberg correspondence and sharpens the target further: for the actual completed zeta function, Suzuki's pointwise sign `Psi(t)>=0` is already equivalent to RH, and under RH it automatically upgrades to the full screw/CND/Lévy structure.

## What remains possible

A surviving prime-lattice route should not seek another positive avatar of the native zeta kernel or another repackaging of the completed screw/Lévy criterion. The minimal useful target is upstream: derive the sign of the completed arithmetic balance `Psi(t)` — or an equivalent polarization of the same zero-sensitive object — from exact rational-prime structure without importing an RH-equivalent positivity assumption.

Mixed exponent-vector geometry is relevant only if it can be shown to force that completed sign. The prime-power axes already carry the von Mangoldt input; adding full-lattice decoration without a sign-producing global operation does not close the gap.

## Status / novelty

HLS spaces, complete-Pick theory, Drury--Arveson kernels, compound-Poisson zeta distributions, Schoenberg negative type, Suzuki screw functions, and Nakamura--Suzuki infinite divisibility are prior art. The Mathia synthesis is the sharpened gate: **native positive interpolation/probability geometry is universal, while completed positivity is already the RH-level object; the missing theorem is the arithmetic sign/polarization itself**.

## Falsification criterion

Produce an RH-sensitive transition in a native HLS kernel property that survives the PL-142/143 controls, or derive `Psi(t)>=0` for all real `t` from an upstream rational-prime mechanism without assuming a zero-localization, Weil-positivity, screw, CND, or Lévy criterion of equivalent strength.

## Lean-formalizable core

- Reciprocal-coefficient complete-Pick obstruction at `pq`.
- Positive Dirichlet coefficients of `zeta^tau` and prime-power support of `log K`.
- Compound-Poisson pushforward of prime-power energies.
- Screw-kernel/Schoenberg/CND equivalence.
- Logical reduction from completed positivity avatars to the zeta-specific scalar sign target.
