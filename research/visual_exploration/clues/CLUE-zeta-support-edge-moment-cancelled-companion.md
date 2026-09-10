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
---

# Can a moment-cancelled low-frequency packet isolate a higher-order zeta arithmetic correction after universal quadratic cancellation?

## Observation

`VIS-141` forces any Rudnick–Sarnak-safe companion to a near-edge pair factor into a shrinking low-frequency band. `VIS-142`--`VIS-144` then identify the finite-CUE null-side cost: in the ultra-low-frequency regime the centered response is genuinely quadratic, and a signed packet with `integral q^2 dnu_b(q)=0` cancels its leading CUE term.

`VIS-145` closes the most optimistic interpretation of that cancellation. For **any** signed finite-window correction kernel `H` entering through the same centered-cosine transform,

`Delta_H(q)=integral H(x)[1-cos(2*pi*q*x)]dx`,

the packet response satisfies

`|integral Delta_H dnu_b - 2*pi^2 mu_2(H) integral q^2 dnu_b|`
` <= (2/3)pi^4 M_4(H)b^4 ||nu_b||_TV`.

Thus second-moment cancellation is not CUE-selective: it removes the quadratic response of the zeta-minus-CUE correction as well whenever that correction has the same smooth finite-window representation. The desired arithmetic residual, if present, must survive at quartic-or-higher order, through nonuniform `L`-dependent moment growth, or through a genuinely different observable/information carrier.

Targeted prior-art orientation confirms that finite-height zeta pair-correlation models do contain source-specific arithmetic lower-order structure beyond the limiting CUE/GUE law. Conrey–Snaith derive lower-order `n`-correlation terms conditionally on the ratios conjecture, while Keating–Smith explicitly use asymptotically lower-order pair-correlation terms in a formal/heuristic Fourier inversion recovering prime-pair arithmetic. This makes an arithmetic carrier plausible, but neither result proves that the present shrinking support-safe packet retains it after the exact moment-null transform.

## Research question

After expressing the strongest available finite-height **zeta-minus-finite-CUE** pair correction in the exact frozen bounded-window companion functional, what is the first nonzero term that survives a predeclared signed packet with

`integral q^2 dnu_(b_L)(q)=0`?

Does a quartic-or-higher arithmetic coefficient, or a provably nonuniform `L`-dependent moment profile, remain large enough to dominate the theorem/transfer and stochastic error floors under the same shrinking support constraint? If not, is there a different support-safe asymmetric observable whose source-specific contribution is not annihilated by the same low-order moment projection?

## Why it may matter

The previous formulation hoped that CUE and zeta might simply have different quadratic coefficients, so a second-moment-null packet could remove the universal term while retaining the arithmetic one. `VIS-145` shows that this cannot happen within the same smooth finite-window centered-cosine representation: the packet projects every quadratic coefficient to zero.

That is a useful narrowing rather than a dead end. Known finite-height pair-correlation formulas indicate where arithmetic lower-order structure can enter, but the correct question is now whether that structure survives **after** the exact support-safe transform at a higher order and with favorable `L`-dependence. A positive answer would identify a genuinely discriminating companion; a negative answer would close the moment-cancellation escape without fitting confirmation zeros.

## Decisive test

Do not inspect untouched confirmation-zero data. Freeze the source-window, unfolding, effective-size, diagonal-subtraction, edge-coordinate, support, packet-shape, and normalization conventions first.

1. Derive an exact or controlled representation of the finite-height zeta-minus-finite-CUE mean through the same companion variable `q`. Do not identify the spacing-domain arithmetic factor in a pair-correlation formula with the frequency-domain packet coefficient without carrying out the Fourier/window transform.
2. Apply a fixed bounded-complexity signed packet with `m_2=integral q^2 dnu_(b_L)=0` **before** taking the shrinking-band asymptotic.
3. Compute or bound the first surviving term. Under a common smooth finite-window kernel this begins no earlier than the quartic remainder controlled by `VIS-145`; record its coefficient/moment growth in `L` rather than only its power of `b_L`.
4. Propagate the exact packet total variation and any normalization through the available restricted-support theorem remainder, finite-height zeta-to-null transfer error, stochastic variance, and cross-window covariance.

The route survives only if a source-specific post-cancellation term is nonzero and dominates all those error channels in one common `L`-dependent regime. Kill the current moment-null design if the first surviving arithmetic term is erased with the universal terms, if its required normalization amplifies errors to the same or larger scale, or if the needed uniform finite-height transform lies outside available support/control.

A different observable remains admissible only if its new information carrier is stated explicitly and does not merely rename the same finite-window centered-cosine functional.

## Evidence boundary

`VIS-144` establishes the finite-CUE quadratic response and its signed second-moment cancellation. `VIS-145` establishes the stronger generic obstruction: every smooth finite-window correction in the same centered-cosine representation loses its quadratic term under the same packet, with an explicit quartic remainder bound.

The cited finite-height zeta pair-correlation literature supplies conditional/heuristic evidence that arithmetic lower-order terms exist in broader formulas; it does **not** establish the exact `L`-dependent kernel, uniformity, covariance law, or post-cancellation amplitude needed here. Nothing currently proves that a quartic arithmetic coefficient survives, that it is detectable, or that the necessary restricted-support family is uniform. No RH implication or confirmation-zero evidence is claimed.

## Research disposition

Accepted in narrowed form. The quadratic-selectivity hypothesis is resolved negatively by `VIS-145`. Continued work should test only the remaining higher-order/nonuniform channel: derive the exact finite-height zeta-minus-CUE companion response, impose `m_2=0`, and determine the first surviving arithmetic term together with its full `L`-dependent error and covariance budget. If that term cannot beat the amplified error floor, reject the moment-cancelled companion rather than opening additional packet variants.