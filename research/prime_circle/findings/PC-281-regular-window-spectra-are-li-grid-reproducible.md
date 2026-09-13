# PC-281 — regular finite-section spectra are Li-grid reproducible

**Status:** `DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the regular-profile part of the truncated positive-spectral escape left open by PC-280.

PC-280 identifies the surviving truncated anchored operator as

\[
M_{p,r;B}^{f}(h,k)=f(ph+rk),
\qquad h,k\in H_B:=\{-B,\ldots,B\},
\]

with all source dependence carried by the placement of two multiplicatively dilated finite-section windows inside one source-independent cyclic convolution operator. What remained open was whether the **full singular spectrum** of that finite section can retain a prime-specific order-one law even when scalar near-resonance observables have already been matched by the Li-weighted denominator-`q` control of PC-277.

For every profile obtained by sampling a uniformly regular function on the circle, the answer is negative throughout the same classical PNT transport regime. Let `q` be an odd prime, `N:=2B+1<=q`, and let

\[
F_q:\mathbb T\to\mathbb C,
\qquad
\|F_q\|_\infty\le A_q,
\qquad
\operatorname{Lip}(F_q)\le L_q,
\tag{1}
\]

for the geodesic metric on `T=R/Z`. Put `f_q(t)=F_q(t/q)` on `Z/qZ`, and for arbitrary sources `x,y in T` define

\[
M_{x,y;B}^{F_q}(h,k):=F_q(hx+ky),
\qquad h,k\in H_B.
\tag{2}
\]

At `x=p/q,y=r/q`, (2) is exactly the PC-280 matrix `M_{p,r;B}^{f_q}`. Write

\[
\Sigma_{q,B}^{F_q}(x,y)
:=
\bigl(\sigma_1,\ldots,\sigma_N\bigr)
\left(\frac1N M_{x,y;B}^{F_q}\right),
\tag{3}
\]

with singular values in decreasing order. Then the **entire normalized ordered singular spectrum** obeys the exact source-Lipschitz estimate

\[
\boxed{
\left\|
\Sigma_{q,B}^{F_q}(x,y)-
\Sigma_{q,B}^{F_q}(x',y')
\right\|_\infty
\le
B L_q\bigl(d(x,x')+d(y,y')\bigr).
}
\tag{4}
\]

Combining (4) with the prime-to-Li-grid transport estimate of PC-277 yields a matched-control theorem for the whole spectrum. If `rho^{prime,spec}_{q,B,F_q}` is the spectral law on the distinct prime source pairs used in PC-277 and `rho^{Li,spec}_{q,B,F_q}` is the law obtained from two independent draws from PC-277's denominator-`q` Li-grid control `\widetilde\lambda_q`, then for some absolute `c>0`,

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,spec}_{q,B,F_q},
\rho^{Li,spec}_{q,B,F_q}
\right)
\ll
B L_q
\left(
(\log q)e^{-c\sqrt{\log q}}+
\frac{\log q}{q}
\right)
+
A_q\frac{\log q}{q}.
}
\tag{5}
\]

In particular, if `A_q=O(1)` and

\[
B L_q=\exp\!\bigl(o(\sqrt{\log q})\bigr),
\tag{6}
\]

then the distance in (5) tends to zero. More generally, (5) itself is the exact sufficient condition: bounded amplitude is not needed if the final diagonal-conditioning term also vanishes.

Thus **window truncation does not rescue a regular anchored profile from the classical source transport obstruction**. In the subexponential regime the full normalized singular spectrum, not merely a scalar moment or top singular value, is reproducible by a non-prime denominator-`q` control carrying only the smooth logarithmic-integral source bias.

## 1. Whole-spectrum Lipschitz bound

For `h,k in H_B`, the circle metric gives

\[
\begin{aligned}
&\left|
F_q(hx+ky)-F_q(hx'+ky')
\right|\\
&\qquad\le
L_q\,d(hx+ky,hx'+ky')\\
&\qquad\le
B L_q\bigl(d(x,x')+d(y,y')\bigr).
\end{aligned}
\tag{7}
\]

There are `N^2` matrix entries. Therefore, after the `1/N` normalization in (3),

\[
\left\|
\frac{M_{x,y;B}^{F_q}-M_{x',y';B}^{F_q}}{N}
\right\|_{\mathrm{op}}
\le
\left\|
\frac{M_{x,y;B}^{F_q}-M_{x',y';B}^{F_q}}{N}
\right\|_F
\le
B L_q\bigl(d(x,x')+d(y,y')\bigr).
\tag{8}
\]

The ordered singular values satisfy

\[
\max_j|\sigma_j(A)-\sigma_j(B)|
\le
\|A-B\|_{\mathrm{op}}.
\tag{9}
\]

For completeness, (9) follows directly from the min-max characterization of singular values: replacing `A` by `B+(A-B)` changes every extremal norm by at most `||A-B||_op`; reversing `A,B` gives the opposite inequality. Applying (9) to (8) proves (4).

The same normalization gives a uniform state-space bound,

\[
\boxed{
0\le\sigma_j\!\left(M_{x,y;B}^{F_q}/N\right)\le A_q
\quad\text{for every }j,
}
\tag{10}
\]

because `||M/N||_op<=||M/N||_F<=A_q`. The factor `1/N` is therefore the natural bounded-spectrum normalization for bounded profiles; no source arithmetic is inserted by it.

## 2. Transport of the complete singular spectrum

PC-277 proves for the normalized prime source `\nu_q` and the exact denominator-`q` Li-grid control `\widetilde\lambda_q` that

\[
W_1(\nu_q,\widetilde\lambda_q)
\ll
(\log q)e^{-c\sqrt{\log q}}
+
\frac{\log q}{q}.
\tag{11}
\]

Couple two independent copies of an optimal coupling for (11). Since (4) is Lipschitz for the `ell^1` product source metric,

\[
\begin{aligned}
&W_1^{(\ell^\infty)}\!\left(
(\Sigma_{q,B}^{F_q})_*(\nu_q^{\otimes2}),
(\Sigma_{q,B}^{F_q})_*(\widetilde\lambda_q^{\otimes2})
\right)\\
&\qquad\le
2B L_q\,W_1(\nu_q,\widetilde\lambda_q).
\end{aligned}
\tag{12}
\]

The prime law used by the line is on distinct source pairs. Conditioning `\nu_q^{\otimes2}` off the diagonal changes a bounded spectral law by at most the diagonal mass times its diameter. That mass is `O((log q)/q)`, while (10) bounds the `ell^infty` diameter by `A_q`. Hence

\[
W_1^{(\ell^\infty)}
\left(
\rho^{prime,spec}_{q,B,F_q},
(\Sigma_{q,B}^{F_q})_*(\nu_q^{\otimes2})
\right)
\ll
A_q\frac{\log q}{q}.
\tag{13}
\]

Equations (11)--(13) give (5). Swapping the two sources transposes (2), so the ordered singular spectrum is unchanged; consequently the same statement applies to the canonical unordered distinct-pair convention without an additional asymmetry term.

This is stronger than transporting one spectral statistic. The `ell^infty` metric controls **every ordered singular value simultaneously**, including the spectral edge, gaps formed from corresponding ordered values, and any subsequently applied uniformly Lipschitz functional of the normalized spectrum.

## 3. Intrinsic Prime-Circle profiles covered by the theorem

The theorem is not restricted to artificial smooth test functions. Many natural anchored profiles forced by the circle geometry are regular after any macroscopic smoothing.

Let

\[
d_\circ(t):=|1-e^{2\pi i t}|=2|\sin(\pi t)|.
\tag{14}
\]

This is `O(1)`-Lipschitz on `T`. Therefore every fixed Lipschitz chord profile

\[
F(t)=g(d_\circ(t))
\tag{15}
\]

has `L_q=O(Lip(g))`, and its entire finite-section spectrum is Li-grid reproducible for every bandwidth satisfying `log B=o(sqrt(log q))`.

The logarithmic anchor potential has a genuine singularity at the common vertex, so it is not covered without regularization. But the natural mollification

\[
F_{\varepsilon}(t)
:=
\log\bigl(d_\circ(t)+\varepsilon\bigr)
\tag{16}
\]

satisfies

\[
L_q=O(\varepsilon^{-1}),
\qquad
A_q=O(1+|\log\varepsilon|).
\tag{17}
\]

Hence any sequence with

\[
B/\varepsilon
=
\exp\!\bigl(o(\sqrt{\log q})\bigr)
\tag{18}
\]

lies inside (5); the amplitude term in (5) also vanishes automatically in this regime. Thus merely smoothing `log|1-z|` and then taking the PC-280 singular spectrum does not create a new prime-sensitive mechanism.

Likewise, regularized inverse-chord profiles such as `(d_circ(t)+varepsilon)^{-alpha}` are covered whenever their resulting product `B L_q` satisfies (5). The theorem therefore forces any surviving single-profile spectral candidate to exploit the **actual microscopic singularity/sharp transition**, not just the macroscopic shape of an anchored chord or potential kernel.

## 4. Why this does not follow merely from PC-280

PC-280 is an exact operator classification, not a source-blindness theorem. A proper finite window can have a strongly source-dependent singular spectrum because multiplication by `p` and `r` changes the placement of its two window projections. PC-281 adds a different statement: if the underlying phase profile is regular on the circle, then changing the source points by a small amount changes **all normalized singular values only by `O(B L_q)` times that displacement**.

This makes PC-277's classical prime-to-Li transport applicable at the matrix-spectrum level. The arithmetic finite-section placement can still vary with `(p,r)`, but throughout (5) that variation cannot distinguish the true prime source from the matched rational source at order one. The obstruction is therefore not the cyclic-convolution factorization by itself; it is the combination of that finite-section geometry with source regularity.

The result also explains why the exact-anchor-selector control in PC-280 behaves differently. The profile `1_{0}` is discontinuous at the denominator scale and has no `q`-uniform Lipschitz realization. Its intersection statistic `|pH_B intersect rH_B|` is therefore outside the present transport theorem rather than a counterexample to it.

## 5. Prior-art and novelty audit

The two abstract ingredients are classical. Singular values are 1-Lipschitz with respect to operator-norm perturbations in the coordinatewise bound (9), and PC-280 already places the matrix inside the established finite-section/Fourier-concentration setting. PC-277 already anchors the quantitative PNT transport input. No novelty is claimed for matrix perturbation theory, PNT transport, cyclic convolution, or prolate/partial-Fourier finite sections.

A targeted literature check against singular-value perturbation/Mirsky-type inequalities and partial-Fourier/prolate finite sections found the expected general matrix and concentration theory. It did not reveal an independent result that combines the Prime-Circle phase matrix, a Li-weighted denominator-`q` source control, and a whole-spectrum transport bound of the form (5). Absence of such a result is not used as evidence of novelty.

The project-local delta is the exact synthesis forced by the current frontier: **regular PC-280 finite sections inherit the classical PC-277 source approximation at the level of their entire normalized singular spectrum**. This closes a broad natural subclass of the positive-spectral escape without claiming a new RH criterion. Because the load-bearing external input is already durably sourced by PC-277 and the perturbation step is proved above, no new `SOURCES.md` dependency is required.

## 6. Surviving boundary and falsification tests

Equation (5) deliberately does not cover every profile allowed by PC-280. The following remain outside this no-go:

- exact threshold/selector masks whose transition width is microscopic in `q`;
- the unsmoothed logarithmic singularity at the common vertex;
- profiles whose Lipschitz scale grows fast enough that `B L_q` defeats (5);
- source-dependent profiles `F_{q,p,r}`;
- genuinely cross-level or non-single-phase operators not representable by one profile `F_q(hx+ky)`.

These exclusions are now informative rather than generic. Within the PC-280 family a viable order-one positive-spectral discrepancy must be paid for by **microscopic variation, discontinuity, or some structure not transported through one regular phase profile**. Merely increasing the finite-section size while keeping the anchored profile regular does not suffice in the regime (5).

The claim has direct finite checks. For arbitrary Lipschitz trigonometric profiles and source pairs, one can perturb `(x,y)` and verify (4) against the complete singular-value vector; any coordinate exceeding the right-hand side falsifies the theorem. Sampling the same profile at `(p/q,r/q)` must reproduce the discrete PC-280 matrix exactly. The profile controls in (15)--(18) can be checked directly from their circle Lipschitz constants. Small-prime numerical stress tests satisfy the deterministic bound to machine precision, but the stored result depends only on (7)--(13), not on numerics.

## 7. Consequence for the research line

The positive finite-section frontier is narrower than after PC-280. For a bounded regular anchor profile and every bandwidth with `B L_q=exp(o(sqrt(log q)))`, the complete normalized singular spectrum is asymptotically reproduced by a denominator-`q` rational source carrying only the classical `Li` bias. This excludes a large class of smooth chord, mollified-potential, and regular Fourier-multiplier realizations from supplying a new RH-facing discriminator in that regime.

The unresolved part of this branch is therefore concentrated where the theorem fails for structural reasons: genuinely microscopic/sharp anchor profiles, the intermediate rational-microscopic bandwidth window, or constructions that couple levels/coordinates before they collapse to a single regular phase profile. Any future claim from the finite-section route should be tested first against (5), not merely against uniform non-prime sources.