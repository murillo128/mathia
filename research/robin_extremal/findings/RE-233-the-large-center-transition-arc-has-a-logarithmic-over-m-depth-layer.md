# RE-233 — The large-center transition arc has a logarithmic-over-m depth layer

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + POSITIVE-REAL-CENTER-DRIFT + WIDENING-CORRIDOR + MACROSCOPIC-BOUNDARY-LAYER + LOGARITHMIC-DETUNING + SEQUENCE-SENSITIVE-TRANSITION + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent finding:** RE-232.

RE-232 proved that for an unbounded positive-real single center with finite scaled depth

\[
\kappa_m:=\frac{N_m}{m(a_m-1)}\to\kappa>1,
\]

the truncated negative-binomial predictor has a sharp fixed-arc exponential boundary

\[
\alpha_*(\kappa)
=
\arccos\!\left(\frac{1+\log\kappa}{\kappa}\right).
\]

Every fixed arc strictly below `alpha_*(kappa)` is predicted exponentially well and every fixed arc strictly above it fails. The exact equality case was left open because the exponential rate vanishes there.

This finding resolves that equality in a clean rate-achieving large-center subfamily and, more importantly, shows that **the equality case is not determined by the limiting value `kappa` alone**. There is a transition layer of width `log(m)/m` in the scaled depth. At exact tuning the closed boundary arc is predicted with error of order `m^(-1/2)`; an undershoot of more than an explicit multiple of `log(m)/m` destroys prediction.

The result is representation-specific. It does not improve the universal separated lower bound and it does not lower the `5.996390` construction from RE-218.

## 1. Fast-center regime and the boundary scalar

Use the same exact predictor as RE-232,

\[
Q_{m,N,a}(z)
=
z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z)
=
\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)}.
\tag{1}
\]

Assume

\[
a_m>1,\qquad
a_m\to\infty,\qquad
\delta_m:=\frac1{a_m-1},\qquad
m\delta_m\to0,
\tag{2}
\]

and

\[
\kappa_m:=\frac{N_m\delta_m}{m}\to\kappa>1.
\tag{3}
\]

The condition `m delta_m -> 0` is a convenient clean boundary-layer regime. For example `a_m=m^2` satisfies it and still has `log a_m=o(m)`, so it remains inside the rate-achieving class used in the Wiener calculation of RE-232.

Put

\[
h(x):=x-1-\log x,
\tag{4}
\]

fix the limiting transition arc

\[
\alpha_*:=\alpha_*(\kappa)
=
\arccos\!\left(\frac{1+\log\kappa}{\kappa}\right),
\tag{5}
\]

and define the moving boundary exponent

\[
q_m
:=
\kappa_m(1-\cos\alpha_*)-h(\kappa_m).
\tag{6}
\]

Because

\[
1-\cos\alpha_*
=
\frac{h(\kappa)}{\kappa},
\tag{7}
\]

one has `q_m -> 0` and `q_m=0` when `kappa_m=kappa`.

The main conclusion is

\[
\boxed{
\sup_{|\theta|\le\alpha_*}
\left|F_{m,N_m,a_m}(e^{-i\theta})-1\right|
\asymp_\kappa
\frac{e^{m q_m}}{\sqrt m}.
}
\tag{8}
\]

Consequently,

\[
\boxed{
F_m(e^{-i\theta})\to1
\ \text{uniformly on }[-\alpha_*,\alpha_*]
\iff
m q_m-\frac12\log m\to-\infty.
}
\tag{9}
\]

Thus the equality case of RE-232 has a complete scalar criterion in this fast-center regime.

## 2. The denominator has an explicit Gaussian prefactor

Retain the exact normalization from RE-232,

\[
D_{m,N,a}
=
\int_0^1
s^{m-1}
\left(1-\frac sa\right)^N ds
=
p_m^{N_m}I_m,
\qquad
p_m:=1-\frac1{a_m},
\tag{10}
\]

where

\[
I_m
=
\int_0^1
s^{m-1}
\left(1+\delta_m(1-s)\right)^{N_m}ds.
\tag{11}
\]

Since

\[
N_m\delta_m=m\kappa_m
\tag{12}
\]

and, by (2),

\[
N_m\delta_m^2
=
m\kappa_m\delta_m
=o(1),
\tag{13}
\]

the logarithm of the second factor in (11) has the uniform local expansion

\[
N_m\log(1+\delta_m(1-s))
=
m\kappa_m(1-s)+o(1)
\tag{14}
\]

on every fixed neighborhood of the interior saddle. The limiting phase

\[
\phi_x(s):=\log s+x(1-s)
\tag{15}
\]

has its unique maximum at `s=1/x`, with

\[
\phi_x(1/x)=h(x),
\qquad
\phi_x''(1/x)=-x^2.
\tag{16}
\]

Also `s^(m-1)=s^(-1) exp(m log s)`, so the amplitude at the saddle is `x`. The ordinary local Gaussian Laplace estimate therefore gives, uniformly for `kappa_m` in a fixed compact neighborhood of `kappa`,

\[
\boxed{
I_m
=
\sqrt{\frac{2\pi}{m}}\,
e^{m h(\kappa_m)}
(1+o(1)).
}
\tag{17}
\]

The cancellation of the saddle amplitude `kappa_m` against `sqrt(|phi''|)=kappa_m` is why the leading prefactor in (17) is independent of `kappa`.

No external incomplete-beta asymptotic theorem is required for (17): split (11) into a fixed saddle neighborhood and its exponentially smaller complement, use (14) in the neighborhood, and apply the quadratic Taylor expansion of (15).

## 3. Endpoint Laplace asymptotics determine the full closed-arc error

The exact angular derivative from RE-232 is

\[
\frac{d}{d\theta}
F_m(e^{-i\theta})
=
-i e^{-im\theta}
\frac{R_m(\theta)}{I_m},
\tag{18}
\]

where

\[
R_m(\theta)
=
\left(1+\delta_m(1-e^{-i\theta})\right)^{N_m}.
\tag{19}
\]

Equation (13) gives the uniform complex expansion on every fixed theta interval

\[
R_m(\theta)
=
\exp\!\left(
m\kappa_m(1-e^{-i\theta})
\right)
(1+o(1)).
\tag{20}
\]

Combining (17)--(20), define

\[
S_m(\theta)
:=
-i\theta
+\kappa_m(1-e^{-i\theta})
-h(\kappa_m).
\tag{21}
\]

Then uniformly on `[0,alpha_*]`,

\[
\boxed{
F'_m(\theta)
=
-i\sqrt{\frac{m}{2\pi}}\,
e^{mS_m(\theta)}
(1+o(1)),
}
\tag{22}
\]

where `F'_m(theta)` denotes the derivative of `F_m(e^{-i theta})`.

Its real part is

\[
\Re S_m(\theta)
=
\kappa_m(1-\cos\theta)-h(\kappa_m),
\tag{23}
\]

which is strictly increasing on `(0,alpha_*)` for all large `m`. Hence the integral from `0` to `alpha_*` is a one-sided endpoint Laplace integral. Since

\[
S'_m(\alpha_*)
=
\kappa_m\sin\alpha_*
+i(\kappa_m\cos\alpha_*-1)
\to
S'_\kappa(\alpha_*)\ne0,
\tag{24}
\]

one obtains

\[
\boxed{
F_m(e^{-i\alpha_*})-1
=
-\frac{i}{\sqrt{2\pi m}}\,
\frac{e^{mS_m(\alpha_*)}}
{S'_\kappa(\alpha_*)}
(1+o(1)).
}
\tag{25}
\]

Taking absolute values,

\[
\boxed{
|F_m(e^{-i\alpha_*})-1|
=
\frac{e^{mq_m}}
{\sqrt{2\pi m}\,d_\kappa}
(1+o(1)),
}
\tag{26}
\]

where

\[
d_\kappa
:=
|S'_\kappa(\alpha_*)|
=
\sqrt{
(\kappa\sin\alpha_*)^2+
(\kappa\cos\alpha_*-1)^2
}
>0.
\tag{27}
\]

This is the lower half of (8).

For the upper half, fix a small endpoint neighborhood. On it,

\[
\Re S_m(\theta)
\le
q_m-c_\kappa(\alpha_*-\theta)
\tag{28}
\]

for some fixed `c_kappa>0`, while outside that neighborhood the real exponent is smaller than `q_m` by a fixed positive amount. Integrating the absolute derivative in (22) therefore gives

\[
\sup_{0\le\theta\le\alpha_*}
|F_m(e^{-i\theta})-1|
\le
C_\kappa\frac{e^{mq_m}}{\sqrt m}
+e^{-c m}.
\tag{29}
\]

Because `q_m=o(1)`, the second term is negligible relative to the first. The modulus in (19) is even in `theta`, so the same bound holds on the negative half of the arc. Equations (26) and (29) prove (8) and hence (9).

The important point is that there is no unresolved cancellation at equality: the full error is controlled by one nonstationary endpoint layer, whose complex prefactor in (25) is nonzero.

## 4. The transition width is exactly logarithmic over m

Let

\[
c_\kappa:=\frac{\log\kappa}{\kappa}>0.
\tag{30}
\]

Differentiating (6) as a function of its moving argument gives, at `x=kappa`,

\[
\frac{d}{dx}
\left[
x(1-\cos\alpha_*)-h(x)
\right]_{x=\kappa}
=
-\frac{\log\kappa}{\kappa}
=
-c_\kappa.
\tag{31}
\]

Therefore

\[
q_m
=
-c_\kappa(\kappa_m-\kappa)
+O((\kappa_m-\kappa)^2).
\tag{32}
\]

Suppose the scaled depth undershoots the limiting value by

\[
\kappa_m
=
\kappa
-\beta\frac{\log m}{m}
+o\!\left(\frac{\log m}{m}\right).
\tag{33}
\]

Then

\[
m q_m-\frac12\log m
=
\left(
\beta\frac{\log\kappa}{\kappa}
-\frac12
\right)\log m
+o(\log m).
\tag{34}
\]

Define

\[
\boxed{
\beta_*(\kappa)
:=
\frac{\kappa}{2\log\kappa}.
}
\tag{35}
\]

Equations (9) and (34) give the sharp two-sided detuning law

\[
\boxed{
\beta<\beta_*(\kappa)
\Longrightarrow
\text{closed-boundary prediction succeeds},
}
\tag{36}
\]

while

\[
\boxed{
\beta>\beta_*(\kappa)
\Longrightarrow
\text{closed-boundary prediction fails}.
}
\tag{37}
\]

Thus the transition is not on the coarser `o(1)` scale of `kappa_m`; it lives at `log(m)/m`.

At exact tuning, for example

\[
a_m=m^2,
\qquad
N_m=
\left\lfloor
\kappa m(a_m-1)
\right\rfloor,
\tag{38}
\]

one has

\[
\kappa_m-\kappa
=
O(m^{-3}),
\qquad
q_m=O(m^{-3}),
\tag{39}
\]

so (8) gives

\[
\boxed{
\sup_{|\theta|\le\alpha_*}
|F_m(e^{-i\theta})-1|
=
\Theta_\kappa(m^{-1/2}).
}
\tag{40}
\]

The open arc of RE-232 therefore extends to the closed transition arc for this naturally tuned family, but only with polynomial rather than exponential convergence.

Conversely, choosing the same centers `a_m=m^2` but

\[
\kappa_m=\kappa-m^{-1/3}+o(m^{-1/3})
\tag{41}
\]

gives `m q_m -> +infinity`, so prediction fails strongly; choosing

\[
\kappa_m=\kappa+m^{-1/3}+o(m^{-1/3})
\tag{42}
\]

gives `m q_m -> -infinity`, so it succeeds much faster than `m^(-1/2)`. These matched controls have the same limiting `kappa` and the same limiting arc. They prove directly that no theorem phrased only in terms of `kappa_m -> kappa` can classify the equality case.

At the exact logarithmic coefficient `beta=beta_*(kappa)`, the first-order powers balance. A finer `1/m` displacement then decides whether the factor in (8) tends to zero, a nonzero constant, or infinity. The scalar criterion (9), rather than `beta` alone, is the canonical boundary statement.

## 5. Wiener cost is unchanged

The boundary classification does not create a cheaper predictor.

For `a_m=m^2`, one still has `log a_m=o(m)`, and the coefficient calculation in RE-232 applies with `kappa_m->kappa`. Hence

\[
\frac1m\log\|F_m\|_A
\to
w(\kappa)
:=
\kappa+1+\log\kappa.
\tag{43}
\]

At exact tuning, (40) therefore realizes the **closed** transition arc at normalized Wiener rate

\[
\frac{w(\kappa)}{\alpha_*(\kappa)}.
\tag{44}
\]

RE-232 already proved

\[
\frac{w(\kappa)}{\alpha_*(\kappa)}>6
\qquad(\kappa>1).
\tag{45}
\]

So adding the boundary point does not alter the optimization conclusion: the finite-supercritical positive-real large-center branch remains strictly more expensive than the `5.996390` finite-center construction of RE-218.

## 6. Falsification boundary

Several restrictions are load-bearing.

The theorem assumes a **positive-real** center. Complex supercritical centers can have a genuinely complex denominator saddle and are not reduced to (17) by this argument.

The theorem also assumes

\[
m\delta_m=\frac{m}{a_m-1}\to0.
\tag{46}
\]

This makes the finite-center correction `N_m delta_m^2` vanish and exposes the clean Gaussian prefactor. Slower center growth can carry an additional order-one or larger correction into the transition layer. RE-232's exponential boundary remains valid there, but the precise `log(m)/m` equality criterion requires a separate expansion.

The result assumes finite `kappa>1`; `kappa_m->infinity` is still outside the finite-saddle normal form.

Finally, this is a theorem about the truncated negative-binomial **single-center** predictor. It does not improve `C_sep>=1`, does not prove a universal factor-six lower bound, and does not constrain multi-center/minimax, rational, or other predictor classes.

## 7. Prior-art audit

A fresh literature search was made for moving-parameter incomplete-beta transitions, incomplete Laplace saddle/end-point asymptotics, negative-binomial partial-sum transition layers, and predictor-specific boundary costs.

The nearest classical sources remain N. M. Temme's uniform incomplete-gamma/incomplete-beta expansions (Mathematics of Computation 29 (1975), 1109--1114) and *Incomplete Laplace Integrals: Uniform Asymptotic Expansion with Application to the Incomplete Beta Function* (SIAM Journal on Mathematical Analysis 18 (1987), 1638--1663), together with the explicit remainder treatment of G. Nemes and A. B. Olde Daalhuis, *Uniform Asymptotic Expansion for the Incomplete Beta Function* (SIGMA 12 (2016), 101).

Those works make the appearance of Gaussian/error-function transition prefactors classical asymptotic background. The audit did not identify the Mathia predictor's specific fixed arc `alpha_*(kappa)`, the scalar boundary criterion (9), or the `beta_*(kappa) log(m)/m` depth-detuning threshold.

No external theorem is load-bearing here: (17) is an elementary one-saddle Laplace estimate from the exact integral, and (25) is an elementary nonstationary endpoint Laplace estimate from the exact derivative. Therefore no new durable `SOURCES.md` dependency is required.

## 8. Consequence for the current frontier

RE-232 left three narrow single-center directions: the equality arc, complex supercritical drift, and `kappa_m->infinity`. The positive-real equality arc is now classified in a broad rate-achieving fast-center regime.

The classification has an important negative lesson. The equality case is **sequence-sensitive**: the limiting pair `(kappa, alpha_*(kappa))` is insufficient. Exact or mildly over-tuned depth predicts the closed arc, while a sufficiently large `log(m)/m` undershoot fails. This is a genuine boundary layer, not a missing sign in the exponential-rate proof.

It also does not rescue the architecture. Even the exactly tuned closed arc retains the six-plus Wiener cost. For improving the current separated upper bound, the remaining high-value alternatives are therefore still a genuine geometry change such as multi-center/minimax or a different predictor representation; further positive-real equality tuning only refines the boundary of an already dominated branch.
