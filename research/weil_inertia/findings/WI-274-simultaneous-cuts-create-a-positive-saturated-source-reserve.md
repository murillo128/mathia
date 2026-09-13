# WI-274 — simultaneous cuts create a positive saturated source reserve

## Status

- **Evidence:** `EXACT-DERIVED + SOURCE-SPECIFIC-RIGIDITY + SIMULTANEOUS-CUT-BOOTSTRAP + PRIOR-ART-AUDITED`.
- **Scope:** an exact strengthening of the unrestricted first-crossing source constraints in `WI-253`, `WI-269`, `WI-270`, and `WI-273`. Instead of testing one sharp cut or one translated window at a time, it integrates the entire family of admissible half-line cuts. Every translated pair is then counted for exactly the length of its lag. The result is a strictly positive lower bound on the *saturated* endpoint source functional, even though the one-parameter lower bound of `WI-253` degenerates as the aperture tends to the first crossing.
- **What it does not claim:** this is not RH, does not prove that the first null mode is one-signed, does not yet prove nonzero prime overlap in the sign-changing branch, and does not provide a numerical lower bound for the spectral-area reserve. The main reserve below is valid for an arbitrary real first null mode; the prime-overlap corollary additionally assumes one sign.
- **Novelty boundary:** sharp-cut localization, layer-cake/Fubini counting, ground-state transforms, and domain monotonicity are classical ingredients. Suzuki supplies the localized Weil operator and first-crossing framework. `WI-253` supplies the sliding autocorrelation source, while `WI-269`--`WI-273` supply the sharp-cut/source normalization and the single-cut screening analysis. The Mathia deduction is to integrate all sharp cuts before estimating the source, obtaining a positive spectral-area reserve at the saturated endpoint. A targeted prior-art audit found Suzuki's operator framework and generic localization/layer-cake methods but no source stating this zeta-specific integrated first-crossing inequality. No priority claim is made.

## Claim

Assume RH is false. Let

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\}
\]

be Suzuki's first unrestricted localized Weil crossing, and let `v` be a normalized real attained zero mode

\[
\|v\|_2=1,\qquad A_av=0,\qquad q_a\ge0,
\tag{1}
\]

extended by zero outside `(-a,a)`. As in `WI-269`, put

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\qquad 0<h<2a,
\tag{2}
\]

and define the real autocorrelation

\[
C_v(h):=\int_{\mathbb R}v(x+h)v(x)\,dx.
\tag{3}
\]

For almost every `t\in(-a,a)`, let

\[
M_L(t)=\int_{-a}^{t}v(x)^2dx,
\qquad
M_R(t)=\int_t^av(x)^2dx,
\tag{4}
\]

\[
r_L(t)=\frac{a+t}{2},
\qquad
r_R(t)=\frac{a-t}{2},
\tag{5}
\]

and

\[
J_t(h):=\int_{t-h}^{t}v(x+h)v(x)\,dx.
\tag{6}
\]

The two complementary sharp truncations have the same form energy

\[
\begin{aligned}
Q_t
&:=q_a\!\left(v\mathbf 1_{(-a,t)}\right)
=q_a\!\left(v\mathbf 1_{(t,a)}\right)\\
&=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}J_t(\log n)
+\int_0^{2a}w(h)J_t(h)\,dh.
\end{aligned}
\tag{7}
\]

Firstness gives the two simultaneous lower bounds

\[
Q_t\ge\lambda_{r_L(t)}M_L(t),
\qquad
Q_t\ge\lambda_{r_R(t)}M_R(t).
\tag{8}
\]

Define the saturated source functional

\[
\boxed{
\mathcal S_v
:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}(\log n)C_v(\log n)
+\int_0^{2a}h\,w(h)C_v(h)\,dh.
}
\tag{9}
\]

Then the whole cut family forces

\[
\boxed{
\mathcal S_v
\ge
2\int_{a/2}^{a}\lambda_r\,dr
>0.
}
\tag{10}
\]

Thus the saturated endpoint source cannot disappear at the first crossing. This is stronger than taking `r\uparrow a` in the `WI-253` inequality `\mathcal F_v(r)\ge r\lambda_r`, whose right side may tend to zero.

There is a useful one-signed consequence. Let `h_0=\log\rho`, where `\rho^3-\rho-1=0`, so that

\[
w(h)>0\quad(0<h<h_0),
\qquad
w(h)<0\quad(h>h_0),
\tag{11}
\]

and define the finite positive archimedean budget

\[
K_+
:=\int_0^{h_0}h\,w(h)\,dh<\infty.
\tag{12}
\]

If `v` is one-signed, take `v\ge0`. Then `0\le C_v(h)\le1`, and the weighted active-prime overlap

\[
\mathcal P_v
:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}(\log n)C_v(\log n)
\tag{13}
\]

obeys

\[
\boxed{
\mathcal P_v
\ge
2\int_{a/2}^{a}\lambda_r\,dr-K_+.
}
\tag{14}
\]

Consequently, complete prime-lag screening on the one-signed branch can occur only if

\[
\boxed{
\int_{a/2}^{a}\lambda_r\,dr\le\frac{K_+}{2}.
}
\tag{15}
\]

This converts the narrow-gap Carleman difficulty of `WI-270`/`WI-273` into a different quantitative target: compare an integrated firstness reserve with a finite exact archimedean budget.

## 1. Sharp-cut identity is sign-independent

`WI-270` proves that, for almost every `t`, both sharp truncations belong to the localized form domain. Although that finding subsequently specializes to a one-signed mode for its Carleman estimate, the admissibility and ground-state-transform step do not use the sign of `v`.

Let `H_t=\mathbf 1_{(t,\infty)}`. The weak null equation gives

\[
q_a(v,H_tv)=q_a(v,(1-H_t)v)=0.
\tag{16}
\]

Because `H_t^2=H_t`, the multiplier identity of `WI-269` retains exactly the source edges crossing the cut. The two complementary indicators have the same squared multiplier difference, so both truncations have the common value (7). This establishes (7) for a general real first null mode.

The left truncation is supported in an interval of length `a+t`, hence radius `r_L=(a+t)/2`; the right truncation has radius `r_R=(a-t)/2`. Translation invariance and the definition of `\lambda_r` therefore give (8). In particular,

\[
2Q_t
\ge
\lambda_{r_L(t)}M_L(t)
+\lambda_{r_R(t)}M_R(t)
\tag{17}
\]

for almost every cut.

## 2. Integrating all cuts counts every lag by exactly its length

For every fixed `0<h<2a`, Fubini gives the exact signed identity

\[
\boxed{
\int_{-a}^{a}J_t(h)\,dt
=h\,C_v(h).
}
\tag{18}
\]

Indeed, after inserting (6), a fixed pair `(x,x+h)` contributes precisely for cuts

\[
x<t<x+h,
\]

an interval of `t`-length exactly `h`. No positivity of `v(x+h)v(x)` is needed. Absolute Fubini is legitimate because

\[
\int_{-a}^{a}|J_t(h)|dt
\le h\int_{\mathbb R}|v(x+h)v(x)|dx
\le h\|v\|_2^2=h.
\tag{19}
\]

The factor `h` also regularizes the short-range source: `w(h)=O(1/h)` as `h\downarrow0`, so `h\,w(h)` is locally bounded. The prime sum is finite at fixed `a`. Integrating (7) therefore yields

\[
\boxed{
\int_{-a}^{a}Q_t\,dt=\mathcal S_v.
}
\tag{20}
\]

This is the key difference from estimating cuts separately: the entire source is now paid once with its exact lag multiplicity.

## 3. Firstness has a strictly positive integrated reserve

Write

\[
f(x)=v(x)^2,
\qquad
\int_{-a}^{a}f(x)dx=1.
\tag{21}
\]

Integrating the right side of (17), swapping the mass and cut integrals, and using `dt=2dr` gives

\[
\begin{aligned}
I
&:=\int_{-a}^{a}
\left[
\lambda_{r_L(t)}M_L(t)
+\lambda_{r_R(t)}M_R(t)
\right]dt\\
&=\int_{-a}^{a}f(x)W_a(x)\,dx,
\end{aligned}
\tag{22}
\]

where

\[
W_a(x)
=2\left[
\int_{(a+x)/2}^{a}\lambda_r\,dr
+
\int_{(a-x)/2}^{a}\lambda_r\,dr
\right].
\tag{23}
\]

Domain inclusion makes `r\mapsto\lambda_r` nonincreasing. The function `W_a` is even, and for `x\ge0`,

\[
\begin{aligned}
W_a(x)-W_a(0)
=2\Bigg[
&\int_{(a-x)/2}^{a/2}\lambda_r\,dr\\
-&\int_{a/2}^{(a+x)/2}\lambda_r\,dr
\Bigg]\ge0,
\end{aligned}
\tag{24}
\]

because the two intervals have the same length and the first lies entirely at smaller radii, where `\lambda_r` is no smaller. Hence

\[
W_a(x)\ge W_a(0)=4\int_{a/2}^{a}\lambda_r\,dr.
\tag{25}
\]

Using `\int f=1`,

\[
I\ge4\int_{a/2}^{a}\lambda_r\,dr.
\tag{26}
\]

Integrating (17), then applying (20) and (26), proves

\[
2\mathcal S_v
=2\int_{-a}^{a}Q_tdt
\ge I
\ge4\int_{a/2}^{a}\lambda_rdr,
\]

which is (10). At a first crossing, `\lambda_r>0` for every `0<r<a`; therefore the integral over `[a/2,a)` is strictly positive.

Equality in the center-minimum step is also rigid: any mass of `v^2` away from the center can only increase the weight `W_a(x)` unless `\lambda_r` is locally flat across the paired radius intervals in (24). This gives a potential second bootstrap direction if the spectral-area inequality is nearly saturated.

## 4. One-signed screening has only a finite archimedean budget

Assume now `v\ge0`. Then

\[
0\le C_v(h)\le\|v(\cdot+h)\|_2\|v\|_2\le1.
\tag{27}
\]

By the unique sign change (11),

\[
\int_0^{2a}h\,w(h)C_v(h)dh
\le
\int_0^{h_0}h\,w(h)dh
=K_+.
\tag{28}
\]

(The same inequality remains valid if `2a<h_0`, since the omitted part of the defining integral for `K_+` is positive.) Combining (9), (10), and (28) gives (14). If all active prime autocorrelations vanish, then `\mathcal P_v=0`, and (15) follows.

The point is not that (15) is already contradictory. Rather, the single-cut Carleman analysis pays a short-range `1/h` singularity separately at an individual cut, whereas integrating all cuts first supplies the exact factor `h` from (18). The positive continuous budget becomes finite and source-specific. This avoids the `Theta(L)\to\pi/2` narrow-gap wall isolated in `WI-273`; the remaining question is whether the first-crossing spectral area is large enough, or can be strengthened using further null-mode structure.

## 5. Relation to `WI-253` and the current clue

`WI-253` proves, for `0<r<a`,

\[
\mathcal F_v(r)
=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\min(\log n,2r)C_v(\log n)
+\int_0^{2a}\min(h,2r)w(h)C_v(h)dh
\ge r\lambda_r.
\tag{29}
\]

For each fixed lag below `2a`, the source weight in `\mathcal F_v(r)` tends to `h` as `r\uparrow a`, so its formal endpoint is exactly `\mathcal S_v`. The lower bound `r\lambda_r`, however, can collapse to zero at the first crossing. Equation (10) shows that this endpoint functional retains the accumulated positivity of **all** interior radii:

\[
\mathcal S_v\ge2\int_{a/2}^{a}\lambda_rdr>0.
\tag{30}
\]

Thus the accepted clue `CLUE-first-global-crossing-sliding-autocorrelation-symbol.md` has genuine partial progress: the full cut family creates an unscreenable total source reserve before any Fourier-symbol estimate. It does not yet resolve the clue because, for sign-changing `v`, prime and archimedean pieces can still cancel inside `\mathcal S_v`; for one-signed `v`, the finite budget test (15) is not yet known to fail.

## 6. Prior-art audit and provenance

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), https://arxiv.org/abs/2606.09096. The paper supplies the localized closed Weil form/operator framework used here; it does not state (10) in the form found during the targeted audit.

Local dependencies:

- `WI-253` — first global crossing and the sliding autocorrelation/source functional;
- `WI-269` — exact signed-source ground-state transform for multipliers;
- `WI-270` — almost-everywhere admissibility of sharp half-line cuts and the common cut energy;
- `WI-273` — exact positive-tail refinement and the `pi/2` Carleman wall for arbitrarily narrow one-signed gaps.

Generic layer-cake/coarea counting and variational domain monotonicity are classical background rather than novelty claims. Targeted searches around Suzuki/localized Weil first crossings, simultaneous sharp-cut localization, integrated ground-state transforms, and layer-cake spectral-gap inequalities found no matching zeta-specific spectral-area reserve. Search absence is only an audit record, not evidence of priority.

## 7. Falsification checklist and next test

The finding should be withdrawn or corrected if any of the following fails under the exact localized Weil form conventions used by `WI-269`/`WI-270`:

1. the almost-everywhere sharp-cut form-domain statement cannot be used for sign-changing real `v`;
2. the two complementary sharp truncations do not share the same source energy `Q_t`;
3. the cut-counting identity (18) acquires a missing factor or boundary term;
4. firstness does not imply both inequalities in (8) after translation to the minimal containing interval;
5. `r\mapsto\lambda_r` is not nonincreasing under domain inclusion;
6. the sign assumption has inadvertently entered the proof of (10), rather than only the corollary (14)--(15).

The highest-value next test is quantitative: obtain a rigorous lower bound for

\[
\int_{a/2}^{a}\lambda_rdr
\tag{31}
\]

from compact-window positivity, operator comparison, continuity/threshold information, or a source-conditioned variational argument, and compare it with `K_+/2`. If that comparison cannot beat the finite budget, the next route is to combine (10) with the PSD multiplier/source constraints of `WI-269` rather than returning to a single-cut mass estimate.
