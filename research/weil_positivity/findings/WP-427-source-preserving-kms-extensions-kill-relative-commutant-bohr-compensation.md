---
id: WP-427
title: Source-preserving KMS extensions kill relative-commutant Bohr compensation
kind: no-go
status: triage
created: 2026-09-24
parents:
  - WP-254
  - WP-425
  - WP-426
---

# WP-427 — Source-preserving KMS extensions kill relative-commutant Bohr compensation

## Claim

Let `(C,\gamma)` be a C*-dynamical system, let `\beta>0`, and let `\Omega` be a `\beta`-KMS state. Suppose `A\subset C` is a `\gamma`-invariant C*-subalgebra, write `\alpha=\gamma|_A`, and take `b\in A'\cap C`. Then, for every `a\in A` and every real `t`,
\[
\Omega(\alpha_t(a)b)=\Omega(ab).
\]

In particular, if `a_\omega\in A` is an entire Bohr eigenoperator satisfying
\[
\alpha_t(a_\omega)=e^{i\omega t}a_\omega,\qquad \omega\ne0,
\]
then
\[
\Omega(a_\omega b)=0
\qquad
(b\in A'\cap C).
\]

Thus a coupled KMS extension can evade the product-state obstruction of WP-425 only by leaving the auxiliary insertion outside the source relative commutant or by deforming the source dynamics itself. Merely abandoning product dynamics while retaining the original source flow and commuting compensation does not recover nonzero mixed Bohr correlations.

## Derivation

Take first an entire analytic `a\in A` and define
\[
F(z)=\Omega(\alpha_z(a)b).
\]
The KMS identity and `b\in A'\cap C` give
\[
F(z)
=\Omega(\alpha_z(a)b)
=\Omega(b\,\alpha_{z+i\beta}(a))
=\Omega(\alpha_{z+i\beta}(a)b)
=F(z+i\beta).
\]
Hence `F` is entire and `i\beta`-periodic. On the closed fundamental strip `0\le \operatorname{Im}z\le\beta`,
\[
|F(t+is)|
\le \|b\|\,\|\alpha_{is}(a)\|,
\]
and the right-hand side is uniformly bounded in real `t` and continuous in `s`. Periodicity therefore makes `F` bounded on the whole plane. Liouville's theorem gives that `F` is constant, so `F(t)=F(0)` for every real `t`. Density of entire analytic elements extends the identity to all `a\in A`.

For a Bohr eigenoperator one can see the annihilation directly:
\[
\Omega(a_\omega b)
=\Omega(b\,\alpha_{i\beta}(a_\omega))
=e^{-\beta\omega}\Omega(ba_\omega)
=e^{-\beta\omega}\Omega(a_\omega b).
\]
Since `\beta>0` and `\omega\ne0`, `e^{-\beta\omega}\ne1`, hence `\Omega(a_\omega b)=0`.

## Bost-Connes consequence

Assume an ambient coupled system contains the Bost-Connes source algebra as a `\gamma`-invariant subalgebra and `\gamma` restricts there to the standard Bost-Connes time evolution. Source ratio monomials `\mu_m f\mu_n^*` remain Bohr eigenoperators with frequency `\log(m/n)`. Whenever `m\ne n`, any auxiliary insertion lying in the source relative commutant therefore has zero equilibrium cross moment.

This strictly strengthens WP-425. The earlier result excluded product KMS dynamics because separate time-translation invariance destroys nonzero source Bohr columns. The present argument does not assume a product state, a product algebra decomposition, or separate invariance of an auxiliary factor. It uses only preservation of the source flow plus commutation of the compensator with the source algebra.

## Matched controls

The commutation hypothesis is load-bearing. Let `C=M_2`, let `H=\operatorname{diag}(0,E)`, and take the Gibbs `\beta`-KMS state for `\gamma_t(x)=e^{itH}xe^{-itH}`. With `a=e_{01}` and `b=e_{10}`, the operators do not commute and
\[
\Omega(ab)=\Omega(e_{00})>0.
\]
So a genuinely noncommuting compensator can carry a nonzero Bohr cross moment.

The positive-temperature hypothesis is also essential for the mode corollary: at `\beta=0`, the factor `e^{-\beta\omega}` is `1` and the argument gives no annihilation. Finally, if the source copy is not invariant under the ambient dynamics, or if the ambient flow does not restrict to the original Bost-Connes evolution, the theorem does not constrain the original source Bohr modes.

## Consequence for the Weil program

The affiliation/conditioning route now has a sharper boundary. Moving from product dynamics to a general KMS extension is not enough if the auxiliary boundary variable remains in the Bost-Connes relative commutant. A viable construction must therefore use at least one of two genuinely stronger mechanisms:

1. a noncommuting correspondence or auxiliary operator whose source interaction invalidates the relative-commutant step; or
2. a coupled dynamics that changes the source evolution itself.

The second option inherits the programmability warning of WP-426: a deformed source flow is evidentially useful only if its generator is derived from the arithmetic source data rather than tuned from the target state. It must also avoid the exterior-equivalence / Morita-trivial regime already closed by WP-254.

This is an RH-independent architecture result. It does not prove the Weil sign condition; it removes a broad commuting KMS-extension mechanism from the live search space.

## Novelty audit

The abstract KMS argument is classical. Standard analytic-element/KMS machinery is covered by Bratteli and Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, 2nd ed. (Springer, 1997). Batty, “G-central subalgebras and extensions of KMS states,” *J. Functional Analysis* **66** (1986), 11–20, DOI `10.1016/0022-1236(86)90077-7`, is adjacent prior art on KMS extensions and central subalgebras. No novelty claim is made for the generic operator-algebra theorem.

The Mathia-specific contribution is the frontier closure obtained by applying that mechanism to the current Bost-Connes/Weil architecture. WP-425 is restricted to product KMS systems; WP-254 closes exterior-equivalent/Morita-trivial couplings; WP-426 shows that arbitrary state-selected modular dynamics is programmable. None of those findings states the present source-preserving relative-commutant no-go.

## Classification

This is a **no-go** finding. The decisive obstruction is exact and source-independent once the KMS/source-preserving/commuting hypotheses hold. The surviving research direction is correspondingly narrow: derive a genuinely noncommuting source-positive correspondence, or derive a nontrivial source deformation whose dynamics is arithmetically forced rather than target-programmed.
