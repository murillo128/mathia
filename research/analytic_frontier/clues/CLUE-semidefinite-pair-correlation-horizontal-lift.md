---
id: CLUE-analytic-frontier-semidefinite-pair-correlation-horizontal-lift
type: research-clue
status: accepted
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-002-pair-correlation-hilbert-horizontal-information.md
  - research/analytic_frontier/findings/ANF-003-common-translation-vector-features-scalarize.md
  - research/analytic_frontier/findings/ANF-004-convex-finite-pair-moment-lifts-dualize.md
  - research/analytic_frontier/findings/ANF-005-signed-affine-pair-certificates-pay-normalization-slack.md
  - research/analytic_frontier/findings/ANF-006-local-ordered-gap-certificates-escape-global-pair-moment-ceiling.md
  - research/analytic_frontier/findings/ANF-007-two-point-local-gap-bridge-cannot-beat-montgomery-taylor.md
  - research/analytic_frontier/findings/ANF-008-improving-n-point-bridge-saturates-block-cap.md
  - research/analytic_frontier/findings/ANF-009-increasing-point-order-pressure-bridge-collapses-to-montgomery-taylor.md
  - research/analytic_frontier/findings/ANF-010-out-of-band-form-factor-positivity-has-scalar-gram-sign-obstruction.md
  - research/analytic_frontier/findings/ANF-011-negative-out-of-band-tails-violate-conjugate-pair-barrier.md
  - research/analytic_frontier/findings/ANF-012-conjugate-comb-tests-force-positive-band-spectrum.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# What survives beyond the scalar affine pair-correlation ceiling?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality extracts unconditional horizontal information from the BGSST complex-zero pair-correlation formula. `ANF-003` and `ANF-004` then show that common-translation vector features and finite convex lifts add no information if they are compressed to scalar global pair moments before the counting step. `ANF-005` isolates the remaining affine support-one problem: with normalization slack `delta`, any improvement over Montgomery--Taylor must satisfy

\[
M(F)+\delta<m_{\rm MT},
\qquad
m_{\rm MT}=0.3274992963\ldots .
\]

The scalar freedom is now much narrower than it first appeared. `ANF-010` identifies BGSST's unconditional all-frequency positivity as enough to discard a Cohn--Elkies negative outer tail on the analytic side, but shows that a scalar PSD Gram kernel cannot carry that tail. `ANF-011` removes the PSD assumption for the out-of-band route: a nontrivial negative Fourier--Laplace tail drives the scalar kernel to `-infinity` on the imaginary axis and violates the universal conjugate-pair floor. `ANF-012` closes the analogous compact-band loophole. For every continuous real-even compact-band profile `J`, universality over conjugation-invariant complex multisets forces `J>=0` by high-multiplicity conjugate binomial-comb tests. Thus a universal affine support-one scalar certificate is automatically positive-definite on the real line. Its remaining sign freedom is only **spatial** sign change of `F=widehat J`, paid for by `delta`; the spectral density itself cannot be signed.

The configuration-level branch behaves differently. `ANF-006` records a fully checked local ordered-gap certificate beating the Montgomery--Taylor baseline, proving that information preserved before global scalar compression can matter. `ANF-007` shows that two points are insufficient inside that bridge; `ANF-008` shows block size is forced once the finite certificate is fixed; and `ANF-009` shows that merely increasing point order in the unchanged pressure family has an envelope returning to the baseline. The demonstrated escape is therefore real, but the present local bridge also has a structural ceiling unless its information carrier changes.

## Research question

Two distinct questions remain.

First, in the **universal affine support-one scalar** class, let `J>=0` be continuous, real-even and supported in `[-1,1]`, put `F=widehat J`, and let `delta` be the smallest normalization slack compatible with the simple-real counting inequality. Can such a positive-definite but spatially signed kernel satisfy

\[
M(F)+\delta<m_{\rm MT},
\]

or do the remaining universal complex-configuration constraints already force `M(F)+delta>=m_MT`? `ANF-012` means that searches over spectrally signed support-one profiles are no longer relevant to this question.

Second, in the **configuration-level** class, what genuinely new local memory, nonlinear defect, matrix/inertia statistic, window accounting, or analytic bridge can retain a fixed gain after the `ANF-007`--`ANF-009` filters? Simply enlarging scalar block size or point count inside the existing `F/Phi_n` pressure architecture is already ruled out as a durable asymptotic strategy.

## Why it may matter

A strict sub-Montgomery--Taylor example in the narrowed positive-spectral affine class would show that scalar global pair correlation still contains unused unconditional horizontal information, but the gain would have to come from spatial sign and the full complex-configuration inequality rather than from a signed spectrum. Conversely, proving the Montgomery--Taylor floor under these now-forced spectral-positivity constraints would nearly exhaust the universal affine scalar support-one route.

The configuration-level branch is the known escape from that compression ceiling. Its next value lies in identifying exactly what extra pre-compression information survives the current local-pressure obstructions and can still be evaluated unconditionally for zeta zeros.

## Decisive test

For the scalar branch, optimize over nonnegative support-one spectral profiles `J` rather than arbitrary signed profiles. For each candidate `F=widehat J`, determine the minimal `delta` forced by finite conjugation-invariant configurations and test the objective `M(F)+delta`. A rigorous lower bound

\[
M(F)+\delta\ge m_{\rm MT}
\]

throughout this class rejects the remaining universal affine support-one route. A strict counterexample is only a necessary-stage survivor; it must still satisfy the complete universal counting inequality.

For any proposed out-of-band scalar affine construction, apply `ANF-011` before optimization. For any compact-band spectrally signed construction, apply `ANF-012`: the conjugate-comb tests already make it impossible under universal affine counting. A proposal survives these filters only by changing the information carrier or by proving a zeta-specific inequality that does not quantify over arbitrary conjugation-invariant multisets.

For the configuration-level branch, first apply the exact block cap from `ANF-008` and the point-order envelope from `ANF-009`. A surviving proposal must alter the local functional or bridge itself and then provide an evidence-matched finite inequality plus a complete passage to zeta zeros at the claimed trust tier.

## Evidence boundary

No universal affine support-one improvement and no complete Montgomery--Taylor no-go theorem for the remaining positive-spectral/spatially-signed class is established. `ANF-012` proves spectral positivity under its continuity and compact-support hypotheses; it does not imply `F(x)>=0` and therefore does not by itself trigger the Carneiro--Chandee--Littmann--Milinovich nonnegative-spatial-kernel extremal theorem.

`ANF-011` closes the useful negative out-of-band Fourier--Laplace tail only for the universal affine scalar template. Zeta-specific, non-affine, higher-order, matrix/inertia-before-compression and local ordered-configuration mechanisms remain outside that theorem.

`ANF-006` establishes one verified local configuration-level gain, while `ANF-007`--`ANF-009` constrain only the registered pressure family. They are not ceilings for richer Bellman/coboundary, altered-window, multi-profile, matrix or otherwise modified pre-compression methods.

## Research disposition

Accepted and narrowed. The scalar branch is now a **positive-spectral but potentially spatially signed** support-one extremal problem; spectrally signed compact-band profiles and useful negative out-of-band scalar tails are closed by `ANF-012` and `ANF-011`. The configuration-level branch remains open only through a genuine carrier or bridge change, not larger scalar blocks or point-count escalation in the existing pressure family.