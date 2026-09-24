---
id: WP-426
title: State-selected modular dynamics makes KMS equilibrium programmable
branch: weil_positivity
status: supported
kind: modular-kms-state-programmability-and-source-selection-obstruction
claim_strength: exact RH-independent source-selection obstruction for unconstrained state-selected modular or interacting KMS dynamics
created: 2026-09-24
related: [WP-254, WP-395, WP-396, WP-397, WP-420, WP-423, WP-424, WP-425]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - M. Takesaki, Theory of Operator Algebras II, Springer, 2003, Chapter VIII, modular automorphism groups and KMS characterization
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, 1997, Section 5.3, KMS states and modular theory
  - Tomita--Takesaki theorem, every faithful normal state is KMS for its own modular automorphism group up to the standard time-sign convention
  - WP-425, arbitrary product-KMS separate invariance and the surviving source-derived interacting/non-product escape
---

# WP-426 — State-selected modular dynamics makes KMS equilibrium programmable

## Claim

`WP-425` closes opposite-frequency compensation for every positive-temperature KMS state of a **fixed decoupled product dynamics**, leaving genuinely source-derived interacting/non-product dynamics and a distinct von Neumann/modular category among the live architectural escapes. There is an exact source-selection gate on that remainder.

Let `M` be a von Neumann algebra and let `phi` be a faithful normal state. Tomita--Takesaki theory canonically associates to the pair `(M,phi)` a modular automorphism group `sigma^phi`. With the standard choice of sign convention, `phi` is a KMS state for that modular flow at unit inverse temperature; reversing/rescaling modular time gives the corresponding statement at any prescribed `beta>0`.

Therefore, if the candidate state is allowed to be chosen first and the dynamics is then declared to be its modular dynamics, **the KMS condition does not select the state at all**. Every faithful normal state passes by construction. The modular group is canonical for the algebra--state pair, but it is not source-selected by the algebra alone.

The finite-dimensional control makes the programmability completely explicit. For every faithful density matrix `rho` on `M_n(C)` and every `beta>0`, define

\[
H_\rho=-\beta^{-1}\log\rho.
\tag{1}
\]

Then

\[
e^{-\beta H_\rho}=\rho,
\qquad
\operatorname{Tr}(e^{-\beta H_\rho})=1,
\tag{2}
\]

so `rho` is exactly the `beta`-KMS/Gibbs state for the inner interacting dynamics

\[
\alpha_t^\rho(x)=e^{itH_\rho}x e^{-itH_\rho}.
\tag{3}
\]

In particular, arbitrary faithful correlated or entangled finite-dimensional states can be made equilibrium states by choosing the interaction after the state. Given any reference Hamiltonian `H_0`, the same construction may be written as an interaction `V_\rho=H_\rho-H_0`; in finite dimension `V_\rho` is bounded.

Hence **"move to an interacting/modular KMS dynamics" is not by itself a source-selection mechanism**. To remain admissible under the `weil_positivity` mandate, the dynamics, modular weight, or interaction must be fixed independently from Bost--Connes/global source data before the desired finite-prime support, Weil coefficients, or sign are inspected. State-selected modular dynamics is a universal matched control and cannot explain the Weil orientation.

This does not rule out a source-forced interacting dynamics or a canonical modular weight. It sharpens what such a proposal must prove: source selection of the dynamics/weight is an independent obligation, not a consequence of the existence of a KMS state.

**Classification:** `CLASSICAL-TOMITA-TAKESAKI + EXACT-DERIVED + NEGATIVE/SOURCE-SELECTION-OBSTRUCTION + STATE-SELECTED-MODULAR-DYNAMICS-UNIVERSAL + FINITE-DIMENSIONAL-GIBBS-PROGRAMMABILITY-CONTROL + INTERACTING-DYNAMICS-NOT-CLOSED-WHEN-SOURCE-FIXED + NOT-A-WEIL-POSITIVITY-PROOF`.

## Modular KMS universality

For a faithful normal state `phi` on `M`, Tomita--Takesaki theory constructs a strongly continuous one-parameter group

\[
\sigma_t^\phi\in\operatorname{Aut}(M).
\]

The modular KMS theorem states that `phi` satisfies the KMS boundary relation for `sigma^phi`, with the sign of modular time depending on convention. Equivalently, after fixing a convention once and for all, for each `beta>0` one obtains a rescaled flow of the form

\[
\alpha_t^{\phi,\beta}=\sigma_{\pm t/\beta}^{\phi}
\tag{4}
\]

for which `phi` is `beta`-KMS.

Conversely, for a faithful normal KMS state of a given von Neumann dynamics, the represented dynamics agrees with the state's modular automorphism group up to the same time normalization. Thus the equilibrium relation is highly constraining when the dynamics is fixed **before** the state, but becomes tautological as a selector when the dynamics may depend on the candidate state.

That direction-of-definition distinction is exactly the one needed here. The surviving branch after `WP-425` cannot be validated by starting from a desired positive functional/correlation pattern and then invoking its modular group as the missing active dynamics. The modular group would merely repackage the already chosen state.

## Finite-dimensional matched control

The matrix-algebra model shows that no specifically arithmetic or Bost--Connes input is needed for this phenomenon. Let `rho>0` with `Tr rho=1`. Functional calculus gives a bounded self-adjoint `log rho`, hence the bounded Hamiltonian (1). Equations (2)--(3) are exact, so every faithful state on a finite matrix algebra is a Gibbs/KMS state of some inner dynamics.

If the Hilbert space is bipartite, `rho` may contain arbitrary full-rank correlations or entanglement. Unless `rho` factorizes in the special way associated with an additive Hamiltonian, `H_rho` is generally non-product and its decomposition relative to a chosen free Hamiltonian contains an interaction term. Thus allowing an unspecified interacting Hamiltonian does not merely enlarge the candidate family a little: at finite dimension it spans the entire faithful state space.

The control also separates faithfulness from the architectural point. A rank-deficient state is not an exact finite-temperature Gibbs state for a bounded full-matrix Hamiltonian, but it becomes faithful after an arbitrarily small admixture of the normalized trace, and exactly the same modular statement applies on its support corner. No conclusion below requires pretending that a nonfaithful full-algebra state has a bounded logarithm.

## Prior-art and novelty audit

The operator-algebra theorem is classical. Tomita--Takesaki modular theory and its KMS characterization are standard material; Takesaki, *Theory of Operator Algebras II*, Chapter VIII, and Bratteli--Robinson, *Operator Algebras and Quantum Statistical Mechanics 2*, Section 5.3, are canonical references. A targeted literature check confirms the standard statement that every faithful normal state is an equilibrium state for its own modular dynamics and that, in matrix algebras, modular evolution is implemented by powers of the density matrix.

The Mathia-specific novelty claim is therefore deliberately narrower: this is a **control/classification result for the live `weil_positivity` architecture**, not a new theorem in modular theory. Repository audit found no prior `weil_positivity` finding using state-selected modular-flow universality as the source-selection obstruction. `WP-395`--`WP-397` analyze frequency sectors relative to a fixed critical KMS/modular structure; they do not allow an arbitrary candidate state to define the dynamics. `WP-420`--`WP-425` analyze fixed product dynamics and progressively remove auxiliary-fibre escapes; `WP-425` explicitly leaves genuinely source-derived interacting/non-product dynamics open.

The nearest conceptual repository control is the broader anti-programming rule already present in the mandate: the object producing positivity must be fixed independently of the target. The present finding turns that principle into an exact theorem for one surviving category. A modular flow chosen from the desired state is mathematically canonical only **after** the target state has been supplied, and hence fails the required direction of source selection.

## Adversarial controls and boundaries

Several boundaries are essential.

1. **This does not rule out fixed source dynamics.** If Bost--Connes, an adelic completion, a boundary construction, or another independently specified source produces a concrete dynamics `alpha` before any target state is selected, then the `beta`-KMS condition for that fixed `alpha` can be highly restrictive. The theorem only kills the freedom to choose `alpha` as a function of the state one wants.

2. **It does not rule out a canonical source-derived modular weight.** A von Neumann algebra together with a distinguished normal semifinite faithful weight may have a meaningful modular flow. The unresolved obligation is to derive that weight from source data and then recover the finite, archimedean, and polar Weil sectors without target coding. Tomita--Takesaki does not provide the distinguished weight from the algebra alone.

3. **Faithfulness is explicit.** The full-algebra theorem above is stated for faithful normal states. Nonfaithful states require support reduction or separate treatment. In finite dimension every genuine finite-temperature Gibbs state for a bounded Hamiltonian is faithful, so this qualification does not weaken the matched control relevant to finite active fibres.

4. **The abelian case is consistent with `WP-424`.** For a faithful normal state on an abelian von Neumann algebra the modular group is trivial. State programmability therefore persists, but there is no nontrivial modular interaction to exploit; this agrees with the earlier commutative-fibre freezing result.

5. **No contradiction with `WP-425`.** The dynamics programmed by a correlated `rho` is generally interacting/non-product. `WP-425` concerns a fixed decoupled product flow and proves separate invariance for its KMS states. The two results meet exactly at the boundary identified there: changing the dynamics can evade the product theorem, but only a source-derived change is admissible.

6. **No contradiction with category-specific perturbation obstructions.** `WP-254` and related findings constrain particular exterior-equivalent/module or bounded-perturbation architectures. The present control does not assert that every state-selected `H_rho` lies in those admissible source classes; it says the opposite methodological point: without an independently imposed source class, arbitrary interacting KMS dynamics is too programmable to carry evidential weight.

A direct falsification test is therefore not to find a faithful state that fails to have a modular flow; Tomita--Takesaki excludes that. The relevant way to escape this obstruction is to exhibit a dynamics or modular weight that is **specified from the arithmetic/global source independently of the desired state**, then prove that its KMS/positive structure recovers the required Weil coefficients and sign.

## Consequence for the live route

After `WP-425`, the phrase "genuinely source-derived interacting/non-product dynamics" is load-bearing. The adjective **source-derived** cannot be dropped. At finite dimension, an unspecified interaction can encode any faithful target state through `H=-beta^{-1}log rho`; at von Neumann level, any faithful normal state supplies its own modular equilibrium dynamics.

Accordingly, the surviving thermodynamic/modular route now has a sharper publication gate. It must first specify the source construction that fixes the dynamics, interaction, weight, or form without looking at the Weil sign. Only after that may KMS equilibrium or modular positivity be used. The construction must still derive the Mangoldt/prime-power coefficients, archimedean Gamma contribution, polar normalization, admissible Weil test space, and an independent sign theorem.

The canonical research mandate remains unchanged. This finding removes a target-programmable interpretation of the surviving modular/interacting escape; it does not prove Weil positivity or RH.