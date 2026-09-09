# MC-177 — Gallagher diagonal energy directly forces Mertens power cancellation

**Status:** `EXACT-DERIVED`, `FRONTIER-RESTRICTION`, `DIRECT-TRANSFER`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The diagonal Gallagher target of `MC-172` has a direct real-variable consequence that is stronger than the single critical-shell restriction in `MC-176`: it already forces a fixed power bound for the global Mertens function, with exactly the same exponent that `MC-174` reached through vertical twists, heat-semigroup smoothing, and Poisson subordination.

Fix

\[
\frac18\le\tau<\frac38,
\qquad
T_\beta=e^{\tau/\beta},
\]

and assume

\[
\limsup_{\beta\downarrow0}
\beta\log\mathcal G_\mu(\beta,T_\beta)
\le\frac18.
\tag{1}
\]

Then for every `epsilon>0`,

\[
\boxed{
M(x)\ll_{\epsilon,\tau}
x^{\alpha_\tau+\epsilon},
\qquad
\alpha_\tau:=\sqrt{\frac14+2\tau}.
}
\tag{2}
\]

Consequently

\[
\boxed{
\zeta(s)\ne0
\qquad
\text{for}\qquad
\operatorname{Re}s>\alpha_\tau.
}
\tag{3}
\]

The proof uses only positivity of the Gallagher integral, elementary removal of the Gaussian coefficient on one shell, an exact multiplicative-window boundary identity for `M`, Cauchy--Schwarz, and the classical Dirichlet/Abel implication from a Mertens power bound to zeta nonvanishing. It does **not** require the fixed vertical-twist transport or heat/Poisson continuation argument used in `MC-174`.

At the earliest twist-stable horizon `tau=1/8`, `(2)` gives

\[
M(x)\ll_\epsilon x^{1/\sqrt2+\epsilon}.
\tag{4}
\]

Thus the difficulty priced in `MC-174` is already inherent in the untwisted signed local energy. Proving diagonal Gallagher type is not merely proving a local variance estimate and then paying an analytic-continuation cost later: the full positive shell family itself contains enough information to force a major global Mertens power saving.

A second, more general consequence makes the local-to-global budget explicit. Suppose for some fixed `0<theta<1` and `0<eta<=1`, with `H=X^theta`, one had uniformly for all sufficiently large `X`

\[
\int_X^{2X}
\left|M\!\left(ye^{1/T}\right)-M(y)\right|^2
\frac{dy}{y}
\le
X^{o(1)}\bigl(H+H^{2-\eta}\bigr),
\qquad T=\frac XH.
\tag{5}
\]

Then

\[
\boxed{
M(x)
\ll
x^{\max(1-\theta\eta/2,\,\theta)+o(1)}.
}
\tag{6}
\]

Hence **any fixed-power suppression of coherent short-interval second moment, if uniform at one fixed polynomial window scale, already implies a fixed global Mertens power saving.** This explains why the currently proved logarithmic or `o(1)` relative short-interval gains do not cross the same threshold.

## 1. A positive Gallagher shell gives a quantitative local `L^2` bound

For `T>=1`, define on a shell `X<=y<=2X`

\[
B_{\beta,T}(y)
:=
e^{\beta(\log y)^2}
\sum_{y<n\le ye^{1/T}}
\mu(n)e^{-\beta(\log n)^2}.
\tag{7}
\]

Then the Gallagher energy from `MC-172` is

\[
\mathcal G_\mu(\beta,T)
=
T\int_0^\infty
 e^{-2\beta(\log y)^2}
 |B_{\beta,T}(y)|^2\frac{dy}{y}.
\tag{8}
\]

Every shell contribution is nonnegative. Therefore

\[
\mathcal G_\mu(\beta,T)
\ge
T e^{-2\beta(\log(2X))^2}
J_{\beta,T}(X),
\tag{9}
\]

where

\[
J_{\beta,T}(X)
:=
\int_X^{2X}|B_{\beta,T}(y)|^2\frac{dy}{y}.
\tag{10}
\]

Now let `c>tau` be fixed and, for arbitrary large `X`, choose

\[
\beta=\frac c{\log X},
\qquad
T=T_\beta=X^{\tau/c}.
\tag{11}
\]

From `(1)`,

\[
\mathcal G_\mu(\beta,T)
\le
X^{1/(8c)+o(1)}.
\tag{12}
\]

Also

\[
e^{2\beta(\log(2X))^2}
=X^{2c+o(1)},
\qquad
T^{-1}=X^{-\tau/c}.
\]

Hence `(9)` gives

\[
\boxed{
J_{\beta,T}(X)
\le
X^{\,2c+(1/8-\tau)/c+o(1)}.
}
\tag{13}
\]

Unlike `MC-176`, this shell is not fixed at the diagonal Gaussian saddle `beta log X=1/4`. Here `beta log X=c` remains a free constant and will be optimized against the boundary reconstruction of `M`.

## 2. Gaussian removal and an exact multiplicative boundary identity

Set

\[
q=e^{1/T},
\qquad
S_T(y):=
\sum_{y<n\le qy}\mu(n)
=M(qy)-M(y).
\tag{14}
\]

For `X<=y<=2X` and `y<n<=qy`, write `delta=log(n/y)`. Then `0<delta<=1/T`, while `beta log y=O_c(1)`. Therefore

\[
\beta\bigl((\log n)^2-(\log y)^2\bigr)
=O_c(1/T),
\]

and so

\[
\left|
B_{\beta,T}(y)-S_T(y)
\right|
\ll_c
\frac1T+\frac X{T^2}.
\tag{15}
\]

The logarithmic shell has fixed measure `log 2`, hence

\[
\|S_T\|_{L^2([X,2X],dy/y)}
\le
J_{\beta,T}(X)^{1/2}
+O_c\!\left(\frac1T+\frac X{T^2}\right).
\tag{16}
\]

The unweighted local sum has an exact boundary reconstruction. Put

\[
I(X,T)
:=
\int_X^{2X}S_T(y)\frac{dy}{y}.
\]

Changing variables `u=qy` in the first term of `(14)` gives

\[
I(X,T)
=
\int_{2X}^{2qX}M(u)\frac{du}{u}
-
\int_X^{qX}M(u)\frac{du}{u}.
\tag{17}
\]

Since `log q=1/T` exactly and the increments of `M` satisfy

\[
|M(v)-M(u)|\le |v-u|+1,
\]

one obtains

\[
\boxed{
I(X,T)
=
\frac{M(2X)-M(X)}{T}
+O\!\left(\frac X{T^2}+\frac1T\right).
}
\tag{18}
\]

Cauchy--Schwarz on the fixed logarithmic shell, followed by `(16)`, therefore yields

\[
\boxed{
|M(2X)-M(X)|
\ll_c
T J_{\beta,T}(X)^{1/2}
+rac XT+1.
}
\tag{19}
\]

This is the key local-to-global step. It uses the **signed** local sum itself before any absolute-value averaging has erased its boundary orientation.

## 3. Optimizing the shell recovers the `MC-174` exponent directly

Insert `(13)` into `(19)`. Since `T=X^{\tau/c}`,

\[
T J_{\beta,T}(X)^{1/2}
\le
X^{a_\tau(c)+o(1)},
\tag{20}
\]

with

\[
\boxed{
a_\tau(c)
=
c+
\frac{1/16+\tau/2}{c}.
}
\tag{21}
\]

The elementary boundary term is

\[
\frac XT=X^{b_\tau(c)},
\qquad
b_\tau(c)=1-\frac\tau c.
\tag{22}
\]

The first exponent is minimized at

\[
c=c_\tau
:=
\sqrt{\frac1{16}+\frac\tau2}
=
\frac{\alpha_\tau}{2},
\tag{23}
\]

where

\[
a_\tau(c_\tau)=2c_\tau=\alpha_\tau.
\tag{24}
\]

For `1/8<=tau<3/8`, one has `c_tau>tau`, so the local window length tends to infinity. In the same range,

\[
b_\tau(c_\tau)<\alpha_\tau.
\tag{25}
\]

For example, `(25)` follows after multiplying by `c_tau` from

\[
c_\tau<\frac18+2\tau,
\]

whose square is valid throughout `tau>=1/8` because `4tau^2>3/64` there.

Thus `(19)` at the optimized shell gives, for every `epsilon>0`,

\[
M(2X)-M(X)
\ll_{\epsilon,\tau}
X^{\alpha_\tau+\epsilon}.
\tag{26}
\]

The scale `X` was arbitrary. Summing `(26)` over the dyadic telescoping chain

\[
M(x)
=
\sum_{j\ge1}
\left(
M(x/2^{j-1})-M(x/2^j)
\right)
+O(1)
\]

proves `(2)`.

The classical Dirichlet/Abel argument then makes

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}
\]

holomorphic for `Re(s)>alpha_tau`; it agrees with `1/zeta(s)` for `Re(s)>1`. Hence zeta has no zero in the larger half-plane, proving `(3)`.

The equality of `(3)` with the boundary in `MC-174` is therefore structural, not accidental. `MC-174` extracted the exponent through a spectral-time route; the present argument shows that the same exponent is already encoded in the real-variable shell/boundary geometry of `mathcal G_mu`.

## 4. General variance-to-Mertens transfer budget

The boundary identity `(18)` is useful independently of the Gaussian heat family. Let

\[
H:=\frac XT,
\qquad
J_S(X,T)
:=
\int_X^{2X}|S_T(y)|^2\frac{dy}{y}.
\]

Then `(18)` and Cauchy--Schwarz give the deterministic inequality

\[
\boxed{
|M(2X)-M(X)|
\ll
\frac XH J_S(X,T)^{1/2}
+H+1.
}
\tag{27}
\]

Suppose `H=X^theta` and the local second moment obeys the fixed-power envelope `(5)`. Since `0<eta<=1`,

\[
J_S(X,T)^{1/2}
\le
X^{o(1)}H^{1-\eta/2},
\]

so `(27)` becomes

\[
|M(2X)-M(X)|
\le
X^{o(1)}
\left(
XH^{-\eta/2}+H
\right).
\tag{28}
\]

Dyadic telescoping proves `(6)`.

This gives an exact information threshold. For every fixed `eta>0` and `0<theta<1`, both exponents

\[
1-\frac{\theta\eta}{2}
\quad\text{and}\quad
\theta
\]

are strictly below `1`. Thus a uniform fixed-power variance improvement at any fixed polynomial local scale would already be a fixed-power global Mertens theorem. At square-root variance `eta=1`, the elementary boundary transfer is optimized at `theta=2/3`, where it would give `M(x)<=x^{2/3+o(1)}`. At the `MC-176` critical shell `theta=1/2`, the same generic transfer gives only `x^{3/4+o(1)`; the stronger `1/sqrt(2)` exponent from `(4)` uses the **full Gallagher target across shells** and optimizes at the different shell `c_tau=1/(2sqrt2)` when `tau=1/8`.

This distinction is important: controlling one Good--Churchhouse-order shell is a necessary fragment of the Gallagher target, but it is not equivalent to controlling the full target.

## Prior art and novelty assessment

Gallagher localization itself is classical (`MC-S42`), and its Dirichlet/Selberg-integral formulation is recorded in `MC-S43`. The implication from a Mertens power bound to zeta nonvanishing is classical Abel/Dirichlet theory. No novelty is claimed for these ingredients, for Cauchy--Schwarz, or for the elementary boundary averaging identity `(18)` as a general analytic device.

The current integer short-interval literature does not make `(5)` available with a fixed positive `eta` in the relevant unconditional ranges. `MC-S2` gives very strong almost-all Möbius cancellation but only logarithmic normalized saving at its quantitative level, which remains `eta=0` in the power taxonomy already audited in `MC-175`. A current literature check also includes Matomäki and Teräväinen, *On the Möbius function in all short intervals*, J. Eur. Math. Soc. 25 (2023), 1207–1225, DOI `10.4171/JEMS/1205`: their uniform result gives `o(H)` for `H=x^theta`, `theta>0.55`, not a fixed-power saving of the form needed in `(5)`.

Targeted searches around Möbius short-interval mean squares, Mertens increments, Gallagher/Selberg integrals, and local-to-global variance transfer did not locate the exact optimized implication `(1) -> (2)` as a standalone theorem. **No novelty claim is made.** The durable contribution is the line-specific composition and difficulty calibration: the same Gallagher target previously priced spectrally in `MC-174` already contains a direct global Mertens power theorem before any spectral-time continuation step.

## Boundaries and falsification controls

This finding does not prove `(1)`, any fixed positive `eta` instance of `(5)`, or a new unconditional Mertens exponent. It prices what such estimates would imply.

The conclusion `(2)` uses the **full** asymptotic Gallagher bound `(1)` for every sufficiently small `beta`, because arbitrary large `X` is encoded through `beta=c_tau/log X`. A bound known only on a sparse sequence of `beta` values would not automatically give the uniform global conclusion.

The local energy must retain the signed Möbius orientation. A support-only or phase-blind quadratic statistic such as the autocorrelation classified in `MC-173` cannot be substituted into `(19)` without an additional signed reconstruction.

The Gaussian removal error is carried explicitly in `(15)`–`(19)`; no bounded-offset shell assumption from the currently reviewed `MC-176` argument is used. In particular, the derivation remains independent of the shell-selection repair there.

Equation `(6)` requires a uniform local variance estimate for all sufficiently large `X` at the stated polynomial scale. Almost-all control with an exceptional set, logarithmic averaging, or a sparse scale subsequence cannot be inserted silently.

No analytic continuation or zero-free region for `1/zeta` is used to derive the Mertens bound `(2)`. Zeta enters only after the global arithmetic bound has already been obtained, through the standard one-way consequence `(2) -> (3)`.

## Consequence for the live frontier

`MC-176` identified a necessary Good--Churchhouse-order critical shell. The present result shows that the more ambitious full `MC-172` diagonal target is globally expensive even before one invokes the spectral machinery of `MC-174`: at `tau=1/8` it already contains a direct `M(x)<<x^{1/sqrt(2)+epsilon}` theorem.

The frontier should therefore distinguish two questions sharply. One may search for **partial polynomial improvement of a concrete short-interval second moment**, which is already consequential by `(6)` but does not require the full heat target. Or one may continue toward the full Gallagher diagonal type, in which case any proposed proof mechanism must be commensurate with a fixed global Mertens power saving and cannot plausibly be supplied by present logarithmic almost-all technology alone.