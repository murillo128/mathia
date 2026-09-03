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
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# What survives beyond the scalar affine pair-correlation ceiling?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality extracts unconditional horizontal information from the BGSST complex-zero pair-correlation formula. `ANF-003` and `ANF-004` show that common-translation vector features and finite convex lifts add no information if they are compressed to scalar global pair moments before the counting step. `ANF-005` isolates the residual universal affine support-one question.

The sign freedoms in that scalar branch are now tightly constrained. `ANF-010` shows that BGSST's all-frequency positivity is analytically sufficient to discard a Cohn--Elkies negative outer tail, but a scalar PSD Gram kernel cannot carry such a tail. `ANF-011` removes the PSD assumption for the out-of-band route: a nontrivial negative Fourier--Laplace tail violates the universal conjugate-pair floor. `ANF-012` closes the analogous compact-band spectral-sign loophole: universality over conjugation-invariant multisets forces every continuous compact-band spectral profile `J` to satisfy `J>=0`. The only scalar sign freedom left is therefore **spatial** sign change of `F=widehat J`.

`ANF-013`--`ANF-015` then tested that freedom on long real lattices. With

\[
P_J(h)=\frac1h\sum_{k\in\mathbb Z}J(k/h),\qquad
p(J)=\inf_hP_J(h),
\]

the long simple/duplicated lattice family gives the survival ratio `C(J)/p(J)<C_MT`. `ANF-014` rewrites this ratio as a positive Mellin defect above `1+3/pi^2`; `ANF-015` proves the first Mellin floor is strictly non-sharp and introduces the multiplicative packing dual

\[
\sum_{n\ge1}w(nt)\le t^{-2},\qquad
D(w)=1+\int_1^\infty w(t)\left(1-\frac1t\right)dt.
\]

`ANF-016` now resolves that thermodynamic subproblem in the opposite direction from a no-go theorem. The explicit cubic spectrum

\[
J_*(x)=1-\frac38|x|-\frac74|x|^2+\frac98|x|^3
\qquad(|x|\le1)
\]

is nonnegative, has `p(J_*)=1`, and has exact cost

\[
C(J_*)=\frac{53}{40}=1.325<C_{\rm MT}.
\]

Moreover its spatial kernel satisfies

\[
\widehat J_*(m)=-\frac1{16\pi^2m^2}<0
\qquad(m\in\mathbb Z\setminus\{0\}),
\]

so it realizes precisely the spatial-sign escape left open by `ANF-012`. Weak duality immediately gives `D(w)<=53/40` for every admissible `ANF-015` packing witness. Therefore **the optimized thermodynamic packing dual cannot reach Montgomery--Taylor**. The all-scale periodization stage is settled: finite-size, non-lattice or complex configuration information is genuinely required to close the remaining universal affine scalar route.

The configuration-level branch remains distinct. `ANF-006` records a fully checked local ordered-gap certificate beating the Montgomery--Taylor baseline, while `ANF-007`--`ANF-009` show that simply increasing block size or point order inside the same pressure architecture does not supply a durable asymptotic strategy. Its next escape must alter the information carrier or bridge itself.

## Research question

Two distinct questions remain.

First, in the **universal affine support-one scalar** class, what is the next finite-configuration obstruction beyond thermodynamic periodization? For the explicit `J_*` of `ANF-016`, if

\[
F_*=\widehat J_*,
\qquad
L_n(h)=F_*(0)+2\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)F_*(kh),
\]

do finite simple/duplicated arithmetic progressions already force the largest admissible intercept `A` back to

\[
A-C(J_*)\le2-C_{\rm MT}?
\]

If not, can a lattice-surviving positive spectrum pass all finite real configurations, and where do vertically displaced conjugate configurations first impose a stronger constraint?

Second, in the **configuration-level** class, what genuinely new local memory, nonlinear defect, matrix/inertia statistic, window accounting or analytic bridge can retain a fixed gain after the `ANF-007`--`ANF-009` filters? Simply enlarging scalar blocks or point count inside the existing `F/Phi_n` pressure family remains ruled out as a durable asymptotic strategy.

## Why it may matter

The scalar branch has crossed a useful boundary. Before `ANF-016`, it was still plausible that optimizing the infinite-lattice packing dual might close the entire residual route without inspecting finite configurations. That is now impossible: an exact primal witness lies below Montgomery--Taylor. Any complete scalar no-go theorem must identify information that the thermodynamic limit discards.

Finite arithmetic progressions are the cheapest next layer because they retain explicit boundary corrections while staying exactly computable. If those corrections alone restore the Montgomery--Taylor ceiling, they would explain precisely why the thermodynamic cubic survivor is spurious. If they do not, the surviving candidate becomes a concrete probe for the first genuinely non-lattice or complex obstruction.

The configuration-level branch is the known escape from scalar compression. Its value lies in identifying pre-compression information that survives current local-pressure obstructions and can still be evaluated unconditionally for zeta zeros.

## Decisive test

For the scalar branch, begin with the exact finite-lattice energies

\[
L_n(h)=F_*(0)+2\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)F_*(kh).
\]

A simple `n`-site lattice gives an intercept constraint of the form `A<=1+L_n(h)`, while duplicating every site gives `A<=2L_n(h)`. Optimize these constraints over bounded `n` and `h`, first for `J_*` and then, only if necessary, for nearby positive-spectral perturbations.

A rigorous pair `(n,h)` for which the duplicated/simple finite-volume constraint implies

\[
A-C(J_*)\le2-C_{\rm MT}
\]

kills the cubic survivor and exposes a finite-size no-go mechanism worth generalizing. If every finite lattice test remains above the benchmark, move next to arbitrary finite real configurations and then conjugation-invariant complex multisets. A profile surviving these stages would still require a proof of the complete universal affine counting inequality before it could support any new zeta-zero proportion.

For any proposed out-of-band scalar construction, apply `ANF-011` before optimization. For any compact-band spectrally signed construction, apply `ANF-012`. Those branches remain closed unless the information carrier changes or the inequality becomes zeta-specific rather than universal.

For the configuration-level branch, first apply the exact block cap from `ANF-008` and the point-order envelope from `ANF-009`. A survivor must alter the local functional or bridge and then provide an evidence-matched finite inequality plus a complete passage to zeta zeros at the claimed trust tier.

## Evidence boundary

`ANF-016` is an exact **thermodynamic survivor**, not a universal affine certificate and not a `67.5%` zeta-zero theorem. It proves only that positive spectral density plus all long-lattice periodization constraints permit `C/p<C_MT`, and therefore that the `ANF-015` packing dual has optimum strictly below `C_MT`. Finite-volume lattice constraints, non-lattice real configurations and complex conjugate configurations are not controlled by that result.

`ANF-011` and `ANF-012` still close useful negative out-of-band tails and compact-band spectral sign changes inside the universal affine scalar template. Zeta-specific, non-affine, higher-order, matrix/inertia-before-compression and ordered-configuration mechanisms remain outside those theorems.

`ANF-006` establishes one verified configuration-level gain, while `ANF-007`--`ANF-009` constrain only the registered pressure family. They are not ceilings for richer Bellman/coboundary, altered-window, multi-profile, matrix or otherwise modified pre-compression methods.

## Research disposition

Accepted and narrowed. The thermodynamic multiplicative-packing stage is **resolved by counterexample**: `ANF-016` gives an explicit positive spectrum with `p=1` and `C=53/40<C_MT`, so no packing-dual optimization over the `ANF-015` constraints can recover Montgomery--Taylor. The live scalar question moves to finite-volume, non-lattice and complex universal configuration constraints. The configuration-level branch remains open only through a genuine carrier or bridge change.
