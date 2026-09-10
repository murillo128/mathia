# WI-225 — Logvinenko--Sereda forces logarithmic cutoff for adaptive scalar screens

## Status

`LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

The harmonic-analysis input is the classical Logvinenko--Sereda theorem in Kovrijkine's quantitative form. The specialization below to the WI-224 adaptive zeta-screen normalization is an exact deduction. It closes the adaptive scalar minimax gap left explicitly open in WI-224, but it does **not** improve the unconditional simple-critical zero proportion and it makes no priority claim.

## Claim

Work in the scalar detector architecture inherited from WI-218--WI-224. Let `J_0` be a fixed compact interval of length `b>0`, and for each `T` let

\[
\varphi_T\in L^2(J_0),\qquad
\int_{J_0}\varphi_T(u)\,du=1.
\tag{1}
\]

Define the imaginary-axis transfer function

\[
H_T(\xi)
:=\Phi_T(2\pi i\xi)
=\int_{J_0}\varphi_T(u)e^{2\pi i\xi u}\,du.
\tag{2}
\]

Then there are constants `c_0,c_1>0`, depending only on `b`, such that for every `R>0` and every admissible detector,

\[
\boxed{
\sup_{|\xi|\ge R}|H_T(\xi)|
\ge c_0e^{-c_1R}.
}
\tag{3}
\]

Consequently, any scalar total-mass screen that controls all remote zeros by one stopband supremum and needs a polynomially small tail in `T` must have

\[
\boxed{R_T=\Omega(\log T).}
\tag{4}
\]

For the nontrivial mesoscopic regime `M=T^{\vartheta+o(1)}` with fixed `0<\vartheta<1`, the WI-224 spline construction already gives `R_T=O(\log T)`. Hence within this architecture

\[
\boxed{R_T=\Theta(\log T)}
\tag{5}
\]

and the corresponding physical localization radius is necessarily

\[
\boxed{
\frac{M}{\log T}R_T=\Theta(M).
}
\tag{6}
\]

In particular, arbitrary `T`-dependent adaptation of a normalized fixed-support scalar detector cannot improve the WI-224 `O(M)` physical radius to `o(M)` while the remote contribution is paid by global zero mass times a single uniform stopband bound.

## 1. Classical input: quantitative Logvinenko--Sereda

Kovrijkine's Theorem 1 states the following one-dimensional form. If `f in L^p(R)`, `1<=p<=infinity`, the Fourier support of `f` lies in an interval of length `b`, and `E` is `(a,gamma)`-thick, meaning

\[
|E\cap I|\ge\gamma a
\tag{7}
\]

for every interval `I` of length `a`, then for an absolute constant `C`

\[
\|f\|_{L^p(E)}
\ge
\left(\frac{\gamma}{C}\right)^{C(ab+1)}
\|f\|_{L^p(\mathbb R)}.
\tag{8}
\]

Primary source: O. Kovrijkine, *Some results related to the Logvinenko--Sereda theorem*, Proc. Amer. Math. Soc. **129** (2001), no. 10, 3037--3047, DOI `10.1090/S0002-9939-01-05926-3`, arXiv `math/0012186`. The statement and the inclusion of `p=infinity` were checked against the primary paper before using (8).

## 2. The detector transfer function is bandlimited

Use the Fourier convention

\[
\widehat f(\omega)
=\int_{\mathbb R}f(\xi)e^{-2\pi i\xi\omega}\,d\xi.
\tag{9}
\]

Equation (2) is the inverse Fourier transform of `varphi_T` (up to the harmless reflection imposed by convention). Therefore

\[
\operatorname{supp}\widehat H_T
\subseteq -J_0,
\tag{10}
\]

an interval of the same fixed length `b`. Compact support and `varphi_T in L^2` imply `varphi_T in L^1`, so `H_T` is bounded and continuous. Normalization gives

\[
H_T(0)=1,
\qquad
\|H_T\|_\infty\ge1.
\tag{11}
\]

Notice that no uniform `L^2` bound is needed for the quantitative lower bound (3); WI-224's uniform-conditioning hypothesis remains necessary for pairing against its unspecified `o(1)` screen residual, but Logvinenko--Sereda itself only needs each detector to define a bounded bandlimited `H_T`.

## 3. Thick-set specialization gives the exponential lower bound

For `R>0` set

\[
E_R:=\mathbb R\setminus[-R,R].
\tag{12}
\]

Every interval of length `4R` loses at most `2R` to `[-R,R]`, hence `E_R` is `(4R,1/2)`-thick. Apply (8) with `p=infinity`, `f=H_T`, `a=4R`, and `gamma=1/2`. Together with (11),

\[
\sup_{|\xi|\ge R}|H_T(\xi)|
\ge
\left(\frac1{2C}\right)^{C(4bR+1)}
\|H_T\|_\infty
\ge
\left(\frac1{2C}\right)^{C(4bR+1)}.
\tag{13}
\]

Absorbing the fixed factors into constants gives (3). This also lower-bounds any full Fourier--Laplace strip norm used by the off-line screen, because

\[
\sup_{|\alpha|\le1,\ |\xi|\ge R}
|\Phi_T(\alpha+2\pi i\xi)|
\ge
\sup_{|\xi|\ge R}|\Phi_T(2\pi i\xi)|.
\tag{14}
\]

Thus allowing real-part displacement does not evade the obstruction.

## 4. Polynomial remote suppression forces `R_T=Omega(log T)`

WI-224's scalar total-mass screen bounds the remote detector contribution by

\[
\ll \frac{N_T}{M}\,\varepsilon_T,
\qquad
\varepsilon_T
:=\sup_{|\xi|\ge R_T}|H_T(\xi)|,
\tag{15}
\]

or by the larger strip supremum in (14). In the nontrivial mesoscopic regime

\[
M=T^{\vartheta+o(1)},
\qquad 0<\vartheta<1,
\qquad N_T\asymp T\log T,
\tag{16}
\]

making (15) `o(1)` requires

\[
\varepsilon_T=o(M/N_T)
=T^{-(1-\vartheta)+o(1)}/\log T.
\tag{17}
\]

So the required stopband suppression is polynomial in `T`. Combining (3) and (17),

\[
c_0e^{-c_1R_T}
\le \varepsilon_T
\le T^{-(1-\vartheta)+o(1)}/\log T,
\tag{18}
\]

which after logarithms yields

\[
R_T
\ge
\frac{1-\vartheta-o(1)}{c_1}\log T
=\Omega(\log T).
\tag{19}
\]

WI-224 constructs uniformly `L^2`-conditioned adaptive spline detectors with `R_T=O(\log T)` and polynomially small strip tail. Therefore (19) is sharp in order and proves (5). Under the inherited normalization

\[
\xi_\rho
=\frac{(\gamma_\rho-\gamma_0)\log T}{2\pi dM},
\tag{20}

the dimensionless cutoff becomes physical radius `(M/log T)R_T`, giving (6).

## 5. What route is actually closed

The result is a barrier for the **scalar fixed-support, global-supremum/total-mass architecture**. WI-224's `O(M)` localization is order-optimal there. The adaptive minimax interval left open there, `omega(1)<=R_T<=O(log T)`, collapses to `Theta(log T)` as soon as the tail must beat the global factor `N_T/M` polynomially.

This does not show that zeta screens themselves have an `Omega(M)` localization floor under richer information. In particular, the argument does not exclude coupled or vector-valued observables, phase/sign-sensitive cancellation of remote channels, arithmetic or zero-density input that reduces the effective remote mass, support width growing with `T` if a future explicit-formula regime legally permits it, or direct source-coercivity inequalities using the full signed covariance rather than a scalar Fourier tail. Those are now the relevant escape routes.

Nor does (6) convert the already forced `Omega(M)` radial-weighted source into `Omega(M)` distinct zeros. The multiplicity/radial-weight ledger and the local zero-count capacity gap identified in WI-224 remain separate.

## 6. Prior-art and novelty audit

The underlying theorem is classical and is cited above. Searches around `Logvinenko--Sereda`, `Kovrijkine`, zeta zeros, compact-support detectors, thick sets, and source/screen localization did not surface a prior application of (8) to this Weil-inertia screen architecture. The local `weil_inertia` corpus had no Kovrijkine/Logvinenko--Sereda result, and WI-224 explicitly recorded `R_T=Omega(log T)` for arbitrary adaptive fixed-support scalar detectors as the open minimax barrier.

The durable delta is therefore the exact specialization (12)--(19), not the uncertainty theorem itself. No claim of external priority is made. If a prior application is found later, the classification should be downgraded to literature-backed without changing the mathematical consequence.

## Consequence for the research line

The scalar-detector cutoff problem introduced by WI-224 is closed in asymptotic order. Further optimization of adaptive fixed-support scalar windows cannot shrink the physical screen below `Theta(M)` while remote zeros are controlled by a uniform stopband times total mass. Research effort should move to a source-coercive ingredient that survives confluence and drifting bows but keeps more structure than a scalar total-mass envelope: coupled observables, signed covariance, arithmetic restrictions on the remote reservoir, or a direct conversion of the already localized radial-weighted mass into an impossible local zero/multiplicity budget.
