# RE-218 — Explicit off-center retuning pushes the separated Wiener exponent below six

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + WIENER-NORM-UPPER-BOUND + ORDINARY-PRIME-REALIZATION + KV-FIDELITY + PRIOR-ART-AUDIT`.

**Parent findings:** RE-208, RE-216, RE-217.

RE-217 isolates the pure separated-prediction constant `C_sep` and leaves the rigorous interval

\[
1\le C_{\rm sep}\le 6.081,
\]

where the upper endpoint comes from the explicit off-center binomial predictor of RE-216. RE-216 also notes that numerical retuning of that representation appears to offer only a modest improvement, but does not promote such tuning into a theorem.

A fully explicit retuning is nevertheless enough to cross the clean threshold six. Keep the same arc parameter as RE-216, but replace its expansion center and truncation depth by

\[
\alpha=\frac{13}{25},\qquad
 a=\frac{229}{100},\qquad
 \lambda=\frac{499}{125}=3.992.
\tag{1}
\]

Then the same self-contained off-center negative-power expansion gives a separated predictor with support in a fixed corridor contained in `[H,5H+o(1)]`, uniform error tending exponentially to zero in `HT`, and

\[
\boxed{
\log\|\mu_T\|_{TV}
\le
(5.996390+o(1))HT.
}
\tag{2}
\]

Consequently

\[
\boxed{C_{\rm sep}\le 5.996390<6.}
\tag{3}
\]

This is a small but strict improvement of the live spectral bottleneck. Through the unchanged ordinary-prime realization of RE-208, for `H=log 8` the rigorously realized logarithmic-height range improves from `c<0.0395410...` to

\[
\boxed{c<0.0400989... .}
\tag{4}
\]

No stronger prime theorem, relaxed multiplicity model, new source architecture, or external approximation theorem is used.

## 1. Use the same off-center expansion with explicit retuned parameters

Put

\[
A:=HT,
\qquad
\delta:=\frac{\alpha}{T},
\qquad
m:=\left\lceil\frac{H}{\delta}\right\rceil,
\qquad
N:=\lceil\lambda m\rceil,
\qquad
z:=e^{-i\delta t}.
\tag{5}
\]

For `|t|<=T`, we have `|arg z|<=alpha`. As in RE-216,

\[
z^{-m}
=
 a^{-m}\left(1-\frac{a-z}{a}\right)^{-m}
=
\sum_{k=0}^{\infty}
\binom{m+k-1}{k}a^{-m-k}(a-z)^k.
\tag{6}
\]

The uniform contraction factor on the whole observed arc is

\[
r
:=
\max_{|\theta|\le\alpha}
\frac{|a-e^{-i\theta}|}{a}
=
\frac{\sqrt{a^2+1-2a\cos\alpha}}{a}
=0.65785242214654\ldots .
\tag{7}
\]

Elementary interval evaluation of the cosine and logarithms in (7) gives, for example,

\[
0.65785242<r<0.65785243.
\tag{8}
\]

For `k>=N`, the ratio of consecutive absolute tail terms is at most

\[
r\frac{m+k}{k+1}
\le
0.823
\tag{9}
\]

for all sufficiently large `m`. Hence the full tail is bounded by a fixed multiple of its first term.

At `N=lambda m+O(1)`, Stirling gives the exponential tail rate

\[
\begin{aligned}
\tau
&:=
-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log r\\
&=-0.0000748740220\ldots<0.
\end{aligned}
\tag{10}
\]

Therefore the truncation in (6) satisfies, uniformly on `|t|<=T`,

\[
\left|
 z^{-m}
-
\sum_{k=0}^{N}
\binom{m+k-1}{k}a^{-m-k}(a-z)^k
\right|
\le
\exp[-(7\times10^{-5}+o(1))m].
\tag{11}
\]

The numerical margin in (10) is deliberately retained rather than optimizing on the zero-tail boundary; it makes the uniform convergence statement independent of any asymptotically varying parameter choice.

Multiplying by `z^m` gives an exponential polynomial whose delays are

\[
L_j=(m+j)\delta,
\qquad 0\le j\le N.
\tag{12}
\]

Thus

\[
L_j\ge H,
\qquad
L_{\max}
\le
(1+\lambda)H+o(1)
=4.992H+o(1),
\tag{13}
\]

so the same fixed-corridor separation required by RE-217 is preserved. At `t=0` the truncated expression differs from one by the exponentially small quantity in (11); dividing all coefficients by that value imposes exact DC normalization and changes the Wiener norm only by `1+o(1)`.

## 2. The explicit coefficient exponent is below six

Expand each `(a-z)^k` in nonnegative powers of `z`. As in RE-216, for a fixed output degree all contributions have the same sign, so the coefficient `ell^1` norm before DC normalization is exactly

\[
A_m
=
 a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(\frac{a+1}{a}\right)^k.
\tag{14}
\]

These summands increase with `k`; the final term therefore determines the exponential rate, with the number of terms contributing only `e^{o(m)}`. Stirling at `N=lambda m+O(1)` yields

\[
\frac1m\log A_m
\le
\nu+o(1),
\tag{15}
\]

where

\[
\begin{aligned}
\nu
&:=
-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log\frac{a+1}{a}\\
&=3.11811785265851\ldots .
\end{aligned}
\tag{16}
\]

Since

\[
m=\frac{HT}{\alpha}+O(1)=\frac{25}{13}HT+O(1),
\tag{17}
\]

we obtain

\[
\frac{\nu}{\alpha}
=5.99638048588175\ldots<5.996390.
\tag{18}
\]

Combining (11), (14)--(18), and the harmless DC normalization proves (2)--(3).

The useful point is not the last decimals themselves. The construction supplies a fixed explicit corridor, a fixed positive convergence margin, and a Wiener exponent strictly below six; it is therefore a genuine rigorous improvement of the RE-217 upper bound rather than an unconstrained numerical optimum.

## 3. Arithmetic realization and selector-scale consequence

Set, as in RE-208 and RE-216,

\[
T_Q=c\log Q,
\qquad H=\log 8,
\qquad
d_Q=\frac1{\sqrt Q\log Q}.
\tag{19}
\]

Equations (11) and (17) give a polynomially decaying spectral error in `Q` for every fixed `c>0`, while (2) gives

\[
\|\mu_{T_Q}\|_{TV}
\le
Q^{\kappa+o(1)},
\qquad
\kappa:=5.996390\,Hc.
\tag{20}
\]

The RE-208 reservoir-centroid realization uses the predictor only through its `O(log Q)` number of real coefficients, spacing `asymp 1/log Q`, fixed support corridor, vanishing uniform spectral error, and total reciprocal coefficient variation. The retuned predictor has exactly the same interface as RE-216, so the ordinary-prime `{0,1,2}` construction and its KV estimates apply unchanged whenever

\[
\kappa<\frac12.
\tag{21}
\]

For `H=log 8`, (21) is

\[
0<c<
\frac{1}{2(5.996390)\log 8}
=0.0400989\ldots .
\tag{22}
\]

The local packet still carries selector-scale debt before the first repair cloud; integer population rounding, exact Euler prime powers, reservoir placement, and Chebyshev edit-mass estimates remain those already verified in RE-208/RE-216. This finding changes only the spectral coefficient exponent.

## 4. Adversarial checks and representation audit

The main possible failure is that the improved norm comes from moving too close to the convergence boundary. Equation (10) rules this out: the tail exponent is a fixed negative constant, not an `o(1)` artifact. The consecutive-tail ratio in (9) stays uniformly below one, so the first omitted term controls the full tail. Rounding `N` and `m` changes all logarithmic rates only by `o(m)`.

A second possible failure is support leakage toward zero or negative delays. Equation (12) shows that every atom remains at a nonnegative polynomial degree after multiplication by `z^m`, and (13) keeps the entire predictor inside the same fixed separated corridor used by RE-216. The modest reduction of the upper corridor endpoint from `5H` to `4.992H+o(1)` cannot create extra source freedom.

A third control is whether the apparent gain is caused by cancellation hidden inside the coefficient norm. It is not: (14) is the exact `ell^1` norm because each fixed output degree receives terms with one common alternating sign. The calculation therefore measures the same Wiener currency as RE-217.

Finally, this is not a new generic prediction mechanism. Off-center Taylor/binomial prediction is classical approximation machinery, and broad prior-art search again finds Chebyshev, Newton/difference, and finite-memory polynomial predictors for band-limited signals. No theorem from that literature is used in (5)--(18), and no novelty is claimed for polynomial extrapolation itself. The line-specific result is the explicit quantitative coupling of a sub-six Wiener exponent to the already established ordinary-prime `{0,1,2}` realization. No `SOURCES.md` update is required because there is no new load-bearing external dependency.

## Research consequence

The live pure-approximation interval tightens from

\[
1\le C_{\rm sep}\le6.081
\]

to

\[
\boxed{1\le C_{\rm sep}\le5.996390<6.}
\tag{23}
\]

and the explicit ordinary-prime hiding range at `H=log 8` increases by about `1.4%`, from `c<0.0395410...` to `c<0.0400989...`.

This also acts as a negative control on further tuning of the same representation: a fixed parameter change can improve RE-216, but only modestly. The major unresolved factor remains between the unit lower bound of RE-217 and the roughly six-unit explicit upper bound. Closing that gap still requires either a genuinely lower-Wiener-norm predictor family or a source realization whose relevant signed-prefix cost is substantially smaller than total coefficient variation.