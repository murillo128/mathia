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
  - research/visual_exploration/findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md
  - research/visual_exploration/findings/VIS-340-wang-prime-squarelog-partial-summation-invertible.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The generic filter question is separated from the arithmetic burden. `VIS-333` gives the exact summatory log-frequency multiplier

`m(xi)=4(1+i xi)/(4+xi^2)`,

which has no real-frequency zero and attenuates high frequencies by only one order. `VIS-334` gives the exact causal inverse and shows that a smooth pointwise gain for both `Q` and `Q'` transfers back to the normalized source remainder. `VIS-335` and `VIS-336` show that this derivative tax is sharp generically: fixed high-frequency modes and an increasing-frequency chirp can make `Q` small while leaving the missing source scale in `Q'`.

`VIS-337` realizes the derivative channel on the actual arithmetic staircase. With

`F(u)=e^(-u)E_A(e^u)`

and

`mu=sum Lambda(n)^2/n delta_(log n)`,

one has

`(1+D)F=mu-u du`,

and every prime-power jump is copied exactly into Wang's derivative channel. Individual atoms are exponentially below the Korobov--Vinogradov-scale source envelope, so isolated jumps cannot carry the missing scale.

`VIS-338` removes the complete proper-prime-power escape: the `k>=2` source, its Green response, its one-sided derivative response, and its far-tail jump mass are all `O(U^2 e^(-U/2))`, exponentially below the live envelope. The only possible envelope-scale source carrier is therefore the `k=1` prime contribution against the continuous baseline.

`VIS-339` identifies that surviving prime source exactly. If

`G(u)=e^(-u)theta(e^u)-1`

and

`nu_prime=mu_prime-u du`,

then

`nu_prime=u(1+D)G`,

and every smooth prime packet is an exact functional of `G`. Thus atomic coordinates, tapers, phases, blocks, or multiscale linear statistics do not create an independent source channel.

`VIS-340` closes the parallel summatory escape. If

`A_prime(x)=sum_(p<=x)(log p)^2`

and

`P(u)=e^(-u)[A_prime(e^u)-e^u(u-1)]`,

then exact partial summation gives

`P(u)=uG(u)-H(u)+2e^(-u)`,

where `H` is the one-sided exponential average of `G`, and the map is explicitly invertible after removing the endpoint term. The full normalized `Lambda^2` summatory remainder differs from `P` only by an `O(u^2e^(-u/2))` proper-prime-power correction. At a Korobov--Vinogradov envelope, `H` stays on the same envelope scale, so at envelope-saturating heights `F(u)/(uG(u))->1`.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`.

## Research question

Does the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`

have a genuinely nonstationary or scale-migrating property at the live source-envelope scale which survives the exact quotients in `VIS-339` and `VIS-340`, and which Wang's nonvanishing one-order filter turns into a pointwise smaller

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`?

If such a property exists, does Wang's complete downstream error decomposition retain the smaller `Q` scale without requiring `Q'` or equivalent unsmoothed information at the larger source scale?

## Why it may matter

The source side has now been stripped of four false mechanisms. The desired leverage cannot come from isolated arithmetic singularities (`VIS-337`), collective proper-prime-power mass (`VIS-338`), repackaging prime atoms into smooth packets (`VIS-339`), or the elementary theta-to-square-log summatory partial-summation step (`VIS-340`).

A positive result must therefore expose a genuine property of the classical prime-counting error itself. The only remaining plausible source-side leverage is that `G` contains nonstationary or migrating log-frequency structure which the exact Wang filter attenuates pointwise even though it cannot annihilate any fixed band. A negative result showing that every admissible such structure is either a stronger PNT remainder in disguise or is repaid downstream would close the remaining fixed-source transform route for a source-specific reason.

## Decisive test

Start from the exact source quotients

`nu_prime=u(1+D)G`

and

`F(u)=uG(u)-H(u)+2e^(-u)+O(u^2e^(-u/2))`,

with the exact causal inverse for the prime-only summatory term supplied by `VIS-340`.

A candidate survives the source gate only if its content remains nontrivial when stated directly as a quantitative property of `G`. Reject any mechanism whose apparent gain is produced only by atomic packetization, prime square-log weighting, ordinary partial summation, positive-mass estimates, coherent regular variation, a fixed/bounded log-frequency band, or a restatement of an already assumed prime-number-theorem remainder.

For a surviving candidate, derive the resulting pointwise size of `Q` through the exact multiplier from `VIS-333` and compare it against the Korobov--Vinogradov-scale input. If a proposed gain is `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate still carries the Mellin/zero-free-half-plane cost isolated in `VIS-331`.

Then trace the same mechanism through Wang's complete destination. Explicitly identify every term depending on `Q`, `Q'`, or equivalent unsmoothed source information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Kill a candidate if its only content disappears under the `VIS-339` theta translation or the `VIS-340` summatory inversion, if it relies on isolated prime discontinuities or proper-prime-power mass, if it discards signed baseline cancellation by absolute values, if it hides a stronger theta/PNT remainder, or if a downstream term pays back the derivative carrier.

## Evidence boundary

`VIS-333`--`VIS-336` classify generic filter transfer and repayment. `VIS-337` proves that prime-power atoms enter `Q'` exactly and that each individual atom is too small. `VIS-338` proves that all proper prime powers are collectively negligible at the live envelope scale. `VIS-339` proves that the remaining centered `k=1` prime source is exactly `u(1+D)G` and that its smooth packet statistics are exact functionals of `G`. `VIS-340` proves that the prime square-log summatory remainder is an explicitly invertible partial-summation image of the same `G`, with proper prime powers exponentially lower order.

None of these results proves a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, arithmetic frequency migration, or destination-level avoidance of derivative-sensitive information. The clue therefore remains `accepted`.

## Research disposition

Outcome: **narrowed**.

The live source question no longer concerns whether a clever representation of primes creates hidden cancellation before Wang's filter. Both the atomic and summatory source descriptions quotient back explicitly to the Chebyshev-theta remainder. The remaining candidate mechanism must be a genuine nonstationary property of `G` itself, followed by demonstrable attenuation through Wang's nonvanishing filter and a destination-level proof that the derivative carrier is not paid back.