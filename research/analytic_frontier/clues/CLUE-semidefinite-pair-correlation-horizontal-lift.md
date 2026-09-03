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
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# What survives beyond the scalar affine pair-correlation ceiling?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality extracts unconditional horizontal information from the BGSST complex-zero pair-correlation formula. `ANF-003` and `ANF-004` show that common-translation vector features and finite convex lifts add no information if they are compressed to scalar global pair moments before the counting step. `ANF-005` isolates the residual universal affine support-one question.

The sign freedoms in that scalar branch are now tightly constrained. `ANF-010` shows that BGSST's all-frequency positivity is analytically sufficient to discard a Cohn--Elkies negative outer tail, but a scalar PSD Gram kernel cannot carry such a tail. `ANF-011` removes the PSD assumption for the out-of-band route: a nontrivial negative Fourier--Laplace tail violates the universal conjugate-pair floor. `ANF-012` closes the analogous compact-band spectral-sign loophole: universality over conjugation-invariant multisets forces every continuous compact-band spectral profile `J` to satisfy `J>=0`. The only scalar sign freedom left is therefore **spatial** sign change of `F=widehat J`.

`ANF-013`--`ANF-015` tested that freedom on long real lattices. With

\[
P_J(h)=\frac1h\sum_{k\in\mathbb Z}J(k/h),\qquad
p(J)=\inf_hP_J(h),
\]

the long simple/duplicated lattice family gives the survival ratio `C(J)/p(J)<C_MT`. `ANF-016` proved that this thermodynamic condition is genuinely weaker than Montgomery--Taylor: the explicit cubic spectrum

\[
J_*(x)=1-\frac38|x|-\frac74|x|^2+\frac98|x|^3
\qquad(|x|\le1)
\]

has `J_*>=0`, `p(J_*)=1` and `C(J_*)=53/40<C_MT`, while its spatial kernel changes sign. Thus no optimization of the thermodynamic packing dual alone can close the scalar branch.

`ANF-017` identifies the finite-volume layer and eliminates that particular survivor. For any finite set of distinct real points `X`, let

\[
e_J(X)=\frac1{|X|}\sum_{x,y\in X}\widehat J(x-y),
\qquad
q_{\rm real}(J)=\inf_X e_J(X).
\]

Testing both `X` and the same support with multiplicity two and reoptimizing the spectral amplitude gives the exact finite-configuration cap `2-C(J)/e_J(X)`. Hence a scalar shape can beat Montgomery--Taylor only if `C(J)/q_real(J)<C_MT`. The 15-site edge-detuned witness of `ANF-017` forces the cubic back below Montgomery--Taylor.

`ANF-018` now identifies `q_real` with a mature classical variational object. If

\[
B_{\rm stab}(F)
=\sup_X\left(-\frac1{|X|}\sum_{x<y}F(x-y)\right),
\]

then exactly

\[
q_{\rm real}(J)=F(0)-2B_{\rm stab}(F).
\]

Thus the remaining scalar no-go is equivalent to the sharp stability/binding inequality

\[
B_{\rm stab}(F)
\ge\frac12\left(F(0)-\frac{C(J)}{C_{\rm MT}}\right).
\]

Sütő's compact-Fourier ground-state theorem shows that this is precisely a classical positive-type pair-potential class and identifies the unit chain as the one-dimensional critical-density bulk ground state under its regularity hypotheses. The key distinction is finite volume: the optimal stability constant can gain binding below that bulk value, exactly as the boundary-detuned cubic witness does.

Writing `j_0=J(0)`, `I(J)=int |alpha|J(alpha)dalpha`, `m_MT=C_MT-1`, and `b_fin=j_0-q_real`, the same target is

\[
C_{\rm MT}b_{\rm fin}+I(J)\ge m_{\rm MT}j_0.
\]

Therefore any spectrum with `I(J)>=m_MT j_0` is already killed by the unit-chain limit. Only the thin regime `I(J)<m_MT j_0` needs finite binding. For the cubic, the exact required gain is `0.001882710090706...`; `ANF-017` proves at least `0.001920094737772...`, exceeding the threshold by only `3.74e-5`. This explains quantitatively why its thermodynamic escape was so fragile.

`ANF-018` also checks a tempting shortcut. The translation autocorrelation of an exact finite minimizer is spatially nonnegative and has spectrum `J|S_X|^2/|X|`, but its zero-frequency spectral value is multiplied by `|X|`. A black-box return to the Carneiro--Chandee--Littmann--Milinovich nonnegative-spatial theorem therefore loses a factor `|X|`; autocorrelation positivity alone does not preserve the original BGSST budget.

The configuration-level branch remains distinct. `ANF-006` records a fully checked local ordered-gap certificate beating the Montgomery--Taylor baseline, while `ANF-007`--`ANF-009` show that simply increasing block size or point order inside the same pressure architecture does not supply a durable asymptotic strategy. Its next escape must alter the information carrier or bridge itself.

## Research question

Two distinct questions remain.

First, in the **universal affine support-one scalar** class, prove or refute the sharp one-dimensional stability inequality

\[
\boxed{
B_{\rm stab}(\widehat J)
\ge\frac12\left(
\widehat J(0)-\frac{J(0)+\int|\alpha|J(\alpha)d\alpha}{C_{\rm MT}}
\right)
}
\]

for every continuous even `J>=0` supported in `[-1,1]`, with the right side vacuous when nonpositive. This is exactly equivalent to `C(J)/q_real(J)>=C_MT`. If false, construct an explicit positive spectrum and give a rigorous **upper bound** on its optimal stability constant below the displayed threshold; surviving a collection of sampled finite configurations is not enough.

Second, in the **configuration-level** class, what genuinely new local memory, nonlinear defect, matrix/inertia statistic, window accounting or analytic bridge can retain a fixed gain after the `ANF-007`--`ANF-009` filters? Simply enlarging scalar blocks or point count inside the existing `F/Phi_n` pressure family remains ruled out as a durable asymptotic strategy.

## Why it may matter

The scalar branch now has a precise bridge to classical many-particle mathematics. `q_real` is the diagonal-restored best stability constant, not merely a numerical finite-set floor. This opens a mature body of tools around one-dimensional ground states, stability constants, finite-cluster binding and structure factors while preserving the exact zeta-side quantity that must be controlled.

The bridge also separates useful and insufficient information. Thermodynamic ground-state results control the bulk and explain the unit-chain constraint, but `ANF-017` proves that boundary-sensitive finite binding can be decisive at the `10^-5` margin relevant here. Conversely, a claimed scalar survivor must control the global optimal stability constant from above; finite searches can falsify such a survivor but cannot establish it.

The configuration-level branch is the known escape from scalar compression. Its value lies in identifying pre-compression information that survives current local-pressure obstructions and can still be evaluated unconditionally for zeta zeros.

## Decisive test

For the scalar branch, search the one-dimensional stability/ground-state literature and derive bounds directly for `B_stab(widehat J)`. The first automatic filter is `I(J)>=m_MT J(0)`, which is already fatal by the unit-chain limit. In the residual regime, compare any rigorous lower-energy construction against the exact required binding

\[
b_{\rm fin}\ge\frac{m_{\rm MT}J(0)-I(J)}{C_{\rm MT}}.
\]

A candidate counterexample must go the opposite direction and prove that **every** finite real configuration has energy above `C(J)/C_MT`, equivalently that `B_stab` stays strictly below its threshold. Only such a shape should proceed to vertically displaced conjugation-invariant complex multisets.

Do not substitute thermodynamic or periodic ground-state energy for `q_real`: `ANF-017` already demonstrates a finite boundary correction that changes the verdict. Likewise, an autocorrelation transform may be useful only if it controls its `|X|`-fold spectral normalization loss rather than applying the nonnegative-spatial extremal theorem as a black box.

For any proposed out-of-band scalar construction, apply `ANF-011` before optimization. For any compact-band spectrally signed construction, apply `ANF-012`. Those branches remain closed unless the information carrier changes or the inequality becomes zeta-specific rather than universal.

For the configuration-level branch, first apply the exact block cap from `ANF-008` and the point-order envelope from `ANF-009`. A survivor must alter the local functional or bridge and then provide an evidence-matched finite inequality plus a complete passage to zeta zeros at the claimed trust tier.

## Evidence boundary

`ANF-018` is a structural reduction and prior-art redirect, not a proof of the sharp stability inequality. Sütő's infinite-volume theorem has extra integrability hypotheses and does not identify the finite-volume optimal stability constant required here. The stealthy-hyperuniform literature is relevant to the interaction class and structure-factor machinery, but it likewise does not erase the finite boundary problem.

The autocorrelation observation in `ANF-018` is exact for an attained finite minimizer; minimizing sequences give only asymptotic nonnegativity from below. Its purpose is to falsify a naive black-box return to the nonnegative-spatial Montgomery--Taylor theorem, not to rule out a more structured use of autocorrelations.

`ANF-011` and `ANF-012` still close useful negative out-of-band tails and compact-band spectral sign changes inside the universal affine scalar template. Zeta-specific, non-affine, higher-order, matrix/inertia-before-compression and ordered-configuration mechanisms remain outside those theorems.

`ANF-006` establishes one verified configuration-level gain, while `ANF-007`--`ANF-009` constrain only the registered pressure family. They are not ceilings for richer Bellman/coboundary, altered-window, multi-profile, matrix or otherwise modified pre-compression methods.

## Research disposition

Accepted and narrowed. The live scalar problem is now a sharp best-stability-constant inequality for one-dimensional positive-type compact-spectrum pair potentials. `ANF-018` supplies the exact conversion and shows that the `ANF-017` cubic witness succeeds by barely providing the missing finite-cluster binding beyond the unit-chain bulk energy. Future scalar candidates must be judged against the global stability constant, not only thermodynamic lattices or sampled finite supports. The configuration-level branch remains open only through a genuine carrier or bridge change.