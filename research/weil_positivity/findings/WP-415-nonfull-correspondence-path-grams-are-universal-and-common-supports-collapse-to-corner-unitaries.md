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

`WP-414` leaves non-full source/range geometry and correspondence-valued paths as a possible escape from the passive full-fibre Bost--Connes obstruction. The ordinary Hilbert-module Gram part of that escape is nevertheless rigid.

Let `X` be a right Hilbert `A`-module, let `xi_a in X` be finitely many path vectors, and let `phi` be any positive functional on `A`. Define

\[
G_{ab}:=\phi(\langle \xi_a,\xi_b\rangle_A).
\tag{1}
\]

Then `G` is positive semidefinite for every `X`, every path family, and every positive `phi`. Thus non-fullness can constrain **which coefficients occur**, but ordinary scalarized module-Gram positivity cannot by itself supply the missing Weil orientation.

There is a sharper exact reduction for common support. Suppose

\[
p_a:=\langle\xi_a,\xi_a\rangle_A
\tag{2}
\]

is a projection for every `a`, and suppose the generalized rank-one projection

\[
q:=\theta_{\xi_a,\xi_a}\in\mathcal K(X)
\tag{3}
\]

is independent of `a`. Fix a reference path `0` and define the coefficient

\[
r_a:=\langle\xi_0,\xi_a\rangle_A.
\tag{4}
\]

Then

\[
\boxed{r_a^*r_a=p_a,\qquad r_ar_a^*=p_0,\qquad \xi_a=\xi_0r_a,\qquad \langle\xi_a,\xi_b\rangle_A=r_a^*r_b.}
\tag{5}
\]

Hence common-range paths reduce exactly to coefficient-algebra partial-isometry correlations. If all source projections also agree, `p_a=p`, every `r_a` is a unitary in the corner `pAp`, and the scalarized path Gram is a corner-unitary correlation Gram.

**Classification:** `CLASSICAL-HILBERT-CSTAR-MODULE-GRAM-POSITIVITY + EXACT-DERIVED-COMMON-SUPPORT-REDUCTION + NONFULL-CORRESPONDENCE + PARTIAL-ISOMETRY-CORRELATIONS + CORNER-UNITARY-CORRELATIONS + KMS-BALANCED-FIXED-POINT-TRACE + MATCHED-NONARITHMETIC-PROPER-CORNER-CONTROL + NO-NEW-SIGN-FROM-NONFULLNESS-ALONE + COEFFICIENT-SELECTION-MAY-SURVIVE + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Scalarized module Grams are universally positive

For arbitrary scalars `c_a`,

\[
\begin{aligned}
\sum_{a,b}\overline{c_a}G_{ab}c_b
&=\phi\!\left(
\left\langle\sum_a\xi_ac_a,\sum_b\xi_bc_b\right\rangle_A
\right)\\
&\ge0.
\end{aligned}
\tag{6}
\]

No fullness assumption, groupoid model, Bost--Connes arithmetic, KMS state, or dynamics enters this inequality. It is the defining positivity of a Hilbert C-star module followed by a positive functional. Arithmetic content must therefore lie in an additional theorem forcing the **entries** of (1), not in the sign of the Gram itself.

For this research line that coefficient theorem would still have to recover the completed Weil data: the finite prime-power coefficients with their `log p` factors, the archimedean Gamma contribution, the polar terms, and the correct global orientation on the declared test class.

## 2. Common generalized range support forces partial-isometry factorization

Because `p_a` is a projection,

\[
\langle\xi_a-\xi_ap_a,\xi_a-\xi_ap_a\rangle_A
=p_a-p_a^2-p_a^2+p_a^3=0,
\tag{7}
\]

so `xi_a=xi_a p_a`. Therefore

\[
q\xi_a
=\theta_{\xi_a,\xi_a}\xi_a
=\xi_ap_a
=\xi_a.
\tag{8}
\]

Using `q=theta_{xi_0,xi_0}` and (4),

\[
\xi_0r_a
=\theta_{\xi_0,\xi_0}\xi_a
=q\xi_a
=\xi_a.
\tag{9}
\]

The source and range identities follow directly:

\[
\begin{aligned}
r_a^*r_a
&=\langle\xi_a,\xi_0\rangle_A\langle\xi_0,\xi_a\rangle_A
 =\langle\xi_a,q\xi_a\rangle_A=p_a,\\
r_ar_a^*
&=\langle\xi_0,\xi_a\rangle_A\langle\xi_a,\xi_0\rangle_A
 =\langle\xi_0,q\xi_0\rangle_A=p_0.
\end{aligned}
\tag{10}
\]

Finally,

\[
\langle\xi_a,\xi_b\rangle_A
=\langle\xi_0r_a,\xi_0r_b\rangle_A
=r_a^*p_0r_b
=r_a^*r_b.
\tag{11}
\]

If `p_a=p` for all `a`, then `r_a^*r_a=r_ar_a^*=p`, so each `r_a` is a unitary in the unital corner `pAp`. The module may be non-full and the corner proper; the positive sign remains the universal Gram sign of (6).

## 3. Equal-degree KMS scalarization remains tracial

Suppose `X` carries compatible dynamics and the path vectors are homogeneous of the same degree. Then the relative coefficients `r_a=<xi_0,xi_a>` have degree zero and lie in the fixed-point coefficient algebra. For a KMS state `phi_beta`, the KMS boundary relation on fixed analytic elements gives

\[
\phi_\beta(AB)=\phi_\beta(BA).
\tag{12}
\]

Thus `phi_beta` restricts to a trace on the C-star algebra generated by the balanced `r_a`. The readout is a tracial partial-isometry correlation Gram, or a tracial corner-unitary correlation Gram when the sources coincide. This is the correspondence analogue of `WP-414`: KMS scalarization narrows the surviving correlations but does not make their Gram sign arithmetic.

This does not rule out active module dynamics or varying supports. Those can change the coefficient system itself. The obstruction applies once the proposed readout is the ordinary positive-functional scalarization of the Hilbert-module Gram.

## 4. A genuinely non-full proper-corner control programs the correlations

Take

\[
A=\mathbf C\oplus M_3(\mathbf C),
\qquad
X=\{0\}\oplus M_3(\mathbf C)
\tag{13}
\]

with the standard right action and inner product. The module is genuinely non-full because its inner products generate the proper ideal `{0} direct-sum M_3(C)`.

Inside the matrix summand let

\[
p=e_{11}+e_{22},\qquad q=e_{22}+e_{33},\qquad v=e_{21}+e_{32}.
\tag{14}
\]

Then `v^*v=p` and `vv^*=q`. For real `theta`, set

\[
w_\theta=e^{i\theta}e_{11}+e^{-i\theta}e_{22},
\qquad
\xi_0=(0,v),
\qquad
\xi_\theta=(0,vw_\theta).
\tag{15}
\]

Here `w_theta` is a unitary of the proper corner `pM_3(C)p`. Both vectors have source `(0,p)` and the same generalized range support corresponding to `q`. With the state

\[
\phi(\lambda,a)=\tfrac13\operatorname{Tr}(a),
\tag{16}
\]

the diagonal Gram entries are `2/3`, while

\[
\phi(\langle\xi_0,\xi_\theta\rangle)=\tfrac23\cos\theta.
\tag{17}
\]

After normalization by the common diagonal,

\[
\widetilde G_\theta=
\begin{pmatrix}
1&\cos\theta\\
\cos\theta&1
\end{pmatrix},
\qquad
\operatorname{spec}(\widetilde G_\theta)=\{1+|\cos\theta|,1-|\cos\theta|\}.
\tag{18}
\]

Thus a completely nonarithmetic, genuinely non-full proper-corner model already gives a continuous family of positive common-support Grams ranging from rank one to the identity. Positivity survives while the spectrum is freely varied. This matched control shows that non-fullness/common support does not select the desired arithmetic orientation.

## 5. Relation to the current frontier

This finding narrows the explicit escape left by `WP-414`. In the full passive matrix amplification, common source and range turn relative equal-scale paths into unit-space unitaries. Passing to a correspondence does not remove the generic-Gram problem: arbitrary correspondence paths already give (6), common generalized range gives partial isometries, and common source plus range gives corner unitaries.

The result does not subsume `WP-411`--`WP-414`. Those findings concern projection cancellation, the KMS spectral gate, central twists, and full-fibre noncentral holonomy. The new content here is the non-full Hilbert-module gate and the common-support partial-isometry classification.

The surviving correspondence branch is therefore narrower than "use a non-full module." It must exploit source-forced **varying support/incidence**, a source-forced twisted/projective multiplication, active modular fibre dynamics, or a genuinely orientation-sensitive non-Gram readout. Any successful route must still derive the completed finite-plus-archimedean Weil coefficients rather than infer them from generic positivity.

## 6. Prior-art and novelty audit

The operator-algebraic ingredients are classical. Lance's Hilbert C-star module theory supplies the `A`-valued inner product and generalized rank-one operators `theta_{xi,eta}`; positivity of (6) is the elementary scalarization of the module Gram. Non-full Hilbert bimodules and non-saturated Fell-bundle equivalences are standard; Abadie--Ferraro is a representative reference explicitly treating Fell bundles without saturation assumptions. Bost--Connes supplies the arithmetic dynamical setting. The KMS trace property on fixed elements is standard C-star dynamical-systems theory.

No novelty is claimed for those general results. The Mathia-specific contribution is their application at the exact survivor left open by `WP-414`: **ordinary non-full correspondence Grams have universal sign, while the common generalized-range subclass reduces to coefficient partial-isometry correlations and, under common source support, to corner-unitary correlations.** Non-fullness may still select coefficients or incidence; it does not create a new Gram-sign mechanism.

The internal audit distinguishes this from the nearest durable findings. `WP-411` treats passive full-rank matrix decoration, `WP-413` central equal-scale twists, and `WP-414` full-fibre noncentral paths while explicitly leaving improper/non-full source/range geometry open. None gives this Hilbert-module gate or the common-support partial-isometry reduction. The finding therefore narrows rather than renames the remaining branch.

External prior art was checked against Hilbert-module and non-saturated Fell-bundle literature. The general module identities are standard, and no originality is assigned to them. The durable claim is only their use as a falsification theorem for this exact Weil-positivity mechanism.

## 7. Adversarial boundary and falsification

The universal sign statement fails to apply if the scalarization is not positive, the pairing is not a Hilbert C-star-module inner product, or the readout is not the ordinary Gram (1). The common-support classification additionally requires projection-valued source norms and a common generalized rank-one range projection. If these supports vary, the partial-isometry reduction can change materially.

That is the main surviving correspondence-level falsification surface. A source-derived varying-support family would become relevant only if its incidence forces the completed-Weil coefficients in a way that matched nonarithmetic controls cannot reproduce. Likewise, a Fell-bundle cocycle matters only if the arithmetic source fixes it independently of the desired sign; selecting a cocycle because its Gram is positive repeats the target-selection problem.

Nothing here proves the Riemann Hypothesis, the Weil criterion, positivity of the finite Weil defect, or existence of the missing Gamma/polar completion. It is a structural no-go for one mechanism of positivity. The next useful test is a concrete source-forced varying-support/incidence model or an orientation-sensitive non-Gram functional with an exact finite-plus-archimedean coefficient identity.