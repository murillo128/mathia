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
---

# Can load-bearing q-dependent arithmetic asymmetry beat the Möbius source-frame tariff?

## Observation

The normalized empty-vector source has survived a long sequence of exact reductions, but most generic uses of the first-exit label are now closed. `MC-472`--`MC-483` eliminate direct completion, hard-mask Fourier/Parseval, coefficient-blind restriction, and positive or bracketed sieve replacements as routes to a fixed conductor-power gain. `MC-484` supplies the canonical lossless escape: exact Buchstab first exit removes the bracket selector while retaining a dimension-two residual pair sieve and an explicit prime label `q`.

The subsequent chain shows that most visible q-dependence is not load-bearing. `MC-485`--`MC-486` close complete and incomplete coefficient-blind inverse-shift frame gains; `MC-487` identifies the common inverse shift as affine gauge; `MC-488` shows that exact first-exit cells are a disjoint least-prime partition; and `MC-489`--`MC-491` price rowwise dilation, distinct-residue conditioning, and repeated-residue mask coherence without producing a conductor-power saving.

The native repeated-residue branch is now especially rigid. `MC-492` proves that same-root rows with the Buchstab common sign cannot cancel even on incomplete domains. `MC-494` strengthens the completed cross-root analysis by showing that arbitrary repeated-residue multiplicity tensorizes into two nonnegative amplitudes before Jacobi interference. `MC-495` shows that the same aggregation happens **before completion as well**: on any incomplete common `m`-domain the whole repeated-residue two-root block reduces to

\[
U=K_a^+A,\qquad V=K_a^-B,
\]

with `A,B>=0`. The only possible destructive term is therefore

\[
C_{A,B}=\sum_m A(m)B(m)R_a(m),
\qquad
R_a(m)=\chi(am+h)\chi(am-h)\overline{\chi(am)}^2.
\]

After projection modulo `p`, this is one nonnegative source-derived weight `w(t)` against the fixed rational-character phase `chi(1-t^{-2})`. The uniform part of `w` is exactly the already-small complete Jacobi contribution; any larger incomplete effect must come from the centered conductor profile `w(t)-\bar w`. Thus repeated-residue multiplicity itself is closed even in the incomplete setting. What remains is a source-weight/phase correlation problem, or a pre-aggregation q-dependent sign/complex phase that prevents the collapse.

## Research question

Can the exact normalized first-exit family produce a justified operation in which the first-exit label `q` changes the **inner arithmetic coefficient or kernel** before positive closure, rather than only the row coordinate, scalar weight, support, or repeated-residue multiplicity?

There are now two precise surviving forms. First, derive the exact conductor projection `w(t)` created by endpoints, lower-prime cutoffs, pair-sieve masks and source coefficients, and prove that its centered component has a sufficiently strong negative correlation with the relative phase `chi(1-t^{-2})` to yield a fixed conductor-power gain after reconstruction. Second, derive a genuinely q-dependent signed/complex coefficient, modulus, or reciprocal-phase role before the aggregation step of `MC-495`, analogous in spirit to the factor-specific quotient-breaking mechanism isolated in `MC-456`.

If neither structure can be derived from the exact source frame, the normalized empty-vector first-exit continuation should be closed and research should return to separately retained nonempty rough-block, boundary, or pre-positive cross-component channels.

## Why it may matter

The surviving question is no longer whether more averaging variables can be exposed. The exact reductions show that the obvious candidates repeatedly collapse: inverse shifts are gauge, first-exit supports are a deterministic partition, coefficient-blind phase families remain at the conductor scale, scalar weights do not access a hidden small singular direction, and repeated-residue multiplicity produces no new conductor phase even without completion.

`MC-495` makes the remaining incomplete escape auditable. A fixed-fraction energy reduction requires an order-one negative weighted correlation of the **actual** source overlap with one explicit relative character phase. This is much sharper than saying that endpoints or incomplete sums might help: the source geometry must now explain where the phase-selective conductor bias comes from and how it survives all normalization and reconstruction tariffs.

## Decisive test

Work first in the `R=T=1` empty-vector source frame and keep the exact first-exit cell

\[
E_q=\{n:q\mid n(n+h),\ (n(n+h),P(q))=1\}
\]

with exact shortened endpoints and source coefficients. Reject proposals whose only q-dependence is already priced by `MC-485`--`MC-495`: coefficient-blind complete/incomplete phase averaging, affine inverse shifts, common transforms of disjoint first-exit cells, rowwise dilation followed by positive `L^2` closure, scalar reweighting, dense same-root repeated-residue blocks, or completed/incomplete cross-root multiplicity by itself.

For an incomplete repeated-residue proposal, compute the exact projected overlap weight

\[
w(t)=\sum_{m\equiv t\ (p)}A(m)B(m)
\]

and the centered correlation

\[
\sum_{t\in\mathbf F_p}(w(t)-\bar w)\chi(1-t^{-2}).
\]

Do not replace `w` by a smooth, uniform, random, or interval model unless the replacement error is quantitatively transferred. Accept this route only if the resulting bound gives a fixed conductor-power gain after diagonal energy, endpoint costs, q-summation, shell reconstruction and all source weights are restored.

For a pre-aggregation proposal, identify the first exact formula where two first-exit labels occupy genuinely different arithmetic roles inside the transformed kernel or coefficient: for example a q-dependent modulus, reciprocal phase, or `m`-dependent sign/complex coefficient not removable by affine relabeling. A harmless scalar row factor or increased multiplicity does not pass.

## Evidence boundary

`MC-484` proves exact selector-free Buchstab first exit and preserves the dimension-two pair sieve. `MC-485`--`MC-491` close coefficient-blind phase-frame, affine-shift, partition, dilation and small/repeated-residue conditioning loopholes. `MC-492` rules out native same-root repeated-residue cancellation. `MC-494` removes arbitrary completed cross-root multiplicity as a resource. `MC-495` removes incomplete repeated-residue multiplicity as an independent phase resource and identifies the exact surviving object as a weighted rational-character bias.

None of these findings estimates the centered source weight in `MC-495`, derives a new q-dependent signed/complex pre-aggregation coefficient, proves a factor-specific dispersion theorem for the exact dimension-two source frame, or improves `M(x)`. `MC-456` remains a neighboring positive template only; it is not evidence that the required quotient-breaking structure exists here.

## Research disposition

The clue remains `accepted`, with a stricter frontier. The primary live test is now **source-derived phase-selective conductor bias or genuinely q-specific pre-aggregation arithmetic asymmetry**. Bare repeated-residue density, pair counting, or incompleteness without control of the exact projected weight should not be revisited as distinct mechanisms.