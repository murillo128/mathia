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
  - research/mobius_cancellation/findings/MC-509-localized-growing-mask-state-becomes-source-injective.md
  - research/mobius_cancellation/findings/MC-510-localized-relative-mask-state-is-pair-injective.md
  - research/mobius_cancellation/findings/MC-511-relative-state-recurrence-loses-collision-budget-before-reconstruction.md
---

# Can localized cross-state coupling beat the Möbius source-frame tariff?

## Observation

The normalized empty-vector first-exit branch has survived a long chain of exact reductions, but the lower-prime hard-mask route is now much narrower than a generic “full-profile coupling” question. `MC-505`--`MC-506` show that the centered conductor kernel sees only the physical pushforward by `t=x+j`, with fixed bias requiring excess collision mass. `MC-507` shows that row/column marginals and unitary-invariant matrix summaries do not control that pushforward. `MC-508` then excludes fixed finite local-mask rigidity when source localization is removed.

Localization does create rigidity, but `MC-509` and `MC-510` show that exact growing mask coordinates pay for it by becoming source-addressing data. After quotienting the one-row affine gauge, the exact relative state is modular `q/r`; its fibres shrink according to a rational-reconstruction tariff and eventually become ordered-pair injective. `MC-511` sharpens the obstruction: if the physical pair-phase participation `R_*` is large enough, same-relative-state contributions can become negligible at the natural conductor collision scale even before pair injectivity. Material collision excess must then be carried by distinct exact states that merge only after the physical conductor pushforward.

## Research question

Does the **actual localized first-exit source** force enough dispersion of the many-to-one map from distinct gauge-invariant source states to the physical conductor coordinate `t=x+j` to make the `MC-506` excess collision statistic subcritical after all reconstruction costs?

Equivalently, after retaining pair provenance but not conditioning it away, can one bound cross-state physical collisions using the moving cutoff, endpoint/quotient geometry, lower-prime mask evolution, or another genuinely source-derived relation? If the effective pair-phase participation `R_*` is too small for the `MC-511` gate, determine what exact reconstruction concentration causes that failure rather than treating raw pair multiplicity as averaging. A genuinely signed or complex pre-aggregation coefficient remains a separate escape because the current collision reduction is nonnegative.

## Why it may matter

The remaining nonnegative route is now representation-specific. Longer exact profiles do not automatically help: finite profiles are programmable without localization, while sufficiently rich localized profiles become source labels, and their same-state collision budget can be exhausted before full reconstruction. A successful theorem must therefore control how **different** arithmetic states collapse under the physical addition map, not merely prove that the states are individually rigid or recurrent.

This gives a concrete way to distinguish arithmetic structure from representation artifacts. If cross-state collisions remain large under the exact localized source map, the hard-mask continuation survives but with a precise carrier. If they can be bounded below the `MC-506` threshold, the remaining nonnegative hard-mask route is closed and attention should move to the separately retained signed/complex pre-aggregation, nonempty rough-block, or boundary channels.

## Decisive test

Work in the exact `R=T=1` empty-vector source frame. Keep ordered source-pair provenance through the physical conductor pushforward. For each pair `u=(q,r)`, form its nonnegative contribution `b_u(t)` to `t=x+j`, its exact gauge-invariant relative state `Lambda_z(u)`, and the physical effective participation

\[
R_*=
\frac{W^2}{\sum_{u,t}b_u(t)^2}.
\]

Apply the `MC-510` relative-state fibre tariff first and the `MC-511` same-state collision gate second. If `R_* >> p` and `M_zR_* >> H(2Q+H)`, same-state collision recurrence is already negligible at scale `W^2/p`; do not spend further effort on deeper exact-state conditioning. Estimate instead the cross-state term

\[
C_{\rm cross}
=
\sum_t\sum_{\sigma\ne\tau}
 c_{\sigma,t}c_{\tau,t},
\]

and determine whether the exact source geometry forces it below the level compatible with material centered conductor bias.

Any proposed bound must identify a hypothesis absent from the nonlocalized CRT controls of `MC-508` and must preserve the physical source measure rather than replace it by a smooth, uniform, random, independent, or completed model without a quantitative transfer error. The endpoint-only branch keeps its existing `MC-500`/`MC-501`/`MC-499`/`MC-498` staged audit and is not reopened by this clue.

## Evidence boundary

`MC-509`--`MC-511` do **not** bound the total anti-diagonal collision excess. They show only that exact localized profile rigidity is not itself a free averaging resource and quantify when repeated exact-state collisions cannot carry the relevant second moment. Distinct states may still concentrate on the same physical conductor argument and may still align with the centered quadratic phase.

No persisted finding currently proves a useful lower bound for `R_*`, a cross-state collision estimate, a source-specific dispersion theorem for the map into `t=x+j`, a q-dependent signed/complex coefficient before nonnegative aggregation, or any improved bound for `M(x)`. These remain the missing premises.

## Research disposition

The clue remains `accepted`, but its live nonnegative mechanism is narrowed from generic localized full-profile coupling to **localized cross-state physical pushforward control**. Exact-state recurrence is now subject to the `MC-510` fibre tariff and the stronger `MC-511` collision-budget gate; the next useful result must estimate `R_*` from the exact reconstruction or control collisions between distinct relative states after the physical conductor map.