# MC-176 — Gallagher diagonal type forces a critical-shell Good–Churchhouse variance bound

**Status:** `EXACT-DERIVED`, `FRONTIER-RESTRICTION`, `NECESSARY-CONDITION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The diagonal Gallagher target isolated in `MC-172` and priced in `MC-174`–`MC-175` contains a sharp **necessary** short-interval variance condition. It cannot become small by averaging cancellation across logarithmic scales while leaving the heat-critical scale uncontrolled, because the Gallagher energy is a positive integral and already contains that scale as a positive summand.

Fix

\[
\frac18\le \tau<\frac14,
\qquad
T_\beta=e^{\tau/\beta},
\]

and suppose the true Möbius phase satisfies the diagonal heat-type target

\[
\limsup_{\beta\downarrow0}
\beta\log \mathcal G_\mu(\beta,T_\beta)
\le \frac18.
\tag{1}
\]

Choose dyadic `X_beta=2^{k_beta}` so that

\[
\beta\log X_\beta\longrightarrow\frac14.
\tag{2}
\]

On `X_beta<=y<=2X_beta`, let

\[
B_{\beta,\tau}(y)
=
e^{\beta(\log y)^2}
\sum_{y<n\le ye^{1/T_\beta}}
\mu(n)e^{-\beta(\log n)^2}
\tag{3}
\]

be the normalized local sum from `MC-175`, and define the ordinary variable-length additive short sum

\[
S_{\beta,\tau}(y)
:=
\sum_{y<n\le y+y/T_\beta}\mu(n).
\tag{4}
\]

Then

\[
\boxed{
\sup_{X_\beta\le y\le2X_\beta}
|B_{\beta,\tau}(y)-S_{\beta,\tau}(y)|=O(1),
}
\tag{5}
\]

and `(1)` forces

\[
\boxed{
\limsup_{\beta\downarrow0}
\beta\log
\int_{X_\beta}^{2X_\beta}
|S_{\beta,\tau}(y)|^2\frac{dy}{y}
\le
\frac14-\tau.
}
\tag{6}
\]

If

\[
H_\beta:=\frac{X_\beta}{T_\beta},
\]

then

\[
\beta\log H_\beta\longrightarrow\frac14-\tau,
\qquad
H_\beta=X_\beta^{\,1-4\tau+o(1)}.
\tag{7}
\]

Thus `(6)` says that at the single heat-critical shell `beta log X -> 1/4`, the normalized integer Möbius second moment must have **diagonal/square-root exponential type**:

\[
\int_{X_\beta}^{2X_\beta}
|S_{\beta,\tau}(y)|^2\frac{dy}{y}
\le
H_\beta\,e^{o(1/\beta)}.
\tag{8}
\]

At the earliest twist-stable horizon `tau=1/8`, this is a square-root-length short-interval condition,

\[
H_\beta=X_\beta^{1/2+o(1)}.
\tag{9}
\]

The order in `(8)` is precisely the variance scale predicted by the classical Good–Churchhouse picture for Möbius block sums, though `(8)` is only an exponential-order upper bound for a dyadic variable-length average, not their normal-distribution conjecture or its asymptotic constant.

The consequence is a genuine restriction on the Gallagher route: **diagonal heat type already requires square-root local second-moment behavior at a conventional integer short-interval scale.** It is therefore not an easier intermediate merely because it was reached through heat flow and Gallagher localization.

## 1. Positivity isolates the heat-critical shell

From `(3)`, the Gallagher energy may be written

\[
\mathcal G_\mu(\beta,T_\beta)
=
T_\beta\int_1^\infty
 e^{-2\beta(\log y)^2}
 |B_{\beta,\tau}(y)|^2\frac{dy}{y}.
\tag{10}
\]

Every shell contribution is nonnegative. Therefore

\[
\mathcal G_\mu(\beta,T_\beta)
\ge
T_\beta
 e^{-2\beta(\log(2X_\beta))^2}
J_\beta,
\tag{11}
\]

where

\[
J_\beta
:=
\int_{X_\beta}^{2X_\beta}
|B_{\beta,\tau}(y)|^2\frac{dy}{y}.
\tag{12}
\]

Taking `beta log` in `(11)` and using `(1)`–`(2)` gives

\[
\begin{aligned}
\limsup_{\beta\downarrow0}\beta\log J_\beta
&\le
\frac18-\tau
+2\left(\frac14\right)^2\\
&=
\frac14-\tau.
\end{aligned}
\tag{13}
\]

This is not the sufficient scale-uniform envelope of `MC-175`. It is a necessary consequence of the target itself, obtained from one positive shell. In particular, no cancellation between different dyadic shells can repair a failure of `(13)`.

The location `beta log X=1/4` is also forced naturally by the diagonal term. It is the Gaussian saddle of

\[
X e^{-2\beta(\log X)^2},
\]

whose exponential type is `1/8`. This is exactly the `eta=1` saddle implicit in the phase diagram of `MC-175`.

## 2. The Gaussian and multiplicative-window decorations disappear at this scale

It remains to check that `(13)` is not an artifact of the Gaussian coefficient or of using multiplicative rather than ordinary additive windows.

For `y<n<=ye^{1/T_beta}`, write `delta=log(n/y)`. Then `0<delta<=1/T_beta`, and

\[
\beta\big((\log n)^2-(\log y)^2\big)
=
\beta(2\log y\,\delta+\delta^2)
\ll \frac1{T_\beta}
\tag{14}
\]

uniformly on the shell because `beta log y=O(1)`. Hence

\[
\left|
e^{-\beta((\log n)^2-(\log y)^2)}-1
\right|
\ll \frac1{T_\beta}.
\tag{15}
\]

The multiplicative interval contains `O(1+y/T_beta)` integers, so replacing its normalized Gaussian weights by `1` costs at most

\[
O\!\left(\frac1{T_\beta}
+\frac{y}{T_\beta^2}\right).
\tag{16}
\]

Next,

\[
y\left(e^{1/T_\beta}-1\right)
=
\frac{y}{T_\beta}
+O\!\left(\frac{y}{T_\beta^2}\right),
\tag{17}
\]

so replacing the multiplicative endpoint by `y+y/T_beta` changes only

\[
O\!\left(1+\frac{y}{T_\beta^2}\right)
\tag{18}
\]

integer terms.

On the critical shell,

\[
\beta\log\frac{X_\beta}{T_\beta^2}
\longrightarrow
\frac14-2\tau\le0
\tag{19}
\]

because `tau>=1/8`. Equations `(16)`–`(19)` prove `(5)`.

By the `L^2(dy/y)` triangle inequality, `(5)` implies

\[
\left|
J_\beta^{1/2}
-
\left(
\int_{X_\beta}^{2X_\beta}
|S_{\beta,\tau}(y)|^2\frac{dy}{y}
\right)^{1/2}
\right|
=O(1).
\tag{20}
\]

Since `tau<1/4`, the exponent `1/4-tau` is positive. Combining `(13)` and `(20)` therefore proves `(6).

## 3. Heat horizon becomes the ordinary interval-length exponent

From `(2)` and `T_beta=e^{tau/beta}`,

\[
\frac{\log T_\beta}{\log X_\beta}\longrightarrow4\tau.
\]

Thus the interval length `y/T_beta` on this shell is within a fixed factor of

\[
H_\beta
=
X_\beta^{\,\theta+o(1)},
\qquad
\boxed{\theta=1-4\tau.}
\tag{21}
\]

The twist-stable range `1/8<=tau<1/4` maps exactly to

\[
0<\theta\le\frac12.
\tag{22}
\]

This differs from the moving coherent saddle `theta_0=1-2tau` in `MC-175`. The present shell is the **diagonal critical shell**, and because `(1)` forces its actual contribution to be small, the corresponding `theta=1-4tau` condition is necessary rather than merely the saddle of a chosen sufficient majorant.

At `tau=1/8`, `(21)` gives `theta=1/2`. At later horizons the same target demands diagonal-order variance in progressively shorter polynomial intervals. Hence choosing a later `tau` weakens the zero-free consequence in `MC-174` but simultaneously moves the required integer variance estimate to a shorter, not obviously easier, scale.

## 4. Prior art and novelty assessment

The short-interval variance target itself is classical. Good and Churchhouse, *The Riemann hypothesis and pseudorandom features of the Möbius sequence*, Mathematics of Computation 22 (1968), 857–861, conjectured that long Möbius block sums have asymptotically normal distribution with variance `6h/pi^2`. Nathan Ng, *The Möbius function in short intervals*, in *Anatomy of Integers*, CRM Proceedings and Lecture Notes 46 (AMS, 2008), 247–257, derived conditional moment formulae from a strong Möbius tuple conjecture and formulated a corresponding normal/variance conjecture over a broad short-interval range. Keating and Rudnick (`MC-S44`) proved a function-field variance analogue, while the 2026 almost-all integer theorem `MC-S2` gives powerful logarithmic cancellation but, as `MC-175` audits, not diagonal second-moment scale at exponential resolution.

A targeted search of current Möbius short-interval, variance, second-moment, Gallagher/Selberg-integral, and 2026 almost-all literature found no unconditional integer theorem supplying `(8)` in the polynomial scales `(22)`. No novelty is claimed for the Good–Churchhouse variance scale, the Gaussian saddle, or the elementary comparison of multiplicative and additive windows.

The durable contribution here is narrower: within the already-defined Mathia Gallagher/heat construction, the desired diagonal type has a **necessary critical-shell projection** onto that classical variance problem. `MC-175` showed that a scale-uniform power-law *sufficient* envelope requires `eta=1` in the early range; the present result shows that the target itself forces diagonal-order variance at one explicit integer shell even without assuming that envelope.

## Boundaries and failure modes

This finding does not assert the asymptotic

\[
\frac1X\int_X^{2X}
\left|\sum_{y<n\le y+H}\mu(n)\right|^2dy
\sim\frac6{\pi^2}H
\]

for integers. It derives only the exponential-order upper bound `(8)` for the variable length `y/T_beta` along a heat-selected sequence of dyadic scales.

The condition is necessary, not sufficient for `(1)`. Even if the critical shell has diagonal variance, other logarithmic shells can still make `mathcal G_mu` too large. Conversely, failure to prove `(8)` with current methods is not evidence that `(8)` is false.

The restriction `tau>=1/8` is used only in the exact unweighting/additive-window comparison `(5)`, through `X_beta/T_beta^2=O(1)`. The positive-shell bound `(13)` itself exists for every fixed `tau`; below `1/8` an additional argument would be needed to identify it with an ordinary unweighted additive short sum at `O(1)` cost.

No zero-free hypothesis, analytic continuation of `1/zeta`, random-walk independence, or Good–Churchhouse conjecture is used to derive `(5)`–`(8)`.

## Consequences for the live frontier

The Gallagher branch can now be screened more sharply. For `1/8<=tau<1/4`, any proof of diagonal Gallagher type must in particular control the signed Möbius second moment on the critical shell `X~e^{1/(4beta)}` at interval length `H~X^{1-4tau}` down to diagonal exponential order.

At the strongest currently priced horizon `tau=1/8`, this means a Good–Churchhouse-order upper bound at `H~X^{1/2}`. A proposed mechanism that does not touch this shell, or only supplies logarithmic relative cancellation there, cannot prove the Gallagher target. The next useful question is therefore whether existing Dirichlet-polynomial or correlation machinery can prove any **genuinely polynomial reduction of the critical-shell second moment itself**, rather than another almost-all pointwise estimate that remains exponentially coherent.