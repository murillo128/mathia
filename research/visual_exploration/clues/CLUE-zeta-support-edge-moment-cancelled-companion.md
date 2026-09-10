---
id: CLUE-visual-exploration-zeta-support-edge-moment-cancelled-companion
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-141-rudnick-sarnak-edge-companion-bandwidth-collapse.md
  - research/visual_exploration/findings/VIS-142-low-frequency-cue-companion-linear-centered-amplitude.md
  - research/visual_exploration/findings/VIS-143-low-frequency-cue-companion-finite-window-quadratic-regime.md
  - research/visual_exploration/findings/VIS-144-low-frequency-cue-companion-two-sided-quadratic-response.md
---

# Can a signed low-frequency packet cancel the universal CUE quadratic mode while retaining a zeta arithmetic correction?

## Observation

`VIS-141` forces any Rudnick–Sarnak-safe companion to a near-edge pair factor into a shrinking low-frequency band. `VIS-142` and `VIS-143` show that bounded-normalization finite-CUE centered means vanish there, with an ultra-low-frequency upper scale `O(Mb^2)` once `Mb<<1`.

`VIS-144` sharpens that null geometry. For a single low-frequency mode under fixed capacity and bounded source-window aspect ratio, the finite-CUE centered mean is actually `Theta(Mb^2)`, so scalar amplification by `Theta(1/(Mb^2))` is the correct deterministic null-mean normalization scale. More importantly, the exact leading packet term is proportional to the signed second frequency moment `integral q^2 dnu_b(q)`. A signed packet can therefore impose this moment equal to zero and remove the full universal quadratic CUE mean term without widening its Fourier support.

## Research question

Does the finite-height zeta pair statistic have, in the same shrinking support-safe companion band, a lower-order arithmetic contribution whose low-frequency functional is not proportional to the universal CUE second-moment term?

Equivalently, can one choose a predeclared signed packet `nu_(b_L)` with `integral q^2 dnu_(b_L)(q)=0` such that the finite-CUE quadratic centered mean cancels but a source-specific zeta correction survives at a quantitatively detectable scale after the same packet is applied?

## Why it may matter

The current restricted-support escape looked forced into a bad scalar tradeoff: push the companion toward zero frequency, lose finite-CUE amplitude, then amplify by `1/b_L` or `1/(M_L b_L^2)` and magnify theorem, transfer, noise, and covariance errors at the same time.

Moment cancellation changes the shape of that design problem. It does not make the signal larger, but it may remove the leading universal null component algebraically rather than by scalar amplification. If the arithmetic correction has a different low-frequency expansion, a signed packet could act as a matched annihilator of the universal CUE term while preserving an arithmetic component. If the arithmetic term shares the same second-moment functional, the idea dies cleanly and the restricted-support route narrows further.

## Decisive test

Do not inspect untouched confirmation-zero data. Starting from the exact finite-height zeta pair-correlation formula or the strongest available smoothed explicit formula compatible with the frozen bounded-tent/Montgomery conventions, derive the low-frequency expansion of the **zeta-minus-finite-CUE** companion mean for a predeclared shrinking band `|q|<=b_L`.

Construct a simple bounded-complexity signed packet, for example a symmetric finite combination of two or three nonzero frequencies, whose total mass/normalization convention is fixed in advance and whose signed second moment is exactly zero. Propagate that packet through both the finite-CUE term and the zeta arithmetic lower-order term before taking asymptotics.

The route survives only if all of the following can be proved in one common `L`-dependent regime: the CUE quadratic term cancels as predicted by `VIS-144`; the first surviving zeta-specific term is nonzero under the same packet; its magnitude dominates the finite-height transfer/theorem remainder; and the packet total variation plus induced variance/cross-window covariance remain controlled enough that the arithmetic component is not erased by the normalization needed for detection.

Kill the route if the zeta-minus-CUE expansion is also proportional to the same second moment at the first relevant order, if moment cancellation forces total variation or higher moments to diverge too quickly, if the surviving term lies outside available support/uniformity, or if stochastic/four-level error dominates the residual arithmetic amplitude.

## Evidence boundary

The exact result currently established is only the finite-CUE null-side moment expansion in `VIS-144`. It proves that signed second-moment cancellation removes the leading quadratic centered CUE mean and that a single mode has genuine `Theta(Mb^2)` response in the ultra-low-frequency regime.

Nothing currently proves that zeta has a different low-frequency coefficient, that an arithmetic term survives the same annihilator, that a suitable packet has acceptable variance, or that Rudnick–Sarnak/finite-height errors are uniform for the resulting `L`-dependent signed family. The clue is therefore a redesign question, not evidence for an arithmetic residual or progress toward RH.