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

AF-291 proves that the normalized eta margin collapses on every fixed RH-relevant contour despite correct analytic boundary convergence. AF-292 shows that no positive diagonal Hilbert reweighting improves the critical-strip power. AF-293 classifies arbitrary positive-definite Hilbert mixing under a condition-number budget:

`D_(Gamma,N)(K) asymp_Gamma min(1, sqrt(K)/(sqrt(N) H_N(alpha)))`.

AF-294 now closes the uniformly controlled nonlinear version of the same escape. For relative discriminator margin `rho_X=dist(x,D)/d(x,a)`, any injective `eta`-quasisymmetric representation with honest transport of the bad set satisfies

`1/eta(1/rho_X) <= rho_Y <= eta(rho_X)`.

Hence one uniform distortion function cannot turn `rho_N -> 0` into an order-one target margin. A nonlinear family that repairs the eta margin must let its relative distortion degenerate at the shrinking discriminator scale, change the bad set/target category, add genuinely new information, use a quotient/compression requiring its own fidelity analysis, or leave the quasisymmetric metric category.

The live question is therefore not whether a clever coordinate system can enlarge the margin. It is whether the source supplies a **natural reason** for the required scale-dependent distortion or for a genuinely different target geometry, rather than merely relocating the same instability into the representation.

## Treat the information bills separately

Finite local degree, prime breadth, mixed-channel coupling, sample count, frame conditioning, nuisance gauge, residual jitter, target distance to ill-posedness, linear condition number, and nonlinear relative distortion are distinct resources. Exact or stable upstream recovery is useful only if the final observable remains stable in its own quotient geometry. AF-293--AF-294 show that neither bounded-condition linear mixing nor uniformly quasisymmetric nonlinear reparameterization removes a vanishing target margin for free.