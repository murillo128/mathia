---
id: WP-415
title: Non-full correspondence path Grams are universal and common supports collapse to corner-unitary correlations
branch: weil_positivity
status: supported
kind: nonfull-correspondence-path-gram-obstruction
claim_strength: exact RH-independent Hilbert-correspondence obstruction; scalarized correspondence-path Grams are positive for every positive functional, and common generalized rank-one range support reduces them to coefficient partial-isometry correlations, with common source support reducing further to corner-unitary correlations, so non-fullness/common support alone adds no arithmetic sign mechanism beyond the universal Gram positivity left open by WP-414
created: 2026-09-23
related: [WP-411, WP-412, WP-413, WP-414]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - E. C. Lance, Hilbert C*-Modules: A Toolkit for Operator Algebraists, London Mathematical Society Lecture Note Series 210, Cambridge University Press, 1995
  - F. Abadie and D. Ferraro, Equivalence of Fell bundles over groups, J. Operator Theory 81 (2019), 273-319; arXiv:1711.02577
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
---

# WP-415 — Non-full correspondence path Grams are universal and common supports collapse to corner-unitary correlations

## Claim

`WP-414` leaves non-full source/range geometry and correspondence-valued paths as one possible escape from the passive full-fibre Bost--Connes obstruction. There is a sharp distinction inside that escape. A non-full correspondence can constrain **which coefficients occur**, but ordinary Hilbert-module Gram positivity cannot by itself supply the missing Weil orientation: after scalarization by any positive functional, that sign is automatic in every Hilbert C-star module.

Let `X` be a right Hilbert `A`-module, let `xi_a in X` be finitely many path vectors, and let `phi` be any positive functional on `A`. Define

\[
G_{ab}:=\phi(\langle \xi_a,\xi_b\rangle_A).
\tag{1}
\]

Then

\[
\boxed{G\succeq0}
\tag{2}
\]

for every `X`, every path family, and every positive `phi`. Hence non-fullness cannot make the **positive sign** arithmetic unless the source first forces a special coefficient identity whose content is stronger than positivity of (1).

There is a further exact reduction for the most direct common-support continuation of `WP-414`. Suppose

\[
p_a:=\langle\xi_a,\xi_a\rangle_A
\tag{3}
\]

is a projection for every `a`, and suppose the generalized rank-one range projections agree in the compact operators on `X`:

\[
q:=\theta_{\xi_a,\xi_a}\in\mathcal K(X)
\qquad\text{is independent of }a.
\tag{4}
\]

Fix a reference path `0` and set

\[
u_a:=\langle\xi_0,\xi_a\rangle_A.
\tag{5}
\]

Then

\[
\boxed{
u_a^*u_a=p_a,\qquad u_au_a^*=p_0,\qquad \xi_a=\xi_0u_a,\qquad \langle\xi_a,\xi_b\rangle_A=u_a^*u_b.}
\tag{6}
\]

Thus common-range paths reduce exactly to **partial-isometry correlations in the coefficient algebra**. If in addition all source projections agree, `p_a=p`, every `u_a` is a unitary of the proper corner `pAp`, and

\[
G_{ab}=\phi(u_a^*u_b)
\tag{7}
\]

is a corner-unitary correlation Gram. This is the non-full/common-support analogue of the full-unitary reduction in `WP-414`.

The conclusion is deliberately limited. Varying source supports, incidence between inequivalent support projections, twisted multiplication, or genuinely non-Gram readouts can still carry source information. What is closed here is the idea that passing from the full-fibre setting to an ordinary non-full Hilbert-correspondence Gram, by itself, creates a new arithmetic positivity mechanism.

**Classification:** `CLASSICAL-HILBERT-CSTAR-MODULE-GRAM-POSITIVITY + EXACT-DERIVED-COMMON-SUPPORT-REDUCTION + NONFULL-CORRESPONDENCE + PARTIAL-ISOMETRY-CORRELATIONS + CORNER-UNITARY-CORRELATIONS + KMS-BALANCED-FIXED-POINT-TRACE + MATCHED-NONARITHMETIC-PROPER-CORNER-CONTROL + NO-NEW-SIGN-FROM-NONFULLNESS-ALONE + COEFFICIENT-SELECTION-MAY-SURVIVE + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Scalarized Hilbert-module path Grams are universally positive

For arbitrary scalars `c_a`, the defining Hilbert-module identity gives

\[
\begin{aligned}
\sum_{a,b}\overline{c_a}G_{ab}c_b
&=\phi\!\left(
\sum_{a,b}\overline{c_a}\langle\xi_a,\xi_b\rangle_Ac_b
\right)\\
&=\phi\!\left(
\left\langle\sum_a\xi_ac_a,\sum_b\xi_bc_b\right\rangle_A
\right)\\
&\ge0.
\end{aligned}
\tag{8}
\]

Nothing in (8) requires fullness of `X`, a groupoid model, Bost--Connes arithmetic, a KMS state, or even a dynamics. It is the defining positivity of a Hilbert C-star module followed by a positive functional.

This is the first gate on the correspondence escape. A source-derived non-full module may still be highly arithmetic, and its inner products may encode useful coefficients. But if the proposed Weil sign theorem is simply that the scalar matrix (1) is positive, the theorem has not used that arithmetic: the same sign holds for every matched nonarithmetic Hilbert module. The arithmetic burden therefore moves to an **exact coefficient theorem** showing that the source-selected inner products equal the completed Weil coefficients with the correct finite, archimedean, and polar normalization.

## 2. Common generalized range support forces partial-isometry factorization

Assume (3)--(4). Because `p_a` is a projection,

\[
\|\xi_a-\xi_ap_a\|^2
=\|(1-p_a)p_a(1-p_a)\|=0,
\tag{9}
\]

so `xi_a=xi_a p_a`. Therefore

\[
q\xi_a
=\theta_{\xi_a,\xi_a}\xi_a
=\xi_a\langle\xi_a,\xi_a\rangle_A
=\xi_ap_a
=\xi_a.
\tag{10}
\]

Using the same `q=theta_{xi_0,xi_0}` and the definition (5),

\[
\xi_0u_a
=\xi_0\langle\xi_0,\xi_a\rangle_A
=\theta_{\xi_0,\xi_0}\xi_a
=q\xi_a
=\xi_a.
\tag{11}
\]

The source and range identities follow directly:

\[
\begin{aligned}
u_a^*u_a
&=\langle\xi_a,\xi_0\rangle_A\langle\xi_0,\xi_a\rangle_A
 =\langle\xi_a,q\xi_a\rangle_A
 =p_a,\\
u_au_a^*
&=\langle\xi_0,\xi_a\rangle_A\langle\xi_a,\xi_0\rangle_A
 =\langle\xi_0,q\xi_0\rangle_A
 =p_0.
\end{aligned}
\tag{12}
\]

Hence each `u_a` is a partial isometry from the support `p_a` to `p_0`. Finally, (11) gives

\[
\langle\xi_a,\xi_b\rangle_A
=\langle\xi_0u_a,\xi_0u_b\rangle_A
=u_a^*p_0u_b
=u_a^*u_b,
\tag{13}
\]

where `p_0u_b=u_b` follows from `u_bu_b^*=p_0`.

If `p_a=p` for all `a`, then `u_a^*u_a=u_au_a^*=p`, so `u_a` is a unitary in the unital corner `pAp`. Equation (13) therefore reduces the entire common-support path family to a corner-unitary correlation system. The module may be non-full and `p` may be a proper support, but the positive sign of its ordinary path Gram is still the same state/positive-functional Gram identity as in the full case.

## 3. Equal-degree KMS scalarization remains tracial on the surviving correlations

Suppose now that `X` carries a compatible dynamics and the path vectors `xi_a` are homogeneous of the same degree. Then the relative coefficients `u_a=<xi_0,xi_a>` are degree zero, hence lie in the fixed-point coefficient algebra. If `phi_beta` is a KMS state for the coefficient dynamics, the KMS boundary relation on fixed analytic elements gives

\[
\phi_\beta(AB)=\phi_\beta(BA).
\tag{14}
\]

Consequently the restriction of `phi_beta` to the C-star algebra generated by the balanced `u_a` is tracial, and (7) becomes a tracial partial-isometry correlation Gram, or a tracial corner-unitary correlation Gram when the sources coincide.

This is the correspondence analogue of the KMS conclusion of `WP-414`, not a stronger no-go theorem about all module dynamics. Active dynamics can change which degree-zero coefficients exist, and varying supports can encode incidence data. The exact point is narrower: once the candidate readout has become an ordinary balanced Hilbert-module Gram, neither non-fullness nor the KMS scalarization makes its positive sign destination-specific.

## 4. A genuinely non-full proper-corner control continuously programs the correlations

The obstruction is visible without any arithmetic source. Let

\[
A=\mathbf C\oplus M_3(\mathbf C),
\qquad
X=\{0\}\oplus M_3(\mathbf C)
\tag{15}
\]

with the standard right action and inner product. This module is genuinely non-full because the ideal generated by its inner products is the proper ideal `{0} direct-sum M_3(C)` of `A`.

Inside the matrix summand put

\[
p=e_{11}+e_{22},
\qquad
q=e_{22}+e_{33},
\qquad
v=e_{21}+e_{32}.
\tag{16}
\]

Then `v^*v=p` and `vv^*=q`. For `theta in R`, let

\[
u_\theta=e^{i\theta}e_{11}+e^{-i\theta}e_{22},
\tag{17}
\]

which is a unitary of the proper corner `pM_3(C)p`, and define

\[
\xi_0=(0,v),
\qquad
\xi_\theta=(0,vu_\theta).
\tag{18}
\]

Both vectors have the same source projection `(0,p)`, and their rank-one compact operators have the same proper range support corresponding to `q`. Take the state

\[
\phi(\lambda,a)=\tfrac13\operatorname{Tr}(a).
\tag{19}
\]

Then each diagonal Gram entry is `2/3`, while

\[
\phi(\langle\xi_0,\xi_\theta\rangle)
=\tfrac13\operatorname{Tr}(u_\theta)
=\tfrac23\cos\theta.
\tag{20}
\]

After normalization by the common diagonal, the two-path Gram is

\[
\widetilde G_\theta
=\begin{pmatrix}
1&\cos\theta\\
\cos\theta&1
\end{pmatrix},
\qquad
\operatorname{spec}(\widetilde G_\theta)
=\{1+|\cos\theta|,1-|\cos\theta|\}.
\tag{21}
\]

Thus a completely nonarithmetic, genuinely non-full module with fixed proper source and range supports already supplies a continuous family of positive common-support Grams, from rank one to the identity. Non-full geometry does not select the correlation spectrum, and positivity survives every choice.

The control also marks the exact survivor. If a source theorem constrains the support projections themselves, forces nontrivial Murray--von Neumann incidence among *different* supports, or determines a distinguished family of partial isometries, that coefficient rigidity is additional data not present in (21). Such a theorem must be tested at the coefficient level; it cannot be inferred from Gram positivity.

## 5. Relation to the current Weil-positivity frontier

This finding narrows the explicit escape left by `WP-414`. In the full passive matrix amplification, common source and range turn relative equal-scale paths into unitaries of the unit-space matrix algebra. Passing to a Hilbert correspondence does not remove the generic-Gram problem. Arbitrary correspondence paths already give (8), and the direct common-range analogue gives partial isometries by (12); common source and range give corner unitaries by (13).

The result does **not** subsume `WP-411`--`WP-414`. `WP-411` concerns cancellation in range projections, `WP-412` the KMS spectral gate, `WP-413` central equal-scale twists, and `WP-414` full-fibre noncentral holonomy. Here the new content is the exact non-full/common-support reduction and the separation between module-induced sign and potentially arithmetic support/incidence data.

For the accepted Bost--Connes conditioning clue, the surviving correspondence branch is therefore more specific than "use a non-full module." It must exploit source-forced **varying support/incidence**, a twisted/projective multiplication whose coefficients are fixed by the arithmetic source, active modular fibre dynamics, or a readout that is not merely a positive-functional scalarization of an `A`-valued Gram. Any positive proposal must still derive the completed finite-prime coefficients including the `log p` factors, the archimedean Gamma contribution, and the polar terms, and then prove the Weil sign on the declared test class.

## 6. Prior-art and novelty audit

The operator-algebraic ingredients are classical. Lance's Hilbert C-star module theory contains the `A`-valued inner product and generalized rank-one operators `theta_{xi,eta}`; positivity of (8) is the elementary scalarization of the module Gram. Non-full Hilbert bimodules and non-saturated Fell-bundle equivalences are standard objects; Abadie--Ferraro is a representative reference explicitly treating Fell bundles without saturation assumptions. Bost--Connes supplies the arithmetic dynamical setting motivating the survivor. The KMS trace property on fixed elements is standard C-star dynamical-systems theory.

No novelty is claimed for any of these general facts. The Mathia-specific contribution is the exact obstruction at the survivor left open by `WP-414`: **ordinary non-full correspondence Grams have universal sign, and the common generalized-range subclass reduces to coefficient partial-isometry correlations, becoming corner-unitary correlations under common source support.** This identifies precisely what non-fullness can still contribute: coefficient/support selection, not a new positive sign theorem.

The internal audit distinguishes the result from the nearest durable findings. `WP-411` treats passive full-rank matrix decoration of projection readouts. `WP-413` treats central equal-scale twists. `WP-414` treats full-fibre noncentral common-bisection paths and explicitly leaves improper/non-full source/range geometry open. None of them gives the Hilbert-module identity (8) as the gate for that survivor or the common-support partial-isometry classification (6). The present result therefore narrows, rather than renames, the surviving branch.

External prior art was also checked against Hilbert-module and non-saturated Fell-bundle literature. The general module identities are standard, and no originality is assigned to them. The durable claim is only their application as a falsification theorem for this exact Weil-positivity mechanism.

## 7. Adversarial boundary and falsification

The universal positivity statement can fail only if the proposed scalarization is not a positive functional, the path pairing is not a Hilbert C-star-module inner product, or the readout is not the ordinary Gram (1). Any of those changes is a legitimate new category, but then positivity must be proved there rather than inherited from this argument.

The common-support classification has additional explicit hypotheses. If `p_a=<xi_a,xi_a>` is not a projection, or if the compact rank-one operators `theta_{xi_a,xi_a}` do not agree, the partial-isometry identities (11)--(13) need not hold. In particular, varying source/range support is **not** ruled out. That is the main remaining correspondence-level falsification surface.

A source-derived family with varying supports would overturn the relevance conclusion only if the resulting incidence fixes the required completed-Weil coefficients in a way that matched nonarithmetic controls cannot reproduce. Likewise, a projective/Fell-bundle multiplication could matter if its cocycle is forced independently by the arithmetic source and survives the novelty tests; merely choosing a cocycle because its Gram has the desired sign would repeat the target-selection problem already exposed elsewhere in the line.

Finally, nothing here proves the Riemann Hypothesis, the Weil criterion, positivity of the finite Weil defect, or existence of the missing Gamma/polar completion. It is a structural no-go for one proposed **mechanism of positivity**. The next useful test is not another common-support Gram, but a concrete source-forced varying-support/incidence model or an orientation-sensitive non-Gram functional with an exact finite-plus-archimedean coefficient identity.