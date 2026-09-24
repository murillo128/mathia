---
id: WP-424
title: Finite-temperature KMS dynamics is GNS-trivial on commutative active fibres
branch: weil_positivity
status: supported
kind: central-kms-freezing-and-nonatomic-commutative-frequency-compensation-obstruction
claim_strength: exact RH-independent obstruction for arbitrary commutative active fibres at every positive inverse temperature, with a stronger central-subalgebra formulation
created: 2026-09-24
related: [WP-253, WP-420, WP-421, WP-422, WP-423]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - M. Takesaki, Tomita's Theory of Modular Hilbert Algebras and its Applications, Lecture Notes in Mathematics 128, Springer, 1970, modular automorphism group and KMS boundary condition
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, 1997, standard KMS representation theory
  - WP-423, which proves separate invariance for a different noncommutative atomic product-fibre class by matrix-corner factorization
---

# WP-424 — Finite-temperature KMS dynamics is GNS-trivial on commutative active fibres

## Claim

`WP-421` showed that joint invariance alone can preserve a Bost--Connes source Bohr mode by pairing it with an opposite auxiliary frequency. `WP-422` removed finite spectral capacity as the decisive obstruction by programming all prime logarithmic gaps into a countable Gibbs fibre. `WP-423` then proved that genuine KMS equilibrium kills this compensation for finite-matrix and countable atomic type-I product fibres.

The non-atomic **commutative** branch is obstructed even more rigidly.

Let `(A,alpha)` be a unital C-star dynamical system, let `(B,tau)` be a unital **commutative** C-star dynamical system, and equip `A tensor B` with the product flow

\[
\gamma_t=\alpha_t\otimes\tau_t.
\]

Let `beta>0`, and let `Omega` be a beta-KMS state for `gamma`, with GNS representation `(pi_Omega,H_Omega,xi_Omega)`. Then the entire fibre dynamics is trivial in the GNS quotient:

\[
\boxed{
\pi_\Omega(1\otimes\tau_t(b))=\pi_\Omega(1\otimes b)
\quad(t\in\mathbf R,\ b\in B).
}
\tag{1}
\]

Consequently `Omega` is separately invariant under both factors,

\[
\Omega(a\otimes\tau_t(b))=\Omega(a\otimes b)
=\Omega(\alpha_t(a)\otimes b),
\tag{2}
\]

and every nonzero fibre Bohr mode is actually GNS-null. In particular, if

\[
\alpha_t(a_\omega)=e^{it\omega}a_\omega,\qquad \omega\ne0,
\]

then for every `b in B`, including an opposite-frequency fibre mode,

\[
\boxed{\Omega(a_\omega\otimes b)=0.}
\tag{3}
\]

Thus replacing the atomic active fibres of `WP-423` by an arbitrary continuous/non-atomic commutative fibre does **not** reopen the opposite-frequency KMS joining route. A surviving auxiliary KMS mechanism must use genuinely noncentral noncommutative fibre degrees of freedom, or leave the decoupled product architecture in a way not already covered by the Morita/exterior-equivalence obstruction of `WP-254`.

The core statement is more general than the tensor-product application: at nonzero inverse temperature, an invariant central C-star subalgebra of a KMS system is represented with **trivial time evolution** in the KMS GNS representation.

**Classification:** `CLASSICAL-KMS/MODULAR-FACT-SPECIALIZATION + EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CENTRAL-SUBALGEBRA-GNS-FREEZING + COMMUTATIVE-NONATOMIC-FIBRE-CLOSED + OPPOSITE-BOHR-COMPENSATION-KILLED + NONCOMMUTATIVE-NONATOMIC/INTERACTING-ESCAPES-REMAIN + NOT-A-WEIL-POSITIVITY-PROOF`.

## Direct KMS derivation

The result can be proved directly from the KMS boundary identity, without assuming that `Omega` is faithful and without passing first to a faithful normal state on a support corner.

Write `C=A tensor B`. Let `c in C` be central and entire analytic for `gamma`. For every entire analytic `x in C`, the KMS identity in the convention used in `WP-423` gives

\[
\Omega(cx)=\Omega\!\left(x\,\gamma_{i\beta}(c)\right).
\tag{4}
\]

Because `c` is central, `cx=xc`. Hence

\[
\Omega\!\left(x[c-\gamma_{i\beta}(c)]\right)=0
\qquad(x\in C_{\rm an}).
\tag{5}
\]

Set

\[
d=c-\gamma_{i\beta}(c).
\]

The complex-time image of a central entire analytic element remains central: it commutes with the dense analytic subalgebra, hence with all of `C`. Thus `d` is central and analytic. Taking `x=d^*` in (5) yields

\[
\Omega(d^*d)=0.
\tag{6}
\]

Therefore `pi_Omega(d)xi_Omega=0`. Centrality upgrades this cyclic-vector nullity to operator nullity: for every `y in C`,

\[
\pi_\Omega(d)\pi_\Omega(y)\xi_\Omega
=\pi_\Omega(y)\pi_\Omega(d)\xi_\Omega=0.
\]

Since `pi_Omega(C)xi_Omega` is dense,

\[
\pi_\Omega(c)=\pi_\Omega(\gamma_{i\beta}(c)).
\tag{7}
\]

Apply the same argument to `gamma_t(c)` for every real `t`. If

\[
F(z)=\pi_\Omega(\gamma_z(c)),
\]

then `F` is an entire operator-valued function and

\[
F(t)=F(t+i\beta)\qquad(t\in\mathbf R).
\tag{8}
\]

The identity theorem gives `F(z)=F(z+i beta)` for every complex `z`. Hence `F` is periodic in the imaginary direction. For `z=x+iy`, use real-time isometry and contractivity of `pi_Omega`:

\[
\|F(x+iy)\|
\le \|\gamma_{iy}(c)\|.
\tag{9}
\]

By imaginary periodicity it is enough to take `y` in a compact interval of length `beta`; the right-hand side is then uniformly bounded by norm continuity of the analytic orbit. Thus `F` is a bounded entire Banach-space-valued function. Scalarizing by bounded linear functionals and applying Liouville shows that `F` is constant. Therefore

\[
\pi_\Omega(\gamma_t(c))=\pi_\Omega(c)
\qquad(t\in\mathbf R)
\tag{10}
\]

for every central entire analytic `c`. Gaussian analytic smoothing and norm density extend (10) to every element of an invariant central C-star subalgebra.

For the product system with commutative `B`, the subalgebra `1 tensor B` is central and gamma-invariant, so (10) is exactly (1).

## Separate invariance and the frequency obstruction

Every positive-temperature KMS state is invariant under the total flow `gamma`. Combining total invariance with (1) gives, for all `a in A`, `b in B`,

\[
\begin{aligned}
\Omega(\alpha_t(a)\otimes b)
&=\Omega\!\left(\gamma_t(a\otimes\tau_{-t}(b))\right)\\
&=\Omega(a\otimes\tau_{-t}(b))\\
&=\Omega(a\otimes b).
\end{aligned}
\tag{11}
\]

This proves separate source invariance; separate fibre invariance is already stronger at the representation level by (1).

If `b_nu` is a fibre eigenoperator,

\[
\tau_t(b_\nu)=e^{it\nu}b_\nu,
\]

then (1) gives

\[
(e^{it\nu}-1)\pi_\Omega(1\otimes b_\nu)=0.
\]

For `nu!=0`, choose `t` with `e^{it nu}!=1`; then

\[
\pi_\Omega(1\otimes b_\nu)=0.
\tag{12}
\]

So a commutative active fibre does not merely fail to contribute a nonzero expectation at an opposite Bohr frequency: its entire nonzero-frequency sector disappears in the KMS GNS quotient. Equation (3) follows immediately from separate source invariance.

## Prior-art and novelty audit

The abstract mechanism is **classical**, not a new theorem of operator algebras. Tomita--Takesaki theory identifies finite-temperature KMS dynamics in the GNS von Neumann algebra with the modular automorphism group after rescaling, and the modular group fixes the center pointwise. Takesaki's 1970 monograph and Bratteli--Robinson give the standard framework. The derivation above is an elementary C-star/KMS proof specialized so that non-faithful-state support issues do not obscure the exact statement needed here.

The Mathia-specific contribution is the placement of that classical fact on the live `weil_positivity` frontier. `WP-421` left opposite-frequency joint invariance open; `WP-422` showed countably many programmed fibre frequencies are cheap; `WP-423` closed the atomic type-I KMS realization but explicitly left non-atomic/direct-integral and continuous-center fibres as possible categories. The present result closes the **purely commutative non-atomic/continuous-center** version of that escape exactly. It does not claim novelty for the modular-center theorem itself.

No Riemann zeros, RH, Weil positivity, or desired sign were used. The obstruction is source-independent and therefore passes the zero-data-removal control in the line contract.

## Adversarial controls and boundaries

The following limits are load-bearing.

1. **Positive inverse temperature.** The argument uses a nonzero imaginary KMS period. It does not classify the degenerate `beta=0` trace condition.

2. **Centrality, not merely infinite dimension.** The proof applies because `1 tensor B` is central when `B` is commutative. It does not extend to a noncommutative non-atomic fibre merely because that fibre has a large center. It only freezes the central part; noncentral direct-integral fibres may still carry compensating Bohr modes.

3. **Product structure for separate source invariance.** The central-freezing lemma itself is more general and applies to any invariant central subalgebra of a KMS system. Product dynamics is used in (11) to convert that freezing plus total invariance into separate source invariance. A genuinely interacting architecture that changes the relevant noncentral correspondence remains outside this finding; bounded exterior-equivalent/Morita-trivial versions are already constrained by `WP-254`.

4. **No hidden global completion.** The theorem supplies no Mangoldt coefficient, archimedean Gamma term, polar normalization, or Weil sign. It only removes an auxiliary-frequency mechanism. Any surviving route still has to derive all of those features from source geometry before positivity is identified, as required by the canonical research mandate.

5. **No contradiction with `WP-421`.** `WP-421` constructed/allowed compensated coherences under mere joint invariance. KMS is strictly stronger. The disappearance of commutative fibre Bohr modes in (12) is precisely the additional equilibrium constraint.

## Consequence for the live route

A non-atomic auxiliary fibre is not enough. If its active degrees of freedom remain central/commutative, finite-temperature KMS equilibrium freezes them in the physical GNS quotient, so they cannot repair the mixed-prime or opposite-frequency obstruction by carrying the missing prime logarithmic phases.

The thermodynamic escape therefore narrows to a genuinely different category: noncommutative non-atomic fibres with noncentral active modes, or an interacting/source-derived correspondence whose KMS structure is not a decoupled product and is not exterior-equivalent to the already-closed coefficient systems. Even there, support richness alone is irrelevant; the construction must still force the exact arithmetic coefficients and global Weil completion independently of the desired sign.
