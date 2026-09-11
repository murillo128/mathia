# ANF-172 — endpoint phase is the dyadic slope defect of a positive Fejer scale family

**Status:** `EXACT-DERIVED + POSITIVE-SCALE-REPRESENTATION + PHASE-PRESERVING + TARGET-SCALE-DISCRIMINATOR`. `ANF-171` shows that the single positive moving-window square function `Q_H` is not a scale-sharp surrogate for endpoint danger: at the exact `ANF-170` threshold it can be large while the signed shell `Re S_H` is negligible because the current coefficient and the preceding block sit in quadrature. The phase information is nevertheless not intrinsically incompatible with a positive-energy formulation.

For every endpoint sequence there is an exact positive Fejer family `F_L` indexed by the physical window length `L`. If `T_L:=L F_L`, then the signed dyadic shell is exactly a **difference of discrete scale slopes**

\[
2\operatorname{Re}S_H
=
(T_{2H}-T_{2H-1})-(T_H-T_{H-1}).
\]

Thus the angle lost by `Q_H` is retained by how a positive short-window energy changes with scale. For the actual source `r_X=\vartheta-Q_R`, every `F_L` is a positive average of squared exact twisted-residual sums over intersections of endpoint prefixes with length-`L` intervals. This gives a third source interface between direct prime-pair correlation and the phase-blind square function: a **coupled two-scale Selberg/Fejer increment**. It does not make the arithmetic theorem automatic; estimating the positive energies independently and subtracting coarse asymptotics can still lose the required scale precision. The useful target is the coupled slope defect itself.

## 1. The endpoint lag ledger has a positive Fejer interpolation

Fix one endpoint and use the notation of `ANF-169`--`ANF-171`. Let

\[
b_1,\ldots,b_{K-1}\in\mathbb C,
\qquad
w_m:=1-\frac{m}{K},
\tag{1}
\]

and define

\[
A
:=
\sum_{m=1}^{K-1}w_m|b_m|^2,
\tag{2}
\]

together with the weighted lag correlations

\[
G_h
:=
\sum_{j=1}^{K-1-h}
w_{j+h}\,
\overline{b_j}b_{j+h},
\qquad
R_h:=\operatorname{Re}G_h.
\tag{3}
\]

The dangerous dyadic shell of `ANF-169` is

\[
S_H:=\sum_{h=H}^{2H-1}G_h,
\qquad
2H<K.
\tag{4}
\]

For an integer `1<=L<K`, define the endpoint Fejer energy

\[
\boxed{
\mathcal F_L
:=
A+
2\sum_{h=1}^{L-1}
\left(1-\frac{h}{L}\right)R_h.
}
\tag{5}
\]

This quantity is nonnegative for every coefficient vector, despite the endpoint weight `w_{j+h}`. The cleanest proof is an exact Gram representation. Extend the index `s` over all integers and put

\[
I_{r,s,L}
:=
\{j:1\le j\le r,\ s<j\le s+L\}.
\tag{6}
\]

Then

\[
\boxed{
\mathcal F_L
=
\frac{1}{KL}
\sum_{r=1}^{K-1}
\sum_{s\in\mathbb Z}
\left|
\sum_{j\in I_{r,s,L}}b_j
\right|^2
\ge0.
}
\tag{7}
\]

Only finitely many `s` contribute. To verify (7), expand the square. For fixed `j,k`, the number of prefix horizons `r` containing both indices is

\[
K-\max(j,k),
\tag{8}
\]

while the number of length-`L` integer windows containing both is

\[
\left(L-|j-k|\right)_+.
\tag{9}
\]

After division by `KL`, the matrix coefficient is therefore

\[
\left(1-\frac{\max(j,k)}{K}\right)
\left(1-\frac{|j-k|}{L}\right)_+.
\tag{10}
\]

The diagonal of (10) gives (2), and for `j<k=j+h` the off-diagonal coefficient is exactly

\[
w_{j+h}\left(1-\frac{h}{L}\right),
\tag{11}
\]

which gives (5).

Equivalently, the matrix in (10) is the Schur product of the endpoint-prefix Gram matrix with the usual triangular Fejer lag matrix. No positivity theorem beyond the explicit counting identity (7) is needed.

## 2. The signed dyadic shell is exactly a scale-slope defect

Set

\[
T_L:=L\mathcal F_L,
\qquad
T_0:=0.
\tag{12}
\]

From (5),

\[
T_L
=
LA+
2\sum_{h=1}^{L-1}(L-h)R_h.
\tag{13}
\]

Its first discrete scale difference is therefore

\[
\boxed{
D_L
:=
T_L-T_{L-1}
=
A+
2\sum_{h=1}^{L-1}R_h.
}
\tag{14}
\]

Taking the difference of (14) at scales `H` and `2H` yields the exact identity

\[
\boxed{
D_{2H}-D_H
=
2\sum_{h=H}^{2H-1}R_h
=
2\operatorname{Re}S_H.
}
\tag{15}
\]

This recovers precisely the phase-sensitive quantity that enters the endpoint ledger. No Cauchy--Schwarz relaxation and no modulus replacement has occurred.

Combining (15) with `ANF-169` gives an immediate necessary condition for macroscopic endpoint completion. If

\[
E_{\partial}\ge\delta X K\log X,
\tag{16}
\]

then for one endpoint `sigma` and one dyadic `H` with `2H<K`,

\[
\operatorname{Re}S_H^\sigma
\ge
\frac{\delta}{8\log_2(2K)}X\log X,
\tag{17}
\]

and hence

\[
\boxed{
D_{2H}^\sigma-D_H^\sigma
\ge
\frac{\delta}{4\log_2(2K)}X\log X.
}
\tag{18}
\]

Consequently a sufficient source theorem is

\[
\boxed{
\sup_{\sigma,H}
\left|
D_{2H}^\sigma-D_H^\sigma
\right|
=
o\!\left(\frac{X\log X}{\log K}\right)
}
\tag{19}
\]

over the surviving dyadic endpoint scales. By the contrapositive of `ANF-169`, (19) forces

\[
E_{\partial}=o(XK\log X).
\tag{20}
\]

Equation (19) is algebraically equivalent to controlling the signed dyadic correlation, but its **representation is different**: each `T_L` is a positive short-window square energy by (7), and the sign is carried only by the coupled variation across scales.

## 3. The ANF-171 quarter-turn packet is classified correctly

The distinction from `Q_H` is visible on the exact stress control of `ANF-171`. There

\[
b_j=a e^{ij\theta},
\qquad
\theta=\frac{\pi}{3H-1},
\tag{21}
\]

with `H=o(K)`, and the complete moving window lies at a quarter turn relative to `b_m`. `ANF-171` proves

\[
A Q_H
\asymp
a^4K^2H^2,
\qquad
|S_H|
\asymp
a^2KH,
\tag{22}
\]

while

\[
|\operatorname{Re}S_H|
\ll
a^2H^2.
\tag{23}
\]

The positive relaxation can therefore sit at its danger scale while the true endpoint statistic is negligible.

The Fejer-scale family does not make that false positive. By (15),

\[
\boxed{
|D_{2H}-D_H|
\ll
a^2H^2.
}
\tag{24}
\]

At the target-scale normalization used in `ANF-171`,

\[
a^2=\log X,
\qquad
H\asymp\frac{X}{K L_*},
\qquad
L_*:=\log_2(2K),
\tag{25}
\]

so

\[
\frac{|D_{2H}-D_H|}
     {X\log X/L_*}
\ll
\frac{X}{K^2L_*}
\longrightarrow0
\tag{26}
\]

throughout the difficult range `0<epsilon<1/4`, since `K=X^{1-2epsilon+o(1)}`.

Thus all individual energies in (7) remain positive, yet their **scale slopes remember the quarter-turn cancellation** that `Q_H` forgets. The obstruction identified in `ANF-171` is therefore more precise than “positive methods lose phase.” A single phase-blind positive statistic loses phase; a coupled positive scale family can retain it exactly through its scale variation.

## 4. For the physical source the positive family is a genuine short-interval variance object

At the left endpoint, insert

\[
b_j^-
=
r_X(X+j)(X+j)^{-iU},
\qquad
r_X=\vartheta-Q_R.
\tag{27}
\]

Every inner sum in (7) is then exactly

\[
\sum_{j\in I_{r,s,L}}
r_X(X+j)(X+j)^{-iU},
\tag{28}
\]

namely the distinguished-twist prime-minus-Ramanujan residual on an ordinary integer interval, additionally truncated by an endpoint prefix. The right endpoint has the same form after reversing its coefficient order.

Therefore `mathcal F_L` does not require expanding

\[
r_X(n)r_X(n+h)
\tag{29}
\]

into prime--prime, prime--Ramanujan, Ramanujan--prime, and Ramanujan--Ramanujan pieces before exploiting positivity. Those four terms remain coupled inside the exact residual sums in (28). This is the same source information that `ANF-149` identified as essential, now organized as a positive family over physical scales.

This suggests a concrete alternative to the two routes left by `ANF-171`. Instead of proving the stronger phase-blind estimate `A Q_H=o(...)`, or attacking every signed shifted correlation after expansion, one may target the **coupled scale increment**

\[
\boxed{
\big(T_{2H}-T_{2H-1}\big)
-
\big(T_H-T_{H-1}\big)
=
o\!\left(\frac{X\log X}{\log K}\right)
}
\tag{30}
\]

directly for the actual residual. The left side is exactly `2 Re S_H`, but the four `T` terms are positive Fejer/Selberg-type square energies built from (28).

There is an important precision warning. Separate upper bounds for `T_H` and `T_{2H}`, or separate asymptotics for `mathcal F_H` and `mathcal F_{2H}`, do not automatically control (30). The main scale in `T_L` contains the large affine contribution `LA`; (30) detects a much smaller change of **first slope** after that affine part cancels exactly. A theorem that estimates the positive energies independently with errors larger than `X log X/log K` can therefore lose the same endpoint information in a different way.

The useful arithmetic object is consequently not “Selberg energy is small” but **adjacent-scale stability of the endpoint Fejer energy at two dyadically separated scales**. Any application of existing short-interval variance machinery has to be audited at that increment precision rather than only at the level of its main term.

## 5. Prior-art boundary and frontier consequence

The triangular lag kernel in (5), its positive moving-window realization, and the general relation between short-interval variances and autocorrelations are classical harmonic-analysis/analytic-number-theory facts. A bounded prior-art audit found the expected Fejer-kernel identity and the standard short-interval-variance/pair-correlation literature; no external result is used in the derivation above.

The Mathia-specific content is the exact combination of the endpoint-prefix weight from `ANF-157`/`ANF-169` with the Fejer scale parameter and the identity (15), which restores the **particular signed dyadic shell** surviving `ANF-171`. No claim is made that (30) is easier than the signed correlation theorem in every analytic framework. It is an alternative representation whose value is that it preserves the prime-minus-Ramanujan cancellation inside positive short-interval squares while discriminating the target-scale quarter-turn control.

The live gate should therefore no longer be phrased as a choice between a signed correlation theorem and a phase-blind positive square-function theorem. There is a third exact interface:

\[
\boxed{
\text{endpoint danger}
\Longrightarrow
\text{large dyadic defect in the scale slope of a positive Fejer family}.
}
\tag{31}
\]

A useful next audit is to ask whether available or sharpenable twisted Selberg-integral technology can control the increment in (30) **coupled across scales**, rather than estimating `T_L` independently. If that still costs a polynomially excessive error, the frontier remains the direct signed prime--Ramanujan correlation of `ANF-169`; if the scale increment admits extra cancellation, it provides a phase-faithful positive route around the `ANF-171` obstruction.
