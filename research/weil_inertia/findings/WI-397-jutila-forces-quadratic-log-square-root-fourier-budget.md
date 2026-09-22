# WI-397 — Jutila forces a quadratic-log square-root-prime Fourier budget

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + QUANTITATIVE-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.

**Parent findings:** WI-029, WI-395, WI-396.

## Claim

WI-396 proves qualitatively that the density-normalized horizontal sensitivity of every scalar Fourier-Stieltjes test, measured in the absolute square-root-prime Fourier norm, tends to zero. The uniform form of Jutila's near-critical-line zero-density theorem upgrades that qualitative `o(1)` to the explicit natural scale

\[
\boxed{
Q_T\ll \frac1{L_T^2},
\qquad
L_T:=\log(T/2\pi),
}
\tag{1}
\]

where

\[
Q_T
:=
\frac1{N_T}
\sum_{\rho\in E_T^+}q(\delta_\rho),
\qquad
N_T:=N(2T)-N(T),
\]

`E_T^+` is the multiset of right-half off-critical zero occurrences

\[
\rho=\frac12+\delta_\rho+i\gamma_\rho,
\qquad
T<\gamma_\rho\le2T,
\qquad
0<\delta_\rho<\frac12,
\]

and `q` is the sharp WI-395 strip-contraction factor.

Consequently, for every finite complex Borel measure `mu` with

\[
\|\mu\|_{1/2}
:=
\int_{\mathbb R}e^{|u|/2}\,d|\mu|(u)<\infty
\]

and

\[
h(z)=\int_{\mathbb R}e^{iuz}\,d\mu(u),
\]

one has the unconditional quantitative critical-projection bound

\[
\boxed{
\frac1{N_T}
\sum_{\rho\in E_T^+}
\left|
h(\gamma_\rho+i\delta_\rho)
+h(\gamma_\rho-i\delta_\rho)
-2h(\gamma_\rho)
\right|
\ll
\frac{\|\mu\|_{1/2}}{L_T^2}.
}
\tag{2}
\]

Therefore any scalar test family that produces a fixed positive density-scale horizontal separation `c>0` must pay

\[
\boxed{
\|\mu_T\|_{1/2}\gg_c L_T^2.
}
\tag{3}
\]

This is substantially stronger than WI-396's conclusion `||mu_T||_{1/2}->infinity`: a source theorem that tries to rescue the scalar channel by signed prime cancellation while keeping the true normalized arithmetic cost `O(1)` must beat the componentwise absolute square-root-prime budget by a factor of order at least `L_T^2`.

The power `2` is also the strongest rate available from **only** the two interfaces used here: Jutila's near-line density bound and WI-395's one-pair contraction. A hypothetical bounded positive density of off-line mirror pairs at normalized depth

\[
Y_\rho:=\delta_\rho L_T=Y_0>0
\]

is compatible with Jutila's tail bound at every fixed `Y_0`, while

\[
q(Y_0/L_T)
\sim
\frac{16}{e^2}\frac{Y_0^2}{L_T^2}.
\]

Thus such an abstract admissible population has `Q_T\asymp L_T^{-2}`. Obtaining `o(L_T^{-2})` requires genuinely stronger information that makes the bounded-`Y` off-line mass itself vanish or changes the observable; it cannot be extracted from the present zero-density tail plus the scalar weighted-Fourier inequality alone.

No unconditional RH conclusion and no improved simple-critical-zero proportion is claimed.

## 1. The load-bearing literature input is the uniform sigma form of Jutila

WI-029 already audits Jutila's published estimate

\[
\boxed{
N(\sigma,T)
\ll_\eta
T^{1-(1-\eta)(\sigma-1/2)}\log T
}
\tag{4}
\]

for fixed `eta>0` in the near-critical-line regime. The point needed here, and rechecked in the prior-art pass, is that this is a **uniform zero-density estimate in `sigma`**, not merely a statement obtained after fixing one displacement `A` and then sending `T` to infinity. Standard modern statements write the Vinogradov constant as depending on `eta`, not on `sigma`; Conrey--Ghosh--Gonek record the estimate in exactly this form, and modern zero-density surveys likewise state Jutila's sharpening uniformly near the line.

Take once and for all `eta=1/2`. Put

\[
Y_\rho:=|\beta-1/2|L_T
\]

and retain the WI-029 dyadic tail

\[
D_T(a)
:=
\#\{\rho:T<\gamma\le2T,\ Y_\rho>a\}.
\]

For

\[
0\le a\le A_T,
\qquad
A_T:=9\log L_T,
\tag{5}
\]

we have

\[
\sigma=\frac12+\frac a{L_T}
=\frac12+O\!\left(\frac{\log\log T}{\log T}\right),
\]

so this remains inside the classical near-line range. Functional-equation symmetry, (4), and Riemann--von Mangoldt give uniformly over (5)

\[
\frac{D_T(a)}{N_T}
\ll
\exp\!\left[-\frac a2\frac{\log(2T)}{L_T}\right].
\tag{6}
\]

For all sufficiently large `T`, `log(2T)/L_T>2/3`; hence the convenient uniform envelope

\[
\boxed{
\frac{D_T(a)}{N_T}\ll e^{-a/3}
\qquad(0\le a\le A_T).
}
\tag{7}
\]

The constants in (6)--(7) are absolute after the fixed choice `eta=1/2`. In particular,

\[
\boxed{
\frac{D_T(A_T)}{N_T}\ll L_T^{-3}.
}
\tag{8}
\]

This is the only strengthening of WI-029 used below: instead of freezing `a` before the `T` limit, we consume the standard uniformity of the published density theorem on the slowly growing window `a<=9 log L_T`.

## 2. The sharp strip contraction is quadratic at the critical line

WI-395 proves

\[
q(\delta)
=
\sup_{D\ge0}
2(\cosh(\delta D)-1)e^{-D/2}
\tag{9}
\]

and

\[
q(\delta)
=
\frac{16}{e^2}\delta^2+O(\delta^3)
\qquad(\delta\downarrow0).
\]

For the quantitative argument no asymptotic remainder is needed. If `0<=delta<=1/4`, then

\[
2(\cosh(\delta D)-1)
\le
\delta^2D^2e^{\delta D},
\]

so

\[
q(\delta)
\le
\delta^2\sup_{D\ge0}D^2e^{-D/4}
=
\frac{64}{e^2}\delta^2
<9\delta^2.
\tag{10}
\]

Thus the horizontal mirror-pair discrepancy has a genuinely quadratic zero at the critical line in exactly the weighted norm that represents componentwise absolute square-root-prime control.

## 3. Layer-cake integration removes the extra log-log loss

A one-threshold split at `Y=A_T` would give the weaker estimate `Q_T<< (log L_T)^2/L_T^2`. The exponential tail (7) contains more information: integrating it controls the whole second moment of the shallow normalized depths.

For the right-half multiset `E_T^+`, positivity and the layer-cake identity give

\[
\begin{aligned}
\frac1{N_T}
\sum_{\rho\in E_T^+\atop Y_\rho\le A_T}
Y_\rho^2
&\le
\int_0^{A_T}
2a\,
\frac{\#\{\rho\in E_T^+:Y_\rho>a\}}{N_T}
\,da\\
&\le
\int_0^{A_T}
2a\,
\frac{D_T(a)}{N_T}
\,da\\
&\ll
\int_0^\infty2ae^{-a/3}\,da
\ll1.
\end{aligned}
\tag{11}
\]

For sufficiently large `T`, `A_T/L_T<1/4`. Therefore (10)--(11) imply

\[
\frac1{N_T}
\sum_{\rho\in E_T^+\atop Y_\rho\le A_T}
q(\delta_\rho)
\le
\frac9{L_T^2}
\frac1{N_T}
\sum_{Y_\rho\le A_T}Y_\rho^2
\ll
L_T^{-2}.
\tag{12}
\]

On the deep tail use only the sharp WI-395 fact `0<=q(delta)<1`. Equation (8) gives

\[
\frac1{N_T}
\sum_{\rho\in E_T^+\atop Y_\rho>A_T}
q(\delta_\rho)
\le
\frac{D_T(A_T)}{N_T}
\ll L_T^{-3}.
\tag{13}
\]

Adding (12) and (13) proves (1).

## 4. Quantitative critical projection and the arithmetic price

WI-395 gives separately for every right-half occurrence

\[
|\Delta_{\delta_\rho}h(\gamma_\rho)|
\le
q(\delta_\rho)\|\mu\|_{1/2}.
\tag{14}
\]

Summing (14), dividing by `N_T`, and inserting (1) proves (2). Equivalently, if `Z_T` is the actual dyadic zero multiset and `Pi Z_T` is obtained by moving every zero horizontally to the critical line while preserving ordinate and multiplicity, then

\[
\boxed{
\sup_{\|\mu\|_{1/2}\le1}
\frac1{N_T}
\left|
\sum_{\rho\in Z_T}\widetilde h_\mu(\rho)
-
\sum_{\rho\in\Pi Z_T}\widetilde h_\mu(\rho)
\right|
\ll L_T^{-2}.
}
\tag{15}
\]

As in WI-396, (15) is a zero-multiset consequence of the scalar pairwise estimate, not a claim that every Fourier-Stieltjes transform is automatically an admissible Weil test.

Now suppose a scalar source-exact architecture needs a fixed normalized horizontal signal

\[
\frac1{N_T}
\sum_{\rho\in E_T^+}
|\Delta_{\delta_\rho}h_T(\gamma_\rho)|
\ge c>0.
\tag{16}
\]

Equations (2) and (16) force (3). In the Guinand--Weil interface isolated by WI-393--WI-395, `||mu_T||_{1/2}` is precisely the componentwise absolute Fourier budget whose frequency `u` is charged at the square-root-prime scale `e^{|u|/2}`. Therefore a signed arithmetic estimate that keeps the true normalized prime contribution bounded while (16) holds must realize a cancellation gain of at least quadratic logarithmic size relative to that absolute envelope.

This gives a concrete falsification target for the surviving signed-cancellation route. An `o(1)` or fixed-factor improvement over the absolute prime estimate is categorically insufficient at density scale; even a gain growing slower than `L_T^2` cannot support a fixed horizontal signal through this scalar interface.

## 5. Why the `L_T^{-2}` rate is the endpoint of these two inputs

The rate in (1) is not asserted to be the true behavior of zeta zeros. It is the strongest universal rate forced by the current pair of inputs.

Fix any bounded normalized depth `Y_0>0` and any small positive density `p`. An abstract symmetric zero population in which a proportion `p` of occurrences sit at

\[
\beta=\frac12\pm\frac{Y_0}{L_T}
\]

is compatible with a Jutila-type exponential tail after adjusting the harmless implied constant: its tail is `p` below `Y_0` and zero above it. WI-029 already emphasizes that published zero density does not make the bounded-`Y` mass vanish. For that population, WI-395 gives

\[
Q_T
=
p\,q(Y_0/L_T)
\sim
p\frac{16Y_0^2}{e^2L_T^2}.
\tag{17}
\]

Hence no deduction that sees the zero set only through Jutila's horizontal tail and the pointwise contraction `q(delta)` can replace (1) by `o(L_T^{-2})`. To cross that boundary one must add information that excludes a positive-density bounded-`Y` core, for example vertical correlation/spacing information of the kind already identified in WI-029, or use a non-scalar/matrix/indefinite observable whose off-line response does not begin quadratically in `delta` under the same arithmetic budget.

This is a route barrier, not an adversarial model claimed to be realizable by the actual zeta function.

## 6. Prior-art and novelty audit

The literature-backed input is classical: Matti Jutila, *Zeros of the zeta-function near the critical line*, in **Studies in Pure Mathematics to the Memory of Paul Turán** (Birkhäuser, 1983), 385--394, proves the sharpened Selberg density estimate used in (4). Conrey--Ghosh--Gonek, *Simple zeros of the Riemann zeta-function*, Proc. London Math. Soc. (3) 76 (1998), 497--522, records the same estimate in the uniform form `N(sigma,T) <<_eta T^{1-(1-eta)(sigma-1/2)} log T`. Modern zero-density accounts likewise state Jutila's result as a uniform near-line estimate.

The line-local audit covered WI-029's normalized-depth tail, WI-395's sharp strip contraction, and WI-396's qualitative critical-projection theorem. Repository searches for a quadratic-log quantitative projection/budget consequence found no existing `weil_inertia` finding. External searches around Jutila zero density, horizontal moments, weighted Wiener/Beurling norms, and critical-line projection located the classical ingredients but no statement of (1)--(3) or (15). Absence of a search hit is not a priority claim.

The durable new content is the exact synthesis: consume the uniform `sigma` range of Jutila, integrate the exponential normalized-depth tail rather than using one cutoff, and combine the resulting bounded second moment with the sharp quadratic vanishing of `q`. The endpoint example (17) identifies precisely what extra information would be needed to improve the rate.

## Decisive audit test

The finding has three load-bearing checks:

1. verify that Jutila's estimate (4) is uniform in `sigma` over `sigma-1/2 <= 9 log L_T/L_T`, with an implied constant depending only on the fixed `eta=1/2`;
2. verify the elementary global bound `q(delta) <= 64 e^{-2} delta^2` for `0<=delta<=1/4` from WI-395's exact supremum formula;
3. verify the layer-cake inequality (11), remembering that `D_T(a)` counts both horizontal sides and therefore is an upper bound for the right-half tail used there.

If the first uniformity check failed, the proof would fall back to WI-396's qualitative diagonal argument and (1) would not be justified. Given those three interfaces, equations (7)--(15) are deterministic.

## Research consequence

The density-scale scalar signed-cancellation route now has a quantitative entry price. It is not enough to beat the absolute square-root-prime envelope by a diverging factor of unspecified size: retaining an order-one horizontal signal requires at least a quadratic-log gain, `Omega((log T)^2)`, in the current normalization. Conversely, Jutila plus scalar strip contraction cannot demand more than that, because a bounded normalized-depth core can saturate the `L_T^{-2}` scale. Future work on the signed prime polynomial should therefore be tested immediately against this quadratic-log target; if the available cancellation theorem cannot reach it at defect-anchored ordinates, that scalar route is closed without further optimization.