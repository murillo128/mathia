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
---

# Can load-bearing q-dependent arithmetic asymmetry beat the Möbius source-frame tariff?

## Observation

The normalized empty-vector source has survived a long chain of exact reductions, but most generic uses of the first-exit label are now closed. `MC-472`--`MC-483` eliminate direct completion, hard-mask Fourier/Parseval, coefficient-blind restriction, and positive or bracketed sieve replacements as routes to a fixed conductor-power gain. `MC-484` supplies the canonical lossless escape: exact Buchstab first exit removes the bracket selector while retaining a dimension-two residual pair sieve and an explicit prime label `q`.

`MC-485`--`MC-495` then show that most visible q-dependence is not load-bearing. Inverse shifts are affine gauge, exact first-exit cells form a deterministic least-prime partition, rowwise dilation retains the conductor-scale diagonal, small/repeated-residue completed subframes are stable, native same-root repeated-residue blocks have constructive rather than destructive interference, and both completed and incomplete repeated-residue multiplicity collapse before they can create new conductor directions. The incomplete two-root problem reduces to one nonnegative source-derived weight against one explicit relative character phase.

The endpoint part of that weight is now much more tightly priced. `MC-496` rules out endpoint-only order-one bias when weighted overlap lengths are above the square-root completion scale. `MC-497` shows in the quadratic case that shorter dangerous intervals must begin at a sparse exceptional set of **physical** conductor starts. `MC-498` converts that exceptional-set condition into a weighted source-frame inequality: within a dyadic overlap-length band, endpoint bias is controlled by the `l1/l2` effective support of the actual start pushforward, while the physical quotient maps `ceil(X/q)` and `ceil((X+h)/r)` have explicit deterministic fibre costs.

`MC-499` adds a necessary population gate before that detailed weight audit. In one repeated-residue dyadic block the physical start is always one of the two winning endpoints, so the effective start support is at most `2(1+Q/p)`. Consequently the `MC-497`/`MC-498` second-moment certificate cannot close a block by start dispersion unless the available label population is already larger than the short-overlap tariff `T_{p,H}`. Below that scale a failed `kappa/D` test is forced by cardinality and must not be misdiagnosed as unusual coefficient localization or arithmetic concentration.

`MC-500` closes the apparent escape of increasing `Q` to create more repeated-residue labels. On a dyadic block, each endpoint image has at most `min(1+Q/p,2+Z/(2Q))` distinct physical quotient values. Thus label growth `Q/p` and quotient compression `Z/Q` compensate, giving the Q-free ceiling `R_start <= 4+sqrt(X/(2p))+sqrt((X+h)/(2p))`. The current exceptional-start certificate can therefore work at some dyadic scale only if the source height itself is large enough relative to `p T_{p,H}^2`.

Thus the endpoint-only loophole now has a three-stage admission test: first a Q-free source-height feasibility gate, then per-block source-population feasibility, and only then exact reconstruction participation/fibres. Independently, the lower-prime pair-sieve profile inside the overlap and a genuinely q-dependent pre-aggregation sign/phase/modulus remain live arithmetic channels.

## Research question

Can the exact normalized first-exit family produce either of the two remaining load-bearing resources?

First, do the physical source height and overlap-length regime even permit the `MC-498` endpoint-dispersion certificate at **any** dyadic first-exit scale? If the Q-free `MC-500` gate passes, which material dyadic q/overlap blocks then have enough repeated-residue labels to pass `MC-499`? On those blocks, do the true outer/staged winning-endpoint weights satisfy the stronger `MC-498` participation/fibre threshold? If a population-feasible block still fails, what exact quotient folding, side imbalance, or coefficient concentration causes the loss, and does that structure itself carry usable arithmetic information?

Second, beyond endpoints, can the exact lower-prime hard masks or another source operation create a centered conductor weight with fixed negative correlation against the relative phase, or create a genuinely q-dependent signed/complex coefficient, modulus, or reciprocal-phase role **before** the nonnegative aggregation of `MC-495`? The latter must be analogous in substance, not merely vocabulary, to the factor-specific quotient breaking isolated in `MC-456`.

If neither resource survives with all reconstruction costs restored, the normalized empty-vector first-exit continuation should be closed and research should return to separately retained nonempty rough-block, boundary, or pre-positive cross-component channels.

## Why it may matter

The surviving question is no longer whether more averaging variables can be exposed. The exact reductions repeatedly show that visible multiplicity, shifts, support labels and endpoint incompleteness can collapse to lower-dimensional or positive objects before they yield cancellation. `MC-498` replaces a distributional guess about exceptional starts by quantities computed directly from the source coefficients; `MC-499` shows that those quantities are worth computing only after a source-population gate; `MC-500` shows that even population can be a misleading optimization variable because reciprocal quotient compression imposes a source-height ceiling independent of `Q`.

That separates three negative outcomes. Failure of the Q-free `MC-500` gate means the whole endpoint-dispersion certificate is method-limited throughout the dyadic first-exit range. Passing `MC-500` but failing `MC-499` identifies a particular block as method-limited by label population. Only a block that passes both gates but has poor `kappa/D` raises a genuine source-localization, quotient-folding, or winning-side imbalance question. This prevents detailed coefficient audits in regimes where the present second-moment method is structurally incapable of succeeding.

## Decisive test

Work in the `R=T=1` empty-vector source frame and keep the exact first-exit cell

\[
E_q=\{n:q\mid n(n+h),\ (n(n+h),P(q))=1\}
\]

with exact shortened endpoints and all source/reconstruction coefficients. Reject proposals whose only q-dependence is already priced by `MC-485`--`MC-500`: coefficient-blind complete/incomplete phase averaging, affine inverse shifts, common transforms of disjoint first-exit cells, rowwise dilation followed by positive `L^2` closure, scalar reweighting, bare repeated-residue multiplicity, long endpoint overlaps, or short endpoint overlaps without the source-height/population/effective-support audit.

For the quadratic endpoint-only branch, partition the material source into dyadic overlap-length bands and compute

\[
T_{p,H}=\frac pH\log^2(2H)+\sqrt p\log(2H).
\]

Before choosing a dyadic first-exit scale, put `Z_*=max(X,X+h)` and test the Q-free ceiling from `MC-500`. If

\[
T_{p,H}
\not\ll_\delta
4+\sqrt{2Z_*/p}
\]

at the target normalized saving `delta`, record that source-height/length regime as method-limited for the current exceptional-start second moment: no dyadic `Q` can supply enough physical start diversity, so detailed reconstruction weights cannot repair the certificate.

Only when the Q-free gate is feasible should each repeated-residue dyadic q-block be compared with the `MC-499` population ceiling `1+Q/p` (or the exact active-label count when available). If the available population is not larger than `T_{p,H}` by the margin required for the target saving, record that block as method-limited by population; a failed participation ratio carries no further localization information.

Only for blocks passing both gates form the actual nonnegative pair weights, split them by the winning physical start `max(ceil(X/q),ceil((X+h)/r))`, and compute the induced weights `gamma_q`, `delta_r`, their participation ratios `kappa_+`, `kappa_-`, and the quotient-fibre costs `D_+`, `D_-` from `MC-498`. Charge the number of dyadic blocks and the original shell/reconstruction weights. If the `MC-498` threshold holds with enough margin after these costs, treat endpoint-only bias as closed on that block. If it fails despite ample source height and label population, isolate the smallest weighted block responsible and determine whether the loss comes from quotient folding, winning-side imbalance, or genuine coefficient localization/arithmetic structure.

For the remaining incomplete hard-mask route, compute the exact projected overlap weight

\[
w(t)=\sum_{m\equiv t\ (p)}A(m)B(m)
\]

with the lower-prime pair-sieve factors retained, and estimate the centered correlation with `chi(1-t^{-2})` without replacing `w` by a smooth, uniform, random, or interval model unless the replacement error is quantitatively transferred.

For a pre-aggregation proposal, identify the first exact formula where two first-exit labels occupy genuinely different arithmetic roles inside the transformed kernel or coefficient: a q-dependent modulus, reciprocal phase, or `m`-dependent sign/complex coefficient not removable by affine relabeling. A harmless scalar row factor or increased multiplicity does not pass.

## Evidence boundary

`MC-484` proves exact selector-free Buchstab first exit and preserves the dimension-two pair sieve. `MC-485`--`MC-495` close coefficient-blind phase-frame, affine-shift, partition, dilation, completed repeated-residue and multiplicity-only loopholes, leaving one weighted incomplete relative-phase correlation. `MC-496` closes long endpoint-only overlaps, `MC-497` makes short dangerous starts sparse in the quadratic case, `MC-498` supplies a deterministic effective-support/fibre criterion for the actual endpoint start map, `MC-499` proves that repeated-residue label population can make that criterion infeasible before coefficient localization is considered, and `MC-500` proves that reciprocal quotient compression imposes a Q-free source-height ceiling on the start diversity available to the same certificate.

None of these findings checks the actual source-height gate in every material overlap-length regime, classifies the surviving dyadic blocks by `MC-499`, evaluates the `MC-498` participation ratios on doubly feasible blocks for the full q-vdC reconstruction, controls the lower-prime hard-mask contribution to the conductor profile, derives a new q-dependent signed/complex pre-aggregation coefficient, or improves `M(x)`. `MC-456` remains a neighboring positive template only; it is not evidence that the required quotient-breaking structure exists here.

## Research disposition

The clue remains `accepted`. The endpoint test is now explicitly staged: **apply the MC-500 Q-free source-height gate first; only surviving regimes proceed to the MC-499 per-block population gate; only doubly feasible blocks proceed to the exact MC-498 winning-endpoint participation/fibre audit**. Failure at either of the first two stages is a limitation of the present endpoint-dispersion certificate, not evidence for true phase bias. A failure after both gates pass is the first regime where source concentration/folding becomes diagnostically meaningful. In parallel, lower-prime hard-mask phase selectivity and genuinely q-specific pre-aggregation arithmetic asymmetry remain independent admissible routes.