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
  - research/weil_inertia/findings/WI-258-phase-modulation-couples-firstness-slack-to-localized-cosine-defect.md
---

# Can the sliding autocorrelation symbols exclude a first global Weil zero mode?

## Observation

`WI-253` shows that under RH failure the first unrestricted localized Weil zero mode `v` must satisfy, for every `0<r<a_*`,

\[
\frac1{2\pi}\int_{\mathbb R}\Sigma_r(z)|\widehat v(z)|^2\,dz
\ge r\lambda_r>0,
\]

where `Sigma_r` is an explicit finite-prime plus archimedean cosine symbol and `|vhat|^2` is a nonnegative spectral density. This sliding-center formulation bypasses the reflected half-line Hankel obstruction of the first-odd-mode route because arbitrary translated windows are allowed at the first global crossing.

`WI-258` adds a second exact parameter without changing support. If

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right]
\]

is the source-weighted autocorrelation measure of `WI-254`, then phase modulation `v_t(x)=e^{itx}v(x)` gives

\[
\int_0^{2a_*}(1-\cos(th))\,d\mu_v(h)\ge0
\qquad(t\in\mathbb R),
\]

and, after the same translated-window averaging,

\[
\mathcal F_v(r)
+J_v(r,t)
\ge r\lambda_r,
\]

where

\[
J_v(r,t)=
\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h).
\]

Thus any source-forced negative value `J_v(r,t)<=-epsilon` gives at least `epsilon` of strict firstness slack at that radius.

## Research question

Exploit the **simultaneous two-parameter family** in `(r,t)`, rather than one aperture at a time. Can the actual von-Mangoldt atoms, the sign-changing archimedean density, compact support, and positive-definiteness of `C_v` force a negative localized cosine defect at some medium radius? Equivalently, can the prime-threshold phase structure prevent a compactly supported first-crossing zero mode from satisfying all of the scalar aperture and modulation inequalities simultaneously?

This question is deliberately narrower than asking for more generic zero-mode regularity. `WI-257` proves that an abstract bounded self-adjoint perturbation can realize arbitrary domain vectors as zero modes, so any successful continuation must use the specific zeta source in `mu_v`.

## Why it may matter

The scalar aperture family is information-complete only when its **exact** profile is known; firstness supplies merely a lower envelope. `WI-258` adds an independent inequality cone on profiles compatible with that lower envelope. At the abstract transform level the extra cone is genuinely nonredundant: a signed measure can have positive `min`-transform at every radius while violating the cosine-defect inequality.

The localized phase correction is also threshold-local. A prime-power atom contributes only once `2r>log n`, and then with the explicit factor

\[
\frac{\Lambda(n)}{\sqrt n}
(2r-\log n)(1-\cos(t\log n))C_v(\log n).
\]

Frequency therefore gives a way to suppress or emphasize individual prime-power shifts without paying extra spatial support. This is the first current interface in the line that turns a quantitative signed source defect directly into stronger firstness slack.

## Decisive test

Work first in the smallest medium-radius regimes containing the first few prime powers. For fixed `r`, study

\[
\inf_{t\in\mathbb R}J_v(r,t)
\]

under the exact constraints that `C_v` is the autocorrelation of a function supported in `[-a_*,a_*]`, `C_v(0)=1`, and `mu_v` has the zeta factorization above. Keep the finite von-Mangoldt atoms and continuous `w(h)` contribution separate.

A meaningful positive outcome is a source-specific bound

\[
\inf_t J_v(r,t)\le-\varepsilon
\]

with `epsilon>0` forced for every admissible first-crossing mode, or another exact multi-radius/multi-frequency incompatibility that cannot hold for arbitrary bounded perturbations. By `WI-258` this would immediately imply

\[
\mathcal F_v(r)-r\lambda_r\ge\varepsilon.
\]

A meaningful negative outcome is an explicit source-compatible compact-support autocorrelation model satisfying the scalar aperture bounds and the full phase-modulated cone, or an exact reduction showing that the proposed phase optimization is already implied by the zero-mode equation plus known autocorrelation positivity.

Stress-test every proposed implication against the pure logarithmic-core crossing of `WI-239` and the rank-two bounded-perturbation construction of `WI-257`. The generic fact that phase modulation preserves support is not sufficient; the gain must come from the explicit zeta source or from a compact-support/autocorrelation constraint that interacts nontrivially with that source.

## Evidence boundary

No incompatibility theorem is known. `WI-253` proves only a necessary continuum of positive aperture averages and does not assert pointwise positivity of `Sigma_r`, a lower rate for `lambda_r`, parity of the global first mode, or any RH consequence. `WI-254` proves that the exact aperture profile is an invertible `min`-transform of the source-weighted real autocorrelation, but pointwise firstness cannot be differentiated to read prime-threshold signs and the small-radius lower bound is asymptotically saturated at leading order.

`WI-255` shows that the first `O(r)` correction is universal on a first-crossing null mode: the prime and regular archimedean pieces cancel against `Q_W(v)=0`. `WI-256` identifies the next remainder as the local translation-defect modulus

\[
E_v(r)=\int_0^{2r}\left(\frac rh-\frac12\right)(1-C(h))\,dh\ge0,
\]

but the available `H^log` control does not determine its quadratic coefficient. `WI-257` then proves that generic bounded-perturbation zero-modehood cannot supply the missing regularity.

`WI-258` does **not** evade those barriers by a hidden smoothness assumption. Instead it gives the exact identities

\[
Q_W^{a_*}(e^{itx}v)
=2\int(1-\cos(th))\,d\mu_v(h)\ge0
\]

and

\[
S_v(r)+J_v(r,t)\ge0,
\qquad
S_v(r)=\mathcal F_v(r)-r\lambda_r.
\]

These are stronger than scalar `min`-transform positivity as inequality constraints, but analogous modulation inequalities exist for generic translation-invariant nonnegative forms. Therefore they become RH-facing only if the explicit von-Mangoldt/archimedean structure forces a sign or quantitative deficit that generic models need not satisfy.

## Research disposition

The direction remains `accepted`. The small-aperture regularity branch is closed unless new source-specific information appears. The live branch is now the **medium-radius phase-defect problem**: use the actual prime-threshold weights in `J_v(r,t)`, together with positive-definite autocorrelation constraints and compact support, to force or refute a negative localized cosine defect.

Prioritize the first few guaranteed prime-power thresholds and exact finite positivity constraints before introducing larger numerical searches. A successful estimate should be stated directly as a quantitative lower bound for firstness slack through `WI-258`; a failure should identify a concrete source-compatible model rather than another generic bounded-perturbation example.