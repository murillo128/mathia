---
id: WP-277
title: Compact-resolvent arithmetic sources cannot manufacture the pole continuum by subcritical relatively bounded coupling
branch: weil_positivity
status: supported
kind: source-continuum-provenance-obstruction
claim_strength: exact source-specific compact-resolvent no-go for bounded and relative-bound-<1 couplings
created: 2026-09-13
related: [WP-259, WP-273, WP-275, WP-276]
prior_art:
  - compact-resolvent spectral theory
  - Kato-Rellich relatively bounded perturbations
  - resolvent identity
  - Weyl-von Neumann-Kuroda perturbation theory as a matched control
---

# WP-277 — Compact-resolvent arithmetic sources cannot manufacture the pole continuum by subcritical relatively bounded coupling

## Claim

`WP-276` shows that trace-class source surgery cannot create a new absolutely continuous channel from a wholly singular source. For the actual arithmetic Hamiltonians currently carrying Mathia's exact critical finite data, the obstruction is substantially stronger.

On the permutation-fixed prime Fock sector of `WP-259`,

\[
H_{\rm ar} e_n=(\log n)e_n,
\qquad n\ge1.
\tag{1}
\]

This operator has **compact resolvent**. Consequently, if `K` is any self-adjoint auxiliary Hamiltonian with compact resolvent and

\[
A_0=H_{\rm ar}\oplus K,
\tag{2}
\]

then every symmetric perturbation `V` which is `A_0`-bounded with relative bound strictly smaller than one leaves the resolvent compact. In particular this includes every bounded self-adjoint finite--archimedean coupling, with no Schatten-class assumption at all:

\[
\boxed{
(A_0+V-z)^{-1}\text{ is compact for }z\in\rho(A_0+V).
}
\tag{3}
\]

Hence `A_0+V` still has purely discrete spectrum with finite-multiplicity eigenvalues and cannot contain the absolutely continuous real-line channel required by the pole sector in `WP-273`--`WP-275`.

This closes the most direct escape left explicitly open by `WP-276`. Passing from trace class to Hilbert--Schmidt, another compact ideal, or even an arbitrary bounded noncompact coupling does **not** manufacture the missing continuum when both zeroth-order sectors have compact resolvent. A source-first construction must instead do at least one of the following before the Weil sign is read: supply an intrinsic non-compact-resolvent/absolutely-continuous archimedean sector already at zeroth order; use a genuinely supercritical unbounded/domain-changing coupling outside the relative-bound-`<1` class; or take an infinite-volume/direct-limit/category change in which compact resolvent is lost.

This is not a Weil-positivity theorem. It is a provenance obstruction: the pole continuum cannot be an emergent consequence of ordinary bounded mixing of Mathia's present discrete arithmetic source with another discrete auxiliary system.

**Classification:** `EXACT-DERIVED + SOURCE-SPECIFIC-COMPACT-RESOLVENT + BOUNDED-COUPLING-NO-GO + RELATIVE-BOUND-<1-EXTENSION + POLE-CONTINUUM-PROVENANCE + STRICT-STRENGTHENING-OF-WP-276-ON-CURRENT-SOURCE + PRIOR-ART-CLASSICAL + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. The current arithmetic Hamiltonian has compact resolvent

The symmetric prime-Fock source of `WP-259` is canonically indexed by the positive integers and satisfies (1). For any nonreal `z`,

\[
(H_{\rm ar}-z)^{-1}e_n
=\frac1{\log n-z}e_n.
\tag{4}
\]

Since

\[
\frac1{|\log n-z|}\longrightarrow0
\qquad(n\to\infty),
\tag{5}
\]

this diagonal resolvent is compact on `ell^2(N)`. Equivalently, every bounded energy window contains only finitely many basis states and the eigenvalues escape to `+infinity`.

The same compact-resolvent property holds on the prime-power axis used by the exact Mangoldt carrier. It also holds for the ambient free prime-Fock Hamiltonian: below a fixed energy `E`, every word has product at most `e^E`, hence bounded length and letters from a finite prime set, so the corresponding spectral projection has finite rank.

Thus the present source is stronger than merely "pure point." It is a confining discrete system with no essential spectral channel at finite energy.

## 2. Bounded coupling cannot create a continuum

First take `V=V^*` bounded. Let `K` in (2) also have compact resolvent. A finite-dimensional auxiliary is the simplest special case. Then `A_0` has compact resolvent because a finite direct sum of compact resolvents is compact.

Choose `y>||V||` and set `z=iy`. Since `A_0` is self-adjoint,

\[
\|(A_0-iy)^{-1}\|\le\frac1y,
\tag{6}
\]

so

\[
\|V(A_0-iy)^{-1}\|<1.
\tag{7}
\]

On `Dom(A_0)`,

\[
A_0+V-iy
=\bigl(I+V(A_0-iy)^{-1}\bigr)(A_0-iy).
\tag{8}
\]

The first factor is invertible by the Neumann series, hence

\[
(A_0+V-iy)^{-1}
=(A_0-iy)^{-1}
\bigl(I+V(A_0-iy)^{-1}\bigr)^{-1}.
\tag{9}
\]

The first factor on the right is compact and the second is bounded. Therefore the perturbed resolvent is compact.

For a self-adjoint operator, compact resolvent implies a complete orthonormal eigenbasis, finite multiplicity of every eigenvalue, and no finite accumulation point. In particular,

\[
\boxed{
\mathcal H_{\rm ac}(A_0+V)=\{0\}.
}
\tag{10}
\]

The conclusion is independent of whether `V` is finite rank, trace class, Hilbert--Schmidt, compact, or noncompact bounded. The Schatten boundary that mattered in `WP-276` is therefore not the relevant boundary once the stronger source property of compact resolvent is used.

## 3. The obstruction extends to subcritical relatively bounded couplings

The bounded hypothesis is not sharp. Suppose `V` is symmetric and `A_0`-bounded with constants `a<1` and `b>=0`:

\[
\|V\psi\|
\le a\|A_0\psi\|+b\|\psi\|,
\qquad \psi\in\operatorname{Dom}(A_0).
\tag{11}
\]

Kato--Rellich gives self-adjointness of `A_0+V` on the same domain. For `z=iy`, spectral calculus gives

\[
\|A_0(A_0-iy)^{-1}\|\le1,
\qquad
\|(A_0-iy)^{-1}\|\le |y|^{-1}.
\tag{12}
\]

Hence

\[
\|V(A_0-iy)^{-1}\|
\le a+\frac b{|y|}.
\tag{13}
\]

For sufficiently large `|y|`, the right-hand side is strictly below one. The same factorization (8)--(9) therefore applies, proving compactness of the perturbed resolvent.

Thus even a substantial class of unbounded source couplings cannot create the pole continuum. The live unbounded escape must leave this subcritical relative-bounded regime, change the domain/ambient representation more radically, or start from a zeroth-order sector which already lacks compact resolvent.

## 4. Why this blocks the `WP-273`--`WP-275` pole sector

After the canonical pole normalization used in `WP-275`, the negative continuum sector is

\[
\mathcal H_{\rm pole}=L^2(\mathbb R,dx)
\tag{14}
\]

with modulation group

\[
(U(t)f)(x)=e^{itx}f(x).
\tag{15}
\]

Its self-adjoint generator is multiplication by `x`, which has absolutely continuous spectral type on the real line. This is precisely the kind of channel absent from every compact-resolvent operator.

Therefore a candidate architecture of the form

\[
\boxed{
\text{discrete arithmetic source}
\oplus
\text{finite/discrete archimedean auxiliary}
\xrightarrow{\text{bounded or rel.-bound }<1\text{ mixing}}
\text{pole continuum}
}
\tag{16}
\]

is impossible before any question of Weil orientation is reached.

This is stronger than the exact-covariance obstruction of `WP-275`. There the continuum already existed and a bounded intertwiner from the pure-point arithmetic flow to it had to vanish. Here the proposed continuum is not supplied at all: the mixed Hamiltonian itself cannot acquire one from compact-resolvent ingredients under the declared perturbation class.

It also sharpens `WP-276` on the present source. `WP-276` deliberately treated a general wholly singular operator, for which Hilbert--Schmidt or other non-trace-class perturbations can change spectral type. Equation (3) shows that this general escape disappears for Mathia's current logarithmic arithmetic Hamiltonian as long as the auxiliary is also compact-resolvent and the coupling is subcritical relatively bounded.

## 5. Matched controls and aggressive falsification

**A pre-existing continuum survives the theorem because it violates the hypothesis.** If the auxiliary sector is already `L^2(R)` with multiplication generator, then `A_0` does not have compact resolvent. Bounded coupling may produce nontrivial scattering. But the continuum has then been supplied at zeroth order; its arithmetic/archimedean canonicity and sign theorem still have to be derived independently.

**Weyl--von Neumann--Kuroda does not contradict the result.** Classical perturbation theory shows that Hilbert--Schmidt, and more generally suitable `S_p` perturbations with `p>1`, can radically alter continuous versus pure-point spectral type. The diagonal pure-point operator appearing in that theorem need not have compact resolvent: its eigenvalues may be dense in intervals carrying the original essential spectrum. Mathia's source is more restrictive because its finite-energy spectral projections are finite dimensional and its eigenvalues escape to infinity. The distinction `pure point != compact resolvent` is essential here.

**Strong/direct limits can create continuum.** A sequence of compact-resolvent finite-volume operators can converge to an operator with continuous spectrum. Such a thermodynamic or infinite-volume limit is therefore a legitimate escape, but it changes the source architecture rather than applying one bounded perturbation on a fixed Hilbert space. Its limit, normalization, and arithmetic data must be independently forced.

**Supercritical unbounded coupling remains open.** Relative bound `>=1`, singular form couplings that change the form domain, extensions with noncompact resolvent difference, and other domain-changing constructions are not covered. Merely relabeling a bounded coupling as a boundary interaction does not evade the proof; the candidate must actually fail the compact-resolvent factorization hypothesis.

**The theorem does not identify the Gamma sector.** Compact-resolvent oscillator or gauge models can still generate useful discrete Gamma-like determinants, but boundedly coupling two discrete sectors cannot turn them into the real-line pole continuum of the source-side Krein decomposition. A successful global geometry may need both a discrete determinant structure and an independent continuous boundary/scattering sector.

## 6. Prior art and novelty boundary

No novelty is claimed for compact-resolvent perturbation theory. The resolvent argument above is standard. The relative-bound extension is a direct Kato--Rellich application; see T. Kato, *Perturbation Theory for Linear Operators*, Springer, for the classical self-adjoint perturbation framework. The spectral-instability control is classical Weyl--von Neumann--Kuroda theory; see S. T. Kuroda, *On a Theorem of Weyl-von Neumann*, Proceedings of the Japan Academy 34 (1958), 11--15, DOI `10.3792/pja/1195524841`.

A targeted audit of compact-resolvent perturbation theory and operator-theoretic zeta constructions found the standard ingredients, but no need to claim a new operator theorem. The durable Mathia-specific content is the compatibility obstruction obtained by combining those ingredients with the exact source already isolated in `WP-259` and the pole-continuum requirement isolated in `WP-273`--`WP-275`.

The important correction to the post-`WP-276` frontier is conceptual and exact: **for the current arithmetic source, leaving trace class or Hilbert--Schmidt is not enough. Every bounded, and every subcritical relatively bounded, coupling between compact-resolvent sectors preserves discreteness.** The continuum must have an independent zeroth-order provenance or arise through a genuinely stronger category change.

## Consequence for `weil_positivity`

The surviving source-first architecture is now narrower. Before asking whether a geometric form has the Weil sign, a candidate must explain the existence of its global continuous sector in one of two non-tautological ways:

1. derive an intrinsic infinite-dimensional archimedean/boundary operator which already has noncompact resolvent and the required absolutely continuous spectral type, then couple it to the arithmetic source; or
2. derive a canonical supercritical/domain-changing/infinite-volume mechanism that destroys compact resolvent for an independent geometric reason.

Only after that provenance problem is solved does the earlier sign problem return: the same construction must still reproduce the exact finite Mangoldt contribution, Gamma and polar terms, survive matched arithmetic controls, and prove nonnegativity independently of RH or inserted zero data.

## Conclusion

Mathia's current logarithmic arithmetic Hamiltonian is not merely pure point; it has compact resolvent. That stronger property rules out an entire apparent escape from `WP-276`: **ordinary bounded or subcritical relatively bounded finite--archimedean mixing cannot manufacture the pole continuum at all.** A viable Weil-positive geometry must contain a genuine continuum before such mixing, or cross a substantially more singular structural boundary.