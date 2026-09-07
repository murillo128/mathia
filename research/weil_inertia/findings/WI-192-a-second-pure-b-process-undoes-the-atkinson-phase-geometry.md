# WI-192 — a second pure B-process undoes the Atkinson phase geometry

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. This finding closes the most immediate phase-only continuation of WI-191. For each fixed shift `h`, the B-process phase that produced the WI-191 Atkinson transform is exactly the Legendre/B-transform of the original logarithmic chirp, and a second pure B-transform returns that logarithmic phase with reciprocal stationary Jacobian and opposite stationary-phase signature. After the product regrouping `n=hk`, the same involution survives at the continuous phase level: the grouped Atkinson phase has derivative `m/h`, and its second B-dual is `A log(1+1/j)`. Thus another B-process cannot create a genuinely new geometric source of cancellation by itself. Any gain after WI-191 has to enter through the arithmetic fiber coefficient `B_n`, the changed discrete lattice created by grouping, an intervening A/differencing step, a Voronoi/functional-equation input that uses coefficient structure, or a different source coupling.

No bound for the shifted-von-Mangoldt covariance is claimed and no simple-critical-zero percentage changes. In particular, this does **not** rule out `A^r B`, `B A^r B`, bilinear decompositions, spectral transforms, or a B-process applied only after arithmetic coefficients have been reorganized in a way that supplies new cancellation. The barrier is specifically against treating a second B-transform of the Atkinson phase as a new phase mechanism.

## 1. Fixed-shift B-duality is exactly involutive

Use the source notation of WI-188--WI-191 and set

\[
A:=\frac{U}{2\pi},
\qquad
f_h(m):=A\log\!\left(1+\frac hm\right),
\qquad h>0.
\tag{1}
\]

Then

\[
f_h'(m)=-\frac{Ah}{m(m+h)},
\qquad
f_h''(m)=\frac{Ah(2m+h)}{m^2(m+h)^2}>0.
\tag{2}
\]

For a positive integer B-frequency `k`, let `m_h(k)` be the stationary point defined by

\[
\frac{Ah}{m_h(k)(m_h(k)+h)}=k,
\tag{3}
\]

so that `f_h'(m_h(k))=-k`. With the standard B-transform convention

\[
f^*(\nu)=f(x_\nu)-\nu x_\nu,
\qquad f'(x_\nu)=\nu,
\tag{4}
\]

the first dual phase at frequency `-k` is

\[
G_h(k):=f_h(m_h(k))+k\,m_h(k)=f_h^*(-k).
\tag{5}
\]

Differentiate (5). The terms containing `m_h'(k)` cancel because `f_h'(m_h(k))=-k`, giving the exact identity

\[
\boxed{G_h'(k)=m_h(k).}
\tag{6}
\]

Differentiating (3), or differentiating `f_h'(m_h(k))=-k`, gives

\[
\boxed{G_h''(k)=m_h'(k)=-\frac1{f_h''(m_h(k))}<0.}
\tag{7}
\]

Now apply the B-transform to `G_h`. Its stationary frequency is an integer `m_0` with `G_h'(k_0)=m_0`, hence `m_h(k_0)=m_0`, and therefore

\[
\boxed{
G_h(k_0)-m_0k_0=f_h(m_0).
}
\tag{8}
\]

So before any product regrouping, the second Legendre phase is literally the original logarithmic chirp. The leading stationary Jacobians cancel as well:

\[
\frac1{\sqrt{f_h''(m_0)}}
\frac1{\sqrt{|G_h''(k_0)|}}
=1.
\tag{9}
\]

The stationary signatures cancel too. The first transform has positive curvature and therefore the usual `+1/8` phase in `e(t)=exp(2 pi i t)` notation; the second has negative curvature and contributes `-1/8`. Thus, at the geometric stationary-phase level, `B^2` returns phase, amplitude, and signature to the source configuration. Endpoint/error terms still have to be controlled in an actual exponential-sum theorem, but they do not turn the second B-transform into a new phase geometry.

This is the specialization of the classical fact that the van der Corput B-transform is an involution. Olivier Robert states this explicitly immediately after his Theorem 4 in **On van der Corput's k-th derivative test for exponential sums**, *Indagationes Mathematicae* 27:2 (2016), 559--589, DOI `10.1016/j.indag.2015.11.009`. No new B-process theorem is claimed here.

## 2. The product-grouped Atkinson phase has the exact reciprocal derivative

WI-191 groups the first B-frequencies by

\[
n:=hk,
\qquad
q:=\frac nA,
\qquad
 y:=\frac hm.
\tag{10}
\]

Stationarity is equivalent to

\[
q=\frac{y^2}{1+y},
\tag{11}
\]

and the product-grouped dual phase is

\[
 g_U(n)
 =A\left[\log(1+y)+\frac{y}{1+y}\right].
\tag{12}
\]

WI-191 identified (12), up to the elementary parity and fixed phase factors, with the classical Atkinson phase. The derivative structure is even more rigid. From

\[
\frac{dq}{dy}=\frac{y(2+y)}{(1+y)^2}
\tag{13}
\]

and

\[
\frac{d}{dy}\left(\log(1+y)+\frac{y}{1+y}\right)
=\frac{2+y}{(1+y)^2},
\tag{14}
\]

one gets

\[
\boxed{g_U'(n)=\frac1y=\frac mh.}
\tag{15}
\]

A second differentiation gives

\[
\boxed{
 g_U''(n)
 =-\frac{(1+y)^2}{A\,y^3(2+y)}<0.
}
\tag{16}
\]

Thus the integer frequencies of a second B-process on the one-dimensional Atkinson phase are not a new hidden variable: they are exactly the reciprocal gap ratios `m/h` of the source saddle geometry.

For an integer second-dual frequency `j>0`, equation (15) forces

\[
y=\frac1j,
\qquad
q=\frac1{j(j+1)},
\qquad
n_j=\frac{A}{j(j+1)}.
\tag{17}
\]

Substituting into (12) yields an exact cancellation of the rational part:

\[
\begin{aligned}
 g_U(n_j)-j n_j
 &=A\left[\log\left(1+\frac1j\right)+\frac1{j+1}\right]
   -\frac{A}{j+1}\\
 &=\boxed{A\log\left(1+\frac1j\right)}.
\end{aligned}
\tag{18}
\]

Equation (18) is precisely the source logarithmic phase (1) at ratio `m/h=j`. Hence the full Atkinson phase of WI-191 is not merely asymptotically self-dual near small `n/U`; its second B-dual is exactly the original logarithmic family.

## 3. The grouped Jacobian records only the lattice rescaling

At the second stationary point `y=1/j`, equation (16) becomes

\[
\boxed{
|g_U''(n_j)|
=\frac{j^2(j+1)^2}{A(2j+1)}.
}
\tag{19}
\]

At the corresponding source ratio `m=jh`, equation (2) gives

\[
\boxed{
 f_h''(jh)
 =\frac{A(2j+1)}{j^2(j+1)^2h^2}.
}
\tag{20}
\]

Therefore

\[
\boxed{
\frac1{\sqrt{f_h''(jh)}}
\frac1{\sqrt{|g_U''(n_j)|}}
=h.
}
\tag{21}
\]

The factor `h` is exactly the coordinate/lattice rescaling introduced by `n=hk`: for a fixed `h`, the first dual variable occupies the sublattice `n in h Z`, not the full integer lattice. Before this regrouping, (9) shows that the two stationary Jacobians multiply to one. After regrouping, the missing lattice density is carried by the arithmetic fiber coefficient

\[
B_n=\sum_{hk=n}C_{h,k}
\tag{22}
\]

from WI-191. Consequently, a second B-process on a schematic full-lattice sum `sum_n B_n e(g_U(n))` can differ from literal inversion only through the coefficient/fiber/lattice information in `B_n`; the phase and smooth stationary Jacobian themselves contain no new saving.

This distinction is load-bearing. The source coefficient contains `Lambda(m)Lambda(m+h)` and is not a smooth amplitude, so neither the first nor second stationary-phase display may be promoted to an exponential-sum estimate by simply evaluating the von-Mangoldt factors at the continuous saddles. Any legitimate implementation must first expose an arithmetic transform or decomposition for which the B-process hypotheses hold. Equation (21) says what survives once that arithmetic step is made legitimate; it does not supply that step.

## 4. At the count-saturating bow the second B-range returns to the source power scale

The scale bookkeeping is consistent with the exact involution. On the source dyadic block `m asy X`, a first stationary integer `k>=1` can occur only once

\[
\frac{Uh}{X^2}\gg1,
\tag{23}
\]

up to the fixed dyadic constants. Thus the active shifts begin at scale `h gg X^2/U`. At the other end, the localizer permits `h lesssim X/H`. Since the second B-frequency is `j=m/h`, the corresponding dual range is, again up to fixed dyadic/localizer constants,

\[
\boxed{
H\ \lesssim\ j\ \lesssim\ \frac{U}{X}.
}
\tag{24}
\]

For the count-saturating source-compatible bow of WI-188, `X=T^(1/2+o(1))` and `U asy T`. Hence

\[
\frac{U}{X}=T^{1/2+o(1)},
\tag{25}
\]

so the upper second-dual scale has exactly the same power exponent as the original prime-side length. The first B-process may compress the geometry into the Atkinson product variable of length `U/H^2`, but a pure second B-process returns to a square-root source-scale variable. Depending on `H`, the number of terms in one representation can be smaller than in the other; what does **not** appear is a new phase scale below both. Any actual advantage must therefore be attributed to the arithmetic organization of the coefficients, not to repeated Legendre dualization.

## 5. Prior-art audit and exact boundary of the negative result

The general involution is classical, not Mathia novelty. A modern explicit source is Olivier Robert, **On van der Corput's k-th derivative test for exponential sums**, *Indagationes Mathematicae* 27:2 (2016), 559--589, DOI `10.1016/j.indag.2015.11.009`: Section 4 defines `f*(nu)=f(x_nu)-nu x_nu` with `f'(x_nu)=nu` and explicitly recalls that the B-transform is an involution. Graham--Kolesnik's classical treatment, already cited in WI-189, is the standard broader source for the B-process.

The Atkinson side is the literature already audited in WI-191: Atkinson's 1949 mean-square formula, Jutila's divisor/short-interval development, and modern explicit formulations such as Simonič--Starichkova. The exact equations (15)--(21) are a specialization of the classical B-involution to the WI-188/WI-191 bow phase, not a claim that Atkinson theory missed an involution.

Two neighboring results were checked for a black-box escape and do not alter the boundary. Ishikawa--Matsumoto, **An explicit formula of Atkinson type for the product of the Riemann zeta-function and a Dirichlet polynomial**, *Central European Journal of Mathematics* 9:1 (2011), 102--126, DOI `10.2478/s11533-010-0085-5`, develops Atkinson-type formulas with Dirichlet-polynomial coefficients, but its coefficient architecture is not the growing-shift `Lambda(m)Lambda(m+h)` covariance of WI-188. More recently, Ze Sen Tang, **Reciprocity for The Short Twisted Second Moment of The Riemann Zeta Function**, arXiv:2608.14852v1 (14 Aug 2026), proves a Gaussian short-interval reciprocity theorem for `H=T^delta`, `delta in (1/2,1)`, with the explicit dominance condition `H^2/max(p,q)>T^(1+epsilon)` and dual support length `T/H`. The count-saturating bow has `H=T^epsilon/log T` with fixed `epsilon<1/2`, so it lies outside Tang's theorem even before accounting for the different shifted-prime coefficient structure. These are neighboring reciprocity technologies, not ready-made estimates for (22).

A targeted search did not locate the bow-specific identities (15)--(24) written in this form. That absence is not evidence of priority. The durable Mathia delta is narrower: once WI-191 has identified the exact Atkinson phase, the classical B-involution can be specialized with no asymptotic expansion and shows that **pure repeated B-dualization is not the missing source-specific coercivity**.

## 6. Research consequence

WI-191 left the live arithmetic target schematically as

\[
\sum_{n\lesssim U/H^2} B_n\,e(g_U(n))
\tag{26}
\]

with `B_n` a shifted-prime deformation of a divisor coefficient. WI-192 removes one tempting but nonproductive interpretation of that target. Applying a second B-process because the Atkinson phase has favorable curvature merely walks back along the same Legendre geometry. To obtain a new estimate one must do something that breaks the involution before or during the next transform.

The viable routes are therefore more specific:

- expose enough structure in `B_n` that a Voronoi/Atkinson-type coefficient transform has arithmetic content rather than only phase content;
- insert an A-process/differencing or bilinear decomposition between B-transforms so the phase being transformed is genuinely changed;
- exploit cancellation across the hyperbolic fibers `hk=n`, where WI-191 located all source-specific information;
- or abandon this source coupling for another invariant that sees off-line defect directly.

The falsification criterion for future phase arguments is now exact. If a proposal uses only `g_U`, its curvature, and another one-dimensional B-transform, with no new statement about `B_n` or the fiber/lattice structure, then equations (15)--(21) reduce it to the original logarithmic chirp and it cannot count as new progress toward defect elimination. This keeps the line aligned with its canonical objective: the remaining gain has to be arithmetic or defect-sensitive, not another presentation of the same classical phase duality.