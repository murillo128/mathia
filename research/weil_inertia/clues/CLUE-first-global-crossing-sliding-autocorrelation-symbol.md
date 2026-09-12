---
id: CLUE-weil-inertia-first-global-crossing-sliding-autocorrelation-symbol
type: research-clue
status: accepted
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-253-first-global-crossing-has-a-sliding-autocorrelation-flux-constraint.md
  - research/weil_inertia/findings/WI-254-sliding-aperture-profile-is-invertible-but-small-scale-firstness-is-saturated.md
  - research/weil_inertia/findings/WI-255-first-small-aperture-correction-is-universal-and-cannot-bootstrap.md
---

# Can the sliding autocorrelation symbols exclude a first global Weil zero mode?

## Observation

`WI-253` shows that under RH failure the first unrestricted localized Weil zero mode `v` must satisfy, for every `0<r<a_*`,

\[
\frac1{2\pi}\int_{\mathbb R}\Sigma_r(z)|\widehat v(z)|^2\,dz
\ge r\lambda_r>0,
\]

where `Sigma_r` is an explicit finite-prime plus archimedean cosine symbol and `|vhat|^2` is a nonnegative spectral density. This sliding-center formulation bypasses the reflected half-line Hankel obstruction of the first-odd-mode route because arbitrary translated windows are allowed at the first global crossing.

## Research question

Exploit the **simultaneous** family `{Sigma_r:0<r<a_*}` rather than one radius at a time. Does the piecewise-linear dependence on `r`, including the threshold changes at `r=(log n)/2`, force a spectral distribution incompatible with a compactly supported zero mode of `A_{a_*}`? Equivalently, can positivity/uncertainty constraints on `|vhat|^2`, together with the exact zero-mode equation, show that not all of the averages in `WI-253` can remain strictly positive?

## Why it may matter

The current odd localization program retains a difficult signed radial observable and cannot import generic one-sign ground-state theory. `WI-253` replaces that observable by ordinary autocorrelation, so harmonic-analysis tools can act directly on a nonnegative spectral density. A contradiction from two or more radii would be a genuine first-crossing bootstrap rather than another uniform all-test discrepancy bound.

## Decisive test

First derive the exact `r`-variation of `Sigma_r` and of

\[
\mathcal F_v(r)=\frac1{2\pi}\int\Sigma_r(z)|\widehat v(z)|^2\,dz,
\]

with correct one-sided derivatives at every prime-power threshold. Keep the prime atoms and continuous archimedean density separate. Then test whether a nonnegative spectral density coming from a function supported in `[-a_*,a_*]` can satisfy the entire inequality family together with `Q_W(v)=0`.

A meaningful positive outcome is an exact incompatibility, monotonicity, convexity, or moment constraint using at least two radii that cannot be reduced to the original null equation. A meaningful negative outcome is an explicit compact-support spectral model satisfying the full sliding family, or an exact reduction showing that a proposed refinement is algebraically redundant with the null equation.

Stress-test any proposed implication against generic translation-invariant first-crossing forms and against the pure logarithmic-core countermodel of `WI-239`; a conclusion that follows without using the explicit zeta source is not sufficient.

## Evidence boundary

No incompatibility theorem is known. `WI-253` proves only a necessary continuum of positive averages and does not assert pointwise positivity of `Sigma_r`, a lower rate for `lambda_r`, parity of the global first mode, or any RH consequence. `WI-254` proves that the exact aperture profile is an invertible `min`-transform of the source-weighted real autocorrelation, but it also shows that pointwise firstness cannot be differentiated to read prime-threshold signs and that the small-radius lower bound is asymptotically saturated at leading order.

`WI-255` goes one order further: `H^log` regularity gives a genuine `O(r)` expansion, but on a first-crossing null mode the prime and regular archimedean pieces cancel exactly against `Q_W(v)=0`. The coefficient is universal, and comparison with `r lambda_r` yields only the already-known constant-function variational bound `mu_1 <= 1-log 2`. Thus neither the leading term nor the first subleading term supplies source-sensitive small-radius rigidity. The clue remains a separate research question because medium radii, threshold coupling, and operator-level zero-mode information are not resolved by that cancellation.

## Research disposition

The direction survives derivation, stress testing, and prior-art audit and remains worth continued investigation, but the small-aperture branch is now substantially narrower. `WI-254` validates that the full aperture parameter carries the complete real-autocorrelation information of this source representation while closing derivative-sign inference and a uniform multiplicative reserve. `WI-255` additionally closes the entire first `O(r)` correction as a bootstrap: its apparently arithmetic coefficient is algebraically redundant with the scalar null equation.

The precise unresolved gate is therefore to obtain **additional control on the exact profile that is not reducible to one scalar null identity**. The most credible next targets are medium-radius curvature/slope relations across one or more prime-power thresholds, a genuinely higher-order small-radius invariant if extra regularity can first be proved, or a relation extracted from the full operator equation `A_{a_*}v=0` rather than only from `Q_W(v)=0`.