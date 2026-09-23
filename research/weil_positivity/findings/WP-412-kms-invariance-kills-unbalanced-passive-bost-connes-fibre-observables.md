---
id: WP-412
title: KMS invariance kills every scale-unbalanced passive Bost--Connes fibre observable
branch: weil_positivity
status: supported
kind: passive-fibre-kms-spectral-subspace-obstruction
claim_strength: exact RH-independent obstruction for passive full-unitary matrix-decorated Bost--Connes scale eigenoperators; every nonzero-scale spectral word has zero expectation in every positive-temperature KMS state, so pairwise off-diagonal bisection observables have diagonal GNS Gram and only scale-balanced cycles can retain fibre holonomy thermodynamically
created: 2026-09-23
related: [WP-407, WP-408, WP-409, WP-410, WP-411]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
---

# WP-412 — KMS invariance kills every scale-unbalanced passive Bost--Connes fibre observable

## Claim

`WP-411` leaves open the possibility that passive finite-dimensional matrix decoration becomes visible if the sign-bearing construction retains off-diagonal observables such as `V_m^*V_n` instead of collapsing immediately to the range projections `E_n`. At positive temperature, the KMS state itself imposes a further exact filter.

Let `(A,alpha)` be the passive matrix-decorated Bost--Connes system of `WP-411`, with analytic full-fibre unitary bisection elements `V_n` satisfying

\[
V_n^*V_n=1,
\qquad
\alpha_t(V_n)=n^{it}V_n.
\tag{1}
\]

Let `Phi_beta` be any normalized `KMS_beta` state with `beta>0`. Then for `m != n`,

\[
\boxed{\Phi_\beta(V_m^*V_n)=0.}
\tag{2}
\]

More generally, every analytic word `X` which is homogeneous for the scale dynamics,

\[
\alpha_t(X)=q^{it}X,
\qquad q>0,
\tag{3}
\]

has

\[
\boxed{q\neq1\ \Longrightarrow\ \Phi_\beta(X)=0.}
\tag{4}
\]

For a word in the passive scale sections and their adjoints,

\[
X=V_{n_1}^{\varepsilon_1}\cdots V_{n_r}^{\varepsilon_r},
\qquad \varepsilon_j\in\{+1,-1\},
\]

where exponent `-1` denotes the adjoint for the purpose of the scale degree, its thermal expectation can therefore be nonzero only if

\[
\boxed{\prod_{j=1}^r n_j^{\varepsilon_j}=1.}
\tag{5}
\]

In particular, the GNS vectors of the lifted bisection elements themselves satisfy

\[
\langle \pi_\beta(V_m)\Omega_\beta,\pi_\beta(V_n)\Omega_\beta\rangle
=\delta_{mn}.
\tag{6}
\]

Thus the first off-diagonal escape named in `WP-411` is sharply narrower than it appears: **passive fibre information cannot enter a KMS scalar readout through an isolated scale-changing observable. It can survive only in the zero-scale spectral subspace, hence through scale-balanced products/cycles (or after changing the dynamics/state/readout category).**

**Classification:** `CLASSICAL-KMS-INVARIANCE + EXACT-DERIVED-BC-OBSTRUCTION + PASSIVE-FIBRE-DYNAMICS + SPECTRAL-SUBSPACE-SELECTION + OFF-DIAGONAL-PAIRING-COLLAPSE + SCALE-BALANCED-CYCLE-SURVIVOR + NOT-A-CLASSIFICATION-OF-BALANCED-HOLONOMY + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Exact KMS spectral-subspace calculation

A `KMS_beta` state at positive inverse temperature is invariant under its time evolution. Hence

\[
\Phi_\beta(X)=\Phi_\beta(\alpha_t(X))
\]

for every `t`. If `X` obeys (3), then

\[
\Phi_\beta(X)=q^{it}\Phi_\beta(X)
\]

for all real `t`. When `q != 1`, choose `t` with `q^{it} != 1`; equation (4) follows.

For the passive Bost--Connes sections,

\[
\alpha_t(V_m^*V_n)
=m^{-it}n^{it}V_m^*V_n
=\left(\frac nm\right)^{it}V_m^*V_n.
\]

Distinct positive integers have distinct logarithmic scale, so `m != n` implies a nonzero dynamical frequency and therefore (2).

The same argument is multiplicative for arbitrary homogeneous words. Each `V_n` contributes `+log n` and each `V_n^*` contributes `-log n`; the total frequency vanishes exactly when (5) holds. Fixed-point algebra elements may be inserted without changing this degree. Therefore the conclusion is not a peculiarity of length-two words: KMS scalarization projects the passive algebra onto its zero-scale spectral sector before any arithmetic interpretation is attempted.

Finally, (6) follows from (2) off the diagonal and from `V_n^*V_n=1` on the diagonal. This Gram is the identity, not the critical GCD/Poisson Gram of the range-projection vectors in `WP-411`. The two readouts therefore forget the fibre data in different ways: projection readout retains divisibility geometry while cancelling the matrix coefficients; direct bisection-vector readout retains neither cross-scale coherence nor matrix holonomy at first order.

## 2. What remains visible: balanced cycles

The obstruction does **not** say that passive matrix decoration is thermodynamically invisible in every observable. It identifies exactly where visibility can first occur.

A product such as

\[
V_a^*V_bV_c^*V_d
\]

has zero scale degree when `bd=ac`. Such a balanced word lies in the fixed-point spectral subspace and KMS invariance alone does not force its expectation to vanish. Its matrix coefficient may contain an ordered product such as

\[
U_a^*U_bU_c^*U_d,
\]

so noncommutativity or holonomy can in principle survive there. This is precisely compatible with the cycle/holonomy frontier isolated in `WP-407`: phase information requires a closed multiplicative relation rather than a single open edge.

The point is a restriction, not a positive construction. Arbitrary passive matrices can program balanced holonomy, so a nonzero balanced expectation is not yet arithmetic evidence. A viable Weil mechanism would still need the source itself to force the relevant cycle data, retain it in a positive form, survive matched nonarithmetic controls, and supply the archimedean and polar sectors.

## 3. Adversarial controls and boundaries

The statement survives arbitrary choice of finite-dimensional full-unitary coefficients and does not require them to commute. It also does not depend on extremality or uniqueness of the KMS state: every positive-temperature KMS state is invariant under the dynamics, so the spectral-selection argument is state-independent within that class.

Several nearby escapes are outside the theorem rather than counterexamples. Active fibre dynamics can change the scale degree of the decorated section. A non-KMS functional can have nonzero expectation on nonzero spectral subspaces. Operator-valued conditional expectations onto a fixed-point algebra need not erase balanced matrix information. Non-full correspondences may also alter the source/range relations before this calculation is applied. Finally, a finite--archimedean coupling may create new zero-total-energy observables even when each finite component is individually off-shell.

A matched nonarithmetic semigroup system with the same eigenoperator law obeys exactly the same selection rule. Therefore (4) is universal thermal kinematics, not a Riemann-specific sign mechanism. Any proposal that attributes arithmetic orientation merely to the vanishing of unbalanced KMS moments fails this control.

The decisive falsification test is explicit: produce a normalized positive-temperature KMS state and an analytic passive homogeneous observable of nonzero scale degree with nonzero expectation. That would contradict KMS invariance itself. By contrast, a nonzero expectation of a balanced cycle does not falsify the finding; it lands exactly in the surviving sector identified here.

## 4. Prior-art and novelty audit

The two ingredients are classical. KMS-state invariance under the defining one-parameter automorphism group is standard equilibrium C-star-algebra theory, and the Bost--Connes time evolution `alpha_t(mu_n)=n^{it}mu_n` is part of the original Bost--Connes construction. No novelty is claimed for either fact.

The durable contribution is the line-specific consequence for the `WP-411` operator-valued escape: retaining `V_m^*V_n` does not by itself retain passive fibre information after KMS scalarization, because every unequal-scale matrix coefficient is annihilated exactly. The surviving passive-fibre search space is therefore the scale-zero algebra of balanced words/cycles, not the whole off-diagonal algebra.

This is not already the projection obstruction of `WP-411`. There the matrix coefficient cancels algebraically in `V_nV_n^*` before the state is applied, while here the coefficient may remain present in the operator but its nonzero-scale moment is killed dynamically by KMS invariance. Nor does this subsume `WP-407`--`WP-410`: those findings classify gauge/holonomy and source-twist visibility, whereas the present result adds an independent thermodynamic spectral-selection gate.

## Consequence

**Supported exact negative with a precise survivor.** Passive matrix-valued Bost--Connes data cannot contribute to a KMS scalar positivity form through isolated cross-scale moments: the pairwise bisection Gram is exactly diagonal, and every nonzero-scale homogeneous word has zero thermal expectation. Any passive operator-valued continuation of the accepted Bost--Connes clue must therefore work inside the scale-balanced fixed-point sector, where genuine cycle holonomy may survive, or must change one of the hypotheses by introducing source-forced active fibre dynamics, a different state/weight/readout category, a non-full correspondence, altered source/range geometry, or finite--archimedean coupling.

The accepted conditioning clue remains unresolved. This result narrows its surviving operator-valued branch from generic off-diagonal observables to source-forced **balanced** observables whose holonomy is both thermodynamically visible and arithmetically canonical.