---
id: CLUE-visual-wang-phase-anchored-small-values
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-416-wang-bandwidth-normalized-balance-radius.md
  - research/visual_exploration/findings/VIS-417-beat-scale-defeats-coarse-amplitude-controls.md
  - research/visual_exploration/findings/VIS-418-time-translation-defeats-fixed-height-small-value-controls.md
---

# Do distinguished arithmetic heights align with Wang quiet regions beyond the shell's own translation orbit?

## Observation

`VIS-416` isolates the bandwidth-normalized amplitude `a_i(T)=|F_i(T)|/||F_i||_infinity` as the candidate source-sensitive factor after removing the generic reciprocal-bandwidth scale. `VIS-417` shows that long finite-window suppression can still be manufactured by an unresolved beat scale even when mode count, coefficient magnitudes, long-time energy, bandlimit, and global sup norm are fixed.

`VIS-418` strengthens that control. Even after the complete two-mode frequency set and its beat gap are fixed, global translation can move an arbitrarily long quiet interval onto or away from any prescribed observation height while preserving the full frequency geometry, coefficient magnitudes, long-time energy, and sup norm. Fixed-height localization therefore contains a phase/time-origin alignment component that ordinary spectral matching does not remove.

## Research question

For canonical finite Wang shells, do pre-specified distinguished arithmetic heights exhibit unusually small normalized amplitudes or unusually persistent local quiet regions **relative to the translation orbit of the same shell**, after bandwidth normalization and without scanning the shift to favor the observed source?

Equivalently: is there a source-dependent phase anchoring that places arithmetic heights closer to shell zero geometry than would be expected from the shell's own translated waveform, rather than merely from its bandwidth, beat scales, or frequency support?

## Why it may matter

This isolates a substantially cleaner source question than comparing raw balance radii against loosely matched random sums. A translation-orbit baseline preserves the shell's exact frequencies, coefficient magnitudes, beat gaps, and internal spectral crowding. What it changes is only alignment between that fixed waveform and the distinguished height.

A positive effect would still not prove an RH mechanism, but it would identify a genuinely source-sensitive alignment channel that survives the generic band-limited and beating obstructions already established. A null result would close another visually attractive route without confusing spectral geometry with arithmetic phase anchoring.

## Decisive test

Choose the arithmetic height panel, shell family, amplitude/persistence statistic, and translation-window rule before inspecting the comparison values. For each shell `F_i`, keep its realized frequency set and coefficients fixed and compare the canonical value at the pre-specified height `T` with the same statistic for translated functions `F_i(.-s)` over a pre-specified shift ensemble.

The shift ensemble must be calibrated to the actual shell geometry. For periodic/commensurate shells, use the full translation period or an exactly equivalent phase average. For non-periodic or quasiperiodic finite sums, either prove an appropriate long-interval/Kronecker equidistribution calibration for the chosen observable or keep the result explicitly finite-window and test stability as the translation window grows. Do not replace the one-dimensional translation orbit by independent random phases unless a theorem shows that the larger phase-torus null is equivalent for the statistic being used.

Apply the same bandwidth normalization from `VIS-416`, and include persistence only after the beat-scale controls from `VIS-417` are respected. Kill the direction if the canonical heights are typical under their own translation orbit, if any apparent excess vanishes under pre-registered window growth, or if the effect can be recreated solely by selecting favorable heights/shifts after inspection.

## Evidence boundary

The cited findings establish only control requirements. They do not show that canonical Wang heights have anomalous phase alignment, do not provide the translation-orbit distribution for the actual shells, and do not establish a source-specific small-value law.

This clue proposes a matched self-null that preserves substantially more spectral structure than previous coarse controls. Its calibration, confirmation protocol, and any arithmetic excess remain unproved.