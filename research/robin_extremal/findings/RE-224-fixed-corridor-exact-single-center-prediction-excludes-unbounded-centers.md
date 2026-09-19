# RE-224 — Fixed-corridor exact single-center prediction excludes unbounded real centers

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + EXACT-REMAINDER + ENDPOINT-LAPLACE-BOUND + FIXED-CORRIDOR-LOCALIZATION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-221, RE-222, RE-223.

RE-222 shows that a positive-real single-center predictor can approach the factor-two Wiener boundary only by leaving every compact subset of its contracting parameter domain. RE-223 then removes the collapsing-truncation direction in a fixed repair corridor. Two further apparent escapes remained coupled together in the wording of the frontier: perhaps the real expansion center could run to infinity, or equivalently the observed arc could approach its upper admissible edge while the truncation ratio stayed bounded.

Neither is possible for an exact normalized single-center predictor in a fixed corridor. The point is independent of the absolute-tail certificate. Before any asymptotic incomplete-beta machinery is used, uniform prediction near `theta=0` forces the real center to stay below the truncation scale.

Let

\[
Q_{m,N,a}(z)
:=
z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)},
\tag{1}
\]

with `m>=2`, `N>=0` and `a>1`. Suppose `alpha_m>0`, `m alpha_m -> infinity`, and

\[
\epsilon_m
:=
\sup_{|\theta|\le\alpha_m}
\left|F_{m,N_m,a_m}(e^{-i\theta})-1\right|
\longrightarrow0.
\tag{2}
\]

Put

\[
C_m:=(m-1)-\frac{N_m}{a_m-1},
\qquad
L_m:=m+\frac{N_m}{a_m-1}.
\tag{3}
\]

Then, whenever `C_m>0`, one has for all sufficiently large `m`

\[
\boxed{
\epsilon_m
\ge
\frac{\log(3/2)}{2}
\frac{C_m}{L_m}.
}
\tag{4}
\]

Consequently every uniformly predicting family satisfies

\[
\boxed{
\frac{\bigl((m-1)-N_m/(a_m-1)\bigr)_+}
{m+N_m/(a_m-1)}
\longrightarrow0.
}
\tag{5}
\]

In particular, if the truncation ratios `lambda_m=N_m/m` are bounded above, then

\[
\boxed{
\limsup a_m
\le
1+\limsup\lambda_m.
}
\tag{6}
\]

Thus an exact real single-center predictor whose delay support remains in one fixed multiplicative corridor cannot send its expansion center to infinity. Combined with the contraction condition `r(alpha,a)<1`, equation (6) also keeps the arc uniformly away from `pi/2`.

For the factor-two frontier this has a sharper consequence. RE-223 bounds `lambda_m` away from zero for every fixed-corridor family whose normalized Wiener rate is at most two, while the corridor itself bounds `lambda_m` above. Equation (6) now bounds the center above, and contraction already bounds it below. Therefore, after RE-222, **only two real single-center degeneracies remain in a fixed corridor:**

\[
\boxed{
\alpha_m\to0
\quad\text{or}\quad
r(\alpha_m,a_m)\to1
}
\tag{7}
\]

along any subsequence that could approach Wiener rate two. Unbounded centers, `alpha_m -> pi/2`, `lambda_m -> 0`, and ordinary nondegenerate retuning are all excluded by RE-222--RE-224.

This is still a representation-local statement. It does not improve the global `C_sep>=1` theorem, and it does not exclude broad-corridor families with `lambda_m->infinity`, genuinely complex centers, several centers, minimax predictors or another basis.

## 1. The exact incomplete-beta derivative gives a local flatness test

For `a>1`, the integral identity from RE-221 has a positive real denominator:

\[
F_{m,N,a}(z)
=
\frac{
\displaystyle\int_0^z
s^{m-1}\left(1-\frac sa\right)^N ds
}{
\displaystyle D_{m,N,a}},
\qquad
D_{m,N,a}
:=
\int_0^1
s^{m-1}\left(1-\frac sa\right)^N ds>0.
\tag{8}
\]

Along `z=e^{-i theta}`,

\[
\frac{d}{d\theta}F_{m,N,a}(e^{-i\theta})
=
\frac{-iV(\theta)}{D_{m,N,a}},
\tag{9}
\]

where

\[
V(\theta)
:=
e^{-im\theta}
\left(1-\frac{e^{-i\theta}}a\right)^N.
\tag{10}
\]

At the center of the observed arc,

\[
V(0)=\left(1-\frac1a\right)^N=:b^N,
\qquad b=\frac{a-1}{a}>0.
\tag{11}
\]

The logarithmic derivative of `V` obeys the elementary uniform bound

\[
\left|\frac{d}{d\theta}\log V(\theta)\right|
\le
m+\frac{N}{|a-e^{-i\theta}|}
\le
m+\frac{N}{a-1}
=L_m.
\tag{12}
\]

No remainder estimate has appeared: this is the derivative of the exact finite polynomial after normalization.

Choose

\[
\eta:=\log\frac32,
\qquad
h_m:=\frac{\eta}{L_m}.
\tag{13}
\]

Because `L_m>=m` and `m alpha_m -> infinity`, one has `h_m<alpha_m` for all sufficiently large `m`. Integrating (12) along `[0,h_m]` gives

\[
\left|\frac{V(\theta)}{V(0)}-1\right|
\le e^\eta-1
=\frac12.
\tag{14}
\]

Hence the exact derivative cannot cancel itself on this microscopic interval:

\[
\left|
\int_0^{h_m}V(\theta)d\theta
\right|
\ge
\frac12 h_m V(0).
\tag{15}
\]

Since `F(1)=1` exactly, equations (9) and (15) yield

\[
\epsilon_m
\ge
\left|F(e^{-ih_m})-F(1)\right|
\ge
\frac{\eta}{2L_m}
\frac{b^N}{D_{m,N,a}}.
\tag{16}
\]

The remaining issue is therefore purely the real endpoint size of `D`.

## 2. An endpoint Laplace bound forces the center below the truncation scale

Set `y=1-s` in (8). After dividing by `b^N`,

\[
\frac{D_{m,N,a}}{b^N}
=
\int_0^1
(1-y)^{m-1}
\left(1+\frac{y}{a-1}\right)^Ndy.
\tag{17}
\]

Using only `log(1-y)<=-y` and `log(1+x)<=x`,

\[
\frac{D_{m,N,a}}{b^N}
\le
\int_0^1
\exp\left(
-\left[(m-1)-\frac{N}{a-1}\right]y
\right)dy.
\tag{18}
\]

If `C_m>0`, this is at most `1/C_m`, so

\[
\frac{b^N}{D_{m,N,a}}
\ge C_m.
\tag{19}
\]

Substitution into (16) proves the nonasymptotic estimate (4). Therefore vanishing uniform prediction error forces (5).

The geometry of (5) is simple. The quantity `N/(a-1)` is the amount by which the truncation can offset the order-`m` endpoint slope of the incomplete-beta integrand. If it remains a fixed fraction below `m`, the normalized polynomial changes by a fixed amount already on a time scale `Theta(1/m)`, which lies inside every arc satisfying `m alpha_m -> infinity`. Exact cancellation farther out on the arc cannot repair this local failure.

Now assume

\[
\Lambda:=\limsup\frac{N_m}{m}<\infty.
\tag{20}
\]

If (6) failed, some subsequence would satisfy `a_m-1>=Lambda+delta` for a fixed `delta>0`. Along that subsequence,

\[
\frac{N_m}{a_m-1}
\le
\frac{\Lambda+o(1)}{\Lambda+\delta}m,
\tag{21}
\]

and therefore the ratio in (5) would stay bounded below by a positive constant. This contradicts (2), proving (6).

Notice that this argument does not say that `a-1<=lambda` is sufficient for prediction. It is only a necessary localization. Near the transition `a-1=lambda`, or on the interior-stationary side, the endpoint bound deliberately stops deciding the problem; those are precisely the regimes where incomplete-beta saddle geometry and exact cancellation can matter.

## 3. Fixed-corridor rate-two escape reduces to two singular geometries

In the RE-216 parameterization,

\[
\delta_m=\frac{\alpha_m}{T_m},
\qquad
m\delta_m=H+o(1),
\tag{22}
\]

and the polynomial delays are

\[
L_j=(m+j)\delta_m,
\qquad 0\le j\le N_m.
\tag{23}
\]

Thus a fixed delay corridor `[H,RH+o(H)]` gives

\[
\lambda_m:=\frac{N_m}{m}
\le R-1+o(1).
\tag{24}
\]

Equation (6) then yields

\[
\limsup a_m\le R.
\tag{25}
\]

The contraction condition for the single real center is

\[
r(\alpha,a)^2
=1+\frac1{a^2}-\frac{2\cos\alpha}{a}<1,
\tag{26}
\]

which is equivalent to

\[
a>\frac1{2\cos\alpha}.
\tag{27}
\]

Together with (25), this keeps the upper arc edge away from `pi/2`:

\[
\limsup\alpha_m
\le
\arccos\frac1{2R}
<\frac\pi2.
\tag{28}
\]

Now restrict to a subsequence whose normalized Wiener rate is at most two. RE-223 implies

\[
\liminf\lambda_m
\ge
0.06242231801357475\ldots .
\tag{29}
\]

Hence `lambda_m` lies in a compact positive interval, `a_m` is bounded above by (25) and below by (27), and `alpha_m` is bounded away from `pi/2` by (28). If both `alpha_m` were bounded away from zero and `r(alpha_m,a_m)` bounded away from one, the triples `(alpha_m,a_m,lambda_m)` would lie in a compact subset of the interior domain used by RE-222. RE-222 would then force a uniform Wiener gap strictly above two, contradicting the chosen subsequence.

This proves (7). The earlier list of possible real single-center degeneracies has therefore collapsed to two genuinely singular geometries: a vanishing observed arc, or approach to the contraction boundary. A future exact-remainder analysis no longer needs to treat center escape, the upper arc endpoint, or truncation collapse as independent possibilities in the fixed-corridor problem.

## 4. Prior-art boundary and adversarial checks

Endpoint/saddle transitions for incomplete beta functions are classical. Temme's uniform incomplete-beta asymptotics, including *Uniform asymptotic expansions of the incomplete gamma functions and the incomplete beta function* (Math. Comp. 29, 1975) and *Incomplete Laplace integrals: uniform asymptotic expansion with application to the incomplete beta function* (SIAM J. Math. Anal. 18, 1987), treat precisely the broader class of moving endpoint and saddle regimes. Nemes and Olde Daalhuis, *Uniform Asymptotic Expansion for the Incomplete Beta Function* (SIGMA 12, 2016, 101), supplies later remainder-controlled uniform expansions. Band-limited prediction by difference/Newton methods is likewise classical.

None of those results is load-bearing here. Equations (8)--(19) use only the exact finite-polynomial identity already established in RE-221, two elementary logarithmic inequalities, and a microscopic interval on which the exact derivative has controlled phase. No `SOURCES.md` update is required. The line-specific content is the consequence for the singular frontier left by RE-222--RE-223.

Several boundaries are essential. The core estimate assumes a positive real center `a>1`; centers `a<=1` are already bounded and therefore need no exclusion for the stated corollary. The condition `m alpha_m -> infinity` is necessary to fit the `Theta(1/m)` test interval inside the observed arc and is exactly the expanding-window regime of the continuum problem. Equation (4) gives no obstruction once `N/(a-1)` reaches the endpoint-saddle transition; this is deliberate rather than a proof gap. If `lambda_m` itself tends to infinity, an unbounded center can scale with it and the fixed-corridor conclusion no longer applies. Complex centers change positivity of `D` and remain outside the theorem, as do multi-center and non-binomial predictors.

Finally, (7) is not a universal factor-two theorem. It says that **within the fixed-corridor positive-real single-center representation**, every putative rate-two exact-cancellation escape must concentrate on one of two boundary geometries. The global separated-prediction interval remains

\[
1\le C_{\rm sep}\le5.996390.
\tag{30}
\]

## Research consequence

RE-222 left several boundary directions after eliminating nondegenerate drift, and RE-223 removed `lambda->0`. RE-224 removes two more without invoking an absolute-tail certificate: a fixed-corridor exact predictor cannot send its real center to infinity, and the contraction condition then prevents `alpha->pi/2`.

The real single-center exact-remainder problem is now localized to **`alpha->0` or `r->1`**. Those two limits can interact, but they are much more specific than generic parameter degeneration. A useful next test is therefore to derive a uniform incomplete-beta normal form in these two regimes and decide whether genuine cancellation can keep the Wiener rate at or below two. If not, the entire fixed-corridor positive-real single-center route to the global unit floor is closed, leaving complex cancellation, multi-center/minimax geometry or a different predictor basis as the live constructive alternatives.