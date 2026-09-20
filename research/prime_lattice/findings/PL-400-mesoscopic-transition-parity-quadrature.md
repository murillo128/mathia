# PL-400 — Mesoscopic continuation phase puts the prime-pair bulk in quadrature

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTEXT + NEGATIVE/ROUTE-RESTRICTION`.

**Parent findings:** `PL-396`, `PL-397`, `PL-399`, `PL-075`.

## Claim

`PL-399` determined only the magnitude of the growing-gap incomplete-gamma tail. Keeping its complex phase exposes a stronger restriction on the most canonical arithmetic compensation proposed there.

Let

\[
q=r+d,
\qquad d=d(r)\to\infty,
\qquad d=o(r^{1/3}),
\]

and evaluate the continuation-faithful incomplete-gamma coefficients at the same pair saddle

\[
T=2\pi rq,
\qquad s=\frac12+iT,
\qquad Q_n(T)=Q\!\left(\frac{s}{2},\pi i n^2\right).
\]

Write `theta` for the Riemann--Siegel phase and define the normalized same-sign cross-channel coefficient

\[
P_{r,d}
:=
\exp\!\left(i\{2\theta(T)-T\log(rq)\}\right)
Q_q(T)Q_r(T).
\tag{1}
\]

This is the phase-bearing coefficient multiplying the universal radial factor `(rq)^(-1/2)` for the ordered `(r,q)` term in the `C(t)^2` part of `Z(t)^2`, where `Z(t)=2 Re C(t)` in the representation used in `PL-396`.

Then

\[
\boxed{
P_{r,d}
=
\frac{1+o(1)}{\sqrt2\,\pi d}
\exp\!\left(-\frac{i\pi}{2}(d^2+1)\right).
}
\tag{2}
\]

Consequently

\[
\boxed{
\Re P_{r,d}=o(d^{-1})
\quad(d\ \text{even}),
}
\tag{3}
\]

whereas

\[
\boxed{
\Re P_{r,d}
=-\frac{1+o(1)}{\sqrt2\,\pi d}
\quad(d\ \text{odd}).
}
\tag{4}
\]

This parity split is fatal to the leading version of the proposed von-Mangoldt compensation. The shifted correlation `Lambda(r)Lambda(r+d)` can have a bulk prime-pair term only at **even** `d`, precisely where the leading `1/d` transition tail is in quadrature and disappears under the real projection. At odd `d`, where the transition tail has a leading real part, one has unconditionally and uniformly for `1<=d<=X`

\[
\sum_{r\le X}\Lambda(r)\Lambda(r+d)
=O((\log X)^2),
\qquad d\ \text{odd},
\tag{5}
\]

because a nonzero term forces the even member of the pair to be a power of `2`.

Thus the canonical route

\[
\text{mesoscopic continuation tail}
+\Lambda(r)\Lambda(r+d)
\longrightarrow
\text{leading Hardy--Littlewood amplification}
\]

fails in this real same-sign cross-channel: analytic phase and arithmetic parity select opposite gap classes. This is a route restriction, not a statement that all arithmetic couplings, all quadratic channels, or all gap aggregations vanish.

## 1. Phase refinement of the `PL-399` transition variable

Use the notation of `PL-399`

\[
a=\frac{s}{2},
\qquad
\lambda_n=\frac{2\pi i n^2}{s},
\qquad
f(\lambda)=\lambda-1-\log\lambda,
\qquad
y_n^2=a f(\lambda_n).
\tag{6}
\]

Put

\[
\delta=\frac dr,
\qquad
L=\frac qr=1+\delta.
\]

At `T=2 pi rq`, `PL-399` gives

\[
\lambda_q=L+\frac{i}{4\pi r^2}+O(r^{-4}).
\tag{7}
\]

For real `L=1+delta`,

\[
f(L)
=\frac{\delta^2}{2}-\frac{\delta^3}{3}
 +\frac{\delta^4}{4}+O(\delta^5),
\]

hence

\[
(1+\delta)f(1+\delta)
=\frac{\delta^2}{2}
 +\frac{\delta^3}{6}
 -\frac{\delta^4}{12}
 +O(\delta^5).
\tag{8}
\]

Since

\[
a=\frac14+i\pi rq,
\]

(7)--(8), together with `f'(L)=1-L^{-1}=O(delta)`, yield

\[
y_q^2
=
\frac{i\pi d^2}{2}
+rac{i\pi d^3}{6r}
+O\!\left(\frac dr+\frac{d^4}{r^2}\right).
\tag{9}
\]

The stronger mesoscopic condition `d=o(r^(1/3))` is used exactly here: it makes every term after `i pi d^2/2` in (9) tend to zero. Therefore

\[
\boxed{
e^{-y_q^2}
=e^{-i\pi d^2/2}\{1+o(1)\}.
}
\tag{10}
\]

Also, as in `PL-399`,

\[
y_q
=d\sqrt{\frac{\pi i}{2}}\{1+o(1)\},
\qquad
Q_r(T)=1+O(d^{-1}).
\tag{11}
\]

The standard large-complex-argument expansion

\[
\operatorname{erfc}(y)
=
\frac{e^{-y^2}}{\sqrt\pi\,y}
\{1+O(|y|^{-2})\}
\]

and the `O(r^-1)` subordinate incomplete-gamma correction already audited in `PL-399` now give the **complex** refinement

\[
\boxed{
Q_q(T)
=
\frac{1+o(1)}{\sqrt2\,\pi d}
 e^{-i\pi/4}
 e^{-i\pi d^2/2}.
}
\tag{12}
\]

Equation (12) sharpens the magnitude-only statement of `PL-399`. No new special-function theorem is being asserted; it is the retained phase of the same classical `erfc` asymptotic.

## 2. The Hardy phase locks the tail to parity

The Riemann--Siegel theta expansion is

\[
2\theta(T)
=
T\log\frac{T}{2\pi}-T-\frac\pi4+O(T^{-1}).
\tag{13}
\]

At the pair saddle `T=2 pi rq`,

\[
2\theta(T)-T\log(rq)
=-T-\frac\pi4+O(T^{-1}).
\]

Since `rq` is an integer,

\[
e^{-iT}=e^{-2\pi i rq}=1,
\]

and hence

\[
\exp\!\left(i\{2\theta(T)-T\log(rq)\}\right)
=e^{-i\pi/4}\{1+o(1)\}.
\tag{14}
\]

Combining (11), (12), and (14) proves (2):

\[
P_{r,d}
=
\frac{1+o(1)}{\sqrt2\,\pi d}
 e^{-i\pi(d^2+1)/2}.
\]

For integral `d`, only its parity matters. If `d` is even, `d^2=0 mod 4`, so the leading phase is `-i`; if `d` is odd, `d^2=1 mod 4`, so the leading phase is `-1`. Taking the real part gives (3)--(4).

The conclusion is unchanged if one writes the conjugate same-sign channel instead: `-i` becomes `+i` for even gaps, while the leading real part still vanishes. It is not invariant under an arbitrary phase rotation of `C`, but no such gauge freedom is available once the real Hardy function `Z=C+conjugate(C)` and the standard theta normalization are fixed.

## 3. Von Mangoldt parity selects the opposite gap class

For odd `d`, `r` and `r+d` have opposite parity. If

\[
\Lambda(r)\Lambda(r+d)\ne0,
\]

both integers are prime powers. The even member must therefore be a power `2^k`. Among pairs with `r<=X` and `d<=X` there are only `O(log X)` possible even prime powers, and for each such pair

\[
\Lambda(2^k)=\log2,
\qquad
\Lambda(m)\le\log(2X).
\]

This proves the uniform elementary bound (5). In particular, odd gaps cannot carry a linear-size von-Mangoldt pair density.

For even `d`, by contrast, the Hardy--Littlewood singular series is the usual positive prime-pair series; `PL-075` already records that the prescribed-shift asymptotic remains classical hard input and is known only in averaged growing-shift regimes at the required level of generality. The present point does **not** assume that conjecture. It needs only the structural fact that the possible bulk prime-pair class is even `d`, while (3) removes the leading real `1/d` continuation coefficient in exactly that class.

This gives a sharper audit of the escape left by `PL-399`. Multiplying the transition tail by `Lambda(r)Lambda(r+d)` does not merely pay the previously known `1/d` tariff. In the canonical real same-sign quadratic channel, its leading tail is phase-orthogonal to the gap parity on which a bulk prime-pair signal can live.

## 4. Matched control: the parity lock is not RH-specific

The phase selection in (3)--(4) is archimedean and universal. It becomes restrictive for von Mangoldt coefficients only because arithmetic parity removes the odd-gap bulk.

A square-free support control does not have that property. Mirsky's classical theorem gives a positive density of simultaneous square-free values at every fixed nonzero gap, including odd gaps. Thus a `mu^2(r)mu^2(r+d)` control can occupy the real odd-gap tail in (4) without carrying Riemann-zero information. This prevents the parity lock itself from being interpreted as an RH selector.

The durable content is therefore narrower: it rules out one natural attempted **prime-specific amplification** of the continuation tail. Any surviving arithmetic coupling must alter the arithmetic weight, the channel, the projection, or the joint gap aggregation in a way that survives the same matched-control test.

## 5. Prior-art and novelty audit

All individual ingredients are classical or already stored:

- `PL-396` and `PL-399` inherit the exact Paris--Cang incomplete-gamma representation and its uniform `erfc` transition from the standard incomplete-gamma asymptotics recorded in DLMF §§8.12 and 7.12.
- The Riemann--Siegel theta expansion in (13) is classical.
- `PL-075` records the Hardy--Littlewood parity split for von-Mangoldt shifted correlations and the relevant averaged-shift literature.
- The odd-gap bound (5) is elementary from the support of `Lambda` on prime powers.

A targeted literature search around Riemann--Siegel/incomplete-gamma smoothing, complementary-error-function transition phases, near-diagonal additive gaps, parity, and prime-pair correlations recovered the classical smoothing literature (including Paris/Berry--Keating type representations) and the separate Hardy--Littlewood/pair-correlation literature, but no source was found that combines the mesoscopic transition phase with the parity support of `Lambda` in the form (2)--(5).

Accordingly, no theorem-level novelty is claimed for the ingredients. The stored delta is the **line-specific composition and route obstruction**: retaining the phase discarded in `PL-399` shows that the leading continuation tail and the bulk prime-pair parity live in orthogonal real/imaginary sectors in this specific completed quadratic channel.

No new literature anchor is required beyond those already recorded for `PL-399` and `PL-075` in `SOURCES.md`.

## 6. Adversarial boundaries and falsification tests

1. **The phase-pinned regime is narrower than `PL-399`.** Equation (2) assumes `d->infinity` and `d=o(r^(1/3))`. For `d` on or above the `r^(1/3)` scale, the cubic phase `pi d^3/(6r)` in (9) is no longer negligible and the pure parity lock can rotate. The broader `1/d` magnitude law of `PL-399` still applies for `d=o(r)`.

2. **This is one quadratic channel.** The coefficient (1) belongs to the same-sign `C^2+conjugate(C)^2` part of `Z^2`. The mixed `|C|^2` channel, archimedean correction cross-terms, higher moments, or another completed observable can have different phases. No whole-`Z^2` cancellation theorem is asserted.

3. **No broad gap sum is controlled here.** The `o(1/d)` in (3) is pointwise along the stated mesoscopic regime. Summing it over a growing family of even gaps requires a uniform remainder estimate and arithmetic correlation input not supplied here.

4. **Von Mangoldt is an inserted endpoint coupling.** The exact Paris--Cang representation of zeta has coefficient `1`, not `Lambda`. This finding tests the explicit live escape proposed after `PL-399`: can a prime-sensitive endpoint weight compensate the transition tail? It does not claim that an unweighted zeta identity secretly contains the displayed `Lambda` pair sum.

5. **The sign of the odd-gap coefficient is not the important invariant.** Branch conjugation can reverse imaginary orientation but leaves the even-gap leading real part zero. The robust route restriction is the parity split between real and quadrature sectors.

6. **Different arithmetic weights remain open.** Möbius orientation, divisor weights, separate endpoint factor vectors, or a target-relative coupling need not share the von-Mangoldt parity support. They must be analyzed independently rather than ruled out by (3)--(5).

7. **A decisive falsification of this finding is local.** Re-expanding the exact `Q(s/2, pi i q^2)` transition at `T=2 pi r(r+d)` and obtaining a leading phase different from `e^{-i pi/4}e^{-i pi d^2/2}`, after the same principal transition branch and Hardy `theta` normalization are fixed, would invalidate (2). A result showing a linear-size odd-gap `Lambda` correlation would invalidate the arithmetic step, but the elementary prime-power support argument precludes that.

## Research consequence

The most immediate arithmetic escape from `PL-399` is now substantially narrower. A mesoscopic gap can expose growing arithmetic structure and its continuation tail is only `1/d`, but **the leading complex phase matters**: for `d=o(r^(1/3))`, the real Hardy projection suppresses that tail on even gaps, while von Mangoldt parity suppresses bulk arithmetic on odd gaps.

The next viable completed transition mechanism cannot simply attach `Lambda(r)Lambda(r+d)` to the `PL-399` tail and appeal to Hardy--Littlewood amplification. It must either use a channel whose canonical phase couples to the even-gap arithmetic sector, exploit the cubic-phase regime `d` near or above `r^(1/3)` with quantitative control, or introduce a different arithmetic coupling whose signed mass survives both the `1/d` continuation weight and the matched-control gate.