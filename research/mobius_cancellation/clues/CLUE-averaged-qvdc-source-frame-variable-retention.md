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
  - research/mobius_cancellation/findings/MC-479-selberg-envelope-leakage-is-order-one-on-near-cutoff-single-violations.md
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

`MC-479` now closes the simplest unsigned transfer back to the exact mask. The Selberg envelope equals the hard pair-sieve indicator exactly on genuine survivors; the entire difference is positive false-positive leakage. More importantly, a residue that violates exactly one sieve prime `r` with `z/2<r<z` still receives envelope weight

\[
\left(1-\frac{r}{(r-\nu_r(h))G_1(z)}\right)^2
=1+O(1/\log z),
\]

while the exact mask is zero. These single near-cutoff violations force complete-period leakage only logarithmically smaller than the survivor mass. Thus `beta-A` is not a small pointwise or phase-blind `L^1` error capable of paying a fixed conductor power.

The low-denominator family itself is therefore not the main representation-complexity obstruction, but neither is ordinary majorant accuracy the missing bridge. The remaining base-component gap is specifically **cancellation of the translated-ratio phase against Selberg false-positive leakage**, or a genuinely signed/factorable replacement that suppresses that leakage before coefficient-blind closure.

The mixed rough/boundary and first-exit terms remain mathematically distinct, as do nonempty rough-block components and cross-component interference before positive closure.

## Research question

Can the false-positive leakage of the low-denominator Selberg envelope be controlled after coupling it to `K_h`, or replaced by a signed/factorable surrogate, with a remainder strictly below the conductor-saving budget supplied by `MC-477`--`MC-478`?

For the exact mask

\[
A_{W,h}(n)=\mathbf1_{(n(n+h),W)=1}
\]

and the corresponding low-denominator envelope `beta`, `MC-479` gives

\[
L_{W,h}(n):=\beta(n)-A_{W,h}(n)\ge0,
\qquad
L_{W,h}(n)=0\ \text{whenever }A_{W,h}(n)=1.
\]

The direct missing object is therefore

\[
\sum_{n\in I}K_h(n)L_{W,h}(n).
\]

A useful result may derive a bilinear, Buchstab, truncated-sieve, first-exit, dispersion, or positive quadratic representation of this **leakage-weighted character sum** in which the translated-ratio phase remains visible. What no longer qualifies is an attempt to prove that `beta-A` is uniformly or absolutely small: `MC-479` rules that out in the relevant sense. A norm estimate whose right-hand side depends only on coefficient magnitude and therefore treats `K_h` like constant positive coefficients likewise cannot exploit the surviving conductor gain.

For nonempty components and boundary terms, the same question should be asked only after their exact support and first-exit structure is retained; they are not automatically covered by the empty-vector analysis.

## Why it may matter

The route has progressively removed several apparent resources that were artifacts of representation or positive closure: favorable gcd sectors, generic well-factorability, residual coefficient signs, complete-period resonance, full inclusion-exclusion, hard-mask Fourier expansion, generic Hilbert-space averaging, coefficient-uniform restriction, and now unsigned Selberg-envelope accuracy. The low-denominator envelope remains the first surviving representation in this chain whose individual character modes and aggregate absolute coefficient mass both fit a polynomial source budget.

If its false-positive leakage can also be coupled to `K_h` with a conductor-sensitive saving, the base component would genuinely evade the full-primorial obstructions of `MC-473`--`MC-475`. If every legitimate treatment of that leakage either costs its full positive mass or loses the `K_h`-specific gain under positive closure, the main restriction-style escape is closed and attention should redirect to boundary/nonempty components or pre-positive cross-component interference.

## Decisive test

Work in the `R=T=1` empty-vector source frame and retain the centering from `MC-472`. Use the actual Bera--Viswanadham/Ramaré--Ruzsa enveloping object or one precisely specified signed/truncated/factorable replacement; do not revert to the exact full-primorial Fourier frame already closed by `MC-473`--`MC-475`.

For the actual Selberg envelope, start from the exact leakage identity from `MC-479`, not from pointwise majorization. Derive a valid estimate or structural decomposition for

\[
\sum_{n\in I}K_h(n)L_{W,h}(n)
\]

that retains `K_h` information. Charge the resulting terms explicitly against the conductor-sensitive envelope budget

\[
\frac{z^2(\log(2z))^5}{G(z)}\sqrt p\log(2p)
\]

from `MC-478`, together with source interval length, shell summation, Fejér weights, coefficient normalization, endpoint separation, and source depth from the staged architecture.

Accept the route only if the complete accounting gives a strict conductor-power gain for the exact base component. Kill the Selberg-envelope transfer if every legitimate leakage decomposition has trivial-scale positive mass after the phase is discarded, and no `K_h`-sensitive estimate survives. A different signed surrogate remains admissible only if its exact matching/error theorem is proved rather than inferred from majorization.

For mixed/boundary terms, use the exact first-exit decomposition from `MC-470`; for nonempty pieces, retain the exact bin-product support pruning; for cross-component interference, retain the signed finite decomposition through the proposed transform and exhibit a concrete surviving cross term rather than appealing to cancellation after separate absolute bounds.

## Evidence boundary

`MC-477` proves only a denominator-independent character estimate for each low-denominator rational mode and a crude envelope recombination. `MC-478` improves only that envelope recombination by exploiting exact local pair-sieve Fourier factorization. `MC-479` proves that the Selberg envelope is exact on survivors but has order-one false positives near the cutoff and only logarithmically suppressed unsigned leakage on the complete local period. None of these results controls the **twisted** leakage sum on the actual source interval, boundary terms, nonempty components, or cross-component interference.

The displayed low-denominator budget is an upper bound for one coefficientwise envelope treatment, not a lower bound or an optimal barrier. The complete-period leakage lower bound is an adversarial control against phase-blind replacement, not a short-interval lower bound. No conductor-power estimate for the exact rough×rough discrepancy, Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted`, but the restriction-style branch is narrower again. The low-denominator character modes and their aggregate pair-sieve `ell^1` cost survive and are priced by `MC-477`--`MC-478`; `MC-479` eliminates unsigned envelope accuracy as the missing mechanism. The immediate unresolved question is now the **translated-character sum against Selberg false-positive leakage**, or an exact signed/factorable surrogate that removes that leakage without sacrificing the conductor gain.