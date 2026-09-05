# XF-058 — normalized selector square function detects the critical chirp

**Status:** `EXACT-DERIVED` + `RAPID-SOURCE-DECAY` + `MATCHED-CONTROL` + `AGGREGATE-SEPARATION`. XF-056 proves that the actual Xi carrier is `o(1)` against every individual compact selector whose center moves continuously through the slow Cauchy cone. XF-057 then shows that taking a supremum over those pointwise coefficients is not coercive: a quadratic chirp spreads critical triple-flux variation over many `1/M` frequency cells and makes every individual coefficient vanish.

The same chirp does **not** escape the naturally normalized square function of the selector family. With the XF-056/XF-057 scales

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

and continuous slow-frequency cone

\[
\Theta_T=
\left[\frac cq,\frac{C\log\log T}{q}\right],
\tag{2}
\]

define for the actual Xi carrier

\[
\mathfrak E_T^{\Xi}(t)
:=
M\int_{\Theta_T}
|\mathcal S_{T,\theta}(t)|^2\,d\theta,
\tag{3}
\]

where `\mathcal S_{T,theta}` is exactly the XF-056 statistic. Then for every fixed `t_0>0`,

\[
\boxed{
\sup_{0\le t\le t_0}
\mathfrak E_T^{\Xi}(t)=o(1).
}
\tag{4}
\]

In fact the pointwise estimate underlying XF-056 is rapidly logarithmically small: for every fixed `B>0`,

\[
\boxed{
\sup_{0\le t\le t_0}
\sup_{\theta\in\Theta_T}
|\mathcal S_{T,\theta}(t)|
=O_B((\log T)^{-B}).
}
\tag{5}
\]

On the matched-control side, use the XF-057 chirp

\[
\Phi_j=\frac{a_0}{q}j+\frac{b}{2q^3}j^2,
\qquad
\varepsilon=\frac\kappa M,
\tag{6}
\]

\[
z_{j+1}-z_j
=\sigma_T(1+\varepsilon\cos\Phi_j),
\tag{7}
\]

with fixed `b,kappa>0`. For every fixed nonzero XF-056 envelope `g`, the admissible constant `a_0` may be chosen sufficiently large relative to `b` and `g` while remaining fixed as `T\to\infty`. For such a choice, if

\[
S_T^{\rm chirp}(\theta)
:=
\sum_{j\in\mathbb Z}
 g(j/M)
 e^{-i(\theta j+\varphi_{\theta,T})}
\quad\text{evaluated at the displaced points }z_j
\tag{8}
\]

is the same matched zero statistic as in XF-057 (equivalently the exact XF-056 probe summed over the control points), then

\[
\boxed{
0<
\liminf_{T\to\infty}
M\int_{\Theta_T}
|S_T^{\rm chirp}(\theta)|^2\,d\theta
\le
\limsup_{T\to\infty}
M\int_{\Theta_T}
|S_T^{\rm chirp}(\theta)|^2\,d\theta
<\infty.
}
\tag{9}
\]

The arbitrary probe phases disappear after taking absolute values. Thus the exact obstruction in XF-057 is specifically a **pointwise-frequency obstruction**, not an obstruction to square-function aggregation. The chirp makes

\[
\sup_{\theta\in\Theta_T}|S_T^{\rm chirp}(\theta)|=o(1)
\tag{10}
\]

while retaining both

\[
M V_M\asymp 1
\tag{11}
\]

and the nonvanishing aggregate (9).

The normalization by `M` in (3) and (9) is the natural one: an XF-056 selector has frequency resolution `1/M`, so an order-one coherent response occupying one resolution cell has unnormalized `L^2(d\theta)` energy of order `1/M`. The square function preserves that scale when the same budget is spread over a growing number of cells.

This does **not** yet prove the missing source-to-transition inverse theorem. It proves a narrower but decisive compatibility fact: the first aggregate norm suggested after XF-057 is not killed by the chirped matched control, and the existing Xi moving-line argument is quantitatively strong enough to make that aggregate vanish at the source.

## 1. XF-056 already contains rapid logarithmic pointwise decay

The proof of XF-056 uses the moving zero-free line

\[
a_T=A\log T
\tag{12}
\]

and writes the carrier pairing as an integral of the horizontal logarithmic derivative against the shifted oscillatory probe. Uniformly over the continuous cone, the height cost is only polylogarithmic:

\[
e^{a_T\omega_{\theta,T}}
\le (\log T)^K
\tag{13}
\]

for a fixed `K=K(A,C)`. The reflected Euler-product remainder is

\[
O(T^{-\kappa_A}(\log T)^{K_1})
\tag{14}
\]

on the physical `W`-window, so after multiplying by the window size and by (13) it beats every fixed negative power of `\log T`.

For the deterministic gamma/polar background, XF-056 gives

\[
W\omega_{\theta,T}
=M\theta
\ge cq
\asymp \log^2T.
\tag{15}
\]

Repeated integration by parts may be performed any fixed number `N` of times. The term with all derivatives on the envelope is bounded by

\[
O_N\!\left(
(\log T)^{K_2}W(M\theta)^{-N}
\right),
\tag{16}
\]

while terms with derivatives on the deterministic background gain powers of `W/T`, up to fixed logarithmic factors. The physical tails are controlled by arbitrarily high fixed Schwartz powers of `g`. Therefore, after choosing `N` and the Schwartz power in terms of a prescribed fixed `B`, the same proof gives (5), not merely `o(1)`.

Since

\[
|\Theta_T|
=O\!\left(\frac{\log\log T}{q}\right),
\qquad
M=q^2,
\tag{17}
\]

one has

\[
\mathfrak E_T^{\Xi}(t)
\le
M|\Theta_T|
\sup_{\theta\in\Theta_T}|\mathcal S_{T,\theta}(t)|^2
\ll
q\log\log T\,(\log T)^{-2B}.
\tag{18}
\]

Taking any sufficiently large fixed `B` proves (4), uniformly for `0\le t\le t_0`.

This rapid-decay extraction uses no new Xi input beyond XF-054--XF-056. It only keeps the quantitative freedom already present in the moving-line proof instead of stopping once `o(1)` has been obtained.

## 2. The chirp's first-order selector response is its local-frequency Fourier transform

Write

\[
u_j:=\cos\Phi_j,
\qquad
A_0=0,
\qquad
A_{j+1}-A_j=u_j.
\tag{19}
\]

Then XF-057 gives

\[
z_j=T+j\sigma_T+\sigma_T\varepsilon A_j.
\tag{20}
\]

For notational simplicity absorb the harmless phase `e^{-i\varphi_{\theta,T}}` and put

\[
g_j:=g(j/M),
\qquad
B_g(\theta):=
\sum_j A_jg_j e^{-i\theta j}.
\tag{21}
\]

Taylor expansion of the exact XF-056 probe around the arithmetic lattice gives the first-order response

\[
L_T(\theta)
=
\varepsilon
\left[
\frac1M B_{g'}(\theta)-i\theta B_g(\theta)
\right].
\tag{22}
\]

The arithmetic-lattice zeroth-order term vanishes exactly on `\Theta_T` by the same Poisson-support argument as XF-056/XF-057.

Now define

\[
U_T(\theta)
:=
\sum_j u_j g((j+1)/M)e^{-i\theta j}.
\tag{23}
\]

The discrete primitive (19) gives the exact summation-by-parts identity

\[
(e^{i\theta}-1)B_g(\theta)
=U_T(\theta)+C_g(\theta),
\tag{24}
\]

where

\[
C_g(\theta)
:=
\sum_j A_j
\bigl(g((j+1)/M)-g(j/M)\bigr)e^{-i\theta j}.
\tag{25}
\]

Taylor expansion of the slowly varying envelope gives

\[
C_g(\theta)
=\frac1M B_{g'}(\theta)+D_g(\theta),
\tag{26}
\]

with `D_g` lower order. Substituting (24)--(26) into (22) yields

\[
\boxed{
L_T(\theta)
=-\varepsilon U_T(\theta)
+arepsilon
\left[(e^{i\theta}-1-i\theta)B_g(\theta)-D_g(\theta)\right].
}
\tag{27}
\]

The leading object is therefore not one coherent Fourier coefficient. It is the Fourier transform of the locally chirped gap modulation itself.

XF-057 already proves uniformly on `\Theta_T`

\[
|B_g(\theta)|=O_g(q^{5/2}).
\tag{28}
\]

Since `\theta=O(\log\log T/q)`, the multiplier in the error of (27) is `O(\theta^2)`. The Schwartz Taylor remainder in (26), together with the XF-057 bound

\[
|A_j|\ll q^{3/2}+|j|q^{-3/2},
\tag{29}
\]

gives `D_g(\theta)=O_g(q^{-1/2})`. Consequently

\[
\int_{\Theta_T}
\left|
(e^{i\theta}-1-i\theta)B_g(\theta)-D_g(\theta)
\right|^2d\theta
=O_g((\log\log T)^5).
\tag{30}
\]

Multiplying by `M\varepsilon^2=\kappa^2/M` shows that the error in (27) contributes `o(1)` to the normalized square energy (9).

## 3. Plancherel puts order `M` chirp energy inside the slow cone

Decompose

\[
U_T(\theta)
=\frac12\bigl(V_{+,T}(\theta)+V_{-,T}(\theta)\bigr),
\tag{31}
\]

\[
V_{\pm,T}(\theta)
:=
\sum_j
 g((j+1)/M)e^{\pm i\Phi_j}e^{-i\theta j}.
\tag{32}
\]

Discrete Plancherel gives the full-circle identity

\[
\int_{-\pi}^{\pi}
|V_{\pm,T}(\theta)|^2\,d\theta
=
2\pi\sum_j|g((j+1)/M)|^2
=2\pi M\|g\|_2^2+o(M).
\tag{33}
\]

It remains to show that a fixed positive fraction of the `V_+` energy lies in `\Theta_T`, while the corresponding `V_-` contribution there can be made negligible relative to that fraction.

Fix a small `\eta>0`. Because `g` is Schwartz, choose a fixed `L` so large that

\[
\int_{|x|>L}|g(x)|^2\,dx
\le \eta\|g\|_2^2.
\tag{34}
\]

Then choose the admissible fixed chirp parameter `a_0` so large that

\[
a_0>b(L+2)+2c.
\tag{35}
\]

On the central region `|j|\le (L+1)M`, the phase increments satisfy

\[
\Phi_{j+1}-\Phi_j
=
\frac{a_0+b(j/M)+o(1)}q
\tag{36}
\]

and therefore remain a fixed positive distance, on the `1/q` scale, above the lower cone edge `c/q`. They also lie below the upper edge `C\log\log T/q` for all sufficiently large `T` because `a_0,b,L` are fixed.

Insert a fixed smooth cutoff that equals one on `|j|\le LM` and vanishes outside `|j|\le(L+1)M`. For the resulting central `V_+` sequence, the classical first-difference/nonstationary-phase summation-by-parts estimate gives only `O(q)` amplitude below the lower cone edge. More explicitly, when `\theta\le c/q`, the increments of `\Phi_j-\theta j` are monotone and have magnitude at least a fixed multiple of `1/q`; telescoping through

\[
e^{i\psi_j}
=
\frac{e^{i\psi_{j+1}}-e^{i\psi_j}}
{e^{i(\psi_{j+1}-\psi_j)}-1}
\tag{37}
\]

and one Abel summation gives the stated `O(q)` bound. Integrating the sharper reciprocal-distance version of the same estimate over the low-frequency complement costs only `O(q)=o(M)` square energy.

At the upper cone edge no pointwise exponential-sum estimate is needed. If

\[
v_j=g((j+1)/M)e^{i\Phi_j}
\tag{38}
\]

on the smoothly cut central block, then

\[
\sum_j|v_{j+1}-v_j|^2=O(1),
\tag{39}
\]

because the envelope changes by `O(1/M)` and the phase changes by `O(1/q)`, with `M=q^2`. Parseval for the first difference gives

\[
\int_{-\pi}^{\pi}
|e^{i\theta}-1|^2|V_{+,T}^{\rm core}(\theta)|^2\,d\theta
=O(1).
\tag{40}
\]

Hence the energy above `C\log\log T/q` is

\[
O\!\left(\frac{q^2}{(\log\log T)^2}\right)
=o(M).
\tag{41}
\]

The same nonstationary-phase estimate shows that the core of `V_-` has only `o(M)` square energy on the positive cone, because its phase increments there are `-(\Phi_{j+1}-\Phi_j)-\theta` and never approach zero.

The discarded `|j|>LM` tails have full Fourier `L^2` norm `O(\sqrt{\eta M})` by Plancherel. Choosing `\eta` sufficiently small and then keeping it fixed, the reverse triangle inequality in `L^2(\Theta_T)` gives constants `0<c_g<C_g<\infty`, independent of `T`, such that

\[
\boxed{
c_gM
\le
\int_{\Theta_T}|U_T(\theta)|^2\,d\theta
\le
C_gM.
}
\tag{42}
\]

The upper bound follows directly from full-circle Plancherel. This is the aggregate fact hidden by the pointwise estimate in XF-057: each resolution cell is weak, but the total `L^2` energy across all occupied cells is of order `M` before multiplication by the critical amplitude.

Combining (27), (30), and (42), with `\varepsilon=\kappa/M`, gives

\[
\int_{\Theta_T}|L_T(\theta)|^2\,d\theta
\asymp
\frac{\kappa^2}{M}.
\tag{43}
\]

## 4. The exact nonlinear probe has the same normalized square energy

XF-057 bounds the complete quadratic Taylor remainder of the exact displaced-point statistic uniformly over the cone by

\[
|R_T(\theta)|
=O\!\left(
\frac{\kappa^2(\log\log T)^2}{q}
\right).
\tag{44}
\]

Therefore

\[
\begin{aligned}
M\int_{\Theta_T}|R_T(\theta)|^2d\theta
&\ll
q^2\cdot\frac{\log\log T}{q}
\cdot
\frac{(\log\log T)^4}{q^2}\\
&=O\!\left(\frac{(\log\log T)^5}{q}\right)
=o(1).
\end{aligned}
\tag{45}
\]

The cross term between `L_T` and `R_T` is also `o(1)` after multiplication by `M`, by Cauchy--Schwarz and (43)--(45). Equations (43)--(45) prove the two-sided nonvanishing statement (9) for the exact XF-057 matched zero statistic.

This check matters because the pointwise blindness in XF-057 was established for the exact displaced points, not merely for a linearized gap field. The square-function recovery survives the same nonlinear Taylor error at the critical amplitude.

## 5. Stress tests and evidence boundary

The result is consistent with both limiting controls already in the line. If `b=0`, the chirp becomes one coherent wave and its order-one selector response is concentrated in a single `1/M` band; the normalized square energy is still order one. For fixed `b>0`, XF-057 spreads that response over `Theta(q)` bands and lowers every individual coefficient to `o(1)`, but (9) shows that the total normalized energy does not disappear.

The parameter choice (35) is not an arithmetic hypothesis and does not strengthen the source assumptions. It is only a convenient matched-control choice ensuring that essentially all of the fixed Schwartz envelope sees the positive-frequency branch before the tiny tail is discarded. Since `a_0` remains fixed, its local frequency is still `Theta(1/q)` and lies inside the XF-056 cone for large `T`. The triple-flux estimate of XF-057 remains unchanged in scale.

Several stronger conclusions are **not** established here. In particular:

- no lower-frame inequality is proved for an arbitrary transition-side gap field;
- no deterministic inequality yet bounds `M V_M` by `\mathfrak E_T` for general nonlinear configurations;
- ultraslow frequencies `o(1/q)`, sparse defects, mixed low/high geometry, and localization at moving physical centers are not controlled by (4);
- the matched chirp is still not asserted to be an actual Xi zero block or an exact positive-time Xi trajectory;
- no upper bound on the de Bruijn--Newman constant follows from (4) and (9) alone.

The durable conclusion is narrower: **the square-function route survives the exact matched obstruction that killed pointwise-frequency coercivity, and the Xi source estimate is already quantitatively strong enough on that norm.** The next gate should therefore be an actual source-to-transition frame/coercivity inequality, not another denser family of pointwise selectors.

## 6. Prior-art and novelty boundary

Discrete Plancherel, first-difference Fourier energy, Abel summation, the Kusmin--Landau/first-derivative exponential-sum estimate, and square-function aggregation are classical. The Graham--Kolesnik exponential-sum reference already anchored in `SOURCES.md` covers the classical oscillatory-estimate background used here; no new load-bearing external source is introduced.

A targeted literature check of de Bruijn--Newman heat-flow work, Fourier formulations around Xi, exponential-sum chirp estimates, and standard time-frequency/square-function identities did not locate a theorem that supplies this particular source-to-transition statement. No novelty is claimed for Parseval, square functions, or the generic fact that a chirp has distributed Fourier energy. The line-specific delta is the matched scale combination

\[
M=q^2,
\qquad
\varepsilon=M^{-1},
\qquad
\Phi''\asymp q^{-3},
\qquad
|\Theta_T|\asymp\frac{\log\log T}{q},
\tag{46}
\]

together with the rapid Xi bound (5): it makes the normalized selector square energy vanish for the actual Xi carrier while remaining order one on the exact critical chirp that defeats every pointwise selector.

`SOURCES.md` therefore requires no modification.

## 7. Consequence for `xi_flow`

XF-057 identifies frequency spreading, rather than frequency detuning, as the current source-to-transition loss. XF-058 now shows that this spreading is exactly what `L^2` aggregation repairs on the canonical matched obstruction. The existing continuous selector family contains enough aggregate information; the unresolved issue is whether that information can be transferred coercively to the transition-side gap/flux observable.

The next constructive theorem should preserve the `M\,d\theta` normalization in (3) and prove one of two things: either a lower-frame/square-function estimate that dominates the relevant low-frequency part of the transition field strongly enough to force `M V_M=o(1)`, or a new matched configuration with nonvanishing critical flux but vanishing normalized square energy. A new pointwise-frequency estimate cannot decide that question.