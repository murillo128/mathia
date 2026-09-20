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

`VIS-339` now identifies that surviving prime source exactly. If

`G(u)=e^(-u)theta(e^u)-1`

and

`nu_prime=mu_prime-u du`,

then

`nu_prime=u(1+D)G`.

Moreover, every smooth packet satisfies

`integral phi d nu_prime = integral [(u-1)phi-u phi']G du`,

and `G` is recoverable from `nu_prime` after one boundary value. Thus a smooth prime packet, taper, phase, block, or multiscale linear statistic is not an independent information channel merely because it is expressed in atomic coordinates: it is an exact functional of the normalized Chebyshev-theta remainder.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`.

## Research question

Does the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`

have a genuinely nonstationary or multiscale property at the live source-envelope scale which, under Wang's exact nonvanishing filter, makes

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

pointwise smaller while the missing scale is carried by the derivative channel?

If such a property exists, does Wang's complete downstream error decomposition retain the smaller `Q` scale without requiring `Q'` or equivalent unsmoothed information at the larger source scale?

## Why it may matter

The remaining escape has now been stripped of three false sources of apparent leverage. It cannot be an isolated arithmetic singularity (`VIS-337`), it cannot be collective proper-prime-power mass (`VIS-338`), and it cannot gain independent status merely by repackaging the prime atoms into a smooth packet (`VIS-339`).

A positive result must therefore expose a genuine property of the classical prime-counting error itself, in a representation for which Wang's filter gives useful attenuation and the final destination does not repay that attenuation. A negative result showing that every admissible nonstationary property is repaid downstream would close the remaining fixed-source transform route for a source-specific reason.

## Decisive test

Start from the exact decomposition

`mu-u du = u(1+D)G + mu_pp`.

Use `VIS-338` as a hard control: account explicitly for the exponentially negligible `mu_pp` term. On the surviving source, do not begin from an atomic packet and infer novelty from its geometry. First translate any proposed smooth statistic through the `VIS-339` identity

`integral phi d nu_prime = integral [(u-1)phi-u phi']G du`.

A candidate survives the source gate only if the translated statement is a nontrivial quantitative property of `G` at the relevant scale rather than ordinary partial summation, a positive-mass estimate, coherent regular variation, a fixed/bounded log-frequency band, or a restatement of an already assumed prime-number-theorem remainder.

For a surviving candidate, derive the resulting pointwise size of `Q` and compare it against the Korobov--Vinogradov-scale input. If a proposed gain is `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate still carries the Mellin/zero-free-half-plane cost isolated in `VIS-331`.

Then trace the same mechanism through Wang's complete destination. Explicitly identify every term depending on `Q`, `Q'`, or equivalent unsmoothed source information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Kill a candidate if its only content disappears under the `VIS-339` theta translation, if it relies on isolated prime discontinuities or proper-prime-power mass, if it discards the signed baseline cancellation by absolute values, if it hides a stronger bound for the theta/source remainder, or if a downstream term pays back the derivative carrier.

## Evidence boundary

`VIS-333`--`VIS-336` classify generic filter transfer and repayment. `VIS-337` proves that prime-power atoms enter `Q'` exactly and that each individual atom is too small. `VIS-338` proves that all proper prime powers are collectively negligible at the live envelope scale. `VIS-339` proves that the remaining centered `k=1` prime source is exactly `u(1+D)G` and that its smooth packet statistics are exact functionals of `G`.

None of these results proves a new bound or nonstationary theorem for `G`, an improvement of the Korobov--Vinogradov remainder, arithmetic frequency migration, or destination-level avoidance of derivative-sensitive information. The clue therefore remains `accepted`.

## Research disposition

Outcome: **narrowed**.

The live source question is no longer "can many prime atoms form a special packet?" It is whether the normalized Chebyshev-theta remainder itself has a source-envelope-scale nonstationary structure that Wang's filter can exploit without the complete destination paying back the derivative carrier.