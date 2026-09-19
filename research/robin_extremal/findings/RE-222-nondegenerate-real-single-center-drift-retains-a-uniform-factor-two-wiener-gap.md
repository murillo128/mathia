# RE-222 — Nondegenerate real single-center drift retains a uniform factor-two Wiener gap

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + EXACT-REMAINDER + COMPACT-PARAMETER-UNIFORMIZATION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-219, RE-221.

RE-221 shows that, for every **fixed** positive-real single-center triple `(alpha,a,lambda)`, exploiting the exact complex cancellation of the incomplete-beta remainder does not evade the factor-two Wiener floor. Its stated boundary deliberately leaves open parameters that drift with the prediction scale. RE-219 already handles arbitrary drift when the discarded negative-binomial tail is controlled termwise in absolute value, but it does not cover exact cancellation-sensitive truncation.

The fixed-parameter qualifier in RE-221 is not an escape by itself. On every compact subset of the interior contracting parameter domain, the RE-221 argument is locally uniform and in fact leaves a **strict uniform margin above two**. Hence any real single-center exact-remainder family that even approaches Wiener exponent two must drive at least one parameter to a genuine boundary or infinity; smooth bounded retuning inside the admissible interior cannot help.

Define

\[
\mathcal D
:=
\left\{
(\alpha,a,\lambda):
0<\alpha<\frac\pi2,\ a>0,\ \lambda>0,\
r(\alpha,a)<1
\right\},
\tag{1}
\]

where

\[
r(\alpha,a)
:=
\left|1-\frac{e^{-i\alpha}}a\right|
=
\frac{\sqrt{a^2+1-2a\cos\alpha}}a.
\tag{2}
\]

Let `K` be any compact subset of `D`. For integers `m -> infinity`, choose

\[
(\alpha_m,a_m,\lambda_m)\in K,
\qquad
\lambda_m:=\frac{N_m}{m},
\qquad N_m\in\mathbb Z_{\ge0},
\tag{3}
\]

and form the exact normalized single-center predictor

\[
Q_m(z)
:=
z^m a_m^{-m}
\sum_{k=0}^{N_m}
\binom{m+k-1}{k}
\left(1-\frac z{a_m}\right)^k,
\qquad
F_m(z):=\frac{Q_m(z)}{Q_m(1)}.
\tag{4}
\]

Assume the actual polynomials predict uniformly on their moving symmetric arcs,

\[
\sup_{|\theta|\le\alpha_m}
\left|F_m(e^{-i\theta})-1\right|
\longrightarrow0.
\tag{5}
\]

Then there is a constant `eta_K>0`, depending only on the compact parameter set, such that

\[
\boxed{
\liminf_{m\to\infty}
\frac{\log\|F_m\|_A}{m\alpha_m}
\ge 2+\eta_K.
}
\tag{6}
\]

In particular, under the RE-216 scaling `m alpha_m = HT+O(1)`, no cancellation-sensitive positive-real single-center family whose parameters stay nondegenerate can have leading Wiener rate at or below two.

This is still a representation-local theorem. It does not improve the global `C_sep >= 1` lower bound, and it does not settle families that approach the boundary of `D`, genuinely complex-center cancellation, several centers, minimax polynomials, rational predictors, or a different approximation basis.

## 1. The exact incomplete-beta identities survive moving parameters

The algebra in RE-221 is pointwise in the parameters. Differentiating the finite sum in (4) gives

\[
Q_m(z)
=
\frac{
\displaystyle\int_0^z
s^{m-1}\left(1-\frac{s}{a_m}\right)^{N_m}ds
}{
\displaystyle\int_0^1
s^{m-1}\left(1-\frac{s}{a_m}\right)^{N_m}ds
}
\cdot Q_m(1),
\tag{7}
\]

so after DC normalization

\[
F_m(z)
=
\frac{
\displaystyle\int_0^z
s^{m-1}\left(1-\frac{s}{a_m}\right)^{N_m}ds
}{D_m},
\qquad
D_m:=
\int_0^1
s^{m-1}\left(1-\frac{s}{a_m}\right)^{N_m}ds.
\tag{8}
\]

Along the unit circle,

\[
\frac{d}{d\theta}F_m(e^{-i\theta})
=
\frac{-i e^{-im\theta}
\left(1-e^{-i\theta}/a_m\right)^{N_m}}
{D_m}.
\tag{9}
\]

No absolute-tail estimate has entered. Because `K` is compact in the open domain (1), there are fixed positive margins from `alpha=0`, `alpha=pi/2`, `a=0`, `lambda=0`, and the contraction boundary `r=1`, while `a` and `lambda` are bounded above.

Take any subsequence. Compactness gives a further subsequence, not relabeled, such that

\[
(\alpha_m,a_m,\lambda_m)
\longrightarrow
(\alpha,a,\lambda)\in K.
\tag{10}
\]

Put

\[
r_m=r(\alpha_m,a_m),
\qquad
r_{0,m}:=\left|1-\frac1{a_m}\right|,
\tag{11}
\]

with limits `r` and `r_0`. Since the limiting arc has positive width,

\[
r>r_0.
\tag{12}
\]

This strict inequality is the key compact-interior separation that disappears only in a degenerate limit.

## 2. The endpoint-variation argument is locally uniform

The real denominator in (8) obeys

\[
|D_m|
\le
\int_0^1
s^{m-1}
\left|1-\frac{s}{a_m}\right|^{N_m}ds.
\tag{13}
\]

For a convergent parameter sequence as in (10), the elementary one-dimensional Laplace upper bound used in RE-221 is uniform in a small compact neighborhood of the limiting triple. At exponential scale its only possible candidates are the real endpoint

\[
f_{1,m}:=\lambda_m\log r_{0,m},
\tag{14}
\]

and, when

\[
s_{*,m}:=rac{a_m}{1+\lambda_m}<1,
\tag{15}
\]

the stationary value

\[
f_{*,m}
:=
\log a_m
+\lambda_m\log\lambda_m
-(1+\lambda_m)\log(1+\lambda_m).
\tag{16}
\]

Thus

\[
\frac1m\log|D_m|
\le
\max(f_{*,m},f_{1,m})+o(1)
\tag{17}
\]

when (15) holds, and the endpoint-only bound applies otherwise. The `o(1)` is uniform after restricting to the compact neighborhood selected by (10). This does not require a special-function asymptotic expansion: split `[0,1]` into the finitely many monotone branches of the logarithm of the absolute integrand and bound each integral by its supremum times a subexponential factor.

Now use (9) at the moving endpoint. Set

\[
h_m=m^{-2}.
\tag{18}
\]

Because `alpha_m` stays bounded away from zero and the endpoint factor `|1-e^{-i theta}/a_m|` stays bounded away from zero on `[alpha_m-h_m,alpha_m]`, the logarithmic derivative of the numerator in (9) is `O_K(m)` there. Across an interval of length `m^{-2}` its phase and modulus therefore change by `o(1)`, uniformly along the convergent subsequence. Consequently

\[
\left|
F_m(e^{-i\alpha_m})-
F_m(e^{-i(\alpha_m-h_m)})
\right|
=
(1+o(1))
\frac{h_m r_m^{N_m}}{|D_m|}.
\tag{19}
\]

Assumption (5) makes the left side tend to zero. Since `h_m=e^{o(m)}`, (17)--(19) imply at the limiting triple exactly the RE-221 endpoint inequality

\[
\lambda\log r
\le
\max(f_*,f_1),
\tag{20}
\]

with the endpoint-only analogue if the stationary point is unavailable, where

\[
f_1=\lambda\log r_0,
\qquad
f_*=\log a+\lambda\log\lambda-(1+\lambda)\log(1+\lambda).
\tag{21}
\]

But (12) gives

\[
\lambda\log r>f_1.
\tag{22}
\]

Hence the endpoint-only case is impossible, the stationary point must exist, and

\[
\lambda\log r\le f_*.
\tag{23}
\]

Equivalently,

\[
\tau_{\alpha,a}(\lambda)
:=-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log r
\le0.
\tag{24}
\]

The same concavity argument as RE-221 then places `lambda` on or beyond the unique upper root

\[
\lambda\ge\lambda_0(\alpha,a),
\qquad
\tau_{\alpha,a}(\lambda_0)=0,
\qquad
\lambda_0>\frac r{1-r}.
\tag{25}
\]

Thus parameter drift inside a compact interior set does not open a cancellation branch before the negative-binomial mode. Every convergent subsequence is forced onto the same upper truncation branch as the fixed-parameter theorem.

## 3. Compactness upgrades the strict fixed-parameter inequality to a uniform gap

The exact coefficient Wiener norm before DC normalization is

\[
A_m
=
a_m^{-m}
\sum_{k=0}^{N_m}
\binom{m+k-1}{k}
\left(1+\frac1{a_m}\right)^k.
\tag{26}
\]

Along (10), its logarithmic rate is

\[
\frac1m\log A_m
\longrightarrow
\nu_a(\lambda),
\tag{27}
\]

where

\[
\nu_a(\lambda)
:=-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log\frac{a+1}{a}.
\tag{28}
\]

The function `nu_a(lambda)` is strictly increasing in `lambda`. Exact DC normalization is exponentially harmless here as well. At `z=1`, the first omitted absolute-tail exponent differs from (24) by

\[
\lambda\log\frac{r_0}{r}<0.
\tag{29}
\]

Therefore (25) gives `Q_m(1)=1+O(e^{-cm})` along the convergent subsequence for some local `c>0` (and when `a=1`, `Q_m(1)=1` exactly). Hence

\[
\frac1m\log\|F_m\|_A
\longrightarrow
\nu_a(\lambda)
\ge
\nu_a(\lambda_0(\alpha,a)).
\tag{30}
\]

At the upper root, RE-219's exact one-variable geometry gives the strict pointwise inequality

\[
\nu_a(\lambda_0)
=
\lambda_0
\log\frac{(a+1)/a}{r}
>2\alpha.
\tag{31}
\]

The new point is to retain that strictness under parameter motion. Define

\[
G(\alpha,a)
:=
\frac{\nu_a(\lambda_0(\alpha,a))}{\alpha}-2.
\tag{32}
\]

Throughout the interior contracting domain, `G>0`. The upper root `lambda_0(alpha,a)` is continuous: `tau` is continuous in all variables, the upper root is unique, and its derivative in `lambda` is strictly negative there. Therefore `G` is continuous.

Let `P_K` be the projection of `K` onto the `(alpha,a)` coordinates. It is compact and remains inside the contracting interior, so

\[
\eta_K
:=
\min_{(\alpha,a)\in P_K}G(\alpha,a)
>0.
\tag{33}
\]

Every subsequential limit compatible with (5) therefore has Wiener exponent at least `2+eta_K`. Applying this to a subsequence realizing the liminf proves (6).

This is stronger than merely extending RE-221 from fixed to slowly varying parameters. **Even approaching exponent two is impossible while the real single-center geometry remains in a compact interior regime.** The gap can shrink to zero only by leaving every such compact set.

## 4. What an exact real single-center escape would now have to do

Suppose a cancellation-sensitive real single-center family had

\[
\liminf
\frac{\log\|F_m\|_A}{m\alpha_m}
\le2.
\tag{34}
\]

Then the triples `(alpha_m,a_m,N_m/m)` occurring along a low-cost subsequence cannot remain in any compact subset of `D`. At least one genuine degeneration must occur: the arc can collapse or approach its admissible edge, the center/contraction geometry can approach the boundary or infinity, or the truncation ratio can leave every fixed positive finite range. Equation (34) does **not** assert that any of those boundary regimes succeeds; it says only that all nondegenerate drift has now been excluded.

Combined with RE-219, the remaining loophole is narrower still. RE-219 already proves the factor-two floor for arbitrarily drifting positive-real parameters whenever the discarded series is certified in absolute value. Therefore a hypothetical sub-two real single-center construction must use **both** ingredients absent from the current lower bounds:

1. a genuinely degenerate asymptotic parameter regime; and
2. cancellation of the exact finite remainder that cannot be replaced by the RE-219 absolute-tail certificate.

Either ingredient alone is insufficient. This separates a real singular asymptotic problem from ordinary scalar retuning and makes it a much sharper target for any future attempt to improve the constructive side.

The global separated-prediction interval is unchanged:

\[
1\le C_{\rm sep}\le5.996390.
\tag{35}
\]

The theorem remains about one representation class before ordinary-prime realization; no new source-capacity statement follows from it.

## 5. Prior art and falsification boundary

Uniform asymptotics for incomplete beta functions with varying parameters are classical. Temme developed uniform incomplete-beta asymptotics in the 1970s and 1980s, including *Uniform asymptotic expansions of the incomplete gamma functions and the incomplete beta function* (Math. Comp. 29, 1975) and *Incomplete Laplace integrals: uniform asymptotic expansion with application to the incomplete beta function* (SIAM J. Math. Anal. 18, 1987). Nemes and Olde Daalhuis later gave a remainder-controlled uniform expansion in *Uniform Asymptotic Expansion for the Incomplete Beta Function* (SIGMA 12, 2016, 101).

No novelty is claimed for uniform incomplete-beta asymptotics, and none of those results is load-bearing here. The proof above uses only the exact finite-polynomial identities already established in RE-221, an elementary locally uniform Laplace upper bound, subsequential compactness, and the strict RE-219 geometric inequality. No `SOURCES.md` update is therefore required.

Several falsification boundaries are essential. Compact interior control is the theorem: it does not cover a sequence whose parameters genuinely approach the boundary of `D` or infinity. A complex center changes the exact integration path and phase geometry, so RE-220's radialization of absolute tails does not promote this result to exact complex cancellation. Several centers can cancel after coefficient recombination and remain outside the argument. Finally, a global lower bound above `C_sep=1` would require information about arbitrary separated measures, not this single-center representation.

## Research consequence

RE-221 left `asymptotically drifting/degenerate single-center parameters` as one combined escape. RE-222 separates those words: **drift without degeneration does not help**. On every compact admissible real single-center parameter family, exact cancellation pays not merely two but `2+eta_K` for some fixed positive margin.

The only real single-center exact-remainder regime still capable of changing the factor-two story is therefore a singular boundary regime. That regime must be analyzed together with the RE-208 interface, because collapsing arc width, weak contraction, diverging center or extreme truncation depth can also change shell count, spacing and ordinary-prime realization costs. Outside that singular route, a serious reduction of the current `5.996390` upper bound still requires genuinely different geometry such as multi-center/minimax prediction, another basis, or genuinely complex-center cancellation.
