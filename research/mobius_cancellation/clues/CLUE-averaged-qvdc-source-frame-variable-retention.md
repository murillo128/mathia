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
  - research/mobius_cancellation/findings/MC-480-selberg-leakage-complete-period-phase-factorizes.md
  - research/mobius_cancellation/findings/MC-481-centered-selberg-leakage-is-target-equivalent-modulo-envelope.md
  - research/mobius_cancellation/findings/MC-482-two-sided-beta-sieve-transfer-forces-a-polylogarithmic-cutoff.md
  - research/mobius_cancellation/findings/MC-483-well-factorable-bracket-width-does-not-transfer-the-signed-error.md
  - research/mobius_cancellation/findings/MC-484-buchstab-first-exit-removes-selector-but-preserves-dimension-two.md
  - research/mobius_cancellation/findings/MC-485-complete-q-shift-frame-coefficient-blind-l2-ceiling.md
  - research/mobius_cancellation/findings/MC-486-incomplete-q-subframes-remain-l2-tight.md
  - research/mobius_cancellation/findings/MC-487-first-exit-inverse-shifts-are-affine-gauge.md
  - research/mobius_cancellation/findings/MC-488-first-exit-cells-form-disjoint-source-partition.md
---

# Can a q-dependent transform of the normalized first-exit family beat the Möbius source-frame tariff?

## Observation

The empty-vector source has survived a long sequence of exact reductions but most generic summaries are now closed. `MC-472`--`MC-476` rule out direct full-period, inclusion-exclusion, hard-mask Fourier, plain Parseval and coefficient-blind restriction routes. `MC-477`--`MC-483` show that positive or bracketed sieve surrogates either leak too much, retain the hard-mask selector, or force only a polylogarithmic useful cutoff when one demands a fixed conductor-power gain.

`MC-484` supplied the canonical selector-free escape: exact Buchstab first exit writes the hard mask as a signed sum over first-exit primes `q`, leaving a dimension-two residual pair sieve. `MC-485`--`MC-486` show that the bare complete or incomplete inverse-shift phase family has no generic coefficient-blind `L^2` gain once moving coefficients are frozen. `MC-487` then shows that the common inverse shifts `hq^{-1}` in the phase and residual sieve are affine gauge: in an intrinsic integer coordinate the translated-ratio separation and pair polynomial are fixed, while q-dependence moves to support, cutoff, endpoints and coefficients.

`MC-488` closes one more apparent source of extra dimensionality. The **exact progression-plus-cutoff first-exit cells are disjoint**: each source integer in the Buchstab shell has a unique least active prime divisor `q_*(n)`. Their incidence Gram matrix is diagonal, and every common unitary/Parseval transform preserves that orthogonality. If the outer coefficient is common, the q-sum refolds exactly to the original hard-mask difference; with q-dependent coefficients it becomes a one-variable weight `c_{q_*(n)}(n)`.

The accepted continuation is therefore narrower again. The live resource is **not** overlap of exact normalized q-supports under a common transform. It must be a transform whose arithmetic itself depends on `q`, an exact outer coefficient that uses the least-prime label nontrivially, or a pre-positive factor-specific construction in which q enters a separate modulus/phase role before the first-exit partition refolds.

## Research question

Can the exact normalized first-exit family be passed through a justified **q-dependent** dispersion, completion, reciprocity, Poisson, or staged-factor operation for which distinct first-exit labels occupy genuinely different arithmetic roles and the resulting off-diagonal kernel yields a fixed conductor-power gain after all diagonals, endpoints and source weights are restored?

Equivalently, can the actual coefficient `c_{q_*(n)}(n)` be shown to carry arithmetic structure strong enough to beat the known harmonic/endpoint tariff without replacing the exact first-exit cutoff by an uncontrolled envelope? If neither route survives, the empty-vector first-exit continuation should be closed and research should return to the separately retained nonempty rough-block, boundary or pre-positive cross-component channels.

## Why it may matter

The normalization now distinguishes bookkeeping from genuine source structure. Buchstab first exit remains useful because it removes the `MC-483` bracket selector without positive replacement, but the outer q-label is deterministic on the exact source shell. A common Fourier or Hilbert-space transform cannot turn that deterministic partition into a new averaging dimension.

The surviving possibility is exactly the type of asymmetry identified in `MC-456`: in successful neighboring dispersion arguments, factor labels become analytically visible because they enter different modulus or reciprocal-phase roles **before** positive closure. A valid continuation here must produce that kind of q-dependent arithmetic operation from the exact Möbius source frame, not merely rewrite the disjoint first-exit cells in another common basis.

## Decisive test

Work first in the `R=T=1` empty-vector source frame and normalize to the common intrinsic source coordinate. Keep the exact first-exit cell

\[
E_q=\{n:q\mid n(n+h),\ (n(n+h),P(q))=1\}
\]

with exact interval endpoints and source coefficients. Before estimating anything, identify the proposed row operator `U_q` or transformed kernel and verify that it is **genuinely q-dependent** in an arithmetic way. There must exist distinct first-exit labels for which the transformed interaction is not obtainable from one common source isometry or relabeling.

Reject a route immediately if it applies the same unitary/completion to every exact row and expects cross-q dispersion: `MC-488` makes the full row Gram diagonal before and after every common unitary transform. Reject a route that drops `A_q` merely to recover overlap of the bare progressions `q|n` or `q|n+h`; that changes the exact first-exit family and must pay the positive/bracket transfer barriers of `MC-479`--`MC-483`.

For a surviving q-dependent transform, compute the true off-diagonal and diagonal terms before claiming gain. Accept the route only if the final estimate saves a fixed conductor power after coefficient normalization, dyadic q summation, endpoint costs, root collisions, shell reconstruction and all q-vdC/Fejér/staged-sieve weights are restored. A per-q estimate followed by triangle inequality is insufficient unless its aggregate already beats the existing first-exit budget.

A second admissible route is to prove a special property of the actual least-prime-weighted coefficient `c_{q_*(n)}(n)`. Such a property must be arithmetic and quantitative; the deterministic q-label alone is not enough.

## Evidence boundary

`MC-484` proves exact selector-free Buchstab first exit and the residual dimension-two pair sieve. `MC-485`--`MC-486` close complete and incomplete coefficient-blind inverse-shift frame routes. `MC-487` proves that the shared inverse shifts are affine gauge. `MC-488` proves that the exact normalized progression-plus-cutoff cells form a disjoint least-prime partition and remain orthogonal under every common unitary transform.

None of these findings proves or rules out a genuinely q-dependent dispersion/completion theorem, a special arithmetic estimate for the exact coefficient `c_{q_*(n)}(n)`, a conductor-power saving, or an improved bound for the Möbius function. `MC-456` supplies only a neighboring quotient-breaking template whose factor-specific modulus geometry must still be derived here.

## Research disposition

The clue remains `accepted`, but its admission gate is now strict. Closed routes include: positive/bracket replacement without transfer control; complete or incomplete coefficient-blind inverse-shift averaging; exploiting the visible `hq^{-1}` motion; and seeking cross-q dispersion from the exact first-exit support/cutoff family through one common source transform.

The active test is now **q-dependent arithmetic transformation or exact least-prime-weight structure before positive closure**. If no such operation can be derived from the source frame with a quantitative gain, the normalized empty-vector first-exit branch should be treated as exhausted rather than revisiting another coordinate version of the same partition.