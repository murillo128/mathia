# RE-234 — Finite-ray complex large centers retain the six-plus Wiener floor

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-DRIFT + WIDENING-CORRIDOR + FINITE-RAY-NORMAL-FORM + WIENER-COST + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-218, RE-220, RE-228, RE-230, RE-232.

RE-230 left one genuinely different unbounded-complex-center regime open. If the truncation depth grows only sublinearly relative to `m|a|`, the normalized predictor reverts microscopically to the raw delay and fails. But a complex center could still be sent to infinity while widening the delay corridor at the same rate as its modulus. RE-232 showed that the positive-real version of that finite-supercritical regime really predicts fixed arcs, at a normalized Wiener cost strictly above six. The remaining question is whether a drifting complex phase can reduce that cost.

It cannot in the finite-ray regime.

Consider the exact normalized truncated negative-binomial predictor

\[
Q_{m,N,a}(z)
:=z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)}.
\tag{1}
\]

Let

\[
a_m=\rho_m e^{i\varphi_m},
\qquad
\rho_m\to\infty,
\qquad
\varphi_m\to\varphi,
\qquad
\frac{N_m}{m\rho_m}\to\tau\in(0,\infty),
\tag{2}
\]

along a phase-convergent subsequence. Fix `alpha>0`, assume eventual contraction on the symmetric arc,

\[
\max_{|\theta|\le\alpha}
\left|1-\frac{e^{-i\theta}}{a_m}\right|<1,
\tag{3}
\]

and suppose

\[
\sup_{|\theta|\le\alpha}
|F_m(e^{-i\theta})-1|\to0.
\tag{4}
\]

Contraction at the two endpoints implies, in the limit,

\[
\cos(\varphi+\alpha)\ge0,
\qquad
\cos(\varphi-\alpha)\ge0.
\tag{5}
\]

Hence

\[
c:=\cos\varphi>0.
\tag{6}
\]

Define the effective radial load

\[
\boxed{x:=\tau c.}
\tag{7}
\]

Then every successful family satisfying (2)--(4) obeys

\[
\boxed{x>1}
\tag{8}
\]

and the necessary macroscopic arc restriction

\[
\boxed{
x\cos\alpha\ge1+\log x.
}
\tag{9}
\]

Equivalently,

\[
\boxed{
\alpha\le
\alpha_*(x)
:=
\arccos\!\left(\frac{1+\log x}{x}\right).
}
\tag{10}
\]

Moreover the exact normalized Wiener norm satisfies

\[
\boxed{
\liminf_{m\to\infty}
\frac1m\log\|F_m\|_A
\ge
\tau+1+\log x
\ge
x+1+\log x.
}
\tag{11}
\]

Combining (10)--(11) with the one-variable inequality proved in RE-232 gives

\[
\boxed{
\liminf_{m\to\infty}
\frac{\log\|F_m\|_A}{m\alpha}
\ge
\frac{x+1+\log x}{\alpha_*(x)}
>6.
}
\tag{12}
\]

Thus a complex phase does not rescue the finite-ray large-center branch. The positive-real geometry from RE-232 is already the cheapest possible radialization of this regime, and even it is strictly more expensive than the certified finite-center construction of RE-218 with exponent `5.996390`.

## 1. The denominator sees only the effective radial load

The exact derivative identity from RE-221 is

\[
\frac{d}{d\theta}F_m(e^{-i\theta})
=
\frac{-i e^{-im\theta}
\left(1-e^{-i\theta}/a_m\right)^{N_m}}
{D_m},
\tag{13}
\]

where

\[
D_m
:=
\int_0^1
s^{m-1}
\left(1-\frac{s}{a_m}\right)^{N_m}ds.
\tag{14}
\]

Uniformly for `s in [0,1]`,

\[
\log\left|1-\frac{s}{a_m}\right|
=
-\frac{s\cos\varphi_m}{\rho_m}
+O(\rho_m^{-2}).
\tag{15}
\]

Because `N_m/(m rho_m) -> tau`, (15) gives

\[
\frac{N_m}{m}
\log\left|1-\frac{s}{a_m}\right|
\to-xs
\tag{16}
\]

uniformly in `s`. Therefore

\[
\limsup_{m\to\infty}
\frac1m\log|D_m|
\le d(x),
\tag{17}
\]

where the elementary maximization of `log s-xs` on `[0,1]` gives

\[
d(x)=
\begin{cases}
-x,&0<x\le1,\\[3pt]
-1-\log x,&x>1.
\end{cases}
\tag{18}
\]

No incomplete-beta asymptotic theorem is needed for this bound.

For every fixed `theta`, the numerator in (13) satisfies

\[
\frac{N_m}{m}
\log\left|1-\frac{e^{-i\theta}}{a_m}\right|
\to
-\tau\cos(\theta+\varphi).
\tag{19}
\]

Hence

\[
\liminf_{m\to\infty}
\frac1m
\log\left|
\frac{d}{d\theta}F_m(e^{-i\theta})
\right|
\ge
R_x(\theta),
\tag{20}
\]

with

\[
R_x(\theta)=
\begin{cases}
x-\tau\cos(\theta+\varphi),&0<x\le1,\\[3pt]
1+\log x-\tau\cos(\theta+\varphi),&x>1.
\end{cases}
\tag{21}
\]

The symmetric arc now removes the apparent phase advantage. Since

\[
\frac{
\cos(\varphi+\alpha)+
\cos(\varphi-\alpha)}2
=c\cos\alpha,
\tag{22}
\]

at least one endpoint `sigma alpha`, `sigma in {+1,-1}`, satisfies

\[
\cos(\varphi+\sigma\alpha)
\le c\cos\alpha.
\tag{23}
\]

If `x<=1`, (20)--(23) give the strictly positive endpoint exponent

\[
R_x(\sigma\alpha)
\ge x(1-\cos\alpha)>0.
\tag{24}
\]

If `x>1` but

\[
1+\log x>x\cos\alpha,
\tag{25}
\]

then the same endpoint has

\[
R_x(\sigma\alpha)>0.
\tag{26}
\]

Either case contradicts flat prediction.

To make that contradiction independent of any pointwise derivative pathology, differentiate the numerator logarithmically. On a fixed arc,

\[
\frac{d}{d\theta}
\log\left[
e^{-im\theta}
\left(1-\frac{e^{-i\theta}}{a_m}\right)^{N_m}
\right]
=
-im+
N_m\frac{i e^{-i\theta}}{a_m-e^{-i\theta}}
=O(m),
\tag{27}
\]

because `N_m/rho_m=O(m)`. If (20) is positive at an endpoint, move a fixed arbitrarily small distance into the arc if necessary. On an interval of width `delta/m`, with `delta>0` sufficiently small, the derivative magnitude remains exponentially large while its phase rotates by less than a fixed acute angle. Integrating (13) there produces exponentially large variation of `F_m`, incompatible with (4).

Thus (8)--(10) are necessary.

## 2. Complex DC cancellation cannot discount the Wiener norm

Write

\[
S_{m,N}(s)
:=
\sum_{k=0}^{N}
\binom{m+k-1}{k}s^k.
\tag{28}
\]

As in RE-220, the phase of a complex center factors degree by degree after re-expanding `Q`. Therefore the Wiener norm is exact:

\[
\boxed{
\|Q_{m,N,a}\|_A
=
\rho^{-m}
S_{m,N}\!\left(1+\frac1\rho\right).
}
\tag{29}
\]

Set

\[
s_m:=1+\frac1{\rho_m},
\qquad
w_k:=\binom{m+k-1}{k}s_m^k.
\tag{30}
\]

The last `L_m=floor(rho_m)` terms of the sum in (29) are all within a fixed multiplicative factor of `w_{N_m}`. Indeed

\[
\frac{w_{k-1}}{w_k}
=
\frac{k}{(m+k-1)s_m}
=1-O(\rho_m^{-1})
\tag{31}
\]

uniformly for `N_m-L_m<=k<=N_m`, since `N_m/(m rho_m)->tau>0`. Hence

\[
S_{m,N_m}(s_m)
\ge e^{-O(1)}\rho_m
\binom{m+N_m-1}{N_m}s_m^{N_m}.
\tag{32}
\]

Also

\[
\binom{m+N_m-1}{N_m}
=
\prod_{j=1}^{m-1}
\frac{N_m+j}{j}
\ge
\frac{N_m^{m-1}}{(m-1)!}.
\tag{33}
\]

Combining (29), (32), (33), Stirling, and

\[
\frac{N_m}{m}\log\left(1+\frac1{\rho_m}\right)
\to\tau,
\tag{34}
\]

gives the growth bound that remains valid even for extremely fast center growth:

\[
\boxed{
\liminf_{m\to\infty}
\frac1m\log\|Q_m\|_A
\ge
\tau+1+\log\tau.
}
\tag{35}
\]

It remains to price the exact DC normalization. Put

\[
q_m:=\left|1-\frac1{a_m}\right|.
\tag{36}
\]

Contraction at `theta=0` gives `q_m<1`. Therefore

\[
|Q_m(1)|
\le
\rho_m^{-m}S_{m,N_m}(q_m)
\le
\rho_m^{-m}(1-q_m)^{-m}.
\tag{37}
\]

Since

\[
q_m^2
=
1-\frac{2\cos\varphi_m}{\rho_m}
+\frac1{\rho_m^2},
\tag{38}
\]

we have

\[
\rho_m(1-q_m)
=
\frac{2\cos\varphi_m-1/\rho_m}{1+q_m}
\to c.
\tag{39}
\]

Thus

\[
\limsup_{m\to\infty}
\frac1m\log|Q_m(1)|
\le-\log c.
\tag{40}
\]

Dividing (35) by the exact normalizer and using `x=tau c` yields

\[
\liminf_{m\to\infty}
\frac1m\log\|F_m\|_A
\ge
\tau+1+\log\tau+\log c
=
\tau+1+\log x.
\tag{41}
\]

Since `0<c<=1`, `tau=x/c>=x`, and therefore

\[
\boxed{
\liminf_{m\to\infty}
\frac1m\log\|F_m\|_A
\ge x+1+\log x.
}
\tag{42}
\]

Any destructive phase cancellation in `Q_m(1)` only makes the exact normalized Wiener norm larger, not smaller.

## 3. The positive-real ray is already the cheapest finite ray

Prediction forces `x>1` and `alpha<=alpha_*(x)`. Hence (42) gives

\[
\liminf_{m\to\infty}
\frac{\log\|F_m\|_A}{m\alpha}
\ge
\frac{x+1+\log x}{\alpha_*(x)}.
\tag{43}
\]

RE-232 proved, by an elementary one-variable inequality, that

\[
\frac{x+1+\log x}
{\arccos((1+\log x)/x)}
>6
\qquad(x>1).
\tag{44}
\]

Therefore every successful finite-ray complex large-center family covered here has normalized Wiener rate strictly above six.

The mechanism is transparent. A phase tilt replaces the predictive load `tau` by the smaller radial component `x=tau cos(phi)`, but the coefficient norm still pays the full `tau`. After expressing the admissible arc through `x`, one has `tau>=x`, so phase can only increase the cost relative to the positive-real ray. Complexification creates no hidden discount.

This does **not** change the global separated-predictor interval

\[
1\le C_{\rm sep}\le5.996390.
\tag{45}
\]

The lower endpoint remains the representation-independent obstruction of RE-217, while the upper endpoint remains the explicit finite-center construction of RE-218. Equation (44) only removes another single-center large-center escape route.

## 4. Falsification boundary and remaining escape routes

The hypotheses used above are deliberate.

- The ray load is finite and positive: `N_m/(m|a_m|)->tau in (0,infty)`. RE-230 already treats the subcritical `tau->0` direction in the corresponding microscopic sense, while `tau->infty` is not covered here.
- The observed arc is fixed and symmetric. Shrinking or scale-dependent arcs require a different normalization.
- Eventual contraction is assumed. It is what places the limiting complex ray in the right half-plane and gives `q_m<1` for the DC estimate.
- The proof is for the truncated negative-binomial **single-center** representation. It says nothing by itself about multi-center/minimax constructions, rational predictors, or another polynomial basis.
- The equality case `alpha=alpha_*(x)` is only a necessary boundary here; no sufficiency or transition profile is asserted.
- This is a Wiener-cost obstruction for the continuum separated predictor. It is not a new direct theorem about the final `{0,1,2}` prime-edit realization.

The phase-convergence assumption loses no genuine drifting-phase family: every phase sequence has a convergent subsequence, and uniform prediction would persist on that subsequence. Thus a successful finite-ray family cannot evade the obstruction merely by rotating its center without settling to one phase.

The most interesting single-center regime left by this chain is therefore the **super-broad** complex large-center limit `N/(m|a|)->infinity`, if one is willing to let the delay corridor broaden without bound. For the fixed-corridor Robin realization, however, that direction is already structurally remote. Architectures that change the geometry — especially multi-center/minimax or rational prediction — remain the more credible route toward improving the `5.996390` construction.

## 5. Prior-art audit

A global search was made for complex-parameter incomplete-beta asymptotics, truncated negative-binomial asymptotics with moving complex parameters, and complex-frequency/superoscillatory exponential-polynomial cost bounds. The relevant literature still provides the expected classical context: uniform incomplete-beta/Laplace asymptotics and general exponential dynamic-range costs for superoscillation. I did not find a result giving the finite-ray reduction `x=tau cos(phi)`, the exact complex-center Wiener comparison above, or the resulting six-plus obstruction for this predictor.

No external theorem is load-bearing in the argument: (17) is an elementary Laplace upper bound, (29) is the exact coefficient identity already established in the local line, and the final one-variable inequality is inherited from RE-232. Therefore `SOURCES.md` needs no new dependency entry.

## Conclusion

Within finite positive ray load, sending a single center to complex infinity cannot undercut the positive-real large-center cost. Uniform prediction forces the radialized load `x=tau cos(phi)` into exactly the same macroscopic admissibility geometry as RE-232, while the Wiener norm continues to pay the full `tau`. The resulting normalized cost is strictly above six.

So complex phase closes no part of the gap between the current universal lower bound `1` and the explicit upper bound `5.996390`; it only makes the large-center single-center branch more expensive. A real improvement now has to come from a genuinely different geometry, or from a still-unclassified super-broad singular limit outside the finite-ray regime.