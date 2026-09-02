# Huxley–Watt harmonic endpoint versus the Watt sawtooth kernel

![Absolute difference between the centered harmonic endpoint kernel and Watt's sawtooth kernel](huxley-watt-harmonic-sawtooth-boundary-layer.png)

## Question

`MC-021` isolates the bounded endpoint kernel
\[
\kappa(y)=y\left(H_{\lfloor y\rfloor}-\log y-\gamma\right),
\qquad y\ge 1,
\]
inside its Möbius bilinear form. Nigel Watt's earlier Mertens-kernel work studies
\[
K(x,z)=\frac12+\left\lfloor\frac1{xz}\right\rfloor-\frac1{xz}.
\]
The visual question is whether the new centered harmonic kernel has genuinely different bulk geometry, or whether it approaches Watt's sawtooth away from the corner \(xz\approx1\).

## Construction

Set \(x=m/N\), \(z=n/N\), and
\[
y=\frac{N^2}{mn}=\frac1{xz}.
\]
Then Watt's kernel is exactly
\[
K(x,z)=\frac12-\{y\}.
\]
The retained image uses `N=600` and plots the pointwise absolute residual
\[
\left|\kappa\!\left(\frac{N^2}{mn}\right)-K\!\left(\frac mN,\frac nN\right)\right|
\]
over all \(1\le m,n\le N\). No Möbius signs are included: the purpose is to isolate the geometry of the two kernels before asking about signed quadratic-form cancellation.

The accompanying exact analysis in `VIS-003` writes \(y=q+r\), \(r=\{y\}\), and derives uniformly as \(y\to\infty\)
\[
\kappa(y)
=
\frac12-r-\frac{B_2(r)}{2y}+O(y^{-2}),
\qquad
B_2(r)=r^2-r+\frac16.
\]

## Observation

The image shows a broad low-residual region toward the coordinate axes, where \(mn/N^2\) is small, and increasingly visible hyperbolic bands toward the upper-right corner. The dominant sawtooth discontinuity pattern is therefore shared with Watt's kernel; the difference is organized primarily by the product coordinate \(xz=mn/N^2\) and becomes largest where \(y\) is no longer asymptotically large.

This suggests that the centered harmonic endpoint should not be treated visually as an unrelated two-dimensional bulk kernel. Its first new layer is a periodic Bernoulli correction to a known Mertens sawtooth carrier, with a non-asymptotic boundary region near \(mn\asymp N^2\).

## Robustness

The leading identification is analytic and independent of the rendering resolution, colormap, or the particular choice `N=600`: it follows from the harmonic-number/Euler–Maclaurin expansion with the fractional part \(r=\{y\}\) kept explicit. Changing `N` only resamples the same product-coordinate relation.

The picture does not show that the associated Möbius quadratic forms are close at the scale needed by `MC-021`. Pointwise smallness in the bulk can accumulate over \(N^2\) pairs, and the corner \(y=O(1)\) is outside the asymptotic regime. Those are mathematical, not rendering, limitations.

## Research consequence

The precise asymptotic identification is persisted as [[research/visual_exploration/findings/VIS-003-harmonic-endpoint-watt-sawtooth-asymptotic]].

It also motivates [[research/mobius_cancellation/clues/CLUE-harmonic-endpoint-watt-boundary-correction]]: split the `MC-021` bilinear form into Watt's already-studied sawtooth carrier plus the Bernoulli/boundary correction, then determine whether the correction is genuinely easier, equally hard, or the actual location of the missing cancellation. The visualization itself is supporting context, not evidence for a quadratic-form bound.
