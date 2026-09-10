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
---

# Can a moment-cancelled low-frequency packet isolate a higher-order zeta arithmetic correction after universal quadratic cancellation?

## Observation

`VIS-141` forces any Rudnick–Sarnak-safe companion to a near-edge pair factor into a shrinking low-frequency band. `VIS-142`--`VIS-144` then identify the finite-CUE null-side cost: in the ultra-low-frequency regime the centered response is genuinely quadratic, and a signed packet with `integral q^2 dnu_b(q)=0` cancels its leading CUE term.

`VIS-145` closes the most optimistic interpretation of that cancellation. For any smooth finite-window correction entering through the same centered-cosine transform, the same packet also removes the quadratic source-specific response. The desired arithmetic residual, if present, must therefore survive at quartic-or-higher order, through nonuniform `L`-dependent moment growth, or through a genuinely different observable/information carrier.

`VIS-146` adds the missing normalization gate. For every signed packet supported in `|q|<=b`, `|m_(2j)|<=b^(2j)||nu_b||_TV`. Hence a second-moment-null packet normalized by `|m_4|=1` necessarily has `||nu_b||_TV>=b^-4`; a fixed two-scale packet attains this exponent, so it cannot be improved by a more clever bounded-complexity rescaling. More strongly, if the surviving quartic source term is `A_4 q^4` and the theorem/transfer uncertainty is known only by `||e||_infinity<=epsilon`, then the best robust signal-to-error ratio permitted by those envelopes is at most `|A_4|b^4/epsilon`. Packet rescaling multiplies signal and total-variation-linear error together and cannot improve that ratio.

Targeted prior-art orientation confirms that finite-height zeta pair-correlation models do contain source-specific arithmetic lower-order structure beyond the limiting CUE/GUE law. Conrey–Snaith derive lower-order `n`-correlation terms conditionally on the ratios conjecture, while Keating–Smith explicitly use asymptotically lower-order pair-correlation terms in a formal/heuristic Fourier inversion recovering prime-pair arithmetic. This makes an arithmetic carrier plausible, but neither result proves that the present shrinking support-safe packet retains it after the exact moment-null transform or that its coefficient beats the new `b^4` error gate.

## Research question

After expressing the strongest available finite-height **zeta-minus-finite-CUE** pair correction in the exact frozen bounded-window companion functional, what is the first nonzero term that survives a predeclared signed packet with

`integral q^2 dnu_(b_L)(q)=0`?

If that term is quartic, what is its exact coefficient `A_4(L)` and does

`epsilon_L/(|A_4(L)| b_L^4) -> 0`

hold for the strongest available theorem/transfer error envelope in the same coordinate and support regime? If not, no packet normalization can repair the deterministic deficit under total-variation control. If the ratio is favorable, does the same packet survive sixth-order Taylor remainder, stochastic variance, and cross-window covariance? A different observable remains admissible only if it carries source-specific information outside this common finite-window moment channel.

## Why it may matter

The previous formulation hoped that algebraic cancellation might remove the universal null without paying the scalar amplification cost of an ultra-low-frequency companion. `VIS-145` showed that the cancellation also removes every common quadratic source correction. `VIS-146` now shows that moving the signal to quartic order does not make normalization free: the shrinking support has only `O(b^4)` fourth-moment capacity per unit total variation, and any uncertainty controlled in the same norm scales with the weights in exactly the same way.

The remaining question is therefore sharper and largely normalization-independent. A useful quartic arithmetic carrier must be intrinsically strong enough, through `A_4(L)` or controlled nonuniform moment growth, to beat the per-mode error before packet tuning matters. A positive answer would justify studying packet shape and covariance; a negative answer would close the current moment-cancelled support-edge design without trying additional signed filters that cannot change the deterministic ratio.

## Decisive test

Do not inspect untouched confirmation-zero data. Freeze the source-window, unfolding, effective-size, diagonal-subtraction, edge-coordinate, support, packet-shape, and normalization conventions first.

1. Derive an exact or controlled representation of the finite-height zeta-minus-finite-CUE mean through the same companion variable `q`. Do not identify a spacing-domain arithmetic factor with the frequency-domain packet coefficient without carrying out the Fourier/window transform.
2. Expand that exact finite-window response through quartic order and identify `A_4(L)` after imposing `m_2=0`. Carry the sixth-order remainder with its actual `L`-dependent moment bound rather than only its formal power of `b_L`.
3. Put the strongest available restricted-support theorem/transfer remainder into a per-mode envelope `epsilon_L` in the same frozen coordinate. Before optimizing any packet, test the necessary robust gate from `VIS-146`: `epsilon_L/(|A_4(L)|b_L^4) -> 0` for asymptotically strong quartic separation. If the available error has additional sign, orthogonality, oscillation, or norm structure that beats total variation, prove and use that stronger structure explicitly.
4. Only if the deterministic gate survives, apply a fixed bounded-complexity `m_2=0` packet and propagate its exact total variation through stochastic variance and cross-window covariance. Packet rescaling is not evidence of improved separation.

Kill the current moment-null design if the quartic source coefficient vanishes, if its `L`-growth is too weak for the `b_L^4` support-capacity gate, if the sixth-order/nonuniform correction is uncontrolled at the required scale, or if stochastic/four-level error dominates after the deterministic gate passes.

Do not proceed to an `m_4=0` sixth-order packet merely to cancel another universal term unless the sixth-order source coefficient and error budget are already identified; `VIS-146` shows that unit sixth-moment normalization then costs at least `b_L^-6` in total variation.

## Evidence boundary

`VIS-144` establishes the finite-CUE quadratic response and signed second-moment cancellation. `VIS-145` establishes the generic quadratic obstruction for every smooth finite-window correction in the same centered-cosine representation. `VIS-146` establishes the support-moment capacity bound, the explicit quartic expansion after `m_2=0`, and the normalization-invariant minimax gate for errors controlled only through total variation.

The cited finite-height zeta pair-correlation literature supplies conditional/heuristic evidence that arithmetic lower-order terms exist in broader formulas; it does **not** establish the exact `A_4(L)`, the required support-uniform transform, the theorem/transfer error `epsilon_L`, the covariance law, or post-cancellation detectability. Nothing currently proves that a quartic arithmetic coefficient survives strongly enough, that the deterministic gate is favorable, or that the necessary restricted-support family is uniform. No RH implication or confirmation-zero evidence is claimed.

## Research disposition

Accepted in further narrowed form. The next work is no longer packet design. First identify the actual quartic-or-higher zeta-minus-CUE coefficient and compare it with the same-coordinate theorem/transfer error at the structural `b_L^(2j)` support-capacity scale. Only a favorable deterministic ratio justifies returning to signed packet shape, variance, or covariance. If the ratio is not favorable and no stronger error structure is available, reject the moment-cancelled companion rather than opening additional filter variants.