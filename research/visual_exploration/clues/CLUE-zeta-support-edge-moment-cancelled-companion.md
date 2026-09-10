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
---

# Can a moment-cancelled low-frequency packet isolate a higher-order zeta arithmetic correction after universal quadratic cancellation?

## Observation

`VIS-141` forces any Rudnick--Sarnak-safe companion to a near-edge pair factor into a shrinking low-frequency band. `VIS-142`--`VIS-144` then identify the finite-CUE null-side cost: in the ultra-low-frequency regime the centered response is quadratic, and a signed packet with `integral q^2 dnu_b(q)=0` cancels its leading CUE term.

`VIS-145` closes quadratic selectivity: the same moment-null packet removes the quadratic response of every smooth finite-window source correction entering through the same centered-cosine transform. `VIS-146` then shows that moving the signal to quartic order does not make normalization free. A quartic-normalized packet on `|q|<=b` costs at least `b^-4` in total variation, and a source term `A_4 q^4` cannot robustly beat a per-mode `L^infinity` error `epsilon` unless the intrinsic ratio `|A_4|b^4/epsilon` is favorable.

`VIS-147` removes the next shortcut. The standard finite-height Riemann-zero two-point expansion through the displayed `rho_bar^-3` term is already absorbed, at fixed spacing, by the classical effective-CUE matrix-size correction plus a small coordinate stretch. Those terms therefore cannot be reused as a post-null arithmetic `A_4(L)`. More importantly, the remaining `O(rho_bar^-4)` statement is a fixed-spacing asymptotic, while the coefficient required by `VIS-146` is the fourth spatial moment of the zeta-minus-calibrated-finite-CUE residual over the `VIS-130` source window `M_L=Theta(L)`. Pointwise asymptotics do not control that growing-window moment.

`VIS-148` identifies a concrete escape from that nonuniformity obstruction without weakening the deterministic gate. If the post-calibration source-transfer error has a `k`-fold primitive with vanishing endpoint traces on the bounded `VIS-130` source window, repeated integration by parts gives a low-frequency error `O(b_L^k ||G_(k,L)||_1)`. The same certificate reduces the growing-window loss in the fourth spatial moment by one power of `M_L` per primitive; for `k>=5` the transfer error's quartic moment vanishes exactly. Thus the next source question is no longer merely "find a stronger norm": test whether the finite-height source carries four or more exact cumulative cancellations, or an equivalent oscillatory/orthogonality certificate, after the frozen finite-CUE calibration directions are removed.

## Research question

Let `H_L(x)` be the actual zeta-minus-calibrated-finite-CUE correction after freezing the `VIS-130` bounded source taper, Montgomery weight, local unfolding, diagonal convention, effective-size rule, and any source-derived coordinate stretch. Can one derive, from the strongest available finite-height pair-correlation formula or theorem, a decomposition

`H_L = H_L^main + E_L`

on the full `M_L=Theta(L)` source window such that the main term has a genuinely post-calibration quartic moment

`mu_4(H_L^main)=integral x^4 H_L^main(x) dx`

with a controlled higher-order remainder, while `E_L` has four or more vanishing low moments together with a controlled compact-support primitive, or another source-side structure yielding an equivalent low-frequency gain?

With

`A_4(L)=-(2/3) pi^4 mu_4(H_L^main)`,

can the same source-side argument provide a theorem/transfer error `epsilon_L` in the companion coordinate for which

`epsilon_L/(|A_4(L)| b_L^4) -> 0`

under one Rudnick--Sarnak-admissible shrinking-band regime? For a primitive certificate, `VIS-148` makes this explicit: a `k`-primitive transfer error contributes at most order `b_L^k ||G_(k,L)||_1`, so `k=4` must win through the norm ratio and `k>=5` can additionally gain a positive power of `b_L`.

## Why it may matter

The route no longer has a packet-design ambiguity that can plausibly be solved by tuning weights. `VIS-145` and `VIS-146` show that the decisive issue is the source-side amplitude and error before packet optimization. `VIS-147` further shows that the familiar low-order zeta/CUE correction formulas do not directly supply that amplitude: their first displayed terms are calibration directions, and their residual estimate lacks the weighted growing-window uniformity the quartic companion needs.

`VIS-148` turns the previously vague possibility of "cancellation or a stronger norm" into a finite hierarchy that can be checked against the actual finite-height representation. This matters because a positive source theorem need not prove an implausibly strong uniform `O(L^-6)`-type pointwise residual if it instead preserves enough exact cumulative cancellation. Conversely, failure to obtain even the fourth-primitive-scale certificate, or an equivalent oscillatory estimate, would make the negative conclusion substantially sharper.

A positive result would identify an arithmetic carrier that survives all currently known null and normalization obstructions in one common representation. A negative result would close the moment-cancelled support-edge route for a precise reason — insufficient post-calibration information/control — without inspecting confirmation zeros or proliferating signed filters.

## Decisive test

Do not inspect untouched confirmation-zero data and do not design another packet yet. Freeze the source window, unfolding, effective-size rule, coordinate stretch, diagonal subtraction, Montgomery weight, edge coordinate, and shrinking support family first.

Start from a finite-height pair-correlation source that retains the arithmetic lower-order structure, such as the full diagonal/off-diagonal representation reviewed by Keating--Smith or a stronger rigorous substitute if available. Transport it into the exact `VIS-130` bounded-source coordinate **before** subtracting the calibrated finite-CUE null. The size correction and source-derived scale stretch identified by the classical Forrester--Mays matching must be treated as null/calibration directions rather than counted again as source residual.

Then test the source residual in this order. First isolate any candidate `H_L^main` that contributes a post-calibration fourth moment and control the sixth-order or exact-transform remainder required by `VIS-146`. Second, write the remaining transfer error `E_L` on the same bounded source interval and test its low algebraic moments. If four or more vanish, construct the canonical repeated primitive and bound its `L^1` or another useful norm; if they do not vanish, determine whether the source supplies a different exact oscillatory/orthogonality estimate with an equally explicit low-frequency power.

For a `k`-primitive certificate compare the actual quantity

`(2*pi)^k ||G_(k,L)||_1 b_L^(k-4) / |A_4(L)|`

to zero, together with every other theorem/transfer error in the same coordinate. A fourth-primitive certificate only matches quartic order and therefore still needs a favorable norm ratio. A fifth-or-higher certificate removes quartic contamination from that error and gains shrinking-band power, but it is useful only if its primitive norm does not grow fast enough to erase that gain.

If the deterministic ratio fails, if the main-term sixth-order remainder cannot be controlled, or if no justified growing-window cancellation/transfer structure exists, reject the current moment-null companion. Only a favorable deterministic gate justifies returning to packet variance and four-level covariance.

## Evidence boundary

`VIS-141`--`VIS-146` establish the support collapse, finite-window low-frequency expansion, universal quadratic cancellation, and total-variation moment-capacity gate. `VIS-147` establishes only an identifiability and uniformity obstruction: the displayed standard `rho_bar^-2`/`rho_bar^-3` corrections are effective-CUE calibration directions at fixed spacing, and the remaining fixed-spacing error does not determine the growing-window quartic moment.

`VIS-148` is an exact classical-analysis transfer lemma, not evidence that the zeta residual satisfies its hypotheses. It proves what a `k`-primitive cancellation certificate would buy: a `b_L^k` low-frequency error factor and a graded reduction of quartic-moment window growth. It does not derive those cancellations from the Keating--Smith/finite-height source, identify `A_4(L)`, or control the retained carrier's absolute sixth moment.

The full finite-height pair-correlation literature contains arithmetic lower-order information, but it is heuristic/conditional in important forms and has not yet been transported into the exact frozen bounded-source companion with the required uniform or cumulative-cancellation error. Nothing currently proves that a detectable quartic arithmetic coefficient survives, that the `VIS-146` ratio is favorable, or that the necessary Rudnick--Sarnak family is uniform. No RH implication or confirmation-zero evidence is claimed.

## Research disposition

Accepted in further narrowed form. The next work is a source-to-observable cancellation test, not another packet-design pass: transport the post-calibration finite-height residual into the `VIS-130` bounded source representation, isolate any genuine quartic main carrier, and test whether the remaining transfer error has four or more exact vanishing moments with controlled repeated primitives, or an equivalent oscillatory certificate. Only after that deterministic source gate survives should packet variance and four-level covariance resume.