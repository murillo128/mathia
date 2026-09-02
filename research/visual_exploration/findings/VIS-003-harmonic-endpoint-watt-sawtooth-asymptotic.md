# VIS-003 — the centered harmonic endpoint kernel has Watt's sawtooth as its leading boundary model

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT`.

## Claim

Let
\[
\kappa(y)
=
y\left(H_{\lfloor y\rfloor}-\log y-\gamma\right),
\qquad y\ge1,
\]
be the centered harmonic kernel isolated in `MC-021`, and write
\[
y=q+r,\qquad q=\lfloor y\rfloor,\qquad r=\{y\}\in[0,1).
\]
Then, uniformly in \(r\),
\[
\boxed{
\kappa(y)
=
\frac12-r-\frac{B_2(r)}{2y}+O(y^{-2})
}
\qquad (y\to\infty),
\]
where
\[
B_2(r)=r^2-r+\frac16.
\]

The leading term
\[
W(y)=\frac12-\{y\}
\]
is exactly Nigel Watt's Mertens kernel after the scaling \(x=m/N,\ z=n/N\):
\[
K(x,z)
=
\frac12+\left\lfloor\frac1{xz}\right\rfloor-\frac1{xz}
=
W\!\left(\frac1{xz}\right).
\]
Consequently, for \(1\le m,n\le N\) in the regime \(mn/N^2\to0\),
\[
\boxed{
\kappa\!\left(\frac{N^2}{mn}\right)
=
K\!\left(\frac mN,\frac nN\right)
-
\frac{mn}{2N^2}
B_2\!\left(\left\{\frac{N^2}{mn}\right\}\right)
+
O\!\left(\frac{m^2n^2}{N^4}\right).
}
\]

Thus the oscillatory bulk of the `MC-021` endpoint kernel is not a wholly new kernel geometry: its leading boundary model is the classical Watt sawtooth, followed by an explicit periodic Bernoulli correction. This does **not** imply that the corresponding Möbius bilinear form is already controlled at the \(O_\varepsilon(N^{1+\varepsilon})\) scale required by `MC-021`.

## Derivation

Use the classical Euler–Maclaurin expansion
\[
H_q
=
\log q+\gamma+\frac1{2q}-\frac1{12q^2}+O(q^{-4}).
\]
Since \(q=y-r\) with \(0\le r<1\), expand uniformly in the bounded parameter \(r\):
\[
\log q-\log y
=
\log\!\left(1-\frac r y\right)
=
-\frac r y-\frac{r^2}{2y^2}+O(y^{-3}),
\]
\[
\frac1{2q}
=
\frac1{2y}+\frac r{2y^2}+O(y^{-3}),
\]
and
\[
-\frac1{12q^2}
=
-\frac1{12y^2}+O(y^{-3}).
\]
Adding gives
\[
H_q-\log y-\gamma
=
\frac{\frac12-r}{y}
+
\frac{-\frac12r^2+\frac12r-\frac1{12}}{y^2}
+
O(y^{-3}).
\]
Because
\[
-\frac12r^2+\frac12r-\frac1{12}
=
-\frac12B_2(r),
\]
multiplication by \(y\) yields the claimed expansion.

The leading term can also be written
\[
\frac12-r
=
\frac12+\lfloor y\rfloor-y.
\]
With \(y=1/(xz)\), this is precisely Watt's kernel \(K(x,z)\).

## Visual diagnostic

The retained visualization
[[research/visual_exploration/visualizations/huxley-watt-harmonic-sawtooth-boundary-layer]]
plots
\[
\left|
\kappa\!\left(\frac{N^2}{mn}\right)
-
K\!\left(\frac mN,\frac nN\right)
\right|
\]
for `N=600`. It shows the expected product-coordinate boundary layer: the difference fades toward \(mn/N^2=0\) and becomes organized into hyperbolic bands near the corner \(mn\asymp N^2\), where \(y\) is small and the asymptotic expansion is not expected to be sharp.

The image is illustrative only. The mathematical content of this finding is the uniform asymptotic expansion above.

## Prior art and novelty assessment

Nigel Watt studies
\[
K(x,z)=\frac12+\left\lfloor\frac1{xz}\right\rfloor-\frac1{xz}
\]
as a symmetric kernel whose Möbius quadratic form occurs in a Mertens identity; see Nigel Watt, *On eigenvalues of the kernel \(1/2+\lfloor1/(xy)\rfloor-1/(xy)\)*, Journal de théorie des nombres de Bordeaux 31 (2019), 653–662, DOI `10.5802/jtnb.1099`, and the related arXiv work cited there. `MC-021` already records this as adjacent prior art.

The harmonic-number expansion and its Bernoulli corrections are classical Euler–Maclaurin theory; see NIST DLMF §2.10(i) and Chapter 24 for Bernoulli polynomials.

No novelty is claimed for Watt's kernel, Euler–Maclaurin, Bernoulli polynomials, or the asymptotic manipulation itself. The research contribution is the explicit identification of the `MC-021` centered harmonic kernel with Watt's sawtooth as its leading product-coordinate model, which narrows where genuinely new cancellation could reside.

## Boundary conditions and failure modes

The expansion is asymptotic for \(y\to\infty\). On the discrete square this means \(mn/N^2\to0\); it gives no small-error statement uniformly over the full corner \(mn\asymp N^2\), where \(y=O(1)\).

More importantly, a pointwise kernel expansion is not a quadratic-form estimate. If
\[
B(N)=\sum_{m,n\le N}\mu(m)\mu(n)\kappa\!\left(\frac{N^2}{mn}\right),
\]
then replacing \(\kappa\) by \(K\) produces a correction whose absolute sum can still be of order \(N^2\). The factor \(mn/N^2\) in the first correction does not by itself supply the full factor of cancellation needed for the `MC-021` target \(B(N)=O_\varepsilon(N^{1+\varepsilon})\).

Likewise, Watt's spectral results for the continuum kernel do not automatically transfer to the exact finite Möbius matrix with the strength needed here. Any such transfer requires its own discretization, boundary, and sign-cancellation audit.

## Audit criterion

For \(y=q+r\) with \(0\le r<1\), define
\[
E(y)
=
\kappa(y)
-
\left(\frac12-r\right)
+
\frac{B_2(r)}{2y}.
\]
The claim is equivalent to
\[
E(y)=O(y^{-2})
\]
uniformly in the fractional part \(r\). It can be audited directly from the Euler–Maclaurin remainder together with the Taylor expansions in \(r/y\).

A failure of uniform \(O(y^{-2})\), or a sign error in the Bernoulli correction, would invalidate the stated refinement while leaving only the coarser leading relation \(\kappa(y)=1/2-\{y\}+O(1/y)\).

## Consequence for the research line

`MC-021` correctly identifies a bounded product kernel after centering the \(g(n)=1/n\) Huxley–Watt endpoint. `VIS-003` shows that its dominant fine-scale oscillation is already the Watt sawtooth kernel rather than an independent new bulk pattern.

The most informative next split is
\[
\text{known Watt sawtooth carrier}
+
\text{periodic Bernoulli correction}
+
\text{non-asymptotic corner}.
\]
If the `MC-021` square-scale closure target is genuinely easier than the unweighted Watt problem, that advantage must be visible in the signed correction/boundary contribution or in a cancellation mechanism coupling it to the centered coefficients \(H(N)\) and \(1+J(N)\), not merely in the existence of a visually different harmonic formula.
