# ANF-167 — uniform local activity does not erase the endpoint charge barrier

**Status:** `EXACT-DERIVED + MATCHED-INFORMATION-CONTROL + TWO-SIDED-LOCAL-MOMENT-BUDGET + ENDPOINT-CHARGE-PERSISTENCE`. `ANF-166` shows that arbitrary fixed logarithmic cancellation on every interval above the current activation length does not control the absolute endpoint primitive: a small charge can be accumulated once and then retained through most of the bow horizon. Its particular matched control makes the mechanism visually extreme by leaving the endpoint coefficients zero after the charging block, while moving almost all `L^2` mass into a central calibrator.

That coefficient desert is not essential. One can superimpose a uniformly active alternating sparse calibrator across the **entire** coefficient range, including both endpoint regions, so that every sufficiently long interval carries the same `L^1` and `L^2` orders expected from an arithmetic residual,

\[
\sum_{n\in I}|b_n|\asymp |I|,
\qquad
\sum_{n\in I}|b_n|^2\asymp |I|\log X,
\]

while all interval sums of the calibrator remain `O(log X)`. The endpoint primitive therefore stays charged at size `asymp sqrt(X log X)` for `Theta(K)` prefix lengths and its square completion remains a prescribed positive fraction of `XK log X`.

Consequently, adding two-sided local coefficient-mass information to the inputs of `ANF-166` does **not** close the bow endpoint obstruction. A source-side theorem must use information that couples signs/phases/locations, or control the primitive itself; mere knowledge that arithmetic energy is present everywhere is insufficient.

## 1. A uniformly active bounded-prefix calibrator

Use the finite bow geometry of `ANF-157`. Let

\[
N=X,\qquad M=N+K-1,
\]

with `K=o(X)` and `K\to\infty`. Let `H_0=H_0(X)` satisfy

\[
\sqrt{X\log X}\ll H_0\ll K.
\tag{1}
\]

Fix `delta>0` and define

\[
a_X:=\sqrt{\frac{\delta}{2}X\log X},
\qquad
q_X:=\frac{a_X}{H_0}.
\tag{2}
\]

As in `ANF-166`, let the endpoint charge be

\[
e_n=
\begin{cases}
q_X,&1\le n\le H_0,\\
-q_X,&M-H_0<n\le M,\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
\]

Rounding `H_0` to an integer changes none of the asymptotics. The two edge blocks have opposite total mass, so

\[
\sum_{n=1}^M e_n=0.
\tag{4}
\]

Now put

\[
L:=\lceil\log X\rceil.
\tag{5}
\]

Let `J` be the largest even integer such that `JL\le M`, and define a sparse alternating sequence on the whole coefficient range by

\[
c_{jL}=(-1)^jL\quad (1\le j\le J),
\qquad
c_n=0\quad\text{otherwise}.
\tag{6}
\]

Because `J` is even,

\[
\sum_{n=1}^M c_n=0.
\tag{7}
\]

More importantly, every contiguous interval contains a consecutive block of the spike indices `j`. The alternating sum of any consecutive block of equal-magnitude spikes is `0` or `\pm L`. Hence for **every** interval `I\subset[1,M]`,

\[
\boxed{
\left|\sum_{n\in I}c_n\right|\le L.
}
\tag{8}
\]

Thus `c` is active throughout the domain but its primitive never leaves an `O(log X)` strip.

## 2. Every long interval carries two-sided `L^1` and `L^2` mass

Set

\[
b:=c+e.
\tag{9}
\]

Since both components are globally centered,

\[
\sum_{n=1}^M b_n=0.
\tag{10}
\]

For an interval `I` of length `H`, the number `m_I` of grid points `jL` inside `I` satisfies

\[
m_I=\frac{H}{L}+O(1).
\tag{11}
\]

The omission of at most the final `O(L)` tail caused by choosing `J` even is absorbed in the same error. From (1)--(2), `q_X=o(1)`. Therefore, uniformly for every interval with `H\ge H_0`, each spike inside `I` has magnitude

\[
|b_{jL}|=|(-1)^jL+e_{jL}|=L+O(q_X),
\tag{12}
\]

while every non-spike contributes at most `q_X`. Equations (11)--(12) give absolute constants `0<c<C<\infty` such that, for all sufficiently large `X`, every `I` with `|I|=H\ge H_0` obeys

\[
\boxed{
cH\le \sum_{n\in I}|b_n|\le CH,
}
\tag{13}
\]

and

\[
\boxed{
cH\log X\le \sum_{n\in I}|b_n|^2\le CH\log X.
}
\tag{14}
\]

The pointwise envelope is also unchanged at the relevant scale,

\[
\boxed{|b_n|\ll\log X.}
\tag{15}
\]

Thus the matched control has no endpoint coefficient desert at the level of either local total variation or local quadratic mass. In fact the two-sided estimates hold already for intervals much shorter than `H_0`, once `H/L\to\infty`; the statement above uses only the range relevant to the current bow gate.

## 3. Long-interval discrepancy remains stronger than every fixed logarithmic saving

For any interval `I`, the edge sequence satisfies

\[
\left|\sum_{n\in I}e_n\right|\le a_X,
\tag{16}
\]

while (8) gives the calibrator contribution. Hence

\[
\boxed{
\left|\sum_{n\in I}b_n\right|\le a_X+L.
}
\tag{17}
\]

Specialize, as in `ANF-166`, to

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\tag{18}
\]

and choose fixed `eta>0` with

\[
H_0=X^{5/8+\eta}\ll K.
\tag{19}
\]

Then

\[
q_X
=\frac{a_X}{H_0}
\asymp
X^{-1/8-\eta}\sqrt{\log X}
=o_A((\log X)^{-A})
\tag{20}
\]

for every fixed `A>0`, while `L=o(a_X)`. For every interval `|I|=H\ge H_0`, (17) therefore yields

\[
\boxed{
\left|\sum_{n\in I}b_n\right|
\le (1+o(1))q_XH
=o_A\!\left(H(\log X)^{-A}\right)
}
\tag{21}
\]

for every fixed `A`. The control simultaneously has uniform local activity (13)--(14) and stronger-than-any-fixed-log interval cancellation above the same activation scale.

This separates two pieces of information that can otherwise look morally interchangeable. Large local `L^2` mass says that coefficients are present; a small interval sum says that their **net increment** is small. Neither statement determines the absolute value already stored in the primitive before the interval begins.

## 4. The moving-window diagonal still has bow scale

Let `w_n` denote the exact incidence count of coefficient `n` in the `N` windows of length `K` used in `ANF-157`. Thus `w_n=K` on the full-incidence region and differs from `K` only within the first and last `K-1` coefficient positions.

For the calibrator,

\[
\sum_{n=1}^M|c_n|^2
=JL^2
=(1+o(1))X\log X.
\tag{22}
\]

The total incidence deficit from the two endpoint ramps is at most

\[
O(K^2L),
\tag{23}
\]

because each edge range contains `O(K/L)` spikes, each of squared size `L^2`, and each incidence deficit is at most `K`. Hence

\[
D_{N,K}(c)
:=\sum_{n=1}^M w_n|c_n|^2
=(1+o(1))XK\log X.
\tag{24}
\]

For the charge component, since it is supported only in the first and last `H_0` positions and `H_0<K`, the ramp incidence gives

\[
D_{N,K}(e)=O(q_X^2H_0^2)=O(X\log X).
\tag{25}
\]

The cross term is negligible by Cauchy--Schwarz on the edge regions; for instance

\[
\left|\sum_n w_nc_n\overline{e_n}\right|
\le
D_{N,K}(c;\operatorname{supp}e)^{1/2}
D_{N,K}(e)^{1/2}
=o(XK\log X),
\tag{26}
\]

because `D_{N,K}(c; supp e)=O(LH_0^2)`, `H_0=o(K)`, and `K=o(X)` in the bow regime. Therefore

\[
\boxed{
D_{N,K}(b)=(1+o(1))XK\log X.
}
\tag{27}
\]

So the new control matches the same global diagonal currency as `ANF-166` while also distributing the calibrating `L^2` mass through the endpoint zones themselves.

## 5. The endpoint square completion remains macroscopic

Let

\[
S_r^-(x):=\sum_{n=1}^r x_n,
\qquad
S_r^+(x):=\sum_{n=M-r+1}^{M}x_n.
\]

For `1\le r<K`, (8) gives

\[
|S_r^\pm(c)|\le L.
\tag{28}
\]

The charge component is unchanged from `ANF-166`:

\[
|S_r^\pm(e)|=q_X\min(r,H_0).
\tag{29}
\]

Hence

\[
E_\partial(e)
:=\sum_{r=1}^{K-1}
\left(|S_r^-(e)|^2+|S_r^+(e)|^2\right)
=
\delta XK\log X\,(1+o(1)).
\tag{30}
\]

The calibrator cannot materially change this value. Indeed,

\[
\begin{aligned}
|E_\partial(b)-E_\partial(e)|
&\le
2\sum_{r<K}\bigl(
|S_r^-(e)||S_r^-(c)|
+|S_r^+(e)||S_r^+(c)|
\bigr)\\
&\quad+
\sum_{r<K}\bigl(|S_r^-(c)|^2+|S_r^+(c)|^2\bigr)\\
&\ll Ka_XL+KL^2
=o(XK\log X),
\end{aligned}
\tag{31}
\]

because `a_X\asymp\sqrt{X\log X}` and `L\asymp\log X`. Therefore

\[
\boxed{
E_\partial(b)
=
\delta XK\log X\,(1+o(1)).
}
\tag{32}
\]

The primitive plateau survives even though the coefficients continue to carry order-one `L^1` density and order-`log X` `L^2` density throughout the plateau region. The reason is simple but structurally important: the added activity is a bounded-prefix oscillation. It changes the primitive by only `O(log X)`, far below the stored charge `a_X\asymp\sqrt{X\log X}`.

## 6. Information boundary and remaining source-side gate

The control `b` is synthetic. It is **not** asserted to equal the actual demodulated arithmetic residual

\[
r_X(n)n^{-iU}
=(\vartheta(n)-Q_X(n))n^{-iU}.
\tag{33}
\]

In particular, the alternating spike locations and signs do not satisfy the exact prime/rough support law, the Cramer--Granville amplitude law, or the coupling between the real residual and the logarithmic carrier `n^{-iU}`. This finding therefore does not show that the actual endpoint completion is large.

What it rules out is a natural attempted repair of `ANF-166`. Suppose one augments the already available aggregate inputs by proving that every endpoint interval of the relevant lengths contains the expected amount of coefficient activity, even in the strong two-sided form (13)--(14). Those facts still cannot imply `E_\partial=o(XK\log X)` by themselves: the present control satisfies them and retains (32).

The next source-side theorem must therefore constrain **how** the local mass is signed and phased, not merely prove that it is there. Viable information must distinguish the actual prime-minus-rough residual from an everywhere-active bounded-prefix oscillation superimposed on a persistent charge. Examples of genuinely different currencies include a source-faithful autocorrelation or return law for the endpoint primitive, a direct square-function estimate, or a theorem coupling the prime/rough placement and amplitudes to the distinguished logarithmic carrier strongly enough to force discharge below `sqrt(X log X)`.

A local lower bound for `sum |r_X|`, `sum |r_X|^2`, or the number of nonzero coefficients does not cross this boundary unless accompanied by such signed/phase information.

## Prior-art audit and novelty boundary

A fresh audit checked bounded-prefix discrepancy, alternating/telescoping constructions, and Steinitz-type balancing as the nearest general frameworks. The fact that large coefficient activity can coexist with a bounded primitive is classical in spirit, and no novelty is claimed for alternating cancellation itself. No external theorem is load-bearing here: (6)--(32) are a direct finite construction.

The durable line-specific content is the strengthened matched-information obstruction. `ANF-166` could be challenged on the ground that its endpoint plateau lived in a coefficient desert. `ANF-167` removes that escape by matching two-sided local `L^1/L^2` activity at every long endpoint scale while preserving the same bow-normalized persistent charge. No new literature anchor is therefore required in `SOURCES.md`.

## Consequence for the research line

The absolute-prefix gate of `ANF-166` survives a substantial source-side strengthening: **uniform local energy is not an anchor**. The remaining unsupported implication cannot be closed by adding lower local mass estimates to the existing all-interval discrepancy bounds. Any successful analytic input must see a correlation that the alternating calibrator erases—most naturally the exact prime/rough sign-placement law together with the distinguished twist—or estimate the endpoint primitive square function directly.

This narrows the frontier from “rule out a coefficient desert” to a sharper question: can the actual arithmetic residual sustain a `sqrt(X log X)` primitive while continuing to exhibit its forced prime/rough activity, or does the source-specific sign/phase coupling necessarily discharge that memory on a scale `o(K)`?