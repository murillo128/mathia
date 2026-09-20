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
  - research/visual_exploration/findings/VIS-338-proper-prime-power-tail-negligible.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The generic filter question is now separated from the actual arithmetic burden. `VIS-333` gives the exact summatory log-frequency multiplier

`m(xi)=4(1+i xi)/(4+xi^2)`,

which has no real-frequency zero and attenuates high frequencies by only one order. `VIS-334` gives the exact causal inverse and shows that a smooth pointwise gain for both `Q` and `Q'` transfers back to the normalized source remainder. `VIS-335` and `VIS-336` prove that this derivative tax is sharp generically: a fixed high-frequency mode and a single increasing-frequency quadratic chirp can make `Q` small while leaving the missing source scale in `Q'`.

`VIS-337` tests the most immediate arithmetic realization. For the actual normalized squared-von-Mangoldt remainder

`F(u)=e^(-u)E_A(e^u)`,

one has distributionally

`(1+D)F=mu-u du`,

where

`mu=sum Lambda(n)^2/n delta_(log n)`.

Every prime-power jump is copied exactly into Wang's derivative channel:

`Delta Q'(log n)=-4 Lambda(n)^2/n`.

Each individual atom is exponentially below the Korobov--Vinogradov-scale source envelope, so an isolated jump cannot carry the missing scale.

`VIS-338` now removes the next apparent escape. If `mu_pp` denotes all **proper** prime powers `p^k` with `k>=2`, then

`mu_pp([U,infinity))=O(U^2 e^(-U/2))`,

and its entire response through Wang's Green kernel, together with the one-sided derivative response and the total absolute far-tail jump mass, is on the same exponential scale. This is `o(exp(-c U^(3/5)(log U)^(-1/5)))` for every fixed positive `c`.

Thus the higher-prime-power branch is not merely small atom by atom: it is **collectively negligible at the live PNT envelope scale**. Any remaining source-envelope-scale mechanism must come from the `k=1` prime atoms and their signed organization against the continuous baseline, not from a generic packet of prime powers.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`.

## Research question

Can one prove a genuinely collective, scale-migrating or nonstationary organization of the actual weighted **prime** source

`mu_prime-u du`,

where

`mu_prime=sum_p (log p)^2/p delta_(log p)`,

that makes Wang's exact output

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

pointwise smaller than the current Korobov--Vinogradov-scale source envelope, with the missing scale carried by a collective derivative channel rather than by isolated jumps, proper-prime-power mass, or a hidden stronger estimate for `E_A` itself?

If so, does Wang's complete downstream error decomposition retain the smaller `Q` scale without requiring `Q'` or equivalent unsmoothed information at the larger source scale?

## Why it may matter

The remaining escape is now genuinely prime-specific rather than a generic smoothing or prime-power phenomenon. High-frequency attenuation is structurally available, one derivative is its exact inverse price, and the actual source does populate that derivative channel. But `VIS-337` excludes isolated atoms and `VIS-338` excludes the complete `k>=2` source at the relevant asymptotic scale.

A positive result must therefore identify collective signed structure in the prime atoms relative to the continuous baseline. A negative result showing that every such prime-only collective realization is necessarily repaid in Wang's destination would close the remaining fixed-source transform route for a source-specific reason rather than by analogy with smooth controls.

## Decisive test

Start from the exact decomposition

`mu-u du = (mu_prime-u du) + mu_pp`.

Use `VIS-338` as a hard control: any proposed envelope-scale mechanism must survive after the exponentially negligible `mu_pp` contribution is accounted for explicitly. Do not attribute scale-carrying power to a packet merely because it contains many higher prime powers.

On the surviving prime source `mu_prime-u du`, identify a collective packet, phase, block, or multiscale statistic involving a growing set of prime atoms and prove that it produces source-envelope-scale nonstationary cancellation after the continuous baseline is removed. The mechanism must survive the exact constraints in `VIS-291`, `VIS-333`, `VIS-334`, the isolated-jump control `VIS-337`, and the collective proper-power control `VIS-338`.

Derive the resulting pointwise size of `Q` and compare it against the Korobov--Vinogradov-scale input. If a proposed gain is `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate still carries the Mellin/zero-free-half-plane cost isolated in `VIS-331`.

Then trace the same collective mechanism through Wang's complete destination. Explicitly identify every term depending on `Q`, `Q'`, or equivalent unsmoothed source information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Kill a candidate if it reduces to coherent regular variation, a fixed or bounded log-frequency band, a generic chirp, isolated prime discontinuities, proper-prime-power mass, an absolute-variation estimate that discards the signed baseline cancellation, a hidden stronger bound for `E_A`, or a downstream term that pays back the derivative carrier.

## Evidence boundary

`VIS-333`--`VIS-336` classify generic filter transfer and repayment. `VIS-337` proves that actual prime-power atoms are copied into `Q'` and that each individual atom is exponentially below the live PNT envelope. `VIS-338` proves that the entire proper-prime-power (`k>=2`) source and its canonical Wang response are collectively exponentially below that envelope.

None of these results proves collective cancellation among the `k=1` prime atoms, arithmetic frequency migration, an improved Korobov--Vinogradov remainder, or destination-level avoidance of derivative-sensitive information. In particular, the subtraction of the continuous baseline remains essential; the clue cannot be reduced to a positive-mass estimate on `mu_prime`.

The clue therefore remains `accepted`.

## Research disposition

Outcome: **narrowed**.

The generic nonstationary escape is real, but the admissible arithmetic carrier has now narrowed twice: isolated atoms are too small, and all proper prime powers together are exponentially negligible. The live source question is specifically collective organization of the prime (`k=1`) atoms against the continuous baseline, followed by the existing destination-level repayment audit.