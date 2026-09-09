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
  - research/prime_flute/findings/PF-250-half-line-fractional-edge-powers-retain-supercritical-separated-window.md
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

The original bilateral fixed-output calibration gave only `R<3/2` for the square root and, more generally, `R<1/2+2\sigma` for a toy edge law `\lambda^\sigma`. PF-248--PF-250 show that this is too pessimistic for the **spectral Dirichlet half-line** operator actually relevant to each parity chain. The image term cancels the leading bilateral contribution in every fixed row. PF-250 proves for every `0<\sigma<1` that

\[
\langle e_m,J_0^\sigma e_n\rangle
\asymp_m n^{-2-2\sigma}
\]

with a nonzero leading coefficient, and after any fixed positive output separation the sharp full-output weighted threshold is

\[
\boxed{R<\frac32+2\sigma.}
\]

Thus the square-root case leaves `R<5/2` and even a quarter-root edge law leaves `R<2`. A positive fractional edge exponent is therefore not, by itself, a free half-line obstruction to PF-243's strict `R>1` requirement.

## Research question

Can the actual fixed-axis functional factor entering the PF-243 separated Robin-Poisson maps be identified near the zero edge of PF-247's relative Jacobi operator and shown to have enough edge regularity that its mode-mixing tail supports some uniform `K_a^R` gain with `R>1`?

In particular, does the half-line image cancellation survive the passage from the constant Dirichlet Jacobi model to PF-247's asymptotically constant parity chains and then through the actual seam-normalized source-to-bulk maps? Or do the first-moment-critical coefficient tail, the Hardy ends, the `T_a` replacement, or the `O(w^2)` hypercycle-coordinate defect close every supercritical window?

## Why it may matter

PF-247 ends with "quantify functional-calculus decay" as a live route, while the accepted PF-243 clue asks only for one exponent `R>1`. PF-248--PF-250 now give a sharp free half-line exponent budget rather than a bilateral analogy. The critical edge is not expected to give exponential locality, but the boundary cancellation makes algebraic locality materially stronger than the full-line kernel suggests.

A positive transfer would identify a concrete exponent range and a specific mechanism for the missing separated smoothing estimate. A negative result would be equally useful: if the correct variable-chain/operator geometry destroys the image cancellation strongly enough that no `R>1` survives, then the fixed-axis Jacobi functional-calculus route can be closed before spending effort on the later geometric perturbations.

## Decisive test

First identify the exact scalar function, operator mean, or finite product of functions of the fixed-axis relative operator that actually occurs in the seam-normalized far-leg Poisson factor; do not assume that it is literally `J^{1/2}` merely because square roots occur in the normalization. Determine its leading non-smooth edge behavior at `\lambda=0`.

For a model spectral edge law `\lambda^\sigma`, use the **half-line spectral** kernel rather than a bilateral Toeplitz row. PF-250 gives the free positive-separation threshold `R<3/2+2\sigma` for every `0<\sigma<1`. Then transfer the estimate to PF-247's variable Jacobi coefficients and test whether any fixed `R>1` survives. Only if that succeeds should the route spend margin on the `T_a` versus `A` replacement and the width-dependent hypercycle/axis coordinate defect. The actual PF-238 seam must remain fixed throughout.

Kill this direction if the correctly identified actual factor has no nonlocal half-line smoothing mechanism capable of reaching `R>1`, if PF-247's specific first-moment-critical `O(j^{-2})` coefficient tail destroys every `R>1` weighted estimate, or if one of the later canonical perturbations produces a non-summable long-range tail. **Do not kill it merely because a fractional edge exponent is at most `1/4`**: PF-250 shows that the earlier bilateral threshold behind that criterion does not survive the Dirichlet half-line correction.

## Evidence boundary

The full-line fractional-discrete kernel scale is classical. Das--de la Fuente-Fernandez (2026) records the exact gamma-ratio kernel for spectral fractional powers of the discrete Dirichlet half-line Laplacian, and PF-250 derives the sharp positive-separation weighted threshold needed here. PF-248 and PF-249 are the `sigma=1/2` specialization.

None of PF-248--PF-250 proves PF-243's four separated source-to-bulk estimates, transfers automatically to the variable PF-247 Jacobi operator, identifies the actual complete-lift Robin factor, or controls the `T_a`/hypercycle perturbations. No new theorem about zeta zeros or RH is claimed. This remains an accepted research clue rather than mathematical evidence; acceptance authorizes continued investigation only.

## Research disposition

Accepted for continued investigation. PF-248 performs the first missing half-line test and materially changes the toy exponent budget: the Dirichlet image term cancels the bilateral `n^{-2}` contribution in each fixed output row of the constant half-line square root, giving `n^{-3}` decay and the wider fixed-row threshold `R<5/2`.

PF-248 also shows why this does not resolve the clue. The actual PF-247 parity coefficients differ from the constant chain by `O(j^{-2})`; this is trace class but has divergent first weighted moment, so standard first-moment Jost transfer is unavailable at the zero edge.

PF-249 completes the next **constant square-root model** test. If the free square-root conversion is followed by the exponential output damping supplied by any fixed positive separation, then the full-output operator `E_dJ_0^{1/2}N^R` is Hilbert--Schmidt exactly for `R<5/2` and unbounded for `R>=5/2`. Thus summing the whole separated output does not consume the half-line margin.

PF-250 removes the remaining artifact of the original bilateral calibration. For the spectral Dirichlet half-line power `J_0^\sigma`, `0<\sigma<1`, the image cancellation gives fixed-row decay `n^{-2-2\sigma}` and the sharp separated full-output threshold `R<3/2+2\sigma`. In particular, a quarter-root factor would still leave `1<R<2`; `\sigma<=1/4` is no longer a valid free-model kill criterion.

The precise surviving question is therefore structural rather than a free exponent-budget question: identify the actual normalized Robin factor and determine whether the specific first-moment-critical `O(j^{-2})` PF-247 chain preserves **any** separated weighted estimate with `R>1`. Only after that fixed-axis transfer succeeds should the route spend margin on `T_a` and the hypercycle-coordinate perturbation.