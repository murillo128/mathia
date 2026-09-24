---
id: WP-425
title: Finite-temperature product KMS states are separately invariant for arbitrary active fibres
branch: weil_positivity
status: supported
kind: general-product-kms-separate-invariance-and-opposite-frequency-obstruction
claim_strength: exact RH-independent obstruction for arbitrary decoupled product C-star dynamics at every positive inverse temperature
created: 2026-09-24
related: [WP-254, WP-412, WP-420, WP-421, WP-422, WP-423, WP-424]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, 1997, standard analytic KMS boundary identity and invariance
  - C. J. K. Batty, G-central subalgebras, and extensions of KMS states, J. Funct. Anal. 66 (1986), 11-20, adjacent KMS extension/centrality framework
  - WP-420, separate-invariance selection rule and product-state special case
  - WP-423, atomic type-I arbitrary-KMS special case with stronger finite-block factorization
  - WP-424, commutative-fibre special case with stronger GNS freezing
---

# WP-425 — Finite-temperature product KMS states are separately invariant for arbitrary active fibres

## Claim

`WP-420` showed that separate invariance kills compensation between distinct source and auxiliary Bohr frequencies, but deliberately left open a correlated state that is invariant only under the diagonal/product flow. `WP-423` proved that genuine KMS equilibrium restores separate invariance for finite-matrix and countable atomic type-I fibres. `WP-424` closed arbitrary commutative fibres by a stronger central/GNS argument, while leaving genuinely noncentral noncommutative fibres as the remaining decoupled product-dynamics category.

That remaining product-dynamics escape is not real. Let `(A,alpha)` and `(B,tau)` be arbitrary unital C-star dynamical systems and equip a C-star tensor product `A tensor B` with the decoupled product flow

\[
\gamma_t=\alpha_t\otimes\tau_t.
\]

Let `beta>0`, and let `Omega` be any `beta`-KMS state for `gamma`. No product-state, factoriality, type-I, atomicity, commutativity, nuclearity, or finite-dimensionality assumption is imposed on `Omega`, `A`, or `B` beyond the existence of the chosen tensor-product dynamics. Then `Omega` is separately invariant under both factors:

\[
\boxed{
\Omega(\alpha_t(a)\otimes b)=\Omega(a\otimes b)
=\Omega(a\otimes\tau_t(b))
}
\tag{1}
\]

for every `a in A`, `b in B`, and `t in R`.

Consequently, if `a_omega` is a nonzero source Bohr mode,

\[
\alpha_t(a_\omega)=e^{it\omega}a_\omega,
\qquad \omega\ne0,
\]

then

\[
\boxed{
\Omega(a_\omega\otimes b)=0
\quad\text{for every }b\in B.
}
\tag{2}
\]

In particular, an auxiliary observable carrying the opposite frequency cannot revive the source mode, even if `Omega` is correlated or entangled and even if the active fibre is genuinely noncommutative and noncentral. Thus **every finite-temperature KMS state of a decoupled product dynamics obeys the separate-invariance hypothesis of `WP-420`**.

This closes the entire opposite-Bohr-frequency compensation route inside decoupled product KMS dynamics. A surviving thermodynamic construction must change the dynamics itself through a genuinely source-derived interacting/non-product relation, rather than merely enlarge the auxiliary fibre or choose a non-product KMS state for the same product flow.

**Classification:** `CLASSICAL-KMS-ANALYTICITY + EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GENERAL-PRODUCT-KMS-SEPARATE-INVARIANCE + ARBITRARY-NONCOMMUTATIVE-FIBRE + OPPOSITE-BOHR-COMPENSATION-KILLED + WP-423/424-SPECIAL-CASES-SUBSUMED-AT-STATE-LEVEL + INTERACTING-DYNAMICS-REMAIN + NOT-A-WEIL-POSITIVITY-PROOF`.

## Direct KMS proof

Take an entire analytic element `a in A` and arbitrary `b in B`. The two canonical factor copies commute inside the tensor product. Applying the KMS boundary identity to

\[
x=a\otimes1,
\qquad
y=1\otimes b
\]

gives

\[
\begin{aligned}
\Omega(a\otimes b)
&=\Omega\!\left((1\otimes b)\,\gamma_{i\beta}(a\otimes1)\right)\\
&=\Omega\!\left((1\otimes b)(\alpha_{i\beta}(a)\otimes1)\right)\\
&=\Omega(\alpha_{i\beta}(a)\otimes b).
\end{aligned}
\tag{3}
\]

For this fixed pair define the entire scalar function

\[
F(z)=\Omega(\alpha_z(a)\otimes b).
\tag{4}
\]

Since `alpha_z(a)` is again entire analytic, the same KMS calculation applied to `alpha_z(a)` yields

\[
F(z+i\beta)=F(z)
\qquad(z\in\mathbf C).
\tag{5}
\]

Thus `F` has imaginary period `i beta`. It is also bounded on one fundamental horizontal strip. Indeed, writing `z=t+is`, real-time automorphisms are isometric, so

\[
|F(t+is)|
\le \|b\|\,\|\alpha_{t+is}(a)\|
=\|b\|\,\|\alpha_{is}(a)\|.
\tag{6}
\]

The right side is uniformly bounded for `s` in the compact interval `[0,beta]`. Periodicity (5) transports this bound to the whole complex plane. Liouville's theorem therefore makes `F` constant. In particular,

\[
\Omega(\alpha_t(a)\otimes b)=\Omega(a\otimes b)
\qquad(t\in\mathbf R)
\tag{7}
\]

for every entire analytic `a` and arbitrary `b`. Entire analytic elements are norm dense in `A`, so (7) extends to every `a in A`.

Interchanging the two factors gives

\[
\Omega(a\otimes\tau_t(b))=\Omega(a\otimes b)
\tag{8}
\]

for every `a,b,t`, proving (1). Equivalently, one can combine (7) with the standard total-flow invariance of a KMS state to obtain (8).

The proof uses only three ingredients: the KMS imaginary-time boundary identity, commutation of the two tensor factors, and boundedness of real-time C-star automorphisms. It is independent of the internal representation theory of either factor.

## Bohr selection rule and the `WP-420` escape

For an actual Bohr eigenoperator there is an even shorter calculation. If

\[
\alpha_t(a_\omega)=e^{it\omega}a_\omega,
\]

then analytic continuation gives

\[
\alpha_{i\beta}(a_\omega)=e^{-\beta\omega}a_\omega.
\]

Equation (3) becomes

\[
\Omega(a_\omega\otimes b)
=e^{-\beta\omega}\Omega(a_\omega\otimes b).
\tag{9}
\]

For `beta>0` and `omega!=0`, the scalar factor is not one, proving (2) directly.

This is precisely the missing implication in the active-fibre sequence. `WP-420` proved that **if** a state is separately invariant, a fibre frequency `-omega` cannot compensate a source frequency `+omega`. Its Bell-state control showed that mere invariance under the total flow is too weak: a correlated total-invariant state can retain the compensated coherence. The present result shows that such a control cannot be promoted to a positive-temperature KMS state for the same decoupled product dynamics. KMS analyticity supplies the extra imaginary-time constraint that forces separate invariance.

Applied to Bost--Connes, source homogeneous elements have degrees

\[
\sigma_t(\mu_m f\mu_n^*)
=\left(\frac mn\right)^{it}\mu_m f\mu_n^*,
\]

so every nontrivial ratio `m/n` has nonzero frequency `log(m/n)`. Under an arbitrary product-dynamics KMS state, no observable in an auxiliary fibre can carry an opposite energy and preserve a nonzero expectation of that source degree. The cross-ratio coherence needed by the proposed finite--archimedean compensation mechanism is therefore absent before any positivity argument begins.

## Prior-art and novelty audit

The operator-algebra mechanism should be classified as an **elementary consequence of standard KMS theory**, not as a new general theorem about C-star dynamical systems. The analytic KMS boundary identity, density of entire analytic elements, and invariance of KMS states are classical; Bratteli--Robinson is the standard reference. A targeted literature audit also found adjacent work on KMS extensions and central subalgebras, including Batty's 1986 paper, but no reason to claim global novelty for the short tensor-factor argument above.

The Mathia-specific contribution is the closure of an explicitly live branch of the `weil_positivity` search. `WP-423` obtained arbitrary-KMS separate invariance only for an atomic type-I fibre class, using matrix corners and in that class proving stronger factorization. `WP-424` obtained a stronger GNS-triviality statement for arbitrary commutative active fibres by modular/central arguments. Equation (1) shows that the **state-level separate-invariance conclusion needs neither category restriction**: it holds for arbitrary active fibres whenever the dynamics remains a decoupled product.

This result is therefore not evidence for Weil positivity. It is a generic no-go that survives matched nonarithmetic controls automatically. Its value is to remove a falsely surviving architectural degree of freedom: noncommutative fibre richness and state entanglement do not by themselves evade the product-KMS obstruction.

## Adversarial controls and boundaries

Several distinctions are load-bearing.

1. **Nonzero temperature parameter.** The imaginary period is `i beta`. The argument is stated for `beta>0`, the thermodynamic regime relevant here. At `beta=0`, the KMS condition degenerates to a trace condition and does not force the same separate-invariance statement.

2. **Product dynamics, not product state.** No factorization `Omega=phi tensor psi` is assumed or proved. Correlations, mixtures of phases, and nontrivial fixed-point-sector dependence may remain. The theorem only says that those correlations are separately invariant under the two factor flows.

3. **State-level invariance is weaker than the special-category conclusions.** `WP-423` remains stronger on its atomic type-I class because it classifies nonzero finite corners and factors them through canonical Gibbs states. `WP-424` remains stronger for commutative fibres because it makes the nonzero fibre-frequency sector vanish in the KMS GNS representation, not merely in mixed expectations.

4. **Interacting dynamics remain outside the theorem.** If the true source system carries an interaction `gamma_t` that is not a decoupled `alpha_t tensor tau_t`, the commuting-factor KMS calculation does not produce an independent imaginary period for either factor. Such an interaction must itself be source-derived and must survive the exterior-equivalence/Morita-trivial controls already represented by `WP-254`; merely rewriting a product flow in more complicated coordinates is not an escape.

5. **No arithmetic completion is supplied.** Nothing here derives the Mangoldt coefficients, archimedean Gamma term, polar normalization, admissible Weil test space, or global sign. The theorem only closes one auxiliary-frequency mechanism.

A direct falsification test is correspondingly sharp: exhibit `beta>0`, a genuine `beta`-KMS state for a decoupled product flow, and `a,b,t` with

\[
\Omega(\alpha_t(a)\otimes b)\ne\Omega(a\otimes b).
\]

That would contradict the KMS calculation above. A merely total-invariant correlated state, including the Bell-state control of `WP-420`, is not a counterexample.

## Consequence for the live route

The decoupled product-KMS branch is now closed at full C-star generality for the purpose that motivated it. Atomic versus non-atomic, commutative versus noncommutative, finite versus infinite, and product versus correlated **state** are no longer relevant distinctions for opposite-frequency compensation: every positive-temperature KMS state for the product flow is separately invariant.

The live thermodynamic possibility must therefore move to a genuinely different architecture: a source-derived interacting/non-product dynamics or correspondence whose equilibrium relation does not retain the two independent factor symmetries. Alternatively, one may abandon KMS equilibrium and justify a merely invariant or other positive readout by an independently source-forced Weil interpretation. Either route still has to derive the finite Mangoldt coefficients, Gamma sector, polar normalization, test-space/domain, and destination sign rather than programming them.

The canonical research mandate remains unchanged. This finding narrows the admissible architecture; it does not establish Weil positivity or RH.