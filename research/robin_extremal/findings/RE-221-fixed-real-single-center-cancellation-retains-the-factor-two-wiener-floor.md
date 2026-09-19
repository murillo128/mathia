# RE-221 — Fixed real single-center cancellation retains the factor-two Wiener floor

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + EXACT-REMAINDER + INCOMPLETE-BETA-REDUCTION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-216--RE-220.

RE-219 proves a factor-two Wiener floor for a positive-real single-center negative-binomial predictor when the discarded Taylor tail is certified termwise in absolute value. RE-220 removes complex phase as an escape only for that same absolute-tail certificate. One live possibility therefore remained even before introducing several centers: perhaps the **actual complex cancellation of the finite Taylor remainder** lets the original real-center predictor truncate much earlier than the absolute-tail argument and thereby reduce its Wiener exponent below two.

For fixed single-center parameters, it does not. Let

\[
0<\alpha<\frac\pi2,\qquad a>0,
\qquad
r:=\frac{\sqrt{a^2+1-2a\cos\alpha}}{a}<1,
\tag{1}
\]

and let

\[
N=\lambda m+O(1),\qquad \lambda>0,
\tag{2}
\]

with `alpha`, `a`, and `lambda` fixed as `m -> infinity`. Form the **exact** truncated single-center predictor

\[
Q_{m,N,a}(z)
:=
z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\tag{3}
\]

and impose exact DC normalization by

\[
F_m(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)}.
\tag{4}
\]

Assume the actual polynomial, with no triangle-inequality estimate on its discarded series, predicts uniformly on the symmetric arc:

\[
\sup_{|\theta|\le\alpha}
\left|F_m(e^{-i\theta})-1\right|
\longrightarrow0.
\tag{5}
\]

Then the truncation ratio must lie beyond exactly the same upper exponential boundary that appears in RE-219. In particular the normalized coefficient Wiener norm obeys

\[
\boxed{
\liminf_{m\to\infty}
\frac{\log\|F_m\|_A}{m\alpha}
\ge2.
}
\tag{6}
\]

Under the RE-216 scaling `m alpha = HT+O(1)`, this is

\[
\boxed{
\liminf
\frac{\log\|\mu_T\|_{TV}}{HT}
\ge2.
}
\tag{7}
\]

Thus, for every fixed positive-real center/arc/truncation triple in the contracting RE-216 architecture, **using the exact cancellation-sensitive remainder does not evade the factor-two floor**. The absolute-tail proof in RE-219 was sufficient, but for fixed real parameters it was not the source of the obstruction.

This result is intentionally representation-local. It does not raise the global `C_sep >= 1` bound of RE-217, and it does not rule out asymptotically drifting/degenerate single-center parameters, genuinely complex-center cancellation, several centers, minimax polynomials, or a different approximation basis.

## 1. The truncated predictor is exactly an incomplete-beta polynomial

Put

\[
x:=\frac za.
\tag{8}
\]

Then (3) becomes

\[
Q_{m,N,a}(z)
=
x^m
\sum_{k=0}^{N}
\binom{m+k-1}{k}(1-x)^k.
\tag{9}
\]

For integer `m,N`, differentiating the finite sum gives the exact identity

\[
\frac{d}{dx}Q_{m,N,a}
=
\frac{(m+N)!}{(m-1)!N!}
 x^{m-1}(1-x)^N.
\tag{10}
\]

Since the left side vanishes at `x=0`, (9) is the classical regularized incomplete-beta polynomial

\[
Q_{m,N,a}(z)=I_{z/a}(m,N+1).
\tag{11}
\]

The special-function name is not needed below; (10) is the useful structure. After changing variables in the integral of (10), the normalized polynomial has the exact representation

\[
F_m(z)
=
\frac{
\displaystyle\int_0^z
s^{m-1}\left(1-\frac sa\right)^N ds
}{
\displaystyle\int_0^1
s^{m-1}\left(1-\frac sa\right)^N ds
}.
\tag{12}
\]

Write the denominator as `D_m`. Along `z=e^{-i theta}`, differentiation of (12) gives

\[
\frac{d}{d\theta}F_m(e^{-i\theta})
=
\frac{
-i e^{-im\theta}
\left(1-e^{-i\theta}/a\right)^N
}{D_m}.
\tag{13}
\]

This identity retains the full complex cancellation of the truncated series. No absolute tail has been introduced.

## 2. Uniform prediction forces the same exponential truncation boundary

Let

\[
r_0:=\left|1-\frac1a\right|.
\tag{14}
\]

Because `alpha>0`,

\[
r>r_0.
\tag{15}
\]

The denominator in (12) satisfies

\[
|D_m|
\le
\int_0^1
s^{m-1}
\left|1-\frac sa\right|^N ds.
\tag{16}
\]

At exponential scale, the integrand is governed by

\[
h(s)=\log s+\lambda\log\left|1-\frac sa\right|.
\tag{17}
\]

There are only two possible maxima on `[0,1]`. If

\[
s_*:=\frac{a}{1+\lambda}<1,
\tag{18}
\]

the branch `0<s<a` has the stationary maximum

\[
f_*=
\log a+\lambda\log\lambda
-(1+\lambda)\log(1+\lambda).
\tag{19}
\]

The other candidate is the real endpoint `s=1`, with exponent

\[
f_1=\lambda\log r_0.
\tag{20}
\]

If `s_*>=1`, only the endpoint can maximize (16). If `a<1`, the branch `a<s<=1` is strictly increasing in absolute value and likewise contributes only the endpoint. Hence

\[
\frac1m\log|D_m|
\le
\max(f_*,f_1)+o(1)
\tag{21}
\]

when (18) holds, and is at most `f_1+o(1)` otherwise.

Now use the **actual** endpoint variation of the normalized polynomial. Take `h_m=m^{-2}`. For fixed `alpha,a,lambda`, the logarithmic derivative of the numerator in (13) is `O(m)` on `[alpha-h_m,alpha]`. Therefore the derivative has essentially constant complex phase and magnitude on this tiny arc, and

\[
\left|
F_m(e^{-i\alpha})-
F_m(e^{-i(\alpha-h_m)})
\right|
=
(1+o(1))
\frac{h_m r^N}{|D_m|}.
\tag{22}
\]

Assumption (5) makes the left side tend to zero. Since `h_m=e^{o(m)}`, equations (21)--(22) force

\[
\lambda\log r
\le
\max(f_*,f_1)
\tag{23}
\]

whenever the stationary point exists, with the analogous endpoint-only inequality otherwise.

But (15) gives

\[
\lambda\log r>f_1.
\tag{24}
\]

Consequently the endpoint-only case is impossible: the stationary point (18) must exist, it must dominate the real denominator, and

\[
\lambda\log r\le f_*.
\tag{25}
\]

Equivalently,

\[
\boxed{
\tau(\lambda):=
-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log r
\le0.
}
\tag{26}
\]

This is exactly the exponential tail boundary used in RE-219, now obtained as a **necessary condition for the true normalized polynomial itself** rather than as a sufficient triangle-inequality certificate.

## 3. The admissible root is the upper root, not a cheap pre-mode branch

Condition (26) alone would be insufficient if it allowed the small-`lambda` region before the negative-binomial mode. The denominator geometry excludes that branch automatically.

If `a>1`, existence of (18) requires

\[
\lambda>a-1.
\tag{27}
\]

At the entry point `lambda=a-1`, with `r_0=(a-1)/a`, one has

\[
\tau(a-1)
=(a-1)\log\frac r{r_0}>0.
\tag{28}
\]

If `0<a<1`, instead

\[
\tau(0)=-\log a>0.
\tag{29}
\]

For `a=1`, `tau(0)=0` but `tau(lambda)>0` for all sufficiently small positive `lambda`, because the term `-lambda log lambda` dominates there. Finally,

\[
\tau''(\lambda)
=-\frac1{\lambda(1+\lambda)}<0,
\qquad
\tau(\lambda)\longrightarrow-\infty
\quad(\lambda\to\infty),
\tag{30}
\]

since `r<1`. Thus after the stationary point becomes available there is a unique upper zero `lambda_0`, and (26) forces

\[
\boxed{\lambda\ge\lambda_0.}
\tag{31}
\]

Moreover

\[
\lambda_0>rac r{1-r},
\tag{32}
\]

the negative-binomial mode. The exact cancellation-sensitive predictor therefore cannot truncate on the cheap side of that mode while remaining uniformly flat on the whole symmetric arc.

## 4. DC normalization is exponentially harmless and RE-219's factor-two geometry applies

The coefficient Wiener norm before DC normalization is still the exact quantity from RE-216--RE-220:

\[
A_m
=
a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1+\frac1a\right)^k.
\tag{33}
\]

For fixed `lambda`, its exponential rate is

\[
\nu(\lambda)
=
-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log\frac{a+1}{a}.
\tag{34}
\]

The final summand dominates exponentially, and `nu(lambda)` is strictly increasing.

It remains to check that dividing by `Q_{m,N,a}(1)` did not hide an exponential gain. At `z=1` the expansion parameter has modulus `r_0<r`. Since `lambda>=lambda_0>r/(1-r)`, the absolute tail at `z=1` is already beyond its mode, and its first omitted exponential rate is

\[
\tau(\lambda)
+\lambda\log\frac{r_0}{r}<0.
\tag{35}
\]

(with the `a=1` case even simpler because `r_0=0`). Hence

\[
Q_{m,N,a}(1)=1+O(e^{-c m})
\tag{36}
\]

for some fixed `c>0`. Exact DC normalization changes the Wiener norm only by `1+o(1)`.

Therefore the cheapest possible fixed-parameter exact predictor is again obtained at the upper boundary `lambda_0`. At `tau(lambda_0)=0`, RE-219's elementary arc geometry gives

\[
\nu(\lambda_0)
=
\lambda_0
\log\frac{(a+1)/a}{r}
>2\alpha.
\tag{37}
\]

The strict inequality is the same one-variable estimate proved in RE-219 after `lambda_0>r/(1-r)`; no absolute-tail hypothesis enters that geometric step. Since `nu` increases with `lambda`, (31), (34), and (37) yield

\[
\log\|F_m\|_A
\ge
(2\alpha+o(1))m,
\tag{38}
\]

which proves (6)--(7).

## 5. Prior-art and falsification boundary

The identity (11) is classical: finite negative-binomial sums are regularized incomplete-beta polynomials, and the negative-binomial CDF is conventionally written using `I_x`. Broad literature search also recovers the classical band-limited prediction and superoscillation literature, where exponential dynamic-range costs are well known. No novelty is claimed for incomplete beta functions, negative-binomial partial sums, or superoscillation itself.

None of that literature is load-bearing here. Equations (9)--(13) follow by direct differentiation of the finite polynomial, and the exponent comparison (16)--(38) is self-contained. The line-specific content is that the **exact normalized remainder** of the particular RE-216 predictor is forced onto the same upper truncation branch that RE-219 previously reached by absolute domination, so the already-established Wiener factor-two obstruction survives cancellation. No `SOURCES.md` update is required.

Several controls delimit the claim. The symmetric arc and its nonzero width are essential to (15) and the endpoint comparison. The center is positive real; RE-220's radialization applies to coefficient norm and absolute tails, not to the exact complex remainder, so genuinely complex-center cancellation is not settled here. The parameters are fixed as `m` grows; asymptotically degenerate single-center schemes are not promoted into this theorem. Several centers can cancel after coefficient recombination and are also outside the argument. Finally, this is a representation obstruction before prime realization, not a new source-capacity theorem.

## Research consequence

RE-219 left cancellation-sensitive remainder control as one possible way to break its factor-two floor. RE-221 removes that escape for the fixed positive-real single-center family actually used by RE-216 and RE-218: **even the exact polynomial, after optimal DC normalization, must truncate beyond the same upper negative-binomial boundary and therefore pays Wiener exponent at least two.**

The global interval remains

\[
1\le C_{\rm sep}\le5.996390.
\tag{39}
\]

What has narrowed is the constructive search space. Improving the current upper bound by a serious constant now requires genuinely new geometry: multi-center/minimax prediction, a different polynomial or rational basis, genuinely complex-center cancellation, or an asymptotically degenerate single-center scheme whose regularity and shell count would have to be rechecked against the RE-208 ordinary-prime interface. Merely replacing the absolute-tail estimate of the current fixed real-center predictor by an exact remainder calculation cannot cross the factor-two representation floor.
