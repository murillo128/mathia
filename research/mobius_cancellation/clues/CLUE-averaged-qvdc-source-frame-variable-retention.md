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
  - research/mobius_cancellation/findings/MC-489-first-exit-rowwise-dilation-retains-p-scale-diagonal.md
  - research/mobius_cancellation/findings/MC-490-sifted-rowwise-subframes-are-riesz-stable.md
  - research/mobius_cancellation/findings/MC-491-repeated-residue-first-exit-rows-have-logarithmic-coherence.md
  - research/mobius_cancellation/findings/MC-492-native-repeated-residue-blocks-have-no-common-sign-cancellation.md
  - research/mobius_cancellation/findings/MC-493-native-cross-root-blocks-need-square-root-multiplicity.md
  - research/mobius_cancellation/findings/MC-494-complete-repeated-residue-blocks-tensorize-before-root-interference.md
  - research/mobius_cancellation/findings/MC-495-incomplete-cross-root-multiplicity-collapses-to-weighted-character-bias.md
  - research/mobius_cancellation/findings/MC-496-endpoint-only-cross-root-bias-has-a-square-root-conductor-threshold.md
  - research/mobius_cancellation/findings/MC-497-quadratic-short-overlap-bias-requires-exceptional-starts.md
  - research/mobius_cancellation/findings/MC-498-endpoint-start-bias-is-priced-by-effective-quotient-fibres.md
  - research/mobius_cancellation/findings/MC-499-endpoint-start-dispersion-has-a-source-population-ceiling.md
  - research/mobius_cancellation/findings/MC-500-dyadic-endpoint-quotient-support-has-q-free-square-root-ceiling.md
  - research/mobius_cancellation/findings/MC-501-dyadic-endpoint-certificate-has-q-free-source-width-barrier.md
  - research/mobius_cancellation/findings/MC-502-cross-root-first-exit-rows-have-q-plus-r-logarithmic-sieve-coherence.md
  - research/mobius_cancellation/findings/MC-503-fixed-hard-mask-profiles-obey-effective-support-start-tariff.md
  - research/mobius_cancellation/findings/MC-504-profile-start-participation-obeys-product-tariff.md
  - research/mobius_cancellation/findings/MC-505-varying-profile-bias-sees-only-centered-matched-fourier-diagonal.md
  - research/mobius_cancellation/findings/MC-506-anti-diagonal-pushforward-reduces-bias-to-excess-collisions.md
  - research/mobius_cancellation/findings/MC-507-uniform-marginals-do-not-control-anti-diagonal-collisions.md
  - research/mobius_cancellation/findings/MC-508-fixed-conductor-phase-leaves-finite-mask-coordinates-programmable.md
---

# Can localized full-profile coupling beat the Möbius source-frame tariff?

## Observation

The normalized empty-vector first-exit branch has survived a long chain of exact reductions, but most generic uses of the first-exit label are closed. `MC-472`--`MC-495` eliminate direct completion, coefficient-blind phase averaging, affine inverse shifts, multiplicity-only repeated-residue effects, and several positive or bracketed sieve replacements. The incomplete two-root problem reduces to one nonnegative source-derived weight against an explicit relative conductor-character phase.

The endpoint branch is already sharply staged. `MC-496`--`MC-501` show that endpoint-only bias must pass, in order, the Q-free source-width gate, the Q-free source-location gate, the per-block population gate, and finally the exact winning-endpoint participation/fibre tariff. Failure of an early gate makes the present endpoint certificate method-limited rather than proving true phase bias.

The lower-prime hard-mask branch has now narrowed further. `MC-502` shows that complete-period plus/minus mask coherence is only logarithmic/totient-sized. `MC-503` shows that a fixed exact incomplete profile has large normalized quadratic bias only on a sparse set of conductor starts controlled by its effective support. `MC-504` removes the artificial uniform-start assumption: for conditional start participation `R_a` and profile support `R_b`, fixed normalized bias requires `R_aR_b` at most conductor scale.

`MC-505` then removes the need to choose profile classes at all. For a general start/profile coefficient table `B`, the centered conductor kernel sees only the matched Fourier diagonal of the doubly centered interaction. `MC-506` gives the corresponding physical-space currency: after pushing the nonnegative mass by the actual sum coordinate `t=x+j`, large normalized bias requires excess collision mass of that pushforward. `MC-507` proves that uniform or otherwise well-controlled start and profile marginals do not control those anti-diagonal collisions; the required theorem must use the physical coupling itself.

`MC-508` rules out the first weak version of such coupling. At fixed conductor phase, every fixed finite set of lower-prime moving mask roots can be prescribed arbitrarily by CRT and Dirichlet once the realizing first-exit prime `q` is allowed to escape the active source scale. Therefore finitely many local congruence coordinates cannot be the missing rigidity. Any useful dependence must be destroyed by that nonlocalized control: the full growing profile over all lower primes, the moving cutoff/order carried by `q`, tight localization of `q` in the physical source range, or the archimedean quotient/start/endpoints and reconstruction weights.

## Research question

Does the **actual localized first-exit source**, with `q` constrained to its physical source block and with its entire growing lower-prime profile and archimedean row geometry retained, force subcritical excess collisions in the `MC-506` physical sum coordinate?

Equivalently, can the source-derived coefficient measure on start/profile-offset pairs be shown not to concentrate on anti-diagonals strongly enough to sustain fixed conductor bias, using a mechanism that genuinely fails for the nonlocalized finite-coordinate CRT controls of `MC-508`? If such a theorem exists, identify exactly whether its rigidity comes from the growing mask dimension, the moving cutoff `q`, source localization, quotient/end-point geometry, or a genuinely signed/complex pre-aggregation coefficient. If none survives all reconstruction costs, the normalized empty-vector first-exit continuation should be closed and attention returned to separately retained nonempty rough-block, boundary, or pre-positive cross-component channels.

## Why it may matter

The remaining hard-mask question is no longer generic “profile/start dependence.” It has an exact target and an adversarial control. `MC-506` says the only load-bearing statistic for the centered conductor kernel is excess collision mass after the physical addition map; `MC-507` says marginal regularity cannot bound it; and `MC-508` says any fixed finite local residue description can be matched while keeping conductor phase fixed if localization is dropped.

This sharply separates a potentially arithmetic phenomenon from a representation artifact. A successful estimate must use scale-growing or archimedean structure that is genuinely present in the first-exit source. Conversely, if a matched nonlocalized control reproduces the same collision behaviour, the proposed mechanism has not found rational-prime-specific rigidity.

## Decisive test

Work in the `R=T=1` empty-vector source frame and retain the exact first-exit cells, shortened endpoints, lower-prime hard masks, source/reconstruction coefficients, and the actual source range of every first-exit label.

For the endpoint-only branch, keep the existing staged audit unchanged: apply the `MC-501` Q-free width gate and `MC-500` Q-free location gate first, then the `MC-499` per-block population gate, and only on surviving blocks the exact `MC-498` winning-endpoint participation/fibre test.

For the hard-mask branch, form the exact nonnegative source coefficient table `B_{x,j}` in the physical conductor start `x` and profile offset `j`. Push this mass through `t=x+j` as in `MC-506` and measure the normalized collision excess

\[
\Delta=p\sum_t\nu(t)^2-1,
\]

with `nu` the normalized pushforward. The target is a bound on `Delta` strong enough, after all shell and reconstruction costs, to force the required conductor saving.

Stress-test any proposed bound against matched controls from `MC-508`: fix the conductor residue of `q` and any selected finite set of local lower-prime mask roots, but remove tight localization and realize the same finite data by primes in the resulting CRT class. A valid positive theorem must identify a hypothesis absent from these controls and prove that it is quantitatively used. Candidates include the full growing lower-prime profile, the moving cutoff/order `q`, the actual narrow source interval, or the archimedean quotient/start geometry. Another theorem about finitely many local mask residues does not pass.

The complete auxiliary-sieve component remains charged separately by the `MC-502` `q+r` coherence ceiling. Do not replace the exact source measure by a smooth, uniform, random, independent, or interval model unless the replacement error is quantitatively transferred. For any pre-aggregation alternative, identify the first exact formula where two first-exit labels occupy genuinely different arithmetic roles; scalar row factors, affine relabelings, multiplicity, complete-period collision factors, fixed nonnegative profiles, marginal regularity, and finite local mask coordinates are already closed mechanisms.

## Evidence boundary

`MC-484` proves selector-free Buchstab first exit while retaining the dimension-two pair sieve. `MC-485`--`MC-495` close coefficient-blind phase-frame, affine-shift, partition, dilation, completed repeated-residue, and multiplicity-only loopholes. `MC-496`--`MC-501` stage the endpoint certificate through exact width, location, population, and participation constraints.

For the hard-mask branch, `MC-502` closes complete-period coherence at logarithmic/totient scale. `MC-503` prices fixed-profile exceptional starts. `MC-504` prices actual conditional start participation jointly with profile support. `MC-505` identifies the centered matched Fourier diagonal as the complete varying-profile interaction seen by the conductor kernel. `MC-506` converts that interaction into an exact physical anti-diagonal collision statistic. `MC-507` proves that the marginals do not control this statistic. `MC-508` proves that fixed finite local mask coordinates remain programmable at fixed conductor phase once tight prime localization is removed.

None of these findings bounds the anti-diagonal collision excess for the **actual localized full growing first-exit profile**, proves that source localization supplies the missing rigidity, derives a new pre-aggregation signed/complex coefficient, evaluates every material endpoint regime, or improves `M(x)`. `MC-456` remains only a neighboring positive template; it is not evidence that the required quotient-breaking structure exists here.

## Research disposition

The clue remains `accepted`. The endpoint audit retains its existing four-stage gate. The lower-prime branch is now staged as: complete-period coherence closed by `MC-502`; fixed-profile and conditional-participation tariffs imposed by `MC-503`--`MC-504`; arbitrary profile variation reduced by `MC-505`--`MC-506` to physical anti-diagonal collisions; marginal control ruled out by `MC-507`; and finite local congruence rigidity ruled out by `MC-508` without localization. The live mechanism is therefore **localized, scale-growing full-profile/archimedean source coupling**, or a genuinely q-specific signed/complex pre-aggregation operation.