# MI-008 — Fixed-dimensional Gram lags are a Newton-clock null

**Evidence level:** proved

## Core intuition

A fixed-dimensional vector of consecutive Gram-point prime-phase lags can display coherence, deterministic curves, marginal Haar behavior, or full joint Haar behavior without introducing any new arithmetic randomness. The exact inverse Gram clock already generates all of these regimes. The natural coordinates are successive Newton finite differences of that clock.

Visual complexity in a finite delay embedding is therefore not evidence of a new prime-phase source unless it survives this deterministic clock quotient.

## Strongest justified claim

VIS-150 identifies the single-lag transition near `h~log^2 N`. Below that scale a dephased lag cloud collapses, at critical scale it traces a deterministic logarithmic torus curve, and above it clock shear begins to create Haar-looking marginals.

VIS-151 removes the upper-range restriction caused by the earlier Taylor approximation. For any well-sampled lag satisfying `h M_N/(N log^2 N)->infinity`, every fixed finite-support torus character cancels by an exact first-derivative estimate. Thus even macroscopic single lags have Haar population for deterministic clock reasons.

VIS-152 treats an equal-step `r`-lag vector. Every joint character has a first nonzero lag moment of some order `q<=r`; the deepest possible cancellation is the `r`-th finite difference. The supercritical joint-Haar threshold is exactly controlled by

`M_N h^r/(N^r log^2 N)`,

while below the corresponding scale an explicit order-`r` character retains modulus-one coherence. For `h=o(N)`, the transition is `h^r ~ N^(r-1) log^2 N`.

VIS-153 resolves the critical window. A triangular integer automorphism sends ordinary lag coordinates to successive Newton differences. At order-`r` critical scaling, the first `r-1` coordinates converge jointly to Haar and the top coordinate converges to an explicit one-parameter deterministic prime-torus curve. No information is discarded by the transform.

## Synthesis of evidence

The entire fixed-dimensional equal-step phase portrait is classified by the derivative hierarchy of the inverse Riemann--Siegel clock. Adding finitely many delays buys a higher order of clock cancellation, not a new source. Random-looking lower differences and the surviving critical top curve are two faces of the same deterministic mechanism.

This sharply narrows visually motivated prime-phase research. A credible residual must use structure outside the fixed-dimensional consecutive delay algebra: growing dimension/support, irregular sampling that breaks the finite-difference clock model, or an independently informative analytic coordinate.

## Counterevidence / boundary cases

The theorems fix the delay dimension and character support. They do not control `r=r(N)`, prime characters whose support/coefficients grow with `N`, irregular lag sets, nonconsecutive Gram indices, or joint statistics with zeta values, derivatives, zeros, or other analytic coordinates.

Haar convergence here is weak fixed-character convergence, not a stochastic independence theorem. The interpretation is a deterministic null, not a claim that Gram phases are genuinely random.

## Epistemic status

**Exact fixed-dimensional clock classification away from and at the critical scale:** consecutive equal-step Gram lag vectors are governed by Newton finite differences of the inverse Gram clock, with coherent, mixed critical, and Haar regimes determined by the corresponding shear scale.

## Novelty/prior-art status

VIS-151--VIS-153 explicitly use classical Gram asymptotics, exponential-sum bounds, and compact-group Fourier criteria and make no broad novelty claim. This intuition records their role as a Mathia control family.

## Falsification criterion

Exhibit a fixed `r`, equal-step consecutive Gram-lag statistic whose limiting fixed-character behavior is not captured by the Newton-difference hierarchy under the hypotheses of VIS-151--VIS-153, or show that the critical product law fails for an admissible character. Either would invalidate the deterministic-null classification.

## Lean-formalizable core

The finite algebraic statement that the triangular lag-to-Newton-difference exponent matrix lies in `GL_r(Z)` and exactly converts lag coordinates into forward finite differences is a natural finite formal target; the asymptotic Fourier analysis is separate.
