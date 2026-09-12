---
id: WP-275
title: Source-time-covariant positive sampling compressions are trivial by spectral type
branch: weil_positivity
status: supported
kind: source-side-covariant-compression-obstruction
claim_strength: exact RH-independent spectral-type no-go for time-covariant pole-completed sampling contractions
created: 2026-09-12
related: [WP-131, WP-225, WP-256, WP-269, WP-273, WP-274]
---

# WP-275 — Source-time-covariant positive sampling compressions are trivial by spectral type

## Claim

The nonlocal positive-compression escape left open by `WP-273` and `WP-274` cannot preserve the most immediate source-side dynamics.

Let

\[
\mathcal H_{\rm pp}=L^2(\sigma_\Lambda),
\qquad
\mathcal H_{\rm ac}=L^2(\mathbb R,dx),
\]

where `WP-273`'s pole-normalized arithmetic measure is

\[
\sigma_\Lambda
 =\sum_{n=p^k}\frac{\Lambda(n)}{n+1}
   \bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\]

Both sectors carry the canonical log-coordinate modulation group

\[
(U_{\rm pp}(t)h)(s)=e^{its}h(s),
\qquad
(U_{\rm ac}(t)g)(x)=e^{itx}g(x).
\]

If a bounded map

\[
C:D\subseteq\mathcal H_{\rm pp}\longrightarrow\mathcal H_{\rm ac}
\]

has a domain invariant under every `U_pp(t)` and exactly intertwines these groups,

\[
C U_{\rm pp}(t)=U_{\rm ac}(t)C,
\qquad t\in\mathbb R,
\]

then

\[
\boxed{C=0.}
\]

Consequently, any nonnegative graph compression of the pole-completed Weil Krein form that is invariant under the diagonal canonical modulation flow is supported entirely in the arithmetic sector. In particular, a nontrivial function-derived positive sampling range cannot be both globally nonlocal and exactly covariant for this natural source-side log-energy action.

This does **not** rule out non-equivariant Clark/de Branges/canonical-system constructions. It says that the surviving source-first route must do more than introduce global nonlocality: before positivity is obtained it must also break, twist, enlarge, or otherwise change the spectral realization of the canonical log-energy dynamics.

## 1. Exact pole-normalized setting

`WP-273` rewrites the pole-completed candidate sign problem as the Krein difference

\[
Q(h,g)
 =\|h\|_{\mathcal H_{\rm pp}}^2
  -\|g\|_{\mathcal H_{\rm ac}}^2.
\]

Any nonnegative linear subspace `M` of this Krein space has injective projection onto the positive sector. Writing

\[
D=P_{\rm pp}M,
\]

there is therefore a uniquely defined contraction

\[
C:D\to\mathcal H_{\rm ac},
\qquad
M=\{(h,Ch):h\in D\},
\]

with

\[
\|Ch\|_{\rm ac}\le \|h\|_{\rm pp}.
\]

`WP-273` already showed that cutoff-stable finite-range/local choices of this compression cannot reproduce the required pole continuum. `WP-274` then showed that inverse Clark or canonical-system machinery can manufacture nonlocal positive hosts after the target measure is supplied, but that this is a universal inverse realization rather than a source-derived sign mechanism.

There is a further source-side constraint available before importing such an inverse model. Both sides already have a distinguished real coordinate: the arithmetic atoms sit at `±log n`, while the pole sector is a continuum in the same explicit-formula coordinate. The corresponding multiplication group `e^{itx}` is therefore the minimal exact dynamical structure one can ask a source-derived sampling map to respect.

The original unnormalized pole Hilbert space in `WP-273` is `L²(w(x)dx)` for a positive pole weight `w`. The unitary normalization

\[
Tg=\sqrt{w}\,g
\]

commutes with every multiplication operator `e^{itx}`. Hence the statement below is not an artifact of replacing the weighted pole measure by Lebesgue measure.

## 2. Spectral-type lemma

### Proposition

Let `D⊂H_pp` be invariant under `U_pp(t)` for every real `t`, and let `C:D→H_ac` be bounded. If

\[
C U_{\rm pp}(t)h=U_{\rm ac}(t)Ch
\]

for all `h∈D` and `t∈R`, then `C=0`.

### Proof

Because `C` is bounded on `D`, it extends continuously to `K=\overline D`. Since `D` is invariant under both `U_pp(t)` and `U_pp(-t)`, `K` is reducing for the pure-point unitary representation.

For any atom `s` of `σ_Λ`, the singleton spectral projection `E_pp({s})` therefore preserves `K`. Whenever a vector of `K` has a nonzero component at `s`, the corresponding atomic vector belongs to `K`. The atomic spectral components span `K`, so it is enough to show that the extension of `C` kills each such component.

Take an atomic vector `e_s` supported at `s`. Then

\[
U_{\rm pp}(t)e_s=e^{its}e_s.
\]

Intertwining gives

\[
U_{\rm ac}(t)Ce_s=e^{its}Ce_s
\]

for every real `t`. Thus `Ce_s` would be a joint eigenvector of the Lebesgue modulation representation with character `e^{its}`.

But if `g∈L²(R,dx)` obeys

\[
e^{itx}g(x)=e^{its}g(x)
\]

for every `t`, then `g` is supported on the singleton `{s}`. A singleton has Lebesgue measure zero, so `g=0` in `L²(R,dx)`. Hence `Ce_s=0` for every atomic component of `K`, and density gives `C=0` on `K`, hence on `D`. ∎

The obstruction is therefore not decay, compactness, locality, or failure of a particular interpolation kernel. It is the mutually singular spectral type of the two canonical modulation representations: the arithmetic carrier is pure point, while the pole carrier is nonatomic absolutely continuous.

## 3. Consequence for positive graph compressions

Suppose `M⊂H_pp⊕H_ac` is nonnegative for `Q` and invariant under the diagonal flow

\[
U(t)=U_{\rm pp}(t)\oplus U_{\rm ac}(t).
\]

Write `M=graph(C)` as above. Invariance under `U(t)` and `U(-t)` makes `D` invariant and forces

\[
C U_{\rm pp}(t)=U_{\rm ac}(t)C.
\]

The proposition gives `C=0`, so

\[
\boxed{M\subseteq\mathcal H_{\rm pp}\oplus\{0\}.}
\]

This is incompatible with the intended role of a pole-completed sampling range. If a candidate range has the function-derived form

\[
J(\mathcal R)
 =\{(g|_{\operatorname{supp}\sigma_\Lambda},g):g\in\mathcal R\},
\]

then `C=0` forces its continuum component `g` to vanish; consequently its sampled component vanishes as well. The only exactly time-covariant positive range of this direct type is therefore the trivial range.

This strengthens the frontier left by `WP-273`. Nonlocality is necessary but not sufficient: **a surviving nonlocal compression cannot simply identify arithmetic samples with a continuum while preserving the canonical multiplication/time representation on both sides.**

## 4. Source-native Fock corollary

The same obstruction applies directly to the most natural source-native arithmetic carrier already isolated in `WP-256`. There the simple-spectrum prime-free/Fock geometry has energy eigenvectors

\[
H e_{p^k}=k\log p\;e_{p^k},
\]

so the unitary source flow `e^{itH}` is pure point at exactly the logarithmic prime-power energies.

If a bounded boundary, Poisson, or sampling map

\[
B:\mathcal H_{\rm Fock}\to L^2(\mathbb R,dx)
\]

were required to preserve this source dynamics exactly,

\[
B e^{itH}=U_{\rm ac}(t)B,
\]

then the same one-eigenvector argument gives

\[
\boxed{B=0.}
\]

Thus the canonical Mangoldt half-density found in `WP-256` cannot be transported into the pole continuum by a bounded exact intertwiner that keeps the same log-energy/time action. Any successful source-native completion has to alter the representation before the positive sign theorem: for example through a genuinely mixed sector, a noncommuting boundary operation, a change of spectral type, or another source-forced symmetry-breaking construction.

## 5. Matched controls and falsification

The theorem deliberately survives controls in which the arithmetic data are removed. Replace `σ_Λ` by any positive pure-point measure on any countable subset of the real line, with arbitrary positive atom weights. Keep the pole side any nonatomic measure for which the multiplication representation has no matching point spectrum. The same proof gives a zero intertwiner.

Therefore this is **not evidence that the primes themselves force Weil positivity**. It is an architectural no-go for a broad class of source-to-continuum interfaces. The Mangoldt weights, Euler product, critical line, and RH play no role in the proof.

There are also clear escape tests rather than hidden exclusions:

- If the continuum sector acquires matching atoms, the spectral-type argument no longer kills those atomic channels.
- If the source geometry changes the representation before comparison, so that its relevant boundary carrier has continuous spectral type, the hypothesis fails and the route remains open.
- If the positive subspace is not invariant under the full canonical modulation group, the graph contraction need not intertwine and the theorem does not apply.
- If the coupling is unbounded, distributional, matrix-valued with an enlarged mixed carrier, or otherwise outside the bounded graph setting, a separate closability/domain analysis is required.

These are genuine changes of mechanism, not exceptions obtained by changing a coefficient or regularization.

## 6. Prior-art and novelty audit

The underlying operator-theoretic mechanism is classical spectral theory: bounded intertwiners cannot transfer point spectral vectors into a representation with no matching point spectrum. In broader language this sits in the standard spectral-theorem/Fuglede–Putnam territory. Mathia already encountered the same general mechanism in `WP-131`, where a different radial-solenoid/Gamma interface was killed by pure-point versus continuous spectral type.

Accordingly, **the spectral lemma itself is not a novel mathematical theorem**. The new branch-local content is its application to the specific pole-normalized positive graph left open by `WP-273`–`WP-274`, and the resulting restriction on what an independently selected source-side model is allowed to preserve.

This also separates the claim from `WP-225`. That finding used covariance to obstruct a Bost–Connes orientation of a Weil defect. Here the object is instead the positive graph contraction between the arithmetic sampling measure and the pole continuum, and the obstruction is exact mismatch of spectral type.

Inverse Clark/de Branges/canonical-system constructions are not contradicted. Their useful model spaces need not be invariant under the full ambient modulation group, and `WP-274` already showed that a target-built choice can be made by inverse realization. The present result explains why such symmetry breaking is not optional if one starts from the canonical arithmetic time action.

## 7. Research-frontier consequence

After `WP-273`, a survivor had to be globally nonlocal. After `WP-274`, its inner/canonical/de Branges or boundary model also had to be selected independently of the target Weil measure. `WP-275` adds a third requirement:

\[
\boxed{
\text{source-derived survivor}
\;\Rightarrow\;
\text{nonlocal + independently selected + not an exact pure-point-to-continuum time intertwiner}.
}
\]

The remaining plausible target is therefore not a better interpolation formula between the same two spectral representations. It is a Mathia-native construction that **changes the representation before positivity** and does so for an independently geometric reason, while still recovering in one structure the prime-power masses, the archimedean Gamma contribution, and the global pole terms with the required Weil orientation.

A candidate that merely chooses a non-invariant Clark/model space after seeing the target measure remains the inverse tautology of `WP-274`. A candidate that derives a noncommuting boundary/mixed-sector geometry from Prime Circle, Prime Flute, Prime Lattice, or the Fock source before matching arithmetic data would evade the present no-go and is the relevant next falsification target.

## Conclusion

The pole-completed Weil positivity problem cannot be solved by taking Mathia's natural pure-point log-energy carrier, applying a bounded positive/nonlocal sampling compression, and requiring that compression to preserve the same canonical time/modulation action on the pole continuum. Spectral type forces that map to vanish.

This is a negative but durable narrowing result: **global nonlocality alone is not enough. A source-native positivity mechanism must generate its own non-equivariant or spectral-type-changing finite–archimedean coupling before the sign theorem becomes available.**
