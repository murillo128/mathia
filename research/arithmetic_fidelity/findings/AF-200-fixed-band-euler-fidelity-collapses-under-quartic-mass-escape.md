# AF-200 — Fixed-band Euler fidelity collapses under quartic mass escape at fixed Wasserstein separation

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-CONTROL`, `SOURCE-LOCALIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-197 proves a fourth-order fixed-band Euler asymptotic for each fixed five-node mirror-symmetric shape, while AF-199 identifies the Peano B-spline as the exact carrier of every minimal-support moment-flat divided-difference control. Combining those two structures exposes a stronger obstruction than nonuniformity of the Taylor remainder:

> **At fixed positive Wasserstein separation, the five-node quartic source class has no positive fixed-band Euler recovery modulus unless an additional localization resource is imposed.**

Fix

\[
x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and define

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+i\tau,
\]

using the convergent logarithmic series on `u>0`. For the AF-197 mirror-symmetric family with shape `t>0`, choose the common outer gap scale `h` so that

\[
W_1(\mu_+,\mu_-)=\delta>0.
\]

Then

\[
h=\delta\frac{(1+t)^2}{t(3t+1)}.
\tag{1}
\]

Let

\[
D_T(\delta,t)
:=
\sup_{|\tau|\le T}
\left|
\int F_{\sigma+i\tau}(u)\,d(\mu_+-\mu_-)(u)
\right|.
\tag{2}
\]

For every fixed `delta>0`,

\[
\boxed{
D_T(\delta,t)\longrightarrow0
\qquad(t\downarrow0),
}
\tag{3}
\]

although the source probabilities remain mutually singular, their moments agree through degree three, and their exact Wasserstein separation remains `delta`.

More precisely, with

\[
M_0(x,\sigma,T)
:=
\sup_{|\tau|\le T}|F_{\sigma+i\tau}(x)|>0,
\tag{4}
\]

one has

\[
\boxed{
D_T(\delta,t)
=
\frac{t^2}{2(1+t)^2}M_0(x,\sigma,T)
+O\!\left(e^{-\sigma h}\right)
}
\tag{5}
\]

as `t downarrow 0`, where `(1)` makes `h asymp delta/t` and the exponential remainder is uniform on the whole vertical band.

Consequently there is no function

\[
\phi:(0,\infty)\to(0,\infty)
\]

such that

\[
D_T(\mu_+,\mu_-)
\ge
\phi\!\left(W_1(\mu_+,\mu_-)\right)
\tag{6}
\]

for all controls in this unrestricted mirror-symmetric five-node quartic moment-flat class.

The live clue's degenerating small-scale family is an immediate specialization. Taking

\[
t=\delta^3,
\qquad \delta\downarrow0,
\tag{7}
\]

gives

\[
h=\delta^{-2}(1+o(1)),
\qquad
D_T(\delta,\delta^3)
=
\frac{M_0(x,\sigma,T)}2\,\delta^6+o(\delta^6),
\tag{8}
\]

and therefore

\[
\boxed{
\frac{D_T(\delta,\delta^3)}{\delta^4}\longrightarrow0.
}
\tag{9}
\]

Thus AF-197's fixed-shape quartic coefficient cannot be promoted to a `W_1`-only uniform or Gamma-limit principle over varying shapes.

There is also an exact positive reformulation. If `B_{\delta,t}` is the normalized Peano B-spline associated with the five knots, then for every `s` on the band,

\[
\boxed{
\frac1{\delta^4}
\int F_s\,d(\mu_+-\mu_-)
=
\frac{Q_4(t)}{24}
\int F_s^{(4)}(v)B_{\delta,t}(v)\,dv,
}
\tag{10}
\]

where

\[
Q_4(t)=\frac{(1+t)^8(2t+1)}{t^2(3t+1)^4}.
\tag{11}
\]

The normalized spline is a probability density on the knot interval and its barycenter is exactly

\[
\boxed{
\int vB_{\delta,t}(v)\,dv
=x+(1+t)h.
}
\tag{12}
\]

Since its support lies to the right of `x`,

\[
\boxed{
W_1(B_{\delta,t}(v)\,dv,\delta_x)
=(1+t)h.
}
\tag{13}
\]

Hence the missing localization variable is visible directly at the Peano-carrier level. Writing

\[
L_5(x,\sigma,T)
:=
\sup_{u\ge x,\ |\tau|\le T}
|F_{\sigma+i\tau}^{(5)}(u)|<\infty,
\tag{14}
\]

one obtains the uniform deterministic estimate

\[
\boxed{
\left|
\frac{D_T(\delta,t)}{\delta^4}
-
\frac{Q_4(t)}{24}M_4(x,\sigma,T)
\right|
\le
\frac{L_5(x,\sigma,T)}{24}
Q_4(t)(1+t)h,
}
\tag{15}
\]

where

\[
M_4(x,\sigma,T)
=
\sup_{|\tau|\le T}|F_{\sigma+i\tau}^{(4)}(x)|.
\]

Substituting `(1)` and `(11)`, the geometric error factor is

\[
\boxed{
Q_4(t)(1+t)h
=
\delta\,
\frac{(1+t)^{11}(2t+1)}
{t^3(3t+1)^5}.
}
\tag{16}
\]

Therefore a sufficient varying-shape localization condition for the fixed-shape quartic approximation to remain uniform is

\[
\delta\,
\frac{(1+t)^{11}(2t+1)}
{t^3(3t+1)^5}
\longrightarrow0.
\tag{17}
\]

In particular, `(17)` allows shape variation much wider than a compact gap-ratio assumption: near `t=0` it only asks `delta/t^3 -> 0`, while for `t -> infinity` it asks `delta t^4 -> 0` up to the constant `2/243`. This is a sufficient condition, not a sharp necessity theorem.

## Derivation

### 1. Exact Euler observation through the Peano carrier

AF-199 applies to any `m+1` ordered knots. For `m=4`, if

\[
\nu=\mu_+-\mu_-
\]

is the normalized divided-difference control, its fourth signed moment is

\[
M_4^{\rm src}=\int u^4\,d\nu(u)=\frac1A,
\]

and the normalized Peano B-spline `B` satisfies

\[
\int f(u)\,d\nu(u)
=
\frac{M_4^{\rm src}}{4!}
\int f^{(4)}(v)B(v)\,dv.
\tag{18}
\]

For the AF-197 family at exact separation `W_1=delta`,

\[
M_4^{\rm src}=Q_4(t)\delta^4,
\tag{19}
\]

so `(18)` with `f=F_s` gives `(10)` exactly. No Taylor remainder is involved.

For fixed `t`, `(1)` makes the entire spline support contract to `x` at rate `O_t(delta)`, so `(10)` recovers AF-197's fixed-shape expansion. When `t=t(delta)` degenerates, the spline need not localize and the same exact formula explains why the expansion can fail.

### 2. The fixed-Wasserstein escape

AF-197 gives the signed source explicitly:

\[
\nu
=
\alpha\delta_{u_0}
-\frac12\delta_{u_1}
+\gamma\delta_{u_2}
-\frac12\delta_{u_3}
+\alpha\delta_{u_4},
\tag{20}
\]

with

\[
\alpha=\frac{t^2}{2(1+t)^2},
\qquad
\gamma=\frac{2t+1}{(1+t)^2},
\tag{21}
\]

and knots

\[
\begin{aligned}
u_0&=x,\\
u_1&=x+h,\\
u_2&=x+(1+t)h,\\
u_3&=x+(1+2t)h,\\
u_4&=x+(2+2t)h.
\end{aligned}
\tag{22}
\]

Fix `delta>0` and let `t downarrow 0` while choosing `h` by `(1)`. Then

\[
h\sim\frac\delta t\to\infty,
\tag{23}
\]

so every knot except `u_0=x` escapes to `+infinity`.

For `u>0`, the absolutely convergent series

\[
F_s(u)=\sum_{k\ge1}\frac{e^{-ksu}}k
\tag{24}
\]

implies, uniformly for `|tau|<=T`,

\[
|F_s(u)|
\le
\sum_{k\ge1}\frac{e^{-k\sigma u}}k
=-\log(1-e^{-\sigma u})
\le
\frac{e^{-\sigma u}}{1-e^{-\sigma u}}.
\tag{25}
\]

The total variation of `nu` is `2`, because its positive and negative parts are probabilities. Hence the contribution of the four escaping atoms is bounded uniformly by

\[
2\frac{e^{-\sigma(x+h)}}{1-e^{-\sigma(x+h)}}
=O(e^{-\sigma h}).
\tag{26}
\]

Therefore

\[
\int F_s\,d\nu
=
\alpha F_s(x)+O(e^{-\sigma h})
\tag{27}
\]

uniformly on the vertical band. Taking suprema and using `alpha~t^2/2` proves `(5)` and `(3)`. Since `W_1=delta` identically by construction, `(6)` is impossible.

For `t=delta^3`, equations `(1)`, `(21)`, and `(26)` give

\[
h=\delta^{-2}(1+o(1)),
\qquad
\alpha=\frac12\delta^6+O(\delta^9),
\]

while the escaping-atom contribution is superalgebraically smaller than `delta^6`. This proves `(8)`--`(9)`.

### 3. Peano-carrier barycenter and a usable sufficient localization gate

The barycenter identity `(12)` is itself exact and general. For an order-`m` normalized Peano B-spline on knots `u_0,...,u_m`, apply the divided-difference Peano formula to

\[
f(u)=u^{m+1}.
\]

The divided difference is the complete homogeneous polynomial of degree one,

\[
f[u_0,\ldots,u_m]=\sum_{j=0}^m u_j,
\]

while

\[
f^{(m)}(v)=(m+1)!v.
\]

Since `B=m!K`, one obtains

\[
\int vB(v)\,dv
=
\frac1{m+1}\sum_{j=0}^m u_j.
\tag{28}
\]

For the five symmetric knots `(22)`, their arithmetic mean is `x+(1+t)h`, proving `(12)`. Because `B` is supported on `[x,u_4]`, `(13)` follows immediately.

Finally, differentiating the series `(24)` five times shows that `(14)` is finite:

\[
|F_s^{(5)}(u)|
\le
|s|^5\sum_{k\ge1}k^4e^{-k\sigma x}
\qquad(u\ge x,\ |\tau|\le T).
\tag{29}
\]

Thus `F_s^{(4)}` is uniformly Lipschitz on the entire half-line `u>=x`. By `(13)`,

\[
\left|
\int F_s^{(4)}(v)B(v)\,dv-F_s^{(4)}(x)
\right|
\le
L_5(1+t)h.
\tag{30}
\]

Combine `(10)` with `(30)`, take suprema over the band, and use the elementary inequality between sup norms to obtain `(15)`. Equation `(16)` is then direct substitution.

## Consequences for the source-class frontier

The obstruction is not that the Euler logarithm lacks enough derivatives. It is that **`W_1` controls transport cost of the signed source but does not prevent the Peano carrier from escaping to a region where the fixed-band Euler test family is exponentially insensitive**. A tiny amount of source imbalance transported over a huge distance can maintain fixed `W_1` while the declared observation collapses.

This separates three resources that had been conflated in the fixed-shape analysis:

- cancellation order and minimal support determine the divided-difference coefficient pattern;
- exact `W_1` fixes one transport scale;
- Peano-carrier localization controls whether the local derivative profile at `x` is actually sampled by the observation.

The correct residual problem from `CLUE-quartic-euler-localization-uniformity` is therefore narrower. A full source-class converse must impose or derive an equicoercive localization condition strong enough to prevent `(20)`--`(23)`, then determine whether the resulting full Euler objectives have compact sublevels and converge uniformly enough to inherit the homogeneous `Q_4` optimizer. Equation `(17)` is one explicit sufficient gate inside the symmetric family, but no claim is made that it is weakest or that it solves the unrestricted four-gap problem.

The fixed-Wasserstein obstruction also prevents a common overinterpretation of the compute-backed homogeneous optimizer: even a globally sharp minimizer of `Q_4` modulo scale cannot control the full fixed-band Euler discrepancy unless the source class prevents escape of the associated Peano carrier.

## Prior art and novelty assessment

The Peano-kernel and B-spline identities used in `(10)`, `(18)`, and `(28)` are classical and were already audited in AF-199 against Carl de Boor's divided-difference survey and the classical optimal-recovery/spline literature. The general distinction between a restricted test-family discrepancy and a transport metric is likewise standard integral-probability-metric territory: a smaller decaying test family need not control the full 1-Lipschitz witness class defining `W_1`, especially without a tightness or moment condition. The role of equicoercivity in passing from pointwise variational limits to minimizer convergence is also standard Gamma-convergence machinery.

A targeted search across Peano kernels, divided differences, moment matching, Wasserstein/IPM comparisons, and Gamma-convergence did not justify presenting any of those general principles as new. No novelty claim is made for them. The durable result here is the exact specialization to the AF five-node quartic arithmetic control: formulas `(3)`--`(9)` give an explicit fixed-`W_1` escape inside the already-defined source class, and `(10)`--`(17)` identify the corresponding Peano-carrier localization resource and a strictly weaker sufficient gate than compact gap-ratio control.

## Boundaries

- The result concerns fixed `sigma>0` and finite vertical bandwidth `T`. It does not address bands growing with the escaping source scale.
- The control is a matched positive atomic source, not the rational primes. No prime-specificity or RH consequence follows.
- Equation `(17)` is sufficient, not necessary. Cancellation inside the weighted Peano average may permit weaker observation-specific conditions.
- The result is proved inside the AF-197 mirror-symmetric family. That is enough to kill a `W_1`-only lower modulus for the larger unrestricted five-node class, but it does not classify all escaping unrestricted shapes.
- The homogeneous `Q_4` optimization and the full Euler minimization are different problems. This finding does not alter the homogeneous optimum; it shows why localization is required before transferring it to the full observable.
