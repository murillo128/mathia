---
id: CLUE-prime-flute-critical-jacobi-square-root-decay-window
type: research-clue
status: proposed
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate.md
---

# Does the critical Jacobi edge leave a narrow supercritical smoothing window?

## Observation

PF-247 turns the fixed axis compactification into two asymptotically constant parity-Jacobi chains. After the alternating sign normalization, the limiting relative operator has symbol

\[
j(t)=\frac12-\frac12\cos t=\sin^2(t/2),
\]

with spectral edge at zero. This makes the decay problem for non-polynomial functions quantitatively testable rather than merely qualitative.

For the square root, the limiting bilateral symbol is

\[
j(t)^{1/2}=|\sin(t/2)|
=\frac{2}{\pi}-\frac{4}{\pi}\sum_{k\ge1}\frac{\cos(kt)}{4k^2-1}.
\]

Hence the corresponding Toeplitz coefficients are exactly

\[
c_0=\frac{2}{\pi},\qquad
c_k=-\frac{2}{\pi(4k^2-1)}\quad(k\ne0),
\]

so the off-diagonal tail is algebraic, `c_k\sim-1/(2\pi k^2)`, rather than exponential. This is the expected `s=1/2` discrete-fractional-Laplacian decay: Ciaurri--Roncal--Stinga--Torrea--Varona, *Nonlocal discrete diffusion equations and the fractional discrete Laplacian, regularity and applications*, Advances in Mathematics 330 (2018), 688--738, DOI `10.1016/j.aim.2018.03.023`, gives the classical discrete fractional kernel with `|k|^{-1-2s}` decay. General banded-matrix-function decay theory such as Benzi--Razouk, *Decay bounds and O(n) algorithms for approximating functions of sparse matrices*, ETNA 28 (2007), also makes clear why smooth/analytic functional calculus away from a spectral singularity is a different regime from the present square-root edge.

The algebraic tail is not automatically too weak for PF-243. In the simplest fixed-output-mode calibration, `K_a\asymp n` and a `k^{-2}` transfer coefficient weighted on the input by `K_a^R` gives an `\ell^2` row tail of order `n^{R-2}`. That row is square-summable exactly for `R<3/2`. Thus the limiting square-root model leaves a nonempty toy window

\[
1<R<\frac32,
\]

which just clears PF-243's strict `R>1` threshold. This calculation is only a calibration: PF-243 asks for full separated source-to-bulk energy maps, not one fixed Toeplitz row, and PF-247 explicitly leaves the half-line boundary, variable coefficients, actual seam, `T_a` replacement, and width-dependent coordinate defect unresolved.

More generally, if the actual fixed-axis scalar functional factor has edge expansion `f(\lambda)-f(0)\asymp \lambda^\alpha`, the limiting Fourier tail should have the fractional-Laplacian scale `|k|^{-1-2\alpha}`. The same fixed-row test then leaves a supercritical `R>1` window only when `\alpha>1/4`, with `R<1/2+2\alpha` in that toy geometry.

## Research question

Can the actual fixed-axis functional factor entering the PF-243 separated Robin-Poisson maps be identified near the zero edge of PF-247's relative Jacobi operator and shown to have enough edge regularity that its mode-mixing tail supports some uniform `K_a^R` gain with `R>1`?

In particular, does the square-root-type `k^{-2}` calibration survive the passage from the bilateral constant Jacobi model to PF-247's half-line asymptotically constant parity chains and then through the actual seam-normalized source-to-bulk maps, leaving a genuine window such as `1<R<3/2`? Or does summation over output modes, the Hardy ends, the `T_a` replacement, or the `O(w^2)` hypercycle-coordinate defect consume the half-derivative margin and close that window?

## Why it may matter

PF-247 ends with "quantify functional-calculus decay" as a live route, while the accepted PF-243 clue asks only for one exponent `R>1`. The exact edge calculation turns those two statements into a sharp compatibility test. The critical Jacobi edge is not expected to give exponential locality for a square root, but it may still give just enough algebraic locality to cross the trace threshold.

A positive transfer would identify a concrete exponent range and a specific mechanism for the missing separated smoothing estimate. A negative result would be equally useful: if the correct operator geometry converts the `k^{-2}` edge tail into a bound that cannot reach any `R>1`, then the fixed-axis Jacobi functional-calculus route can be closed without asking for unrealistically strong exponential decay.

## Decisive test

First identify the exact scalar function or finite product of functions of the fixed-axis relative operator that occurs in the seam-normalized far-leg Poisson factor; do not assume that it is literally `J^{1/2}` merely because square roots occur in the normalization. Determine its leading non-smooth term at `\lambda=0`. For a model edge law `\lambda^\alpha`, derive the exact or sharp parity-chain matrix tail and verify the weighted high-to-low bound in the constant half-line Jacobi model, including the boundary correction rather than using only the bilateral Toeplitz kernel.

Then replace the toy fixed-row check by the norm actually needed in PF-243: sum over the full far-leg output energy space and determine whether some `R>1` remains admissible. Only if that succeeds transfer the estimate to PF-247's variable Jacobi coefficients, whose deviations from the constant coefficients tend to zero, and finally test the two explicitly named geometric perturbations: the `T_a` versus `A` spectral replacement and the width-dependent hypercycle/axis coordinate defect. The actual PF-238 seam must remain fixed throughout.

Kill this direction if the correct edge exponent is at most `1/4`, if the half-line/full-output accumulation closes every `R>1` window already in the constant model, or if one of the canonical perturbations produces a non-summable long-range tail. Support it only if a bound for the actual separated source maps survives uniformly on the canonical tail for at least one fixed `R>1`.

## Evidence boundary

The Fourier series for `|sin(t/2)|` and its `k^{-2}` coefficient decay are exact classical calculations for PF-247's constant bilateral limit. The `1<R<3/2` interval is only the square-summability threshold of a fixed-output-mode toy calibration. Neither statement proves PF-243's four separated source-to-bulk estimates, transfers automatically to the half-line variable Jacobi operator, or controls the actual complete-lift seam.

No new theorem about discrete fractional Laplacians, Jacobi functional calculus, Robin maps, Schatten classes, zeta zeros, or RH is claimed. The clue isolates a falsifiable exponent-budget question suggested by PF-247 and remains proposed until the Prime Flute Research Watch reconstructs it in the exact corridor geometry.
