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
  - research/weil_inertia/findings/WI-266-suzuki-null-equation-rules-out-endpoint-bump-screening.md
---

# Can Suzuki-specific first-crossing rigidity exclude general finite-aperture screening?

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

`WI-264` showed that the explicit source signs and any finite collection of prime-power layers can be screened by two sufficiently narrow antisymmetric endpoint bumps. `WI-265` strengthened that barrier: the same screened vector can be the exact terminal zero mode of an abstract positive rank-one-defect operator with strict positivity on every proper centered and translated shorter window. Generic first-crossing spectral structure therefore does not defeat the geometry.

`WI-266` now supplies the missing source-specific discrimination. Suzuki's actual null equation has regular kernel

\[
k(h)=e^{h/2}-\frac{e^{-5h/2}}{1-e^{-2h}},
\qquad k'(h)>0\quad(h>0),
\]

away from the local singularity and von-Mangoldt atoms. For every `WI-264` endpoint bump there is a nonempty open interval in the middle support gap on which the vector and all prime translations vanish. On that interval the exact null equation reduces to the continuous convolution, and strict monotonicity makes the positive left endpoint bump dominate the negative right endpoint bump pointwise. Hence `A_a^{Weil}v` has a fixed nonzero sign there, contradicting nullity.

Thus the two-endpoint screening family is no longer a live countermodel. The remaining question is whether this source-specific rigidity extends from that geometry to arbitrary first-crossing modes, or whether a more complicated multi-component support can use prime translations to cancel the continuous kernel.

There is also no finite-scale activation gate at `L=7/20`. `WI-253` records the certified theorem `lambda_0.8>0` for arbitrary complex tests, so any hypothetical first global crossing satisfies `a_*>0.8`. The `FP-0.35` audits in `WI-259`--`WI-262` remain useful artifact audits but are not prerequisites for this clue.

## Research question

Can Suzuki's **specific localized null equation and source identity** force a support-spreading or no-long-gap constraint strong enough to exclude every screened first-crossing mode?

The two source-specific inputs remain

\[
\boxed{\mathcal F_v(r)\ge r\lambda_r\quad\text{for every }0<r<a_*}
\]

and

\[
\boxed{A_{a_*}^{\rm Weil}v=0.}
\]

but `WI-266` changes the target. It is no longer useful to test the already-excluded two-endpoint family or to ask whether abstract nesting alone forces overlap at a prime lag. The live issue is whether the pointwise/distributional equation can be converted into a geometry-independent theorem: for example, a quantitative prohibition on a macroscopic support gap, a lower bound on support propagation under the translations `\pm\log n`, a forced nonzero autocorrelation mass at some arithmetic lag, or a sign/maximum-principle argument for a suitable extremal component of a null vector.

## Decisive test

Start from a hypothetical first-crossing mode with `a_*>0.8` and use Suzuki's exact operator before collapsing to generic spectral data. Write the null equation on a connected component of a support gap or on a region where only a controlled subset of prime translations can be active. Test whether strict monotonicity of the continuous kernel, together with the finite translation graph generated by the active `\log n`, forces one-sided sign or propagation.

A strong positive outcome would prove a source-specific statement of the schematic form

\[
A_a^{\rm Weil}v=0
\quad\Longrightarrow\quad
\text{every gap/component configuration obeys a quantitative propagation constraint},
\]

with a consequence that rules out all finite-aperture source screening relevant to first crossing. A weaker but still useful result would characterize exactly which support graphs can evade the `WI-266` sign argument and thereby reduce the possible exceptional geometries to a rigid class.

The corresponding decisive negative test is now harder than in `WI-265`: construct a **source-compatible multi-component vector** whose prime translations are active in just the right places to cancel the monotone continuous convolution and which satisfies either Suzuki's actual null equation or the full lower-envelope family to established precision. Another abstract operator or another two-endpoint bump does not meet the gate.

The scalar lower-envelope route remains available independently. If one can show for every member of a broader screened class that

\[
\mathcal F_v(r)<r\lambda_r
\]

at some common radius, that also excludes the class. But `WI-266` shows that the pointwise null equation already contains strictly more discriminatory information than the sign-screened autocorrelation observables used in `WI-264`.

## Stress tests

Any proposed implication must survive the existing boundary results. `WI-257` rules out generic bounded-self-adjoint zero-mode regularity. `WI-263` rules out one-prime source-sign/Bochner arguments. `WI-264` shows that all finitely many active source atoms can be placed in one autocorrelation gap. `WI-265` shows that this geometry can coexist with an exact **abstract** first crossing. `WI-266`, however, proves that it cannot coexist with Suzuki's **actual** null equation.

Therefore the arithmetic operator must enter before any reduction that forgets the relative support geometry of `v`, its prime translates, and the strictly monotone regular kernel. Conversely, a proposed generalization of `WI-266` must not assume that every support gap is prime-translation-free: a multi-component vector can have translated mass inside the gap, and those discrete terms are the obvious cancellation mechanism that the next proof must control.

## Evidence boundary

`WI-266` proves only that the explicit `WI-264` antisymmetric two-endpoint family cannot be an actual localized Weil null vector. It does not prove that every null vector has nonzero autocorrelation at a prescribed prime-power lag, that arbitrary macroscopic support gaps are impossible, or that no multi-component source-compatible screen exists. It also does not establish a positive lower profile for `lambda_r` beyond the already certified finite-window inputs.

The exact null equation is available on Suzuki's `H_0^1` core through `B_a=D^*G_aD`, while a general ground-state vector in `D(A_a)` need not have that regularity. Any extension of the pointwise argument to arbitrary first-crossing modes must either prove enough regularity/approximation to justify the equation on the region used, or work distributionally/form-theoretically without inserting unjustified pointwise values.

## Research disposition

The clue remains `accepted`, but its live gate has advanced beyond endpoint screening. Do not spend further passes rebuilding the `WI-264` two-bump geometry, deriving coercivity from abstract nested positivity, or enlarging the aperture merely to activate more prime layers.

Attack the **source-specific propagation problem** exposed by `WI-266`: determine whether the monotone continuous kernel plus the exact finite von-Mangoldt translation graph forbids any macroscopic screened geometry compatible with a null mode. If a multi-component source-compatible countermodel survives the actual equation, persist that barrier and retarget toward a stronger invariant. If the null equation forces propagation, quantify it tightly enough to connect a hypothetical first crossing to a contradiction or an iterative defect-to-zero mechanism.