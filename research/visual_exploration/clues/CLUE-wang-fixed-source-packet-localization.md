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
  - research/visual_exploration/findings/VIS-347-variable-wang-phase-entropy-budget.md
  - research/visual_exploration/findings/VIS-348-higher-wang-moments-inherit-phase-entropy-gate.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has been reduced to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333` gives Wang's exact nonvanishing multiplier `m(xi)=4(1+i xi)/(4+xi^2)`, while `VIS-334` shows that exact pointwise inversion pays one derivative. `VIS-339` and `VIS-340` show that the surviving prime source and the prime square-log summatory source are exact differential/integral images of the same `G`; repackaging primes into packets is therefore not an independent information channel.

The generic scalar smoothing escapes have also been narrowed. `VIS-341` shows that every fixed finite polynomial smoothing order preserves the Korobov--Vinogradov power class. `VIS-342` shows that a fixed positive gain in that class would require polynomially growing effective order. `VIS-343` converts that order into a scale-count cost for pure Wang dilates, and `VIS-344` shows that fixed translated copies cannot pool asymptotic moment cancellation across distinct phase fibers.

`VIS-345` closes moving windows once their lengths resolve the translation gaps. `VIS-346` removes most of the remaining fixed-bank short-window loophole: Turán--Nazarov propagation shows that, for a fixed bank with `B` phase fibers, `O(X^-r)` cancellation on windows of length `ell_X` still forces the same fiber moments through order `r-1` whenever

`X min(ell_X,1)^(B-1) -> infinity`.

`VIS-347` prices the first genuinely scale-dependent escape. For an `X`-dependent bank, let `B_X` be the number of active first-moment phase fibers, `Delta_X` their minimum spacing, `ell_X` the window length, `S_X` the first inverse-scale moment vector, and `T_X=sum_j |c_(j,X)|/a_(j,X)^2`. Then order-`>=2` attenuation forces the Turán--Nazarov phase-entropy budget

`(B_X-1) log(A L_X/e_X)`
` >= log( X ||S_X||_2 / (sqrt(2) D_X) )`,

with `L_X=4(B_X-1)/Delta_X`, `e_X=min(ell_X,L_X)`, and `D_X=C_0/2+2T_X`.

If `D_X/||S_X||_2=X^(o(1))`, this budget must be `(1-o(1))log X`. Consequently, a bounded `B` with `ell_X=X^-alpha` and `Delta_X=X^-beta` needs `(B-1)(alpha+beta)>=1`, while well-separated phases on macroscopic windows need `B_X log B_X` at least of order `log X`, hence `B_X=Omega(log X/log log X)` up to constants.

`VIS-348` shows that the first-moment gate is not special. If the lower translated inverse-scale moment polynomials `P_1,...,P_(q-1)` vanish exactly and `P_q` is the first surviving one, then claiming one further local inverse-frequency order again forces the same one-power `X` Turán--Nazarov budget, now with the phase count, spacing and conditioning of the `q`th moment. Exact low-order Vandermonde cancellation therefore does not make the first surviving higher moment locally cheap.

The finite-bank escape is consequently quantitative at every first surviving tail order: it must pay through exact moment cancellation, phase count, phase coalescence, window shrinkage, or coefficient/scale degeneration before any arithmetic property of `G` is credited.

## Research question

Does `G` possess a genuinely scale-dependent, adaptive, signed, or arithmetic localization that survives these moment, phase-entropy and derivative-repayment gates and produces a pointwise smaller Wang output without reconstructing the larger source scale through `Q'` or equivalent unsmoothed information?

For finite translated/dilated packet mechanisms, can a family expose a complete moment ledger and meet the `VIS-347`/`VIS-348` entropy budgets with controlled coefficient norms, nondegenerate first surviving moments, finite-frequency leakage, and a realizable source coupling? Alternatively, can frequency- or source-dependent coefficients, interacting nonzero asymptotic orders, or an infinite expansion use signed structure of `G` in a way that is not equivalent to making one scalar multiplier uniformly small on a window?

## Why it may matter

The fixed and slowly varying scalar-bank routes are now substantially classified. Neither bounded/subpolynomial scalar order, a small pure-dilation bank, fixed translations, phase-resolving moving windows, ordinary mildly shrinking windows, a casually growing/coalescing phase bank, nor exact cancellation of several low tail moments can manufacture the required smoothing order without an explicit complexity or conditioning payment.

A surviving mechanism would therefore have to use information that those controls deliberately discard: interaction among nonzero orders on a finite window, sufficiently rich scale-dependent phase geometry, adaptive/source-coupled coefficients, an infinite representation, or arithmetic sign structure of `G`. Such a result would be qualitatively different from another filter-tail cancellation and would identify a more credible place to search for leverage.

## Decisive test

Start from the exact source quotients in `VIS-339` and `VIS-340` and state the candidate directly as a quantitative property of `G`. For any finite translated-dilate bank with frequency-independent coefficients, write the moment polynomials

`P_(q,X)(xi)=sum_b [sum_(j:b_j=b)c_(j,X)a_(j,X)^(-q)] exp(-i b xi)`

in order. Record which lower moments vanish exactly and identify the first surviving `P_q`. Apply `VIS-347` when `q=1` and `VIS-348` when `q>1`; compute the relevant phase count, minimum spacing, window length, moment norm and tail-conditioning term before crediting local attenuation.

A candidate that meets an entropy budget is not yet a positive result. Derive its coefficient system explicitly and control the norm/conditioning, finite-frequency leakage, phase crowding, scale count, and any interaction among nonzero asymptotic orders needed to realize the bank. If the apparent gain is purchased by the first surviving moment becoming polynomially small relative to the next-tail conditioning term, record that as coefficient/scale degeneration rather than source cancellation.

If coefficients depend on frequency or directly on `G`, or if the mechanism relies on interaction among several nonzero orders rather than exact lower cancellations, state that dependence explicitly and prove the resulting estimate as a signed source statement rather than rebranding it as fixed-filter smoothing. Any surviving gain must then be propagated through Wang's full destination: identify every occurrence of `Q`, `Q'`, or equivalent unsmoothed information and show that the final bound retains the smaller scale rather than reconstructing the source through the derivative channel.

Kill the route if it reduces to the already-classified scalar truncation order, violates the applicable phase-entropy budget at its first surviving moment, satisfies that budget only through an ill-conditioned coefficient explosion or vanishing moment, restates a stronger theta/PNT remainder, or loses the gain in a destination derivative term.

## Evidence boundary

`VIS-333`--`VIS-348` are obstruction and transfer results. They do not prove a new bound or nonstationarity theorem for `G`, an improvement of the Korobov--Vinogradov remainder, or a destination-level avoidance of derivative repayment.

`VIS-348` is conditional on exact cancellation of lower moment polynomials. It does not classify finite-window cancellation caused by interaction among several nonzero asymptotic orders, frequency/source-dependent coefficients, infinite expansions, or arithmetic sign cancellation coupled directly to `G`. The phase-entropy thresholds remain necessary controls for uniform/local multiplier smallness, not evidence that a qualifying source mechanism exists or is useful downstream.

The clue therefore remains `accepted`: the finite scalar packet hierarchy is narrower, but genuinely source-coupled or non-scalar localization remains unclassified.

## Research disposition

Outcome: **narrowed**.

Future work should require a finite-bank proposal to expose its complete moment ledger and pay the entropy/conditioning cost at the first surviving order. The remaining live branch should now concentrate on mechanisms that are not reducible to that ledger: interacting nonzero orders on finite windows, source/frequency-dependent coefficients, infinite expansions, or direct signed structure of `G`, followed by the unchanged downstream derivative audit.