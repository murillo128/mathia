# XF-058 — normalized selector square function detects the critical chirp

**Status:** `EXACT-DERIVED` + `RAPID-SOURCE-DECAY` + `MATCHED-CONTROL` + `AGGREGATE-SEPARATION`. XF-056 proves that the actual Xi carrier is `o(1)` against every individual compact selector whose center moves continuously through the slow Cauchy cone. XF-057 then proves that a supremum over those pointwise coefficients is not coercive: a quadratic chirp spreads critical triple-flux variation over many `1/M` frequency cells and makes every individual coefficient vanish.

The same chirp does **not** escape the naturally normalized square function of the selector family. Use the XF-056/XF-057 scales

\[
q\asymp \log^2T,
\qquad
M=q^2,
\qquad
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\qquad
W=M\sigma_T,
\tag{1}
\]

and the continuous slow-frequency cone

\[
\Theta_T=
\left[\frac cq,\frac{C\log\log T}{q}\right].
\tag{2}
\]

For the actual Xi carrier, define

\[
\mathfrak E_T^{\Xi}(t)
:=
M\int_{\Theta_T}
|\mathcal S_{T,\theta}(t)|^2\,d\theta,
\tag{3}
\]

where `\mathcal S_{T,theta}` is exactly the XF-056 carrier statistic. Then for every fixed `t_0>0`,

\[
\boxed{
\sup_{0\le t\le t_0}
\mathfrak E_T^{\Xi}(t)=o(1).
}
\tag{4}
\]

In fact the proof already present in XF-056 is quantitatively stronger: for every fixed `B>0`,

\[
\boxed{
\sup_{0\le t\le t_0}
\sup_{\theta\in\Theta_T}
|\mathcal S_{T,\theta}(t)|
=O_B((\log T)^{-B}).
}
\tag{5}
\]

On the matched-control side, take the XF-057 chirp

\[
\Phi_j=\frac{a_0}{q}j+\frac{b}{2q^3}j^2,
\qquad
\varepsilon=\frac\kappa M,
\tag{6}
\]

\[
z_{j+1}-z_j
=\sigma_T(1+\varepsilon\cos\Phi_j),
\qquad z_0=T,
\tag{7}
\]

with fixed `b,kappa>0`. Let the exact XF-056 probe be

\[
f_{T,\theta}(x)
=
g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega_{\theta,T}(x-T)+\varphi_{\theta,T})},
\qquad
\omega_{\theta,T}=\frac{\theta}{\sigma_T},
\tag{8}
\]

and define the exact matched-control statistic

\[
\boxed{
S_T^{\rm chirp}(\theta)
:=
\sum_{j\in\mathbb Z} f_{T,\theta}(z_j).
}
\tag{9}
\]

For every fixed nonzero XF-056 envelope `g`, the admissible constant `a_0` can be chosen sufficiently large relative to `b` and `g`, while remaining fixed as `T\to\infty`, so that

\[
\boxed{
0<
\liminf_{T\to\infty}
M\int_{\Theta_T}|S_T^{\rm chirp}(\theta)|^2\,d\theta
\le
\limsup_{T\to\infty}
M\int_{\Theta_T}|S_T^{\rm chirp}(\theta)|^2\,d\theta
<\infty.
}
\tag{10}
\]

The arbitrary phases `\varphi_{\theta,T}` disappear after taking absolute values. Thus XF-057's obstruction is specifically a **pointwise-frequency obstruction**. The same exact chirp has

\[
\sup_{\theta\in\Theta_T}|S_T^{\rm chirp}(\theta)|=o(1),
\qquad
M V_M\asymp1,
\tag{11}
\]

but its normalized aggregate energy (10) remains nonzero.

The normalization by `M` is forced by the selector resolution. One XF-056 band has index-frequency width `1/M`; an order-one coherent response occupying one such band therefore has unnormalized `L^2(d\theta)` energy of order `1/M`. Equation (10) says that spreading the same critical budget over many cells does not destroy that normalized energy.

This does **not** prove the missing source-to-transition inverse theorem. It establishes a narrower but decisive compatibility fact: the first aggregate norm suggested after XF-057 survives the canonical chirped obstruction, and the Xi moving-line estimate is already strong enough to make that aggregate vanish at the source.

## 1. XF-056 already gives rapid logarithmic decay

The moving-line proof in XF-056 takes

\[
a_T=A\log T
\tag{12}
\]

and writes the carrier pairing as an integral of the horizontal logarithmic derivative against the shifted oscillatory probe. Uniformly over `\Theta_T`, the height factor costs only a fixed polylogarithm,

\[
e^{a_T\omega_{\theta,T}}
\le(\log T)^K,
\tag{13}
\]

while the reflected Euler-product remainder is

\[
O(T^{-\kappa_A}(\log T)^{K_1}).
\tag{14}
\]

After integration over the physical window of width `W`, this arithmetic remainder beats every fixed negative power of `\log T`.

For the deterministic gamma/polar background, the exact scale identity is

\[
W\omega_{\theta,T}=M\theta\ge cq\asymp\log^2T.
\tag{15}
\]

The XF-056 integration-by-parts argument can be repeated any fixed number `N` of times. The term with all derivatives on the envelope is bounded by

\[
O_N\!\left((\log T)^{K_2}W(M\theta)^{-N}\right),
\tag{16}
\]

and every derivative falling on the deterministic background gains a factor `W/T`, up to fixed powers of `\log T`. The physical tails are killed by an arbitrarily high fixed Schwartz power of `g`. Therefore, for each prescribed fixed `B`, choose `N` and the Schwartz power sufficiently large. The same proof gives (5), not merely `o(1)`.

Since

\[
|\Theta_T|
=O\!\left(\frac{\log\log T}{q}\right),
\qquad
M=q^2,
\tag{17}
\]

we obtain

\[
\mathfrak E_T^{\Xi}(t)
\le
M|\Theta_T|
\sup_{\theta\in\Theta_T}|\mathcal S_{T,\theta}(t)|^2
\ll
q\log\log T\,(\log T)^{-2B}.
\tag{18}
\]

Taking `B` sufficiently large proves (4), uniformly for `0\le t\le t_0`. No new Xi input is used here; this only retains the quantitative freedom already present in XF-054--XF-056.

## 2. The first-order chirp response is a Fourier transform of the local modulation

Put

\[
u_j:=\cos\Phi_j,
\qquad
A_0=0,
\qquad
A_{j+1}-A_j=u_j.
\tag{19}
\]

Then XF-057 gives the exact positions

\[
z_j=T+j\sigma_T+\sigma_T\varepsilon A_j.
\tag{20}
\]

At the reference lattice points `x_j^0=T+j\sigma_T`, write

\[
g_j:=g(j/M),
\qquad
B_g(\theta):=
\sum_j A_jg_j e^{-i\theta j}.
\tag{21}
\]

Absorb the harmless unit phase `e^{-i\varphi_{\theta,T}}`. Taylor expansion of the **exact** statistic (9) around the reference lattice gives the first-order contribution

\[
L_T(\theta)
=
\varepsilon
\left[
\frac1M B_{g'}(\theta)-i\theta B_g(\theta)
\right].
\tag{22}
\]

The zeroth-order arithmetic-lattice sum vanishes exactly on `\Theta_T` by the same Poisson-support argument used in XF-056 and XF-057.

Define

\[
U_T(\theta)
:=
\sum_j u_j g((j+1)/M)e^{-i\theta j}.
\tag{23}
\]

The discrete primitive relation in (19) gives the exact identity

\[
(e^{i\theta}-1)B_g(\theta)
=U_T(\theta)+C_g(\theta),
\tag{24}
\]

with

\[
C_g(\theta)
:=
\sum_j A_j
\bigl(g((j+1)/M)-g(j/M)\bigr)e^{-i\theta j}.
\tag{25}
\]

Because `g` is Schwartz,

\[
C_g(\theta)
=\frac1M B_{g'}(\theta)+D_g(\theta),
\tag{26}
\]

where the XF-057 bound

\[
|A_j|\ll q^{3/2}+|j|q^{-3/2}
\tag{27}
\]

implies uniformly

\[
D_g(\theta)=O_g(q^{-1/2}).
\tag{28}
\]

Substitution into (22) yields

\[
\boxed{
L_T(\theta)
=-\varepsilon U_T(\theta)
+arepsilon
\left[(e^{i\theta}-1-i\theta)B_g(\theta)-D_g(\theta)\right].
}
\tag{29}
\]

Thus the leading selector response is the Fourier transform of the local chirped gap modulation, not one coherent coefficient.

XF-057 already proves

\[
\sup_{\theta\in\Theta_T}|B_g(\theta)|=O_g(q^{5/2}).
\tag{30}
\]

Since `\theta=O(\log\log T/q)` and `e^{i\theta}-1-i\theta=O(\theta^2)`, equations (28)--(30) give

\[
\int_{\Theta_T}
\left|
(e^{i\theta}-1-i\theta)B_g(\theta)-D_g(\theta)
\right|^2d\theta
=O_g((\log\log T)^5).
\tag{31}
\]

Because `M\varepsilon^2=\kappa^2/M`, the error term in (29) contributes `o(1)` to the normalized square energy.

## 3. A fixed fraction of the chirp's Plancherel energy lies in the slow cone

Decompose

\[
U_T(\theta)
=\frac12\bigl(V_{+,T}(\theta)+V_{-,T}(\theta)\bigr),
\tag{32}
\]

where

\[
V_{\pm,T}(\theta)
:=
\sum_j g((j+1)/M)e^{\pm i\Phi_j}e^{-i\theta j}.
\tag{33}
\]

Discrete Plancherel gives

\[
\int_{-\pi}^{\pi}|V_{\pm,T}(\theta)|^2d\theta
=2\pi\sum_j|g((j+1)/M)|^2
=2\pi M\|g\|_2^2+o(M).
\tag{34}
\]

We now localize only for the proof of the lower bound. Fix a small `\eta>0`. Since `g` is Schwartz, choose a fixed `L` and a smooth cutoff `\psi` equal to one on `[-L,L]` and supported in `[-L-1,L+1]` such that

\[
\|(1-\psi)g\|_2^2\le\eta\|g\|_2^2.
\tag{35}
\]

Then choose the fixed chirp parameter `a_0` so large that

\[
a_0>b(L+2)+2c.
\tag{36}
\]

On the support of the core sequence `\psi(j/M)g((j+1)/M)e^{i\Phi_j}`, the phase increments satisfy

\[
\Phi_{j+1}-\Phi_j
=
\frac{a_0+b(j/M)+o(1)}q.
\tag{37}
\]

Hence they stay a fixed positive distance, on the `1/q` scale, above the lower edge `c/q`; because `a_0,b,L` are fixed, they are also below `C\log\log T/q` for all sufficiently large `T`.

For frequencies below the lower cone edge, the increments of `\Phi_j-\theta j` are monotone and remain separated from zero. The elementary first-derivative/Kusmin--Landau summation-by-parts estimate therefore gives the reciprocal-distance bound

\[
|V_{+,T}^{\rm core}(\theta)|
\ll
\frac1{q^{-1}+\operatorname{dist}(\theta,[c/q,\infty))}
\tag{38}
\]

through the low-frequency complement, up to a constant depending only on the fixed cutoff and chirp parameters. One direct proof telescopes with

\[
e^{i\psi_j}
=
\frac{e^{i\psi_{j+1}}-e^{i\psi_j}}
{e^{i(\psi_{j+1}-\psi_j)}-1}
\tag{39}
\]

and then performs one Abel summation. Squaring and integrating (38) shows that only `O(q)=o(M)` core energy lies below the lower edge.

At the upper edge, let

\[
v_j=\psi(j/M)g((j+1)/M)e^{i\Phi_j}.
\tag{40}
\]

The envelope varies by `O(1/M)` and the phase by `O(1/q)`, so

\[
\sum_j|v_{j+1}-v_j|^2=O(1).
\tag{41}
\]

Parseval for the first difference yields

\[
\int_{-\pi}^{\pi}
|e^{i\theta}-1|^2
|V_{+,T}^{\rm core}(\theta)|^2d\theta
=O(1).
\tag{42}
\]

Therefore the core energy above `C\log\log T/q` is

\[
O\!\left(\frac{q^2}{(\log\log T)^2}\right)
=o(M).
\tag{43}
\]

The negative-frequency core `V_-^{\rm core}` is nonstationary throughout the positive cone because its phase increments are `-(\Phi_{j+1}-\Phi_j)-\theta`. The same reciprocal-distance estimate gives

\[
\int_{\Theta_T}|V_{-,T}^{\rm core}(\theta)|^2d\theta
=O(q)=o(M).
\tag{44}
\]

The discarded tails have full Fourier `L^2` norm `O(\sqrt{\eta M})` by Plancherel. Choose `\eta` sufficiently small and then keep it fixed. The reverse triangle inequality in `L^2(\Theta_T)`, together with (34) and (38)--(44), gives fixed constants `0<c_g<C_g<\infty` such that

\[
\boxed{
c_gM
\le
\int_{\Theta_T}|U_T(\theta)|^2d\theta
\le
C_gM.
}
\tag{45}
\]

The upper bound is immediate from full-circle Plancherel. Equation (45) is the aggregate fact hidden by XF-057's pointwise estimate: each resolution cell is weak, but the total `L^2` energy over all occupied cells is still order `M` before multiplication by the critical amplitude.

Combining (29), (31), and (45), with `\varepsilon=\kappa/M`, gives

\[
\boxed{
\int_{\Theta_T}|L_T(\theta)|^2d\theta
\asymp\frac{\kappa^2}{M}.
}
\tag{46}
\]

## 4. The exact nonlinear statistic has the same normalized energy

XF-057 bounds the complete quadratic Taylor remainder of the exact displaced-point statistic uniformly on `\Theta_T` by

\[
|R_T(\theta)|
=O\!\left(
\frac{\kappa^2(\log\log T)^2}{q}
\right).
\tag{47}
\]

Consequently

\[
\begin{aligned}
M\int_{\Theta_T}|R_T(\theta)|^2d\theta
&\ll
q^2\cdot\frac{\log\log T}{q}
\cdot\frac{(\log\log T)^4}{q^2}\\
&=O\!\left(\frac{(\log\log T)^5}{q}\right)
=o(1).
\end{aligned}
\tag{48}
\]

The cross term between `L_T` and `R_T` is also `o(1)` after multiplication by `M`, by Cauchy--Schwarz and (46)--(48). This proves (10) for the **exact** matched-control statistic (9), not merely for a linearized gap field.

That nonlinear check is important: XF-057's pointwise blindness is an exact displaced-zero statement, so the aggregate recovery must survive at the same level. It does.

## 5. Stress tests and evidence boundary

If `b=0`, the control becomes one coherent wave. Its order-one response is concentrated in one `1/M`-scale band, and the normalized square energy is still order one. For fixed `b>0`, the quadratic chirp spreads the response over `Theta(q)` selector cells and lowers each pointwise coefficient to `o(1)`, but equations (45)--(48) show that the normalized total energy remains order one. Thus the square function has the correct calibration on both controls.

The choice (36) is only a convenient matched-control parameter selection. `a_0` remains fixed, so all core frequencies are still `Theta(1/q)` and eventually lie inside the XF-056 cone. The XF-057 critical amplitude `\varepsilon=\kappa/M` and the conclusion `M V_M\asymp1` are unchanged.

Several stronger statements remain open. No lower-frame inequality is proved for an arbitrary transition-side gap field; no deterministic theorem yet bounds `M V_M` by `\mathfrak E_T`; ultraslow frequencies `o(1/q)`, sparse defects, mixed low/high geometry, and moving physical localization are not controlled by (4); and the matched chirp is not asserted to be an actual Xi zero block or an exact positive-time Xi trajectory. In particular, no upper bound on the de Bruijn--Newman constant follows from XF-058 alone.

The durable conclusion is narrower: **the square-function route survives the exact matched obstruction that kills pointwise-frequency coercivity, and the Xi source estimate is quantitatively strong enough on that norm.** The next gate is an actual source-to-transition frame/coercivity inequality, or a stronger matched obstruction that also makes the normalized square energy vanish.

## 6. Prior-art and novelty boundary

Discrete Plancherel, first-difference Fourier energy, Abel summation, the Kusmin--Landau/first-derivative exponential-sum estimate, and square-function aggregation are classical. The Graham--Kolesnik exponential-sum reference already anchored in `SOURCES.md` covers the classical oscillatory-estimate background used here. No new load-bearing external source is introduced.

A targeted literature audit of de Bruijn--Newman heat-flow work, Fourier formulations around Xi, exponential-sum chirp estimates, and standard time-frequency/square-function identities did not locate a theorem supplying this scale-matched source-to-transition statement. No novelty is claimed for Parseval, square functions, or the generic fact that a chirp distributes Fourier energy. The line-specific delta is the simultaneous scaling

\[
M=q^2,
\qquad
\varepsilon=M^{-1},
\qquad
\Phi''\asymp q^{-3},
\qquad
|\Theta_T|\asymp\frac{\log\log T}{q},
\tag{49}
\]

together with the rapid Xi estimate (5): the normalized selector square energy vanishes for the actual Xi carrier while remaining order one on the exact critical chirp that defeats every pointwise selector.

`SOURCES.md` therefore requires no modification.

## 7. Consequence for `xi_flow`

XF-057 identifies frequency spreading, rather than frequency detuning, as the current source-to-transition loss. XF-058 shows that `L^2` aggregation repairs that spreading on the canonical matched obstruction. The continuous selector family therefore contains enough aggregate information to pass this control; the unresolved question is whether that information can be transferred coercively to the transition-side gap/flux observable.

The next constructive theorem should preserve the `M\,d\theta` normalization in (3) and prove one of two outcomes: either a lower-frame/square-function estimate that dominates the relevant low-frequency part of the transition field strongly enough to force `M V_M=o(1)`, or a new matched configuration with nonvanishing critical flux but vanishing normalized square energy. Denser pointwise sampling cannot decide that question.