---
id: WP-419
title: Arbitrary Bost--Connes phase coefficients make fixed-ratio critical blocks Haar-universal and finitely correlation-programmable
branch: weil_positivity
status: supported
kind: critical-kms-arbitrary-phase-coefficient-haar-universality
claim_strength: exact RH-independent classification extending WP-418 from phase characters to arbitrary coefficients in the Bost--Connes phase algebra; each critical fixed-ratio coefficient block is the ordinary Haar L2 space of Z-hat, unitary coefficients only modulate the old GCD envelope by a Haar correlation factor, while unrestricted continuous coefficients can realize every prescribed finite correlation matrix exactly, so coefficient choice is maximally programmable unless an independent source law fixes it
created: 2026-09-23
related: [WP-216, WP-413, WP-415, WP-417, WP-418]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
  - Pontryagin duality for Q/Z and Z-hat, Haar measure on compact profinite groups, and finite-index subgroup measure
  - Standard Hilbert-space Gram factorization of positive semidefinite correlation matrices
---

# WP-419 — Arbitrary Bost--Connes phase coefficients make fixed-ratio critical blocks Haar-universal and finitely correlation-programmable

## Claim

`WP-418` classifies insertion of individual phase characters `e(r)` into the canonical fixed-ratio Bost--Connes rays. The resulting critical Gram keeps the old GCD amplitude and adds only a rational-character compatibility mask. The immediate non-character escape is to replace those characters by arbitrary elements of the full phase algebra

\[
D=C^*(\mathbf Q/\mathbf Z)\cong C(\widehat{\mathbf Z}).
\]

That larger class has an exact classification. Fix a reduced ratio `a/b`, write

\[
x_{k,f}^{a/b}:=\mu_{ak}f\mu_{bk}^*,
\qquad k\ge1,\quad f\in D,
\tag{1}
\]

and let `phi_1` be the unique critical `KMS_1` state. Put

\[
P_k(f):=\mu_k f\mu_k^*\in D.
\tag{2}
\]

Then for all `f,h in D`,

\[
\boxed{
\phi_1\!\left((x_{k,f}^{a/b})^*x_{\ell,h}^{a/b}\right)
=\frac1b\int_{\widehat{\mathbf Z}}
\overline{P_kf(\rho)}\,P_\ell h(\rho)\,dm(\rho),
}
\tag{3}
\]

where `m` is Haar probability measure. In the function model,

\[
P_kf(\rho)
=\mathbf 1_{k\widehat{\mathbf Z}}(\rho)
 f(\rho/k).
\tag{4}
\]

Consequently, if `d=(k,ell)`, `k=dk_0`, `ell=dell_0`, `(k_0,ell_0)=1`, and `L=lcm(k,ell)=dk_0ell_0`, then

\[
\boxed{
\phi_1\!\left((x_{k,f}^{a/b})^*x_{\ell,h}^{a/b}\right)
=\frac1{bL}
\int_{\widehat{\mathbf Z}}
\overline{f(\ell_0t)}\,h(k_0t)\,dm(t).
}
\tag{5}
\]

The diagonal is

\[
\boxed{
\|x_{k,f}^{a/b}\|_{\phi_1}^2
=\frac1{bk}\|f\|_{L^2(m)}^2.
}
\tag{6}
\]

Define

\[
V_k:L^2(\widehat{\mathbf Z},m)\to L^2(\widehat{\mathbf Z},m),
\qquad
V_kf:=\sqrt{k}\,P_kf.
\tag{7}
\]

Then `V_k` is an isometry **onto**

\[
H_k:=L^2(k\widehat{\mathbf Z},m).
\tag{8}
\]

After normalizing `f` and `h`, the critical GNS Gram is exactly

\[
\boxed{
\widetilde K\big((k,f),(\ell,h)\big)
=\left\langle
V_k\frac{f}{\|f\|_2},
V_\ell\frac{h}{\|h\|_2}
\right\rangle_{L^2(m)}.
}
\tag{9}
\]

Thus the full phase-coefficient sector on one fixed ratio is not a new positive geometry: its GNS completion is ordinary Haar `L^2(Z-hat)`. In fact the conclusion is stronger. For **every finite list** `k_1,...,k_N` and **every** Hermitian positive semidefinite correlation matrix `C in M_N(C)` with `C_ii=1`, there exist continuous nonzero coefficients `f_i in C(Z-hat)` such that the normalized vectors `x_{k_i,f_i}^{a/b}` have Gram matrix exactly `C`.

So arbitrary phase-algebra coefficients are **maximally finitely programmable** under the ordinary critical KMS scalarization. A desired finite positive kernel can be written into the coefficient choice itself.

There is a useful sharp boundary. If each coefficient is restricted to a unitary function `u in C(Z-hat,U(1))`, then (5)--(6) give

\[
\boxed{
\widetilde K\big((k,u),(\ell,v)\big)
=\frac{d}{\sqrt{k\ell}}
\int_{\widehat{\mathbf Z}}
\overline{u(\ell_0t)}v(k_0t)\,dm(t),
}
\tag{10}
\]

and therefore

\[
\left|\widetilde K\big((k,u),(\ell,v)\big)\right|
\le \frac{d}{\sqrt{k\ell}}.
\tag{11}
\]

The character formula of `WP-418` is the special case in which the Haar correlation in (10) is exactly `0` or `1`. General unitary phases can soften that mask into an arbitrary Haar correlation, but cannot exceed the old GCD envelope. Complete finite programmability appears only after allowing general, not necessarily unitary, phase-algebra coefficients.

Different rational ratios remain KMS-orthogonal exactly as in `WP-417`--`WP-418`, because every `f in D` has time degree zero. Hence neither arbitrary coefficients nor non-character unitary phases mix thermodynamic ratio sectors.

**Classification:** `CLASSICAL-BC-TRANSFER-ENDOMORPHISM + EXACT-DERIVED + RH-INDEPENDENT + CRITICAL-KMS-HAAR + FIXED-RATIO-COEFFICIENT-CLASSIFICATION + NESTED-CYLINDER-L2-ISOMETRIES + UNITARY-GCD-CORRELATION-ENVELOPE + ARBITRARY-COEFFICIENT-FINITE-CORRELATION-PROGRAMMABILITY + UNIVERSAL-HILBERT-GRAM-SIGN + DECISIVE-NARROWING + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The arbitrary coefficient stays inside the phase algebra after fixed-ratio reduction

The Bost--Connes integer isometries commute multiplicatively. Therefore

\[
\begin{aligned}
x_{k,f}^{a/b}
&=\mu_a\mu_k f\mu_k^*\mu_b^*\\
&=\mu_aP_k(f)\mu_b^*.
\end{aligned}
\tag{12}
\]

The phase algebra is fixed by the time evolution, and `P_k(f)` has degree zero. Hence

\[
\begin{aligned}
(x_{k,f}^{a/b})^*x_{\ell,h}^{a/b}
&=\mu_bP_k(f^*)P_\ell(h)\mu_b^*.
\end{aligned}
\tag{13}
\]

For any fixed element `g in D`, the `KMS_1` relation gives

\[
\phi_1(\mu_bg\mu_b^*)=b^{-1}\phi_1(g).
\tag{14}
\]

At the critical point the restriction of `phi_1` to `D` is Haar measure on `Z-hat`. Combining (13)--(14) proves (3).

Nothing in this step uses a character basis. The character computation of `WP-418` was one Fourier-coordinate realization of a more elementary statement: the entire surviving coefficient lives in the critical Haar representation of the phase algebra.

## 2. The transfer endomorphism is a cylinder isometry after the critical normalization

The standard Bost--Connes transfer relation

\[
P_k(e(r))
=\frac1k\sum_{ks=r}e(s)
\tag{15}
\]

is equivalent under Pontryagin duality to (4). Indeed, on `k Z-hat` the point `rho/k` is unique, while outside `k Z-hat` the character average cancels. By density of finite character combinations, the formula holds for every `f in C(Z-hat)`.

The subgroup `k Z-hat` has Haar mass `1/k`. With `rho=kt` on that subgroup,

\[
\int |P_kf(\rho)|^2dm(\rho)
=\frac1k\int |f(t)|^2dm(t).
\tag{16}
\]

Thus `V_k=sqrt(k)P_k` is an isometry. It is also onto `H_k`: if `g` is supported on `k Z-hat`, then

\[
(V_k^{-1}g)(t)=k^{-1/2}g(kt).
\tag{17}
\]

The same formula preserves continuity. Therefore continuous Bost--Connes coefficients already give a dense set in every support subspace, and no von Neumann or measurable enlargement is needed for the classification.

Equation (6) follows by setting `ell=k` and `h=f` in (3), and (9) follows by dividing (3) by the two diagonal norms.

There is an even simpler whole-sector statement. The linear map on GNS vectors

\[
x_{k,f}^{a/b}\Omega_1
\longmapsto
b^{-1/2}P_kf
\tag{18}
\]

preserves every inner product by (3). Since the `k=1` slice already contains all continuous functions `f`, its closed range is all of `L^2(Z-hat,m)`. Hence the **entire** fixed-ratio phase-coefficient GNS sector is unitarily equivalent to ordinary Haar `L^2`, up to the harmless common factor `b^{-1/2}` before normalization. The reduced numerator `a` disappears completely.

## 3. Explicit overlap formula and the unitary boundary

The supports of `P_kf` and `P_ell h` meet on

\[
k\widehat{\mathbf Z}\cap\ell\widehat{\mathbf Z}
=L\widehat{\mathbf Z},
\qquad L=\operatorname{lcm}(k,\ell).
\tag{19}
\]

Write `rho=Lt`. Then

\[
\rho/k=\ell_0t,
\qquad
\rho/\ell=k_0t,
\]

and ambient Haar measure on `L Z-hat` is `L^{-1}` times normalized Haar measure after this parametrization. Substitution into (3) gives (5).

If `u,v` are unitary-valued, their ambient `L^2` norms are one, so normalization of (5) gives (10). The integral in (10) is an average of a unit-modulus function and therefore has modulus at most one, proving (11).

For characters `u=e(r)` and `v=e(s)`, the integrand is a character of `Z-hat`. Haar orthogonality makes its integral equal to one precisely when

\[
\ell_0r=k_0s\quad\text{in }\mathbf Q/\mathbf Z,
\tag{20}
\]

and zero otherwise. Equation (10) then becomes exactly the masked GCD Gram of `WP-418`.

This check matters because it identifies the correct generalization. It would be false to extend the `WP-418` statement by saying that every arbitrary coefficient preserves the GCD amplitude. **Pure phases do; general phase-algebra elements do not.** Nonunitary coefficients can concentrate on deeper cylinders and amplify normalized overlaps all the way to one.

## 4. Every finite correlation matrix can be programmed exactly

Fix scales `k_1,...,k_N` and let

\[
L=\operatorname{lcm}(k_1,\ldots,k_N).
\tag{21}
\]

Then

\[
H_L\subseteq H_{k_i}
\qquad\text{for every }i.
\tag{22}
\]

The clopen subgroup `L Z-hat` is homeomorphic to `Z-hat`, so `H_L` is infinite-dimensional and contains arbitrarily large finite orthonormal families of continuous functions. Concretely, one may take normalized characters of `L Z-hat` and extend them by zero; clopenness makes those extensions continuous.

Now let `C` be any `N x N` positive semidefinite matrix with unit diagonal. Standard Gram factorization gives unit vectors `z_1,...,z_N` in `C^r`, `r=rank(C)`, such that

\[
C_{ij}=\langle z_i,z_j\rangle.
\tag{23}
\]

Choose orthonormal continuous functions `q_1,...,q_r in H_L` and isometrically embed `C^r` into `H_L` by sending the standard basis to the `q_j`. Let `g_i in H_L` be the images of `z_i`. Then

\[
\|g_i\|_2=1,
\qquad
\langle g_i,g_j\rangle=C_{ij}.
\tag{24}
\]

Because `g_i in H_L subseteq H_{k_i}` and `V_{k_i}` is onto `H_{k_i}`, define

\[
f_i:=V_{k_i}^{-1}g_i.
\tag{25}
\]

Equation (17) shows that every `f_i` is continuous, and isometry gives `||f_i||_2=1`. Finally (9) yields

\[
\boxed{
\widetilde K\big((k_i,f_i),(k_j,f_j)\big)=C_{ij}
\quad\text{for all }i,j.
}
\tag{26}
\]

This is exact finite programmability, not an approximation or a density statement. It also holds for repeated scales.

The mechanism is completely transparent: arbitrary coefficients may localize every chosen vector into the common deeper cylinder `L Z-hat`, where the original divisibility support distinctions no longer constrain their finite Gram geometry.

## 5. Matched control and arithmetic specificity

The positivity in (9) is the ordinary Hilbert-space inequality

\[
\left\|\sum_i c_iV_{k_i}f_i\right\|_2^2\ge0.
\tag{27}
\]

The finite-programming argument uses only nested positive-measure support subspaces with a nontrivial common intersection. The same construction works in a completely nonarithmetic probability space carrying nested measurable subsets of positive measure and isometric coefficient maps onto their `L^2` support spaces. No zeta zero, prime distribution, Gamma factor, polar term, or explicit-formula theorem enters the sign.

This sharpens the target-selection warning after `WP-418`. Character labels could already program compatibility masks. Allowing arbitrary phase-algebra coefficients is much less restrictive: on every finite panel the **entire positive correlation matrix** can be chosen. Therefore agreement with a desired finite positive target is evidence only if a separate source theorem fixes the coefficient family before that target is inspected.

Conversely, the unitary boundary (10)--(11) is genuinely more rigid. A source law forcing a specific non-character unitary family could create nontrivial incidence without the full support-localization freedom used in (21)--(26). But its ordinary KMS sign would still be Haar-Gram positivity, and it would still lack the archimedean and polar sectors. Such a family would need an independent arithmetic provenance theorem and a separate finite--archimedean assembly before it could address the canonical mandate.

## 6. Relation to the current frontier

`WP-417` classifies bare canonical partial-isometry rays and obtains one GCD Gram in every thermodynamic ratio block. `WP-418` retains individual phase characters and finds a rational compatibility mask on that same amplitude. The present result closes the direct next enlargement **inside the existing phase algebra**.

It is stronger than merely observing that arbitrary coefficients again form a Gram. Equations (7)--(9) identify the exact support subspaces, equation (18) identifies the entire fixed-ratio GNS completion with the critical Haar space, equation (10) gives the sharp pure-phase GCD envelope, and equation (26) shows that general continuous coefficients have maximal finite correlation freedom.

This is distinct from `WP-413`, whose equal-scale twisted paths reduce relative holonomy to unit-space unitaries, and from `WP-415`, whose abstract correspondence argument proves universal module-Gram positivity. Here the source and range supports vary along the actual Bost--Connes fixed-ratio rays, and the critical transfer maps are classified explicitly enough to prove exact finite programmability despite those varying supports.

The result does **not** close every "non-character incidence" route. It closes arbitrary coefficient insertion from the canonical phase algebra under the ordinary critical KMS scalarization. Surviving possibilities include a source theorem that selects a special restricted coefficient family, active modular/fibre dynamics, mixing of time degrees, a genuinely non-Gram orientation-sensitive observable, a changed scalarization, a non-phase coefficient module with additional relations, or a canonical finite--archimedean coupling. Any such route must derive its extra structure from the source rather than use the freedom exposed by (26) to fit the desired answer.

## 7. Prior-art and novelty audit

The ingredients are classical. Bost--Connes supplies the phase algebra, integer isometries, transfer endomorphisms, time evolution, and critical KMS state. Pontryagin duality identifies the phase algebra with `C(Z-hat)`, while Haar measure gives the finite-index subgroup masses and the critical scalar product. Realization of a finite positive semidefinite correlation matrix as the Gram of unit vectors is elementary Hilbert-space theory.

The literature audit found these standard ingredients and the usual Bost--Connes transfer formula, but no distinct arithmetic positivity theorem is needed or claimed here. There is no claim of new general operator-algebra or harmonic-analysis mathematics. The durable Mathia contribution is the **line-specific exact composition at the current frontier**: after `WP-418`, replacing characters by arbitrary phase coefficients makes each critical fixed-ratio block Haar-universal, pure phases remain under the old GCD envelope, and unrestricted continuous coefficients can program every finite correlation matrix exactly.

The internal novelty boundary is also sharp. `WP-418` does not imply the programmability statement for arbitrary coefficients because its characters cannot localize amplitude on deeper clopen cylinders; their overlaps are restricted to the `0/1` compatibility mask. `WP-415` supplies abstract Gram positivity but not the concrete Bost--Connes support-isometry classification or the exact realization theorem (26). Thus this finding eliminates a genuinely larger admissible coefficient class rather than renaming either earlier obstruction.

## 8. Adversarial and falsification gates

The theorem depends on four exact structural facts: the Bost--Connes transfer formula (4), Haar restriction of the critical `KMS_1` state, the sandwich identity (14), and the finite-index Haar mass `m(k Z-hat)=1/k`. Failure of any one would invalidate (3)--(9).

The finite-programming theorem additionally requires unrestricted coefficients from the full continuous phase algebra. If a proposed construction restricts coefficients by a source-derived relation -- for example to canonical characters, to a specified unitary orbit, to a fixed subalgebra, or to a coefficient family coupled dynamically across `k` -- then (26) cannot simply be invoked. That restricted family must be analyzed on its own terms. Equation (10), rather than complete programmability, is the correct immediate control for arbitrary unitary-valued coefficients.

Likewise the result is critical-temperature specific in its Haar form. Ratio-frequency orthogonality survives at every positive inverse temperature, but the restriction of a noncritical KMS state to the phase algebra is not being identified here with Haar measure. No claim is made that the same `L^2` realization or programming theorem holds unchanged away from `beta=1`.

Finally, no part of the result supplies the archimedean Gamma contribution, polar normalization, or a completed Weil form. It proves a structural obstruction to treating arbitrary phase-coefficient positivity as explanatory evidence; it does not prove RH, Weil positivity, or impossibility of every Bost--Connes completion.

## Consequence

**Supported exact negative/classification.** The non-character enlargement of `WP-418` inside the canonical Bost--Connes phase algebra does not reveal a new arithmetic sign mechanism under critical KMS scalarization. Pure phases only decorate the old GCD envelope by ordinary Haar correlations. General continuous coefficients are more flexible still: every finite positive correlation matrix can be realized exactly, making coefficient selection maximally target-programmable unless an independent source law fixes it. The next meaningful escape must therefore add or derive structure that is not merely a free choice of phase-algebra coefficient before the same Haar-Gram readout.