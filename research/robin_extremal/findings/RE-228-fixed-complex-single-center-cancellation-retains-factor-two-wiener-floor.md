# RE-228 — Fixed complex single-center cancellation retains the factor-two Wiener floor

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER + EXACT-REMAINDER + DC-NORMALIZATION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-218--RE-221, RE-227.

RE-220 shows that a complex phase cannot help one negative-binomial expansion center when the discarded tail is certified termwise in absolute value. RE-221 then shows that, for a fixed **positive-real** center, even the exact cancellation-sensitive normalized polynomial retains the factor-two Wiener floor. The corresponding fixed-parameter complex-center case remained open because the DC normalization `Q(1)` can itself have complex cancellation and need not be exponentially close to one.

That escape is also blocked. Fix

\[
0<\alpha<\frac\pi2,
\qquad
 a=\rho e^{i\varphi}\ne0,
\qquad
N=\lambda m+O(1),\quad \lambda>0,
\tag{1}
\]

and define the same exact truncated predictor

\[
Q_{m,N,a}(z)
:=
z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_m(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)}.
\tag{2}
\]

Assume the whole symmetric arc is contracting,

\[
r:=\max_{|\theta|\le\alpha}
\left|1-\frac{e^{-i\theta}}a\right|<1,
\tag{3}
\]

and that the **actual normalized polynomial**, with no absolute-tail estimate on its remainder, predicts uniformly:

\[
\sup_{|\theta|\le\alpha}
|F_m(e^{-i\theta})-1|\longrightarrow0.
\tag{4}
\]

Then

\[
\boxed{
\liminf_{m\to\infty}
\frac{\log\|F_m\|_A}{m\alpha}>2.
}
\tag{5}
\]

Thus exact cancellation at one genuinely complex fixed center does not cross the factor-two boundary either. More precisely, put

\[
r_0:=\left|1-\frac1a\right|,
\qquad
u:=1+\frac1\rho,
\qquad
g(x):=(1+x)\log(1+x)-x\log x.
\tag{6}
\]

Symmetric-arc contraction gives `0<=r_0<r<1`. Let `lambda_*` be the unique upper root of

\[
g(\lambda)+\lambda\log r+\log(1-r_0)=0.
\tag{7}
\]

Uniform prediction forces

\[
\boxed{\lambda\ge\lambda_*>rac r{1-r},}
\tag{8}
\]

and the exact normalized coefficient norm obeys

\[
\boxed{
\liminf_{m\to\infty}
\frac1m\log\|F_m\|_A
\ge
\lambda_*\log\frac\nu r.
}
\tag{9}
\]

The right side is strictly larger than `2 alpha`. Complex phase therefore cannot exploit DC normalization to evade the fixed-parameter single-center obstruction.

This theorem is deliberately fixed-parameter. It does not yet supply the diagonal/uniform closure for drifting complex centers that RE-222--RE-227 establish on the positive-real slice. Multi-center coefficient recombination, minimax/rational predictors, and other bases also remain outside the claim.

## 1. Exact complex coefficients still have a phase-free Wiener norm

Write

\[
C_{m,k}:=\binom{m+k-1}{k}.
\tag{10}
\]

RE-220 proves by re-expanding `(a-z)^k` that the unnormalized polynomial in (2) has the exact coefficient norm

\[
A_m:=\|Q_{m,N,a}\|_A
=
\rho^{-m}
\sum_{k=0}^{N}
C_{m,k}
\left(1+\frac1\rho\right)^k.
\tag{11}
\]

There is no triangle inequality hidden in (11): for each output degree the phase of `a` factors out of every contributing truncation level.

The only new difficulty is the normalization scalar. Directly from (2),

\[
Q_{m,N,a}(1)
=
a^{-m}
\sum_{k=0}^{N}
C_{m,k}
\left(1-\frac1a\right)^k.
\tag{12}
\]

Whatever cancellation occurs in this complex sum, its modulus satisfies

\[
|Q_{m,N,a}(1)|
\le
B_m
:=
\rho^{-m}
\sum_{k=0}^{N}
C_{m,k}r_0^k.
\tag{13}
\]

Consequently

\[
\boxed{
\|F_m\|_A
=\frac{A_m}{|Q_{m,N,a}(1)|}
\ge\frac{A_m}{B_m}.
}
\tag{14}
\]

This is the key direction of the estimate. Exact cancellation in `Q(1)` only makes the denominator smaller and the normalized Wiener norm larger. It cannot be used as a hidden discount.

## 2. Exact flatness forces truncation past the negative-binomial mode of the worst endpoint

The finite polynomial in (2) is the same incomplete-beta polynomial as in RE-221, now at complex `a`. Differentiating the finite sum gives

\[
\frac{d}{d\theta}
Q_{m,N,a}(e^{-i\theta})
=
-iK_{m,N}
\left(\frac{e^{-i\theta}}a\right)^m
\left(1-\frac{e^{-i\theta}}a\right)^N,
\tag{15}
\]

where

\[
K_{m,N}:=\frac{(m+N)!}{(m-1)!N!}.
\tag{16}
\]

Choose an endpoint `theta_* in {+alpha,-alpha}` at which (3) attains `r`. Equations (13)--(16) give

\[
|F_m'(e^{-i\theta_*})|
\ge
\frac{K_{m,N}r^N}
{\displaystyle\sum_{k=0}^{N}C_{m,k}r_0^k}.
\tag{17}
\]

For fixed `alpha,a,lambda`, the logarithmic derivative of the right-hand analytic factor in (15) is `O(m)` in a fixed neighborhood of `theta_*`. On an inward interval of length `h_m=m^{-2}`, the derivative therefore changes by only `1+o(1)` in magnitude and by `o(1)` in phase. Hence

\[
|F_m(e^{-i\theta_*})-
F_m(e^{-i(\theta_*-\operatorname{sgn}(\theta_*)h_m)})|
=(1+o(1))h_m|F_m'(e^{-i\theta_*})|.
\tag{18}
\]

The left side tends to zero by (4). Since `h_m=e^{o(m)}`, the exponential rate on the right of (17) cannot be positive.

Stirling gives

\[
\frac1m\log K_{m,N}=g(\lambda)+o(1).
\tag{19}
\]

For fixed `0<=v<1`, the truncated negative-binomial sum has exponential rate

\[
\frac1m\log
\sum_{k=0}^{N}C_{m,k}v^k
=
\begin{cases}
 g(\lambda)+\lambda\log v+o(1),
 &\lambda\le \dfrac v{1-v},\\[1.1ex]
 -\log(1-v)+o(1),
 &\lambda\ge \dfrac v{1-v}.
\end{cases}
\tag{20}
\]

The `v=0` case is read by continuity: the sum is exactly one.

Because the observed arc is symmetric and nontrivial while (3) keeps it inside the contracting half-plane, its worst endpoint is strictly farther from the center than `theta=0`; thus

\[
0\le r_0<r<1.
\tag{21}
\]

If

\[
\lambda\le \frac{r_0}{1-r_0},
\tag{22}
\]

then (17)--(20) have exponential rate

\[
\lambda\log\frac r{r_0}>0,
\tag{23}
\]

so (4) is impossible. Therefore `lambda>r_0/(1-r_0)`, and (20) reduces the necessary flatness condition to

\[
h(\lambda)
:=
g(\lambda)+\lambda\log r+\log(1-r_0)
\le0.
\tag{24}
\]

Now put

\[
x_r:=\frac r{1-r}.
\tag{25}
\]

The elementary negative-binomial identity

\[
g(x_r)+x_r\log r=-\log(1-r)
\tag{26}
\]

gives

\[
h(x_r)
=
\log\frac{1-r_0}{1-r}>0.
\tag{27}
\]

Moreover

\[
h'(\lambda)
=\log\frac{r(1+\lambda)}\lambda,
\qquad
h''(\lambda)=-\frac1{\lambda(1+\lambda)}<0,
\tag{28}
\]

so `h` reaches its maximum at `x_r` and tends to `-infinity` as `lambda->infinity`. There is a unique upper zero `lambda_*>x_r`, and (24) forces (8).

The important point is that this conclusion used the **true normalized polynomial**. The only triangle inequality was the upper bound (13) on its normalization denominator, and cancellation there can only strengthen the obstruction.

## 3. The same denominator bound prices the normalized Wiener norm

Since `nu=1+1/rho>1`, the summands in (11) are exponentially increasing all the way to `k=N`. Thus

\[
\frac1m\log A_m
=
-\log\rho
+g(\lambda)+\lambda\log\nu+o(1).
\tag{29}
\]

Because (8) places `lambda` beyond both `r/(1-r)` and `r_0/(1-r_0)`, equation (20) applied to (13) yields

\[
\frac1m\log B_m
=
-\log\rho-\log(1-r_0)+o(1).
\tag{30}
\]

Combining (14), (29), and (30),

\[
\liminf\frac1m\log\|F_m\|_A
\ge
c(\lambda)
:=
g(\lambda)+\lambda\log\nu+\log(1-r_0).
\tag{31}
\]

This lower-bound rate is strictly increasing because

\[
c'(\lambda)
=
\log\frac{\nu(1+\lambda)}\lambda>0.
\tag{32}
\]

Hence the cheapest admissible fixed truncation ratio is the boundary `lambda_*`. Using (7),

\[
c(\lambda_*)
=
\lambda_*\log\frac\nu r
>
\frac r{1-r}\log\frac\nu r.
\tag{33}
\]

It remains only to compare the final geometric quantity with the arc width.

## 4. Complex phase can only increase the RE-219 geometric floor

At fixed modulus `rho`, let

\[
r_{\mathbb R}
:=
\sqrt{1+\rho^{-2}-2\rho^{-1}\cos\alpha}
\tag{34}
\]

be the worst contraction factor for the positive-real radial center. RE-220 proves directly from the two symmetric endpoints that

\[
r\ge r_{\mathbb R}.
\tag{35}
\]

The radial comparator also contracts because `r_R<=r<1`. For fixed

\[
\nu=1+\rho^{-1}>1,
\tag{36}
\]

define

\[
\Phi_\nu(s)
:=
\frac{s}{1-s}\log\frac\nu s,
\qquad 0<s<1.
\tag{37}
\]

Its derivative is

\[
\Phi_\nu'(s)
=
\frac{\log(\nu/s)-(1-s)}{(1-s)^2}>0,
\tag{38}
\]

because `log(nu/s)>-log s>1-s`. Therefore (35) gives

\[
\Phi_\nu(r)
\ge
\Phi_\nu(r_{\mathbb R}).
\tag{39}
\]

The elementary one-variable arc estimate proved in RE-219 for the radial center is

\[
\Phi_\nu(r_{\mathbb R})>2\alpha.
\tag{40}
\]

Equations (33), (39), and (40) now give

\[
\liminf\frac1m\log\|F_m\|_A
>2\alpha,
\tag{41}
\]

which is exactly (5). The phase of one complex center therefore does not open a fixed-parameter route below factor two even when the remainder and the DC normalization are treated with their full complex cancellation.

## 5. Calibration against the explicit sub-six construction

The bound is substantially sharper than the headline factor two at the parameters already used by RE-218. For

\[
\alpha=\frac{13}{25},
\qquad
\rho=\frac{229}{100},
\qquad
\varphi=0,
\tag{42}
\]

the upper root in (7) is

\[
\lambda_*=3.99161646485557\ldots,
\tag{43}
\]

and (9) gives

\[
\frac{\lambda_*}{\alpha}
\log\frac\nu r
=5.99594835267216\ldots .
\tag{44}
\]

RE-218 chooses the explicit safe value

\[
\lambda=\frac{499}{125}=3.992
\tag{45}
\]

and proves the upper exponent

\[
5.99638048588175\ldots<5.996390.
\tag{46}
\]

Thus, **for that fixed arc and center**, the explicit construction is already within about `4.33e-4` in normalized Wiener exponent of the exact-cancellation lower boundary derived here. This numerical calibration is not used in the theorem and is not claimed to be a global optimization over `alpha`, `rho`, or complex phase. It does show that the near-six cost of RE-218 is not mainly an artifact of its termwise tail estimate at those parameters.

## 6. Prior art, representation audit, and remaining boundary

The finite polynomial in (2) is a regularized incomplete-beta/negative-binomial polynomial; that identity and its large-parameter asymptotics are classical. Temme's 1975 uniform incomplete-beta expansions and his 1987 treatment of incomplete Laplace integrals are representative prior art. Superoscillatory prediction with exponential energy or dynamic-range cost is likewise classical in work such as Ferreira--Kempf. No novelty is claimed for incomplete beta functions, negative-binomial modes, or exponential superoscillation cost.

None of those external results is load-bearing here. Equations (11)--(16) are finite algebraic identities already established in RE-220--RE-221; (20) is the elementary Stirling/Laplace rate of a one-dimensional finite sum; and the decisive comparison (33)--(40) is internal geometry. The line-specific result is that **an upper bound on the exact complex DC normalization forces the same upper negative-binomial branch that prices the Wiener norm**, after which radial endpoint geometry makes complex phase no cheaper than the real comparator. No `SOURCES.md` update is required.

Several boundaries matter. First, the parameters in (1) are fixed while `m` grows. If `a_m`, `alpha_m`, or `lambda_m` approach a singular boundary, the `O(m)` local logarithmic-derivative control used in (18) is not automatically uniform; the positive-real diagonal closure RE-222--RE-227 does not transfer for free. Second, symmetry of the observed arc is essential to (21), (35), and the radial comparison. On a one-sided arc a rotated center can genuinely reduce the worst distance. Third, several centers can cancel after their coefficient vectors are recombined, so (11)--(14) do not reduce multi-center geometry to one modulus.

## Research consequence

The fixed-parameter complex-center escape left by RE-220--RE-221 is closed. For one exact normalized negative-binomial center, complex remainder cancellation and complex DC normalization cannot beat the factor-two Wiener floor; at fixed modulus the final geometric lower bound is actually worsened by center phase.

The remaining single-center question is now narrower: can a **drifting or degenerate complex center** exploit a nonuniform boundary regime that has no positive-real analogue after RE-222--RE-227? If that route also closes, the constructive frontier should move entirely to multi-center/minimax or a different representation. Independently, equations (7)--(9) provide a much sharper parameter-dependent lower bound that can be compared directly with explicit single-center constructions such as RE-218.