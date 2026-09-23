---
id: WP-420
title: Decoupled active KMS fibres cannot mix distinct Bost--Connes time degrees
branch: weil_positivity
status: supported
kind: active-fibre-separate-invariance-schur-mask-obstruction
claim_strength: exact RH-independent obstruction for decoupled active tensor-product fibres; separate invariance kills every Gram coefficient whose Bost--Connes or auxiliary dynamical frequency differs, so compensating opposite fibre frequencies do not restore cross-ratio coherence, while product KMS states only Schur-mask the already surviving Bost--Connes Gram blocks
created: 2026-09-23
related: [WP-252, WP-253, WP-254, WP-412, WP-417, WP-418, WP-419]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
  - Standard invariance of KMS states and the tensor-product construction for equal-temperature KMS systems
  - Schur product theorem for positive semidefinite Gram matrices
---

# WP-420 — Decoupled active KMS fibres cannot mix distinct Bost--Connes time degrees

## Claim

`WP-412` proves that a **passive** fibre cannot rescue a scale-unbalanced Bost--Connes observable from KMS invariance, but it deliberately leaves active fibre dynamics open: an auxiliary mode of opposite energy might make the *total* observable time-neutral. That escape has an exact boundary.

Let `(A,alpha)` and `(B,tau)` be C-star dynamical systems, and let `Omega` be a state on `A tensor B` which is invariant under the two factor flows separately,

\[
\Omega\circ(\alpha_t\otimes\mathrm{id})=\Omega,
\qquad
\Omega\circ(\mathrm{id}\otimes\tau_t)=\Omega.
\tag{1}
\]

Take homogeneous elements `a_i in A`, `b_i in B` with

\[
\alpha_t(a_i)=e^{it\omega_i}a_i,
\qquad
\tau_t(b_i)=e^{it\nu_i}b_i.
\tag{2}
\]

For the positive Gram matrix

\[
K_{ij}:=
\Omega\!\left((a_i\otimes b_i)^*(a_j\otimes b_j)\right),
\tag{3}
\]

one has the exact selection rule

\[
\boxed{
K_{ij}\neq0
\quad\Longrightarrow\quad
\omega_i=\omega_j\ \text{and}\ \nu_i=\nu_j.
}
\tag{4}
\]

In particular, choosing the fibre frequencies to compensate the source frequencies,

\[
\nu_i=c-\omega_i
\tag{5}
\]

so that every tensor `a_i tensor b_i` has the same total frequency `c`, does **not** create coherence between distinct source frequencies. If `omega_i != omega_j`, then `K_ij=0` even though the two tensors have identical total degree.

For the important special case of a product state `Omega=phi tensor psi`, where `phi` and `psi` are KMS states at the same inverse temperature for `alpha` and `tau`, the product state is KMS for the product dynamics and is separately invariant. Its Gram factorizes entrywise:

\[
\boxed{
K=G_A\circ G_B,
\qquad
(G_A)_{ij}=\phi(a_i^*a_j),
\qquad
(G_B)_{ij}=\psi(b_i^*b_j),
}
\tag{6}
\]

where `circ` is the Hadamard/Schur product. Both factors are positive semidefinite Grams, hence so is their Schur product. The active auxiliary fibre therefore contributes only a positive correlation mask **inside the source-frequency blocks that already survive**; it cannot join different Bost--Connes time-degree blocks.

Applied to the fixed-ratio critical carriers of `WP-417`--`WP-419`, this means that a decoupled active KMS fibre can Schur-modulate the existing GCD/Haar/phase coefficient Gram inside each fixed ratio, but cannot use opposite auxiliary energies to couple two different Bost--Connes ratios. Thus the natural product-KMS version of the active-fibre escape left by `WP-412` is closed.

**Classification:** `CLASSICAL-KMS-INVARIANCE + EXACT-DERIVED-TENSOR-SELECTION + ACTIVE-BUT-DECOUPLED-FIBRE + PRODUCT-KMS-SCHUR-MASK + NO-CROSS-RATIO-COMPENSATION + MATCHED-NONARITHMETIC-CONTROL + COUPLED-STATE-ESCAPE-REMAINS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Separate invariance is stronger than total energy balance

From (2),

\[
\alpha_t(a_i^*a_j)
=e^{it(\omega_j-\omega_i)}a_i^*a_j.
\]

Applying the first invariance in (1) to (3) gives

\[
K_{ij}
=e^{it(\omega_j-\omega_i)}K_{ij}
\qquad\text{for all }t.
\]

Hence `K_ij=0` unless `omega_i=omega_j`. Repeating the same argument with the second factor gives `K_ij=0` unless `nu_i=nu_j`, proving (4).

This is exactly the distinction that matters for an active auxiliary fibre. Total invariance under `alpha_t tensor tau_t` would only test

\[
(\omega_j-\omega_i)+(\nu_j-\nu_i)=0.
\tag{7}
\]

Opposite auxiliary frequencies can satisfy (7) even when the source frequencies differ. Separate invariance instead tests the two differences independently. Therefore the obstruction is not that compensation is algebraically impossible; it is that **decoupled equilibrium scalarization retains the independent factor symmetries and projects away the compensated cross-frequency coherence**.

For product KMS states the hypotheses are automatic. Every KMS state is invariant under its own dynamics, so `phi tensor psi` is separately invariant. On analytic elementary tensors the KMS boundary relation also factorizes, showing directly that equal-temperature product KMS states are KMS for `alpha tensor tau`. No Bost--Connes-specific input is used in this step.

## 2. Product KMS readout is only a Schur mask

For a product state,

\[
\begin{aligned}
K_{ij}
&=(\phi\otimes\psi)
\left((a_i^*a_j)\otimes(b_i^*b_j)\right)\\
&=\phi(a_i^*a_j)\,\psi(b_i^*b_j),
\end{aligned}
\]

which is (6). The Schur product theorem then gives positivity without any arithmetic input.

This has two consequences that should not be conflated. First, an auxiliary fibre may still change the numerical Gram *within* a surviving block, sometimes substantially. If the auxiliary correlations are themselves source-forced, that within-block modification could be meaningful and is not ruled out here. Second, no choice of a **decoupled product** fibre can repair missing coherence between different source-frequency blocks, because a zero entry of `G_A` forced by source KMS invariance remains zero after the Schur product.

For the Bost--Connes time evolution,

\[
\sigma_t(\mu_m f\mu_n^*)
=\left(\frac mn\right)^{it}\mu_m f\mu_n^*,
\qquad f\in C^*(\mathbf Q/\mathbf Z),
\tag{8}
\]

so the source frequency is `log(m/n)`. The critical fixed-ratio rays used in `WP-417`, `WP-418`, and `WP-419` lie in a single such spectral block. Their existing GCD envelope, character-compatibility masks, or arbitrary-coefficient Haar correlations may therefore be multiplied by an auxiliary positive Gram. But two distinct ratios `m/n` and `m'/n'` remain orthogonal under every separately invariant readout, even if the fibre contributes frequencies chosen so that both total tensors have degree zero.

This is the precise sense in which active product fibres fail to provide the missing finite--archimedean bridge: they can decorate a block, but they cannot make the finite and auxiliary energies cancel *coherently across source blocks*.

## 3. Sharp boundary: coupled total-invariant states can evade the theorem

The separate-invariance hypothesis is essential, and a finite-dimensional control shows that the surviving escape is real rather than verbal. Take `A=B=M_2`. Let

\[
\alpha_t=\operatorname{Ad}\!\begin{pmatrix}1&0\\0&e^{it\omega}\end{pmatrix},
\qquad
\tau_t=\operatorname{Ad}\!\begin{pmatrix}1&0\\0&e^{-it\omega}\end{pmatrix}.
\tag{9}
\]

The Bell vector

\[
\xi=\frac{|00\rangle+|11\rangle}{\sqrt2}
\]

is fixed by the **total** unitary implementing `alpha tensor tau`, so its vector state is invariant under the total flow. It is not invariant under the two factor flows separately. If

\[
x_1=1\otimes1,
\qquad
x_2=E_{10}\otimes E_{10},
\]

then the two factors of `x_2` have frequencies `+omega` and `-omega`, while `x_2` has total frequency zero, and

\[
\langle\xi,x_2\xi\rangle=\frac12\neq0.
\tag{10}
\]

Thus a genuinely coupled state can retain exactly the compensated coherence forbidden by (4). The theorem therefore does **not** justify discarding active fibres altogether. It identifies what such a construction must abandon: independent factor equilibrium/invariance.

For the Weil-positivity mandate, that is useful information. A viable finite--archimedean mechanism cannot merely tensor a Bost--Connes KMS system with an independent thermal auxiliary system and tune opposite frequencies. It needs a source-forced coupling that changes the state, dynamics, algebraic relation, conditional readout, or scalarization so that only the **joint** symmetry survives and the resulting cross-frequency terms are canonical rather than programmable.

## 4. Adversarial controls, prior art, and novelty

The result passes the matched nonarithmetic control in the strongest possible way: (4) holds for arbitrary C-star dynamical systems satisfying (1). Hence neither the selection rule nor the Schur positivity of (6) can itself be the arithmetic sign mechanism sought by this research line. They are generic equilibrium kinematics. Arithmetic content can only enter through the source Gram that survives, through a source-forced auxiliary Gram, or through a non-decoupled coupling outside the theorem.

The ingredients are classical. KMS-state invariance, product KMS states at equal temperature, and the Schur product theorem are standard; equation (8) is part of the original Bost--Connes dynamics. No novelty is claimed for those facts. A targeted prior-art audit of tensor-product/KMS and Bost--Connes equilibrium constructions found the expected general theory but no result turning this generic factorization into a source-native Weil sign.

The durable contribution is the line-specific closure of an explicitly live escape. `WP-412` rules out passive fibres but leaves active compensating dynamics open. `WP-252`--`WP-254` address equivariant stabilization/Morita-type couplings in a different category, while `WP-417`--`WP-419` classify the critical fixed-ratio Bost--Connes Grams themselves. The present finding isolates the intermediate case: **active but decoupled** auxiliary dynamics with separate equilibrium symmetries. In that class, compensation of total energy is insufficient and the product-KMS readout is exactly a Schur mask of the old source blocks.

A direct falsification test is available. Under hypotheses (1)--(2), exhibit `i,j` with `omega_i != omega_j` or `nu_i != nu_j` and `K_ij != 0`; this would contradict factor invariance. By contrast, a coupled state invariant only under the diagonal/product flow is not a counterexample and is deliberately left open, as the control (9)--(10) demonstrates.

## Consequence

**Supported exact negative with a sharper survivor.** The active-fibre branch of the accepted Bost--Connes conditioning clue splits cleanly. Decoupled/product KMS fibres cannot mix distinct Bost--Connes time degrees: they only Schur-mask the Gram structure already present inside each surviving spectral block. The remaining viable branch must use a genuinely coupled finite--archimedean equilibrium object or another source-forced operation that breaks separate factor invariance while preserving a canonical positive readout.

The canonical Weil-positivity mandate remains unchanged. This finding does not supply its sign theorem; it removes a natural generic construction that would otherwise look like a finite--archimedean compensation mechanism without actually creating source-frequency coherence.