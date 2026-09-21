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
  - research/visual_exploration/findings/VIS-349-wang-cross-order-confluent-exponential-polynomial.md
  - research/visual_exploration/findings/VIS-350-confluent-turan-total-multiplicity.md
  - research/visual_exploration/findings/VIS-351-divided-difference-cluster-conditioning.md
  - research/visual_exploration/findings/VIS-352-hermite-collision-scale-budget.md
  - research/visual_exploration/findings/VIS-353-separated-cluster-block-riesz-floor.md
  - research/visual_exploration/findings/VIS-354-wang-tail-coefficient-block-vandermonde.md
  - research/visual_exploration/findings/VIS-355-source-adaptive-compact-bank-floor.md
  - research/visual_exploration/findings/VIS-356-fixed-depth-bank-growth-anchored-floor.md
  - research/visual_exploration/findings/VIS-357-compact-wang-anchor-packing-collapse.md
  - research/visual_exploration/findings/VIS-358-dense-cluster-occupancy-width-floor.md
  - research/visual_exploration/findings/VIS-359-regular-multicluster-hermite-jet-capacity.md
  - research/visual_exploration/findings/VIS-360-pooled-rescaling-colliding-center-floor.md
  - research/visual_exploration/findings/VIS-361-weighted-pooled-moment-gram-floor.md
  - research/visual_exploration/findings/VIS-362-one-inner-scale-weighted-support-exponent.md
  - research/visual_exploration/findings/VIS-363-polynomial-mass-decay-hermite-order-statistic.md
  - research/visual_exploration/findings/VIS-364-nested-vandermonde-chain-cumulative-scale-spectrum.md
  - research/visual_exploration/findings/VIS-365-finite-weighted-vandermonde-subset-energy-spectrum.md
  - research/visual_exploration/findings/VIS-366-fixed-depth-vandermonde-partition-sum-spectrum.md
  - research/visual_exploration/findings/VIS-367-growing-depth-chebyshev-capacity-baseline.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price fixed smoothing/order, finite dilation and translation geometry, moving windows, phase entropy, confluent propagation, phase collisions, and separated finite cluster blocks. `VIS-354`--`VIS-361` reduce bounded compact positive coefficient geometry to truncated Vandermonde/moment conditioning. `VIS-362`--`VIS-365` then price weighted rank collapse, vanishing masses, nested scales, and arbitrary fixed finite positive branching with stable power valuations.

`VIS-366` removes the remaining fixed-depth positive compact support-count and valuation loopholes. For any positive probability measure `mu` on one compact normalized interval and fixed polynomial depth `q`, define

`Z_k(mu)=(1/k!) integral prod_(i<j)(x_j-x_i)^2 dmu^k`.

If `s_1>=...>=s_q` are the singular values of the degree-`q-1` polynomial sampling operator into `L^2(mu)`, then

`prod_(r<=k) s_r asymp_(q,K) sqrt(Z_k(mu))`

and

`s_k asymp_(q,K) sqrt(Z_k(mu)/Z_(k-1)(mu))`.

For discrete support, `Z_k` is the exact positive sum over all `k`-point weighted Vandermonde squares. This remains valid when support cardinality grows, when the support converges to a continuous positive measure, and when masses/separations have no common power-law valuation.

`VIS-367` now identifies the first generic growing-depth effect. For every positive probability measure on `[-1,1]`,

`Z_q(mu) <= 2^(-(q-1)(q-2))`

and the raw monomial sampling map satisfies

`s_q(q) <= 2^(2-q)`.

These bounds come from the classical Chebyshev minimax polynomial and are completely source-free. Thus even before arithmetic information enters, growing polynomial depth creates a super-exponentially shrinking determinant scale and an exponentially small raw monomial singular direction.

So **fixed depth is closed by the partition-sum audit, while growing depth must now be judged only after quotienting its universal Chebyshev/capacity and coordinate-conditioning baseline**.

## Research question

After quotienting fixed-depth positive compact polynomial-sampling geometry and the universal source-free high-degree Chebyshev/capacity collapse, can a genuinely growing-depth, source-coupled, different-topology, noncompact/global, or nonlinear construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The live routes must now leave or materially outperform the closed baselines. Cancellation depth `q` may grow, but a useful result must survive the generic high-degree compact conditioning in `VIS-367` and the scalar order-growth cost in `VIS-342`. Alternatively, coefficient geometry may become signed, indefinite, non-diagonal, or otherwise non-positive-Hilbert; nodes, weights, or selectors may depend on signed arithmetic information from the source; normalized support may escape compactness together with a nontrivial destination repayment; or the mechanism may use global phase/window geometry, nonlinear source dependence, or a genuinely infinite-dimensional limit with a controlled coefficient topology.

Merely adding more positive compact support points, allowing a continuous positive support, replacing power scales by non-power scales at fixed `q`, or citing the generic high-degree collapse of a raw monomial moment matrix no longer qualifies as a distinct mechanism.

## Why it may matter

The Wang branch has progressively separated arithmetic information from conditioning geometry. `VIS-365` replaced finite branch trees by one tropical subset-energy ledger, `VIS-366` replaced that finite valuation picture by exact positive partition sums, and `VIS-367` shows that the most obvious effect of letting the polynomial depth grow is itself classical source-free approximation geometry.

This makes the remaining frontier materially sharper. A future positive result must show a **net destination gain** after the polynomial coordinate system, high-degree conditioning, truncation/order growth, and outer Wang factors are all charged. A tiny determinant or raw coefficient singular value is not enough; the residual improvement has to carry source information that the same compact polynomial space does not already manufacture.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned or which source-free baseline is claimed to be beaten.

If the effective polynomial/cancellation depth `q` is fixed, the coefficient geometry is positive Hilbert/diagonal after the existing normalization, and the normalized support lies in one fixed compact interval, form its positive coefficient measure `mu` and the partition sums

`Z_k(mu)=(1/k!) integral prod_(i<j)(x_j-x_i)^2 dmu^k`, `1<=k<=q`.

Apply `VIS-366`. Kill the route as source-free conditioning geometry if the claimed improvement is exactly the smallness of `sqrt(Z_k/Z_(k-1))` after restoring the outer Wang mass/scale factors.

If `q=q(parameter)` grows, first affine-normalize the compact node coordinate and identify the actual coefficient norm used by the Wang destination. Apply the `VIS-367` baseline: on `[-1,1]`, generic positive compact monomial geometry already allows

`Z_q <= 2^(-(q-1)(q-2))`, `s_q <= 2^(2-q)`.

Do not credit determinant decay, monomial condition-number growth, or a high-degree near-null direction that is explained by this classical compact-capacity effect. If a better-conditioned polynomial basis is introduced, include the norm of the basis change needed to return to the physical Wang tail coefficients. Then combine the remaining gain with `VIS-342`: a fixed change in the scalar Vinogradov--Korobov power class requires polynomial growth of the relevant effective order, together with its truncation and destination costs.

If coefficient geometry leaves the positive Hilbert setting, define its topology and norm precisely and identify which moment/Gram positivity step fails. If nodes, weights, scales, translations, or selectors use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as a source estimate and show that the selection rule does not already encode the desired stronger bound.

If support escapes the compact normalized regime, or the route uses phase/window growth, nonlinear dependence, or an infinite-dimensional representation, specify the growth parameter, convergence topology, truncation control, coefficient normalization, and full destination cost. Kill the route if the gain disappears once those costs are charged or if it reduces to a stronger source estimate assumed rather than proved.

## Evidence boundary

`VIS-333`--`VIS-365` are exact representation, obstruction, conditioning, interpolation, compactness, and finite-dimensional negative-control results. `VIS-366` adds a support-cardinality-independent exact partition-sum comparison for every positive compact coefficient measure at fixed polynomial depth. `VIS-367` adds only a universal growing-depth **baseline**: classical Chebyshev minimax forces an `exp(-Theta(q^2))` determinant ceiling and an exponential raw-monomial smallest-singular-value ceiling in normalized compact coordinates.

These findings do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement. `VIS-367` does not prove that growing depth is useless, does not provide a uniform lower bound on the achievable Wang destination, and does not classify signed/indefinite/non-diagonal coefficient geometries, source-dependent arithmetic selectors, noncompact/global phase-window escape, nonlinear dependence, or genuinely different infinite-dimensional coefficient topologies.

The clue therefore remains `accepted`, but both fixed-depth positive compact geometry and the raw high-degree compact-capacity collapse are now closed as standalone explanations of arithmetic gain.

## Research disposition

Outcome: **narrowed**.

Treat any fixed-depth positive compact Wang bank as source-free moment conditioning priced by `VIS-366`. When depth grows, first quotient the universal Chebyshev/capacity collapse from `VIS-367` and charge the coefficient/basis-change and scalar order costs from `VIS-342`. Future work must exhibit a residual net destination improvement, different coefficient topology, source-dependent signed arithmetic information, noncompact/global geometry with its costs repaid, nonlinear dependence, or another mechanism outside these positive compact polynomial baselines.