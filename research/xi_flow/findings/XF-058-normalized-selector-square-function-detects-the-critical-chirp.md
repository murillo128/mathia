# XF-058 — normalized selector square function detects the critical chirp

**Status:** `EXACT-DERIVED` + `RAPID-SOURCE-DECAY` + `MATCHED-CONTROL` + `AGGREGATE-SEPARATION`. XF-056 proves that the actual Xi carrier is `o(1)` against every individual compact selector in the continuous slow-frequency cone. XF-057 shows that a quadratic chirp can make the supremum of those pointwise coefficients vanish while retaining critical triple-flux variation. The same chirp does **not** escape the naturally normalized `L^2` aggregate of the selector family.

Use

\[
q\asymp\log^2T,
\qquad M=q^2,
\qquad
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\qquad W=M\sigma_T,
\tag{1}
\]

and

\[
\Theta_T=
\left[\frac cq,\frac{C\log\log T}{q}\right].
\tag{2}
\]

For the actual Xi carrier define

\[
\mathfrak E_T^{\Xi}(t)
:=M\int_{\Theta_T}|\mathcal S_{T,\theta}(t)|^2\,d\theta,
\tag{3}
\]

with `\mathcal S_{T,theta}` exactly as in XF-056. Then for every fixed `t_0>0`,

\[
\boxed{
\sup_{0\le t\le t_0}\mathfrak E_T^{\Xi}(t)=o(1).
}
\tag{4}
\]

More precisely, the XF-056 proof gives for every fixed `B>0`

\[
\boxed{
\sup_{0\le t\le t_0}
\sup_{\theta\in\Theta_T}
|\mathcal S_{T,\theta}(t)|
=O_B((\log T)^{-B}).
}
\tag{5}
\]

For the matched control take the XF-057 chirp

\[
\Phi_j=\frac{a_0}{q}j+\frac{b}{2q^3}j^2,
\qquad
\epsilon=\frac\kappa M,
\tag{6}
\]

\[
z_{j+1}-z_j
=\sigma_T(1+\epsilon\cos\Phi_j),
\qquad z_0=T.
\tag{7}
\]

Let

\[
f_{T,\theta}(x)
=g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega_{\theta,T}(x-T)+\varphi_{\theta,T})},
\qquad
\omega_{\theta,T}=\frac{\theta}{\sigma_T},
\tag{8}
\]

be the exact XF-056 probe and put

\[
\boxed{
S_T^{\rm chirp}(\theta)
:=\sum_{j\in\mathbb Z}f_{T,\theta}(z_j).
}
\tag{9}
\]

For every fixed nonzero XF-056 envelope `g`, one may choose the admissible constant `a_0` sufficiently large relative to fixed `b>0` and `g`, while keeping `a_0` fixed as `T\to\infty`, so that

\[
\boxed{
0<\liminf_{T\to\infty}
M\int_{\Theta_T}|S_T^{\rm chirp}(\theta)|^2d\theta
\le
\limsup_{T\to\infty}
M\int_{\Theta_T}|S_T^{\rm chirp}(\theta)|^2d\theta
<\infty.
}
\tag{10}
\]

Thus the exact XF-057 control simultaneously satisfies

\[
\sup_{\theta\in\Theta_T}|S_T^{\rm chirp}(\theta)|=o(1),
\qquad
M V_M\asymp1,
\tag{11}
\]

while its normalized square-function energy remains order one. The obstruction in XF-057 is therefore a pointwise-frequency obstruction, not an obstruction to square-function aggregation.

The factor `M` is the natural normalization: one selector has index-frequency width `1/M`, so an order-one coherent response confined to one resolution cell has unnormalized `L^2(d\theta)` energy of order `1/M`.

## 1. Rapid source decay is already contained in XF-056

The moving-line proof of XF-056 takes `a_T=A log T`. Uniformly on `\Theta_T`, the vertical shift costs only a fixed polylogarithm,

\[
e^{a_T\omega_{\theta,T}}\le(\log T)^K,
\tag{12}
\]

while the reflected Euler-product error is `T^{-kappa_A}` times a fixed polylogarithm. Hence its contribution beats every fixed negative power of `log T`.

For the deterministic background,

\[
W\omega_{\theta,T}=M\theta\ge cq\asymp\log^2T.
\tag{13}
\]

The integration-by-parts step in XF-056 can be repeated any fixed number `N` of times. The worst envelope term is

\[
O_N\!\left((\log T)^{K_1}W(M\theta)^{-N}\right),
\tag{14}
\]

terms with derivatives on the background gain powers of `W/T`, and the physical tails are killed by arbitrarily high fixed Schwartz powers. Choosing `N` and the Schwartz power after a prescribed `B` proves (5).

Since

\[
M|\Theta_T|=O(q\log\log T),
\tag{15}
\]

(5) implies

\[
\mathfrak E_T^{\Xi}(t)
\ll q\log\log T\,(\log T)^{-2B}=o(1)
\tag{16}
\]

for sufficiently large fixed `B`, proving (4) uniformly for `0\le t\le t_0`.

## 2. The first-order chirp response is its local-frequency Fourier transform

Put

\[
u_j:=\cos\Phi_j,
\qquad
A_0=0,
\qquad
A_{j+1}-A_j=u_j.
\tag{17}
\]

Then the XF-057 positions are

\[
z_j=T+j\sigma_T+\sigma_T\epsilon A_j.
\tag{18}
\]

At the reference lattice `x_j^0=T+j\sigma_T`, write

\[
g_j:=g(j/M),
\qquad
B_g(\theta):=\sum_jA_jg_je^{-i\theta j}.
\tag{19}
\]

After removing the harmless unit phase `e^{-i\varphi_{\theta,T}}`, Taylor expansion of the exact statistic (9) gives the first-order term

\[
L_T(\theta)
=\epsilon\left[
\frac1M B_{g'}(\theta)-i\theta B_g(\theta)
\right].
\tag{20}
\]

The zeroth-order lattice sum vanishes exactly on `\Theta_T` by the same Poisson-support argument as XF-056/XF-057.

Define

\[
U_T(\theta)
:=\sum_j u_jg((j+1)/M)e^{-i\theta j}.
\tag{21}
\]

The primitive identity `A_{j+1}-A_j=u_j` gives

\[
(e^{i\theta}-1)B_g(\theta)
=U_T(\theta)+C_g(\theta),
\tag{22}
\]

where

\[
C_g(\theta)
:=\sum_jA_j\bigl(g((j+1)/M)-g(j/M)\bigr)e^{-i\theta j}.
\tag{23}
\]

Since `g` is Schwartz,

\[
C_g(\theta)=\frac1M B_{g'}(\theta)+D_g(\theta).
\tag{24}
\]

XF-057 proves

\[
|A_j|\ll q^{3/2}+|j|q^{-3/2},
\qquad
\sup_{\theta\in\Theta_T}|B_g(\theta)|=O_g(q^{5/2}),
\tag{25}
\]

and the second-order Taylor remainder of the envelope in (24) gives

\[
D_g(\theta)=O_g(q^{-1/2}).
\tag{26}
\]

Substituting (22)--(24) into (20) yields the exact first-order decomposition

\[
\boxed{
L_T(\theta)
=-\epsilon U_T(\theta)
+\epsilon\mathcal R_T^{(1)}(\theta),
}
\tag{27}
\]

with

\[
\mathcal R_T^{(1)}(\theta)
=(e^{i\theta}-1-i\theta)B_g(\theta)-D_g(\theta).
\tag{28}
\]

Because `theta=O(log log T/q)`, equations (25)--(28) imply

\[
\int_{\Theta_T}|\mathcal R_T^{(1)}(\theta)|^2d\theta
=O_g((\log\log T)^5).
\tag{29}
\]

Since `M epsilon^2=kappa^2/M`, this error is `o(1)` after applying the normalized square-function factor `M`.

## 3. Plancherel keeps order `M` chirp energy in the slow cone

Write

\[
U_T(\theta)
=\frac12(V_{+,T}(\theta)+V_{-,T}(\theta)),
\tag{30}
\]

\[
V_{\pm,T}(\theta)
:=\sum_jg((j+1)/M)e^{\pm i\Phi_j}e^{-i\theta j}.
\tag{31}
\]

Discrete Plancherel gives

\[
\int_{-\pi}^{\pi}|V_{\pm,T}(\theta)|^2d\theta
=2\pi M\|g\|_2^2+o(M).
\tag{32}
\]

Fix a small `eta>0`. Choose a fixed `L` and a smooth cutoff `psi`, equal to one on `[-L,L]` and supported in `[-L-1,L+1]`, such that

\[
\|(1-\psi)g\|_2^2\le\eta\|g\|_2^2.
\tag{33}
\]

Then choose fixed `a_0` with

\[
a_0>b(L+2)+2c.
\tag{34}
\]

On the core support,

\[
\Phi_{j+1}-\Phi_j
=\frac{a_0+b(j/M)+o(1)}q,
\tag{35}
\]

so the positive branch stays a fixed `1/q`-scale distance above the lower edge `c/q`, and eventually lies below the upper edge `C log log T/q`.

Below the lower edge, the increments of `Phi_j-theta j` are monotone and nonstationary. The elementary first-derivative/Kusmin--Landau summation-by-parts bound gives the reciprocal-distance estimate

\[
|V_{+,T}^{\rm core}(\theta)|
\ll
\frac1{q^{-1}+\operatorname{dist}(\theta,[c/q,\infty))}.
\tag{36}
\]

Squaring and integrating shows that only `O(q)=o(M)` core energy lies below the cone.

For the upper edge, if

\[
v_j=\psi(j/M)g((j+1)/M)e^{i\Phi_j},
\tag{37}
\]

then the envelope changes by `O(1/M)` and the phase by `O(1/q)`, hence

\[
\sum_j|v_{j+1}-v_j|^2=O(1).
\tag{38}
\]

Parseval for first differences yields

\[
\int_{-\pi}^{\pi}|e^{i\theta}-1|^2
|V_{+,T}^{\rm core}(\theta)|^2d\theta=O(1),
\tag{39}
\]

so the energy above `C log log T/q` is

\[
O\!\left(\frac{q^2}{(\log\log T)^2}\right)=o(M).
\tag{40}
\]

The negative branch is nonstationary throughout the positive cone, and the same first-derivative estimate gives

\[
\int_{\Theta_T}|V_{-,T}^{\rm core}(\theta)|^2d\theta=O(q)=o(M).
\tag{41}
\]

The discarded tails have full Fourier `L^2` norm `O(sqrt(eta M))` by Plancherel. Taking `eta` sufficiently small and using the reverse triangle inequality in `L^2(Theta_T)` gives constants `0<c_g<C_g<infinity` such that

\[
\boxed{
c_gM
\le\int_{\Theta_T}|U_T(\theta)|^2d\theta
\le C_gM.
}
\tag{42}
\]

Combining (27), (29), and (42) with `epsilon=kappa/M` gives

\[
\boxed{
\int_{\Theta_T}|L_T(\theta)|^2d\theta
\asymp\frac{\kappa^2}{M}.
}
\tag{43}
\]

## 4. The exact nonlinear statistic has the same normalized energy

XF-057 bounds the complete quadratic Taylor remainder of the exact displaced-point statistic by

\[
|R_T(\theta)|
=O\!\left(\frac{\kappa^2(\log\log T)^2}{q}\right)
\tag{44}
\]

uniformly on `Theta_T`. Hence

\[
M\int_{\Theta_T}|R_T(\theta)|^2d\theta
=O\!\left(\frac{(\log\log T)^5}{q}\right)=o(1).
\tag{45}
\]

The cross term between `L_T` and `R_T` is also `o(1)` after multiplication by `M`, by Cauchy--Schwarz and (43)--(45). This proves (10) for the exact statistic (9), not merely for a linearized gap field.

## 5. Stress tests and evidence boundary

When `b=0`, the control becomes one coherent wave: its order-one response occupies one `1/M` band and still has order-one normalized energy. For fixed `b>0`, XF-057 spreads the response over `Theta(q)` cells so every pointwise coefficient vanishes, while (42)--(45) show that the normalized energy remains order one. The square-function normalization therefore has the correct calibration on both controls.

The choice (34) is only a convenient matched-control parameter selection. `a_0` stays fixed, so all core frequencies remain `Theta(1/q)` and eventually lie in the XF-056 cone. The XF-057 critical amplitude and the conclusion `M V_M asymp 1` are unchanged.

No lower-frame inequality is proved for an arbitrary transition-side gap field. No deterministic theorem yet bounds `M V_M` by `mathfrak E_T`. Ultraslow frequencies `o(1/q)`, sparse defects, mixed low/high geometry, and moving physical localization are not controlled here. The chirp remains a matched finite-gap control rather than an asserted Xi zero block or positive-time Xi trajectory. No upper bound on the de Bruijn--Newman constant follows from XF-058 alone.

The durable conclusion is narrower: **square-function aggregation survives the exact matched obstruction that kills pointwise-frequency coercivity, and the Xi source estimate is quantitatively strong enough on that norm.**

## 6. Prior-art and novelty boundary

Discrete Plancherel, first-difference Fourier energy, Abel summation, Kusmin--Landau/first-derivative exponential-sum bounds, and square functions are classical. The Graham--Kolesnik exponential-sum reference already anchored in `SOURCES.md` covers the classical oscillatory-estimate background used here. No new load-bearing source is introduced.

A targeted audit of de Bruijn--Newman heat-flow work, Fourier formulations around Xi, chirp exponential-sum estimates, and standard time-frequency/square-function identities did not locate this scale-matched source-to-transition statement. No novelty is claimed for Parseval, square functions, or the generic Fourier spreading of a chirp. The line-specific delta is the simultaneous scale match

\[
M=q^2,
\qquad
\epsilon=M^{-1},
\qquad
\Phi''\asymp q^{-3},
\qquad
|\Theta_T|\asymp\frac{\log\log T}{q},
\tag{46}
\]

together with the rapid Xi estimate (5): the normalized selector square energy vanishes for the actual Xi carrier while remaining order one on the exact critical chirp that defeats every pointwise selector. `SOURCES.md` therefore requires no modification.

## 7. Consequence for `xi_flow`

XF-057 identifies frequency spreading, rather than detuning, as the current source-to-transition loss. XF-058 shows that `L^2` aggregation repairs that spreading on the canonical matched obstruction. The continuous selector family contains enough aggregate information to pass this control; what remains is to transfer that information coercively to the transition-side gap/flux observable.

The next constructive theorem should preserve the `M dtheta` normalization in (3) and produce one of two outcomes: a lower-frame/square-function estimate strong enough to force `M V_M=o(1)` for the relevant transition field, or a stronger matched configuration with nonvanishing critical flux but vanishing normalized square energy. Denser pointwise sampling cannot decide that question.