---
id: WP-423
title: Atomic product-dynamics KMS states force separate invariance
branch: weil_positivity
status: supported
kind: atomic-product-kms-factorization-and-frequency-compensation-obstruction
claim_strength: exact RH-independent obstruction for finite-matrix and countable atomic type-I active fibres under decoupled product dynamics at every positive inverse temperature
created: 2026-09-24
related: [WP-253, WP-412, WP-420, WP-421, WP-422]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary, CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, 1997, standard KMS theory and finite-dimensional Gibbs states
  - WP-253, which classifies a different compact-stabilization product-dynamics route by equivariant KMS Morita theory
---

# WP-423 — Atomic product-dynamics KMS states force separate invariance

## Claim

`WP-421` showed that **joint invariance alone** permits a source Bohr frequency to be cancelled by an opposite active-fibre frequency. `WP-422` then showed that a countable atomic Gibbs fibre can contain all prime logarithmic gaps, so finite spectral capacity is not the decisive obstruction. The stronger KMS condition changes that conclusion for the whole atomic product-fibre class.

Let `(A,alpha)` be a unital C-star dynamical system, let `beta>0`, and let

\[
B=\left(\bigoplus_{j\in J}^{c_0}M_{d_j}(\mathbf C)\right)^\sim
\]

carry a strongly continuous block-preserving dynamics `tau` whose restriction to each matrix block is inner,

\[
\tau_t|_{M_{d_j}}=\operatorname{Ad}(e^{itK_j}).
\]

Equip `A\otimes B` with the decoupled product dynamics

\[
\gamma_t=\alpha_t\otimes\tau_t.
\]

Then **every beta-KMS state `Omega` for `gamma` is separately invariant under both factors**:

\[
\Omega(\alpha_t(a)\otimes b)=\Omega(a\otimes b)
=\Omega(a\otimes\tau_t(b))
\qquad(a\in A,\ b\in B).
\tag{1}
\]

More precisely, on every finite matrix block that has nonzero state mass, the normalized corner of `Omega` factors exactly as

\[
\Omega_j=\phi_j\otimes\psi_{\beta,K_j},
\qquad
\psi_{\beta,K_j}(x)
=\frac{\operatorname{Tr}(e^{-\beta K_j}x)}{\operatorname{Tr}(e^{-\beta K_j})},
\tag{2}
\]

where `phi_j` is a beta-KMS state of `(A,alpha)`. Different central blocks may carry different source KMS states and arbitrary admissible central weights; that freedom does not restore cross-frequency coherence.

Consequently, if `a_omega` is a nonzero source eigenoperator of degree `omega!=0`,

\[
\alpha_t(a_\omega)=e^{it\omega}a_\omega,
\]

then for **every** `b\in B`, including fibre eigenoperators of degree `-omega`,

\[
\boxed{\Omega(a_\omega\otimes b)=0.}
\tag{3}
\]

Thus the Bell-like opposite-frequency compensation allowed by `WP-421` for merely jointly invariant states is impossible in a genuine KMS state for finite-dimensional active fibres and for the countable atomic Gibbs architecture of `WP-422`. Programming all prime logarithmic Bohr frequencies into the auxiliary Hamiltonian is therefore not a KMS escape as long as source and fibre dynamics remain a product.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FINITE-MATRIX-KMS-FACTORIZATION + ATOMIC-C0-SUM-SEPARATE-INVARIANCE + OPPOSITE-BOHR-COMPENSATION-KILLED + WP-422-GIBBS-PROGRAMMABILITY-NOT-A-KMS-JOINING + INTERACTING/NONATOMIC-ESCAPES-REMAIN + NOT-A-WEIL-POSITIVITY-PROOF`.

## Finite-matrix factorization

The key point is elementary and does not require a uniqueness theorem for the source KMS state. First take `B=M_d(C)` and diagonalize

\[
K=\sum_{r=1}^d\kappa_r e_{rr}.
\]

Let `Omega` be a beta-KMS state for `alpha\otimes Ad(e^{itK})`. For entire analytic `x`, use the KMS identity in the convention

\[
\Omega(xy)=\Omega\!\left(y\gamma_{i\beta}(x)\right).
\tag{4}
\]

Fix `r!=s`, take

\[
x=1\otimes e_{ss},\qquad y=a\otimes e_{rs},
\]

with analytic `a\in A`. Since `xy=0`, `gamma_{i\beta}(x)=x`, and `yx=a\otimes e_{rs}`, equation (4) gives

\[
\Omega(a\otimes e_{rs})=0.
\tag{5}
\]

Analytic elements are norm dense, so (5) holds for every `a\in A`. KMS therefore kills all fibre off-diagonal matrix coefficients, even when the **total** product Hamiltonian has degeneracies that would permit such coefficients for a merely invariant state.

For the diagonal weights take

\[
x=1\otimes e_{rs},\qquad y=a\otimes e_{sr}.
\]

Now

\[
xy=a\otimes e_{rr},
\qquad
\gamma_{i\beta}(x)
=e^{-\beta(\kappa_r-\kappa_s)}(1\otimes e_{rs}),
\]

so (4) yields

\[
\Omega(a\otimes e_{rr})
=e^{-\beta(\kappa_r-\kappa_s)}\Omega(a\otimes e_{ss}).
\tag{6}
\]

Define the source marginal

\[
\phi(a)=\Omega(a\otimes1).
\]

The invariant subalgebra `A\otimes1` inherits the KMS identity, hence `phi` is beta-KMS for `(A,alpha)`. Summing (6) over the diagonal gives, with `Z=\sum_r e^{-\beta\kappa_r}`,

\[
\Omega(a\otimes e_{rr})
=\frac{e^{-\beta\kappa_r}}{Z}\,\phi(a).
\tag{7}
\]

Equations (5) and (7) prove

\[
\boxed{\Omega=\phi\otimes\psi_{\beta,K}.}
\tag{8}
\]

No simplicity, factoriality, or uniqueness of source equilibrium was used. Degenerate eigenspaces of `K` cause no exception: (5) still kills their off-diagonal matrix units, while (6) gives equal Gibbs weight inside a degenerate block.

## Countable atomic extension

Return to

\[
B=\left(\bigoplus_{j\in J}^{c_0}M_{d_j}\right)^\sim.
\]

Let `z_j` be the central unit of the `j`-th matrix block. Each `z_j` is fixed by `tau`. If

\[
\lambda_j=\Omega(1\otimes z_j)>0,
\]

then the normalized corner

\[
\Omega_j(X)=\lambda_j^{-1}\Omega((1\otimes z_j)X)
\]

is itself a beta-KMS state on `A\otimes M_{d_j}`. Applying (8) gives

\[
\Omega_j=\phi_j\otimes\psi_{\beta,K_j}
\tag{9}
\]

with `phi_j` beta-KMS, hence alpha-invariant. If `lambda_j=0`, positivity and Cauchy--Schwarz force `Omega` to vanish on that whole block corner.

Therefore for every finite-support `b` in the `c_0` ideal,

\[
\Omega(\alpha_t(a)\otimes b)=\Omega(a\otimes b).
\tag{10}
\]

Finite-support elements are norm dense in the ideal, so (10) extends to all `b` in it. The remaining scalar component is also invariant because `a\mapsto\Omega(a\otimes1)` is a beta-KMS state of `A`. Every element of the unitization is a scalar plus an element of the ideal, proving separate source invariance on all of `B`.

Every KMS state is invariant under its full dynamics. Hence, using joint `gamma`-invariance together with the already proved separate source invariance,

\[
\begin{aligned}
\Omega(a\otimes\tau_t(b))
&=\Omega\!\left(\gamma_t(\alpha_{-t}(a)\otimes b)\right)\\
&=\Omega(\alpha_{-t}(a)\otimes b)\\
&=\Omega(a\otimes b),
\end{aligned}
\tag{11}
\]

which completes (1). Notice what is and is not fixed by this argument. The KMS condition determines the Gibbs density **inside each matrix block**, but it need not determine the central distribution among blocks. `WP-422`'s freedom to prescribe block masses is therefore real. It simply does not create an entangled KMS joining between a nonzero source time degree and the opposite fibre degree.

## Exact consequence for the active-fibre frontier

The distinction between invariance and KMS is now sharp.

`WP-420` established the no-mixing statement after assuming a product/separately invariant scalarization. `WP-421` deliberately weakened this to joint invariance and exhibited the loophole: if source and active fibre carry opposite Bohr frequencies, a tensor can have total degree zero and survive a jointly invariant state. `WP-422` then showed that countably many such fibre frequencies, including every `log p`, are easy to realize in an honest atomic Gibbs fibre.

The present result closes exactly the missing implication for that architecture. The fact that the **fibre by itself** admits a Gibbs state with programmable Bohr spectrum does not mean that the product system admits a KMS state with the frequency-cancelling correlations used by `WP-421`. Equations (5)--(11) show that every product-dynamics KMS state disintegrates blockwise into source KMS states times the canonical finite-dimensional Gibbs state, and therefore is separately invariant.

For a Bost--Connes source eigenoperator `a_omega` of nonzero degree, separate invariance gives

\[
\Omega(a_\omega\otimes b)
=e^{it\omega}\Omega(a_\omega\otimes b)
\]

for all `t`, so (3) follows. Choosing `b` to have degree `-omega` changes the total degree but not this conclusion. In particular, supplying an atomic fibre transition at every prime gap `-log p` cannot turn those transitions into nonzero critical KMS cross-correlations.

This is independent of the common-anchor divergence proved in `WP-422`: even the disjoint prime-dependent sectors that avoid that trace divergence fail to produce the desired KMS mixing under product dynamics. The obstruction occurs one logical step earlier, at the KMS joining itself.

## Prior-art and novelty audit

The finite-dimensional ingredient is classical operator-algebraic statistical mechanics. For a finite matrix algebra with inner dynamics, the beta-KMS state is the Gibbs state, and the matrix-unit calculation above is the standard direct proof. Bratteli--Robinson gives the general KMS framework and finite-dimensional Gibbs theory. No novelty is claimed for finite-dimensional Gibbs uniqueness, the KMS identity, or invariance of KMS states.

A local audit against the Mathia corpus distinguishes this result from the nearest existing controls. `WP-253` uses equivariant Morita theory to show that spatial dynamics on a **compact stabilization** cannot create a missing KMS weight; it does not classify KMS states on a unital source tensored with the atomic active fibre used here. `WP-412` kills unbalanced passive fibre observables by KMS invariance but does not address opposite-frequency compensation. `WP-420` assumes separate invariance, while `WP-421` and `WP-422` explicitly leave the jointly invariant/KMS distinction open.

Accordingly, the durable Mathia delta is not a new general KMS theorem. It is the exact closure of the atomic active-fibre route opened by `WP-421`--`WP-422`: **within decoupled product dynamics, upgrading the jointly invariant frequency-cancelling state to a genuine KMS state forces the correlations back into separately invariant Gibbs blocks and annihilates every nonzero source time degree.**

A bounded external audit across finite-dimensional KMS/Gibbs states, tensor-product equilibrium, and atomic direct sums found the ingredients to be standard rather than a new operator-algebra theorem. The line-specific obstruction and its application to the all-prime active-fibre construction are the new organization established here.

## Adversarial checks and boundary

A tempting counterexample is a pair of two-level systems with opposite energy gaps. Their product Hamiltonian has a degenerate total-energy eigenspace, so a Bell state supported in that eigenspace is jointly invariant and can carry precisely the coherence used in `WP-421`. It is **not** a beta-KMS state for the full matrix algebra at finite beta. Equation (5) exposes the failure directly: KMS forces every off-diagonal fibre coefficient to vanish before total-frequency cancellation can help.

Energy offsets between the matrix blocks do not evade the theorem. Such offsets commute with each whole block and therefore do not alter its inner automorphism group; they may change a represented Gibbs mixture or be encoded as arbitrary central KMS weights, but the normalized state within each nonzero block still has the form (9). Central programmability survives, cross-frequency coherence does not.

The exact scope is deliberately narrower than an assertion about all possible active systems. The theorem assumes a decoupled product dynamics `alpha\otimes tau` and an atomic fibre that is the unitization of a `c_0` sum of finite matrix algebras with block-preserving inner dynamics. It does **not** classify interacting source--fibre dynamics, non-atomic type-I direct integrals, type-II or type-III fibres, continuous central decompositions, or more general von Neumann KMS joinings. Those categories require their own source-derived construction and their own disintegration analysis.

Nor does the result forbid merely jointly invariant non-KMS states: the `WP-421` examples remain valid in exactly that weaker category. It does not prove that a non-atomic or interacting KMS construction exists, and it does not supply the finite/archimedean Weil completion or prove RH.

## Consequence for the Weil-positivity mandate

The active-fibre branch can no longer use the chain

\[
\text{source Bohr mode}
+\text{opposite atomic fibre mode}
\longrightarrow
\text{joint degree zero}
\longrightarrow
\text{KMS correlation}
\]

under a product flow. The first implication is algebraically correct, but the second fails because the KMS boundary condition is stronger than joint invariance and enforces (1)--(3).

A genuine equilibrium continuation must therefore change category in a mathematically meaningful way: derive an **interacting/non-product source--fibre dynamics**, prove a nontrivial KMS joining for a non-atomic fibre not covered above, or abandon KMS and justify why a merely invariant state has an independently source-forced positive Weil interpretation. Any such continuation still has to derive the prime-power/Mangoldt coefficients, archimedean Gamma term, polar normalization, admissible domain, and the correct global sign from one intrinsic object.

`WP-423` supplies none of those missing pieces. It closes the countable atomic product-KMS compensation mechanism so that future work does not mistake programmable auxiliary Bohr support for a source-forced KMS coupling.