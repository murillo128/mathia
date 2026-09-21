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
  - research/visual_exploration/findings/VIS-368-uniform-positive-hilbert-correlation-is-bounded-preconditioning.md
  - research/visual_exploration/findings/VIS-369-source-free-degenerate-positive-metric-prescribes-singular-spectrum.md
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

`VIS-367` identifies the first generic growing-depth effect. For every positive probability measure on `[-1,1]`,

`Z_q(mu) <= 2^(-(q-1)(q-2))`

and the raw monomial sampling map satisfies

`s_q(q) <= 2^(2-q)`.

These bounds come from the classical Chebyshev minimax polynomial and are completely source-free. Thus even before arithmetic information enters, growing polynomial depth creates a super-exponentially shrinking determinant scale and an exponentially small raw monomial singular direction.

`VIS-368` closes bounded positive coefficient correlation. If an already priced diagonal covariance `W` and a positive-definite correlated covariance `H` satisfy

`mW <= H <= MW`,

then every corresponding Wang singular value changes by at most the fixed factors `sqrt(m)` and `sqrt(M)`. Uniform positive off-diagonal correlation is therefore only bounded preconditioning.

`VIS-369` now closes the opposite, previously unconstrained loophole. If a positive metric is allowed to degenerate freely and to align with the right-singular basis of the already priced source-free Wang map `A_W`, then for any prescribed positive active spectrum `tau_1,...,tau_r` one can choose

`C = V diag((tau_i/sigma_i)^2) V^*`

on the active right-singular sector and obtain exactly that spectrum after the metric change. An arbitrarily small singular direction, whitening, or any chosen asymptotic singular scale can therefore be manufactured without arithmetic source information. The relative metric eigenvalues pay exactly the square of the imposed singular-value factors.

So **fixed depth is closed by the partition-sum audit, growing depth must first quotient the universal Chebyshev/capacity baseline, bounded positive correlations are only preconditioning, and arbitrary source-free positive metric degeneration is too expressive to count as arithmetic structure**.

## Research question

After quotienting fixed-depth positive compact polynomial-sampling geometry, the universal source-free high-degree Chebyshev/capacity collapse, uniformly equivalent positive coefficient metrics, and freely engineered source-free metric degeneration, can a genuinely source-justified or physically mandated metric degeneration, indefinite/non-Hilbert topology, noncompact/global mechanism, or nonlinear source coupling produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

Cancellation depth `q` may grow, but a useful result must survive the generic high-degree compact conditioning in `VIS-367` and the scalar order-growth cost in `VIS-342`. A positive metric no longer counts as a distinct mechanism merely because its relative Loewner spectrum degenerates: `VIS-369` shows that unrestricted degeneration can prescribe the measured singular spectrum by construction. The remaining positive-metric route must therefore explain what fixes the metric independently of the desired Wang singular improvement and must propagate that resource through the physical coefficient and destination norms.

Other live routes include genuinely indefinite or non-Hilbert coefficient topology, nodes/weights/selectors depending on signed arithmetic information from the source, normalized support escaping compactness with a nontrivial destination repayment, global phase/window geometry, nonlinear source dependence, or a genuinely infinite-dimensional limit with a controlled physical coefficient topology.

## Why it may matter

The Wang branch has progressively separated arithmetic information from representation and conditioning geometry. `VIS-365` replaced finite branch trees by one tropical subset-energy ledger, `VIS-366` replaced that finite valuation picture by exact positive partition sums, `VIS-367` showed that the most obvious growing-depth collapse is classical source-free approximation geometry, `VIS-368` removed bounded positive correlation, and `VIS-369` shows that allowing arbitrary positive metric degeneration in the opposite direction makes the diagnostic completely non-identifying.

This sharpens the remaining frontier materially. A future positive result must show a **net destination gain** after polynomial coordinates, high-degree conditioning, coefficient-metric choice, truncation/order growth, and outer Wang factors are all charged. A tiny singular value, dramatic condition-number change, or correlated/degenerating positive norm is not enough when the same effect can be installed by right preconditioning the source-free coefficient map.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned or which source-free baseline is claimed to be beaten.

If the effective polynomial/cancellation depth `q` is fixed, the coefficient geometry is positive Hilbert after normalization, and the normalized support lies in one fixed compact interval, apply `VIS-366` to the underlying positive polynomial-sampling geometry. For a non-diagonal positive covariance `H`, choose the physically natural priced baseline `W` and form

`C=W^(-1/2) H W^(-1/2)`.

If the spectrum of `C` stays in one fixed interval `[m,M] subset (0,infinity)`, apply `VIS-368` and kill the supposed metric gain as bounded preconditioning.

If the spectrum of `C` degenerates, do not credit the degeneration automatically. Compare the full eigenvalue-and-orientation geometry of `C` with the right-singular decomposition of the baseline Wang map. If the metric is free to align with those singular directions, apply `VIS-369`: the active singular spectrum can be prescribed at will, so the observed gain is engineered preconditioning. A surviving positive-metric route must identify an independent mathematical or physical rule that fixes `C` before the target spectral improvement is read off, or derive a source-dependent rule and charge the information and norm cost of that rule through the destination.

If `q=q(parameter)` grows, first affine-normalize the compact node coordinate and identify the actual coefficient norm used by the Wang destination. Apply the `VIS-367` baseline: on `[-1,1]`, generic positive compact monomial geometry already allows

`Z_q <= 2^(-(q-1)(q-2))`, `s_q <= 2^(2-q)`.

Then apply `VIS-368`/`VIS-369` to any positive correlated or degenerating metric dimension by dimension. Uniform Loewner equivalence changes only constants; unrestricted degeneration can engineer the target spectrum. If a better-conditioned polynomial basis is introduced, include the norm of the basis change needed to return to the physical Wang tail coefficients. Then combine any residual gain with `VIS-342`: a fixed change in the scalar Vinogradov--Korobov power class requires polynomial growth of the relevant effective order together with its truncation and destination costs.

If coefficient geometry is genuinely indefinite/non-Hilbert, define its topology and destination norm precisely and identify exactly which positivity/Loewner/SVD-preconditioning step fails. If nodes, weights, scales, translations, metric, or selectors use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as a source estimate and show that the selection rule does not already encode the desired stronger bound.

If support escapes the compact normalized regime, or the route uses phase/window growth, nonlinear dependence, or an infinite-dimensional representation, specify the growth parameter, convergence topology, truncation control, coefficient normalization, and full destination cost. Kill the route if the gain disappears once those costs are charged or if it reduces to a stronger source estimate assumed rather than proved.

## Evidence boundary

`VIS-333`--`VIS-365` are exact representation, obstruction, conditioning, interpolation, compactness, and finite-dimensional negative-control results. `VIS-366` adds a support-cardinality-independent exact partition-sum comparison for every positive compact coefficient measure at fixed polynomial depth. `VIS-367` adds only a universal growing-depth baseline: classical Chebyshev minimax forces an `exp(-Theta(q^2))` determinant ceiling and an exponential raw-monomial smallest-singular-value ceiling in normalized compact coordinates. `VIS-368` adds an exact Loewner comparison showing that uniformly equivalent positive non-diagonal Hilbert metrics preserve every singular-value scale up to bounded factors. `VIS-369` adds an exact SVD construction showing that an unrestricted source-free degenerating positive metric can prescribe every strictly positive active singular value of the baseline Wang map.

These findings do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement. `VIS-367` does not prove that growing depth is useless. `VIS-368` does not classify metric degeneration. `VIS-369` does not rule out a positive degenerating metric fixed independently by the physical problem or genuinely derived from arithmetic source information; it rules out treating freely engineered metric degeneration as evidence. Indefinite/non-Hilbert coefficient spaces, noncompact/global phase-window escape, nonlinear dependence, and genuinely different infinite-dimensional topologies remain outside these closures.

The clue therefore remains `accepted`, but fixed-depth positive compact geometry, raw high-degree compact-capacity collapse, uniformly equivalent positive correlated Hilbert metrics, and arbitrary source-free singular-vector-aligned metric degeneration are now closed as standalone explanations of arithmetic gain.

## Research disposition

Outcome: **narrowed**.

Treat any fixed-depth positive compact Wang bank as source-free moment conditioning priced by `VIS-366`. When depth grows, first quotient the universal Chebyshev/capacity collapse from `VIS-367` and charge the coefficient/basis-change and scalar order costs from `VIS-342`. For a positive non-diagonal metric, apply the relative Loewner test from `VIS-368`; if it is uniformly comparable, it is only bounded preconditioning. If it degenerates, apply `VIS-369`; degeneration aligned freely with the baseline right-singular geometry can manufacture the desired singular spectrum and is not a new resource. Future work must therefore exhibit independently fixed/source-justified metric degeneration with its costs repaid, genuinely different coefficient topology, source-dependent arithmetic information, noncompact/global geometry, nonlinear dependence, or another mechanism outside these positive compact preconditioning baselines.