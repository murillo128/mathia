---
id: CLUE-prime-flute-critical-jacobi-square-root-decay-window
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-248-parity-jacobi-tail-is-trace-class-but-first-moment-critical.md
  - research/prime_flute/findings/PF-249-positive-separation-preserves-free-jacobi-square-root-threshold.md
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

In particular, does the square-root-type calibration survive the passage from the constant half-line Jacobi model to PF-247's asymptotically constant parity chains and then through the actual seam-normalized source-to-bulk maps, leaving a genuine supercritical window? Or do the first-moment-critical coefficient tail, the Hardy ends, the `T_a` replacement, or the `O(w^2)` hypercycle-coordinate defect close it?

## Why it may matter

PF-247 ends with "quantify functional-calculus decay" as a live route, while the accepted PF-243 clue asks only for one exponent `R>1`. The exact edge calculation turns those two statements into a sharp compatibility test. The critical Jacobi edge is not expected to give exponential locality for a square root, but it may still give just enough algebraic locality to cross the trace threshold.

A positive transfer would identify a concrete exponent range and a specific mechanism for the missing separated smoothing estimate. A negative result would be equally useful: if the correct operator geometry converts the edge tail into a bound that cannot reach any `R>1`, then the fixed-axis Jacobi functional-calculus route can be closed without asking for unrealistically strong exponential decay.

## Decisive test

First identify the exact scalar function or finite product of functions of the fixed-axis relative operator that occurs in the seam-normalized far-leg Poisson factor; do not assume that it is literally `J^{1/2}` merely because square roots occur in the normalization. Determine its leading non-smooth term at `\lambda=0`. For a model edge law `\lambda^\alpha`, derive the exact or sharp parity-chain matrix tail and verify the weighted high-to-low bound in the constant half-line Jacobi model, including the boundary correction rather than using only the bilateral Toeplitz kernel.

Then use the norm actually needed in PF-243: sum over the full far-leg output energy space and determine whether some `R>1` remains admissible. Only if that succeeds transfer the estimate to PF-247's variable Jacobi coefficients, whose deviations from the constant coefficients tend to zero, and finally test the two explicitly named geometric perturbations: the `T_a` versus `A` spectral replacement and the width-dependent hypercycle/axis coordinate defect. The actual PF-238 seam must remain fixed throughout.

Kill this direction if the correct edge exponent is at most `1/4`, if the half-line/full-output accumulation closes every `R>1` window already in the constant model, or if one of the canonical perturbations produces a non-summable long-range tail. Support it only if a bound for the actual separated source maps survives uniformly on the canonical tail for at least one fixed `R>1`.

## Evidence boundary

The Fourier series for `|sin(t/2)|` and its `k^{-2}` coefficient decay are exact classical calculations for PF-247's constant bilateral limit. PF-248 and PF-249 sharpen that calibration on the half-line and after positive-separation full-output summation, but neither proves PF-243's four separated source-to-bulk estimates, transfers automatically to the variable PF-247 Jacobi operator, or controls the actual complete-lift seam.

No new theorem about discrete fractional Laplacians, Jacobi functional calculus, Robin maps, Schatten classes, zeta zeros, or RH is claimed. This remains an accepted research clue rather than mathematical evidence; acceptance authorizes continued investigation only.

## Research disposition

Accepted for continued investigation. PF-248 performs the clue's first missing half-line test and materially changes the toy exponent budget: the Dirichlet image term cancels the bilateral `n^{-2}` contribution in each fixed output row of the constant half-line square root, giving `n^{-3}` decay and the wider fixed-row threshold `R<5/2`.

PF-248 also shows why this does not resolve the clue. The actual PF-247 parity coefficients differ from the constant chain by `O(j^{-2})`; this is trace class but has divergent first weighted moment, so standard first-moment Jost transfer is unavailable at the zero edge.

PF-249 completes the next **constant-model** test. If the free square-root conversion is followed by the exponential output damping supplied by any fixed positive separation, then the full-output operator `E_dJ_0^{1/2}N^R` is Hilbert--Schmidt exactly for `R<5/2` and unbounded for `R>=5/2`. Thus summing the whole separated output does not consume the half-line margin: the free proxy still leaves the full interval `1<R<5/2`.

The precise surviving question is now narrower: identify the actual normalized Robin scalar factor and determine whether the specific first-moment-critical `O(j^{-2})` PF-247 chain preserves **any** separated weighted estimate with `R>1`. Only after that fixed-axis transfer succeeds should the route spend margin on `T_a` and the hypercycle-coordinate perturbation.