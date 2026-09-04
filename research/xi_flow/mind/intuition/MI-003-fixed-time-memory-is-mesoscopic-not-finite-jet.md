# MI-003 — Fixed-time Xi memory is mesoscopic; the remaining mean-removal mechanism must be genuinely nonlocal or source-specific

**Evidence level:** supported through XF-022; finite-jet, linearized-scale, and finite-range collision statements are exact in their stated regimes

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. Capacitary and cross-ratio reorganizations show that the far exterior can be made genuinely small using source-valid super-mesoscopic buffers, so lack of spatial room is no longer the principal obstruction.

The live bottleneck is mean/span removal near the boundary. XF-021 rules out compact compression-sensitive centered convex single-gap entropies. XF-022 now shows that simply overlapping local quadratic mean-removal blocks does not fix the problem: every nontrivial finite-range symmetric translation-invariant quadratic kernel annihilating constants has a positive collision-spike configuration. The remaining route must be genuinely global/projective/nonlinear or must use Xi-specific source information to exclude the adversarial local geometry.

## Strongest justified principle

XF-006 rules out robust finite collision jets as Xi-specific; XF-007--XF-013 identify the mesoscopic `log^2 T` scale and the Cauchy/endpoint carrier. XF-014--XF-020 give exact positive-conductance gap diffusion, collision-safe uncentered cross-ratio localization, aggregate far-tail bounds, and source-valid buffers whose leakage is `o(1)`.

XF-021 proves the centered-convex boundary dichotomy: compression sensitivity below a positive reference creates an arbitrarily positive adjacent-collision flux under compact localization.

XF-022 closes the most direct overlap repair. For a finite-range constant-annihilating quadratic kernel `L`, a collapsing gap probes `A L`, where `A` is the nearest-neighbor discrete Laplacian. Because `A L` has zero second moment, it cannot have the one-sided off-diagonal M-matrix sign unless it vanishes identically. Hence some positive local gap configuration forces `Q_L' -> +infinity`. Uniform sums of fixed-length overlapping block variances are a direct corollary.

## What remains possible

The live theorem should use an exact nonlocal span/endpoint-flux identity, a nondecaying or scale-dependent mean remover with controlled tails, a nonlinear/projective cross-ratio assembly, or an independent Xi source theorem that excludes the asymmetric collision patterns used by the no-go. Fixed-length centered stencils are closed unless they add such structure.

## Status / novelty

Fractional localization, discrete Laplacians, convex entropy, cross-ratios, and global zero counting are classical ingredients. The synthesis is the sharpened boundary: **far-tail capacity is affordable, but both compact pointwise centering and finite-range quadratic mean removal reintroduce collision-positive flux**.

## Falsification criterion

Derive a source-forced nonlocal/span identity that controls the near buffer with a positive fixed-time margin, or construct source-admissible Xi-like configurations that defeat every proposed global assembly while respecting the current counting/buffer constraints.

## Lean-formalizable core

- Mesoscopic `log^2 T` memory scale.
- Block cross-ratio tail bound and source-valid buffer scaling.
- Centered-convex collision-spike dichotomy.
- Finite-range `A L` second-moment sign obstruction.
