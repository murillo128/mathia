# VIS-418 — Time translation defeats fixed-height small-value controls even with the full two-mode spectrum fixed

## Claim

For every integer `k>=1`, put `delta=1/(2k)` and reuse the exact beat family from `VIS-417`,

`F_delta(t)=1/2(cos t-cos((1-delta)t))`.

For every real shift `s`, define

`F_(delta,s)(t)=F_delta(t-s)`.

All functions in the translation orbit `{F_(delta,s): s in R}` have exactly the same frequency multiset `{1-delta,1}`, the same frequency gap `delta`, the same two coefficient magnitudes `1/2`, the same maximum frequency `1`, the same long-time mean energy `1/4`, and the same global supremum `1`.

Nevertheless, for every fixed observation height `T_0` and every `0<epsilon<1`, the fixed-height low-amplitude statistic can change from absent to arbitrarily persistent inside that same orbit. With `s=T_0`, the connected component through `T_0` of

`{t: |F_(delta,s)(t)|<=epsilon}`

has length at least `8 epsilon k`; with `s=T_0-2 pi k`, one has `|F_(delta,s)(T_0)|=1`, so `T_0` does not belong to the low-amplitude set at all.

Therefore even an exact match of the full two-mode frequency geometry, including the beat gap, does not determine **where** a long quiet window occurs. For fixed-height Wang small-value tests, phase/time-origin alignment is an additional control variable unless the statistic is explicitly translation-invariant or the canonical phase anchoring itself is the quantity being tested.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY FOURIER-TRANSLATION CONTROL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

## Exact translation orbit

Expanding the shift gives

`F_(delta,s)(t)=1/2 cos(t-s)-1/2 cos((1-delta)(t-s))`.

Thus translation changes only the phases of the two fixed modes. It does not change either frequency, their gap, or either coefficient magnitude.

Every translation-invariant norm or time-average used in `VIS-417` is unchanged. In particular,

`sup_t |F_(delta,s)(t)| = sup_t |F_delta(t)| = 1`,

and a change of variables gives the same long-time mean energy `1/4` for every `s`.

This is the finite-sum instance of the standard Fourier time-shift rule: translation multiplies each Fourier mode by a unit-modulus phase factor while preserving its frequency and coefficient magnitude.

## Quiet window can be placed at any chosen height

`VIS-417` factors the unshifted family as

`F_delta(u)=-sin((1-delta/2)u) sin(delta u/2)`

and proves

`|F_delta(u)| <= delta |u|/2`.

Set `u=t-s`. Then

`|F_(delta,s)(t)| <= delta |t-s|/2`.

Hence the entire interval

`|t-s| <= 2 epsilon/delta`

lies in `{|F_(delta,s)|<=epsilon}`. Its length is

`4 epsilon/delta = 8 epsilon k`.

Choosing `s=T_0` centers this certified quiet interval at the prescribed observation height `T_0`.

## The same orbit can make the same height maximally non-quiet

`VIS-417` also proves

`F_delta(2 pi k)=1`.

Choose instead

`s=T_0-2 pi k`.

Then `T_0-s=2 pi k`, so

`F_(delta,s)(T_0)=1`.

For every `0<epsilon<1`, the point `T_0` is outside the low-amplitude set. Thus a fixed-height statistic assigning zero when the observation point is not low-amplitude takes value `0` for this shift, while another member of the same exact spectral orbit has a connected quiet component of length at least `8 epsilon k` through the same `T_0`.

No frequency, gap, coefficient magnitude, long-time energy, or global-sup statistic distinguishes the two cases.

## Consequence for Wang matched controls

`VIS-416` showed that the raw local balance radius must first be bandwidth-normalized, leaving the dimensionless amplitude

`a_i(T)=|F_i(T)|/||F_i||_infinity`

as the candidate source-sensitive factor. `VIS-417` then showed that matching only coarse spectral/amplitude summaries is insufficient because a shrinking frequency gap can manufacture long finite-window suppression.

The present result closes the next obvious loophole: even after the **entire two-mode frequency set and its gap are held fixed**, a global translation moves the quiet region without changing those spectral data. Therefore a control for a statement about suppression at distinguished heights must specify how phase/time-origin alignment is treated.

There are two mathematically different questions:

1. whether a shell has long quiet regions somewhere, for which global translation is irrelevant but beat-scale geometry remains essential;
2. whether a distinguished arithmetic height lands unusually deep inside a quiet region, for which phase alignment relative to that height is itself part of the observable.

A null that randomizes or averages phase alignment cannot then interpret the resulting difference as a frequency-geometry effect. Conversely, if arithmetic phase anchoring is the intended signal, the null should test that anchoring explicitly rather than treating phase as disposable nuisance.

## Boundaries

This is not evidence that Wang's canonical shell phases are arithmetically anomalous. It proves only that fixed-height small-value localization is not determined by the spectral quantities controlled in `VIS-417`, even after the beat gap itself is fixed.

The construction uses a global translation orbit of one real two-mode function. Independent phase randomization of many modes is a larger operation and is not analyzed here.

The result also does not say that every useful Wang statistic must be phase-conditioned. A genuinely translation-invariant statistic, or a theorem reducing the source question to one, would evade this obstruction.

For actual Wang shells the observation height may be intrinsically distinguished by the arithmetic problem. In that case the correct conclusion is not to quotient it away, but to calibrate whether the canonical source places those heights atypically relative to a matched translation/phase baseline.

## Prior-art and novelty audit

No novelty is claimed for time translation of Fourier modes, phase factors, two-frequency beating, or the observation that a translated waveform moves its extrema and low-amplitude regions. The classical beat mechanism was already bounded as prior art in `VIS-417`.

For the standard Fourier translation rule, the Technical University of Munich LNTwww notes, *The Fourier Transform Theorems*, state that translating a signal `x(t-t_0)` multiplies its transform by the phase factor `exp(-j 2 pi f t_0)`: https://en.lntwww.lnt.ei.tum.de/Signal_Representation/The_Fourier_Transform_Theorems . The derivation above is elementary and does not depend on that source.

The durable Mathia content is the application-specific negative control: a fixed-height Wang small-value null remains under-specified after frequency-gap matching unless phase/time-origin alignment is also treated explicitly.

## Dependencies

- `VIS-416`: bandwidth-normalized Wang balance radius and normalized-amplitude candidate.
- `VIS-417`: exact beat family with fixed coarse statistics and arbitrarily long quiet component.

## Research consequence

The next discriminating test should separate **existence of quiet windows** from **alignment of quiet windows with distinguished arithmetic heights**. For the latter, compare the canonical normalized amplitudes against a pre-specified translation-orbit baseline of the same shell, or derive another phase-aware null that preserves the complete frequency geometry. Only a residual alignment effect beyond that baseline is eligible for source-sensitive interpretation.