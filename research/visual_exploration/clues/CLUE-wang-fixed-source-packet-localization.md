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
  - research/visual_exploration/findings/VIS-343-wang-dilate-mixture-cancellation-order.md
  - research/visual_exploration/findings/VIS-344-wang-translated-dilate-cancellation-fibers.md
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

Subpolynomial `r(u)` therefore still cannot change the fixed `u`-power class. A target exponent `3/5+delta` inside the same scalar model requires `r(u)=u^(5delta/2+o(1))`. Any packet explanation based only on accumulating finitely, polylogarithmically, or otherwise subpolynomially many scalar inverse-frequency powers is excluded as a source of a fixed power-class gain.

`VIS-343` makes that scale-count obstruction exact for pure dilates of Wang's actual multiplier. For

`M(xi)=sum_(j=1)^N c_j m(a_j xi)`

with distinct positive scales and frequency-independent coefficients, the inverse-frequency coefficients are proportional to the moments `sum_j c_j a_j^(-k)`. Vandermonde invertibility implies that a nonzero `N`-dilate combination can cancel at most the first `N-1` powers, so its maximal polynomial high-frequency decay is order `N`. Thus even optimally tuned pure-dilation banks with subpolynomial scale count stay below the order growth required by `VIS-342`; a fixed scalar power-class gain needs polynomially many distinct dilates before coefficient stability, leakage, or destination costs are charged.

`VIS-344` closes the corresponding **uniform translated-tail** escape. For

`M(xi)=sum_j c_j exp(-i b_j xi)m(a_j xi)`,

uniform decay `O(|xi|^-r)` forces the first `r-1` inverse-scale moments to vanish **inside every distinct translation fiber separately**. Finite exponential-polynomial uniqueness prevents different phases from cancelling each other asymptotically. If a translation fiber contains `n_b` active scales, then `r<=n_b`; with `B` active translations and `N` total translated dilates, `N>=Br`. Translation phases therefore do not pool a larger uniform polynomial smoothing order. Any remaining phase-sensitive possibility must be genuinely nonuniform in frequency, adaptive, or source-coupled rather than another constant-weight asymptotic tail cancellation.

The moving-upper occupancy branch is separately closed at the required upper-bound scale by `VIS-329`.

## Research question

Does the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`

have a genuinely nonstationary or scale-migrating property at the live source-envelope scale which survives the exact quotients in `VIS-339` and `VIS-340`, is not reducible to the scalar Korobov--Vinogradov optimization classified by `VIS-341`--`VIS-344`, and which Wang's nonvanishing one-order filter turns into a pointwise smaller

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`?

If the proposed mechanism is still scalarizable as an effective truncation order `r_eff(u)`, can it actually generate polynomial growth of that order while keeping leakage and every destination term under control? For pure or translated constant-weight dilation banks, can it meet the polynomial scale count and fiberwise cancellation costs forced by `VIS-342`--`VIS-344` with stable coefficients and norms?

If it is not scalarizable, what **finite-window, frequency-dependent, adaptive, signed, or arithmetic localization** prevents reduction to a uniform moment-cancellation model or an objective of the form `u nu(t)+r log t`? In particular, can a phase-sensitive packet exploit a moving frequency window or a quantitative property of `G` itself rather than merely shifting copies of the filter tail?

If such a property exists, does Wang's complete downstream error decomposition retain the smaller `Q` scale without requiring `Q'` or equivalent unsmoothed information at the larger source scale?

## Why it may matter

The source side has now been stripped of eight false or incomplete mechanisms. The desired leverage cannot come from isolated arithmetic singularities (`VIS-337`), collective proper-prime-power mass (`VIS-338`), repackaging prime atoms into smooth packets (`VIS-339`), the elementary theta-to-square-log summatory partial-summation step (`VIS-340`), adding a fixed finite amount of polynomial spectral smoothing (`VIS-341`), letting that scalar smoothing order grow only subpolynomially (`VIS-342`), claiming arbitrarily high smoothing from a small pure-dilation bank (`VIS-343`), or using distinct constant-weight translations to pool asymptotic cancellation across phase fibers (`VIS-344`).

A positive result must therefore expose a genuinely stronger property of the classical prime-counting error itself. Within the scalar zero-free-width/truncation model, a fixed improvement in the `u`-power class has an explicit polynomial effective-order cost. Pure dilates require at least that many scales, while several translated fibers must each pay the same order separately. Otherwise the mechanism must be genuinely nonuniform, adaptive, signed, or arithmetic. In every case the attenuation must survive the complete destination without derivative repayment.

## Decisive test

Start from the exact source quotients

`nu_prime=u(1+D)G`

and

`F(u)=uG(u)-H(u)+2e^(-u)+O(u^2e^(-u/2))`,

with the exact causal inverse for the prime-only summatory term supplied by `VIS-340`.

A candidate survives the source gate only if its content remains nontrivial when stated directly as a quantitative property of `G`. Reject any mechanism whose apparent gain is produced only by atomic packetization, prime square-log weighting, ordinary partial summation, positive-mass estimates, coherent regular variation, a fixed/bounded log-frequency band, or a restatement of an already assumed prime-number-theorem remainder.

Translate any proposed high-frequency gain into the zero-free-region/truncation language whenever that is the mechanism being invoked. If it amounts only to replacing the standard fixed polynomial tail cost `t^(-1)` by `t^(-r)` for another fixed `r`, `VIS-341` already shows that the Korobov--Vinogradov exponent class is unchanged. If the proposed scalar order is variable, `VIS-342` supplies the stronger gate: subpolynomial `r_eff(u)` cannot yield a fixed positive improvement in the `u`-power exponent, while a claimed gain `delta` requires `r_eff(u)=u^(5delta/2+o(1))` within the scalar model.

If the proposed mechanism is a linear combination of pure dilates `m(a_j xi)`, apply `VIS-343` before crediting multiscale smoothing. A nonzero bank of `N(u)` distinct dilates has polynomial tail order at most `N(u)`, so a claimed fixed gain `delta` requires at least `N(u)>=u^(5delta/2+o(1))` in this scalar route. Derive the actual coefficient system and control its norm/conditioning and finite-frequency leakage; the scale count is only a necessary condition.

If the proposed mechanism is a constant-weight translated-dilate bank `sum_j c_j exp(-i b_j xi)m(a_j xi)`, apply `VIS-344`. Uniform order `r_eff(u)` requires every active translation fiber to carry at least `r_eff(u)` distinct scales. Cross-phase interference cannot be credited as asymptotic smoothing. A candidate using translations survives this gate only if the claimed estimate is genuinely nonuniform — for example restricted to moving frequency windows — or if frequency-dependent/adaptive coefficients or source arithmetic enter the estimate explicitly.

For any such surviving nonuniform candidate, freeze the window, normalization and admissible coefficient dependence before inspecting confirmation data. State the exact inequality that beats the uniform-tail controls and show that the gain persists when translated back to a property of `G`; merely displaying phase concentration or local destructive interference is insufficient.

For a surviving candidate, derive the resulting pointwise size of `Q` through the exact multiplier from `VIS-333` and compare it against the Korobov--Vinogradov-scale input. If a proposed gain is `exp(-phi(u))`, compute the lower linear rate `liminf phi(u)/u`; any positive rate still carries the Mellin/zero-free-half-plane cost isolated in `VIS-331`.

Then trace the same mechanism through Wang's complete destination. Explicitly identify every term depending on `Q`, `Q'`, or equivalent unsmoothed source information. Accept transform leverage only if the final bound retains the smaller `Q` scale without requiring derivative-sized control that reconstructs the source through `VIS-334`.

Kill a candidate if its only content disappears under the `VIS-339` theta translation or the `VIS-340` summatory inversion, if its frequency migration reduces to the fixed-order optimization of `VIS-341`, the subpolynomial variable-order regime of `VIS-342`, the pure-dilation moment cancellation of `VIS-343`, or the uniform translated-fiber cancellation of `VIS-344`, if it relies on isolated prime discontinuities or proper-prime-power mass, if it discards signed baseline cancellation by absolute values, if it hides a stronger theta/PNT remainder, or if a downstream term pays back the derivative carrier.

## Evidence boundary

`VIS-333`--`VIS-336` classify generic filter transfer and repayment. `VIS-337` proves that prime-power atoms enter `Q'` exactly and that each individual atom is too small. `VIS-338` proves that all proper prime powers are collectively negligible at the live envelope scale. `VIS-339` proves that the remaining centered `k=1` prime source is exactly `u(1+D)G` and that its smooth packet statistics are exact functionals of `G`. `VIS-340` proves that the prime square-log summatory remainder is an explicitly invertible partial-summation image of the same `G`, with proper prime powers exponentially lower order. `VIS-341` proves that changing only a fixed polynomial truncation exponent in the Korobov--Vinogradov optimization changes the exponential constant by `r^(2/5)` but leaves the `3/5,-1/5` exponent class unchanged. `VIS-342` proves, within the same scalar model, that a variable order obeys the exact rescaling `Omega_r(u)=r Omega_1(u/r)` and that any fixed positive power-class gain requires polynomial growth of the effective order. `VIS-343` proves that a nontrivial frequency-independent combination of `N` distinct pure dilates of Wang's actual multiplier has high-frequency polynomial decay order at most `N`. `VIS-344` proves that adding constant-weight translations does not let different phase fibers share those cancelled orders: uniform tail cancellation must occur fiberwise.

None of these results proves a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, arithmetic frequency migration beyond that classical optimization, or destination-level avoidance of derivative-sensitive information. In particular, `VIS-344` does not classify finite or moving frequency windows, frequency-dependent coefficients, source-adaptive nonlinear combinations, or arithmetic sign correlations. None of `VIS-341`--`VIS-344` proves that Wang's complete argument literally acquires a scalar truncation order from a multiscale packet. The clue therefore remains `accepted`.

## Research disposition

Outcome: **narrowed**.

The live source question no longer concerns whether a clever representation of primes creates hidden cancellation before Wang's filter, whether generic Korobov--Vinogradov frequency migration plus fixed or subpolynomial extra inverse-frequency powers changes the asymptotic envelope class, whether a small pure-dilation bank can manufacture a large effective order, or whether fixed translated copies can cooperate across phases to manufacture that uniform tail order. A surviving scalar explanation must produce polynomially growing effective order with the scale/fiber costs above and controlled coefficients/leakage. Otherwise the remaining candidate mechanism must be genuinely nonuniform in frequency, adaptive, signed, or arithmetic in `G`, followed by demonstrable attenuation through Wang's nonvanishing filter and a destination-level proof that the derivative carrier is not paid back.