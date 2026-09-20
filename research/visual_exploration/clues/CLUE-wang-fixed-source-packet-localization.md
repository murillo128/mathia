---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-291-wang-fixed-power-korobov-vinogradov-envelope.md
  - research/visual_exploration/findings/VIS-292-wang-symmetric-smoothing-green-resolvent.md
  - research/visual_exploration/findings/VIS-329-direct-minkowski-decimation-closes-wang-transition.md
  - research/visual_exploration/findings/VIS-331-wang-subpower-envelope-mellin-strip-boundary.md
  - research/visual_exploration/findings/VIS-332-wang-regular-variation-secondary-transfer.md
  - research/visual_exploration/findings/VIS-333-wang-summatory-log-frequency-transfer.md
  - research/visual_exploration/findings/VIS-334-wang-summatory-pointwise-inverse-derivative-tax.md
  - research/visual_exploration/findings/VIS-335-wang-high-frequency-mode-derivative-repayment.md
  - research/visual_exploration/findings/VIS-336-wang-quadratic-chirp-derivative-repayment.md
  - research/visual_exploration/findings/VIS-337-wang-prime-power-jump-derivative-channel.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The generic filter question is now separated from the actual arithmetic burden. `VIS-333` gives the exact summatory log-frequency multiplier

`m(xi)=4(1+i xi)/(4+xi^2)`,

which has no real-frequency zero and attenuates high frequencies by only one order. `VIS-334` gives the exact causal inverse and shows that a smooth pointwise gain for both `Q` and `Q'` transfers back to the normalized source remainder. `VIS-335` and `VIS-336` prove that this derivative tax is sharp generically: a fixed high-frequency mode and a single increasing-frequency quadratic chirp can make `Q` small while leaving the missing source scale in `Q'`.

`VIS-337` now tests the most immediate arithmetic realization. For the actual normalized squared-von-Mangoldt remainder

`F(u)=e^(-u)E_A(e^u)`,

one has distributionally

`(1+D)F=mu-u du`,

where

`mu=sum Lambda(n)^2/n delta_(log n)`.

Every prime-power jump is copied exactly into Wang's derivative channel:

`Delta Q'(log n)=-4 Lambda(n)^2/n`.

But each such atom is at most `4u^2e^(-u)` in derivative amplitude, exponentially below the Korobov--Vinogradov-scale source envelope. The staircase's automatic fine-scale singularity is therefore not enough: any useful arithmetic frequency migration must be a **collective signed organization of many prime-power atoms**, not an isolated-jump effect.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`.

## Research question

Can one prove a genuinely collective, scale-migrating or nonstationary organization of the actual weighted prime-power source

`mu-u du`

that makes Wang's exact output

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

pointwise smaller than the current Korobov--Vinogradov-scale source envelope, with the missing scale carried by a collective derivative channel rather than by isolated prime-power jumps or by a hidden stronger estimate for `E_A` itself?

If so, does Wang's complete downstream error decomposition retain the smaller `Q` scale without requiring `Q'` or equivalent unsmoothed information at the larger source scale?

## Why it may matter

The remaining escape is now genuinely arithmetic rather than a generic smoothing phenomenon. High-frequency attenuation is structurally available, one derivative is its exact inverse price, and the actual source does populate that derivative channel at every prime power. However, the individual atoms are much too small to explain a gain at the current PNT envelope scale.

A positive result must therefore identify collective signed structure across many atoms. A negative result showing that every such collective realization is necessarily repaid in Wang's destination would close the remaining fixed-source transform route for a source-specific reason rather than by analogy with smooth controls.

## Decisive test

Start from the exact signed source measure `mu-u du`, not from an absolute envelope and not from another abstract chirp family. Identify a collective packet, phase, block, or multiscale statistic involving a growing set of prime-power atoms and prove that it produces source-envelope-scale nonstationary cancellation after the continuous baseline is removed. The mechanism must survive the exact constraints in `VIS-291`, `VIS-333`, `VIS-334`, and the isolated-jump control `VIS-337`.

Derive the resulting pointwise size of `Q` and compare it against the Korobov--Vinogradov-scale input. If a proposed gain is `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate still carries the Mellin/zero-free-half-plane cost isolated in `VIS-331`.

Then trace the same collective mechanism through Wang's complete destination. Explicitly identify every term depending on `Q`, `Q'`, or equivalent unsmoothed source information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Kill a candidate if it reduces to coherent regular variation, a fixed or bounded log-frequency band, a generic chirp, isolated prime-power discontinuities, an absolute-variation estimate that discards the signed baseline cancellation, a hidden stronger bound for `E_A`, or a downstream term that pays back the derivative carrier.

## Evidence boundary

`VIS-333`--`VIS-336` classify generic filter transfer and repayment. `VIS-337` proves only that actual prime-power atoms are copied into `Q'` and that each individual atom is exponentially below the live PNT envelope. It does **not** bound collective blocks of atoms, prove arithmetic frequency migration, improve the Korobov--Vinogradov remainder, or show that Wang's destination avoids derivative-sensitive information.

The clue therefore remains `accepted`.

## Research disposition

Outcome: **narrowed**.

The generic nonstationary escape is real, and the actual source does have exact derivative-channel singularities, but isolated singularities are now excluded as the scale-carrying mechanism. The live question is collective arithmetic organization plus destination-level repayment.