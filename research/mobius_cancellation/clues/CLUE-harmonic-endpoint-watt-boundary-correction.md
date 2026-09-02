---
id: CLUE-mobius-cancellation-harmonic-endpoint-watt-boundary-correction
type: research-clue
status: resolved
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-021-huxley-watt-harmonic-endpoint-bilinear-kernel.md
  - research/visual_exploration/findings/VIS-003-harmonic-endpoint-watt-sawtooth-asymptotic.md
  - research/visual_exploration/visualizations/huxley-watt-harmonic-sawtooth-boundary-layer.md
---

# Can the harmonic endpoint gain be isolated in the Bernoulli correction to Watt's kernel?

## Observation

`MC-021` isolates the centered harmonic endpoint kernel
\[
\kappa(y)=y(H_{\lfloor y\rfloor}-\log y-\gamma)
\]
as the bounded carrier in its square-scale Möbius bilinear form. `VIS-003` shows that, uniformly as \(y\to\infty\),
\[
\kappa(y)
=
\frac12-\{y\}
-\frac{B_2(\{y\})}{2y}
+O(y^{-2}).
\]
After the scaling \(y=N^2/(mn)\), the leading term \(1/2-\{y\}\) is exactly Nigel Watt's previously studied Mertens kernel
\[
K(m/N,n/N)=\frac12+\left\lfloor\frac{N^2}{mn}\right\rfloor-\frac{N^2}{mn}.
\]

The retained visualization makes the same separation visible: the kernel difference is small through the product-coordinate bulk and is concentrated into hyperbolic correction bands and the non-asymptotic corner \(mn\asymp N^2\).

## Research question

Can the `MC-021` bilinear form be decomposed into Watt's known sawtooth quadratic form plus a periodic Bernoulli/boundary correction in a way that yields a genuinely stronger cancellation estimate for the full harmonic endpoint?

More precisely, after writing
\[
B(N)
=
\sum_{m,n\le N}\mu(m)\mu(n)
K(m/N,n/N)
+
C(N),
\]
does the exact correction \(C(N)\) admit a source-natural estimate at or below \(O_\varepsilon(N^{1+\varepsilon})\), or does the hard Mertens-scale cancellation simply remain in the Watt component or migrate into the corner?

## Why it may matter

This split prevents a false-new-kernel route. The dominant oscillatory geometry of `MC-021` is already adjacent prior art, so the endpoint can beat the unweighted Huxley–Watt barrier only if the harmonic centering changes the **signed quadratic-form information budget**, not merely the appearance of the kernel.

A successful estimate for the correction, combined with an independently useful treatment of the Watt component, would localize exactly what the \(g(n)=1/n\) endpoint buys. A negative result would sharply classicalize the endpoint by showing that its new Bernoulli/boundary layer does not remove the original square-scale cancellation burden.

## Decisive test

Derive an exact finite decomposition rather than relying only on the asymptotic series. Split the square by the product parameter \(y=N^2/(mn)\), with a controllable cutoff separating the large-\(y\) bulk from the \(y=O(1)\) corner. In the bulk, use the Bernoulli expansion with an explicit remainder; in the corner, retain the exact kernel.

Then estimate the Möbius-signed correction \(C(N)\) while preserving its product structure. Compare the resulting bound with the \(O_\varepsilon(N^{1+\varepsilon})\) target from `MC-021`. A useful kill condition is a source-compatible matched control for which the correction is already of order \(N^{2-o(1)}\), or a proof that obtaining the required correction bound implies an RH-equivalent coarse statistic. A positive outcome must also state precisely what additional estimate remains for Watt's sawtooth quadratic form and for the centered coefficients \(H(N)\) and \(1+J(N)\).

## Evidence boundary

`VIS-003` proves only a pointwise large-\(y\) asymptotic identification. It does not prove that the finite Möbius quadratic forms for \(\kappa\) and \(K\) are close, does not transfer Watt's continuum spectral estimates to the discrete matrix at the needed strength, and does not establish any new bound for \(B(N)\), \(H(N)\), \(J(N)\), or the Mertens function. The visualization is motivation only.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/mobius_cancellation/findings/MC-022-harmonic-watt-correction-weighted-coarse-mode.md]]

The exact finite subtraction is stronger than the proposed bulk/corner estimate. `MC-022` shows that the correction quadratic form equals the doubled-scale quantity `D(N^2)=M(N^2)-N^2 H(N^2)` plus explicit lower-scale terms. The critical bound `D(x)=O_epsilon(x^(1/2+epsilon))` is itself equivalent to RH through an exact Mellin transform. Consequently, in a square-scale bootstrap that already controls the lower-scale coefficients at their critical sizes, estimating the correction separately at `O_epsilon(N^(1+epsilon))` simply reproduces the next-scale RH-equivalent coarse obligation.

This kills the interpretation of the Bernoulli/boundary correction as an automatically cheaper independent remainder. It does **not** kill the full harmonic endpoint: a coupled signed cancellation between Watt's component, the correction, and the centered lower-scale coefficients remains a distinct open mechanism.