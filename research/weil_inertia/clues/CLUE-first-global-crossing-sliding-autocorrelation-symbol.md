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
---

# Can genuine first-crossing rigidity exclude finite-aperture source screening?

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

There is also no longer a finite-scale activation gate at `L=7/20`. `WI-253` already records the certified theorem `lambda_0.8>0` for arbitrary complex tests, so any hypothetical first global crossing satisfies `a_*>0.8`. The `FP-0.35` audits in `WI-259`--`WI-262` remain useful artifact audits, but they are not a prerequisite for this clue.

## Research question

Can the **genuine first-crossing information not reproduced by WI-264** forbid the endpoint-gap screening geometry? The two surviving inputs are especially concrete:

\[
\boxed{\mathcal F_v(r)\ge r\lambda_r\quad\text{for every }0<r<a_*}
\]

and

\[
\boxed{A_{a_*}v=0.}
\]

The target is to derive from one or both a quantitative constraint on the autocorrelation that cannot be satisfied by the screened endpoint-bump family. Useful forms would include a lower bound on autocorrelation mass at one or more von-Mangoldt lags, a prohibition on a long interior autocorrelation gap, a quantitative support-spreading theorem for an actual null vector, or a source-specific relation coupling the zero interval of `C_v` to nonzero translated copies of `v`.

The question is deliberately stronger than “can another prime threshold help?” `WI-264` proves that every finite set of active prime thresholds can be put in the same autocorrelation gap. A successful continuation must therefore use the **equation or firstness reserve**, not the cardinality or signs of the finite source.

## Decisive test

Start from a hypothetical first-crossing mode with `a_*>0.8`; do not recertify `FP-0.35` as a prerequisite. Test the endpoint-gap geometry directly against the two first-crossing constraints.

A strong positive outcome would prove that if a normalized full-span `v` satisfies `A_a v=0` and `lambda_r>0` for every `r<a`, then its autocorrelation cannot vanish on an interval containing all active `log n`, or must satisfy a quantitative lower bound such as

\[
\sum_{\log n<2a} c_n\,|C_v(\log n)|\ge\eta(a)>0
\]

for source-justified nonnegative coefficients `c_n`. Any such theorem would invalidate the WI-264 screening model for genuine first-crossing modes and reopen the phase-defect mechanism.

A second viable outcome would use the entire lower-envelope family rather than the null equation. For the explicit endpoint-bump family, compute or bound `\mathcal F_v(r)` uniformly in the bump width and compare it with rigorous information on `r\lambda_r`. If some radius forces

\[
\mathcal F_v(r)<r\lambda_r,
\]

then firstness alone rules out that screening geometry. The useful result is a uniform exclusion of the whole family, not a numerical failure of one chosen bump.

A meaningful negative outcome is an explicit source-compatible compact-support family that simultaneously retains the all-prime screening of `WI-264` **and** satisfies the quantitative aperture lower envelope to the precision currently known, or an exact model satisfying an analogue of the null equation. That would show that even firstness-level scalar information remains too weak and would push the line toward genuinely operator-valued constraints.

## Stress tests

Any proposed implication must survive the existing countermodels. `WI-257` shows that generic bounded self-adjoint zero-modehood gives no useful translation regularity. `WI-263` rules out one-prime source-sign/Bochner arguments. `WI-264` rules out the stronger idea that activating finitely many additional prime powers removes the screening freedom. Therefore a proof that only uses compact support, positive-definiteness, the list of finite source atoms, or their signs is already known to be insufficient.

The first-crossing operator equation is the most promising remaining discriminator because it couples `v` to all translations appearing in Suzuki's exact localized form rather than only to scalar autocorrelation moments. If that equation is reduced to a scalar inequality that WI-264 also satisfies, the reduction has discarded the very information this clue is trying to exploit.

## Evidence boundary

No theorem currently proves that an actual first-crossing null vector has nonzero autocorrelation at any prescribed prime-power lag. Nor is there a known quantitative theorem excluding a macroscopic autocorrelation zero interval from `A_{a_*}v=0`. `WI-264` is not itself a zeta zero mode and does not satisfy the firstness lower envelope by construction; it is only a decisive countermodel to weaker source-sign and positive-definiteness arguments.

The certified `lambda_0.8>0` theorem is used only to remove the obsolete prime-activation dependency and to place any hypothetical first crossing beyond `0.8`. It does not provide a usable lower profile for `lambda_r` at all radii, and it does not approach RH by itself.

## Research disposition

The clue remains `accepted`, but its live gate has changed. **Do not spend further research passes recertifying `FP-0.35` merely to activate a prime, and do not enlarge the aperture merely to add more finite prime layers.** Instead attack whether the full firstness family or the exact localized null equation forbids the endpoint-gap autocorrelation screening proved in `WI-264`.

If neither firstness nor the null equation can distinguish the screened family, record that barrier and retire the phase-defect route until a new operator or arithmetic invariant is available.