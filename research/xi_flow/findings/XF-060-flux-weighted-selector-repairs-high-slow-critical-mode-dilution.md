# XF-060 — flux-weighted selector repairs high-slow critical-mode dilution

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `NEGATIVE/OBSTRUCTION` + `WEIGHTED-REPAIR-CANDIDATE`. XF-058 shows that the normalized selector square function

\[
\mathfrak E_T
:=M\int |S_T(\theta)|^2\,d\theta
\]

survives the quadratic chirp that defeats every individual pointwise selector, and XF-059 extends the Xi source estimate far below the memory frequency `1/q`. That still does not make the **unweighted** square function uniformly coercive for critical triple flux over the whole growing slow cone.

There is a much simpler obstruction than the XF-057 chirp. Let

\[
q\asymp\log^2T,
\qquad M=q^2,
\qquad
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\qquad W=M\sigma_T,
\tag{1}
\]

and choose any scale

\[
1\ll L_T\ll\log\log T.
\tag{2}
\]

Put

\[
\vartheta_T:=\frac{L_T}{q},
\qquad
\varepsilon_T:=\frac{\kappa}{M^2\vartheta_T^2}
=\frac{\kappa}{q^2L_T^2},
\tag{3}
\]

\[
A_T:=\frac{\varepsilon_T}{2\sin(\vartheta_T/2)}
=\frac{\kappa}{qL_T^3}(1+o(1)),
\tag{4}
\]

and define the ordered matched control

\[
\boxed{
 z_j
 =T+\sigma_T\bigl(j+A_T\sin(\vartheta_Tj+\phi)\bigr).
}
\tag{5}
\]

Then the exact gaps are

\[
\frac{z_{j+1}-z_j}{\sigma_T}
=1+\varepsilon_T
\cos\!\left(\vartheta_T(j+\tfrac12)+\phi\right).
\tag{6}
\]

The control is source-compatible in the same finite-window sense as XF-047/XF-059 because `A_T=o(1)`, but its exact XF-030 triple-flux variation remains critical:

\[
\boxed{
M V_M\longrightarrow\frac{6\kappa}{\pi}>0.
}
\tag{7}
\]

Nevertheless, for the exact XF-056 selector family over any XF-059 cone containing `\vartheta_T`, the unweighted normalized energy satisfies

\[
\boxed{
M\int
|S_T^{\rm wave}(\theta)|^2\,d\theta
=
\frac{C_g\kappa^2}{L_T^4}(1+o(1))
\longrightarrow0,
}
\tag{8}
\]

where

\[
C_g:=\frac14\int_{\mathbb R}|\widehat g(u)|^2\,du>0
\tag{9}
\]

for the nonzero XF-056 envelope `g`. Thus the implication proposed after XF-058,

\[
\mathfrak E_T=o(1)
\quad\Longrightarrow\quad
M V_M=o(1),
\tag{10}
\]

is false for source-compatible matched finite-gap geometry. The failure is a **scale-calibration failure**: an unweighted selector coefficient measures the displacement amplitude, while the triple flux contains two additional discrete derivatives.

The same calculation identifies a natural repair candidate. Define the second-difference-weighted square function

\[
\boxed{
\mathfrak E_T^{(2)}(t)
:=
M\int_{\Theta_{T,\delta}}
(M\theta^2)^2
|\mathcal S_{T,\theta}(t)|^2\,d\theta,
}
\tag{11}
\]

where `\Theta_{T,\delta}` is the infrared-extended cone from XF-059. The actual Xi carrier still obeys

\[
\boxed{
\sup_{0\le t\le t_0}
\mathfrak E_T^{(2),\Xi}(t)=o(1),
}
\tag{12}
\]

because the extra weight is only `O((\log\log T)^4)` on the whole cone, whereas XF-059 gives arbitrarily rapid fixed logarithmic decay for every selector coefficient. On the matched control (5), however,

\[
\boxed{
M\int_{\Theta_{T,\delta}}
(M\theta^2)^2
|S_T^{\rm wave}(\theta)|^2\,d\theta
\longrightarrow C_g\kappa^2>0.
}
\tag{13}
\]

The weight also leaves the XF-058 chirp at order one, because that chirp's Fourier energy is concentrated at `\theta\asymp1/q`, where `M\theta^2\asymp1`. Hence the unweighted square function is now ruled out as a family-uniform inverse norm, while the derivative-weighted square function survives both canonical aggregate stress tests. No arbitrary-gap lower-frame theorem is proved.

## 1. Critical flux forces the high-slow amplitude down by `L_T^{-2}`

The relative gap wave (6) has frequency

\[
\vartheta_T=\frac{L_T}{q}=o(1),
\qquad
M\vartheta_T=qL_T\to\infty.
\tag{14}
\]

XF-059 derives for a small sinusoidal gap perturbation the exact critical combination

\[
M^2\varepsilon_T\vartheta_T^2.
\tag{15}
\]

With (3), this is exactly `\kappa`. Moreover

\[
\frac{\varepsilon_T}{\vartheta_T}
=\frac{\kappa}{qL_T^3}=o(1),
\tag{16}
\]

so the nonlinear error in the XF-030 flux expansion is negligible. Repeating the XF-059 calculation gives

\[
\phi_{j+1}-\phi_j
=
6\varepsilon_T\sin^2(\vartheta_T/2)
\cos(\vartheta_T(j+\tfrac32)+\phi)
+O(\varepsilon_T^2\vartheta_T),
\tag{17}
\]

and, since the `2M`-site window contains `\asymp qL_T` oscillations,

\[
\sum_{j=-M}^{M-3}
\left|
\cos(\vartheta_T(j+\tfrac32)+\phi)
\right|
=\frac{4M}{\pi}+o(M).
\tag{18}
\]

Therefore

\[
M V_M
=
\frac{24}{\pi}
M^2\varepsilon_T\sin^2(\vartheta_T/2)+o(1)
\longrightarrow\frac{6\kappa}{\pi},
\tag{19}
\]

which proves (7).

The root displacement amplitude is (4), so every translated span satisfies

\[
\left|
(z_b-z_a)-\sigma_T(b-a)
\right|
\le2\sigma_TA_T=o(\sigma_T).
\tag{20}
\]

Thus increasing the effective harmonic number `L_T` does not make the critical control less source-compatible. It makes the required gap amplitude **smaller** by `L_T^{-2}`.

This is the calibration distinction hidden by the XF-056 matched family. XF-056 fixes the relative gap amplitude at `\kappa/q^2`, which is critical at `\theta\asymp1/q`; at `\theta=L_T/q` that same amplitude carries `M V_M\asymp L_T^2`, not order-one critical flux. Renormalizing the amplitude to keep `M V_M\asymp1` produces (3).

## 2. The selector response is one `1/M` sideband with amplitude `L_T^{-2}`

Let `\theta` now denote the **probe center** and keep `\vartheta_T` for the control frequency. Define

\[
S_T^{\rm wave}(\theta)
:=\sum_{j\in\mathbb Z}f_{T,\theta}(z_j),
\tag{21}
\]

with the exact XF-056 probe. The arbitrary probe phase is a unit factor and disappears from every absolute-value estimate below.

Write

\[
F_\theta(y)
:=g(y/M)e^{-i\theta y}.
\tag{22}
\]

Then, apart from the harmless global physical phase,

\[
S_T^{\rm wave}(\theta)
=
\sum_j
F_\theta\!\left(j+A_T\sin(\vartheta_Tj+\phi)\right).
\tag{23}
\]

On the XF-059 cone the zeroth-order lattice sum vanishes exactly by the compact Fourier support of `\widehat g`. Taylor expansion gives

\[
S_T^{\rm wave}(\theta)
=L_T^{\rm lin}(\theta)+R_T(\theta),
\tag{24}
\]

where

\[
L_T^{\rm lin}(\theta)
=A_T\sum_j
\sin(\vartheta_Tj+\phi)
\left[
\frac1M g'(j/M)-i\theta g(j/M)
\right]e^{-i\theta j}.
\tag{25}
\]

Put `\chi=\widehat g`. Poisson summation and `\operatorname{supp}\chi\subset(-1,1)` imply, uniformly on the positive slow cone and for large `T`,

\[
\boxed{
L_T^{\rm lin}(\theta)
=-\frac{A_TM\vartheta_T}{2}
 e^{i\phi}
\chi\!\left(M(\theta-\vartheta_T)\right).
}
\tag{26}
\]

The opposite sideband is centered at `-\vartheta_T` and therefore misses the positive cone. Equation (26) can also be checked directly: the derivative-envelope term and the carrier derivative combine so that the coefficient is the **control frequency** `\vartheta_T`, not the moving probe center.

At the matched center,

\[
\frac{A_TM\vartheta_T}{2}
=
\frac{\varepsilon_TM}{2}
\frac{\vartheta_T}{2\sin(\vartheta_T/2)}
=
\frac{\kappa}{2L_T^2}(1+o(1)),
\tag{27}
\]

recovering the general XF-059 matched-response formula. Thus even a coherent pure critical mode has a pointwise coefficient tending to zero once its effective harmonic number tends to infinity.

The exact nonlinear remainder is harmless here. From

\[
F_\theta''(y)
=e^{-i\theta y}
\left[
\frac1{M^2}g''(y/M)
-\frac{2i\theta}{M}g'(y/M)
-\theta^2g(y/M)
\right]
\tag{28}
\]

and Schwartz summability,

\[
|R_T(\theta)|
\ll_g
A_T^2M(\theta+M^{-1})^2
\tag{29}
\]

uniformly throughout `\Theta_{T,\delta}`.

## 3. Unweighted `L^2` energy loses the critical mode

Because of (2), the sideband

\[
|\theta-\vartheta_T|<M^{-1}
\tag{30}
\]

lies strictly inside `\Theta_{T,\delta}` for every fixed `0<\delta<1` and all sufficiently large `T`. Changing variables

\[
u=M(\theta-\vartheta_T)
\tag{31}
\]

in (26) gives

\[
M\int_{\Theta_{T,\delta}}
|L_T^{\rm lin}(\theta)|^2d\theta
=
\frac{A_T^2M^2\vartheta_T^2}{4}
\int_{\mathbb R}|\chi(u)|^2du.
\tag{32}
\]

Using (3)--(4),

\[
A_TM\vartheta_T
=
\frac{\kappa}{L_T^2}(1+o(1)),
\tag{33}
\]

so the right side of (32) is exactly the main term in (8).

For the remainder, the upper edge of the XF-059 cone is `O((\log\log T)/q)`. Equations (2), (4), and (29) give

\[
M\int_{\Theta_{T,\delta}}|R_T(\theta)|^2d\theta
\ll_g
\frac{(\log\log T)^5}{q^3L_T^{12}}
=o(L_T^{-4}).
\tag{34}
\]

The cross term is `o(L_T^{-4})` by Cauchy--Schwarz. Therefore (8) holds for the **exact displaced-point statistic**, not only for the linearized sideband.

This is a stronger obstruction to the specific inverse implication (10) than frequency detuning. The mode lies inside the selector cone, is coherent rather than chirped, and its critical transition-side flux is nonzero. Its aggregate energy vanishes solely because the unweighted norm does not compensate for the two derivatives appearing in the flux observable.

## 4. A second-difference weight restores the matched scale

For a pure wave at frequency `\vartheta`, critical flux fixes

\[
M^2\varepsilon\vartheta^2\asymp1,
\tag{35}
\]

while the selector sideband amplitude is

\[
M\varepsilon.
\tag{36}
\]

Thus the exact missing conversion factor is `M\vartheta^2`. Squaring it produces the weight in (11).

On the support (30), write

\[
\theta=\vartheta_T+\frac uM,
\qquad |u|<1.
\tag{37}
\]

Then

\[
M\theta^2
=M\vartheta_T^2+2u\vartheta_T+O(M^{-1})
=L_T^2+o(1)
\tag{38}
\]

uniformly. Multiplying (32) by the squared weight therefore gives

\[
M\int_{\Theta_{T,\delta}}
(M\theta^2)^2
|L_T^{\rm lin}(\theta)|^2d\theta
\longrightarrow
C_g\kappa^2.
\tag{39}
\]

The weighted remainder still vanishes: compared with (34), the worst possible extra factor over the whole cone is only

\[
\sup_{\Theta_{T,\delta}}(M\theta^2)^2
=O((\log\log T)^4),
\tag{40}
\]

so its contribution is

\[
O_g\!\left(
\frac{(\log\log T)^9}{q^3L_T^{12}}
\right)=o(1),
\tag{41}
\]

and the weighted cross term is again `o(1)`. This proves (13).

The factor `(M\theta^2)^2` is not asserted to be unique or globally optimal. It is simply the exact Fourier multiplier dictated by comparing the selector's displacement-scale response with the two-discrete-derivative critical flux scaling.

## 5. The Xi source estimate easily pays the derivative weight

XF-059 proves for every fixed `B>0`

\[
\sup_{0\le t\le t_0}
\sup_{\theta\in\Theta_{T,\delta}}
|\mathcal S_{T,\theta}(t)|
=O_B((\log T)^{-B}).
\tag{42}
\]

The cone length satisfies

\[
M|\Theta_{T,\delta}|
=O(q\log\log T),
\tag{43}
\]

and (40) holds. Hence

\[
\mathfrak E_T^{(2),\Xi}(t)
\ll
q(\log\log T)^5
\sup_{\theta\in\Theta_{T,\delta}}
|\mathcal S_{T,\theta}(t)|^2.
\tag{44}
\]

Taking `B` sufficiently large gives (12), uniformly for `0\le t\le t_0`. No new explicit-formula, high-line, or heat-transport estimate is needed; the source side had enough quantitative margin already.

The XF-058 chirp is also preserved. Its positive Fourier energy is concentrated on frequencies

\[
\theta\asymp\frac1q
\tag{45}
\]

inside a fixed core chosen there. On that core

\[
0<c_1\le M\theta^2\le c_2<\infty,
\tag{46}
\]

for fixed positive constants after the XF-058 choice of `a_0,b,g`. Therefore the order-one lower and upper bounds for the chirp's unweighted normalized energy remain order one after applying the weight in (11).

The derivative-weighted norm consequently passes three source-side/matched checks simultaneously: it remains `o(1)` for the actual Xi carrier, retains the XF-058 critical chirp, and restores order-one calibration for the high-slow critical family (5).

## 6. Stress tests and evidence boundary

The finding does **not** contradict XF-056. That finding correctly obtains an order-one matched response throughout its cone for a wave whose relative gap amplitude is fixed at `\kappa/q^2`. The new observation is that this fixed amplitude is no longer the borderline `M V_M\asymp1` amplitude when the effective harmonic number `L_T=q\vartheta_T` grows. At critical flux the amplitude must be divided by `L_T^2`, and the unweighted selector response is divided by the same factor.

It also does not contradict XF-058. The XF-057 chirp lives at frequencies `\asymp1/q`, exactly where the unweighted normalization is scale matched. XF-060 supplies the stronger matched configuration explicitly requested in XF-058's final gate: nonvanishing critical flux with vanishing normalized square energy.

Nor does this negate XF-059's infrared result. Below `1/q`, the critical pure-mode response grows because `M\vartheta^2\to0`; above `1/q`, it shrinks because `M\vartheta^2\to\infty`. The memory frequency

\[
\vartheta\asymp M^{-1/2}=q^{-1}
\tag{47}
\]

is precisely the unique scale at which the **unweighted** selector energy is automatically calibrated to critical two-derivative flux.

No theorem here controls an arbitrary nonlinear transition block by `\mathfrak E_T^{(2)}`. Spatial concentration, packet multiplicity, cancellation between bands, nonlinear frequency transfer, and the `L^1` nature of `V_M` may still defeat a weighted `L^2` frame. The new norm is a better candidate, not a completed source-to-transition bridge. No upper bound on the de Bruijn--Newman constant follows.

## 7. Prior-art and novelty boundary

Frequency-weighted square functions and the principle that multiplication by a power of frequency represents derivatives are classical Littlewood--Paley/Sobolev ideas. No novelty is claimed for that general harmonic-analysis mechanism, Poisson summation, Plancherel, or Taylor expansion of a jittered lattice.

A targeted literature audit of de Bruijn--Newman heat flow, Riemann-Xi Fourier formulations, Littlewood--Paley/Sobolev square functions, and weighted square-function estimates did not locate this scale-matched zero-selector/triple-flux calculation. The durable line-specific delta is the exact conjunction

\[
M=q^2,
\qquad
\vartheta_T=\frac{L_T}{q},
\qquad
\varepsilon_T=\frac{\kappa}{M^2\vartheta_T^2},
\qquad
M V_M\to\frac{6\kappa}{\pi},
\tag{48}
\]

with the Xi source selector asymptotics (8), (12), and (13). No external theorem beyond the classical tools already used in XF-056--XF-059 is load-bearing, so `SOURCES.md` does not require modification.

## 8. Consequence for `xi_flow`

The next source-to-transition theorem should **not** attempt a family-uniform lower frame using the raw XF-058 norm `M d\theta`. XF-060 gives an explicit source-compatible critical family for which that norm tends to zero.

The natural next candidate is the derivative-matched phase-space norm (11), or an equivalent norm that charges a selector coefficient according to the two-discrete-derivative cost of the transition flux. The decisive next test is no longer another pure wave: either prove a weighted frame/BV estimate strong enough to force `M V_M=o(1)` for arbitrary source-compatible transition geometry, or construct a packetized/sparse matched control with `M V_M\asymp1` that also defeats the weighted aggregate. The latter would show that frequency calibration alone is insufficient and that spatial phase-space aggregation or genuinely Xi-specific dynamics is required.