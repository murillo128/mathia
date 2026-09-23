---
id: WP-411
title: Passive matrix Bost--Connes decorations leave the critical projection Gram unchanged
branch: weil_positivity
status: supported
kind: operator-valued-bisection-range-projection-obstruction
claim_strength: exact RH-independent obstruction for finite-rank full-unitary matrix-valued decorations of the canonical Bost--Connes integer bisections with trivial fibre dynamics; despite noncommuting fibre coefficients, source/range projections and their KMS-normalized divisibility Gram remain identical to the scalar carrier, so any surviving operator-valued route must retain off-diagonal fibre data, alter the fibre support/rank or dynamics, or leave this projection readout
created: 2026-09-23
related: [WP-216, WP-409, WP-410]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J. Renault, A Groupoid Approach to C*-Algebras, Lecture Notes in Mathematics 793, Springer, 1980
  - P. S. Muhly and D. P. Williams, Equivalence and disintegration theorems for Fell bundles and their C*-algebras, Dissertationes Math. 456 (2008), 1-57, arXiv:0806.1022
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
---

# WP-411 — Passive matrix Bost--Connes decorations leave the critical projection Gram unchanged

## Claim

`WP-410` proves that arbitrary central `U(1)` twists of the Bost--Connes commensurability groupoid cannot change the canonical critical range-projection/KMS Gram. One remaining route in the current frontier is to replace scalar phases by genuinely operator-valued, potentially noncommuting coefficients.

A broad passive finite-rank subclass can also be excluded exactly.

Let `G_BC` be the Bost--Connes commensurability groupoid and let `B_n` be its canonical integer-scale bisection, with

\[
s(B_n)=\widehat{\mathbf Z},
\qquad
r(B_n)=n\widehat{\mathbf Z}.
\]

Fix a finite-dimensional Hilbert space `H_f` of dimension `d`. In the matrix-amplified groupoid algebra, decorate the section over each `B_n` by a continuous unitary coefficient

\[
U_n(g)\in U(H_f),\qquad g\in B_n,
\]

and denote the resulting bisection-supported element by `V_n`. The coefficients for different scales may be noncentral and need not commute. Assume only that they are unitary on the full fibre, that the support bisections are unchanged, and that the fibre is dynamically passive:

\[
\alpha_t(V_n)=n^{it}V_n.
\tag{1}
\]

Then pointwise unitarity removes the entire matrix decoration from the initial and final projections:

\[
\boxed{
V_n^*V_n=1\otimes I_d,
\qquad
V_nV_n^*=E_n\otimes I_d,
\qquad
E_n:=1_{n\widehat{\mathbf Z}}.
}
\tag{2}
\]

Hence

\[
\boxed{
(E_m\otimes I_d)(E_n\otimes I_d)
=E_{\operatorname{lcm}(m,n)}\otimes I_d.
}
\tag{3}
\]

For every normalized `KMS_beta` state `Phi_beta` for the unchanged scale dynamics,

\[
\boxed{
\Phi_\beta(E_n\otimes I_d)=n^{-\beta}.
}
\tag{4}
\]

Therefore the normalized range-projection vectors have exactly the same Gram as in `WP-216` and `WP-410`:

\[
\boxed{
\langle\xi_m^{(\beta)},\xi_n^{(\beta)}\rangle
=\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta.
}
\tag{5}
\]

At `beta=1`, the local prime block is still

\[
G_{1,p}(a,b)=p^{-|a-b|/2},
\]

so the finite Weil ray remains

\[
W_p=\log p\,(I-G_{1,p}).
\tag{6}
\]

Thus **finite-rank noncommuting unitary coefficients do not by themselves rescue the critical Bost--Connes projection carrier**. Their operator-valued information survives only in observables retained before the range-projection collapse, or if one changes one of the hypotheses that made (2)--(4) rigid.

**Classification:** `CLASSICAL-GROUPOID-MATRIX-AMPLIFICATION + EXACT-DERIVED-BC-OBSTRUCTION + FINITE-RANK-UNITARY-COEFFICIENTS + NONCENTRAL-NONCOMMUTING-ALLOWED + PASSIVE-FIBRE-DYNAMICS + BISECTION-SOURCE-RANGE-RIGIDITY + KMS-MASS-RIGIDITY + CRITICAL-GCD-GRAM-RIGIDITY + OFF-DIAGONAL-OPERATOR-DATA-ONLY + NOT-ARBITRARY-FELL-BUNDLE + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Exact source/range calculation

The statement is intentionally narrower than an arbitrary noncentral Fell-bundle theorem. Work with a fixed matrix fibre `M_d(C)` over the same groupoid and with bisection sections whose coefficient is unitary at every arrow. This already allows genuinely noncommuting matrix data between different scale sections.

For a bisection-supported section, convolution with its adjoint has at most one contributing arrow at each relevant unit. On the source side the coefficient is

\[
U_n(g)^*U_n(g)=I_d,
\]

and on the range side it is

\[
U_n(g)U_n(g)^*=I_d.
\]

The support is therefore the only surviving datum in the initial and final projections. Since `B_n` has full source and range `n Z-hat`, this gives (2) exactly.

No trace on the matrix fibre is being assumed. The coefficient disappears **before** any state is applied: the projection itself is literally the scalar characteristic projection tensored with `I_d`. This is stronger than an argument that would average the matrix coefficient away after scalarization.

Because the surviving projections lie in the scalar unit-space algebra tensored with `I_d`, their intersections are unchanged:

\[
(E_m\otimes I_d)(E_n\otimes I_d)
=1_{m\widehat{\mathbf Z}\cap n\widehat{\mathbf Z}}\otimes I_d
=E_{\operatorname{lcm}(m,n)}\otimes I_d.
\]

Thus noncommutativity of `U_m` and `U_n` can affect products of the lifted **bisection sections**, but it cannot enter the divisibility projection lattice used by the critical carrier.

## 2. KMS normalization is fibre-state independent

Assume the matrix decoration is energetically passive, so the canonical scale eigenoperator law (1) remains exact. Let `Phi_beta` be any normalized `KMS_beta` state on the decorated system for which the `V_n` are analytic. The KMS identity gives

\[
\begin{aligned}
\Phi_\beta(E_n\otimes I_d)
&=\Phi_\beta(V_nV_n^*)\\
&=\Phi_\beta\!\left(V_n^*\alpha_{i\beta}(V_n)\right)\\
&=n^{-\beta}\Phi_\beta(V_n^*V_n)\\
&=n^{-\beta}\Phi_\beta(1\otimes I_d)\\
&=n^{-\beta}.
\end{aligned}
\tag{7}
\]

This does not require the restriction of `Phi_beta` to `M_d(C)` to be tracial or maximally mixed. Full-fibre unitarity has already made the source projection the identity, so normalization alone fixes the last line.

Combining (3) and (7), define

\[
\xi_n^{(\beta)}:=n^{\beta/2}\pi_\beta(E_n\otimes I_d)\Omega_\beta.
\]

Then

\[
\begin{aligned}
\langle\xi_m^{(\beta)},\xi_n^{(\beta)}\rangle
&=(mn)^{\beta/2}
  \Phi_\beta(E_{\operatorname{lcm}(m,n)}\otimes I_d)\\
&=(mn)^{\beta/2}\operatorname{lcm}(m,n)^{-\beta}\\
&=\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta,
\end{aligned}
\]

proving (5).

The mechanism is therefore independent of how noncommuting the matrix coefficients are away from the projection readout. If the proposed positive form is built only from these canonical range projections, their intersections, and their KMS masses, the fibre enlargement is invisible.

## 3. What genuinely survives

The obstruction removes only the **passive full-unitary matrix-decoration** branch. It does not collapse the full operator-valued frontier.

First, off-diagonal observables such as `V_m^*V_n`, ordered products around cycles, commutators, or matrix-valued holonomy can retain the `U(d)` data. Any such proposal must keep those observables alive until the sign-bearing form is constructed rather than project immediately to `E_n`.

Second, a coefficient correspondence with non-full range can behave differently. If the lifted scale element is a partial isometry with a nontrivial fibre source or range projection, then `V_nV_n^*` need not equal `E_n otimes I_d`; the fibre projection can survive into the Gram. This includes genuinely nontrivial Hilbert-module/Fell-bundle correspondences not covered by the present matrix-amplified calculation.

Third, an active fibre dynamics can change the KMS weight. If

\[
\alpha_t(V_n)\neq n^{it}V_n
\]

because the coefficient carries its own modular energy, equation (7) no longer follows. Such a route must derive that additional dynamics from the arithmetic source rather than tune it to the desired Weil sign.

Finally, the theorem says nothing about a finite--archimedean correspondence formed before scalar readout. The research mandate still requires an independently signed global completion, not merely a modified finite Gram.

## 4. Matched control and falsification boundary

The same calculation works for a matched nonarithmetic semigroup/groupoid carrying identical support bisections, passive finite-dimensional fibres, and full-rank unitary coefficients. The projection lattice and KMS masses again forget all matrix decoration.

That clone-stability gives a sharp control: if a proposed arithmetic orientation is claimed to arise solely from passive `U(d)` coefficients while the sign-bearing observable uses only the canonical range projections, the mechanism cannot distinguish the arithmetic system from its matched nonarithmetic copy.

The finding is falsified by an explicit construction satisfying all three passive hypotheses—same `B_n` supports, full-fibre unitary coefficients, and pure scale dynamics (1)—for which either (2), (4), or (5) fails. Conversely, constructions using partial-isometry fibres, active modular dynamics, or off-diagonal matrix observables are outside the theorem rather than counterexamples.

## Representation audit

The primary object is the matrix-amplified Bost--Connes groupoid algebra with finite-dimensional coefficient fibre and unitary bisection sections. The claim does not identify an arbitrary operator-valued Fell bundle with a trivial matrix bundle, and it does not assume that noncommuting coefficient products are scalar or gauge-trivial.

The invariant being classified is specifically the canonical **range-projection/KMS Gram**. The theorem permits the decorated algebra itself, its off-diagonal convolution, and its matrix-valued holonomy to differ substantially from the scalar algebra. Those differences matter only if a candidate positivity mechanism retains them in the sign-bearing form.

Finite dimension is part of the stated boundary. The calculation suggests the same source/range cancellation for suitably bounded full-fibre unitaries on a fixed infinite-dimensional coefficient space, but no such extension is needed here and domain/normalization issues are not being silently folded into this result.

## Prior-art and novelty audit

Groupoid C*-algebras represented on Hilbert bundles and the source/range calculation for bisection-supported sections are standard operator-algebraic background; Renault's groupoid monograph is a foundational reference. Muhly--Williams provides the general Fell-bundle representation/disintegration framework. No novelty is claimed for these structural facts or for matrix amplification itself.

The novelty audit also checked the Bost--Connes/unitary-representation and Fell-bundle literature for an existing statement of this exact carrier classification. The relevant literature studies unitary representations, KMS states, and operator-valued/Fell-bundle structures, but no source was located asserting the present Riemann/Weil-positivity no-go. Accordingly the contribution claimed here is only the **line-specific derived obstruction**: when the `WP-216` Bost--Connes carrier is enlarged by passive full-rank matrix coefficients, all such noncentral information disappears from the canonical projection Gram before scalarization.

This is strictly stronger than `WP-410` in coefficient type but strictly narrower in category: `WP-410` covers arbitrary base-dependent central circle twists over the same groupoid, while the present finding covers noncentral finite-dimensional unitary coefficients only in the passive full-fibre matrix-amplified class. It does not claim to classify arbitrary Fell bundles or correspondences.

## Consequence

**Supported exact negative with a narrower operator-valued survivor.** Merely replacing scalar phases by finite-dimensional noncommuting unitary matrices does not alter the Bost--Connes divisibility range projections, their KMS masses, or the critical GCD/Poisson Gram. Therefore the next operator-valued attempt must do something structurally stronger than passive matrix decoration: retain off-diagonal matrix data into the positive form, introduce a source-forced non-full correspondence, give the fibre an independently derived modular dynamics, alter the underlying source/range geometry, or couple the finite and archimedean sectors before the projection readout.

The accepted Bost--Connes conditioning clue remains unresolved. This finding narrows one of its surviving completion mechanisms but does not supply the required completed Weil form or an independent positivity theorem.
