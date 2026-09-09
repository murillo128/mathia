# MC-177 — Gallagher diagonal energy directly forces Mertens power cancellation

**Status:** `EXACT-DERIVED`, `FRONTIER-RESTRICTION`, `DIRECT-TRANSFER`, `BOUNDARY-OPTIMIZATION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The diagonal Gallagher target of `MC-172` has a direct real-variable consequence stronger than the single critical-shell restriction in `MC-176`. It forces a fixed power bound for the global Mertens function without the fixed vertical-twist transport, heat-semigroup smoothing, or Poisson subordination used in `MC-174`.

Fix

\[
0<\tau<\frac38,
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

For every fixed `c>tau`, define

\[
a_\tau(c)
:=c+\frac{1/16+\tau/2}{c},
\qquad
b_\tau(c):=1-\frac\tau c,
\qquad
r_\tau(c):=\max\{a_\tau(c),b_\tau(c)\}.
\tag{2}
\]

Then for every `epsilon>0`,

\[
\boxed{
M(x)\ll_{\epsilon,\tau,c}x^{r_\tau(c)+\epsilon}.
}
\tag{3}
\]

Consequently

\[
\boxed{
\zeta(s)\ne0
\qquad
\text{for}\qquad
\operatorname{Re}s>r_\tau(c).
}
\tag{4}
\]

The best exponent delivered by this one-shell Gallagher/boundary transfer is

\[
\rho(\tau):=\inf_{c>\tau}r_\tau(c).
\tag{5}
\]

Put

\[
\tau_*:=\frac{\sqrt3}{16}.
\tag{6}
\]

For `0<tau<tau_*`, let

\[
c_-(\tau)
:=
\frac{1-\sqrt{3/4-6\tau}}2.
\tag{7}
\]

Then the minimax optimization is exact:

\[
\boxed{
\rho(\tau)=
\begin{cases}
1-\dfrac{\tau}{c_-(\tau)},
&0<\tau<\tau_*,\\[1.2ex]
\sqrt{\dfrac14+2\tau},
&\tau_*\le\tau<\dfrac38.
\end{cases}
}
\tag{8}
\]

The first branch is boundary-limited: the Gaussian-energy term and the elementary boundary-reconstruction error must be balanced. The second branch is energy-limited: the Gallagher term can be minimized before the boundary term becomes dominant.

This sharpens the earlier `tau>=1/8` statement. At the earliest twist-stable horizon `tau=1/8`, `(8)` still gives

\[
\rho(1/8)=\frac1{\sqrt2},
\tag{9}
\]

recovering the exponent of `MC-174`. But the untwisted real-variable argument does not require twist stability and can go below `1/8` while carrying the boundary error honestly.

Most notably, among all `0<tau<3/8`, the transfer exponent has the exact minimum

\[
\boxed{
\min_{0<\tau<3/8}\rho(\tau)=\frac23,
\qquad
\tau=\frac1{12},
\qquad
c=\frac14.
}
\tag{10}
\]

Thus diagonal Gallagher type at the horizon

\[
T_\beta=e^{1/(12\beta)}
\tag{11}
\]

would already imply

\[
\boxed{
M(x)\ll_\epsilon x^{2/3+\epsilon},
\qquad
\zeta(s)\ne0\ \text{for}\ \operatorname{Re}s>\frac23.
}
\tag{12}
\]

This does **not** prove `(1)`. It prices the target. The `2/3` is also not asserted to be the strongest consequence obtainable from `(1)` by every possible argument; it is the exact optimum of the direct positive-shell, Gaussian-removal, Cauchy--Schwarz, boundary-reconstruction mechanism derived below.

A second, more general consequence makes the local-to-global budget explicit. Suppose for some fixed `0<theta<1` and `0<eta<=1`, with `H=X^theta`, one had uniformly for all sufficiently large `X`

\[
\int_X^{2X}
\left|M\!\left(ye^{1/T}\right)-M(y)\right|^2
\frac{dy}{y}
\le
X^{o(1)}\bigl(H+H^{2-\eta}\bigr),
\qquad T=\frac XH.
\tag{13}
\]

Then

\[
\boxed{
M(x)
\ll
x^{\max(1-\theta\eta/2,\,\theta)+o(1)}.
}
\tag{14}
\]

Hence any fixed-power suppression of coherent short-interval second moment, if uniform at one fixed polynomial window scale, already implies a fixed global Mertens power saving.

## 1. A positive Gallagher shell gives a quantitative local `L^2` bound

For `T>=1`, define on a shell `X<=y<=2X`

\[
B_{\beta,T}(y)
:=
e^{\beta(\log y)^2}
\sum_{y<n\le ye^{1/T}}
\mu(n)e^{-\beta(\log n)^2}.
\tag{15}
\]

Then the Gallagher energy from `MC-172` is

\[
\mathcal G_\mu(\beta,T)
=
T\int_0^\infty
 e^{-2\beta(\log y)^2}
 |B_{\beta,T}(y)|^2\frac{dy}{y}.
\tag{16}
\]

Every shell contribution is nonnegative. Therefore

\[
\mathcal G_\mu(\beta,T)
\ge
T e^{-2\beta(\log(2X))^2}
J_{\beta,T}(X),
\tag{17}
\]

where

\[
J_{\beta,T}(X)
:=
\int_X^{2X}|B_{\beta,T}(y)|^2\frac{dy}{y}.
\tag{18}
\]

Let `c>tau` be fixed and, for arbitrary large `X`, choose

\[
\beta=\frac c{\log X},
\qquad
T=T_\beta=X^{\tau/c}.
\tag{19}
\]

The inequality `c>tau` guarantees that the associated additive window length `X/T` tends to infinity. From `(1)`,

\[
\mathcal G_\mu(\beta,T)
\le
X^{1/(8c)+o(1)}.
\tag{20}
\]

Also

\[
e^{2\beta(\log(2X))^2}
=X^{2c+o(1)},
\qquad
T^{-1}=X^{-\tau/c}.
\]

Hence `(17)` gives

\[
\boxed{
J_{\beta,T}(X)
\le
X^{\,2c+(1/8-\tau)/c+o(1)}.
}
\tag{21}
\]

Unlike `MC-176`, this shell is not required to remain within bounded logarithmic distance of the Gaussian saddle. The parameter `c=beta log X` stays free and is optimized against the cost of reconstructing `M` from the local sum.

## 2. Gaussian removal and the exact boundary identity

Set

\[
q=e^{1/T},
\qquad
S_T(y):=
\sum_{y<n\le qy}\mu(n)
=M(qy)-M(y).
\tag{22}
\]

For `X<=y<=2X` and `y<n<=qy`, write `delta=log(n/y)`. Then `0<delta<=1/T`, while `beta log y=O_c(1)`. Therefore

\[
\beta\bigl((\log n)^2-(\log y)^2\bigr)
=O_c(1/T),
\]

so

\[
\left|
B_{\beta,T}(y)-S_T(y)
\right|
\ll_c
\frac1T+\frac X{T^2}.
\tag{23}
\]

The logarithmic shell has fixed measure `log 2`, hence

\[
\|S_T\|_{L^2([X,2X],dy/y)}
\le
J_{\beta,T}(X)^{1/2}
+O_c\!\left(\frac1T+\frac X{T^2}\right).
\tag{24}
\]

Now put

\[
I(X,T)
:=
\int_X^{2X}S_T(y)\frac{dy}{y}.
\]

Changing variables `u=qy` in the first term of `(22)` gives the exact boundary decomposition

\[
I(X,T)
=
\int_{2X}^{2qX}M(u)\frac{du}{u}
-
\int_X^{qX}M(u)\frac{du}{u}.
\tag{25}
\]

Since `log q=1/T` exactly and

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
\tag{26}
\]

Cauchy--Schwarz on the fixed logarithmic shell, followed by `(24)`, therefore yields

\[
\boxed{
|M(2X)-M(X)|
\ll_c
T J_{\beta,T}(X)^{1/2}
+\frac XT+1.
}
\tag{27}
\]

This is the key local-to-global step. It uses the signed local sum before absolute-value averaging can erase its boundary orientation. Crucially, `(27)` remains valid below `tau=1/8`; the growing Gaussian-removal error is not discarded but appears in the explicit `X/T` term.

## 3. Exact minimax optimization in `c`

Insert `(21)` into `(27)`. Since `T=X^{tau/c}`,

\[
T J_{\beta,T}(X)^{1/2}
\le
X^{a_\tau(c)+o(1)},
\tag{28}
\]

with `a_tau(c)` from `(2)`, while

\[
\frac XT=X^{b_\tau(c)}.
\tag{29}
\]

Thus

\[
|M(2X)-M(X)|
\le
X^{r_\tau(c)+o(1)},
\tag{30}
\]

and dyadic telescoping proves `(3)`.

Set

\[
A_\tau:=\frac1{16}+\frac\tau2,
\qquad
c_0:=\sqrt{A_\tau}.
\tag{31}
\]

For every `0<tau<3/8`, one has `c_0>tau`. The function

\[
a_\tau(c)=c+\frac{A_\tau}{c}
\]

decreases on `(tau,c_0)` and increases on `(c_0,infinity)`, with minimum `2c_0`. The boundary exponent

\[
b_\tau(c)=1-\frac\tau c
\]

is strictly increasing.

At `c=c_0`, the condition that the boundary term is already subordinate to the energy term is

\[
b_\tau(c_0)\le a_\tau(c_0)
\quad\Longleftrightarrow\quad
c_0\le\frac18+2\tau
\quad\Longleftrightarrow\quad
\tau\ge\tau_*.
\tag{32}
\]

Therefore, for `tau>=tau_*`, the minimax point is simply `c=c_0`, and

\[
\rho(\tau)=2c_0
=
\sqrt{\frac14+2\tau}.
\tag{33}
\]

This includes the former twist-stable range `tau>=1/8` and explains why the earlier proof recovered the `MC-174` exponent there.

For `0<tau<tau_*`, one instead has `b_tau(c_0)>a_tau(c_0)`. Since `a_tau` decreases and `b_tau` increases on `(tau,c_0)`, the minimax point is their unique crossing in that interval. Solving

\[
a_\tau(c)=b_\tau(c)
\]

gives

\[
c^2-c+\frac1{16}+\frac{3\tau}{2}=0,
\tag{34}
\]

whose relevant root is exactly `c_-(tau)` from `(7)`. This proves the first branch of `(8)`.

The transition `tau=tau_*` is where the crossing reaches the unconstrained energy minimizer. Both branches agree there. No discontinuity or hidden change of shell occurs.

## 4. The direct-transfer optimum is exactly `2/3`

On the boundary-limited branch, equation `(34)` can be solved for `tau`:

\[
\tau
=
\frac23\left(c-c^2-\frac1{16}\right).
\tag{35}
\]

At the crossing, `rho=1-tau/c`, so `(35)` gives the exact identity

\[
\rho
=
\frac13+rac{2c}{3}+rac1{24c}.
\tag{36}
\]

Subtracting `2/3` factors as

\[
\boxed{
\rho-\frac23
=
\frac{(4c-1)^2}{24c}
\ge0.
}
\tag{37}
\]

Equality occurs exactly at `c=1/4`. Substituting this value into `(35)` gives `tau=1/12`, proving `(10)` on the lower branch.

On the energy-limited branch, `(33)` is increasing in `tau`, and at `tau=tau_*` its value is

\[
\rho(\tau_*)
=
\frac{1+\sqrt3}{4}
>
\frac23.
\tag{38}
\]

Hence `2/3` is the global optimum of the direct transfer over all useful horizons `0<tau<3/8`.

At the optimum,

\[
\beta=\frac1{4\log X},
\qquad
T=X^{1/3},
\qquad
\frac XT=X^{2/3}.
\tag{39}
\]

The two terms in `(27)` both have exponent `2/3`: the Gallagher-energy contribution and the boundary/Gaussian-removal contribution meet exactly. This also explains why the `tau>=1/8` `O(1)` unweighting threshold in `MC-176` is not a barrier for the direct global transfer. Below that threshold the decoration error grows, but at `tau=1/12` it is still small enough, after the exact boundary reconstruction, to balance rather than destroy the power saving.

There is a useful consistency check with the generic variance budget below. At square-root local variance (`eta=1`), `(14)` is optimized at window exponent `theta=2/3`, again giving a global `2/3` exponent. The optimal Gallagher shell `(39)` has exactly that local window scale.

## 5. General variance-to-Mertens transfer budget

The boundary identity `(26)` is useful independently of the Gaussian heat family. Let

\[
H:=\frac XT,
\qquad
J_S(X,T)
:=
\int_X^{2X}|S_T(y)|^2\frac{dy}{y}.
\]

Then `(26)` and Cauchy--Schwarz give the deterministic inequality

\[
\boxed{
|M(2X)-M(X)|
\ll
\frac XH J_S(X,T)^{1/2}
+H+1.
}
\tag{40}
\]

Suppose `H=X^theta` and the local second moment obeys `(13)`. Since `0<eta<=1`,

\[
J_S(X,T)^{1/2}
\le
X^{o(1)}H^{1-\eta/2},
\]

so `(40)` becomes

\[
|M(2X)-M(X)|
\le
X^{o(1)}
\left(
XH^{-\eta/2}+H
\right).
\tag{41}
\]

Dyadic telescoping proves `(14)`.

For every fixed `eta>0` and `0<theta<1`, both exponents

\[
1-\frac{\theta\eta}{2}
\quad\text{and}\quad
\theta
\]

are strictly below `1`. Thus a uniform fixed-power variance improvement at any fixed polynomial local scale already gives a fixed-power global Mertens theorem. At `eta=1`, the elementary boundary transfer is optimized at `theta=2/3`, where it gives `M(x)<<x^{2/3+o(1)}`. At the `MC-176` critical shell `theta=1/2`, the same generic transfer gives only `x^{3/4+o(1)}`.

The distinction is important: controlling one Good--Churchhouse-order shell is a necessary fragment of the Gallagher target, but it is not equivalent to controlling the full target. The full heat family lets one choose the shell parameter `c` against the horizon `tau`; `(8)` records the exact price of that freedom within the present transfer.

## Prior art and novelty assessment

Gallagher localization itself is classical (`MC-S42`), and its Dirichlet/Selberg-integral formulation is recorded in `MC-S43`. The implication from a Mertens power bound to zeta nonvanishing is classical Abel/Dirichlet theory. No novelty is claimed for these ingredients, for Cauchy--Schwarz, or for the elementary boundary averaging identity `(26)` as a general analytic device.

The current integer short-interval literature does not provide the fixed-power uniform variance input `(13)` in the regimes needed here. `MC-S2` gives very strong almost-all Möbius cancellation but only logarithmic normalized saving at its quantitative level, which remains `eta=0` in the power taxonomy already audited in `MC-175`. The classical Good--Churchhouse variance picture and the function-field variance analogue `MC-S44` remain comparison targets rather than unconditional integer inputs.

A targeted current search around Möbius short-interval mean squares, Mertens increments, Gallagher/Selberg integrals, boundary averaging, and local-to-global variance transfer did not locate this exact `c`-minimax phase diagram or the `tau=1/12`, `2/3` optimum as a standalone theorem. This is not an exhaustive bibliographic claim, and **no novelty claim is made**. The durable contribution is the line-specific composition and difficulty calibration: once the already-defined Gallagher target is assumed, its direct arithmetic consequence can be priced all the way below the twist-stability threshold without importing zero information.

## Boundaries and falsification controls

This finding does not prove `(1)`, any fixed positive `eta` instance of `(13)`, or a new unconditional Mertens exponent. Every displayed global power bound is conditional on the corresponding Gallagher or local-variance estimate.

The conclusion `(3)` uses the full asymptotic Gallagher bound `(1)` for every sufficiently small `beta`, because arbitrary large `X` is encoded through `beta=c/log X`. A bound known only on a sparse sequence of `beta` values would not automatically give the uniform global conclusion.

The local energy must retain the signed Möbius orientation. A support-only or phase-blind quadratic statistic such as the autocorrelation classified in `MC-173` cannot be substituted into `(27)` without an additional signed reconstruction.

The subcritical extension does not discard the Gaussian-removal error. Its exact contribution is the `X/T` term in `(27)`, and the lower branch of `(8)` is obtained by balancing that term against the Gallagher-energy term. Any attempt to use the smaller unconstrained energy exponent while ignoring `b_tau(c)` below `tau_*` is invalid.

The value `2/3` is optimal only for this direct one-shell transfer family. A different use of correlations between shells, additional arithmetic structure, a sharper signed boundary reconstruction, or another consequence of `(1)` could in principle do better. Conversely, the present calculation proves that simply retuning `tau` and `c` inside `(21)` plus `(27)` cannot beat `2/3`.

Equation `(14)` requires a uniform local variance estimate for all sufficiently large `X` at the stated polynomial scale. Almost-all control with an exceptional set, logarithmic averaging, or a sparse scale subsequence cannot be inserted silently.

No analytic continuation or zero-free region for `1/zeta` is used to derive the Mertens bounds. Zeta enters only after the global arithmetic estimate has already been obtained, through the standard one-way consequence from Mertens power cancellation to nonvanishing.

## Consequence for the live frontier

`MC-176` identifies a necessary Good--Churchhouse-order critical shell. The strengthened direct transfer here shows that the full `MC-172` diagonal target is globally expensive at **every positive exponential horizon**: any fixed `tau>0` below `3/8` already yields some fixed Mertens power saving, and the strongest consequence obtainable by the current direct mechanism is `x^{2/3+epsilon}` at `tau=1/12`.

This moves the useful pricing boundary below the spectral twist threshold of `MC-174`. A proposed proof of full Gallagher diagonal type at `tau=1/12` must therefore be commensurate with a `2/3` Mertens theorem. More modest work should target partial polynomial improvement of a concrete signed short-interval second moment and price it through `(14)`, rather than treating diagonal Gallagher type as an inexpensive intermediate or relying on present logarithmic almost-all cancellation alone.