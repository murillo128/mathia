---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-416-weighted-vdc-filters-cannot-remove-diagonal.md
  - research/mobius_cancellation/findings/MC-417-fejer-riesz-closes-positive-finite-band-kernels.md
  - research/mobius_cancellation/findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md
  - research/mobius_cancellation/findings/MC-458-staged-factor-conditioning-exposes-residual-divisor-sum-kernel.md
  - research/mobius_cancellation/findings/MC-459-staged-residual-energy-is-controlled-by-the-normalized-shift.md
  - research/mobius_cancellation/findings/MC-460-one-sided-residual-conditioning-promotes-reduced-divisor-to-reciprocal-source-shift.md
  - research/mobius_cancellation/findings/MC-461-residual-source-starts-decompose-into-bounded-anchor-slices.md
  - research/mobius_cancellation/findings/MC-463-gcd-sector-normalization-collapses-to-common-anchor-quotient.md
  - research/mobius_cancellation/findings/MC-464-normalized-gcd-gate-makes-favorable-shifts-totient-sparse.md
  - research/mobius_cancellation/findings/MC-465-fejer-weighted-favorable-gcd-classes-remain-sparse.md
  - research/mobius_cancellation/findings/MC-466-original-shift-fejer-envelope-cancels-outer-gcd-advantage.md
  - research/mobius_cancellation/findings/MC-467-residual-scale-interval-shrinkage-cancels-support-growth.md
  - research/mobius_cancellation/findings/MC-468-root-scale-support-makes-well-factorability-vacuous.md
  - research/mobius_cancellation/findings/MC-469-empty-vector-sieve-component-survives-small-outer-cell-pruning.md
  - research/mobius_cancellation/findings/MC-470-empty-vector-residual-is-a-nonnegative-sieve-boundary-count.md
  - research/mobius_cancellation/findings/MC-471-empty-vector-base-is-two-sided-sifted-translated-ratio-sum.md
  - research/mobius_cancellation/findings/MC-472-pair-sieve-complete-period-factorizes.md
  - research/mobius_cancellation/findings/MC-473-termwise-pair-sieve-completion-pays-exponential-branch-multiplicity.md
  - research/mobius_cancellation/findings/MC-474-pair-sieve-fourier-spectral-norm-is-exponential.md
  - research/mobius_cancellation/findings/MC-475-pair-sieve-parseval-coupling-pays-full-frequency-dimension.md
  - research/mobius_cancellation/findings/MC-476-sifted-restriction-is-coefficient-blind-at-zero-frequency.md
  - research/mobius_cancellation/findings/MC-477-low-denominator-envelope-admits-denominator-free-character-completion.md
  - research/mobius_cancellation/findings/MC-478-pair-sieve-local-fourier-factorization-lowers-envelope-l1-cost.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The empty-vector base component has now been reduced to a sharply defined incomplete pair-sieve discrepancy. `MC-472` shows that its complete joint period has no hidden sieve/character resonance. `MC-473`--`MC-475` then close three direct incomplete continuations: exact divisor branching plus independent completion pays exponentially many branches, exact hard-mask Fourier `ell^1` has exponential spectral mass, and plain full-grid `ell^2`/Parseval pays the full primorial frequency dimension. `MC-476` further shows that the modern coefficient-uniform restriction theorem for sifted sets is blind to the translated-ratio character phase at zero frequency.

The representation layer of that restriction theory nevertheless survives. `MC-477` proves that every rational frequency in the Bera--Viswanadham/Ramaré--Ruzsa low-denominator envelope couples to

\[
K_h(n)=\chi(n+h)\overline{\chi(n)}
\]

for only `O(sqrt(p) log p)`, uniformly in the rational denominator. `MC-478` then retains the exact pair-sieve local Fourier product instead of collapsing immediately to the generic `q^{-1/2}` coefficient bound. This lowers the total absolute envelope coefficient cost from the crude `z^3/G(z)` of `MC-477` to

\[
\ll \frac{z^2(\log(2z))^5}{G(z)}.
\]

Thus the low-denominator family itself no longer appears to be the main representation-complexity obstruction. The remaining base-component gap is the **signed interface between the exact pair-sieve indicator and the enveloping representation**. Pointwise majorization cannot be inserted into the complex character sum, while a generic positive norm closure risks erasing exactly the conductor-sensitive gain that the low-denominator completion preserves.

The mixed rough/boundary and first-exit terms remain mathematically distinct, as do nonempty rough-block components and cross-component interference before positive closure.

## Research question

Can the exact rough×rough pair-sieve sum be transferred to the low-denominator envelope, or embedded in a positive quadratic form, with an error strictly below the conductor-saving budget supplied by `MC-477`--`MC-478`?

For the exact mask

\[
A_{W,h}(n)=\mathbf1_{(n(n+h),W)=1}
\]

and the corresponding low-denominator envelope `beta`, the direct missing object is

\[
\sum_{n\in I}K_h(n)\bigl(A_{W,h}(n)-\beta(n)\bigr).
\]

A useful result may instead avoid literal replacement by deriving a bilinear, Buchstab, truncated-sieve, dispersion, or positive quadratic representation in which the exact mask is controlled while the translated-ratio phase remains visible. What does not qualify is a pointwise majorization followed by triangle inequality, or a norm estimate whose right-hand side depends only on coefficient magnitude and therefore treats `K_h` like constant positive coefficients.

For nonempty components and boundary terms, the same question should be asked only after their exact support and first-exit structure is retained; they are not automatically covered by the empty-vector analysis.

## Why it may matter

The route has progressively removed several apparent resources that were artifacts of representation or positive closure: favorable gcd sectors, generic well-factorability, residual coefficient signs, complete-period resonance, full inclusion-exclusion, hard-mask Fourier expansion, generic Hilbert-space averaging, and coefficient-uniform restriction. The low-denominator envelope is the first surviving representation in this chain whose individual character modes and aggregate absolute coefficient mass both fit a polynomial source budget.

If the signed replacement can also be controlled at that scale, the base component would genuinely evade the full-primorial obstructions of `MC-473`--`MC-475`. If every accurate replacement necessarily recreates a trivial-scale signed error or loses the conductor-sensitive phase under positive closure, that would close the main restriction-style escape and redirect attention to boundary/nonempty components or pre-positive cross-component interference.

## Decisive test

Work in the `R=T=1` empty-vector source frame and retain the centering from `MC-472`. Use the actual Bera--Viswanadham/Ramaré--Ruzsa enveloping object or one precisely specified truncated/factorable replacement; do not revert to the exact full-primorial Fourier frame already closed by `MC-473`--`MC-475`.

First derive a valid identity or inequality that connects the exact pair-sieve term to the compressed object **without using sign-insensitive pointwise majorization inside the character sum**. Then charge the resulting error or quadratic remainder explicitly against the conductor-sensitive budget

\[
\frac{z^2(\log(2z))^5}{G(z)}\sqrt p\log(2p)
\]

from `MC-478`, together with source interval length, shell summation, Fejér weights, coefficient normalization, endpoint separation, and source depth from the staged architecture.

Accept the route only if the complete accounting gives a strict conductor-power gain for the exact base component. Kill the restriction-style route if every legitimate exact-to-envelope transfer has trivial-scale signed error, or if the only available positive closure replaces the `K_h`-specific completion gain by a coefficient-blind norm bound.

For mixed/boundary terms, use the exact first-exit decomposition from `MC-470`; for nonempty pieces, retain the exact bin-product support pruning; for cross-component interference, retain the signed finite decomposition through the proposed transform and exhibit a concrete surviving cross term rather than appealing to cancellation after separate absolute bounds.

## Evidence boundary

`MC-477` proves only a denominator-independent character estimate for each low-denominator rational mode and a crude envelope recombination. `MC-478` improves only that envelope recombination by exploiting exact local pair-sieve Fourier factorization. Neither controls the exact pair-sieve indicator, the signed replacement error, boundary terms, nonempty components, or cross-component interference.

The displayed low-denominator budget is an upper bound for one coefficientwise envelope treatment, not a lower bound or an optimal barrier. No conductor-power estimate for the exact rough×rough discrepancy, Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted`, but the restriction-style branch is now substantially narrower. The low-denominator character modes and their aggregate pair-sieve `ell^1` cost have survived and been priced by `MC-477`--`MC-478`; the immediate unresolved question is the **signed exact-to-envelope transfer while retaining the conductor gain**. Further improvement of the envelope coefficient aggregation is useful but no longer substitutes for that missing interface theorem.