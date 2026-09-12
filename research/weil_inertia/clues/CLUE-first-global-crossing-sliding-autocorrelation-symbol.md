---
id: CLUE-weil-inertia-first-global-crossing-sliding-autocorrelation-symbol
type: research-clue
status: proposed
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-253-first-global-crossing-has-a-sliding-autocorrelation-flux-constraint.md
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

A meaningful positive outcome is an exact incompatibility, monotonicity, convexity, or moment constraint using at least two radii that cannot be reduced to the original null equation. A meaningful negative outcome is an explicit compact-support spectral model satisfying the full sliding family, which would decisively show that this representation alone does not bootstrap firstness to a contradiction.

Stress-test any proposed implication against generic translation-invariant first-crossing forms and against the pure logarithmic-core countermodel of `WI-239`; a conclusion that follows without using the explicit zeta source is not sufficient.

## Evidence boundary

No incompatibility theorem is known. `WI-253` proves only a necessary continuum of positive averages and does not assert pointwise positivity of `Sigma_r`, a lower rate for `lambda_r`, parity of the global first mode, or any RH consequence. The clue is therefore a separate research question, not an extension of the finding's evidence.