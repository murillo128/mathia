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
  - research/weil_inertia/findings/WI-256-next-small-aperture-remainder-is-a-local-translation-defect-modulus.md
  - research/weil_inertia/findings/WI-257-bounded-perturbation-zero-modes-do-not-upgrade-translation-regularity.md
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

Exploit the **simultaneous** family `{Sigma_r:0<r<a_*}` rather than one radius at a time. Does the piecewise-linear dependence on `r`, including the threshold changes at `r=(log n)/2`, force a spectral distribution incompatible with a compactly supported zero mode of `A_{a_*}`? Equivalently, can positivity/uncertainty constraints on `|vhat|^2`, together with the exact zero-mode equation and the source-specific structure of its prime-translation perturbation, show that not all of the averages in `WI-253` can remain strictly positive?

## Why it may matter

The current odd localization program retains a difficult signed radial observable and cannot import generic one-sign ground-state theory. `WI-253` replaces that observable by ordinary autocorrelation, so harmonic-analysis tools can act directly on a nonnegative spectral density. A contradiction from two or more radii would be a genuine first-crossing bootstrap rather than another uniform all-test discrepancy bound.

## Decisive test

First derive the exact `r`-variation of `Sigma_r` and of

\[
\mathcal F_v(r)=\frac1{2\pi}\int\Sigma_r(z)|\widehat v(z)|^2\,dz,
\]

with correct one-sided derivatives at every prime-power threshold. Keep the prime atoms and continuous archimedean density separate. Then test whether a nonnegative spectral density coming from a function supported in `[-a_*,a_*]` can satisfy the entire inequality family together with the **specific** zero-mode equation for Suzuki's von-Mangoldt weighted translation operator.

A meaningful positive outcome is an exact incompatibility, monotonicity, convexity, or moment constraint using at least two radii that cannot be reduced to the original null equation or to generic bounded-perturbation regularity. A meaningful negative outcome is an explicit compact-support spectral model satisfying the full sliding family, or an exact reduction showing that a proposed refinement is algebraically redundant with the null equation.

Stress-test any proposed implication against generic translation-invariant first-crossing forms, against the pure logarithmic-core countermodel of `WI-239`, and against the bounded-perturbation rank-two zero-mode stress test of `WI-257`; a conclusion that follows without using the explicit zeta source is not sufficient.

## Evidence boundary

No incompatibility theorem is known. `WI-253` proves only a necessary continuum of positive averages and does not assert pointwise positivity of `Sigma_r`, a lower rate for `lambda_r`, parity of the global first mode, or any RH consequence. `WI-254` proves that the exact aperture profile is an invertible `min`-transform of the source-weighted real autocorrelation, but it also shows that pointwise firstness cannot be differentiated to read prime-threshold signs and that the small-radius lower bound is asymptotically saturated at leading order.

`WI-255` goes one order further: `H^log` regularity gives a genuine `O(r)` expansion, but on a first-crossing null mode the prime and regular archimedean pieces cancel exactly against `Q_W(v)=0`. The coefficient is universal, and comparison with `r lambda_r` yields only the already-known constant-function variational bound `mu_1 <= 1-log 2`. Thus neither the leading term nor the first subleading term supplies source-sensitive small-radius rigidity.

`WI-256` identifies the exact next remainder. After the `WI-255` terms,

\[
\mathcal F_v(r)-r\log(1/r)-r(\psi(2)-\log(4\pi))
=E_v(r)+\frac72r^2+o(r^2),
\]

where

\[
E_v(r)=\int_0^{2r}\left(\frac rh-\frac12\right)(1-C(h))\,dh\ge0.
\]

The available `H^log` control does not force `E_v(r)=O(r^2)`, and generic membership in Suzuki's operator domain `D(A_a)` does not determine its quadratic coefficient either.

`WI-257` closes the next generic escape hatch. After scaling to `(-1,1)`, Suzuki's operators are a fixed logarithmic self-adjoint operator `T_0` plus bounded self-adjoint perturbations `K_a`, so all scaled operator domains equal `D(T_0)`. Moreover every vector in `D(T_0)` can be made a zero mode by some rank-at-most-two bounded self-adjoint perturbation, while `D(T_0)` contains both a normalized constant with `E(r)=r^2/2` and smooth compactly supported vectors with `E(r)=O(r^3)`. Thus the abstract equation `(T_0+K)v=0` with bounded `K` cannot determine the quadratic translation coefficient. Any successful small-radius continuation must use the actual arithmetic structure of `K_{a_*}`, not zero-modehood as generic operator regularity.

The clue remains a separate research question because medium radii, prime-power threshold coupling, and source-specific operator identities are not resolved by these barriers.

## Research disposition

The direction remains accepted, but its small-aperture branch is now conditional on **source-specific** zero-mode information rather than generic regularity. `WI-254` validates that the full aperture parameter carries the complete real-autocorrelation information of this source representation while closing derivative-sign inference and a uniform multiplicative reserve. `WI-255` closes the entire first `O(r)` correction as a bootstrap, `WI-256` isolates the next obstruction as the local translation-defect modulus `E_v`, and `WI-257` proves that generic bounded-perturbation use of `A_{a_*}v=0` cannot control that modulus.

The precise unresolved gate is therefore to extract an identity or inequality from the **specific** finite von-Mangoldt translation sum, its threshold dependence in `a`/`r`, and the archimedean kernel that is not valid for arbitrary bounded self-adjoint perturbations. Absent such a source-specific estimate, prioritize medium-radius curvature/slope relations across one or more prime-power thresholds or another relation extracted from the full simultaneous operator family rather than only from `Q_W(v)=0`.