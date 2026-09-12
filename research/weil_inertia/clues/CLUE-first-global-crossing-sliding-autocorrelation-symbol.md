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
  - research/weil_inertia/findings/WI-259-first-prime-finite-scale-positivity-is-the-gate-for-the-phase-defect-program.md
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
\mathcal F_v(r)+J_v(r,t)\ge r\lambda_r,
\]

where

\[
J_v(r,t)=\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h).
\]

Thus any source-forced negative value `J_v(r,t)<=-epsilon` gives at least `epsilon` of strict firstness slack at that radius.

`WI-259` identifies the missing gate before this can genuinely use a prime atom at every hypothetical first crossing. The first prime enters only for `r>(log 2)/2`. A validated finite-scale theorem `lambda_{7/20}>0` would force `a_*>7/20`; then the fixed radius `r=7/20` is admissible and, because `log 2<7/10<log 3`, its discrete source contains exactly the single atom `n=2`. A public `FP-0.35` computational candidate targets precisely this theorem, but Mathia does not yet treat it as established because the corrected post-fix certificate has not been independently replayed and the source repository's theorem-status metadata is inconsistent.

## Research question

Can the actual zeta source at the first guaranteed prime scale force a negative localized cosine defect? More precisely, after independently establishing `lambda_{7/20}>0`, can the exact one-prime identity at `r=7/20`, together with compact support and positive-definiteness of `C_v`, force

\[
\inf_{t\in\mathbb R}J_v(7/20,t)<0?
\]

This is deliberately narrower than asking for more generic zero-mode regularity or immediately introducing several prime powers. `WI-257` proves that an abstract bounded self-adjoint perturbation can realize arbitrary domain vectors as zero modes, while `WI-259` shows that prime activation itself is not presently guaranteed without a finite-scale positivity theorem past `(log 2)/2`.

## Why it may matter

The scalar aperture family is information-complete only when its **exact** profile is known; firstness supplies merely a lower envelope. `WI-258` adds an independent inequality cone on profiles compatible with that lower envelope. At the abstract transform level the extra cone is genuinely nonredundant: a signed measure can have positive `min`-transform at every radius while violating the cosine-defect inequality.

At `r=7/20`, once the positivity gate is established, the discrete part becomes maximally simple:

\[
\frac{\log2}{\sqrt2}
\left(\frac7{10}-\log2\right)
(1-\cos(t\log2))C_v(\log2),
\]

with no `n>=3` atom. This removes multi-prime bookkeeping and exposes the exact competition between one arithmetic shift and the archimedean continuum. The coefficient is small near threshold, so mere prime activation is not itself a contradiction; any gain must come from the coupled source constraints.

## Decisive test

First audit the finite-scale gate rather than presuming it. Independently replay or independently prove the public `FP-0.35` claim `lambda_{7/20}>0` in the same localized-Weil normalization used by WI-238. The current external state is only `COMPUTATIONAL-CERTIFICATE + NEEDS-INDEPENDENT-REPLAY`; README status or a finite Ritz eigenvalue is not sufficient.

If the gate validates, freeze `r=7/20` and study the exact identity

\[
\begin{aligned}
J_v(7/20,t)
={}&\frac{\log2}{\sqrt2}
\left(\frac7{10}-\log2\right)
(1-\cos(t\log2))C_v(\log2)\\
&+\int_0^{7/10}
\left(\frac7{10}-h\right)(1-\cos(th))w(h)C_v(h)\,dh
\end{aligned}
\]

under the exact constraints that `C_v` is the autocorrelation of a function supported in `[-a_*,a_*]`, `C_v(0)=1`, and `v` is a first-crossing zero mode. Keep the single von-Mangoldt atom and continuous `w(h)` contribution separate.

A meaningful positive outcome is a source-specific bound

\[
\inf_t J_v(7/20,t)\le-\varepsilon
\]

with `epsilon>0` forced for every admissible first-crossing mode, or another exact multi-frequency incompatibility. By `WI-258` this would immediately imply

\[
\mathcal F_v(7/20)-(7/20)\lambda_{7/20}\ge\varepsilon.
\]

A meaningful negative outcome is either failure of the finite-scale positivity gate under independent replay, or an explicit source-compatible compact-support autocorrelation model satisfying the scalar aperture bounds and the full phase-modulated cone at `r=7/20`.

Stress-test every proposed implication against the pure logarithmic-core crossing of `WI-239` and the rank-two bounded-perturbation construction of `WI-257`. Also respect the external first-prime operator facts audited in `WI-259`: the prime overlap has operator norm one immediately after threshold and is indefinite, while the endpoint archimedean potential can absorb it at `L=7/20`. Therefore the gain must come from the full source coupling or first-crossing structure, not from treating `n=2` as a small or automatically destabilizing perturbation.

## Evidence boundary

No incompatibility theorem is known. `WI-253` proves only a necessary continuum of positive aperture averages and does not assert pointwise positivity of `Sigma_r`, a lower rate for `lambda_r`, parity of the global first mode, or any RH consequence. `WI-254` proves that the exact aperture profile is an invertible `min`-transform of the source-weighted real autocorrelation, but pointwise firstness cannot be differentiated to read prime-threshold signs and the small-radius lower bound is asymptotically saturated at leading order.

`WI-255` shows that the first `O(r)` correction is universal on a first-crossing null mode: the prime and regular archimedean pieces cancel against `Q_W(v)=0`. `WI-256` identifies the next remainder as the local translation-defect modulus

\[
E_v(r)=\int_0^{2r}\left(\frac rh-\frac12\right)(1-C(h))\,dh\ge0,
\]

but the available `H^log` control does not determine its quadratic coefficient. `WI-257` then proves that generic bounded-perturbation zero-modehood cannot supply the missing regularity.

`WI-258` gives the exact identities

\[
Q_W^{a_*}(e^{itx}v)=2\int(1-\cos(th))\,d\mu_v(h)\ge0
\]

and

\[
S_v(r)+J_v(r,t)\ge0,
\qquad
S_v(r)=\mathcal F_v(r)-r\lambda_r.
\]

These are stronger than scalar `min`-transform positivity as inequality constraints, but analogous modulation inequalities exist for generic translation-invariant nonnegative forms. `WI-259` further shows that the first-prime version is conditional on a positivity margin past `(log2)/2`. The public `FP-0.35` certificate is not yet part of Mathia's established evidence and must not be silently promoted to a theorem.

## Research disposition

The direction remains `accepted`, but the live branch is narrowed. **First settle the `L=7/20` finite-scale positivity gate.** If it validates, use the exact one-prime radius `r=7/20` before considering larger radii or several prime powers. If it fails, return to proving any rigorous positivity margin past `(log2)/2`; do not presume that a hypothetical first crossing sees a von-Mangoldt atom.

After the gate, the target is still source-specific: combine the single `n=2` threshold weight, the sign-changing archimedean continuum, positive-definite autocorrelation constraints, and first-crossing slack to force or refute a negative localized cosine defect. A successful estimate should be stated directly as a quantitative lower bound for firstness slack through `WI-258`; a failure should identify a concrete source-compatible model rather than another generic bounded-perturbation example.