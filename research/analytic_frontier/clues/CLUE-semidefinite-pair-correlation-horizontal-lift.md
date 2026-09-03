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

`ANF-017` now identifies the next missing layer and eliminates that particular survivor. For any finite set of distinct real points `X`, let

\[
e_J(X)=\frac1{|X|}\sum_{x,y\in X}\widehat J(x-y),
\qquad
q_{\rm real}(J)=\inf_X e_J(X).
\]

Testing both `X` and the same support with multiplicity two and reoptimizing the spectral amplitude gives the exact finite-configuration cap `2-C(J)/e_J(X)`. Hence a scalar shape can beat Montgomery--Taylor only if

\[
\frac{C(J)}{q_{\rm real}(J)}<C_{\rm MT}.
\]

For the cubic `J_*`, a 15-site real configuration whose central 13 sites have spacing `41/40` and whose two edge gaps are `21/20` has

\[
e_{J_*}(X)=0.998079905262228\ldots,
\qquad
\frac{53/40}{e_{J_*}(X)}=1.327549019887219\ldots>C_{\rm MT}.
\]

Therefore **all positive amplitude scalings of the cubic survivor are killed by a finite real configuration**, before any complex or vertically displaced test is needed. The obstruction is specifically finite-volume and boundary-sensitive: only the two edge gaps must detune from the periodic bulk.

The configuration-level branch remains distinct. `ANF-006` records a fully checked local ordered-gap certificate beating the Montgomery--Taylor baseline, while `ANF-007`--`ANF-009` show that simply increasing block size or point order inside the same pressure architecture does not supply a durable asymptotic strategy. Its next escape must alter the information carrier or bridge itself.

## Research question

Two distinct questions remain.

First, in the **universal affine support-one scalar** class, is the finite-real ratio itself already a Montgomery--Taylor no-go theorem? For every continuous even `J>=0` supported in `[-1,1]`, must

\[
\boxed{
\frac{C(J)}{q_{\rm real}(J)}\ge C_{\rm MT}?
}
\]

If not, construct an explicit positive spectrum with strict reverse inequality and identify a finite-dimensional certificate that controls or computes its real-configuration floor. Only a profile surviving this stronger real test should proceed to vertically displaced conjugation-invariant complex multisets.

Second, in the **configuration-level** class, what genuinely new local memory, nonlinear defect, matrix/inertia statistic, window accounting or analytic bridge can retain a fixed gain after the `ANF-007`--`ANF-009` filters? Simply enlarging scalar blocks or point count inside the existing `F/Phi_n` pressure family remains ruled out as a durable asymptotic strategy.

## Why it may matter

The scalar branch has now separated three increasingly strong information layers. Spectral positivity and thermodynamic periodization permit the cubic `J_*`; amplitude-aware finite real configurations do not. `ANF-017` therefore shows exactly what the infinite-lattice limit discarded: a boundary degree of freedom can lower finite energy enough to erase the apparent gain.

A universal inequality `C(J)/q_real(J)>=C_MT` would close the remaining universal-affine scalar route without needing complex configurations at all. A strict survivor would be much more meaningful than `ANF-016`: it would have passed every finite real support and would isolate conjugation/vertical geometry as genuinely load-bearing.

The configuration-level branch is the known escape from scalar compression. Its value lies in identifying pre-compression information that survives current local-pressure obstructions and can still be evaluated unconditionally for zeta zeros.

## Decisive test

For the scalar branch, treat

\[
R_{\rm real}(J)=\frac{C(J)}{q_{\rm real}(J)}
\]

as the new shape functional. First seek an analytic lower bound `R_real(J)>=C_MT` over continuous even `J>=0` supported in `[-1,1]`, using positive-definite finite-energy structure rather than only lattice periodization. Any candidate counterexample must come with an explicit lower control on `q_real(J)`; checking a few lattices or a fixed normalization is not enough because amplitude reoptimization restores the junction at `t e=1`.

If a profile rigorously satisfies `R_real(J)<C_MT`, test arbitrary finite real configurations more aggressively and then conjugation-invariant complex multisets. A profile that survives those stages would still require a proof of the complete universal affine counting inequality before it could support any new zeta-zero proportion.

For any proposed out-of-band scalar construction, apply `ANF-011` before optimization. For any compact-band spectrally signed construction, apply `ANF-012`. Those branches remain closed unless the information carrier changes or the inequality becomes zeta-specific rather than universal.

For the configuration-level branch, first apply the exact block cap from `ANF-008` and the point-order envelope from `ANF-009`. A survivor must alter the local functional or bridge and then provide an evidence-matched finite inequality plus a complete passage to zeta zeros at the claimed trust tier.

## Evidence boundary

`ANF-017` is a decisive negative result for the **specific cubic shape** `J_*` and all of its positive amplitude scalings. It does not prove `C(J)/q_real(J)>=C_MT` for every positive support-one spectrum, so the universal affine scalar class remains open at the shape level.

`ANF-011` and `ANF-012` still close useful negative out-of-band tails and compact-band spectral sign changes inside the universal affine scalar template. Zeta-specific, non-affine, higher-order, matrix/inertia-before-compression and ordered-configuration mechanisms remain outside those theorems.

`ANF-006` establishes one verified configuration-level gain, while `ANF-007`--`ANF-009` constrain only the registered pressure family. They are not ceilings for richer Bellman/coboundary, altered-window, multi-profile, matrix or otherwise modified pre-compression methods.

## Research disposition

Accepted and narrowed. The thermodynamic stage remains resolved by the `ANF-016` counterexample, but `ANF-017` shows that its cubic witness is a finite-volume false survivor: a two-scale 15-site real support forces `C/e>C_MT` after the required amplitude reoptimization. The live scalar question is now the universal finite-real ratio `C(J)/q_real(J)`; only a shape strictly below Montgomery--Taylor there should be promoted to complex-configuration testing. The configuration-level branch remains open only through a genuine carrier or bridge change.
