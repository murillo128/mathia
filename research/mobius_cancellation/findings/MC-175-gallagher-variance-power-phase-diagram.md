# MC-175 — Gallagher local-variance power has an exact heat-type phase diagram

**Status:** `EXACT-DERIVED`, `FRONTIER-RESTRICTION`, `RATE-BUDGET`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The live Gallagher target of `MC-172` admits an exact interpolation between the trivial coherent local scale and square-root local variance. This quantifies how much *polynomial* cancellation a short-interval second-moment theorem would have to supply before it can force the Gallagher energy down to diagonal heat type.

Let

\[
T_\beta=e^{\tau/\beta},
\qquad
\mathcal G_\mu(\beta,T_\beta)
=
T_\beta\int_1^\infty
\left|
\sum_{y<n\le ye^{1/T_\beta}}
\mu(n)e^{-\beta(\log n)^2}
\right|^2\frac{dy}{y}.
\tag{1}
\]

Normalize away the Gaussian value at the left endpoint,

\[
B_{\beta,\tau}(y)
:=
e^{\beta(\log y)^2}
\sum_{y<n\le ye^{1/T_\beta}}
\mu(n)e^{-\beta(\log n)^2},
\tag{2}
\]

and for dyadic `X=2^k` put

\[
H_X:=\frac{X}{T_\beta},
\qquad
J_{\beta,\tau}(X)
:=
\int_X^{2X}|B_{\beta,\tau}(y)|^2\frac{dy}{y}.
\tag{3}
\]

Fix `0<=eta<=1`. Consider the scale-uniform variance envelope

\[
\boxed{
J_{\beta,\tau}(X)
\le
R_\beta\left(H_X+H_X^{2-\eta}\right)
\quad\text{for every dyadic }X\ge1,
}
\tag{4}
\]

where the loss is subexponential on the heat scale,

\[
\limsup_{\beta\downarrow0}\beta\log R_\beta\le0.
\tag{5}
\]

The two terms in `(4)` have a direct variance interpretation. `H_X` is the diagonal/sparse-window scale; `H_X^2` is coherent size. Thus `eta=0` is the trivial coherent envelope, while `eta=1` is square-root local second-moment scaling. Intermediate `eta` encodes a fixed power saving over coherent variance when `H_X` is large.

Under `(4)`–`(5)`, one has

\[
\boxed{
\limsup_{\beta\downarrow0}
\beta\log\mathcal G_\mu(\beta,T_\beta)
\le
\max\!\left(
\frac18,
\kappa_\eta(\tau)
\right),
}
\tag{6}
\]

with

\[
\boxed{
\kappa_\eta(\tau)
=
\frac{(2-\eta)^2}{8}
-(1-\eta)\tau.
}
\tag{7}
\]

Moreover

\[
\boxed{
\kappa_\eta(\tau)-\frac18
=
(1-\eta)
\left(\frac{3-\eta}{8}-\tau\right).
}
\tag{8}
\]

Therefore the diagonal target of `MC-172`,

\[
\limsup_{\beta\downarrow0}
\beta\log\mathcal G_\mu(\beta,T_\beta)
\le\frac18,
\tag{9}
\]

is forced by this power-law envelope exactly in the following regimes:

- `eta=1`: square-root local variance suffices for every fixed `tau`;
- `0<=eta<1`: the envelope suffices precisely when
  \[
  \tau\ge\frac{3-\eta}{8}.
  \tag{10}
  \]

In particular, throughout the analytically useful early range

\[
\frac18\le\tau\le\frac14,
\tag{11}
\]

**no fixed interpolation exponent `eta<1` can force diagonal type through `(4)`; square-root local variance is required within this entire power-law information class.** Only for

\[
\frac14<\tau<\frac38
\]

does a weaker fixed power saving suffice, with threshold

\[
\eta\ge 3-8\tau.
\tag{12}
\]

Combining `(9)` with `MC-174` also prices the analytic consequence. For `1/8<=tau<3/8`, any instance of `(4)` strong enough to satisfy `(9)` yields

\[
\zeta(s)\ne0
\qquad
\left(
\operatorname{Re}s>\sqrt{\frac14+2\tau}
\right).
\tag{13}
\]

Hence a fixed power improvement in this *particular signed local second-moment currency* is already expensive. For `0<eta<1`, choosing the first horizon permitted by `(10)`,

\[
\tau=\frac{3-\eta}{8},
\]

would give the fixed zero-free half-plane

\[
\boxed{
\operatorname{Re}s>\sqrt{1-\frac\eta4}.
}
\tag{14}
\]

This is a conditional pricing statement, not a claim that such an integer Möbius variance theorem is known. At `eta=0`, `(14)` degenerates to the boundary `Re(s)>1`; any genuinely positive fixed `eta` would already move the boundary strictly left of `1`.

## 1. The diagonal plus coherent envelope is the natural interpolation

The normalization `(2)` is exact:

\[
\left|
\sum_{y<n\le ye^{1/T_\beta}}
\mu(n)e^{-\beta(\log n)^2}
\right|^2
=
e^{-2\beta(\log y)^2}|B_{\beta,\tau}(y)|^2.
\tag{15}
\]

For `n>y>=1`, the normalized coefficient has modulus at most one because

\[
e^{\beta(\log y)^2-\beta(\log n)^2}\le1.
\]

Consequently the `eta=0` version of `(4)` is available for every bounded coefficient sequence, up to an absolute constant. Indeed, if

\[
N_T(y)=\#\{n:y<n\le ye^{1/T}\},
\]

then on `X<=y<=2X`,

\[
N_T(y)\ll 1+\frac XT.
\tag{16}
\]

Also, by Fubini, each integer contributes for logarithmic `y`-measure at most `1/T`, so

\[
\int_X^{2X}N_T(y)\frac{dy}{y}
\ll \frac XT.
\tag{17}
\]

Since `|B|<=N_T`, equations `(16)`–`(17)` give

\[
J_{\beta,\tau}(X)
\ll
\left(1+\frac XT\right)\frac XT
\ll H_X+H_X^2.
\tag{18}
\]

Thus `eta=0` is not a probabilistic heuristic; it is the deterministic boundedness baseline. Replacing `H_X^2` by `H_X^{2-eta}` asks for a genuine fixed-power suppression of coherent local mass while retaining the unavoidable diagonal/sparse-window term `H_X`.

At `eta=1`, `(4)` becomes

\[
J_{\beta,\tau}(X)\ll R_\beta H_X,
\tag{19}
\]

which is precisely square-root variance scale after logarithmic averaging over starting points. The interpolation has therefore been normalized so that its two endpoints correspond to the two exact scales already separated in `MC-172`.

## 2. Dyadic Gaussian summation gives the exponent dictionary

From `(15)` and a dyadic decomposition,

\[
\begin{aligned}
\mathcal G_\mu(\beta,T_\beta)
&=T_\beta
\sum_{k\ge0}
\int_{2^k}^{2^{k+1}}
 e^{-2\beta(\log y)^2}
 |B_{\beta,\tau}(y)|^2\frac{dy}{y}\\
&\le
T_\beta R_\beta
\sum_{k\ge0}
 e^{-2\beta(k\log2)^2}
\left(H_k+H_k^{2-\eta}\right),
\end{aligned}
\tag{20}
\]

where

\[
H_k=\frac{2^k}{T_\beta}.
\]

The diagonal term simplifies to

\[
T_\beta H_k=2^k,
\]

while the power-saving coherent term is

\[
T_\beta H_k^{2-\eta}
=
2^{k(2-\eta)}T_\beta^{\eta-1}.
\tag{21}
\]

For every fixed `a>0`, completing the square or comparing the sum with its Gaussian integral gives the elementary Laplace law

\[
\lim_{\beta\downarrow0}
\beta\log
\sum_{k\ge0}
\exp\!\left(
 a k\log2-2\beta(k\log2)^2
\right)
=
\frac{a^2}{8}.
\tag{22}
\]

Apply `(22)` first with `a=1`. The first term in `(20)` has exponential type `1/8`. Apply it again with `a=2-eta`, and use

\[
T_\beta^{\eta-1}
=
\exp\!\left(-\frac{(1-\eta)\tau}{\beta}\right).
\]

The second term has type exactly the upper-budget exponent `(7)`. The subexponential factor `R_beta` does not change either type by `(5)`. This proves `(6)`.

The factorization `(8)` is algebraic:

\[
\begin{aligned}
\kappa_\eta(\tau)-\frac18
&=
\frac{(2-\eta)^2-1}{8}-(1-\eta)\tau\\
&=(1-\eta)
\left(\frac{3-\eta}{8}-\tau\right).
\end{aligned}
\]

For `eta=1` the excess vanishes identically. For `eta<1` its sign is therefore determined exactly by `(10)`.

## 3. The relevant local scale moves with the variance exponent

The second term in `(20)` is concentrated at the Gaussian saddle

\[
\log X_{\eta,\beta}
=
\frac{2-\eta}{4\beta}.
\tag{23}
\]

At that saddle,

\[
T_\beta
=
X_{\eta,\beta}^{\,4\tau/(2-\eta)},
\]

so the multiplicative-window length is

\[
H_{\eta,\beta}
\asymp
X_{\eta,\beta}^{\theta_\eta(\tau)},
\qquad
\boxed{
\theta_\eta(\tau)
=1-\frac{4\tau}{2-\eta}.
}
\tag{24}
\]

This matters when comparing `(4)` with ordinary short-interval theorems: the relevant `X` is not fixed while the cancellation exponent changes. The `eta=0` coherent saddle of `MC-172` gives

\[
\theta_0(\tau)=1-2\tau.
\tag{25}
\]

At the threshold horizon `(10)` for `0<eta<1`, the corresponding local-window exponent is

\[
\boxed{
\theta_\eta
=
\frac{1-\eta}{2(2-\eta)}.
}
\tag{26}
\]

For example, `eta=1/3` reaches diagonal heat type at `tau=1/3`, where the relevant power-law local scale is `H\asymp X^{1/5}`. This is only an exponent dictionary: it does not assert that the required `eta=1/3` Möbius second-moment estimate is available at that scale.

## 4. Present almost-all technology is still `eta=0` at exponential resolution

The 2026 almost-all theorem `MC-S2`, already audited in `MC-001` and `MC-172`, gives in its quantitative Möbius range a pointwise short-sum estimate

\[
\left|\sum_{x<n\le x+H}\mu(n)\right|
\ll_A H(\log X)^{-A}
\tag{27}
\]

outside an exceptional set of measure

\[
\ll_A X(\log X)^{-A}.
\tag{28}
\]

Using trivial size `H` on the exceptional set and dividing the resulting second-moment integral by `X`, the retained theorem data give only a budget of the form

\[
H^2(\log X)^{-A}
\tag{29}
\]

up to changing the fixed logarithmic exponent. This is a very strong almost-all statement, but in the power taxonomy `(4)` it remains `eta=0`: for every fixed `eta>0` and every polynomial window `H=X^\theta`,

\[
\frac{H^2(\log X)^{-A}}{H^{2-\eta}}
=
\frac{X^{\theta\eta}}{(\log X)^A}
\longrightarrow\infty.
\tag{30}
\]

At the `eta=0` heat saddle, `X\asymp e^{1/(2\beta)}`. Any fixed logarithmic saving in `(29)` contributes only

\[
\beta\log(\log X)^{-A}=o(1),
\tag{31}
\]

so it does not change the heat exponential type `1/2-tau` of the coherent term. This formalizes the statement made qualitatively in `MC-172`: the published logarithmic almost-all saving is exponentially invisible to the Gallagher target.

The quantitative `MC-S2` threshold `H>=X^{1/3+epsilon}` corresponds at this coherent saddle to

\[
1-2\tau\ge\frac13+\epsilon,
\qquad
\tau\le\frac13-\frac\epsilon2.
\tag{32}
\]

Thus the theorem reaches a substantial part of the live `tau<3/8` geometry, but its *rate class* is the obstruction there, not merely its interval-length threshold.

## 5. Zero-free pricing of a hypothetical fixed power gain

`MC-174` proves that for `1/8<=tau<3/8`, diagonal Gallagher type `(9)` transports through fixed vertical twists and heat subordination to the zero-free half-plane `(13)`.

For a hypothetical fixed `0<eta<1` satisfying `(4)` uniformly at the required Gaussian scales, the earliest horizon at which the power envelope reaches diagonal type is

\[
\tau_\eta=\frac{3-\eta}{8}.
\tag{33}
\]

Substitution into the `MC-174` boundary gives

\[
\sqrt{\frac14+2\tau_\eta}
=
\sqrt{1-\frac\eta4},
\]

which is `(14)`. Therefore even a modest *fixed power* improvement over coherent local second moment, if available in the precise signed scale-uniform currency `(4)`, would already imply a fixed zero-free half-plane.

This explains why replacing `(27)` by a slightly larger logarithmic exponent cannot alter the frontier. The qualitative jump is not “better almost-all cancellation” but a change from subpower to fixed-power suppression of the signed local quadratic energy, with uniformity across the Gaussian saddle family.

The endpoint `eta=1` is special. Since `(8)` vanishes identically, square-root variance would give diagonal heat type for every horizon. Within the twist-stable range of `MC-174`, taking the smallest robust horizon `tau=1/8` would yield its strongest currently priced consequence

\[
\operatorname{Re}s>\frac1{\sqrt2}.
\tag{34}
\]

No such integer Möbius square-root variance theorem is asserted here.

## Prior art and novelty assessment

Gallagher's localization and the relation between Dirichlet-polynomial mean values and short-interval quadratic means are classical (`MC-S42`, `MC-S43`). Modern Möbius short-interval theory, including the quantitative almost-all theorem `MC-S2`, is established prior art. `MC-172` already identified the exact signed Gallagher energy and its diagonal/all-plus `tau=3/8` boundary, while `MC-174` priced diagonal control by the resulting zero-free half-plane.

A targeted literature search for Möbius short-interval mean square, Gallagher/Selberg-integral formulations, and recent short-interval variance results found these established languages and the function-field variance analogue `MC-S44`, but no basis for claiming the interpolation law `(6)`–`(12)` as a new theorem of analytic number theory. The derivation is elementary once the `MC-172` heat/Gallagher scaling is fixed.

The durable contribution is therefore a **line-specific rate budget**: it turns the vague requirement “obtain substantially stronger short-interval cancellation” into an exact two-parameter threshold between local second-moment power `eta` and heat horizon `tau`, and shows that present logarithmic almost-all savings remain in the trivial `eta=0` heat class.

## Boundaries and failure modes

This finding is conditional on the scale-uniform variance envelope `(4)`. It does not prove that such an envelope holds for Möbius for any `eta>0`.

The envelope is deliberately a sufficient information class, not a claim of necessity among all possible mechanisms. A signed correlation identity could in principle control `mathcal G_mu` more efficiently than an absolute local second-moment majorant of the form `(4)`. Conversely, an `H^{2-eta}` estimate proved only on one sparse family of `X`, only after smoothing that loses the dangerous scales, or with an exceptional set carrying exponential heat mass does not satisfy `(4)`.

The subexponential uniformity in `(5)` is essential. A hidden loss `R_beta=exp(c/beta)` simply adds `c` to the heat type and can erase the claimed gain. Likewise, a fixed-power saving at an interval scale different from the saddle `(24)` cannot be inserted without a separate scale-transfer argument.

No converse to `(13)` or `(14)` is asserted. A fixed zero-free half-plane need not imply the local variance envelope `(4)`, and the result does not identify the true optimal route to RH.

## Consequences for the live frontier

The `MC-172` question can now be screened by a quantitative rule. A candidate short-interval theorem should be translated into a dyadic exponent `eta` and checked at the moving saddle `(24)` before any heat or spectral interpretation is attempted.

For `1/8<=tau<=1/4`, a black-box power-law second-moment route must reach square-root scale `eta=1`; sub-square-root fixed power savings are insufficient. For later horizons `1/4<tau<3/8`, partial fixed-power savings can reach diagonal type, but `MC-174` shows that success is already strong enough to force a nontrivial fixed zero-free half-plane. Present logarithmic almost-all results remain below this threshold.

So the next useful attack on the Gallagher branch is not another qualitative short-interval cancellation theorem. It must either produce a genuinely fixed-power signed variance gain with the required scale uniformity, or bypass the envelope `(4)` by exploiting phase-sensitive structure that controls the near-diagonal energy more directly.