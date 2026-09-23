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
---

# Can the normalized first-exit source family beat the Möbius source-frame tariff?

## Observation

The empty-vector source has survived a long sequence of exact reductions but most obvious summaries have now been closed. `MC-472`--`MC-476` rule out direct full-period, inclusion-exclusion, hard-mask Fourier, plain Parseval and coefficient-blind restriction routes. `MC-477`--`MC-483` show that positive or bracketed sieve surrogates either leak too much, retain the hard-mask selector, or force only a polylogarithmic useful cutoff when one demands a fixed conductor-power gain.

`MC-484` supplied the canonical selector-free escape: exact Buchstab first exit writes the hard mask as a signed sum over first-exit primes `q`, leaving a dimension-two residual pair sieve on intervals of length about `H/q`. In the root coordinate `n=a+qm`, both the translated-ratio character phase and the residual pair-sieve mask carry the same inverse-dilation separation `h q^{-1}`. `MC-485`--`MC-486` then show that the bare complete or incomplete inverse-shift phase family has no generic coefficient-blind `L^2` gain below the natural `sqrt(p)` scale once the moving coefficients are frozen.

`MC-487` sharpens the representation again. The common inverse shifts are **affine gauge**, not an independent source variable. On each root branch, returning to the intrinsic integer coordinate (`x=qm=n` on the zero root, or `x=qm=n+h` on the other root) removes the `h q^{-1}` motion simultaneously from the character phase and from the pair-sieve root separation. The fixed translated-ratio kernel has separation `h`; the fixed pair polynomial is `x(x+h)` or `x(x-h)`. What genuinely remains q-dependent is the arithmetic-progression support, exact endpoints, nested roughness cutoff `P(q)`, and the actual outer/staged coefficients.

The accepted continuation is therefore narrower. **The live resource is not motion of the inverse shifts. It is cross-q interaction among the normalized progression supports, changing cutoffs and exact source weights, or a separately proved special alignment of those coefficients.** Any argument whose only q-sensitive ingredient is the visible family `h q^{-1}` has failed the gauge test before analytic estimation begins.

## Research question

After branchwise affine normalization, does the exact first-exit family

\[
\sum_{w\le q<z}
\sum_{x\in J_{q,a}}
 c_{q,a}(x)
 K_{\pm h}(x)
 \mathbf 1_{(x(x\pm h),P(q))=1}
\]

with `J_{q,a}` the exact q-progression/endpoint set induced by the root branch, admit a conductor-sensitive bilinear, dispersion, reciprocity or staged-factor estimate that uses the **joint q-dependence of progression incidence, nested cutoff and actual source coefficients before absolute values**?

If not, can one prove a source-specific obstruction showing that every admissible recombination of this normalized family collapses to the known harmonic/endpoint, full-frequency, positive-envelope or coefficient-blind tariffs? The separately retained nonempty rough-block, first-exit boundary and pre-positive cross-component channels remain alternatives if the normalized empty-vector first-exit family is killed.

## Why it may matter

The normalized formulation removes a coordinate artifact from the frontier. `MC-484` remains important because first exit eliminates the `MC-483` selector without replacing the hard mask by a positive surrogate, but `MC-487` shows that the apparent coupling of two moving inverse shifts is only how the fixed source pair looks after division by `q`. This prevents spending further effort on reciprocity or frame arguments whose only input is that common shift motion.

At the same time, normalization does not trivialize cross-q recombination. The affine change is row-dependent, so a common intrinsic coordinate turns the family into different arithmetic-progressions with different `P(q)` cutoffs rather than one common coefficient vector. That is exactly the structure absent from `MC-485`--`MC-486`. A genuine gain must therefore be visible in the incidence/cutoff/weight family itself.

## Decisive test

Work first in the `R=T=1` empty-vector source frame and split first-exit primes into dyadic blocks. **Normalize each root branch to the intrinsic integer coordinate before proposing a new estimate.** Retain simultaneously the exact progression condition induced by `q`, the source interval endpoints, the fixed translated-ratio separation `±h`, the exact residual pair-sieve cutoff `P(q)`, and the outer q-vdC/Fejér/staged-sieve coefficients actually present in the source frame.

Accept the route only if a proved cross-q estimate gains a fixed conductor power after all coefficient normalizations, shell summations, endpoint terms and diagonal costs are restored. The gain must occur before replacing the `q` sum by absolute values. A per-q estimate followed by triangle inequality is insufficient unless its aggregate already beats the first-exit harmonic/endpoint budget.

Reject any argument that derives its gain only from the family of inverse shifts `h q^{-1}`: `MC-487` removes those shifts branchwise. Reject any argument that then freezes or common-majorizes the progression/cutoff profile and invokes only a phase-frame norm: `MC-485`--`MC-486` close that coefficient-blind architecture. Expansion of the exact hard mask must still pass the exponential branch/frequency tariffs of `MC-473`--`MC-475`, and positive replacement must still pass the transfer barriers of `MC-479`--`MC-483`.

A promising continuation must instead exhibit one of the following in exact form: a dispersion identity coupling distinct q-progressions, a nested-cutoff cancellation unavailable rowwise, a bilinear/factorable structure surviving dimension two, or a proved arithmetic alignment of the actual outer coefficients with the normalized source family. If none yields a conductor-power gain, close this continuation and return to the already separated nonempty/boundary/pre-positive channels rather than reintroducing the inverse-shift coordinate.

## Evidence boundary

`MC-484` proves the exact selector-free Buchstab decomposition and residual dimension-two pair sieve. `MC-485`--`MC-486` prove complete and incomplete coefficient-blind phase-frame obstructions after moving coefficients are frozen. `MC-487` proves that the simultaneous inverse shifts in the phase and pair sieve are branchwise affine gauge and that normalization transfers q-dependence to support/cutoff/weights.

None of those findings proves a bilinear estimate for the normalized cross-q family, a conductor-power saving, a dimension-two analogue of the linear Rosser-Iwaniec remainder theorem, or an improved bound for the Möbius function. Classical Buchstab/switching and character-sum literature supplies the underlying operations; absence of a directly applicable theorem in the targeted audit is not a novelty claim.

## Research disposition

The clue remains `accepted`, but the target is narrowed. The immediate question is no longer whether exact first exit exists, whether complete/incomplete inverse-shift frames produce a coefficient-blind gain, or whether the shared motion `h q^{-1}` itself is exploitable. Those routes are closed by `MC-484`--`MC-487`.

The active test is now the **affine-normalized first-exit progression/cutoff family with its exact source weights retained**. If that family cannot beat the harmonic/endpoint budget before absolute values, the empty-vector first-exit continuation should be regarded as closed and research should move to the already separated alternative channels.