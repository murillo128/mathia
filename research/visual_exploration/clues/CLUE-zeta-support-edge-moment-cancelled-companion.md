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
---

# Can a moment-cancelled low-frequency packet isolate a higher-order zeta arithmetic correction after universal quadratic cancellation?

## Observation

`VIS-141` forces any Rudnick--Sarnak-safe companion to a near-edge pair factor into a shrinking low-frequency band. `VIS-142`--`VIS-144` then identify the finite-CUE null-side cost: in the ultra-low-frequency regime the centered response is quadratic, and a signed packet with `integral q^2 dnu_b(q)=0` cancels its leading CUE term.

`VIS-145` closes quadratic selectivity: the same moment-null packet removes the quadratic response of every smooth finite-window source correction entering through the same centered-cosine transform. `VIS-146` then shows that moving the signal to quartic order does not make normalization free. A quartic-normalized packet on `|q|<=b` costs at least `b^-4` in total variation, and a source term `A_4 q^4` cannot robustly beat a per-mode `L^infinity` error `epsilon` unless the intrinsic ratio `|A_4|b^4/epsilon` is favorable.

`VIS-147` removes the next shortcut. The standard finite-height Riemann-zero two-point expansion through the displayed `rho_bar^-3` term is already absorbed, at fixed spacing, by the classical effective-CUE matrix-size correction plus a small coordinate stretch. Those terms therefore cannot be reused as a post-null arithmetic `A_4(L)`. More importantly, the remaining `O(rho_bar^-4)` statement is a fixed-spacing asymptotic, while the coefficient required by `VIS-146` is the fourth spatial moment of the zeta-minus-calibrated-finite-CUE residual over the `VIS-130` source window `M_L=Theta(L)`. Pointwise asymptotics do not control that growing-window moment.

The source problem is now sharply localized: derive a post-calibration residual in the exact bounded-source representation with enough uniformity, cancellation, or norm structure to control its fourth moment and its transfer error on the same growing window.

## Research question

Let `H_L(x)` be the actual zeta-minus-calibrated-finite-CUE correction after freezing the `VIS-130` bounded source taper, Montgomery weight, local unfolding, diagonal convention, effective-size rule, and any source-derived coordinate stretch. Can one derive, from the strongest available finite-height pair-correlation formula or theorem, an asymptotic or controlled representation strong enough to determine

`mu_4(H_L)=integral x^4 H_L(x) dx`

on the full `M_L=Theta(L)` source window?

With

`A_4(L)=-(2/3) pi^4 mu_4(H_L)`,

can the same source-side argument provide a theorem/transfer error `epsilon_L` in the companion coordinate for which

`epsilon_L/(|A_4(L)| b_L^4) -> 0`

under one Rudnick--Sarnak-admissible shrinking-band regime? If the fourth moment is killed or not controllable, does the source formula expose a genuinely different information carrier rather than another rescaling of the same moment channel?

## Why it may matter

The route no longer has a packet-design ambiguity that can plausibly be solved by tuning weights. `VIS-145` and `VIS-146` show that the decisive issue is the source-side amplitude and error before packet optimization. `VIS-147` further shows that the familiar low-order zeta/CUE correction formulas do not directly supply that amplitude: their first displayed terms are calibration directions, and their residual estimate lacks the weighted growing-window uniformity the quartic companion needs.

A positive result would identify an arithmetic carrier that survives all currently known null and normalization obstructions in one common representation. A negative result would close the moment-cancelled support-edge route for a precise reason — insufficient post-calibration information/control — without inspecting confirmation zeros or proliferating signed filters.

## Decisive test

Do not inspect untouched confirmation-zero data and do not design another packet yet. Freeze the source window, unfolding, effective-size rule, coordinate stretch, diagonal subtraction, Montgomery weight, edge coordinate, and shrinking support family first.

Start from a finite-height pair-correlation source that retains the arithmetic lower-order structure, such as the full diagonal/off-diagonal representation reviewed by Keating--Smith or a stronger rigorous substitute if available. Transport it into the exact `VIS-130` bounded-source coordinate **before** subtracting the calibrated finite-CUE null. The size correction and source-derived scale stretch identified by the classical Forrester--Mays matching must be treated as null/calibration directions rather than counted again as source residual.

Then establish a weighted statement strong enough for the actual fourth moment. A fixed-`x` expansion with an `O(L^-4)` remainder is insufficient. Control the residual on `|x|<=M_L=Theta(L)` in a norm, oscillatory representation, or cancellation estimate that legitimately bounds `integral x^4 H_L(x) dx` and the sixth-order remainder needed by `VIS-146`.

Only after `A_4(L)` is identified should the same-coordinate theorem/transfer error be compared with `|A_4(L)|b_L^4`. If the deterministic ratio fails, or if no justified growing-window control exists and no stronger error structure replaces total variation, reject the current moment-null companion. Only a favorable deterministic gate justifies returning to packet variance and four-level covariance.

## Evidence boundary

`VIS-141`--`VIS-146` establish the support collapse, finite-window low-frequency expansion, universal quadratic cancellation, and total-variation moment-capacity gate. `VIS-147` establishes only an identifiability and uniformity obstruction: the displayed standard `rho_bar^-2`/`rho_bar^-3` corrections are effective-CUE calibration directions at fixed spacing, and the remaining fixed-spacing error does not determine the growing-window quartic moment.

The full finite-height pair-correlation literature contains arithmetic lower-order information, but it is heuristic/conditional in important forms and has not yet been transported into the exact frozen bounded-source companion with the required uniform error. Nothing currently proves that a detectable quartic arithmetic coefficient survives, that the `VIS-146` ratio is favorable, or that the necessary Rudnick--Sarnak family is uniform. No RH implication or confirmation-zero evidence is claimed.

## Research disposition

Accepted in further narrowed form. The next work is a source-to-observable transfer problem: derive and control the post-calibration zeta-minus-finite-CUE residual on the full growing source window, then compute its fourth moment and compare the resulting `A_4(L)b_L^4` scale with the theorem/transfer error. Do not spend another invocation on packet shape unless that deterministic gate first survives.