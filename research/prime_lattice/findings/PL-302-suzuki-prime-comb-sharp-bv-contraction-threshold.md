# PL-302 — Suzuki's arithmetic shift comb loses BV contractivity exactly when the 3-channel activates

**Evidence:** `EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + SHARP-THRESHOLD`

**Status:** `SHIFT-ONLY-CONTRACTION-CLOSED + COUPLED-BV-ROUTE-STILL-OPEN`

## Claim

`PL-301` proved that Suzuki's exact finite arithmetic shift comb preserves bounded variation, but its termwise estimate

\[
\operatorname{TV}(EP_a u)\le 2W(a)\operatorname{TV}(Eu)
\]

was only an upper bound. In particular, at the working aperture `a=0.8` the coefficient `2W(a)>1` did **not** by itself rule out a substantially sharper contraction estimate for the whole shift comb.

That escape can be closed exactly.

Work on

\[
I=(-1,1),
\qquad
C_hu(x)=1_I(x)(Eu)(x+h),
\]

and write the positive version of Suzuki's arithmetic comb as

\[
Q_a=-P_a
=
\sum_{\substack{n\ge2\\ \Lambda(n)>0\\ \log n<2a}}
 w_n\bigl(C_{h_n}+C_{-h_n}\bigr),
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
h_n=\frac{\log n}{a}.
\]

The strict inequality `log n<2a` is the effective support condition: at `log n=2a` one has `h_n=2`, and `C_{\pm2}=0` almost everywhere on `I`.

Define

\[
W_{<}(a)
=
\sum_{\substack{n\ge2\\ \Lambda(n)>0\\ \log n<2a}}
\frac{\Lambda(n)}{\sqrt n}.
\]

Then, on

\[
BV_0(I)=\{u\in L^1(I):Eu\in BV(\mathbb R)\},
\qquad
\|u\|_{BV_0}=\|u\|_1+\operatorname{TV}(Eu),
\]

the exact arithmetic comb has the following sharp contractivity transition:

\[
\boxed{
\|P_a\|_{BV_0\to BV_0}<1
\quad\text{for every}\quad
0<a\le \frac12\log 3,
}
\]

whereas

\[
\boxed{
\|P_a\|_{BV_0\to BV_0}
\ge
\frac{\log2}{\sqrt2}+
\frac{\log3}{\sqrt3}
\approx1.1244131723>1
\quad\text{for every}\quad
a>\frac12\log3.
}
\]

The same endpoint test also gives

\[
\boxed{
\|P_a\|_{L^1\to L^1}\ge W_{<}(a).
}
\]

Thus no sharpening of a **shift-comb-only** BV or `L^1` operator-norm estimate can turn `P_a` into a contraction once the `n=3` channel is genuinely active. At `a=0.8`, the obstruction is already

\[
W_{<}(0.8)
=
\frac{\log2}{\sqrt2}
+
\frac{\log3}{\sqrt3}
+
\frac{\log2}{2}
\approx1.4709867626.
\]

This strengthens the diagnostic in `PL-301`: the earlier number `2W(0.8)` was a crude **upper** variation coefficient, whereas `W_{<}(0.8)` is now an explicit **lower** operator-norm obstruction.

## Exact endpoint-localization argument

Fix `a` and list its finitely many effective lags

\[
0<h_1,\ldots,h_N<2.
\]

Because distinct prime powers give distinct `log n`, these lags are distinct. Choose `delta>0` smaller than

\[
\min_j h_j,
\qquad
\min_j(2-h_j),
\qquad
\min_{i\ne j}|h_i-h_j|.
\]

Set

\[
u_\delta=1_{(1-\delta,1)}.
\]

For each effective lag, the right-going truncated translate vanishes,

\[
C_{-h_j}u_\delta=0,
\]

while

\[
C_{h_j}u_\delta
=
1_{(1-\delta-h_j,\,1-h_j)}.
\]

By the choice of `delta`, all these output intervals lie strictly inside `I` and are pairwise disjoint. Hence

\[
Q_a u_\delta
=
\sum_j w_j
1_{(1-\delta-h_j,\,1-h_j)}.
\]

There is therefore no cancellation at all on this test function. Directly,

\[
\|Q_a u_\delta\|_1
= W_{<}(a)\,\|u_\delta\|_1,
\]

and, because the zero extension of every disjoint weighted interval contributes exactly two jumps,

\[
\operatorname{TV}(EQ_a u_\delta)
= W_{<}(a)\,\operatorname{TV}(Eu_\delta).
\]

Consequently

\[
\frac{\|P_a u_\delta\|_{BV_0}}
{\|u_\delta\|_{BV_0}}
=W_{<}(a),
\]

and the lower bounds above follow. The overall minus sign in `P_a=-Q_a` is irrelevant to either norm.

## Why the threshold is exactly `(log 3)/2`

Let

\[
a_2=\frac12\log2,
\qquad
a_3=\frac12\log3.
\]

For `0<a<=a_2`, there is no effective arithmetic channel, so `P_a=0` almost everywhere.

For

\[
a_2<a\le a_3,
\]

the only effective channel is `n=2`. At the upper endpoint, the `n=3` channel has lag exactly `2` and is still zero almost everywhere. Put

\[
w_2=\frac{\log2}{\sqrt2}
\approx0.4901290717.
\]

Throughout this one-channel aperture interval,

\[
h_2=\frac{\log2}{a}>1.
\]

The two source regions contributing to `C_{h_2}` and `C_{-h_2}` are therefore disjoint, which gives the sharper `L^1` estimate

\[
\|P_a u\|_1\le w_2\|u\|_1.
\]

Together with the exact shift-variation estimate from `PL-301`,

\[
\operatorname{TV}(EP_a u)
\le 2w_2\operatorname{TV}(Eu),
\]

this yields

\[
\|P_a u\|_{BV_0}
\le
2w_2\|u\|_{BV_0},
\]

with

\[
2w_2=\sqrt2\log2
\approx0.9802581435<1.
\]

So `P_a` is a strict `BV_0` contraction throughout `0<a<=a_3`.

For every `a>a_3`, both `n=2` and `n=3` are effective. Therefore

\[
W_{<}(a)
\ge
\frac{\log2}{\sqrt2}
+
\frac{\log3}{\sqrt3}
\approx1.1244131723>1,
\]

and endpoint localization proves noncontractivity immediately. The transition is genuinely one-sided: at `a=a_3` the new channel is still null; for every arbitrarily small increase of `a` it becomes an interior truncated shift and the lower norm bound jumps above one.

## Adversarial stress test

This result is deliberately narrow.

First, it says nothing by itself about contractivity or coercivity of the **full** operator

\[
T+c_aI+P_a+R_a.
\]

The logarithmic principal operator `T`, the completion `R_a`, resolvent structure, spectral gap, or cancellations on the actual ground eigenfunction may still control variation. In particular, the endpoint indicators used here need not approximate the relevant ground-state branch in the graph norm of `T`.

Second, the result does not contradict the uniform BV mapping estimate of `PL-301`; boundedness and contraction are different questions. It only eliminates the hope that the finite positive shift comb itself has a hidden operator-norm contraction at the physically relevant aperture after the `n=3` activation.

Third, no novelty is claimed for the elementary facts about translations, truncations, or BV variation. The substantive source-specific statement is the exact threshold produced by Suzuki's arithmetic weights and support geometry. The calculation depends on the actual prime-power coefficients `Lambda(n)/sqrt(n)` and on the aperture law `h_n=log n/a`; it is not a generic theorem about arbitrary weighted shifts.

## Prior-art audit

The exact localized operator and its arithmetic coefficients come from Suzuki's completed-Weil construction (source `56` in `research/prime_lattice/SOURCES.md`). Generic weighted-translation norm bounds and BV composition/translation estimates are classical background and were not treated as discoveries.

A targeted audit for truncated/weighted translations on intervals, BV operator norms, and Suzuki's localized Weil operator found no prior statement of the source-specific threshold above. More importantly for line-local novelty, `PL-301` supplied only the termwise upper coefficient `2W(a)` and explicitly left open whether a sharper estimate for the arithmetic comb could restore contraction. The endpoint-localization lower bound closes exactly that narrow escape and no more.

## Consequence for the live theorem target

At the current `a=0.8` target, a proof of uniform BV control for the completed-Weil ground branch cannot come from a contraction estimate for `P_a` alone. Any successful argument must use structure that the endpoint-localized positive comb test deliberately discards: coupling to `T`, smoothing/cancellation through `R_a`, a resolvent or spectral-gap estimate, a graph-norm inequality, or a property specific to the actual ground eigenfunction.

The surviving question is therefore sharper than in `PL-301`: not whether the exact arithmetic remainder is BV-stable—it is—but whether the **coupled eigen-equation** suppresses the variation that the arithmetic comb can create on unrestricted BV data.

## Dependencies

- `PL-291`: exact scaled Suzuki operator and prime-power shift structure.
- `PL-294`: exact support/activation geometry for the same localized shifts.
- `PL-299`: uniform BV control for the pure principal branch.
- `PL-300`: generic norm-small perturbations do not transfer BV control.
- `PL-301`: exact Suzuki remainder is BV-stable, with a crude termwise `2W(a)` variation bound.
- Source `56` in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2.
