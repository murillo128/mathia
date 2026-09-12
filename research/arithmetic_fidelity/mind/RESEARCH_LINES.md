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

## Separate source geometry, nuisance symmetry, acquisition conditioning, and target ill-posedness

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`.

AF-244--AF-281 separate source category, breadth, coupling, resolution, periodic transport, and mixed-channel completeness. Finite local Euler degree makes prime-power depth finite, but global Euler fidelity still requires unbounded prime breadth; separate resonant marginals lose joint information, while complete mixed samples recover ordinary Dirichlet coefficients exactly.

AF-282--AF-289 price the finite-prefix two-prime repair. On known support `1,...,N`, joint phase spacing is `Theta(1/N)`, stable mixed degree is `Theta(N)`, and an unweighted `O(N)` raw subframe can have uniformly bounded condition number. A common rowwise timing offset is the exact gauge `F(s)->F(s+i sigma)`, so horizontal zero geometry does not pay for absolute clock origin. Only the residual differential radius

\[
r(\tau)=\inf_\sigma\max_j|\tau_j-\sigma|
=\frac{\operatorname{osc}(\tau)}2
\]

enters the coefficient-orbit estimate.

AF-290 closes the first concrete target-level gap. For a finite Dirichlet polynomial `P_b` and a compact Jordan boundary `Gamma`, the exact coefficient-space distance to a boundary-zero collision is

\[
d_\Gamma(b)
=\min_{z\in\Gamma}
\frac{|P_b(z)|}{(\sum_{n\le N}n^{-2\operatorname{Re}z})^{1/2}}.
\]

The zero count inside `Gamma` is protected for every coefficient perturbation smaller than this radius, and this margin is covariant under the common-clock vertical-translation gauge. Thus a decoder bound of size `eta` transfers to the zero-count target only after the independent gate `eta<d_Gamma(b)/||b||_2` is proved. There is no uniform coefficient-to-zero-count modulus on classes whose normalized boundary margin can approach zero.

The live question is now target-specific rather than another acquisition refinement: identify natural RH-relevant finite carriers or approximants whose normalized distance to the appropriate zero/discriminant locus has a nontrivial lower bound, or prove that this margin necessarily collapses with breadth. Fixed-height observables that retain absolute imaginary origin must be treated separately because they do not descend through the common-clock quotient.

## Treat the information bills separately

Finite local degree, prime breadth, mixed-channel coupling, sample count, frame conditioning, nuisance gauge, residual jitter, and target distance to ill-posedness are distinct resources. Exact or stable upstream recovery is useful only if the final observable is stable in its own quotient geometry. A target-invariant nuisance should be removed before calibration; a target discriminant margin cannot be inferred from source conditioning.
