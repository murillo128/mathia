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
  - research/weil_inertia/findings/WI-263-full-span-autocorrelations-can-null-the-first-prime-and-screen-the-localized-phase-defect.md
  - research/weil_inertia/findings/WI-264-finite-aperture-endpoint-autocorrelations-screen-all-prime-layers.md
  - research/weil_inertia/findings/WI-265-endpoint-screening-survives-an-abstract-first-crossing-compression-model.md
---

# Can Suzuki-specific first-crossing rigidity exclude finite-aperture source screening?

## Observation

`WI-253` and `WI-258` give two exact families that every hypothetical first unrestricted localized Weil zero mode must satisfy. With

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right],
\]

the first-crossing null mode obeys

\[
\mathcal F_v(r)=\int_0^{2a_*}\min(h,2r)\,d\mu_v(h)
\ge r\lambda_r>0
\qquad(0<r<a_*),
\]

and phase modulation gives

\[
\mathcal F_v(r)+J_v(r,t)\ge r\lambda_r,
\qquad
J_v(r,t)=\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h).
\]

A negative `J_v(r,t)` would therefore force strict firstness slack. The open problem is no longer whether the explicit source by itself can force such negativity.

`WI-264` closes that weaker route at **every finite aperture**. For any finite `a>h_0/2`, where `h_0` is the unique sign-change point of Suzuki's continuous source, an antisymmetric pair of sufficiently narrow endpoint bumps has a positive-definite full-span autocorrelation whose open zero interval contains every active prime-power lag `log n<2a`. Simultaneously its self-correlation lies where `w>0` and its cross-correlation lies where `w<0`. Hence every discrete von-Mangoldt mass is screened exactly and

\[
\mathcal M_v(t)\ge0,
\qquad
J_v(r,t)\ge0,
\qquad
\mathcal F_v(r)\ge0
\]

for all admissible `r,t` in that countermodel. This generalizes the one-prime obstruction of `WI-263`: adding more finite prime layers or more phase frequencies cannot by itself break screening.

`WI-265` closes a second generic escape route. The **same screened endpoint-bump vector** can be made the exact terminal zero mode of the positive rank-one-defect operator

\[
A=I-|v\rangle\langle v|,
\]

while every proper centered compression is strictly positive. For every fixed `r<a`, every translated interval of length `2r` even has a common positive Rayleigh reserve, and the localized terminal mode obeys the corresponding center-averaged firstness inequality. Thus endpoint screening is compatible with an exact abstract first crossing, an exact null equation, all proper aperture positivity, and the generic sliding-localization argument. What the model does **not** reproduce is the arithmetic identity that turns that localization defect into the particular source functional `mathcal F_v`.

There is also no longer a finite-scale activation gate at `L=7/20`. `WI-253` already records the certified theorem `lambda_0.8>0` for arbitrary complex tests, so any hypothetical first global crossing satisfies `a_*>0.8`. The `FP-0.35` audits in `WI-259`--`WI-262` remain useful artifact audits, but they are not a prerequisite for this clue.

## Research question

Can the **Suzuki-specific information not reproduced by WI-264/WI-265** forbid the endpoint-gap screening geometry? The two surviving constraints still have the same formal statements,

\[
\boxed{\mathcal F_v(r)\ge r\lambda_r\quad\text{for every }0<r<a_*}
\]

and

\[
\boxed{A_{a_*}^{\rm Weil}v=0,}
\]

but `WI-265` changes what may legitimately be extracted from them. Generic zero-modehood, generic nested positivity, uniform positivity on translated shorter windows, and their averaged localization reserve are now known to be insufficient. A successful argument must use the **specific equality between Suzuki's quadratic form and the von-Mangoldt/archimedean autocorrelation functional**, or the detailed arithmetic kernel in the null equation.

The target is therefore a source-specific quantitative constraint on the autocorrelation that cannot be satisfied by the screened endpoint-bump family. Useful forms would include a rigorous lower bound on the actual `mathcal F_v(r)` relative to `r lambda_r`, a lower bound on autocorrelation mass at one or more von-Mangoldt lags derived from the explicit null equation, a prohibition on a long interior autocorrelation gap for Suzuki's kernel, or a global Fourier/moment identity unavailable to arbitrary positive compression families.

## Decisive test

Start from a hypothetical first-crossing mode with `a_*>0.8`; do not recertify `FP-0.35` as a prerequisite. Do not attempt to rule out endpoint bumps from abstract first-crossing spectral structure: `WI-265` already supplies an exact countermodel to that implication.

The first direct test is the actual lower-envelope family. For the complete screened endpoint-bump family of `WI-264`, compute or bound

\[
\mathcal F_v(r)
\]

uniformly in the bump width and compare it with rigorous information on `r lambda_r`. If some radius forces

\[
\mathcal F_v(r)<r\lambda_r,
\]

uniformly for every screened member, then the **source-specific** firstness identity rules out the geometry even though abstract firstness does not. The useful result is a uniform analytic exclusion, not a numerical failure of one chosen bump.

The second direct test is the actual null equation. Insert the endpoint-gap geometry into Suzuki's explicit kernel/operator equation and ask whether the finite von-Mangoldt translations plus the archimedean term force nonzero mass in the autocorrelation gap or another contradiction. A theorem of the form

\[
A_a^{\rm Weil}v=0
\quad\Longrightarrow\quad
\sum_{\log n<2a}c_n|C_v(\log n)|\ge\eta(a)>0
\]

for source-justified `c_n>=0` would invalidate `WI-264`; an analogous theorem for a continuous set of lags or a Fourier moment would be equally useful.

A meaningful negative outcome now has to pass the stronger gate: construct a **source-compatible** compact-support family retaining the all-prime screening of `WI-264` and satisfying the actual quantitative aperture lower envelope to the available rigorous precision, or construct a screened vector satisfying Suzuki's actual null equation. Another abstract operator model is no longer enough; `WI-265` has already supplied that barrier.

## Stress tests

Any proposed implication must survive the existing countermodels. `WI-257` shows that generic bounded self-adjoint zero-modehood gives no useful translation regularity. `WI-263` rules out one-prime source-sign/Bochner arguments. `WI-264` rules out the idea that activating finitely many additional prime powers removes the screening freedom. `WI-265` further rules out deductions from generic exact zero-modehood plus strict positivity of every proper centered or translated shorter window.

Therefore a proof that uses only compact support, positive-definiteness, the finite source atoms and their signs, nested Rayleigh positivity, or a generic Hilbert-space null equation is already known to be insufficient. The arithmetic operator must enter before the argument discards the distinction between Suzuki's form and the rank-one compression countermodel.

## Evidence boundary

No theorem currently proves that an actual Suzuki first-crossing null vector has nonzero autocorrelation at any prescribed prime-power lag. Nor is there a known quantitative theorem excluding a macroscopic autocorrelation zero interval from the **specific** equation `A_{a_*}^{Weil}v=0`.

`WI-264` is not itself a zeta zero mode. `WI-265` upgrades it only to an abstract exact zero mode with a complete positive first-crossing compression profile; it deliberately does not satisfy Suzuki's source identity by construction. Consequently neither finding settles whether the actual inequality `mathcal F_v(r) >= r lambda_r` excludes the endpoint family. That is now the sharp scalar gate.

The certified `lambda_0.8>0` theorem is used only to remove the obsolete prime-activation dependency and to place any hypothetical first crossing beyond `0.8`. It does not provide a usable lower profile for `lambda_r` at all radii, and it does not approach RH by itself.

## Research disposition

The clue remains `accepted`, but its live gate is now explicitly **source-specific**. Do not spend further research passes recertifying `FP-0.35` merely to activate a prime, enlarging the aperture merely to add finite prime layers, or deriving endpoint coercivity from abstract nested positivity/null-vector facts.

Attack either the actual source-side lower-envelope family `mathcal F_v(r) >= r lambda_r` on the complete screened endpoint family, or the detailed Suzuki null equation before reducing it to generic spectral information. If both of those source-specific constraints can also be matched by a screened family, record that barrier and retire the present phase-defect route until a genuinely stronger arithmetic or operator invariant is available.