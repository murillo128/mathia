# WI-299 — smooth-kernel tail control reaches the first-prime aperture

**Status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + FIRST-PRIME-GATE-REDIRECT`.

Let

\[
L:=\log 2,
\qquad
r_2:=\frac{L}{2}.
\]

For Suzuki's smooth remainder `r` in the localized Weil form, define the even continuous defect

\[
\delta(s):=-r''(s)-\frac74.
\]

Then on the entire prime-free aperture needed after WI-298 one has the exact uniform estimate

\[
\boxed{
0\le \delta(s)<\frac{21621}{100000}|s|
\qquad (0<|s|\le \log 2),
}
\tag{1}
\]

with `delta(0)=0` by continuity. In particular the coarser Eureka/ManXis tail estimate

\[
\left|-r''(s)-\frac74\right|\le \frac{11}{50}|s|
\]

not only extends from its published range `|s|<=69/100` to the exact first-prime diameter `|s|<=log 2`, but admits the smaller coefficient

\[
\frac{21621}{100000}=0.21621<0.22=\frac{11}{50}.
\]

Consequently, in the retained-residual Schur architecture of the public Eureka report, the same high/cross-mode estimate is valid for every

\[
0<a\le r_2,
\]

and improves to

\[
\boxed{
\|R_a\|
\le
\frac{21621}{100000}\frac{49}{30}a^2
=
\frac{353143}{10^6}a^2.
}
\tag{2}
\]

Thus the explicit analytic-domain cutoff at `a=69/200=0.345` is **not** an obstruction to reaching WI-298's gate `a=r_2=0.346573590...`. What remains is the independent finite low-mode / interval-Schur certification on the narrow strip

\[
\frac{69}{200}<a\le\frac{\log2}{2}.
\]

This finding does **not** import Eureka's `a<=0.345` certificate candidate as established evidence and does **not** prove `lambda_{r_2}>0`; it removes one exact analytic cutoff from that candidate architecture.

## 1. Exact source formula

Suzuki decomposes the smooth remainder as `r=r_0+r_1`, with

\[
r_0(t)=-4\bigl(e^{t/2}+e^{-t/2}-2\bigr)
\]

and, for `t>0`,

\[
r_1''(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t}.
\]

Therefore

\[
-r''(t)
=
2\cosh\frac t2
-
\frac{e^{t/2}}{2\sinh t}
+
\frac1{2t}.
\tag{3}
\]

This is the exact normalization used below. It is the same smooth kernel entering Suzuki's scaled localized quadratic form; no numerical fit or alternate kernel is introduced.

Put `t=2x` and write

\[
F(x):=\delta(2x).
\]

Since `e^x=sinh x+cosh x`, equation (3) becomes

\[
\boxed{
F(x)
=
2\cosh x
-
\frac14\bigl(\operatorname{csch}x+\operatorname{sech}x\bigr)
+
\frac1{4x}
-
\frac74.
}
\tag{4}
\]

The apparent singularity cancels at the origin.

## 2. The normalized defect is increasing because the defect is strictly convex

Differentiating (4) twice gives

\[
\begin{aligned}
F''(x)
={}&2\cosh x
-\frac14\bigl(\operatorname{csch}x+2\operatorname{csch}^3x\bigr)\\
&-\frac14\operatorname{sech}x
+\frac12\operatorname{sech}^3x
+\frac1{2x^3}.
\end{aligned}
\tag{5}
\]

For `x>0`, use the elementary Taylor lower bounds

\[
\sinh x\ge x,
\qquad
\sinh x\ge x\left(1+\frac{x^2}{6}\right),
\]

along with `cosh x>=1` and `0<sech x<=1`. Equation (5) then yields

\[
\begin{aligned}
F''(x)
&\ge
\frac74
+
\frac1{2x^3}
-
\frac1{4x}
-
\frac1{2x^3(1+x^2/6)^3}\\
&=
\frac74
-
\frac{x(x^4+16x^2+72)}{4(x^2+6)^3}.
\end{aligned}
\tag{6}
\]

On the interval needed here, `0<x<=L/2<1`. Hence

\[
\frac{x(x^4+16x^2+72)}{4(x^2+6)^3}
<\frac{89}{864},
\]

and therefore

\[
\boxed{
F''(x)>\frac74-\frac{89}{864}
=\frac{1423}{864}>0.
}
\tag{7}
\]

So `F`, and equivalently `delta`, is strictly convex on the positive first-prime interval.

The standard Laurent/Taylor expansions at zero give

\[
\operatorname{csch}x=\frac1x-\frac x6+O(x^3),
\qquad
\operatorname{sech}x=1-\frac{x^2}{2}+O(x^4),
\]

and (4) therefore gives

\[
F(x)=\frac{x}{24}+O(x^2).
\]

Thus

\[
\delta(0)=0,
\qquad
\delta'(0+)=\frac1{48}>0.
\tag{8}
\]

Strict convexity and (8) imply `delta(t)>0` for every `t>0`. Moreover, for a convex function vanishing at zero, the secant slope `delta(t)/t` is nondecreasing. Hence

\[
0<\frac{\delta(t)}{t}\le\frac{\delta(L)}{L}
\qquad(0<t\le L).
\tag{9}
\]

The full interval estimate is therefore reduced exactly to the endpoint `t=log 2`.

## 3. The endpoint admits a short exact rational enclosure

At `L=log 2`,

\[
e^{L/2}=\sqrt2,
\qquad
\sinh L=\frac34,
\]

so (3) simplifies to

\[
\boxed{
\delta(L)
=
\frac{5\sqrt2}{6}
+
\frac1{2L}
-
\frac74.
}
\tag{10}
\]

Two elementary rational bounds suffice. First,

\[
\sqrt2<\frac{577}{408},
\]

because `577^2-2*408^2=1`. Second, using

\[
\log2
=2\operatorname{arctanh}\frac13
=2\sum_{k\ge0}\frac1{(2k+1)3^{2k+1}},
\]

the first six positive terms give

\[
L>
\frac{15757912}{22733865}
>
q:=\frac{693147}{10^6},
\tag{11}
\]

where the second difference is exactly

\[
\frac{15757912}{22733865}-\frac{693147}{10^6}
=
\frac{335369}{4546773000000}>0.
\]

Set

\[
c:=\frac{21621}{100000}.
\]

Because `L>q`, equation (10) and the rational bounds above give

\[
\delta(L)
<
\frac56\frac{577}{408}
+
\frac1{2q}
-
\frac74.
\]

The remaining comparison is exact rational arithmetic:

\[
\boxed{
 cq-
\left(
\frac56\frac{577}{408}
+
\frac1{2q}
-
\frac74
\right)
=
\frac{16023051499639}{3535049700000000000}>0.
}
\tag{12}
\]

Therefore `delta(L)<cq<cL`. Combining this with (9) proves

\[
0<\delta(t)<ct
\qquad(0<t\le L).
\]

Since `r` is even, `delta` is even, and (1) follows for both signs.

## 4. Consequence for the finite-scale positivity gate

The Eureka report's retained-residual Schur construction separates the first 12 normalized Legendre modes from the unresolved high/cross remainder. Its published analytic tail step uses

\[
\left|-r''(s)-\frac74\right|
\le\frac{11}{50}|s|
\qquad(|s|\le69/100)
\]

and `|| |x-y| ||_{L^2([-1,1]^2)}=sqrt(8/3)<49/30` to obtain

\[
\|R_a\|\le\frac{11}{50}\frac{49}{30}a^2.
\]

For `x,y in [-1,1]` and `a<=r_2`, one has

\[
|a(x-y)|\le2a\le\log2.
\]

Thus (1) applies on the full kernel domain and gives (2) by the same Hilbert--Schmidt estimate. Numerically the coefficient drops from

\[
\frac{11}{50}\frac{49}{30}=0.359333\ldots
\]

to

\[
\frac{353143}{10^6}=0.353143.
\]

At the endpoint `a=r_2`, the `n=2` translation has lag exactly equal to the support diameter. Its two support intervals intersect only on a null endpoint, so its `L^2` autocorrelation contribution is zero, exactly as used in WI-298. Hence the endpoint remains a prime-free quadratic-form problem.

The public Eureka report records an outward interval-Cholesky cover only through `a=69/200`, with a positive final-cell lower pivot, and explicitly classifies the result as a certificate candidate requiring independent replay. No continuity extrapolation from that pivot is made here. The remaining gate is a fresh exact/outward certificate on the narrow interval

\[
\left[\frac{69}{200},\frac{\log2}{2}\right],
\]

using the now-valid tail bound (2), or an independent analytic proof of the same positivity statement.

## Prior art and novelty boundary

Primary formula source:

- M. Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), especially the decomposition `r=r_0+r_1`, the displayed formula for `r_1''`, and the scaled localized quadratic form.

Direct neighboring certificate source:

- ManXis/Eureka, **Task-Conditioned Meta-Agent Orchestration for Scientific Discovery**, arXiv:2608.19047 and public report `manxis-contact/Eureka`, Section 5.3. The report states the coefficient `11/50` on `|s|<=69/100`, the resulting residual norm bound, and the `a<=69/200` interval-certificate candidate. Those claims remain at the report's stated candidate evidence level here.

A targeted prior-art search for the same smooth-kernel inequality, the coefficient `11/50`, and an extension to `|s|<=log2` found the Eureka statement on the shorter interval but no source stating (1) or the convexity reduction above. Search absence is not a priority claim. The durable contribution here is the exact derivation that the smooth-kernel remainder itself does not stop the prime-free finite-scale positivity program before the first-prime aperture.

## Boundaries and falsification

1. **No finite-scale positivity theorem is claimed.** Equation (1) controls only the smooth high/cross remainder. The low-mode Schur matrix still requires an exact certificate through `a=r_2`.
2. **No Eureka certificate is imported as established mathematics.** Its `a<=0.345` interval computation remains external candidate evidence until independently reconstructed/certified under Mathia's evidence rules.
3. **The first-prime endpoint is special.** The argument reaches `a=r_2` because the `n=2` overlap is measure zero there. For `a>r_2`, a genuine indefinite prime translation enters and this prime-free reduction no longer applies.
4. **The normalization is load-bearing.** A mismatch in Suzuki's sign convention for `r''`, the scaling `s=a(x-y)`, or the constant `7/4` falsifies the transfer to the Eureka residual bound.
5. **The convexity proof is independently auditable.** It reduces to differentiation of (4), the elementary inequalities `sinh x>=x+x^3/6`, `cosh x>=1`, `sech x<=1`, and the rational endpoint comparisons (11)--(12). No floating-point inequality is used.

## Research consequence

WI-298 reduced the one-signed complete-screening first-crossing branch to the single theorem `lambda_{(log2)/2}>0`. WI-259/WI-260 showed that the public `FP-0.35` route does not yet certify that theorem. The independent Eureka route stopped just below the same aperture at `69/200` and exposed an analytic tail bound only to diameter `69/100`.

Equation (1) removes that diameter cutoff exactly. The highest-value next test is therefore no longer to improve the smooth-kernel estimate or search for another sub-threshold radius. It is to independently reconstruct/certify the retained low-mode Schur inequality only on the missing strip `69/200<a<=(log2)/2`. A positive certificate would combine with WI-298 to exclude the entire one-signed complete-screening first-crossing branch; a failure would identify a genuine finite-modal obstruction rather than an artifact of the published tail domain.
