# XF-061 — single-root defect evades the derivative-weighted slow selector

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `NEGATIVE/OBSTRUCTION` + `SPARSE-FREQUENCY-ESCAPE`. XF-060 repairs the scale-calibration failure of the unweighted selector square function by weighting each slow frequency with the two-discrete-derivative multiplier `(M theta^2)^2`. That weighted norm survives the critical pure-wave and chirped controls tested there. It is nevertheless not coercive for arbitrary source-compatible finite-gap geometry: a single displaced root carries order-one normalized triple-flux variation while its entire derivative-weighted slow-selector energy tends to zero.

Keep the XF-059/XF-060 scales

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\tag{1}
\]

and, for fixed `0<delta<1` and `C>0`, the slow cone

\[
\Theta_{T,\delta}
=
\left[q^{-2+\delta},\frac{C\log\log T}{q}\right].
\tag{2}
\]

Let `kappa>0` be fixed and put

\[
\varepsilon_T:=\frac{\kappa}{M}.
\tag{3}
\]

Starting from the local source lattice `z_j^0=T+j\sigma_T`, move only one root:

\[
\boxed{
 z_1=T+\sigma_T(1+\varepsilon_T),
 \qquad
 z_j=T+j\sigma_T\quad(j\ne1).
}
\tag{4}
\]

Then every translated span differs from the source lattice by at most `\varepsilon_T\sigma_T=o(\sigma_T)`, yet for the exact XF-030 triple-flux variation over any `2M`-scale window containing the defect,

\[
\boxed{
M V_M\longrightarrow12\kappa>0.
}
\tag{5}
\]

On the other hand, if `S_T^{\rm def}(\theta)` is the exact XF-056/XF-059 compact selector evaluated on (4), then the XF-060 weighted energy satisfies

\[
\boxed{
M\int_{\Theta_{T,\delta}}
(M\theta^2)^2
|S_T^{\rm def}(\theta)|^2\,d\theta
\longrightarrow0.
}
\tag{6}
\]

Thus the candidate implication

\[
\mathfrak E_T^{(2)}=o(1)
\quad\Longrightarrow\quad
M V_M=o(1)
\tag{7}
\]

is false even on an ordered finite-gap control that is closer to the local Xi source lattice than the matched families used in XF-047, XF-057, or XF-060. The obstruction is no longer frequency calibration. It is **spectral support**: a compact root defect stores its critical `L^1` flux variation predominantly outside the shrinking slow cone, and the extra two-derivative weight suppresses rather than recovers its low-frequency tail.

## 1. One displaced root is source-compatible by a wide margin

The gaps of (4) are exactly

\[
 g_0=\sigma_T(1+\varepsilon_T),
 \qquad
 g_1=\sigma_T(1-\varepsilon_T),
 \qquad
 g_j=\sigma_T\quad(j\ne0,1).
\tag{8}
\]

For large `T`, `\varepsilon_T<1`, so the configuration is ordered and real-simple. Since only `z_1` differs from the reference lattice, every translated finite span satisfies

\[
\boxed{
\left|
(z_b-z_a)-\sigma_T(b-a)
\right|
\le \varepsilon_T\sigma_T.
}
\tag{9}
\]

At the present scaling,

\[
\varepsilon_T\sigma_T
\asymp\frac1{M\log T}
\asymp\frac1{\log^5T}.
\tag{10}
\]

This is much smaller than the local span errors admitted in XF-047/XF-059. The `2M`-gap physical window still has width `\asymp M\sigma_T\asymp\log^3T=o(T)`, so the same Taylor comparison with the smooth Riemann--von Mangoldt main term applies. The control is therefore source-compatible in exactly the finite-window matched sense used by those findings.

No global Xi realization is asserted. Equation (4) is deliberately the smallest local perturbation capable of testing whether the XF-060 norm itself can control arbitrary transition geometry.

## 2. The exact triple flux sees a critical defect

For a triple beginning at gap index `j`, write

\[
r_j:=\frac{g_{j+1}}{g_j},
\qquad
\phi_j:=\phi(r_j),
\tag{11}
\]

where XF-030 gives the exact rational flux

\[
\phi(r)
=-\frac{(r-1)(r+2)(2r+1)}
{(r+1)(r^2+r+1)}.
\tag{12}
\]

All `\phi_j` vanish except at the three triples touching the defect. Their ratios are

\[
r_{-1}=1+\varepsilon_T,
\qquad
r_0=\frac{1-\varepsilon_T}{1+\varepsilon_T},
\qquad
r_1=\frac1{1-\varepsilon_T}.
\tag{13}
\]

For positive sufficiently small `\varepsilon_T`, equation (12) gives

\[
\phi_{-1}<0,
\qquad
\phi_0>0,
\qquad
\phi_1<0.
\tag{14}
\]

Hence the total variation of the compact flux profile, including the two jumps to and from zero, is exactly

\[
V_M
=2\bigl(\phi_0-\phi_{-1}-\phi_1\bigr)
\tag{15}
\]

whenever the defining XF-035/XF-057 window contains these four jumps. Expanding the exact rational functions at `\varepsilon=0` gives

\[
\begin{aligned}
\phi(1+\varepsilon)
&=-\frac32\varepsilon
 +\frac34\varepsilon^2
 -\frac5{24}\varepsilon^3
 +O(\varepsilon^4),\\
\phi\!\left(\frac{1-\varepsilon}{1+\varepsilon}\right)
&=3\varepsilon
 -\frac43\varepsilon^3
 +O(\varepsilon^5),\\
\phi\!\left(\frac1{1-\varepsilon}\right)
&=-\frac32\varepsilon
 -\frac34\varepsilon^2
 -\frac5{24}\varepsilon^3
 +O(\varepsilon^4).
\end{aligned}
\tag{16}
\]

Therefore

\[
\boxed{
V_M
=12\varepsilon_T
-\frac{11}{6}\varepsilon_T^3
+O(\varepsilon_T^5),
}
\tag{17}
\]

and substituting `\varepsilon_T=\kappa/M` proves (5). The critical transition-side quantity is thus nonvanishing even though the perturbation occupies only two adjacent gaps and tends uniformly to the arithmetic lattice.

This is not a linearized-flux artifact: (15) uses the exact XF-030 rational flux and (17) is merely its asymptotic evaluation at the explicitly shrinking defect amplitude.

## 3. The exact slow selector reduces to one finite difference

Use the exact XF-056/XF-059 probe. After removing its irrelevant global unit phase and writing the index-coordinate profile as

\[
F_\theta(y)
:=g(y/M)e^{-i\theta y},
\tag{18}
\]

the reference lattice contribution vanishes exactly on `\Theta_{T,\delta}` for all sufficiently large `T`. Indeed `\widehat g` is compactly supported in `(-1,1)` and

\[
M\theta\ge q^\delta\longrightarrow\infty,
\tag{19}
\]

so the same Poisson-support cancellation used in XF-059 applies throughout the cone.

Because (4) changes only the point with index `1`, the complete selector is therefore not an infinite perturbative sum but the exact finite difference

\[
\boxed{
S_T^{\rm def}(\theta)
=F_\theta(1+\varepsilon_T)-F_\theta(1).
}
\tag{20}
\]

Since

\[
F_\theta'(y)
=e^{-i\theta y}
\left[
\frac1M g'(y/M)-i\theta g(y/M)
\right],
\tag{21}
\]

the fundamental theorem of calculus gives, uniformly on the whole cone,

\[
\boxed{
|S_T^{\rm def}(\theta)|
\le C_g\varepsilon_T
\left(\theta+\frac1M\right).
}
\tag{22}
\]

At the lower edge of (2), `M\theta\to\infty`, so eventually `M^{-1}\le\theta`. Consequently

\[
|S_T^{\rm def}(\theta)|
\le 2C_g\varepsilon_T\theta.
\tag{23}
\]

The additional factor `theta` has a transparent origin. In gap coordinates the defect is the discrete dipole

\[
h_j
=\varepsilon_T(\delta_{j0}-\delta_{j1}),
\tag{24}
\]

whose Fourier transform contains the factor `1-e^{-i\theta}=O(\theta)` near frequency zero. A root displacement localized at one site therefore has vanishing slow-frequency mass even though its adjacent-gap variation is critical.

## 4. The derivative-weighted slow energy still vanishes

Insert (23) into the exact candidate norm from XF-060. If

\[
\theta_+:=\frac{C\log\log T}{q},
\tag{25}
\]

then

\[
\begin{aligned}
M\int_{\Theta_{T,\delta}}
(M\theta^2)^2
|S_T^{\rm def}(\theta)|^2d\theta
&\ll_g
\varepsilon_T^2M^3
\int_0^{\theta_+}\theta^6d\theta\\
&\ll_g
\varepsilon_T^2M^3\theta_+^7.
\end{aligned}
\tag{26}
\]

Using `\varepsilon_T=\kappa/M` and `M=q^2`,

\[
\boxed{
\varepsilon_T^2M^3\theta_+^7
\ll
\kappa^2
\frac{(\log\log T)^7}{q^5}
\longrightarrow0.
}
\tag{27}
\]

This proves (6). Replacing the small-frequency surrogate `M\theta^2` by the exact discrete second-difference multiplier `4M\sin^2(\theta/2)` does not change the conclusion, because the entire cone shrinks to zero and the two multipliers are uniformly comparable there.

The failure is therefore not the particular polynomial approximation in XF-060. The slow cone itself does not contain enough spectral mass to recover the compact defect's `L^1` triple-flux variation from this quadratic selector energy.

## 5. Slow-frequency spatial tiling alone does not repair the defect

A natural reaction is to add physical localization and sum the same slow-frequency energy over translated envelopes. For this matched control that is still insufficient if the frequency cone is left unchanged.

Let `F_{a,\theta}` be any translate of the same `M`-scale envelope with uniformly bounded `g` and `g'`. The exact reference-lattice cancellation remains the same, and moving one root again changes the selector by one finite difference. Uniformly in the translate,

\[
|S_{a,T}^{\rm def}(\theta)|
\le C_g\varepsilon_T(\theta+M^{-1}).
\tag{28}
\]

Therefore the sum of the weighted energies over any `K_T=O(M)` such translates obeys

\[
\sum_{a=1}^{K_T}
M\int_{\Theta_{T,\delta}}
(M\theta^2)^2
|S_{a,T}^{\rm def}(\theta)|^2d\theta
\ll_g
\varepsilon_T^2M^4\theta_+^7.
\tag{29}
\]

At the present scales this is

\[
\boxed{
O\!\left(
\kappa^2\frac{(\log\log T)^7}{q^3}
\right)=o(1).
}
\tag{30}
\]

Thus a bounded-density phase-space tiling of the **same shrinking slow-frequency family** does not by itself close the sparse-defect escape. Spatial aggregation helps only if it is accompanied by frequency coverage or a dynamical estimate that transfers local variation into the observed band.

Equation (30) is a matched-control statement about the selector geometry. It does not assert a new uniform Xi estimate for moving physical centers; none is needed for the negative conclusion.

## 6. Stress tests and evidence boundary

This finding does not undo the positive matched checks in XF-060. The pure wave and the XF-058 chirp distribute their critical variation over slow frequencies, so the derivative weight correctly calibrates them. The new defect has a different geometry: it is compact in index space and therefore broadband, with only a vanishing dipole tail inside the slow cone. The three controls test different failure modes.

Nor does (4) establish a persistent positive-`Lambda` scenario. A compact defect contains high index frequencies, precisely the modes on which the Cauchy/logarithmic-particle dynamics can smooth rapidly. No claim is made that (5) survives a fixed positive heat-time interval, and no zero-motion equation is used outside its real-simple regime. The result rules out a **static arbitrary-block lower-frame theorem** based only on the XF-060 slow selector norm; it does not rule out a theorem that combines the endpoint selector with heat-time regularization.

The source compatibility is likewise intentionally local. The control is not asserted to be the Xi zero set, and its role is falsificatory: the source-counting information actually consumed by the present finite-window argument cannot by itself prohibit one `O(M^{-1})` root displacement.

A decisive falsification of the obstruction would require an additional admitted hypothesis that genuinely excludes such sparse high-frequency transition geometry. Merely changing the normalization of the existing slow square function cannot do so, because (20)--(27) expose the missing spectral mass directly.

## 7. Prior-art and novelty boundary

Discrete finite differences, the Fourier factor `1-e^{-i\theta}`, frequency-weighted square functions, and the general duality between localization and broadband Fourier support are classical harmonic-analysis facts. No novelty is claimed for those principles.

A targeted audit of de Bruijn--Newman heat-flow work, Xi explicit-formula test functions, Littlewood--Paley/Sobolev square functions, and discrete/BV Fourier estimates did not locate the line-specific conjunction used here: the exact XF-030 triple-flux response of a single source-compatible root displacement together with the XF-059 moving-line slow selector and the XF-060 two-derivative weighting. No external theorem beyond classical tools already anchored for the line is load-bearing, so `SOURCES.md` requires no change.

## 8. Consequence for `xi_flow`

XF-060's derivative weight fixes **scale mismatch**, but XF-061 shows that it cannot by itself fix **spectral-support mismatch**. A source-to-transition theorem cannot quantify over arbitrary source-compatible finite-gap blocks and infer `M V_M=o(1)` from the weighted slow selector alone.

The live alternatives are now sharper. One can enlarge the observable to frequencies that genuinely charge sparse/local variation, subject to the explicit-formula prime-support constraints; or exploit the heat dynamics to prove that any transition-side defect surviving the relevant positive time must have transferred enough mass into the controlled slow sector. A norm that stays confined to `theta=o(1)` without such a dynamical regularization cannot see the single-root counterexample at critical `M V_M` scale.