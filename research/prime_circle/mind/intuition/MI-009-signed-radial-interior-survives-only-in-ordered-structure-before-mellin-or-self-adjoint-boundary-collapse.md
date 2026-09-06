# MI-009 — Signed radial interior survives only before Mellin/refinement-positive collapse

**Evidence level:** exact through PC-185

## Core intuition

The signed cyclotomic radial flux is a genuine prime-power selector, but a large source-native class of scalar/positive radial operations erases that selectivity. The surviving information must participate in an ordered, shell-dependent, or genuinely multi-carrier operation before positive scalarization.

## Strongest justified principle

PC-179 gives the exact positive-on-prime-powers flux and its classical zeta Mellin transform. PC-180--PC-181 show constant symmetric coupling endpoint-collapses and one-carrier functional calculus becomes selector-blind. PC-182 shows that adding nonconstant positive radial depth restores coercivity only by filling the Mangoldt nullspace. PC-183 identifies positive refinement-covariant two-depth kernels with Mellin mixtures, while PC-184 proves finite Euler jets remain one Mellin carrier.

PC-185 closes the obvious nonlocal extension: every fixed bounded shell-independent operator commuting with the intrinsic integer refinement dilations is a Mellin multiplier. A finite family still has shell Mellin rank one, and because the shell amplitude is zero-free in its natural half-plane, every nontrivial positive covariant quadratic readout is positive on every shell. Thus neither locality nor filter complexity is the relevant boundary; the one-carrier refinement commutant itself is.

## What remains possible

Shell/cross-level dependent operators, a second source field not obtained by a fixed equivariant transform, nonlinear or ordered cross-shell constructions, or source-forced sign-indefinite couplings remain outside the theorem. Any continuation must retain mixed-prime discrimination after its final operation.

## Status / novelty

Mellin harmonic analysis and commutant facts are classical. The durable synthesis is the operation-order boundary: **positive/refinement-equivariant radial completion trades arithmetic selectivity for coercivity, and bounded nonlocality does not change that tradeoff**.

## Falsification criterion

Find a bounded shell-independent refinement-equivariant radial operator that is not a Mellin multiplier, or a nonzero positive covariant readout in the PC-185 class that vanishes on a mixed-prime shell while remaining positive on a prime power.

## Lean-formalizable core

- The refinement-semigroup-to-full-dilation commutant reduction.
- Mellin rank-one factorization for finite operator families.
- Zero-free shell amplitude implication for positive covariant readouts.