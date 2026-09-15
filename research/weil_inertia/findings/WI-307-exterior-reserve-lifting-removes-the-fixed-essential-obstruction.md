# WI-307 — Exterior-reserve lifting removes the frozen essential compact-repair obstruction

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-304--WI-306 show that Vincent Liu's particular tail-dropped localization, with the bounded unit-window comparison frozen at high-frequency reserve `beta_0=1/16`, has an essential negative band as soon as the first prime channel is active. That conclusion is exact for the frozen comparison. It is **not invariant under admissible changes of the bounded comparison**.

At every fixed outer aperture `L`, the unit-window archimedean symbol tends to `+infinity`, so the exterior reserve can be raised to an arbitrary prescribed value `B` by pushing the Fourier cutoff far enough out. The resulting localized lower comparison has the form

\[
\boxed{\mathcal D_{\chi,B}=B I-A_{L,\chi}+K_{L,\chi,B},}
\]

where `A_{L,chi}` is the finite sum of active prime-power compressed translations and `K_{L,chi,B}` is compact. Therefore, once

\[
B>\|A_{L,\chi}\|,
\]

the essential spectrum of `D_{chi,B}` is strictly positive. In particular its negative spectral subspace is finite-dimensional, and there exists a finite-rank positive operator that makes this *bounded comparison* positive as an operator.

This does **not** prove positivity of the Weil form: an arbitrary finite-rank repair is not automatically dominated by the omitted source-exact remainder. The substantive consequence is instead a no-go for the current no-go strategy. The essential-numerical-range obstruction of WI-304--WI-306 cannot by itself establish that tail-dropping or compact correction is structurally impossible. At fixed aperture it can always be pushed out of the essential spectrum by reserve lifting. Any RH-relevant obstruction must survive arbitrary admissible reserve choice, control the remaining finite/discrete negative modes, or address the growth of the construction as `L -> infinity`.

## 1. Arbitrarily large bounded lower comparisons on the unit window

Use the source normalization audited in WI-302--WI-306. On `D_1`, write

\[
\sigma_1(t)
=A(t)-\sum_{n\in\{2,3,4,5,7\}}c_n\cos(t\log n),
\qquad
c_n=\frac{2\Lambda(n)}{\sqrt n}.
\]

Liu's Theorem A proof uses

\[
A(t)\ge \log\frac{|t|}{2\pi}-\frac1{|t|}
\qquad(|t|\ge15/4).
\tag{1}
\]

Put

\[
C_1:=\sum_{n\in\{2,3,4,5,7\}}c_n.
\]

Since `|cos|<=1`, (1) gives

\[
\sigma_1(t)
\ge
\log\frac{|t|}{2\pi}-\frac1{|t|}-C_1,
\tag{2}
\]

so `sigma_1(t) -> +infinity` uniformly as `|t| -> infinity`.

Fix any finite `B>0`. Choose `Omega_B` so large that

\[
\sigma_1(t)\ge B
\qquad(|t|\ge\Omega_B).
\tag{3}
\]

For example it is enough to take

\[
\Omega_B\ge \max\left\{\frac{15}{4},\,2\pi e^{B+C_1+1}\right\}.
\]

Define the bounded Hermitian form on `H_1=L^2((-1,1))`

\[
\begin{aligned}
R_B(h)
={}&B\|h\|^2+\mathcal P(h)\\
&+\frac1{2\pi}
\int_{-\Omega_B}^{\Omega_B}
(\sigma_1(t)-B)|F_h(t)|^2\,dt.
\end{aligned}
\tag{4}
\]

Plancherel rewrites this as the exact source expression on the finite band plus the constant exterior weight `B`. Equation (3) therefore gives, for every smooth unit-window test,

\[
\boxed{Q(h)\ge R_B(h).}
\tag{5}
\]

No finite certificate and no RH hypothesis enters (5); it is only the explicit formula, the finite active prime list on the unit window, and the elementary large-`|t|` lower envelope (1).

Moreover

\[
R_B=B I+C_B,
\tag{6}
\]

with `C_B` compact on `H_1`. The pole term has finite rank, while the finite-band Fourier term has a continuous kernel on the bounded square `(-1,1)^2`, hence is Hilbert--Schmidt. Liu uses exactly this compactness mechanism at the frozen value `B=beta_0=1/16`; nothing in it is special to that value as long as the cutoff is finite.

Thus the high-frequency reserve available to this bounded-comparison construction is not intrinsically `1/16`: **at a fixed unit localization window it can be made arbitrarily large by moving the exterior cutoff**.

## 2. Localization preserves the arbitrary reserve

Fix a real normalized

\[
\chi\in C_c^\infty((-1,1)),
\qquad \|\chi\|_2=1,
\]

and an outer aperture `L>0`. For `f in D_L`, put

\[
f_y(u)=\chi(u)f(u+y).
\]

The source-exact localization identity used in WI-304 is

\[
Q(f)=\int Q(f_y)\,dy-\mathcal E_\chi(f),
\tag{7}
\]

where, with

\[
\rho_\chi(x)=\int\chi(v+x)\chi(v)\,dv,
\]

the defect is

\[
\begin{aligned}
\mathcal E_\chi(f)
={}&\int_0^{2L}(1-\rho_\chi(x))
\left(\frac{2e^{-x/2}}{1-e^{-2x}}-4\cosh(x/2)\right)H_f(x)\,dx\\
&+\sum_{\log n<2L}c_n(1-\rho_\chi(\log n))H_f(\log n).
\end{aligned}
\tag{8}
\]

Apply (5) to every `f_y` and define

\[
\mathcal M_{\chi,B}(f)=\int R_B(f_y)\,dy,
\qquad
\mathcal D_{\chi,B}=\mathcal M_{\chi,B}-\mathcal E_\chi.
\tag{9}
\]

Then

\[
\boxed{Q(f)\ge\mathcal D_{\chi,B}(f)}
\qquad(f\in\mathcal D_L).
\tag{10}
\]

The identity

\[
\int\|f_y\|^2dy=\|f\|^2
\]

shows that the `B I` part of (6) remains exactly `B I` after localization. The averaged compact part remains compact: writing the finite-band operator in (6) by its continuous kernel `c_B(u,v)`, the localized kernel is

\[
(s,t)\longmapsto
\int \chi(s-y)\chi(t-y)c_B(s-y,t-y)\,dy,
\]

which is continuous on the bounded square `(-L,L)^2`; the pole contribution is treated identically. Consequently

\[
\boxed{\mathcal M_{\chi,B}=B I+K^{(M)}_{L,\chi,B}}
\tag{11}
\]

with `K^(M)` compact.

## 3. Only the finite prime-power translation sum is noncompact

The continuous part of (8) is compact on `H_L`. Near zero, `1-rho_chi(x)=O(x^2)`, while the displayed archimedean kernel has only a first-order singularity, so their product is `O(x)`; on the remaining finite interval it is bounded. The resulting difference-kernel is therefore square-integrable on the bounded square and defines a Hilbert--Schmidt operator.

For the discrete part, let

\[
J_a=\frac{S_a+S_a^*}{2},
\]

where `S_a` is translation by `a` followed by compression to `(-L,L)`. Since

\[
H_f(a)=\langle f,J_af\rangle,
\]

the noncompact arithmetic part of (8) is

\[
A_{L,\chi}
:=
\sum_{\log n<2L}
\alpha_n J_{\log n},
\qquad
\alpha_n
:=c_n\bigl(1-\rho_\chi(\log n)\bigr).
\tag{12}
\]

Because `chi` is real and normalized, Cauchy--Schwarz gives `rho_chi(a)<=1`, hence `alpha_n>=0`. Also `||J_a||<=1`, so

\[
\|A_{L,\chi}\|
\le
W_{L,\chi}
:=
\sum_{\log n<2L}\alpha_n
<\infty.
\tag{13}
\]

Combining (8), (11), and (12) gives the promised exact operator structure

\[
\boxed{
D_{\chi,B}=B I-A_{L,\chi}+K_{L,\chi,B},
}
\tag{14}
\]

where `K_{L,chi,B}` is compact and self-adjoint.

This decomposition is the point missed by a frozen-reserve reading of WI-304--WI-306: the dangerous translations are genuinely noncompact, but their total bounded strength is finite at every fixed aperture, while the admissible exterior reserve `B` has no finite ceiling.

## 4. Positive essential spectrum and finite-rank operator repair

Choose

\[
B>W_{L,\chi}.
\tag{15}
\]

Then (13) implies

\[
B I-A_{L,\chi}
\succeq
(B-W_{L,\chi})I
=:\delta I,
\qquad \delta>0.
\tag{16}
\]

By the classical Weyl invariance of the essential spectrum under compact self-adjoint perturbations, (14)--(16) yield

\[
\boxed{
\sigma_{\rm ess}(D_{\chi,B})\subseteq[\delta,\infty).
}
\tag{17}
\]

Therefore all spectrum of `D_{chi,B}` below zero consists of isolated eigenvalues of finite multiplicity, and there can be only finitely many of them. Equivalently, the negative spectral projection has finite rank. If

\[
K^-_{L,\chi,B}:=(-D_{\chi,B})_+
\]

denotes the negative part in the functional calculus, then

\[
\boxed{
K^-_{L,\chi,B}\text{ is finite-rank and positive,}
\qquad
D_{\chi,B}+K^-_{L,\chi,B}\succeq0.
}
\tag{18}
\]

Equation (18) is an **operator-theoretic repair only**. It does not license adding `K^-` to the lower bound (10). To prove `Q>=0`, one would still have to obtain a source-valid inequality such as

\[
K^-_{L,\chi,B}\preceq Q-D_{\chi,B}
\]

on the legal smooth domain, or otherwise control the same finite negative sector by retained arithmetic/tail information. Nothing here supplies that domination.

## 5. Consequence for WI-304--WI-306 and the RH objective

For the frozen source comparison `B=beta_0=1/16`, WI-304--WI-306 remain correct: the first prime channel creates an essential negative interval, the compact-repair obstruction starts at `L>log2/2`, and localizer-shape optimization in support length two cannot remove it.

The new conclusion is about **scope**. That essential obstruction is not a property of the localization identity (7), nor of tail-dropping at fixed aperture in every admissible bounded comparison. It is a property of a particular reserve choice. The source itself already exposes the escape variable: the archimedean symbol grows without bound, and equations (2)--(5) turn that growth into an arbitrarily large exterior reserve.

Hence the implication

\[
\text{first active prime}
\Longrightarrow
\text{essential negative band}
\Longrightarrow
\text{no compact repair}
\]

cannot be promoted into an architecture-wide impossibility statement unless the reserve is frozen or independently bounded. At every fixed `L`, reserve lifting moves the problem into a different regime:

\[
\boxed{
\text{possible negativity of }D_{\chi,B}
\text{ is finite/discrete rather than essential.}
}
\tag{19}
\]

This redirects the useful research question. A successful defect-elimination argument now has to control the finite negative spectral sector **with source-valid information**, or prove a uniform-in-`L` obstruction that survives arbitrary reserve lifting. The latter is nontrivial because making `B` large forces the Fourier cutoff `Omega_B` far out. The explicit choice following (3) already grows like `exp(B)`. Thus reserve lifting removes the fixed-aperture essential obstruction but can replace it with a severe scale problem as `L` grows; it is not a bootstrap to RH by itself.

## 6. Prior-art and novelty audit

The load-bearing ingredients are established. Liu's frozen source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59` supplies the exact unit-window symbol, the digamma lower envelope (1), the bounded comparison at `beta_0=1/16`, the localization identity (7)--(8), and the compactness mechanism `R_1-beta_0 I`. The manuscript's Obstruction Theorem fixes that comparison and proves that no fixed compact correction repairs its negative high-frequency limit.

WI-304 extracted the arbitrary-prime-power essential numerical-range criterion and explicitly listed **raising the high-frequency reserve** as one abstract escape. WI-305 showed that the frozen reserve loses already at the first active prime, and WI-306 proved that same-support localizer-shape optimization cannot reduce that first-prime loss. None of those findings proves that the reserve can be raised arbitrarily while preserving a valid lower comparison, nor do they identify the resulting positive-essential-spectrum / finite-negative-index regime.

The operator-theoretic step from (14)--(16) to (17)--(18) is classical Weyl theory for compact perturbations of bounded self-adjoint operators; no novelty is claimed for that theorem. A targeted audit of Liu's frozen manuscript and the current line-local findings found no statement of the arbitrary-reserve construction (4)--(5), no theorem that every fixed aperture can be moved out of the essential-obstruction regime, and no finite-rank negative-part consequence in this localization. No priority claim is made.

### Validation boundary

The result is exact at the level of the bounded source comparison and uses no unreplayed finite matrix certificate from Liu. It does **not** validate Liu's claimed `17/16` coercivity theorem, does not prove positivity of `D_{chi,B}`, and does not prove `Q>=0`. Most importantly, (18) is not a source-valid Weil lower bound until the finite-rank repair is paid for by an independently justified positive remainder. The finding closes only the stronger claim that the frozen essential numerical-range obstruction is unavoidable throughout the localization architecture.