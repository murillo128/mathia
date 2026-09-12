---
id: WP-263
title: Critical Gibbs-weighted Fock incidence collapses on the prime layer
branch: weil_positivity
status: supported
kind: negative
claim_strength: theorem under the conditional-Gibbs incidence construction
created: 2026-09-12
refined: 2026-09-12
related: [WP-262]
prior_art:
  - weighted normalized incidence / normalized signless Laplacian
  - prime zeta function and divergence of sum_p 1/p at s=1
  - Bost-Connes/statistical-mechanical zeta systems as background only
---

# WP-263 — Critical Gibbs-weighted Fock incidence collapses on the prime layer

## Claim

The source Hamiltonian can remove the arbitrary graph choice exposed by WP-262, but the most direct conditional-Gibbs completion fails precisely on the critical prime layer. For fixed multiplicity `k`, weighting the partner-prime incidence by the canonical Gibbs half-density `q^{-βk/2}` gives a positive normalized Gram whenever `Σ_q q^{-βk}` is finite. Matching that half-density to the Weil attenuation `n^{-1/2}` sets `β=1`; then `k=1` is non-normalizable, and every finite-cutoff normalization preserving unit diagonal forces each fixed off-diagonal prime-prime correlation to tend to zero. The layers `k≥2` remain nontrivial, so this is a no-go for this completion, not for Gibbs-based geometry in general.

## Derivation or evidence

Let `e_p^(k)=e_{p^k}` and `e_{pq}^(k)=e_{(pq)^k}` be the source and mixed Fock basis vectors from WP-262. For a fixed `k` and `β`, set

\[
P_k(\beta)=\sum_q q^{-\beta k}.
\]

When this is finite, define the conditional-Gibbs incidence vectors

\[
v_{p,k}^{(\beta)}
=
\frac{1}{\sqrt{P_k(\beta)-p^{-\beta k}}}
\sum_{q\ne p}q^{-\beta k/2}e_{pq}^{(k)}.
\]

For distinct primes `p,r`, the only common mixed basis vector is `e_{pr}^{(k)}`, hence

\[
\langle v_{p,k}^{(\beta)},v_{r,k}^{(\beta)}\rangle
=
\frac{p^{-\beta k/2}r^{-\beta k/2}}
{\sqrt{(P_k(\beta)-p^{-\beta k})(P_k(\beta)-r^{-\beta k})}}.
\]

Equivalently, this is the normalized incidence Gram of the complete weighted graph with edge weights `c_{pr}=p^{-βk}r^{-βk}` and weighted degrees `d_p=p^{-βk}(P_k(β)-p^{-βk})`. Thus the Gram is positive semidefinite independently of RH; on finite truncations it is `I` plus the normalized weighted adjacency and has operator norm at most `2`.

For the Mathia Hamiltonian `H e_n=(\log n)e_n`, the Gibbs half-density `e^{-\beta H/2}` contributes `n^{-\beta/2}`. Matching the Weil finite-prime factor `n^{-1/2}` therefore selects `β=1`. On the prime layer `k=1` this requires `P_1(1)=\sum_p p^{-1}`, which diverges. With a finite cutoff `q≤X`, let `P_X=\sum_{q≤X}q^{-1}`. Then for fixed distinct `p,r`,

\[
\langle v_{p,1,X}^{(1)},v_{r,1,X}^{(1)}\rangle
=
\frac{(pr)^{-1/2}}
{\sqrt{(P_X-p^{-1})(P_X-r^{-1})}}
\longrightarrow 0.
\]

Thus the source-forced critical completion becomes asymptotically diagonal on every fixed finite set of primes. Rescaling the cutoff incidence by order `\sqrt{P_X}` would keep a fixed off-diagonal correlation nonzero, but its diagonal norm then grows like `P_X`; preserving the finite diagonal normalization therefore forbids that rescue.

The obstruction is specific to the prime layer. At `β=1` and `k≥2`, `\sum_p p^{-k}<\infty`, so the same formula yields finite nonzero canonical correlations. Likewise `β>1` normalizes every layer, but this changes the finite-prime attenuation away from the critical Weil half-density and is not selected independently by the present construction.

The ingredients themselves are classical: normalized weighted incidence, the prime-zeta convergence boundary, and Gibbs/zeta statistical mechanics. The branch-specific content is the matched test against WP-262: replacing an arbitrary graph by the source Hamiltonian does produce a canonical correlation law, but the critical normalization needed for the Weil prime term erases that law on `k=1`.

## Falsification target

This finding would be overturned by a Mathia-native source rule that, without an arbitrary cutoff renormalization or a hand-picked graph/kernel, simultaneously keeps the critical `n^{-1/2}` finite-prime diagonal, yields a finite positive global form, and leaves a nonzero cross-prime interaction on the `k=1` sector. A quotient, boundary response, or non-conditional Gibbs construction could in principle do this; the claim does not exclude those mechanisms.

## Consequence

The Hamiltonian/Gibbs route survives only in a narrower form. It can canonically correlate higher prime-power layers, but the direct conditional complete-incidence completion cannot supply the missing critical prime-prime coupling. The next viable geometric route must obtain its cross-prime interaction before this divergent conditional normalization, or from a genuinely global quotient/boundary/cohomological mechanism that controls the prime layer without sacrificing the Weil finite-prime weight.
