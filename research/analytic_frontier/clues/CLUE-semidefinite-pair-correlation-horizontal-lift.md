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
  - research/analytic_frontier/findings/ANF-013-duplicated-lattice-tests-periodization-barrier.md
  - research/analytic_frontier/findings/ANF-014-mellin-periodization-defect-budget.md
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

`ANF-013` adds a thermodynamic real-configuration filter to that residual branch. Long simple and duplicated arithmetic lattices force

\[
A\le \min(1+P_J(h),2P_J(h)),
\qquad
P_J(h)=\frac1h\sum_{k\in\mathbb Z}J(k/h),
\]

at every spacing. If `p(J)=inf_h P_J(h)` and `C(J)` is the BGSST pair cost, optimizing the amplitude of a fixed shape is capped by `max(0,2-C(J)/p(J))`. Therefore any scalar improvement over Montgomery--Taylor must first satisfy the scale-free survival condition `C(J)/p(J)<C_MT`.

`ANF-014` shows that this ratio is itself rigid. The Mellin transform of the all-scale periodization gives

\[
\frac{C(J)}p
=1+\frac{3}{\pi^2}
+\left(1-\frac{3}{\pi^2}\right)\left(\frac{J(0)}p-1\right)
+\frac{6}{\pi^2}\int_1^\infty
\left(\frac{P_J(h)}p-1\right)\frac{dh}{h^2}.
\]

Thus the lattice constraints alone force `C/p>=1+3/pi^2=1.3039635509...`, leaving only `Delta_MT=0.0235357454...` of total nonnegative defect below Montgomery--Taylor. Any survivor must have `J(0)/p<1.0338139554` and weighted periodization excess below `0.0387147494`. Equality in the new floor forces `J(0)=p` and `P_J(h)=p` at every `h>=1`, so the Möbius profile of `ANF-013` is the exact formal equality boundary rather than an arbitrary saturation ansatz.

The configuration-level branch behaves differently. `ANF-006` records a fully checked local ordered-gap certificate beating the Montgomery--Taylor baseline, proving that information preserved before global scalar compression can matter. `ANF-007` shows that two points are insufficient inside that bridge; `ANF-008` shows block size is forced once the finite certificate is fixed; and `ANF-009` shows that merely increasing point order in the unchanged pressure family has an envelope returning to the baseline. The demonstrated escape is therefore real, but the present local bridge also has a structural ceiling unless its information carrier changes.

## Research question

Two distinct questions remain.

First, in the **universal affine support-one scalar** class, let `J>=0` be continuous, real-even and supported in `[-1,1]`, put `F=widehat J`, and let `p=p(J)>0`. Do the remaining universal complex-configuration constraints, or even consistency of one nonnegative profile with its complete periodization family, force the defect

\[
\left(1-\frac{3}{\pi^2}\right)\left(\frac{J(0)}p-1\right)
+\frac{6}{\pi^2}\int_1^\infty
\left(\frac{P_J(h)}p-1\right)\frac{dh}{h^2}
\]

to be at least `Delta_MT`? Equivalently, can any admissible profile remain close enough to all-scale lattice saturation to achieve `C(J)/p(J)<C_MT`? `ANF-014` makes this a quantitative stability question rather than a free functional optimization.

Second, in the **configuration-level** class, what genuinely new local memory, nonlinear defect, matrix/inertia statistic, window accounting, or analytic bridge can retain a fixed gain after the `ANF-007`--`ANF-009` filters? Simply enlarging scalar block size or point count inside the existing `F/Phi_n` pressure architecture is already ruled out as a durable asymptotic strategy.

## Why it may matter

For the scalar branch, the remaining numerical room is now small and structurally localized. A proof that the nonnegative periodization defects must total at least `Delta_MT` would close the thermodynamic-lattice survival stage and strongly constrain any universal affine support-one improvement before the full complex inequality is attempted. Conversely, an explicit profile with total defect below `Delta_MT` would be a genuine stage-one survivor and would identify the near-saturation geometry that spatial sign changes must exploit.

The configuration-level branch is the known escape from scalar compression. Its next value lies in identifying exactly what extra pre-compression information survives the current local-pressure obstructions and can still be evaluated unconditionally for zeta zeros.

## Decisive test

For the scalar branch, apply the `ANF-014` defect identity before any expensive universal-configuration search. After normalizing `p(J)=1`, reject a profile unless

\[
\left(1-\frac{3}{\pi^2}\right)(J(0)-1)
+\frac{6}{\pi^2}\int_1^\infty(P_J(h)-1)\frac{dh}{h^2}
<\Delta_{\rm MT}.
\]

A rigorous lower bound by `Delta_MT` throughout the admissible residual class closes the `C/p<C_MT` lattice route. A strict counterexample is only a necessary-stage survivor; it must then satisfy the complete universal counting inequality, including non-lattice real configurations and vertically displaced conjugate configurations. The Möbius profile is the equality boundary for the weaker floor `1+3/pi^2`, not an asserted admissible extremizer.

For any proposed out-of-band scalar affine construction, apply `ANF-011` before optimization. For any compact-band spectrally signed construction, apply `ANF-012`: the conjugate-comb tests already make it impossible under universal affine counting. A proposal survives these filters only by changing the information carrier or by proving a zeta-specific inequality that does not quantify over arbitrary conjugation-invariant multisets.

For the configuration-level branch, first apply the exact block cap from `ANF-008` and the point-order envelope from `ANF-009`. A surviving proposal must alter the local functional or bridge itself and then provide an evidence-matched finite inequality plus a complete passage to zeta zeros at the claimed trust tier.

## Evidence boundary

No universal affine support-one improvement and no complete Montgomery--Taylor no-go theorem for the remaining positive-spectral/spatially-signed class is established. `ANF-012` proves spectral positivity under its continuity and compact-support hypotheses; it does not imply `F(x)>=0`. `ANF-013` supplies the exact long-lattice necessary ratio, while `ANF-014` rewrites that ratio as a nonnegative Mellin defect and quantifies the remaining margin. Neither finding proves that the defect is at least `Delta_MT`, that the lower floor `1+3/pi^2` is attainable, or that a profile below `C_MT` satisfies the universal affine inequality.

`ANF-011` closes the useful negative out-of-band Fourier--Laplace tail only for the universal affine scalar template. Zeta-specific, non-affine, higher-order, matrix/inertia-before-compression and local ordered-configuration mechanisms remain outside that theorem.

`ANF-006` establishes one verified local configuration-level gain, while `ANF-007`--`ANF-009` constrain only the registered pressure family. They are not ceilings for richer Bellman/coboundary, altered-window, multi-profile, matrix or otherwise modified pre-compression methods.

## Research disposition

Accepted and narrowed. The scalar branch is now a **near-saturation periodization stability problem**: a candidate must fit inside the exact `Delta_MT=0.0235357454...` Mellin defect budget before it is worth testing against the full universal complex-configuration inequality. Spectrally signed compact-band profiles and useful negative out-of-band scalar tails remain closed by `ANF-012` and `ANF-011`. The configuration-level branch remains open only through a genuine carrier or bridge change, not larger scalar blocks or point-count escalation in the existing pressure family.
