# WI-309 — Endpoint-singular localizers give a uniform clipped-tail gap

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-307, WI-308, WI-247, WI-248.

WI-308 reduces every fixed-aperture RH-failure crossing to a discrete negative eigenvalue of the clipped comparison, but its tail reserve

\[
c_{\chi,B}=\inf_\xi r_{\chi,B}(\xi)>0
\]

was only qualitative for a fixed smooth localizer. The stated next gate was to make this reserve effective without reintroducing the exterior-frequency scale obstruction of WI-248.

There is an exact way to close **that half** of the gate. One should not keep the sliding localizer fixed as the exterior reserve `B` grows. For each finite `B`, choose a compactly supported `L^2` localizer with an integrable endpoint singularity whose Fourier tail is just barely square-integrable. Its exponent can be tuned to the exponentially distant clipped-source tail. This yields a positive lower bound for `c_{chi,B}` that is independent of `B`, and hence independent of the outer aperture once `B` is chosen from the active prime mass.

Concretely, for every finite outer half-width `L>0` there is an explicit normalized real localizer `chi_L`, supported in `[-1/2,1/2]`, and an explicit reserve `B_L` such that the exact WI-308 decomposition extends to the closed logarithmic form domain and satisfies

\[
\boxed{
Q=\mathcal D_{L,\chi_L,B_L}+\mathcal T_{\chi_L,B_L},
\qquad
\sigma_{\rm ess}(\mathcal D_{L,\chi_L,B_L})\subseteq[1,\infty),
\qquad
\mathcal T_{\chi_L,B_L}\succeq c_0 I,
}
\tag{1}
\]

with the aperture-independent constant

\[
\boxed{c_0=\frac1{64\pi e}>0.00182968.}
\tag{2}
\]

Consequently, if RH is false, the finite odd zero mode supplied by WI-247 forces, at its finite aperture,

\[
\boxed{
\lambda_{\min}(\mathcal D_{L,\chi_L,B_L})\le -c_0.
}
\tag{3}
\]

Thus the clipped-tail witness need not collapse toward zero as the aperture grows. The remaining obstruction is different and sharper: the compact correction in `D` degenerates as the singularity exponent approaches the `L^2` endpoint, so no uniform control of the finite negative spectrum follows from (1). This is **not** a proof of RH.

## 1. An aperture-adaptive endpoint-singular localizer

Retain the exact unit-window symbol of WI-307--WI-308,

\[
\sigma_1(t)
=A(t)-\sum_{n\in\{2,3,4,5,7\}}c_n\cos(t\log n),
\qquad
c_n=\frac{2\Lambda(n)}{\sqrt n},
\]

and put

\[
C_1:=\sum_{n\in\{2,3,4,5,7\}}c_n.
\]

WI-307 audited the large-frequency lower envelope

\[
\sigma_1(t)
\ge
\log\frac{|t|}{2\pi}-\frac1{|t|}-C_1
\qquad(|t|\ge15/4).
\tag{4}
\]

For a finite reserve `B>=0`, define

\[
T_B:=\max\left\{1000,\,2\pi e^{B+C_1+1}\right\},
\qquad
\eta_B:=\frac1{\log(2T_B)},
\]

and

\[
\alpha_B:=\frac{1-\eta_B}{2},
\qquad
\beta_B:=1-\alpha_B=\frac{1+\eta_B}{2}.
\]

On `(-1/2,1/2)` set, almost everywhere,

\[
\boxed{
\chi_B(u)
:=
\sqrt{\eta_B}\,(1/2-u)^{-\alpha_B},
}
\tag{5}
\]

and set it equal to zero outside that interval. Since `2 alpha_B=1-eta_B`,

\[
\|\chi_B\|_2^2
=
\eta_B\int_0^1 y^{-1+\eta_B}\,dy
=1.
\tag{6}
\]

The localizer is real, nonnegative, compactly supported strictly inside the unit localization window, and belongs to `L^1 cap L^2`. It is deliberately not smooth: as `B` grows, `eta_B` decreases and the endpoint singularity approaches the limiting non-`L^2` profile `y^{-1/2}`.

## 2. Its Fourier tail keeps a fixed amount of mass beyond the clipped-source radius

For `s>0`, the Fourier transform of (5) is

\[
F_{\chi_B}(s)
=
\sqrt{\eta_B}\,e^{-is/2}
\int_0^1 y^{\beta_B-1}e^{isy}\,dy
=
\sqrt{\eta_B}\,e^{-is/2}s^{-\beta_B}
\int_0^s z^{\beta_B-1}e^{iz}\,dz.
\tag{7}
\]

For `0<beta<1`, the classical oscillatory Euler integral gives

\[
\int_0^\infty z^{\beta-1}e^{iz}\,dz
=
\Gamma(\beta)e^{i\pi\beta/2}.
\]

A single integration by parts on the tail gives the elementary error estimate

\[
\left|
\int_s^\infty z^{\beta-1}e^{iz}\,dz
\right|
\le 2s^{\beta-1}.
\tag{8}
\]

Hence, if

\[
S_\eta:=
\left(\frac4{\Gamma(\beta)}\right)^{1/\alpha},
\]

then for `s>=S_eta`,

\[
|F_{\chi_B}(s)|^2
\ge
\frac{\eta_B\Gamma(\beta_B)^2}{4}
 s^{-1-\eta_B}.
\tag{9}
\]

The threshold is harmless uniformly in `B`. Since `T_B>=1000`, one has `eta_B<1/7`, hence `alpha_B>3/7`. Also

\[
\Gamma(\beta_B)
\ge
\int_0^1 e^{-x}x^{\beta_B-1}\,dx
\ge 1-e^{-1}>\frac12.
\]

Therefore

\[
S_{\eta_B}<8^{7/3}=128<2T_B.
\tag{10}
\]

Integrating (9) from `R` to infinity cancels the small normalization factor `eta_B`:

\[
\boxed{
\int_R^\infty|F_{\chi_B}(s)|^2\,ds
\ge
\frac{\Gamma(\beta_B)^2}{4}R^{-\eta_B}
\qquad(R\ge S_{\eta_B}).
}
\tag{11}
\]

This cancellation is the mechanism. The localizer becomes more singular as the clipped tail moves outward, so its Fourier mass at that moving scale does not vanish.

The same calculation also gives the upper bound `|F_chi(s)|=O(s^{-beta_B})`. Since `2 beta_B=1+eta_B`,

\[
\int_\mathbb R
\log(2+|s|)|F_{\chi_B}(s)|^2\,ds<\infty.
\tag{12}
\]

Thus each `chi_B` lies in the logarithmic form domain used by the localized Weil operator, despite not being smooth.

## 3. The clipped tail has a uniform scalar floor

Use the exact WI-308 clipping

\[
q_B(t):=(\sigma_1(t)-B)_+,
\qquad
m_B(t):=\min\{\sigma_1(t),B\}.
\]

By (4) and the definition of `T_B`, for `|t|>=T_B`,

\[
\sigma_1(t)
\ge B+1-\frac1{|t|}
>B+\frac12,
\]

so

\[
q_B(t)\ge\frac12.
\tag{13}
\]

For a real localizer, `|F_chi|^2` is even. For every frequency shift `xi`, the exterior set `|t|>=T_B` captures at least one unshifted Fourier tail beyond `2T_B`:

\[
\int_{|t|\ge T_B}
|F_{\chi_B}(t-\xi)|^2\,dt
\ge
\int_{2T_B}^\infty|F_{\chi_B}(s)|^2\,ds.
\tag{14}
\]

Indeed, if `|xi|<=T_B`, one of the two exterior half-lines contains the corresponding tail beyond `2T_B`; if `|xi|>T_B`, an exterior half-line contains an entire positive or negative half-line, which is stronger.

The WI-308 tail multiplier is

\[
r_{\chi_B,B}(\xi)
=
\frac1{2\pi}
\int_\mathbb R
q_B(t)|F_{\chi_B}(t-\xi)|^2\,dt.
\]

Combining (11), (13), and (14) gives

\[
r_{\chi_B,B}(\xi)
\ge
\frac{\Gamma(\beta_B)^2}{16\pi}
(2T_B)^{-\eta_B}.
\]

But the exponent was chosen so that

\[
(2T_B)^{-\eta_B}=e^{-1}.
\]

Since `Gamma(beta_B)>1/2`, uniformly in `xi` and `B`,

\[
\boxed{
r_{\chi_B,B}(\xi)
>\frac1{64\pi e}
=:c_0.
}
\tag{15}
\]

Plancherel therefore yields the source-exact quadratic-form bound

\[
\boxed{
\mathcal T_{\chi_B,B}(f)
\ge c_0\|f\|_2^2.
}
\tag{16}
\]

Unlike the qualitative `c_{chi,B}>0` in WI-308, the right-hand side no longer deteriorates as the clipping level grows.

## 4. The nonsmooth localizer still gives the same Fredholm structure

The only point requiring care is that WI-307--WI-308 stated the sliding identity for smooth compactly supported localizers. The profile (5) remains legal after passing to the closed form, and the compactness conclusion survives with a weaker Schatten statement.

First, for `0<a<1`, its autocorrelation is

\[
\rho_B(a)
=
\eta_B\int_a^1
 y^{-\alpha_B}(y-a)^{-\alpha_B}\,dy.
\tag{17}
\]

Because `y-a<=y`,

\[
\rho_B(a)
\ge
\eta_B\int_a^1 y^{-2\alpha_B}\,dy
=1-a^{\eta_B}.
\tag{18}
\]

Cauchy--Schwarz gives `rho_B(a)<=1`, while nonnegativity of `chi_B` gives `rho_B(a)>=0`. Thus

\[
\boxed{
0\le1-\rho_B(a)\le a^{\eta_B}
\qquad(0<a<1).
}
\tag{19}
\]

For `a>=1`, the two supports are disjoint and `rho_B(a)=0`.

The continuous localization-defect kernel from WI-307 has only a first-order singularity at the origin. Multiplication by (19) therefore changes its local behavior from `O(a^{-1})` to

\[
O(a^{-1+\eta_B}),
\]

which lies in `L^1` for every finite `B`. Compression of convolution by an `L^1` difference kernel to a bounded interval is compact on `L^2`: approximate the kernel in `L^1` by `L^2` kernels, use Young's inequality for operator-norm convergence, and note that each `L^2` approximation gives a Hilbert--Schmidt compression. Smoothness of `chi` was a convenient sufficient condition in WI-307, not a necessary one.

The averaged compact unit-window part also remains compact. Its kernel is bounded on the unit square, and for the localized kernel Cauchy--Schwarz gives

\[
\int
|\chi_B(s-y)\chi_B(t-y)|\,dy\le1.
\]

On the bounded outer square the averaged kernel is therefore bounded and hence Hilbert--Schmidt. The pole term is handled in the same way. The discrete source part remains the finite compressed-translation sum

\[
A_{L,\chi_B}
=
\sum_{\log n<2L}
 c_n(1-\rho_B(\log n))J_{\log n}.
\tag{20}
\]

Finally, the localization identity itself extends from the smooth core without inserting a new hypothesis. For smooth outer `f`, the prime and continuous source terms can be integrated directly in `y`; the identity

\[
\int H_{f_y}(a)\,dy
=\rho_B(a)H_f(a)
\]

is Fubini-exact. The logarithmic Fourier moment (12) makes the archimedean source absolutely integrable on these products, and (19) makes the defect integral locally integrable. Equivalently, one may approximate `chi_B` by smooth cutoffs in the logarithmic form norm. Since the resulting `D` is bounded and the Weil form is closed, the exact split extends from the smooth outer core to the closed logarithmic form domain.

Hence WI-308's operator identity remains valid for (5):

\[
\boxed{
Q=\mathcal D_{L,\chi_B,B}+\mathcal T_{\chi_B,B},
\qquad
\mathcal D_{L,\chi_B,B}
=B I-A_{L,\chi_B}+K_{L,\chi_B,B},
}
\tag{21}
\]

with `K` compact and self-adjoint.

## 5. Choose the reserve without any circular dependence on the localizer

For the outer aperture `L`, let

\[
P_L
:=
\sum_{\log n<2L}c_n
\]

be the total active prime-power mass and choose

\[
\boxed{B_L:=P_L+1.}
\tag{22}
\]

Because (5) is nonnegative, `0<=rho_B<=1`. Thus every coefficient in (20) satisfies

\[
0\le c_n(1-\rho_B(\log n))\le c_n,
\]

and since `||J_a||<=1`,

\[
\|A_{L,\chi_{B_L}}\|
\le P_L=B_L-1.
\tag{23}
\]

Therefore

\[
B_LI-A_{L,\chi_{B_L}}\succeq I.
\]

Weyl invariance under compact self-adjoint perturbations and (21) give

\[
\boxed{
\sigma_{\rm ess}(\mathcal D_{L,\chi_{B_L},B_L})
\subseteq[1,\infty).
}
\tag{24}
\]

Equations (16), (21), and (24) are exactly (1). There is no fixed-point problem: `B_L` is chosen from the crude source mass `P_L`, then `chi_{B_L}` is defined from that value, and the positivity `rho>=0` guarantees that the true translation norm can only be smaller than the budget used to choose `B_L`.

## 6. RH failure now forces a fixed-depth discrete witness

WI-247 proves that if RH is false, there is a finite odd first-crossing aperture `L=a_*^-` and a normalized nonzero odd closed-form vector `v_*` with

\[
Q(v_*)=0.
\]

Apply (1) at that finite `L`. Then

\[
0
=\langle v_*,\mathcal D_Lv_*\rangle
 +\mathcal T_L(v_*)
\ge
\langle v_*,\mathcal D_Lv_*\rangle+c_0,
\]

so

\[
\langle v_*,\mathcal D_Lv_*\rangle\le-c_0.
\]

Together with (24), the min--max principle gives an actual isolated eigenvalue of finite multiplicity below `-c_0`, establishing (3). In fact any finite-aperture test with `Q(f)<=0` forces the same normalized `-c_0` witness; the odd first crossing is used only to connect the statement canonically to every RH failure.

This is stronger than merely saying that an RH failure creates a negative discrete mode. It says that after an admissible aperture-dependent change of localization coordinates, the mode must penetrate a **uniform fixed distance** into the negative spectrum.

## 7. What this does not solve: compactness becomes nonuniform at the endpoint

The construction does not contradict WI-248's scale barrier. The source tail still begins only beyond a radius at least

\[
2\pi e^{B_L+C_1+1},
\]

which is enormous when the active prime mass is large. The new localizer does not shrink that radius. It changes its Fourier decay so that a fixed amount of mass remains visible there.

The price is transferred into the compact correction. As `L` and hence typically `B_L` grow,

\[
\eta_{B_L}\to0,
\]

and the continuous localization-defect kernel approaches the nonintegrable boundary shape `a^{-1}`. For every finite aperture it is still `O(a^{-1+eta}) in L^1`, hence compact after compression, but the `L^1` norm and any naive approximation-number/Schatten constants can deteriorate like an inverse power of `eta`. The family of compact operators is therefore not uniformly compact in any sense established here.

Accordingly, (1)--(3) do **not** bound the number, location, or total negative mass of the discrete eigenvalues uniformly in `L`. A proof of RH would still need a source-specific estimate that excludes eigenvalues below `-c_0` despite this degenerating compact correction, or a different representation in which the compact sector has a uniform quantitative bound.

The bottleneck after WI-309 is thus more precise:

\[
\boxed{
\text{uniform tail coercivity is available; the live problem is uniform control of the discrete compact sector.}
}
\]

## 8. Prior-art and novelty audit

The ingredients are individually classical or already line-local. The exact clipped split and multiplier `r_{chi,B}` are WI-308; the arbitrary exterior reserve and Fredholm decomposition are WI-307; the finite odd RH-failure zero mode is WI-247. Moyal/Plancherel localization for `L^2` windows is standard time-frequency analysis, and the endpoint Fourier estimate above is proved directly from the classical oscillatory Gamma integral and one integration by parts. Compactness of bounded-interval convolution with an `L^1` kernel follows from `L^1` approximation by Hilbert--Schmidt kernels.

A fresh targeted audit checked the recent fixed-window Weil-positivity literature rather than inferring novelty from line-local absence. Vincent Liu's submitted 15 September 2026 manuscript retains a positive Fourier tail and proves fixed-window coercivity at half-widths `1` and `17/16`, but its architecture uses fixed-window finite-band/tail compensation and does not state an aperture-adaptive endpoint-singular sliding localizer or a uniform-in-clipping tail floor. Rainer Andreas Mittermeier's 10 September 2026 compact-event-cell preprint studies parity kernels, exact cell enclosures, Gershgorin/Schur certificates, and explicitly remains fixed-support. Targeted searches for `Weil positivity` together with `singular window`, `endpoint singular`, `Moyal`, and sliding-localizer terminology found no prior statement of (1)--(3).

Search absence is not a priority claim. The durable Mathia contribution is the exact combination of already legal source pieces: tune an integrable endpoint singularity to the clipped-source radius, retain enough autocorrelation regularity for compactness, and choose `B_L` from the crude active prime mass to remove circularity. If a prior source with this mechanism is found, the mathematical claim remains valid and only this novelty audit should be updated.

### Validation boundary and falsification tests

The result should be withdrawn or weakened if any of the following fails:

1. the clipped WI-308 decomposition cannot be extended from smooth localizers to the endpoint-singular `chi_B` in the closed logarithmic form domain;
2. the archimedean localization-defect kernel is worse than first-order at the origin in the audited normalization, so that (19) does not make it `L^1`;
3. the oscillatory-tail estimate (8) or the normalization leading to (11) has a missing Fourier factor;
4. the uniform-shift exterior inclusion (14) fails for some `xi`;
5. the active compressed translations have a normalization larger than the `c_n` budget used in (23);
6. WI-247's attained finite odd zero mode lies outside the closed form domain on which (21) extends.

All six interfaces were checked against WI-307, WI-308, and WI-247 in this pass. No unreplayed finite matrix certificate, unproved zero statistic, or RH-conditional arithmetic estimate enters the result.