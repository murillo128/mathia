---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-333-wang-summatory-log-frequency-transfer.md
  - research/visual_exploration/findings/VIS-334-wang-summatory-pointwise-inverse-derivative-tax.md
  - research/visual_exploration/findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md
  - research/visual_exploration/findings/VIS-340-wang-prime-squarelog-partial-summation-invertible.md
  - research/visual_exploration/findings/VIS-341-vk-scale-stable-under-finite-spectral-smoothing.md
  - research/visual_exploration/findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md
  - research/visual_exploration/findings/VIS-343-wang-dilate-mixture-cancellation-order.md
  - research/visual_exploration/findings/VIS-344-wang-translated-dilate-cancellation-fibers.md
  - research/visual_exploration/findings/VIS-345-long-window-phase-resolution.md
  - research/visual_exploration/findings/VIS-346-turan-nazarov-short-window-obstruction.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has been reduced to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333` gives Wang's exact nonvanishing multiplier `m(xi)=4(1+i xi)/(4+xi^2)`, while `VIS-334` shows that exact pointwise inversion pays one derivative. `VIS-339` and `VIS-340` show that the surviving prime source and the prime square-log summatory source are exact differential/integral images of the same `G`; repackaging primes into packets is therefore not an independent information channel.

The generic scalar smoothing escapes have also been narrowed. `VIS-341` shows that every fixed finite polynomial smoothing order preserves the Korobov–Vinogradov power class. `VIS-342` shows that a fixed positive gain in that class would require polynomially growing effective order. `VIS-343` converts that order into a scale-count cost for pure Wang dilates, and `VIS-344` shows that fixed translated copies cannot pool asymptotic moment cancellation across distinct phase fibers.

`VIS-345` closes moving windows once their lengths resolve the translation gaps. `VIS-346` removes most of the remaining fixed-bank short-window loophole: Turán–Nazarov propagation shows that, for a fixed bank with `B` phase fibers, `O(X^-r)` cancellation on windows of length `ell_X` still forces the same fiber moments through order `r-1` whenever

`X min(ell_X,1)^(B-1) -> infinity`.

Thus a power-law window `ell_X=X^-alpha` can escape this fixed-bank argument only at the coarse level `alpha>=1/(B-1)`, with the sharper induction threshold determined by the number of fibers active in each moment polynomial. This is a necessary escape scale, not evidence that such ultra-local cancellation exists.

## Research question

Does `G` possess a genuinely scale-dependent, adaptive, signed, or arithmetic localization that survives these fixed-bank obstructions and produces a pointwise smaller Wang output without paying the gain back through `Q'` or equivalent unsmoothed source information?

For translated/dilated packet mechanisms, can a family whose number of phases, phase spacing, scales, or coefficients changes with the source scale exploit windows at or below the `VIS-346` shrinking threshold while keeping coefficient conditioning and finite-frequency leakage controlled? Alternatively, can a frequency- or source-dependent construction use signed structure of `G` in a way that is not equivalent to making one scalar multiplier uniformly small on a window?

## Why it may matter

The fixed finite-bank route is now substantially classified. Neither bounded/subpolynomial scalar order, a small pure-dilation bank, fixed translations, phase-resolving moving windows, nor ordinary mildly shrinking windows can manufacture the required smoothing order without the already identified moment/scale costs.

A surviving mechanism would therefore have to use information that those scalar controls deliberately discard: scale-dependent phase geometry, adaptive coefficients, a growing/coalescing bank, or arithmetic sign structure of `G`. Such a result would be qualitatively different from another filter-tail cancellation and would identify a more credible place to search for leverage.

## Decisive test

Start from the exact source quotients in `VIS-339` and `VIS-340` and state the candidate directly as a quantitative property of `G`. If the mechanism is a fixed translated-dilate bank, apply `VIS-343`–`VIS-346` first. In particular, any claimed order-`r` cancellation on windows `J_X` must either satisfy the required fiber moment equations or operate in the genuinely unresolved regime where `X |J_X|^(B_X-1)` does not diverge after accounting for the active phase count.

For a scale-dependent bank, write explicitly the phase count `B_X`, minimum relevant spacing, window length, scale set, coefficient norm/conditioning, and asymptotic remainder constants. Derive an inequality showing that the claimed attenuation is not just Turán–Nazarov concentration purchased by a rapidly growing or nearly singular coefficient system. If coefficients depend on frequency or on `G`, state that dependence and prove the resulting estimate as a signed source statement rather than rebranding it as fixed-filter smoothing.

Any surviving gain must then be propagated through Wang's full destination. Identify every occurrence of `Q`, `Q'`, or equivalent unsmoothed information and show that the final bound retains the smaller scale rather than reconstructing the source through the derivative channel.

Kill the route if it reduces to the already-classified scalar truncation order, fixed-bank moment cancellation, windows above the `VIS-346` localization threshold, an ill-conditioned coefficient explosion, a restatement of a stronger theta/PNT remainder, or a destination term that pays back the derivative carrier.

## Evidence boundary

`VIS-333`–`VIS-346` are obstruction and transfer results. They do not prove a new bound or nonstationarity theorem for `G`, an improvement of the Korobov–Vinogradov remainder, or a destination-level avoidance of derivative repayment. `VIS-346` does not exclude ultra-shrinking windows at or below its Turán–Nazarov threshold, banks whose phase geometry changes with `X`, adaptive/frequency-dependent coefficients, infinite expansions, or arithmetic sign cancellation coupled directly to `G`.

The clue therefore remains `accepted`: the fixed-bank search space is sharply narrower, but a genuinely source-coupled localization mechanism remains unclassified.

## Research disposition

Outcome: **narrowed**.

Future work should treat "finite-window localization" as a quantitative claim, not a generic escape label. For a fixed bank, the remaining window must be microscopically small in the precise sense above. Otherwise the mechanism must expose and control a genuinely scale-dependent or source-dependent structure and still close the downstream derivative ledger.