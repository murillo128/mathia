---
id: WP-429
title: Coherent KMS sandwiches are state-universal on finite Gibbs truncations
branch: weil_positivity
status: triage
kind: bost-connes-kms-coherent-sandwich-programmability
claim_strength: exact finite-dimensional programmability control with fixed dynamics and fixed faithful KMS state; arbitrary coherent sandwich freedom realizes every positive functional and can orient every nonzero zero-mode-free self-adjoint defect either way
created: 2026-09-24
related: [WP-225, WP-419, WP-426, WP-428]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - K. Kraus, States, Effects, and Operations: Fundamental Notions of Quantum Theory, Lecture Notes in Physics 190, Springer, 1983
  - G. K. Pedersen and M. Takesaki, The Radon-Nikodym theorem for von Neumann algebras, Acta Math. 130 (1973), 53-87, DOI 10.1007/BF02392262
---

# WP-429 — Coherent KMS sandwiches are state-universal on finite Gibbs truncations

## Claim

`WP-428` leaves coherent nonhomogeneous sandwiches `a \mapsto \Omega(b^*ab)` as a genuine cross-frequency escape from the Bohr-diagonal no-go. On a finite faithful Gibbs system, however, **unrestricted choice of the coherent sandwich operator is already completely programmable even when the dynamics and KMS state are held fixed**.

Let

\[
A=M_n(\mathbb C),\qquad
\alpha_t(a)=e^{itH}ae^{-itH},\qquad
\omega_\rho(a)=\operatorname{Tr}(\rho a),
\]

where `H=H^*` and `\rho=Z^{-1}e^{-\beta H}>0`. Thus `\omega_\rho` is the faithful `\beta`-KMS state for the fixed inner dynamics. For every positive functional

\[
\varphi_\sigma(a)=\operatorname{Tr}(\sigma a),\qquad \sigma\succeq0,
\]

define

\[
b=\sigma^{1/2}\rho^{-1/2}.
\tag{1}
\]

Then

\[
b\rho b^*=\sigma
\]

and hence

\[
\boxed{
\omega_\rho(b^*ab)=\varphi_\sigma(a)
\quad\text{for every }a\in M_n(\mathbb C).
}
\tag{2}
\]

Every matrix is entire analytic for `\alpha` and has a finite decomposition into Bohr sectors of the fixed Hamiltonian. Therefore requiring `b` to be analytic, or merely to be a finite coherent sum of Bohr-homogeneous pieces, does not reduce this universality in finite dimension.

A direct consequence is a sign-programmability theorem. If `W=W^*\ne0` has zero time-average,

\[
E_0(W):=\lim_{T\to\infty}\frac1T\int_0^T\alpha_t(W)\,dt=0,
\tag{3}
\]

then `\operatorname{Tr}W=0`; hence `W` has both a positive and a negative eigenvalue. There exist density matrices `\sigma_+` and `\sigma_-`, and corresponding coherent analytic sandwiches `b_+`, `b_-`, such that

\[
\boxed{
\omega_\rho(b_+^*Wb_+)>0,
\qquad
\omega_\rho(b_-^*Wb_-)<0.
}
\tag{4}
\]

Thus the surviving category in `WP-428` is not evidence for Weil orientation merely because cross-frequency interference can produce a nonzero invariant scalar. Unless the admissible coherent operator `b` is fixed or sharply constrained by arithmetic source data **before the target sign is inspected**, the finite Gibbs readout can realize either sign at will.

## Exact finite-dimensional factorization

Equation (2) is elementary. Cyclicity of the matrix trace gives

\[
\begin{aligned}
\omega_\rho(b^*ab)
&=\operatorname{Tr}(\rho b^*ab)\\
&=\operatorname{Tr}(b\rho b^*a)\\
&=\operatorname{Tr}(\sigma a).
\end{aligned}
\tag{5}
\]

Faithfulness of `\rho` is the only ingredient needed to form the bounded inverse `\rho^{-1/2}`. No change of Hamiltonian, modular flow or KMS state is involved. This is therefore a different programmability mechanism from `WP-426`: there the desired state was encoded by rebuilding the dynamics, whereas here the **same fixed Gibbs pair `(\alpha,\omega_\rho)`** supports every positive functional through the choice of one sandwich operator.

If one insists that a single Kraus operator be contractive, take

\[
c=\lambda b,
\qquad 0<\lambda\le \|b\|^{-1}.
\tag{6}
\]

Then `c^*c\preceq I` and

\[
\omega_\rho(c^*ac)=\lambda^2\varphi_\sigma(a).
\tag{7}
\]

The scalar factor does not change the sign of a self-adjoint observable, and it disappears under ordinary postselection normalization. Contractivity by itself therefore does not remove the sign-programmability control. There is, however, a genuine stronger restriction: if `c` is contractive and one also requires the *unnormalized* operation to satisfy `\omega_\rho(c^*c)=1`, faithfulness forces `c^*c=I`. In that deterministic single-Kraus subclass the reachable states are only unitary/isometric orbit states, not all density matrices.

## Why coherence is exactly the programmable resource

Write the finite Bohr decomposition of `b` as

\[
b=\sum_\nu b_\nu,
\qquad
\alpha_t(b_\nu)=e^{i\nu t}b_\nu.
\tag{8}
\]

For a source mode `a_\omega`,

\[
b^*a_\omega b
=\sum_{\nu,\mu}b_\nu^*a_\omega b_\mu,
\]

and the summand indexed by `(\nu,\mu)` has total frequency

\[
\omega+\mu-\nu.
\tag{9}
\]

The invariant state can retain precisely the cross terms with `\nu-\mu=\omega`. This is the survivor isolated by the matched control in `WP-428`.

The present theorem shows that, in a finite faithful Gibbs block, allowing those coherent amplitudes without a source-derived rule gives enough freedom to realize an **arbitrary target density matrix**. By contrast, if `b` is homogeneous, then `b\rho b^*` is invariant under the flow and every nonzero source mode is killed, exactly recovering `WP-428`. If `b` commutes with `H`, the same invariant collapse occurs. The transition from the obstruction to universality is therefore not generic noncommutativity but unrestricted **relative coherence between distinct Bohr sectors**.

## Finite Bost-Connes control

This programmability occurs on a matched finite control carrying the exact retained critical Bost-Connes coefficients. Fix a finite prime set `F` and cutoffs `N_p\ge2`. Put

\[
\mathcal K_{F,N}=\bigotimes_{p\in F}\mathbb C^{N_p},
\qquad
H_{F,N}=\sum_{p\in F}(\log p)N_p,
\tag{10}
\]

where `N_p` is the number operator on the `p`-factor, and let

\[
\rho_{F,N}=Z^{-1}e^{-H_{F,N}}>0.
\tag{11}
\]

Let `S_{p,N_p}` be the truncated unilateral shift in the `p`-factor. The finite compression of the critical nonarchimedean defect is

\[
W_{F,N}
=-\sum_{p\in F}(\log p)
  \sum_{k=1}^{N_p-1}p^{-k/2}
  \left(S_{p,N_p}^{k}+S_{p,N_p}^{*k}\right).
\tag{12}
\]

Every retained coefficient in (12) is the exact critical coefficient `-(\log p)p^{-k/2}` from the finite-prime defect of `WP-428`. Every summand has nonzero Bohr frequency `\pm k\log p`, so

\[
E_0(W_{F,N})=0.
\tag{13}
\]

For nonempty `F`, the matrix is nonzero and self-adjoint. Equations (2)--(4) therefore give coherent analytic operators `b_+` and `b_-` with

\[
\omega_{\rho_{F,N}}(b_+^*W_{F,N}b_+)>0,
\qquad
\omega_{\rho_{F,N}}(b_-^*W_{F,N}b_-)<0.
\tag{14}
\]

This is a **matched programmability control**, not an exact finite-dimensional representation of the full Bost-Connes algebra: truncating the unilateral shifts breaks the infinite isometry relations and removes shells above the cutoff. Its role is narrower and decisive. Any proposed argument that treats an arbitrary coherent KMS sandwich as a canonical positive orientation must already distinguish itself on these finite faithful Gibbs controls; otherwise the sign is supplied by the chosen sandwich rather than by the arithmetic source.

## Prior-art and novelty audit

No novelty is claimed for the matrix factorization (1)--(5), for single-Kraus quantum operations, or for the general idea of Radon-Nikodym comparison of positive functionals. Kraus's *States, Effects, and Operations* is a standard source for positive quantum operations and their operator representations. Pedersen--Takesaki gives the classical noncommutative Radon-Nikodym framework for weights subject to modular invariance; the unrestricted finite-dimensional formula used here is simpler and does **not** assert the modular-invariant derivative conclusion of that theorem.

The Mathia-specific delta is the classification of the exact escape left open by `WP-428`. `WP-419` shows programmability of arbitrary Bost-Connes phase coefficients in a Haar/character construction. `WP-426` shows programmability when the equilibrium flow is reconstructed from the desired state. The present result needs neither move: **the flow and faithful KMS state remain fixed**, while one freely chosen nonhomogeneous coherent sandwich already ranges over all positive functionals on every finite Gibbs control. Consequently every nonzero zero-mode-free finite defect is sign-programmable.

This does not prove that a source-derived coherent correspondence is impossible. It proves that coherence alone has no evidentiary value: source canonicity must be established before the sign calculation, and the admissible class must be narrow enough to break the state-universality mechanism above.

## Boundary conditions and falsification

Faithfulness and finite dimensionality are load-bearing for the exact universal statement. If `\rho` is not faithful, `\rho^{-1/2}` is unavailable on its kernel and not every target support is reachable by a bounded sandwich. In infinite dimension, relative densities may be unbounded and domain/affiliation issues re-enter; equation (1) must not be promoted to an unrestricted bounded-operator theorem there.

The conclusion also fails under strong structural restrictions on `b`. Homogeneous, Hamiltonian-commuting, unitary-only, correspondence-preserving, locality-constrained or source-generated subclasses can have much smaller reachable state sets. Such restrictions are exactly where a viable arithmetic theorem could live. The present finding does not classify them and does not rule out a source-forced coherent correspondence whose relative amplitudes are uniquely determined by Bost-Connes arithmetic.

The finite Bost-Connes model (10)--(12) is only a cutoff control. A full construction could in principle impose infinite-dimensional compatibility conditions absent at every isolated cutoff. To evade this finding non-tautologically, however, those conditions must be stated independently of the desired Weil sign and shown to force the coherent amplitudes across cutoffs.

A direct falsification of the finite theorem would be a faithful density `\rho>0` and a positive `\sigma` for which no matrix `b` satisfies `b\rho b^*=\sigma`; equation (1) excludes this. A falsification of the Bost-Connes control would require a retained term in (12) to have zero Bohr frequency, or a nonzero self-adjoint `W_{F,N}` with only one spectral sign despite zero trace; neither can occur.

## Consequence for the Weil program

The active KMS branch is now sharper. `WP-428` says Bohr-diagonal positive sandwiches are too rigid: they annihilate the critical defect. The present finding gives the complementary boundary: **unrestricted Bohr-coherent sandwiches are too flexible**, since on finite faithful Gibbs controls they can manufacture any positive functional and either sign of the zero-mode-free defect.

A surviving construction must therefore occupy the narrow space between those extremes. It must derive from the arithmetic source, before inspecting the target sign, a nontrivial cross-frequency coherence rule that is neither Bohr-diagonal nor freely programmable. That same rule must remain compatible across the infinite Bost-Connes limit and recover the exact Mangoldt/half-density coefficients, archimedean Gamma contribution, polar normalization, admissible domain and global sign required by the line mandate.

This finding supplies no such rule and no RH consequence. It removes arbitrary coherent KMS sandwiching as evidence for positivity and turns the next question into a **source-canonicity theorem for the allowed cross-frequency amplitudes**.