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

## Separate acquisition conditioning from zero-count conditioning, then price representation distortion

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`.

AF-282--AF-289 show that a finite Dirichlet prefix can be recovered by a well-conditioned mixed frame after the common-clock gauge is removed. AF-290 then identifies a separate target gate: the exact coefficient radius preserving the zero count is distance to the boundary-zero discriminant.

AF-291 proves that the normalized eta margin collapses on every fixed RH-relevant contour despite correct analytic boundary convergence. AF-292 shows that no positive diagonal Hilbert reweighting improves the critical-strip power. AF-293 now classifies arbitrary positive-definite Hilbert mixing under a condition-number budget:

`D_(Gamma,N)(K) asymp_Gamma min(1, sqrt(K)/(sqrt(N) H_N(alpha)))`.

Thus bounded-condition dense mixing is no better asymptotically than the raw coordinates. Making the margin order one requires `kappa(G_N) asymp N H_N(alpha)^2`, or `kappa_2(A_N) asymp sqrt(N) H_N(alpha)` for `G=A* A`, exactly the reciprocal scale of the raw margin.

The live escape is therefore not merely “use non-diagonal mixing.” It must supply an independently justified anisotropic geometry whose conditioning bill is mathematically meaningful, or use a nonlinear representation, target-relevant quotient, non-Hilbert topology, or another carrier whose upstream error can be proved small in the target's own stability geometry.

## Treat the information bills separately

Finite local degree, prime breadth, mixed-channel coupling, sample count, frame conditioning, nuisance gauge, residual jitter, target distance to ill-posedness, and representation distortion are distinct resources. Exact or stable upstream recovery is useful only if the final observable remains stable in its own quotient geometry, and a coordinate transform does not remove instability when its condition number grows at the reciprocal target-margin scale.