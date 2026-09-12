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

## Separate acquisition conditioning from zero-count conditioning, then justify any genuinely new target geometry

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`.

AF-282--AF-289 show that a finite Dirichlet prefix can be recovered by a well-conditioned mixed frame after the common-clock gauge is removed. AF-290 then identifies a separate target gate: the exact coefficient radius preserving the zero count is distance to the boundary-zero discriminant.

AF-291 proves that the normalized eta margin collapses on every fixed RH-relevant contour despite correct analytic boundary convergence. AF-292--AF-294 show that this collapse cannot be repaired for free by positive diagonal Hilbert scaling, bounded-condition dense Hilbert mixing, or a uniformly quasisymmetric nonlinear reparameterization with honest bad-set transport.

AF-295 closes the most canonical quotient escape. For every homogeneous zero-count failure cone,

`dist_gap([b], P D) = dist(b,D)/||b||`,

so the normalized zero-count margin is exactly the projective distance obtained after removing global complex amplitude and phase. The eta margin therefore still collapses after the natural `C*` quotient with the same asymptotic law, and AF-293's condition-number bill becomes the corresponding projective Hilbert-geometry bill.

AF-296 classifies the canonical scale-dependent metric escape. Weighting projective path length by reciprocal distance `1/r` to the discriminant turns multiplicative margin loss into additive condition distance: reaching a level set `r=epsilon` from `r=r_0` costs exactly `log(r_0/epsilon)`, and the eta ray recedes from every fixed stable core by `log(sqrt(N) H_N(alpha))+O(1)`. This does not recover stability for free: the metric is defined from the target failure set and sends that set to an ideal boundary at infinite distance.

The live question is therefore no longer whether a clever quotient or scale-dependent metric can enlarge the displayed margin. A viable repair must identify an **additional target-null quotient**, genuinely new information, or a **source-natural geometry independently derived from arithmetic structure** and prove that its distortion near the eta ray is quantitatively comparable to what condition geometry requires without defining the geometry from the zero-count discriminant itself.

## Treat the information bills separately

Finite local degree, prime breadth, mixed-channel coupling, sample count, frame conditioning, nuisance gauge, residual jitter, target distance to ill-posedness, linear condition number, nonlinear relative distortion, quotient geometry, and target-dependent condition geometry are distinct resources. Exact or stable upstream recovery is useful only if the final observable remains stable in its own quotient geometry. AF-295 shows that the obvious scalar quotient is already encoded by the normalized margin; AF-296 shows that singular metric repair can always re-express collapse, but only by paying an explicit target-aware geometric price.