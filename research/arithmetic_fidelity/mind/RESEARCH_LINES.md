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

AF-290 identifies the exact finite zero-count gate. For a finite Dirichlet polynomial `P_b` and a compact Jordan boundary `Gamma`,

\[
d_\Gamma(b)
=\min_{z\in\Gamma}
\frac{|P_b(z)|}{(\sum_{n\le N}n^{-2\operatorname{Re}z})^{1/2}}
\]

is the Euclidean distance to the boundary-zero discriminant. The zero count is protected only below this target-specific radius, independently of how well conditioned the acquisition map is.

AF-291 now resolves the first natural increasing-breadth test negatively. For the raw Dirichlet eta truncations on any fixed zero-free compact contour in `Re(s)>0`, the analytic boundary modulus stays uniformly separated from zero while the normalized coefficient-space margin

\[
\delta_{\Gamma,N}
=\frac{d_{\Gamma,N}}{\|b^{(N)}\|_2}
\]

still collapses sharply. If `alpha=min_(z in Gamma) Re z`, then

\[
\delta_{\Gamma,N}\asymp
\begin{cases}
N^{-1/2}, & \alpha>1/2,\\
(N\log N)^{-1/2}, & \alpha=1/2,\\
N^{\alpha-1}, & 0<\alpha<1/2.
\end{cases}
\]

Thus analytic convergence to the correct zero count and robustness to relative `ell^2` coefficient error are different resources. A decoder using the AF-290 gate must eventually keep its relative error strictly below this shrinking margin; a breadth-independent relative error cannot suffice for raw eta truncations.

The live target is no longer to ask abstractly whether a natural RH-relevant carrier can lose target margin: one already does. The useful alternatives are to find a representation/preconditioner/quotient whose **target-relative** discriminant geometry has a genuinely better breadth law, or to prove that a broader class of RH-relevant carriers inherits an unavoidable collapse. Fixed-height observables that retain absolute imaginary origin remain separate because they do not descend through the common-clock quotient.

## Treat the information bills separately

Finite local degree, prime breadth, mixed-channel coupling, sample count, frame conditioning, nuisance gauge, residual jitter, target distance to ill-posedness, and the **breadth law of that target distance** are distinct resources. Exact or stable upstream recovery is useful only if the final observable is stable in its own quotient geometry. A target-invariant nuisance should be removed before calibration; a target discriminant margin cannot be inferred from source conditioning or from uniform analytic convergence alone.
