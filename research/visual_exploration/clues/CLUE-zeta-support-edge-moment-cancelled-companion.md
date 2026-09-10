---
id: CLUE-visual-exploration-zeta-support-edge-moment-cancelled-companion
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-141-rudnick-sarnak-edge-companion-bandwidth-collapse.md
  - research/visual_exploration/findings/VIS-142-low-frequency-cue-companion-linear-centered-amplitude.md
  - research/visual_exploration/findings/VIS-143-low-frequency-cue-companion-finite-window-quadratic-regime.md
  - research/visual_exploration/findings/VIS-144-low-frequency-cue-companion-two-sided-quadratic-response.md
  - research/visual_exploration/findings/VIS-145-second-moment-packet-cancels-all-finite-window-quadratic-responses.md
  - research/visual_exploration/findings/VIS-146-shrinking-moment-null-total-variation-error-gate.md
  - research/visual_exploration/findings/VIS-147-effective-cue-calibration-growing-window-quartic-gate.md
  - research/visual_exploration/findings/VIS-148-growing-window-primitive-cancellation-transfer-gate.md
  - research/visual_exploration/findings/VIS-149-moment-null-packet-source-error-fourth-moment-gate.md
---

# Can a moment-cancelled low-frequency packet isolate a higher-order zeta arithmetic correction after universal quadratic cancellation?

## Observation

`VIS-141` forces any Rudnick--Sarnak-safe companion to a near-edge pair factor into a shrinking low-frequency band. `VIS-142`--`VIS-144` identify the finite-CUE null-side cost: in the ultra-low-frequency regime the centered response is quadratic, and a signed packet with `m_2(nu_b)=0` cancels its leading CUE term.

`VIS-145` closes naive quadratic selectivity because that same packet removes the quadratic response of every smooth finite-window source correction entering through the common centered-cosine transform. `VIS-146` then shows that moving the retained signal to quartic order is not normalization-free: a quartic packet has `b^-4` total-variation capacity cost, and generic already-transformed `L^infinity` uncertainty cannot be beaten by scalar rescaling.

`VIS-147` removes the familiar fixed-spacing shortcut. The displayed standard `rho_bar^-2` and `rho_bar^-3` Riemann-zero corrections are already effective-CUE size/scale calibration directions, while the remaining fixed-spacing asymptotic does not control the fourth weighted source moment over the `VIS-130` growing window `M_L=Theta(L)`.

`VIS-148` supplies one concrete escape: sufficiently controlled repeated primitives of a source-coordinate transfer error turn cumulative cancellation into powers of the shrinking companion bandwidth. But `VIS-149` shows that this certificate is stronger than the frozen packeted observable actually requires. For an error `E_L` represented before the same centered-cosine transform, the zeroth Taylor coefficient is absent, odd source components are killed by the even cosine kernel, and the packet's own `m_2=0` condition removes the complete quadratic error response. The first source-error coefficient that survives packet integration is therefore `mu_4(E_L)`, with sixth-order remainder controlled by `M_6(E_L)b_L^2` after dividing by the quartic signal, up to the bounded packet condition number.

The next source test should therefore use the weakest representation-faithful gate first: compare the fourth weighted moment of the post-calibration transfer error directly to the fourth moment of the retained carrier, and control the sixth absolute moment on the growing window. Repeated primitives remain an alternative when they are what the source naturally provides or when direct weighted-moment control is too weak.

## Research question

Let `H_L(x)` be the actual zeta-minus-calibrated-finite-CUE correction after freezing the `VIS-130` bounded source taper, Montgomery weight, local unfolding, diagonal convention, effective-size rule, source-derived coordinate stretch, edge coordinate, and shrinking packet family. Can one derive from the strongest available finite-height pair-correlation representation a decomposition

`H_L = H_L^main + E_L`

on the full `M_L=Theta(L)` source window such that `H_L^main` has a genuinely post-calibration nonzero fourth moment and controlled higher-order remainder, while the source-coordinate error satisfies the transform-adapted gates

`|mu_4(E_L)|/|mu_4(H_L^main)| -> 0`

and, for a bounded-condition quartic packet,

`M_6(E_L)b_L^2/|mu_4(H_L^main)| -> 0`?

Here `mu_4(F)=integral x^4F(x)dx`, `M_6(F)=integral |x|^6|F(x)|dx`, and the packet condition number is

`kappa_(b,L)=b_L^4 ||nu_(b,L)||_TV / |m_4(nu_(b,L))| >= 1`.

If direct weighted-moment control cannot be justified, does the finite-height source instead provide a repeated-primitive, oscillatory, orthogonality, or other certificate strong enough to imply the same packet-level error ratio? With

`A_4(L)=-(2/3)pi^4 mu_4(H_L^main)`,

the final deterministic requirement remains that all theorem/transfer uncertainty after the frozen packet be `o(|A_4(L)m_4(nu_(b,L))|)` in one Rudnick--Sarnak-admissible shrinking-band regime.

## Why it may matter

The route no longer has a plausible packet-design ambiguity. The decisive question is whether the finite-height arithmetic source survives effective-CUE calibration with enough controlled fourth-moment mass on the actual growing source window.

`VIS-149` materially lowers the admission burden compared with interpreting `VIS-148` as a requirement for four or five raw vanishing moments. The frozen observable itself already quotients several directions. A positive result therefore need not prove an unnecessarily strong primitive theorem if it can directly show that the transfer-error fourth moment is negligible and its sixth absolute moment is compatible with the shrinking bandwidth. Conversely, failure of this weaker gate would be stronger evidence that the quartic companion is blocked by missing source information rather than by an overly demanding sufficient certificate.

A favorable deterministic gate would identify a post-calibration arithmetic carrier that survives all current mean-level nulls in one common representation. Only then would packet variance and four-level covariance become meaningful. An unfavorable gate should close the moment-cancelled support-edge route without inspecting untouched confirmation-zero data or proliferating further signed filters.

## Decisive test

Do not inspect untouched confirmation-zero data and do not design another packet. Freeze the bounded source window, unfolding, effective-CUE size rule, source-derived stretch, diagonal subtraction, Montgomery weight, edge coordinate, and one bounded-condition `m_2=0`, `m_4!=0` shrinking packet family first.

Start from a finite-height pair-correlation source retaining the arithmetic lower-order structure, such as the full diagonal/off-diagonal representation reviewed by Keating--Smith or a stronger rigorous substitute if available. Transport it into the exact `VIS-130` bounded-source coordinate before subtracting the calibrated finite-CUE null. Treat the size and stretch terms identified by Forrester--Mays as calibration directions, not as residual signal.

Then isolate a candidate `H_L^main` and the residual `E_L` in that source coordinate. Before demanding repeated primitives, compute or bound the weighted quantities that the frozen packet actually sees. Use the exact `VIS-149` packet decomposition to test

`|mu_4(E_L)|/|mu_4(H_L^main)|`

and

`kappa_(b,L) M_6(E_L)b_L^2/|mu_4(H_L^main)|`.

Both must tend to zero, together with any additional theorem/transport error not representable as the same source kernel. If `mu_4(E_L)` vanishes exactly, the error begins at sixth order after packet integration; no separate vanishing conditions on `mu_0`, odd moments, or `mu_2` are needed for that packet-level conclusion.

Only when these direct weighted-moment gates cannot be established should the source audit escalate to the `VIS-148` primitive hierarchy or an equivalent oscillatory/orthogonality estimate. A primitive certificate is useful if it actually yields a stronger growing-window bound; it is not an independent requirement once the weaker observable-adapted gate already passes.

Reject the current companion if the post-calibration main fourth moment cannot be isolated, if the error fourth moment remains comparable to it, if the sixth absolute moment erases the `b_L^2` gain, or if the source-to-observable transport has an uncontrolled remainder outside this common-kernel representation. Only a favorable deterministic gate justifies returning to stochastic variance and four-level covariance.

## Evidence boundary

`VIS-141`--`VIS-146` establish the support collapse, finite-window low-frequency expansion, universal packet-side quadratic cancellation, and total-variation moment-capacity gate. `VIS-147` establishes an identifiability and growing-window uniformity obstruction for the familiar finite-height expansion. `VIS-148` establishes a valid sufficient primitive/cumulative-cancellation certificate but does not show that the zeta residual satisfies it.

`VIS-149` is an exact representation audit of the already frozen packet architecture. It proves that when the transfer error is genuinely represented in the same pre-transform bounded source coordinate, the packeted mean first sees its fourth source moment and admits an explicit sixth-moment remainder bound. It does not derive `mu_4(E_L)`, `M_6(E_L)`, `mu_4(H_L^main)`, or any favorable asymptotic from the finite-height zeta source.

The finite-height pair-correlation literature contains arithmetic lower-order information, but the needed decomposition has not yet been transported with theorem-level control into this exact bounded-window, calibrated, packeted representation. Nothing currently proves that a detectable quartic arithmetic coefficient survives, that the transform-adapted ratios tend to zero, or that the remaining Rudnick--Sarnak and covariance requirements can be met. No RH implication or confirmation-zero evidence is claimed.

## Research disposition

Accepted in a weaker and more representation-faithful form. The next work is a source-to-observable weighted-moment test. Transport the calibrated finite-height residual into the `VIS-130` bounded source representation, isolate any genuine quartic main carrier, and test the `VIS-149` fourth-moment and sixth-absolute-moment ratios before demanding repeated primitives. Use `VIS-148` only as a stronger alternative certificate when the source naturally supplies cumulative cancellation or direct weighted-moment control is insufficient.