# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source sign complexity to a quantitative finite-order Euler modulus

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-215--AF-220 force ordered sign complexity but leave the quantitative transfer into the shrinking Euler-log observation window open. The next theorem must relate the source sign budget to a separation or curvature modulus at the resolution actually consumed by the target.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

AF-221--AF-233 show that localization has a real information bill and that contraction can lower it only in the metric actually used downstream. A useful compression claim still needs both a cheaper target geometry and a theorem that the final arithmetic argument consumes only that target.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

AF-234--AF-243 show that the RH root-rate endpoint tolerates large output error but is extremely sensitive to breaking the binomial cancellation orbit in the source representation. The live bridge must assemble the required cancellation orbit before the root-rate quotient is formed.

## Separate acquisition conditioning from zero-count conditioning, then derive any surviving geometry from the source rather than the failure set

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`.

AF-282--AF-289 show that a finite Dirichlet prefix can be recovered by a well-conditioned mixed frame after the common-clock gauge is removed. AF-290 then identifies a separate target gate: the exact coefficient radius preserving the zero count is distance to the boundary-zero discriminant.

AF-291 proves that the normalized eta margin collapses on every fixed RH-relevant contour despite correct analytic boundary convergence. AF-292--AF-294 show that this collapse cannot be repaired for free by positive diagonal Hilbert scaling, bounded-condition dense Hilbert mixing, or a uniformly quasisymmetric nonlinear reparameterization with honest bad-set transport.

AF-295 closes the canonical quotient escape: for every homogeneous zero-count failure cone,

`dist_gap([b], P D) = dist(b,D)/||b||`,

so the normalized zero-count margin is exactly the projective distance obtained after removing global complex amplitude and phase.

AF-296 exhibits reciprocal-distance condition geometry as a category-changing escape: weighting length by `1/r` sends the discriminant to infinite distance and logarithmizes approach to it. AF-297 now shows that this is not a peculiarity of the reciprocal profile. For **every fixed target-radial conformal density** `phi(r)`, the boundary distance is exactly `int_0^r phi(t)dt`; if that integral is finite the collapsing margin still collapses, and if it diverges the bad set moves to an infinite-distance ideal boundary. A scale-dependent finite order-one repair must reach density at least `c/r_N` in the collapsing layer, hence `sqrt(N)H_N(alpha)` on the eta ray, with metric multiplier of order `N H_N(alpha)^2`.

The live question is therefore narrower. A useful geometry cannot be merely another radial function of target distance. It must identify an **additional target-null quotient**, genuinely new source information, or a **source-natural nonradial/anisotropic geometry** derived independently from arithmetic structure and prove that it supplies the necessary reciprocal-margin scale without defining that scale from the zero-count discriminant itself.

## Treat the information bills separately

Finite local degree, prime breadth, mixed-channel coupling, sample count, frame conditioning, nuisance gauge, residual jitter, target distance to ill-posedness, linear condition number, nonlinear relative distortion, quotient geometry, target-dependent condition geometry, and source-derived anisotropy are distinct resources. Exact or stable upstream recovery is useful only if the final observable remains stable in its own quotient geometry. AF-295 shows that the obvious scalar quotient is already encoded by the normalized margin; AF-296--AF-297 show that radial singular metric repair can re-express collapse only by either sending failure to infinite distance or paying the reciprocal raw-margin scale explicitly.