# RE-232 — Supercritical large centers have a sharp macroscopic radius and a six-plus Wiener floor

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + POSITIVE-REAL-CENTER-DRIFT + WIDENING-CORRIDOR + MACROSCOPIC-NORMAL-FORM + SHARP-BOUNDARY + WIENER-COST + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-218, RE-223, RE-230, RE-231.

RE-231 identified the unit microscopic transition for an unbounded positive-real single center. With

\[
\kappa_m:=\frac{N_m}{m(a_m-1)},
\]

finite limits `kappa<1` retain a microscopic phase, while `kappa>=1` flatten every fixed `u=m theta` window. That left open the question relevant to actual prediction: whether a finite supercritical `kappa>1` can flatten a **fixed nonzero arc**, and at what Wiener cost.

For the same exact predictor

\[
Q_{m,N,a}(z)
:=z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)},
\tag{1}
\]

assume throughout

\[
a_m>1,
\qquad
a_m\to+\infty,
\qquad
\kappa_m\to\kappa\in[1,\infty).
\tag{2}
\]

For finite `kappa>1`, define

\[
h(\kappa):=\kappa-1-\log\kappa,
\tag{3}
\]

and

\[
\boxed{
\alpha_*(\kappa)
:=
\arccos\!\left(\frac{1+\log\kappa}{\kappa}\right)
\in(0,\pi/2).
}
\tag{4}
\]

Set `alpha_*(1)=0` by continuity of the phase boundary from the supercritical side.

The main conclusions are:

1. for every fixed `0<alpha<alpha_*(kappa)`,

\[
\boxed{
\sup_{|\theta|\le\alpha}
|F_{m,N_m,a_m}(e^{-i\theta})-1|
\le e^{-c m}
}
\tag{5}
\]

for some `c=c(alpha,kappa)>0` and all sufficiently large `m`;

2. for every fixed `alpha>alpha_*(kappa)`, uniform prediction on `[-alpha,alpha]` is impossible; indeed `F_m` has exponentially large oscillation on a microscopic subinterval of that arc;

3. every such positive-real finite-supercritical family obeys the Wiener lower rate

\[
\boxed{
\liminf_{m\to\infty}
\frac1m\log\|F_m\|_A
\ge
w(\kappa)
:=\kappa+1+\log\kappa;
}
\tag{6}
\]

4. the rate `w(kappa)` is achievable for slow center growth such as `a_m=m`, so the optimal normalized cost inside this large-center class is

\[
\boxed{
C_{\infty,+}
=
\inf_{\kappa>1}
\frac{\kappa+1+\log\kappa}
{\alpha_*(\kappa)};
}
\tag{7}
\]

5. purely analytically,

\[
\boxed{C_{\infty,+}>6.}
\tag{8}
\]

Thus the finite-supercritical widening-corridor branch left open by RE-231 is real — it genuinely predicts fixed arcs — but it cannot improve the current finite-center construction of RE-218, whose certified separated Wiener exponent is `5.996390`.

The exact transition point `alpha=alpha_*(kappa)` is not classified here.

## 1. Exact derivative and the macroscopic Laplace rate

Retain the normalization from RE-230--RE-231:

\[
p_m:=1-\frac1{a_m},
\qquad
\delta_m:=\frac1{a_m-1},
\tag{9}
\]

and

\[
D_{m,N,a}
:=
\int_0^1
s^{m-1}
\left(1-\frac sa\right)^N ds
=p^N I_m,
\tag{10}
\]

where

\[
I_m
:=
\int_0^1
s^{m-1}
\left(1+\delta_m(1-s)\right)^{N_m}ds.
\tag{11}
\]

The exact angular derivative is

\[
\frac{d}{d\theta}
F_m(e^{-i\theta})
=
-i e^{-im\theta}
\frac{R_m(\theta)}{I_m},
\tag{12}
\]

with

\[
R_m(\theta)
:=
\left(1+\delta_m(1-e^{-i\theta})\right)^{N_m}.
\tag{13}
\]

Because `kappa_m=N_m delta_m/m -> kappa` and `delta_m->0`, uniformly for `s in [0,1]`,

\[
\frac1m
\log\left[
s^{m-1}
(1+\delta_m(1-s))^{N_m}
\right]
=
\log s+\kappa(1-s)+o(1).
\tag{14}
\]

For `kappa>1`, the limiting exponent

\[
\phi_\kappa(s):=\log s+\kappa(1-s)
\tag{15}
\]

has its unique maximum at `s=1/kappa`, with value

\[
\phi_\kappa(1/\kappa)
=
\kappa-1-\log\kappa
=h(\kappa).
\tag{16}
\]

The elementary Laplace upper and lower bounds therefore give

\[
\boxed{
\frac1m\log I_m\to h(\kappa).
}
\tag{17}
\]

At `kappa=1` the maximum moves to the endpoint `s=1` and the corresponding exponential rate is zero.

On any fixed compact theta interval, expansion of (13) gives uniformly

\[
\frac1m\log|R_m(\theta)|
=
\frac{N_m}{m}
\Re\log\left(1+\delta_m(1-e^{-i\theta})\right)
\to
\kappa(1-\cos\theta),
\tag{18}
\]

because the quadratic remainder contributes

\[
O\!\left(\frac{N_m\delta_m^2}{m}\right)
=O(\kappa_m\delta_m)
=o(1).
\tag{19}
\]

Combining (12), (17), and (18),

\[
\boxed{
\frac1m
\log\left|
\frac{d}{d\theta}F_m(e^{-i\theta})
\right|
\to
\Psi_\kappa(\theta)
:=
\kappa(1-\cos\theta)-h(\kappa)
}
\tag{20}
\]

uniformly on fixed compact theta intervals.

This is the macroscopic normal form missing from RE-231.

## 2. The fixed-arc phase boundary is sharp away from equality

The function `Psi_kappa(theta)` is even and strictly increasing in `|theta|` on `[0,pi]`. Solving `Psi_kappa(alpha)=0` gives

\[
\kappa(1-\cos\alpha)
=
\kappa-1-\log\kappa,
\tag{21}
\]

hence exactly (4).

Suppose first that

\[
0<\alpha<\alpha_*(\kappa).
\tag{22}
\]

Then there exists `c>0` such that

\[
\Psi_\kappa(\theta)\le-2c
\qquad(|\theta|\le\alpha).
\tag{23}
\]

The uniform convergence in (20) gives, for all large `m`,

\[
\sup_{|\theta|\le\alpha}
\left|
\frac{d}{d\theta}F_m(e^{-i\theta})
\right|
\le e^{-cm}.
\tag{24}
\]

Since the normalization is exact,

\[
F_m(1)=1,
\tag{25}
\]

and integration from zero proves (5).

Now suppose

\[
\alpha>\alpha_*(\kappa).
\tag{26}
\]

Choose an interior point `theta_0` with

\[
\alpha_*(\kappa)<|\theta_0|<\alpha.
\tag{27}
\]

Then `Psi_kappa(theta_0)>0`, so (20) gives

\[
|F_m'(\theta_0)|\ge e^{c m}
\tag{28}
\]

for some `c>0`. This large derivative cannot be hidden by arbitrarily fast phase cancellation on a shorter scale. From (12)--(13),

\[
\frac{d}{d\theta}\log F_m'(\theta)
=
-im
+
N_m
\frac{i\delta_m e^{-i\theta}}
{1+\delta_m(1-e^{-i\theta})},
\tag{29}
\]

so on any fixed theta compact set

\[
\left|
\frac{d}{d\theta}\log F_m'(\theta)
\right|
=O(m+N_m\delta_m)
=O(m).
\tag{30}
\]

Take an interval of width `ell/m` around `theta_0`, with fixed `ell>0` sufficiently small. Across that interval the modulus of `F_m'` changes by at most a fixed factor and its phase rotates by less than, say, `pi/4`. Integrating (28) on that interval therefore yields two points inside `[-alpha,alpha]` whose `F_m` values differ by at least

\[
\frac{c_1}{m}e^{c_2m}.
\tag{31}
\]

Uniform convergence to the constant `1` is impossible. This proves the sharp separation between fixed arcs strictly below and strictly above (4).

At `kappa=1`, (17) has zero rate and

\[
\Psi_1(\theta)=1-\cos\theta>0
\qquad(\theta\ne0),
\tag{32}
\]

so every fixed nonzero arc fails. This is consistent with RE-231: the unit threshold flattens compact microscopic `u=m theta` windows but does not yet buy any fixed macroscopic radius.

The equality case `alpha=alpha_*(kappa)` is a genuine transition not decided by the exponential-rate argument; polynomial prefactors matter there.

## 3. Widening buys prediction but has an intrinsic Wiener price

For positive real `a>1`, all coefficients of a fixed degree in (1) have the same sign. The exact Wiener norm of the unnormalized numerator is therefore

\[
\boxed{
\|Q_{m,N,a}\|_A
=
a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1+\frac1a\right)^k.
}
\tag{33}
\]

At DC,

\[
0<Q_{m,N,a}(1)
=
a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac1a\right)^k
\le1,
\tag{34}
\]

because the corresponding infinite negative-binomial series sums to `a^m`. Hence

\[
\|F_{m,N,a}\|_A
\ge
\|Q_{m,N,a}\|_A.
\tag{35}
\]

Write

\[
t_k
:=
\binom{m+k-1}{k}
\left(1+\frac1a\right)^k.
\tag{36}
\]

Since `N/[m(a-1)] -> kappa>1`, one has `N asymp m a`. For the last `L=floor(a/2)` terms,

\[
\frac{t_{k-1}}{t_k}
=
\frac{k}{(m+k-1)(1+1/a)}
\ge
1-\frac{C_\kappa}{a}
\tag{37}
\]

uniformly for `N-L<=k<=N` and all sufficiently large `m`. Consequently there is a constant `c_kappa>0` such that

\[
\sum_{k=0}^{N}t_k
\ge
c_\kappa a\,t_N.
\tag{38}
\]

The factor `a` in (38) is important: it makes the lower rate uniform even if the center grows exponentially fast with `m`.

Using

\[
\binom{m+N-1}{N}
=
\prod_{j=1}^{m-1}\frac{N+j}{j}
\tag{39}
\]

and `N/(ma)->kappa`, Stirling gives, after the `a` factor in (38) cancels the one missing endpoint factor in (39),

\[
\liminf_{m\to\infty}
\frac1m
\log\left[
a^{-m}
\sum_{k=0}^{N}t_k
\right]
\ge
1+\log\kappa+\kappa.
\tag{40}
\]

Together with (35), this proves (6).

The lower rate is not merely an artifact of (38). Take, for example,

\[
a_m=m,
\qquad
N_m=\lfloor\kappa m(a_m-1)\rfloor.
\tag{41}
\]

Then `log a_m=o(m)`, and monotonicity of `t_k` gives the matching upper estimate

\[
t_N
\le
\sum_{k=0}^{N}t_k
\le
(N+1)t_N.
\tag{42}
\]

Moreover (34) is the CDF of a negative-binomial random variable with mean

\[
\mu_m=m(a_m-1)
\tag{43}
\]

and variance

\[
\sigma_m^2=m a_m(a_m-1).
\tag{44}
\]

Since `N_m/kappa -> mu_m` and `kappa>1`, Chebyshev's inequality yields

\[
Q_{m,N_m,a_m}(1)\to1.
\tag{45}
\]

Hence for (41)

\[
\boxed{
\frac1m\log\|F_m\|_A
\to
w(\kappa)
=\kappa+1+\log\kappa.
}
\tag{46}
\]

Combining the sharp fixed-arc boundary with this matching slow-growth realization gives (7): one may choose any fixed `alpha<alpha_*(kappa)` and then let `alpha` approach the boundary from below.

A non-load-bearing numerical minimization of (7) places the minimum near

\[
\kappa\approx2.5614584264,
\qquad
\alpha_*(\kappa)\approx0.7111585218,
\tag{47}
\]

with

\[
C_{\infty,+}\approx6.3305649619.
\tag{48}
\]

The strict comparison with six below is analytic and does not depend on these decimals.

## 4. The entire finite-supercritical large-center branch lies above six

Set

\[
x:=\frac{1+\log\kappa}{\kappa},
\tag{49}
\]

so that

\[
h=\kappa(1-x),
\qquad
w=\kappa(1+x),
\tag{50}
\]

and

\[
\alpha_*
=
2\arctan\sqrt{\frac{1-x}{1+x}}
<
2\sqrt{\frac{1-x}{1+x}}.
\tag{51}
\]

Therefore `w/alpha_*>6` follows from

\[
w^3>144h.
\tag{52}
\]

Define

\[
R(\kappa):=w(\kappa)^3-144h(\kappa).
\tag{53}
\]

Then

\[
R'(\kappa)
=
\frac{3w^2(\kappa+1)-144(\kappa-1)}{\kappa}.
\tag{54}
\]

At a stationary point,

\[
w^2
=48\frac{\kappa-1}{\kappa+1},
\tag{55}
\]

and substitution into (53) gives

\[
R
=
96\left[
\frac{2\kappa+1}{\kappa+1}\log\kappa
-(\kappa-1)
\right].
\tag{56}
\]

The bracket in (56) is positive exactly when

\[
d(\kappa)
:=
\log\kappa-
\frac{\kappa^2-1}{2\kappa+1}
>0.
\tag{57}
\]

Its derivative is

\[
d'(\kappa)
=
-\frac{2\kappa^3-2\kappa^2-2\kappa-1}
{\kappa(2\kappa+1)^2}.
\tag{58}
\]

The numerator in (58) is strictly increasing for `kappa>1`, since its derivative is

\[
2(3\kappa+1)(\kappa-1)>0.
\tag{59}
\]

Thus `d'` changes sign at most once, from positive to negative, so on `[1,e]` the minimum of `d` is attained at an endpoint. Now

\[
d(1)=0,
\tag{60}
\]

while

\[
d(e)>0
\iff
e^2-2e-2<0
\iff
e<1+\sqrt3,
\tag{61}
\]

which follows from the elementary bound `e<2.72<1+sqrt(3)`. Hence every stationary point of `R` in `(1,e]` has `R>0`.

It remains to control `kappa>=e`. Put

\[
A(\kappa)
:=
w(\kappa)^2
-48\frac{\kappa-1}{\kappa+1}.
\tag{62}
\]

The sign of `R'` is the sign of `A`. For `kappa>=e`, `log kappa>=1`, so `w>=kappa+2` and

\[
A'(\kappa)
=
2w\left(1+\frac1\kappa\right)
-\frac{96}{(\kappa+1)^2}
\ge
2(\kappa+2)\left(1+\frac1\kappa\right)
-\frac{96}{(\kappa+1)^2}.
\tag{63}
\]

The right-hand side is increasing for `kappa>=2.7` because its derivative is

\[
2-\frac4{\kappa^2}+\frac{192}{(\kappa+1)^3}>0,
\tag{64}
\]

and at `kappa=2.7` it equals `1084691/184815>0`. Thus `A` is increasing on `[e,infinity)`. Also

\[
(e+1)A(e)
=e^3+5e^2-40e+52>0:
\tag{65}
\]

the polynomial on the right is increasing for `x>=2.7`, and at `x=2.7` it equals `133/1000>0`. Therefore `A>0` and hence `R'>0` for every `kappa>=e`.

Finally,

\[
R(1)=8>0,
\tag{66}
\]

`R` has no nonpositive interior stationary minimum on `(1,e]`, and it is strictly increasing after `e`. Therefore

\[
R(\kappa)>0
\qquad(\kappa>1),
\tag{67}
\]

which proves (52), and consequently

\[
\boxed{
\frac{\kappa+1+\log\kappa}
{\alpha_*(\kappa)}
>6
\qquad(\kappa>1).
}
\tag{68}
\]

This is the branch-pruning statement relevant to RE-218.

## 5. Falsification boundary

The result has several deliberate boundaries.

First, the theorem is **positive-real-center only**. RE-231 allowed a complex subcritical `kappa`, but the supercritical denominator saddle used here is positive and the exact Wiener comparison (33)--(35) uses `a>1`. Complex large centers with finite supercritical scaled depth are not classified by this finding.

Second, `kappa` is assumed to converge to a finite value. The regime `kappa_m->infinity` is not covered by the fixed-parameter Laplace normal form. Nothing here rules out a different scaling limit there, although (68) shows that no finite `kappa>1` approaches a cost below six.

Third, the exact transition arc

\[
\alpha=\alpha_*(\kappa)
\tag{69}
\]

is open. Equation (20) only gives zero exponential rate at the endpoint, so polynomial saddle prefactors decide whether boundary flatness survives.

Fourth, this remains a representation theorem for the truncated negative-binomial single-center predictor. It does not improve the universal separated lower bound `C_sep>=1`, does not prove `C_sep>=6`, and makes no claim about multi-center/minimax, rational predictors, or other bases. It also does not by itself realize the widening corridor with ordinary-prime `{0,1,2}` edits; increasing `N/m` changes the arithmetic support budget.

Finally, the numerical minimizer in (47)--(48) is orientation only. The durable comparison needed at the research frontier is the exact inequality (68).

## 6. Prior-art audit

A fresh search was made for uniform incomplete-beta / incomplete-Laplace saddle asymptotics, negative-binomial partial-sum transitions, large-center truncated negative-binomial prediction, and superoscillatory prediction costs. The nearest classical background remains Temme's incomplete-beta and incomplete-Laplace asymptotics and the general superoscillation literature. Those sources study the relevant asymptotic tools or generic out-of-band prediction cost, but the audit did not identify the predictor-specific fixed-arc boundary (4), the Wiener rate (6), or the strict six-plus branch floor (68).

No external theorem is load-bearing. Equations (17)--(20) use only the exact finite normalization inherited from RE-231 and the elementary Laplace principle; (33)--(46) use the exact coefficient sum, Stirling, and a negative-binomial variance bound; (68) is elementary calculus. No new `SOURCES.md` dependency is therefore required.

## 7. Consequence for the current frontier

RE-230 forced an unbounded center out of every fixed delay corridor. RE-231 then showed that widening at scaled depth `kappa=1` exactly removes the microscopic residual delay, but left open whether the widened branch could become globally useful. RE-232 resolves the finite-supercritical positive-real part of that question.

The answer has two sides. **Yes, widening genuinely works:** every finite `kappa>1` predicts exponentially well on each fixed arc below the explicit radius `alpha_*(kappa)`. But **it is too expensive for the current optimization problem:** its best possible normalized Wiener rate is strictly larger than six, while RE-218 already supplies a finite-center construction below six.

Thus sending a positive-real single center to infinity while widening the corridor proportionally is not a route to improve the current `5.996390` upper bound. The informative remaining single-center boundary is narrower: complex supercritical center drift, `kappa_m->infinity`, or the exact transition `alpha=alpha_*(kappa)`. For improving the separated Wiener constant itself, the stronger architectural alternatives remain multi-center/minimax or a different predictor representation.