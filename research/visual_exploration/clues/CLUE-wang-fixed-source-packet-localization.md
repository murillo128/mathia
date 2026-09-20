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
  - research/visual_exploration/findings/VIS-341-vk-scale-stable-under-finite-spectral-smoothing.md
  - research/visual_exploration/findings/VIS-342-vk-power-gain-requires-growing-truncation-order.md
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

`VIS-341` removes a weaker interpretation of the remaining frequency-migration escape. Bellotti's optimal PNT balance has the form

`Omega_1(u)=inf_t {u nu(t)+log t}`,

with `nu(t)` of Korobov--Vinogradov shape. More generally, replacing the polynomial truncation cost by fixed `t^(-r)` gives

`Omega_r(u) ~ C_A r^(2/5) u^(3/5)(log u)^(-1/5)`.

Thus any fixed finite improvement in polynomial high-frequency decay changes only the exponential constant, not the `3/5,-1/5` exponent class. Wang's one-order filter cannot create a new subpower class merely by being treated as one extra fixed inverse-frequency factor in the standard absolute truncation balance.

`VIS-342` extends that control to a growing scalar order. The exact identity

`Omega_r(u)=r(u) Omega_1(u/r(u))`

shows that, whenever `u/r(u)->infinity`,

`Omega_r(u) ~ C_A u^(3/5) r(u)^(2/5)[log(u/r(u))]^(-1/5)`.

Subpolynomial `r(u)` therefore still cannot change the fixed `u`-power class. A target exponent `3/5+delta` inside the same scalar model requires `r(u)=u^(5delta/2+o(1))`. Any packet explanation based only on accumulating finitely, polylogarithmically, or otherwise subpolynomially many scalar inverse-frequency powers is now excluded as a source of a fixed power-class gain.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`.

## Research question

Does the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`

have a genuinely nonstationary or scale-migrating property at the live source-envelope scale which survives the exact quotients in `VIS-339` and `VIS-340`, is not reducible to the scalar Korobov--Vinogradov optimization classified by `VIS-341` and `VIS-342`, and which Wang's nonvanishing one-order filter turns into a pointwise smaller

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`?

If the proposed mechanism is still scalarizable as an effective truncation order `r_eff(u)`, can it actually generate polynomial growth of that order while keeping leakage and every destination term under control? If it is not scalarizable, what signed or arithmetic localization prevents reduction to an objective of the form `u nu(t)+r log t`?

If such a property exists, does Wang's complete downstream error decomposition retain the smaller `Q` scale without requiring `Q'` or equivalent unsmoothed information at the larger source scale?

## Why it may matter

The source side has now been stripped of six false mechanisms. The desired leverage cannot come from isolated arithmetic singularities (`VIS-337`), collective proper-prime-power mass (`VIS-338`), repackaging prime atoms into smooth packets (`VIS-339`), the elementary theta-to-square-log summatory partial-summation step (`VIS-340`), adding a fixed finite amount of polynomial spectral smoothing (`VIS-341`), or even letting that scalar smoothing order grow only subpolynomially (`VIS-342`).

A positive result must therefore expose a genuinely stronger property of the classical prime-counting error itself. Within the scalar zero-free-width/truncation model, a fixed improvement in the `u`-power class now has an explicit price: polynomially growing effective order. Otherwise the mechanism must be genuinely non-scalar, signed, or arithmetic. In either case the attenuation must survive the complete destination without derivative repayment.

## Decisive test

Start from the exact source quotients

`nu_prime=u(1+D)G`

and

`F(u)=uG(u)-H(u)+2e^(-u)+O(u^2e^(-u/2))`,

with the exact causal inverse for the prime-only summatory term supplied by `VIS-340`.

A candidate survives the source gate only if its content remains nontrivial when stated directly as a quantitative property of `G`. Reject any mechanism whose apparent gain is produced only by atomic packetization, prime square-log weighting, ordinary partial summation, positive-mass estimates, coherent regular variation, a fixed/bounded log-frequency band, or a restatement of an already assumed prime-number-theorem remainder.

Translate any proposed high-frequency gain into the zero-free-region/truncation language whenever that is the mechanism being invoked. If it amounts only to replacing the standard fixed polynomial tail cost `t^(-1)` by `t^(-r)` for another fixed `r`, `VIS-341` already shows that the Korobov--Vinogradov exponent class is unchanged. If the proposed scalar order is variable, `VIS-342` supplies the stronger gate: subpolynomial `r_eff(u)` cannot yield a fixed positive improvement in the `u`-power exponent, while a claimed gain `delta` requires `r_eff(u)=u^(5delta/2+o(1))` within the scalar model.

Accordingly, a scalarizable packet candidate must derive its effective order from the actual filter/truncation estimate, not assign it by analogy, and must show the required polynomial growth without a compensating growth of leakage, constants, source norms, or downstream error terms. A non-scalar candidate must instead identify the signed or arithmetic estimate that invalidates reduction to the scalar objective `u nu(t)+r log t`; merely using many scales or many coefficients is not enough.

For a surviving candidate, derive the resulting pointwise size of `Q` through the exact multiplier from `VIS-333` and compare it against the Korobov--Vinogradov-scale input. If a proposed gain is `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate still carries the Mellin/zero-free-half-plane cost isolated in `VIS-331`.

Then trace the same mechanism through Wang's complete destination. Explicitly identify every term depending on `Q`, `Q'`, or equivalent unsmoothed source information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Kill a candidate if its only content disappears under the `VIS-339` theta translation or the `VIS-340` summatory inversion, if its frequency migration reduces to the fixed-order optimization of `VIS-341` or the subpolynomial variable-order regime of `VIS-342`, if it relies on isolated prime discontinuities or proper-prime-power mass, if it discards signed baseline cancellation by absolute values, if it hides a stronger theta/PNT remainder, or if a downstream term pays back the derivative carrier.

## Evidence boundary

`VIS-333`--`VIS-336` classify generic filter transfer and repayment. `VIS-337` proves that prime-power atoms enter `Q'` exactly and that each individual atom is too small. `VIS-338` proves that all proper prime powers are collectively negligible at the live envelope scale. `VIS-339` proves that the remaining centered `k=1` prime source is exactly `u(1+D)G` and that its smooth packet statistics are exact functionals of `G`. `VIS-340` proves that the prime square-log summatory remainder is an explicitly invertible partial-summation image of the same `G`, with proper prime powers exponentially lower order. `VIS-341` proves that changing only a fixed polynomial truncation exponent in the Korobov--Vinogradov optimization changes the exponential constant by `r^(2/5)` but leaves the `3/5,-1/5` exponent class unchanged. `VIS-342` proves, within the same scalar model, that a variable order obeys the exact rescaling `Omega_r(u)=r Omega_1(u/r)` and that any fixed positive power-class gain requires polynomial growth of the effective order.

None of these results proves a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, arithmetic frequency migration beyond that classical optimization, or destination-level avoidance of derivative-sensitive information. In particular, neither `VIS-341` nor `VIS-342` proves that Wang's multiplier literally changes Bellotti's scalar truncation exponent, or that every multiscale signed packet can be represented by a scalar `r_eff(u)`. The clue therefore remains `accepted`.

## Research disposition

Outcome: **narrowed**.

The live source question no longer concerns whether a clever representation of primes creates hidden cancellation before Wang's filter, whether generic Korobov--Vinogradov frequency migration plus a fixed extra inverse-frequency power changes the asymptotic envelope class, or whether slowly accumulating scalar smoothing powers can do so. A surviving scalar explanation must produce polynomially growing effective order with controlled leakage and destination costs; otherwise the remaining candidate mechanism must be genuinely non-scalar signed/arithmetic structure in `G`, followed by demonstrable attenuation through Wang's nonvanishing filter and a destination-level proof that the derivative carrier is not paid back.