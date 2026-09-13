# WI-266 — Suzuki's null equation rules out the endpoint-bump screening family

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC-RIGIDITY + PRIOR-ART-AUDITED`.

`WI-264` constructed, at every fixed finite aperture, an antisymmetric pair of narrow endpoint bumps whose autocorrelation simultaneously vanishes at every active von-Mangoldt lag and has the favorable sign against Suzuki's continuous source. `WI-265` then showed that the same screened vector can be an exact terminal zero mode of an abstract positive rank-one-defect operator with strict positivity on every proper centered and translated shorter window. Those findings left one source-specific gate deliberately open: whether the **actual localized Weil null equation** can coexist with the endpoint-gap geometry.

It cannot. For every member of the `WI-264` endpoint-bump family satisfying its stated width conditions, Suzuki's exact distributional kernel has a nonempty open interval in the central gap on which all local and von-Mangoldt translation terms vanish, while the remaining continuous convolution is strictly positive. Hence the vector cannot satisfy

\[
A_a^{\rm Weil}v=0.
\]

The mechanism is elementary but genuinely source-specific: away from the origin and the prime-power atoms, Suzuki's Weil kernel is a **strictly increasing function of separation**. The positive left endpoint bump is farther from every positive point in the central interval than the negative right endpoint bump, so exact antisymmetry cannot cancel the continuous kernel there.

This removes the strongest explicit screening countermodel currently available to the first-crossing program. It does **not** prove that an arbitrary first-crossing null vector must have nonzero autocorrelation at a prime-power lag, and it does not exclude more complicated screened support geometries.

## 1. The screened family and its exact width reserve

Fix a finite aperture `a` in the regime of `WI-264`. Let

\[
\mathcal P_a
=\{\ell=\log n:\Lambda(n)>0,\ 0<\ell<2a\},
\]

and, when this set is nonempty, write

\[
\ell_a=\max\mathcal P_a,
\qquad
\delta_a=2a-\ell_a>0.
\tag{1}
\]

At the hypothetical first crossing relevant to the clue, `WI-253` already gives `a>0.8`, so `\mathcal P_a` is nonempty. The `WI-264` construction chooses

\[
0<\varepsilon<
\min\left(
 h_0,\log2,
 a-\frac{h_0}{2},
 \frac{\delta_a}{2}
\right),
\tag{2}
\]

where `h_0` is the sign-change point of the continuous source. Let `\phi\ge0` be a nonzero smooth bump with support closure `[0,\varepsilon]`, vanishing to all orders at the endpoints, and put

\[
u_-(x)=\phi(x+a),
\qquad
u_+(x)=\phi(a-x),
\qquad
v(x)=\frac{u_-(x)-u_+(x)}{\sqrt2}.
\tag{3}
\]

Thus the positive bump is supported on `[-a,-a+\varepsilon]`, the negative bump on `[a-\varepsilon,a]`, and `v\in H_0^1(-a,a)`. The middle interval `(-a+\varepsilon,a-\varepsilon)` is an exact support gap.

The autocorrelation screening result of `WI-264` remains unchanged: because `2\varepsilon<\delta_a`, every active lag in `\mathcal P_a` lies inside the autocorrelation zero interval. The question here is stronger and different: can the vector itself satisfy Suzuki's pointwise/distributional null equation?

## 2. Suzuki's localized operator exposes the missing source-specific constraint

Masatoshi Suzuki's *Weil's quadratic form via the screw function*, arXiv:2606.09096v1 (2026), constructs

\[
B_a=D^*G_aD,
\qquad
\mathfrak D(B_a)=H_0^1(-a,a),
\]

and proves in Theorem 1.1 that the canonical localized Weil operator `A_a` is the Friedrichs extension of `B_a`. In §2.5, equations (2.10)--(2.11), he gives the distributional convolution kernel

\[
B_av=(-g'')*v
\tag{4}
\]

on the core and writes its singular local term, the von-Mangoldt translations, and the regular remainder explicitly. The same distributional identity applies to the smooth `H_0^1` vector (3): it follows directly from `B_a=D^*G_aD` by integration by parts, with the boundary terms zero because `v(\pm a)=0`. On any open set separated from the support of the singular and discrete terms, (4) is represented by an ordinary smooth convolution.

The regular kernel can be read directly from Suzuki's Weil functional, equations (1.1) and the displayed explicit formula preceding it. For `h>0` away from prime-power atoms,

\[
\begin{aligned}
k(h)
&:=(-g'')(h)\\
&=e^{h/2}+e^{-h/2}
 -\frac{e^{h/2}}{e^h-e^{-h}}\\
&=e^{h/2}
 -\frac{e^{-5h/2}}{1-e^{-2h}}.
\end{aligned}
\tag{5}
\]

This is the negative of the continuous source function `w(h)` used in `WI-263`--`WI-265`. More importantly for the null equation, it is strictly increasing:

\[
\boxed{k'(h)>0\qquad(h>0).}
\tag{6}
\]

Indeed

\[
F(h):=\frac{e^{-5h/2}}{1-e^{-2h}}>0
\]

has

\[
\frac{F'(h)}{F(h)}
=-\frac52-\frac{2e^{-2h}}{1-e^{-2h}}<0,
\]

so `F'(h)<0` and therefore `k'(h)=\tfrac12e^{h/2}-F'(h)>0`.

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v1, Theorem 1.1 and equations (2.5), (2.10), (2.11): https://arxiv.org/abs/2606.09096.

## 3. There is a nonempty interval where every prime translation vanishes

Consider positive points in the support gap. A translation `v(x+\ell)` with `\ell\in\mathcal P_a` can meet the right endpoint bump only when

\[
a-\varepsilon-\ell\le x\le a-\ell.
\tag{7}
\]

Since every active `\ell\ge\log2`, all such translations vanish whenever

\[
x>a-\log2.
\tag{8}
\]

Similarly, `v(x-\ell)` can meet the left endpoint bump only when

\[
\ell-a\le x\le\ell-a+\varepsilon.
\tag{9}
\]

Because `\ell\le\ell_a=2a-\delta_a`, all such translations vanish whenever

\[
x>a-\delta_a+\varepsilon.
\tag{10}
\]

The other two endpoint/translation combinations are impossible for `0<x<a-\varepsilon`. Therefore define

\[
\boxed{
I_a=
\left(
\max\{0,a-\log2,a-\delta_a+\varepsilon\},
\ a-\varepsilon
\right).
}
\tag{11}
\]

This interval is nonempty. The three required comparisons are exactly the reserves already present in (2):

\[
\varepsilon<a,
\qquad
\varepsilon<\log2,
\qquad
2\varepsilon<\delta_a.
\tag{12}
\]

For every `x\in I_a`, consequently,

\[
\boxed{
v(x)=0,
\qquad
v(x\pm\log n)=0
\quad
\text{for every }\Lambda(n)>0,\ \log n<2a.
}
\tag{13}
\]

If exceptionally `\log n=2a`, its translated values also vanish on `I_a` after zero extension outside `(-a,a)`. Thus the distinction between `<` in the `WI-264` screening set and `\le e^{2a}` in Suzuki's finite translation sum creates no endpoint case.

Because `I_a` is also disjoint from the support of `v`, the local delta and principal-value singularity in Suzuki's equation contribute only through their ordinary regular values against the endpoint support; after combining the regular pieces they are exactly the kernel `k` in (5). There is no singular point `x=y` on this interval.

## 4. The continuous kernel has a fixed positive sign on that interval

For `x\in I_a` write the left endpoint point as `y=-a+t` and the corresponding right endpoint point as `y=a-t`, with `0\le t\le\varepsilon`. Both separations from `x` are positive because `x<a-\varepsilon`:

\[
|x-(-a+t)|=a-t+x,
\qquad
|x-(a-t)|=a-t-x.
\tag{14}
\]

Using (3), the ordinary part of the convolution (4) on `I_a` is therefore

\[
(B_av)(x)
=\frac1{\sqrt2}
\int_0^\varepsilon
\phi(t)
\left[
 k(a-t+x)-k(a-t-x)
\right]dt.
\tag{15}
\]

Every bracket in (15) is strictly positive for `x>0` by (6), because

\[
a-t+x>a-t-x>0.
\tag{16}
\]

Since `\phi\ge0` and is not identically zero,

\[
\boxed{
(B_av)(x)>0
\qquad(x\in I_a).
}
\tag{17}
\]

This is the contradiction that the abstract rank-one model of `WI-265` cannot reproduce. If the endpoint bump were an actual localized Weil null vector, then `v\in\mathfrak D(B_a)\subset\mathfrak D(A_a)` and Theorem 1.1 would give

\[
0=A_av=B_av.
\tag{18}
\]

But (17) shows that `B_av` is represented by a strictly positive smooth function on the nonempty open interval `I_a`. Hence (18) is impossible even distributionally.

Therefore

\[
\boxed{
\text{no }WI\text{-}264\text{ antisymmetric two-endpoint-bump vector can satisfy }
A_a^{\rm Weil}v=0.
}
\tag{19}
\]

## 5. What this does and does not prove

The contradiction uses information that survives none of the abstract reductions in `WI-265`: the exact translation structure and, crucially, the strict separation monotonicity of Suzuki's regular arithmetic/archimedean kernel. It therefore validates the source-specific direction of the active first-crossing clue. The `WI-264` countermodel remains a correct barrier to arguments that use only autocorrelation positivity, source signs, or finitely many prime layers; it is simply not compatible with the actual null equation.

The result is deliberately narrower than a theorem about arbitrary first-crossing modes. It does not prove that every null vector has `C_v(\log n)\ne0` for some prime power, does not rule out autocorrelation gaps produced by three or more support components, and does not show that the quantitative lower-envelope family `\mathcal F_v(r)\ge r\lambda_r` alone excludes screening. A more complicated vector could arrange prime translations inside its support and could allow the continuous convolution to cancel with those discrete terms.

What is now excluded is the whole explicit family that had survived the previous stress tests: **two narrow antisymmetric endpoint components separated by one empty middle region**. Any replacement countermodel must defeat the pointwise source-specific equation, not merely its quadratic/autocorrelation sign consequences.

## 6. Prior-art and novelty audit

The operator realization and all source formulas used above are Suzuki's established 2026 preprint results. The relation between the localized Weil form, the screw function, and finite-window positivity originates in Suzuki's earlier work, including **Aspects of the screw function corresponding to the Riemann zeta-function**, *J. London Math. Soc.* 107 (2023), DOI `10.1112/jlms.12785`. No part of the localized operator or explicit formula is claimed here as new.

A targeted search around Suzuki's localized Weil operator, compact-support null vectors, endpoint-supported tests, and autocorrelation screening located the source/operator framework but no statement of the support-gap contradiction (11)--(19). Search absence is audit context only and is not a priority claim.

The Mathia deduction is the combination of three already explicit ingredients: the complete endpoint-bump family of `WI-264`, Suzuki's exact null equation, and the strict monotonicity (6) of its regular kernel. Unlike `WI-265`, no auxiliary abstract operator is introduced.

## Falsification and audit test

The finding is exact and uses no numerical certificate. A falsification must locate an error in at least one load-bearing step:

1. the `WI-264` width conditions imply the nonempty interval (11);
2. every active von-Mangoldt translation vanishes on that interval as in (13);
3. Suzuki's distributional formula reduces there to the ordinary regular kernel (5);
4. `k'(h)>0` for every `h>0`;
5. the antisymmetric endpoint signs give (15), hence strict positivity rather than cancellation;
6. the smooth endpoint bump belongs to `H_0^1(-a,a)`, where `A_a` extends `B_a`.

The domain point is important: formula (2.10) in Suzuki is printed first for `C_c^\infty(-a,a)`, while the `WI-264` bump has support closure reaching the endpoints. The present use is through `B_a` on `H_0^1`: its boundary values vanish, integration by parts produces the distribution `-g''`, and on `I_a` that distribution is represented by the smooth ordinary convolution in (15). No pointwise formula for a general element of `\mathfrak D(A_a)` is being assumed.

## Consequence for the research line

The accepted first-crossing program has passed its first genuinely source-specific stress test: the actual Suzuki null equation excludes the explicit endpoint-screening geometry that survived generic spectral firstness. The next useful question is no longer whether the two-bump family can be repaired by abstract positivity. It is whether the same null equation forces a broader **support-spreading or no-long-gap theorem** for arbitrary candidate null vectors, or whether a more complicated source-compatible screened geometry can evade (17).

A productive generalization would identify a support configuration invariant under the prime translations and the monotone continuous kernel strongly enough that any macroscopic empty region produces a one-sided sign contradiction. A decisive negative outcome would instead construct a multi-component screened vector for which the prime translations can cancel the continuous convolution on every support gap. Either result would materially sharpen the route from first-crossing defect to exclusion of off-critical zeros.