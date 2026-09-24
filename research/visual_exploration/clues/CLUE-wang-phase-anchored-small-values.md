---
id: CLUE-visual-wang-phase-anchored-small-values
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-416-wang-bandwidth-normalized-balance-radius.md
  - research/visual_exploration/findings/VIS-417-beat-scale-defeats-coarse-amplitude-controls.md
  - research/visual_exploration/findings/VIS-418-time-translation-defeats-fixed-height-small-value-controls.md
  - research/visual_exploration/findings/VIS-419-wang-shell-translation-orbit-prime-torus-haar.md
---

# Do distinguished arithmetic heights align with Wang quiet regions beyond the shell's own translation orbit?

## Observation

`VIS-416` isolates the bandwidth-normalized amplitude `a_i(T)=|F_i(T)|/||F_i||_infinity` as the candidate source-sensitive factor after removing the generic reciprocal-bandwidth scale. `VIS-417` shows that long finite-window suppression can still be manufactured by an unresolved beat scale even when mode count, coefficient magnitudes, long-time energy, bandlimit, and global sup norm are fixed.

`VIS-418` strengthens that control. Even after the complete two-mode frequency set and its beat gap are fixed, global translation can move an arbitrarily long quiet interval onto or away from any prescribed observation height while preserving the full frequency geometry, coefficient magnitudes, long-time energy, and sup norm. Fixed-height localization therefore contains a phase/time-origin alignment component that ordinary spectral matching does not remove.

`VIS-419` closes the fixed-shell calibration question: each canonical finite Wang shell is a finite character polynomial on its base-prime torus, and long translation of the actual shell is exactly the Haar pushforward of that same character polynomial. The valid Haar coordinates are base-prime phases; ratio-mode phases retain their induced character dependencies.

## Research question

For canonical finite Wang shells, do pre-specified distinguished arithmetic heights exhibit unusually small normalized amplitudes or unusually persistent local quiet regions **relative to the translation orbit of the same shell**, after bandwidth normalization and without scanning the shift to favor the observed source?

Equivalently: is there a source-dependent phase anchoring that places arithmetic heights closer to shell zero geometry than would be expected from the shell's own translated waveform, rather than merely from its bandwidth, beat scales, or frequency support?

## Why it may matter

This isolates a substantially cleaner source question than comparing raw balance radii against loosely matched random sums. A translation-orbit baseline preserves the shell's exact frequencies, coefficient magnitudes, beat gaps, internal spectral crowding, and all algebraic dependencies among ratio modes. What it changes is only alignment between that fixed waveform and the distinguished height.

A positive effect would still not prove an RH mechanism, but it would identify a genuinely source-sensitive alignment channel that survives the generic band-limited and beating obstructions already established. A null result would close another visually attractive route without confusing spectral geometry with arithmetic phase anchoring.

## Decisive test

Choose the arithmetic height panel, shell family, amplitude/persistence statistic, and any finite-window approximation rule before inspecting the comparison values. For each fixed shell `F_i`, use the exact base-prime Haar pushforward supplied by `VIS-419` as the asymptotic translation-orbit null. Equivalently, one may average the actual translated shell over a long shift interval, but independent randomization of ratio-mode phases is not an admissible substitute.

Apply the same bandwidth normalization from `VIS-416`. For persistence, pre-specify a fixed-radius continuous observable such as

`Q_(i,rho)(T)=sup_(|u|<=rho)|F_i(T+u)|/||F_i||_infinity`,

or another statistic with an explicitly justified continuity/tail calibration. If numerical finite-window translation is used instead of direct prime-torus Haar integration, pre-register the shift windows and test stability as they grow; `VIS-419` supplies no quantitative convergence rate.

Kill the direction if the distinguished arithmetic heights are typical under the exact fixed-shell self-null, if any apparent excess vanishes under pre-registered window growth, or if the effect can be recreated solely by selecting favorable heights/shifts after inspection. Any regime where shell support or scale grows with height requires a separate uniform quantitative equidistribution argument before a residual can be interpreted.

## Evidence boundary

`VIS-419` proves the asymptotic fixed-shell translation/Haar calibration and therefore removes the earlier ambiguity about the appropriate self-null. It does not show that any distinguished arithmetic height is anomalous, does not provide a finite-window convergence rate, and does not justify a jointly growing shell/height limit.

The source-specific small-value excess, if any, remains unproved. This clue is accepted because the remaining question is now precise, falsifiable, and separated from the generic bandwidth, beat-scale, and phase-null calibration obstructions.

## Research disposition

Accepted for continued investigation. The next substantive step is a pre-registered distinguished-height test against the exact fixed-shell prime-torus Haar self-null from `VIS-419`, with finite-window or growing-shell effects kept explicitly outside that theorem unless separately controlled.