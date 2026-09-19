# RE-225 — Fixed-corridor contraction-boundary escape forces a vanishing arc

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + EXACT-REMAINDER + FIXED-CORRIDOR-LOCALIZATION + CONTRACTION-BOUNDARY-EXCLUSION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-221--RE-224.

RE-222 reduces every putative factor-two positive-real single-center escape to the boundary of parameter space. RE-223 excludes truncation collapse in a fixed delay corridor, and RE-224 excludes unbounded centers and the upper arc edge. The remaining frontier was therefore stated as two singular geometries: either the observed arc shrinks, `alpha_m -> 0`, or the endpoint contraction deteriorates, `r(alpha_m,a_m) -> 1`.

Those are not independent. In a fixed corridor, once the truncation ratio stays bounded away from zero, **exact uniform prediction cannot approach the contraction boundary while the observed arc has a fixed positive width**. Thus every factor-two candidate in the real single-center architecture must in fact enter the vanishing-arc regime.

Use the exact normalized polynomial from RE-221--RE-224,

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

and put

\[
r(\alpha,a)
:=
\left|1-\frac{e^{-i\alpha}}a\right|.
\tag{2}
\]

Suppose a family satisfies

\[
0<\alpha_m<\frac\pi2,
\qquad
r_m:=r(\alpha_m,a_m)<1,
\qquad
m\alpha_m\to\infty,
\tag{3}
\]

and

\[
\epsilon_m
:=
\sup_{|\theta|\le\alpha_m}
\left|F_{m,N_m,a_m}(e^{-i\theta})-1\right|
\longrightarrow0.
\tag{4}
\]

Write

\[
\lambda_m:=\frac{N_m}{m}.
\tag{5}
\]

Assume the truncation ratios remain in one compact positive interval,

\[
0<\lambda_-\le\lambda_m\le\Lambda<\infty.
\tag{6}
\]

Then for every fixed `alpha_0>0`,

\[
\boxed{
\limsup_{\substack{m\to\infty\\ \alpha_m\ge\alpha_0}} r_m<1.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
r_m\to1\quad\Longrightarrow\quad\alpha_m\to0
}
\tag{8}
\]

along every subsequence satisfying (3)--(6).

The consequence for the factor-two frontier is immediate. In a fixed delay corridor, RE-223 supplies a positive lower bound for `lambda_m` on every subsequence whose normalized Wiener rate is at most two, while the corridor supplies the upper bound. RE-224 bounds the center and keeps the upper arc edge away from `pi/2`. If `alpha_m` were also bounded away from zero, (7) would keep `r_m` away from one, placing the parameters in a compact interior region. RE-222 would then force a uniform Wiener gap strictly above two. Hence

\[
\boxed{
\liminf\frac{\log\|F_m\|_A}{m\alpha_m}\le2
\quad\Longrightarrow\quad
\alpha_m\to0
}
\tag{9}
\]

along the subsequence realizing that liminf, within the fixed-corridor positive-real single-center architecture.

This still does not improve the global `C_sep >= 1` theorem. It is a representation-local localization result: the only remaining real single-center route to the factor-two boundary is now the **vanishing-arc singular limit**. If `r_m -> 1` occurs inside that limit, then from

\[
1-r_m^2
=
\frac{2a_m\cos\alpha_m-1}{a_m^2}
\tag{10}
\]

and boundedness of the center one further gets `a_m -> 1/2`. Thus the contraction-boundary subcase collapses into the corner `(alpha,a) -> (0,1/2)` rather than defining a second independent escape.

## 1. RE-224 localizes the real center relative to the truncation ratio

For `a_m>1`, RE-224 proves the exact necessary condition

\[
\frac{
\left((m-1)-N_m/(a_m-1)\right)_+
}{
m+N_m/(a_m-1)
}
\longrightarrow0.
\tag{11}
\]

Together with `lambda_m` in the compact interval (6), this gives the stronger pointwise localization

\[
\boxed{
a_m\le1+\lambda_m+o(1)}
\tag{12}
\]

on the subsequence `a_m>1`.

Indeed RE-224 already gives `limsup a_m <= 1+Lambda`, so `a_m-1` is bounded. If `(a_m-1)-lambda_m` stayed above a fixed positive number along a subsequence, the ratio in (11) would stay bounded below by a positive constant. This contradicts (11). If the numerator in (11) is nonpositive, (12) is immediate up to the harmless `m/(m-1)` correction.

No analogous localization is needed when `a_m<=1`; the contraction inequality itself will be enough there.

## 2. Away from a vanishing arc the real normalization denominator is exponentially small

The exact integral representation from RE-221 is

\[
F_{m,N,a}(z)
=
\frac{
\displaystyle\int_0^z
s^{m-1}\left(1-\frac sa\right)^Nds
}{
\displaystyle D_{m,N,a}
},
\qquad
D_{m,N,a}
:=
\int_0^1
s^{m-1}\left(1-\frac sa\right)^Nds.
\tag{13}
\]

Assume for contradiction that along a subsequence

\[
\alpha_m\ge\alpha_0>0,
\qquad
r_m\to1.
\tag{14}
\]

We first show that there is a fixed `c>0` such that

\[
\boxed{|D_{m,N_m,a_m}|\le e^{-cm}}
\tag{15}
\]

for all sufficiently large indices of this subsequence.

### The branch `a_m >= 1`

For `a>=1` the integrand in (13) is nonnegative. Substituting `s=au` and extending the upper endpoint from `1/a` to `1` gives the elementary complete-beta bound

\[
0<D_{m,N,a}
\le
 a^m B(m,N+1).
\tag{16}
\]

Uniform Stirling on the compact interval (6) gives

\[
\frac1m\log\!\left(a_m^m B(m,N_m+1)\right)
=
\log a_m
+\lambda_m\log\lambda_m
-(1+\lambda_m)\log(1+\lambda_m)
+o(1).
\tag{17}
\]

Using (12),

\[
\begin{aligned}
\frac1m\log\!\left(a_m^m B(m,N_m+1)\right)
&\le
\lambda_m\log\frac{\lambda_m}{1+\lambda_m}
+o(1)\\
&=-\lambda_m\log\left(1+\frac1{\lambda_m}\right)+o(1).
\end{aligned}
\tag{18}
\]

The last quantity is bounded above by a fixed negative constant because `lambda_m` lies in `[lambda_-,Lambda]`. This proves (15) on the `a_m>=1` branch.

### The branch `a_m < 1`

Split the absolute integral at `s=a`. On `[0,a]`, the same substitution gives exactly

\[
\int_0^a
s^{m-1}\left|1-\frac sa\right|^Nds
=
a^mB(m,N+1).
\tag{19}
\]

On `[a,1]`, put

\[
r_0(a):=\frac{1-a}{a}.
\tag{20}
\]

Since `s<=1` and `(s-a)/a<=r_0(a)`, one has

\[
\int_a^1
s^{m-1}\left|1-\frac sa\right|^Nds
\le r_0(a)^N.
\tag{21}
\]

The contraction condition `r(alpha,a)<1` is equivalent to

\[
a>\frac1{2\cos\alpha}.
\tag{22}
\]

Under (14), this yields

\[
a_m\ge a_0:=\frac1{2\cos\alpha_0}>\frac12.
\tag{23}
\]

If `a_0>=1` this branch is eventually empty. Otherwise

\[
r_0(a_m)
\le
\frac{1-a_0}{a_0}
=2\cos\alpha_0-1
<1.
\tag{24}
\]

The first term (19) has a uniformly negative beta/Stirling exponent because `a_m<1` and `lambda_m` remains in (6); the second term (21) has exponent at most `lambda_- log(2 cos(alpha_0)-1)<0`. Thus (15) follows here as well. Notice that parity of `N` is irrelevant because only an upper bound for `|D|` is used.

The point of (15) is structural. Once the center has been localized by RE-224 and the truncation ratio cannot collapse, the real DC denominator is exponentially small whenever one stays a fixed angular distance away from the vanishing-arc corner and tries to move the complex endpoint toward `r=1`.

## 3. The exact endpoint derivative is then exponentially too large

No remainder estimate is needed. Differentiating (13) on the unit circle gives exactly

\[
\frac{d}{d\theta}F_{m,N,a}(e^{-i\theta})
=
\frac{-iV_{m,N,a}(\theta)}{D_{m,N,a}},
\tag{25}
\]

where

\[
V_{m,N,a}(\theta)
:=
e^{-im\theta}
\left(1-\frac{e^{-i\theta}}a\right)^N.
\tag{26}
\]

At the observed endpoint,

\[
|V_{m,N_m,a_m}(\alpha_m)|=r_m^{N_m}.
\tag{27}
\]

Because `r_m -> 1` and `lambda_m` is bounded above,

\[
\frac1m\log r_m^{N_m}
=
\lambda_m\log r_m
\longrightarrow0.
\tag{28}
\]

Thus the numerator is only subexponentially small, whereas (15) says the denominator is exponentially small.

It remains to exclude cancellation of the derivative over a microscopic interval. From (22)--(23), `a_m` is bounded below by the fixed positive number `a_0`; and from (14),

\[
|a_m-e^{-i\alpha_m}|=a_mr_m\ge\frac{a_0}{2}
\tag{29}
\]

for all sufficiently large `m`. On an interval of length `O(1/m)` ending at `alpha_m`, the same distance is therefore at least `a_0/4`. Hence

\[
\left|\frac{d}{d\theta}\log V_{m,N_m,a_m}(\theta)\right|
\le
m+\frac{N_m}{|a_m-e^{-i\theta}|}
\le C m
\tag{30}
\]

for a fixed `C=C(alpha_0,Lambda)`.

Set

\[
\eta:=\log\frac32,
\qquad
h_m:=\frac{\eta}{Cm}.
\tag{31}
\]

For large `m`, `h_m<alpha_m`. Integrating (30) backward from `alpha_m` shows that throughout `[alpha_m-h_m,alpha_m]`,

\[
\left|
\frac{V(\theta)}{V(\alpha_m)}-1
\right|
\le e^\eta-1
=\frac12.
\tag{32}
\]

Therefore the exact derivative cannot self-cancel on this interval:

\[
\left|
\int_{\alpha_m-h_m}^{\alpha_m}V(\theta)d\theta
\right|
\ge
\frac{h_m}{2}r_m^{N_m}.
\tag{33}
\]

Combining (25), (33), and the uniform prediction hypothesis gives

\[
2\epsilon_m
\ge
\left|
F(e^{-i\alpha_m})-
F(e^{-i(\alpha_m-h_m)})
\right|
\ge
\frac{h_m}{2}
\frac{r_m^{N_m}}{|D_{m,N_m,a_m}|}.
\tag{34}
\]

Equations (15), (28), and `h_m=Theta(1/m)` make the right-hand side grow exponentially. This contradicts `epsilon_m -> 0`, proving (7)--(8).

This argument uses the exact normalized finite polynomial throughout. The contradiction is not an artifact of absolute control of the discarded negative-binomial tail: it comes from an exponentially small real normalization denominator and the inability of the exact endpoint derivative to rotate appreciably on a `Theta(1/m)` interval.

## 4. The factor-two frontier is now a single vanishing-arc problem

Consider the fixed-corridor RE-216 scaling. Along any subsequence whose normalized Wiener rate is at most two, RE-223 yields

\[
\liminf\lambda_m
\ge
0.06242231801357475\ldots,
\tag{35}
\]

while the corridor gives a finite upper bound for `lambda_m`. RE-224 then bounds `a_m` from above and, together with contraction, keeps `alpha_m` away from `pi/2`.

Suppose such a subsequence did not satisfy `alpha_m -> 0`. Passing to a further subsequence gives `alpha_m>=alpha_0>0`. RE-225 then gives `r_m<=rho<1` eventually. All three parameters `(alpha_m,a_m,lambda_m)` now lie in a compact subset of the interior contracting domain. RE-222 supplies a fixed `eta>0` with

\[
\liminf
\frac{\log\|F_m\|_A}{m\alpha_m}
\ge2+\eta,
\tag{36}
\]

contradicting the choice of the subsequence. This proves (9).

Thus the real single-center exact-cancellation program no longer has two unrelated singular frontiers. **At Wiener rate two or below, every fixed-corridor candidate must send the observed arc to zero.** The contraction-boundary case survives only if it is nested inside that same limit. In particular, if both `alpha_m -> 0` and `r_m -> 1`, equation (10) and boundedness of `a_m` force

\[
\boxed{a_m\to\frac12.}
\tag{37}
\]

A useful next normalization is therefore the vanishing-arc regime itself: `alpha_m -> 0` with `m alpha_m -> infinity`, resolving separately an interior-center limit `a_m -> a_*>1/2` and the coupled boundary layer `a_m-1/2 = O(alpha_m^2)` suggested by (10). If both retain a factor-two gap, the entire fixed-corridor positive-real single-center route is closed and the constructive frontier moves to complex exact cancellation, multi-center/minimax geometry, or a different basis.

## 5. Prior-art boundary and adversarial checks

Uniform asymptotics for incomplete beta functions with moving endpoints and saddle transitions are classical. Temme's *Uniform asymptotic expansions of the incomplete gamma functions and the incomplete beta function* (Math. Comp. 29, 1975) and *Incomplete Laplace integrals: uniform asymptotic expansion with application to the incomplete beta function* (SIAM J. Math. Anal. 18, 1987) cover the broader special-function setting, including parameter-uniform endpoint/saddle regimes. The general exponential cost of superoscillatory prediction is also classical.

None of those results is load-bearing here. The new localization uses only the exact finite-polynomial integral and derivative identities already established in RE-221, the exact center localization from RE-224, the complete beta integral, uniform Stirling on a compact positive `lambda` interval, and a microscopic phase-control interval. No `SOURCES.md` update is required.

The assumptions are essential. The positive lower bound in (6) is what makes the denominator gap uniform; if `lambda_m -> 0`, the beta entropy in (18) can vanish, and RE-223 is exactly the independent ingredient that excludes that direction on the factor-two frontier. The upper bound on `lambda_m` is the fixed-corridor hypothesis and is also used by RE-224 to localize the center. Complex centers destroy the positive-real beta decomposition and remain outside the theorem. Multi-center recombination can cancel after coefficients from different centers are combined and is likewise untouched.

The conclusion also does **not** say that `alpha_m -> 0` is sufficient to attain Wiener rate two, or that the factor-two bound is sharp. It says only that this is now the sole singular limit left for a fixed-corridor positive-real single-center exact predictor. The global separated-prediction interval remains

\[
1\le C_{\rm sep}\le5.996390.
\tag{38}
\]

The next falsification target is correspondingly narrow: derive a uniform normal form in the vanishing-arc limit and test whether exact incomplete-beta cancellation can actually keep the normalized Wiener rate at or below two there.