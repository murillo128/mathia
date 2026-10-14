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
  - research/analytic_frontier/findings/ANF-015-mobius-oscillation-strictly-improves-mellin-lattice-floor.md
  - research/analytic_frontier/findings/ANF-016-cubic-positive-spectrum-beats-thermodynamic-lattice-ratio.md
  - research/analytic_frontier/findings/ANF-017-edge-detuned-finite-configuration-kills-cubic-survivor.md
  - research/analytic_frontier/findings/ANF-018-finite-real-floor-is-a-classical-stability-constant.md
  - research/analytic_frontier/findings/ANF-034-central-notch-perturbation-gives-an-explicit-finite-real-separator-ray.md
  - research/analytic_frontier/findings/ANF-081-two-level-clipping-closes-the-full-real-multiplicity-gate.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# What survives beyond the scalar affine pair-correlation ceiling?

## Observation

The source-side motivation is unchanged. ANF-002 extracts unconditional horizontal information from complex-zero pair correlation; ANF-003--ANF-004 show that common-translation vector features and finite convex pair-moment lifts add no information when compressed to scalar global pair moments. ANF-006 obtains a verified ordered-gap improvement, but ANF-007--ANF-009 bound the registered higher-point pressure family. Out-of-band negative scalar tails and spectrally negative compact-band tests also face the exact obstructions of ANF-011--ANF-012.

The former scalar stability question **has been decided negatively**. ANF-018 identifies, for an even continuous nonnegative spectrum \(J\) supported in \([-1,1]\), with \(F=\widehat J\),
\[
q_{\rm real}(J):=\inf_{\varnothing\ne X\subset\mathbb R\ {\rm finite}}
 \frac1{|X|}\sum_{x,y\in X}F(x-y)
 =F(0)-2B_{\rm stab}(F).
\]
The proposed universal Montgomery--Taylor no-go inequality was
\[
B_{\rm stab}(F)\ge
\frac12\left(F(0)-\frac{C(J)}{C_{\rm MT}}\right).
\tag{1}
\]
ANF-034 constructs a central-notch \(J_s=J_{\rm MT}-s\phi_\eta\ge0\), continuous, even, supported in \([-1,1]\), and proves the **uniform, all-finite-real-sets** strict inequality
\[
q_{\rm real}(J_s)>\frac{C(J_s)}{C_{\rm MT}}.
\tag{2}
\]
Consequently,
\[
\boxed{
B_{\rm stab}(\widehat J_s)
=\frac{\widehat J_s(0)-q_{\rm real}(J_s)}2
<
\frac12\left(\widehat J_s(0)-\frac{C(J_s)}{C_{\rm MT}}\right).
}
\tag{3}
\]
This supplies precisely the **global upper bound** on the optimal stability constant that the earlier scalar question demanded; finite searches alone would not have supplied it. ANF-081 subsequently proves a central-notch affine certificate for **every finite real multiset**, with arbitrary support and multiplicities (its admissible notch parameters need not equal those of ANF-034). ANF-017's failed cubic witness was only a failed *particular* shape, not a universal no-go theorem.

The remaining boundary is genuinely different: a finite-real scalar separator is not a universal certificate on **conjugation-invariant complex** configurations, and a strict improvement in the counting theorem for zeta zeros cannot be inferred from (2)--(3). The separate physical near-extremizer question is owned by the accepted local notch-exposure clue and ANF-099. This clue retains the other, configuration-level question: what information must survive **before** global scalar pair compression to improve the zero-counting bridge?

## Research question

Can an ordered local statistic, nonlinear defect, conditional/matrix observable, or a new window-accounting bridge retain a certified gain after the ANF-007--ANF-009 point-order and block-cap filters, **without** collapsing to the same global scalar pair-moment envelope?

A viable candidate must specify its configuration observable and counting bridge, distinguish the information it preserves from existing global pair moments, and explain how the needed source-side mean or inequality could be evaluated unconditionally for zeta zeros. Increasing point order within the unchanged \(F/\Phi_n\) pressure family is already screened and is not a new mechanism.

## Why it may matter

ANF-034 and ANF-081 show that a positive support-one spectrum can strictly beat the Montgomery--Taylor normalization on the entire real configuration class. They remove the claimed universal finite-real stability barrier but do **not** remove the complex counting requirement. Meanwhile ANF-006 demonstrates that local ordered information can produce a certified finite improvement that scalar compression obscures. The unresolved value of this clue lies in identifying a genuinely richer information carrier with a complete, support- and normalization-correct passage to zeta-zero counts, rather than optimizing another real scalar potential.

## Decisive test

For any proposed pre-compression carrier, define the functional on actual admissible zero configurations, including multiplicities and nonreal conjugate pairs. Exhibit the exact information lost under the global pair-moment scalarization (for example, a proved separation on matched admissible configurations), then derive a finite inequality whose gain survives the precise ANF-008 block cap and ANF-009 point-order envelope or **explicitly changes** their hypotheses. Carry the inequality through the pair-correlation/mean-value input with the actual Fourier support, coefficient/sign class, horizontal-information bookkeeping and affine normalization. A formula requiring unproved RH, higher-correlation, or source moment hypotheses must be labelled conditional, not counted as an unconditional gain.

A candidate is rejected if the supposed extra invariant scalarizes before counting, its local gain vanishes at the certified block cap, or the claimed unconditional zeta passage loses the gain. Conversely, a complete new bridge with a certified strict zero-counting consequence resolves this configuration-level clue. Reproving (2) or testing another finite real sample does not address it.

## Evidence boundary

The scalar assertion (1) is **false**, by the explicit ANF-034 construction and the exact ANF-018 identity; ANF-081 makes the real multiplicity scope uniform. This is a Mathia-local logical consequence of persisted derivations, not a claim to a new classical statistical-mechanics theorem. Sütő's thermodynamic compact-Fourier ground-state results do not replace the finite optimal stability constant, and the old ANF-017 cubic computation does not contradict the later central-notch witness.

The original out-of-band and compact-band spectral-sign obstructions ANF-011--ANF-012 still apply to their stated scalar templates. ANF-006--ANF-009 constrain only their registered ordered-pressure family, not arbitrary future nonlinear, matrix, conditional, or zeta-specific counting methods. No complete new pre-compression carrier is proved here, no universal complex central-notch certificate follows, and RH remains open.

## Research disposition

**Accepted only for the configuration-level information-carrier question.** The formerly open universal scalar stability conjecture is **refuted** by ANF-034, via (2)--(3), with the stronger all-real-multiset affine survival in ANF-081. The residual decisive test is a new pre-compression counting bridge; another finite-real scalar stability test cannot settle it.
