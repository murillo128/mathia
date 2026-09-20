# PL-396 — Smooth continuation reopens a fixed-gap off-diagonal Riemann–Siegel boundary layer

**Evidence/status:** `CLASSICAL-INCOMPLETE-GAMMA+EXACT-DERIVED + REPRESENTATION-REFINEMENT + ROUTE-RESTRICTION`.

**Parent finding:** `PL-395`.

## Claim

`PL-395` proved an exact statement about the **sharp main sum** in the balanced Riemann–Siegel representation: for an off-diagonal pair `q>r`, the nominal cross-channel saddle

\[
t_*(q,r)=2\pi qr+O((qr)^{-1})
\]

occurs before the pair enters the sharp support at `t=2 pi q^2`. That support exclusion is real for that representation, but it is **not an invariant statement about the analytically continued zeta function**.

Paris–Cang give an exact, absolutely convergent critical-line representation in which each Dirichlet mode is weighted by a normalized incomplete gamma function

\[
Q_n(t):=Q\!\left(\frac{s}{2},\pi i n^2\right),
\qquad s=\frac12+it,
\]

rather than by a hard indicator `1_{n<=floor sqrt(t/(2 pi))}`. The uniform transition asymptotics of `Q` show that, at the nominal off-diagonal saddle `t=2 pi qr`, **fixed-gap pairs `q=r+d` retain an order-one transition weight**. More precisely, for fixed integer `d` and `r -> infinity`,

\[
Q_q(2\pi qr)
=
\frac12\operatorname{erfc}\!\left(d\sqrt{\frac{\pi i}{2}}\right)
+O(r^{-1}),
\tag{1}
\]

and

\[
Q_r(2\pi qr)
=
\frac12\operatorname{erfc}\!\left(-d\sqrt{\frac{\pi i}{2}}\right)
+O(r^{-1}).
\tag{2}
\]

Thus the larger mode is no longer absent when the Dirichlet phase reaches its saddle. The sharp diagonal collapse of `PL-395` must therefore be interpreted as a property of the hard-cutoff chart, not as a representation-independent elimination of the off-diagonal transition layer.

At the same time, this does **not** restore the broad stationary shell of `PL-394`. If `q/r -> c>1`, the incomplete-gamma transition parameter is separated from zero and the larger-mode weight tends to zero. The robust surviving regime is a shrinking multiplicative neighborhood of the diagonal. For fixed `d=q-r`,

\[
\log\frac qr\sim\frac d r\asymp t^{-1/2},
\]

so in prime-exponent coordinates the transition is localized by

\[
\left|\left\langle v(q)-v(r),(\log p)_p\right\rangle\right|
=O(t^{-1/2}).
\]

This is a **log-energy boundary layer**, not a new metric adjacency of the exponent lattice.

## 1. Exact continuation-faithful representation

Paris and Cang proved an absolutely convergent representation valid for all finite `s != 1`; on the critical line Paris restates it as

\[
Z(t)
=
2\Re\,e^{i\vartheta(t)}
\left\{
\sum_{n=1}^{\infty}
 n^{-s}Q\!\left(\frac{s}{2},\pi i n^2\right)
-
\frac{\pi^{s/2}e^{\pi i s/4}}
{s\Gamma(s/2)}
\right\}.
\tag{3}
\]

The series in (3) converges absolutely. Hence this is not a formal transport of the Dirichlet series from `Re(s)>1`; the analytic continuation is built into the incomplete-gamma weights and the explicit archimedean correction.

For the normalized incomplete gamma function, the standard uniform expansion is

\[
Q(a,z)
=
\frac12\operatorname{erfc}\!\left(\eta\sqrt{a/2}\right)
+
\frac{e^{-a\eta^2/2}}{\sqrt{2\pi a}}
\{c_0(\eta)+O(a^{-1})\},
\tag{4}
\]

uniform through the transition, where

\[
\frac12\eta^2=\lambda-1-\log\lambda,
\qquad
\lambda=\frac za,
\qquad
\eta\sim\lambda-1
\quad(\lambda\to1).
\tag{5}
\]

For (3),

\[
a=\frac s2,
\qquad
\lambda_n=\frac{2\pi i n^2}{s}.
\tag{6}
\]

The transition `lambda_n=1` is precisely the smoothed version of the Riemann–Siegel conductor `n approx sqrt(t/(2 pi))`.

## 2. Fixed-gap pairs survive at their nominal saddle

Take

\[
q=r+d,
\qquad d\in\mathbb Z_{>0}\text{ fixed},
\qquad
T=2\pi qr,
\qquad
s=\frac12+iT.
\]

At this height the cross-channel Dirichlet phase from `PL-394` has its leading stationary center. From (6),

\[
\lambda_q
=
\frac{2\pi i q^2}{s}
=
\frac qr+O(r^{-2}),
\qquad
\lambda_r
=
\frac rq+O(r^{-2}),
\]

where the displayed errors include the vanishing imaginary correction from the `1/2` in `s`. Therefore

\[
\eta_q=\frac d r+O(r^{-2}),
\qquad
\eta_r=-\frac d r+O(r^{-2}).
\]

Also

\[
\frac12\sqrt{s}
=
\frac r2\sqrt{2\pi i}+O(1),
\]

because `T=2 pi r(r+d)`. Consequently,

\[
\frac12\eta_q\sqrt{s}
=
d\sqrt{\frac{\pi i}{2}}+O(r^{-1}),
\qquad
\frac12\eta_r\sqrt{s}
=
-d\sqrt{\frac{\pi i}{2}}+O(r^{-1}).
\]

Substitution in (4) gives (1)--(2). The correction in (4) is `O(r^{-1})` because `|a|^(1/2) asymp r` and the uniform coefficient is regular at the transition.

The important point is not the particular complementary-error-function constant. It is the scaling: **for every fixed additive gap, the larger Dirichlet mode has a finite transition coefficient at the height where the pair phase would be stationary**. In the sharp Riemann–Siegel main sum the same mode is exactly absent there, because

\[
2\pi qr<2\pi q^2.
\]

Therefore “off diagonal implies no saddle because the term has not switched on” cannot be promoted from the hard main sum to a representation-independent statement about `Z(t)`.

## 3. The correct local problem is a uniform saddle–transition problem

There is a second scale match. For fixed `q`, the incomplete-gamma weight changes by order one when `t` moves by

\[
\Delta t=O(q)
\]

around `2 pi q^2`: differentiating `lambda_q approx 2 pi q^2/t` shows that an `O(q)` displacement changes the error-function argument in (4) by `O(1)`.

For a fixed pair near its nominal saddle,

\[
\Phi''_{q,r}(t_*)=\frac1{t_*}+O(t_*^{-3})\asymp r^{-2}.
\]

Hence the quadratic stationary-phase scale is likewise

\[
|t-t_*|=O(r).
\]

For fixed `d`, the gap between the sharp activation time and the nominal saddle is

\[
2\pi q^2-2\pi qr
=2\pi qd
=O(r).
\]

All three scales therefore coincide:

\[
\boxed{
\text{sharp activation offset}
\asymp
\text{incomplete-gamma transition width}
\asymp
\text{stationary-phase width}.
}
\tag{7}
\]

This means the amplitude cannot be frozen while stationary phase is applied, and the hard endpoint cannot be treated as an independent singular event. The near-diagonal channel is a **coalescing saddle/transition layer** and requires a uniform treatment of phase and continuation weight together.

## 4. Relation to the prime-exponent geometry

Write `E(alpha)=<alpha,(log p)_p>`. At `t=2 pi qr`, the conductor is

\[
E_c(t)=\frac12\log\frac{t}{2\pi}
=\frac12(\log q+\log r).
\]

The two lattice points lie symmetrically in scalar log-energy:

\[
E(v(q))-E_c
=
\frac12\log\frac qr,
\qquad
E(v(r))-E_c
=-\frac12\log\frac qr.
\]

For `q=r+d` with fixed `d`, these offsets are `O(t^{-1/2})`. Thus the continuation-faithful smoothing selects a thin slab around the conductor hyperplane in the **same scalar projection** `E(alpha)` already identified throughout this line.

This is an important matched-control warning. Equations (1)--(7) use the spectrum `log n` and the archimedean incomplete-gamma transition, but no genuinely multidimensional feature of the factorization vector `v(n)`. Replacing the prime coordinates by abstract labels carrying the same energies would preserve the local calculation. The result therefore refines the representation geometry; it is not yet prime-specific arithmetic rigidity.

## 5. Prior-art and novelty audit

No theorem-level novelty in the Riemann–Siegel or incomplete-gamma theory is claimed.

Paris–Cang (1997) prove the exact absolutely convergent incomplete-gamma representation and derive its complementary-error-function smoothing. Paris (2022) restates the construction and the uniform asymptotics explicitly, emphasizing that the original Dirichlet series is smoothed across the Riemann–Siegel transition. Berry–Keating (1992) independently developed a smooth error-function representation of `Z(t)`, and Borwein–Bradley–Crandall (2000) explicitly contrast such smooth representations with the discontinuous Riemann–Siegel cutoff. Berry–Keating (1999) also stress that the sharp truncated main sum is discontinuous whereas the exact `Z(t)` is analytic and its correction terms remove those discontinuities.

The elementary fixed-gap limit (1)--(2) is a line-specific consequence of those classical formulas evaluated at the pair saddle isolated in `PL-394`--`PL-395`; it is **not claimed as a new analytic-number-theory theorem**. A targeted novelty search found the classical smoothing literature and stationary-phase literature, but no basis for treating the resulting fixed-gap coefficient as an RH mechanism.

### Sources

1. R. B. Paris and S. Cang, “An asymptotic representation for `zeta(1/2+it)`,” *Methods and Applications of Analysis* **4**(4) (1997), 449--470. Full text: https://intlpress.com/site/pub/files/_fulltext/journals/maa/1997/0004/0004/MAA-1997-0004-0004-a006.pdf.
2. R. B. Paris, “An asymptotic approximation for the Riemann zeta function revisited,” arXiv:2203.07863v2 (2022), especially equations (1.1), (2.1)--(2.6), and Theorem 1. https://arxiv.org/abs/2203.07863.
3. NIST Digital Library of Mathematical Functions, §25.10(ii), Riemann–Siegel formula, and §8.22(ii), incomplete-gamma applications to the Riemann zeta function: https://dlmf.nist.gov/25.10 and https://dlmf.nist.gov/8.22.
4. M. V. Berry and J. P. Keating, “A new asymptotic representation for `zeta(1/2+it)` and quantum spectral determinants,” *Proceedings of the Royal Society A* **437** (1992), 151--173. DOI: https://doi.org/10.1098/rspa.1992.0053.
5. J. M. Borwein, D. M. Bradley, R. E. Crandall, “Computational strategies for the Riemann zeta function,” *Journal of Computational and Applied Mathematics* **121** (2000), 247--296. DOI: https://doi.org/10.1016/S0377-0427(00)00336-8.
6. M. V. Berry and J. P. Keating, “The Riemann Zeros and Eigenvalue Asymptotics,” *SIAM Review* **41**(2) (1999), 236--266. DOI: https://doi.org/10.1137/S0036144598347497.

## 6. Adversarial boundaries and falsification tests

1. **This does not prove a nonzero completed off-diagonal contribution.** The error-function weights are complex and vary on the same `O(r)` scale as the saddle. Their phases can shift or cancel a naive stationary contribution, and the explicit archimedean term in (3) must be retained. The result only proves that the sharp-support exclusion itself is not invariant.

2. **This does not restore the broad shell.** Ratio-separated pairs remain asymptotically suppressed by the transition weight. What survives at order-one transition strength is the shrinking multiplicative neighborhood `log(q/r)=O(t^{-1/2})`, including fixed additive gaps.

3. **The exact `Z(t)` has no cutoff jump.** DLMF's classical Riemann–Siegel remainder has the same `t^{-1/4}` scale as the newly activated last main-sum term and cancels the artificial hard discontinuity when the full formula is assembled. Any mechanism depending on a literal jump at `t=2 pi n^2` is therefore representation-dependent.

4. **The local layer is not prime-specific.** It is controlled by `log n`, the conductor and the archimedean smoothing kernel. A claimed prime-lattice mechanism must add a feature that fails for a matched non-arithmetic energy system, rather than relabeling this scalar transition in exponent coordinates.

5. **Decisive falsification test.** The route restriction would fail if one could show that a completed, smooth, representation-independent observable annihilates every fixed-gap off-diagonal channel at the uniform transition scale before any arithmetic input is used. Conversely, observing an off-diagonal term in one chosen smooth decomposition is not sufficient: a durable positive mechanism must survive changes among exact continuation-faithful representations or be tied to an invariant completed quantity.

## Research consequence

`PL-395` remains correct for the canonical **sharp Riemann–Siegel main sum**, but its diagonal stationary collapse cannot be used as if it were an intrinsic property of completed zeta. The next mathematically honest object is the uniform near-diagonal saddle–transition kernel in which the Dirichlet phase, the incomplete-gamma/error-function continuation weight, and the archimedean correction are treated together.

For the prime-lattice program this narrows the target further. A useful mechanism must extract arithmetic information from that completed transition layer that is not already determined by the scalar energy `log n`; otherwise the construction remains a classical continuation effect with the exponent lattice serving only as coordinates.