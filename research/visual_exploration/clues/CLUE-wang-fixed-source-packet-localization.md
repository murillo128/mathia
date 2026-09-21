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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The source side has already collapsed to the normalized Chebyshev-theta remainder

`G(u)=e^(-u)theta(e^u)-1`.

`VIS-333`--`VIS-340` show that Wang's prime and square-log summatory channels are exact transforms of the same source and that pointwise inversion repays one derivative. `VIS-341`--`VIS-353` price fixed smoothing/order, finite dilation and translation geometry, moving windows, phase entropy, confluent propagation, phase collisions, and separated finite cluster blocks. `VIS-354` identifies the upstream fixed-depth coefficient map as a source-free truncated Vandermonde map; `VIS-355`--`VIS-361` then close bounded source-adaptive selection, anchored scale-count growth, compact packing collapse, regular one- and multi-cluster occupancy, pooled center collisions, and arbitrary positive diagonal coefficient weights whenever the corresponding normalized moment Gram remains healthy.

`VIS-362` and `VIS-363` price the first weighted degenerations. A one-level outer rank collapse with one healthy inner scale pays the appropriate Hermite depth, while polynomially vanishing positive support masses simply add weight valuations to the Hermite jet costs.

`VIS-364` removes the next apparent escape: a strictly nested finite chain of polynomial scales has a complete cumulative Newton spectrum. Merely inserting deeper positive separations does not create an unpriced resource.

`VIS-365` closes the fixed finite branching version altogether. For fixed `N,q`, positive normalized weights with `sqrt(pi_i) asymp epsilon^(a_i)`, and compact distinct nodes with pair separations `|t_i-t_j| asymp epsilon^(kappa_ij)`, define

`Gamma_k = min_(|I|=k) [sum_(i in I) a_i + sum_(i<j, i,j in I) kappa_ij]`.

Then the weighted polynomial-sampling singular values satisfy

`prod_(r=1)^k s_r asymp epsilon^(Gamma_k)`

and

`s_k asymp epsilon^(Gamma_k-Gamma_(k-1))`.

Thus every fixed finite positive weighted branching hierarchy with stable power valuations is already priced by a finite tropical subset-energy ledger. The minimizing supports need not form one nested branch, so branching itself is no longer a residual compact mechanism.

## Research question

After quotienting the entire fixed finite positive-diagonal, power-valued compact Vandermonde geometry, can a genuinely source-coupled, growing, non-power, or different-topology construction produce a smaller Wang destination without merely importing a stronger estimate for `G`, `theta`, or an equivalent unsmoothed source quantity?

The remaining routes must leave at least one hypothesis of `VIS-365`: support cardinality or cancellation depth may grow; node/mass scales may lack stable comparable power valuations; coefficient geometry may become signed, indefinite, non-diagonal, or otherwise non-Hilbert; nodes or weights may depend on signed arithmetic information from the source; or the mechanism may use global phase/window geometry, scale escape, an infinite-dimensional limit, or nonlinear source dependence.

A recursively changing active subspace is interesting only if it actually escapes the finite subset-energy description. A more complicated finite branch tree with positive power-law masses and separations does not.

## Why it may matter

The compact fixed-depth positive branch has changed character. Earlier findings progressively priced particular cluster geometries; `VIS-365` gives a global finite formula that subsumes arbitrary finite branching under stable power valuations. This prevents further work from mistaking increasingly elaborate cluster trees for new arithmetic cancellation.

The useful frontier is therefore sharper: either identify a representation whose asymptotic geometry is genuinely outside a fixed finite valuation ledger, or expose source information that the geometry alone cannot manufacture. That distinction is exactly what the Wang line needs, because any destination gain that is only a singular-value conditioning effect is not evidence of stronger prime cancellation.

## Decisive test

For any proposed continuation, first state exactly which closed assumption is being abandoned.

If `N` and `q` are fixed, the normalized weights are positive, the nodes remain in a compact interval, and all weight and pair-separation scales admit stable power valuations in one parameter `epsilon`, apply `VIS-365` before crediting any gain. Compute the actual exponents `a_i` and `kappa_ij`, then the subset energies `Gamma_k` and the marginal exponent

`gamma_q=Gamma_q-Gamma_(q-1)`.

After restoring the outer Wang factors from `VIS-360`--`VIS-361`, the quotient floor is

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^(gamma_q)`.

Kill the route as source-free conditioning geometry if the claimed compact gain is exactly this scale. `VIS-364` is the corresponding transparent Newton benchmark for a one-branch nested chain and can be used when that representation makes the cost easier to read.

If support size `N=N(epsilon)` or cancellation depth `q=q(epsilon)` grows, account explicitly for the changing family of minors, occupancy, moment-system conditioning, and any loss in the Wang destination. Fixed-dimensional norm equivalences from `VIS-365` cannot simply be carried into that limit.

If scales are claimed to be non-power or mutually non-comparable, specify the actual asymptotic family and show why no single reparameterization or finite valuation data recover the relevant singular hierarchy. A merely awkward choice of parameter is not an escape.

If coefficient geometry leaves the positive diagonal Hilbert setting, define the coefficient topology and norm exactly and identify which step of the positive weighted-moment reduction fails. If coefficients, nodes, scales, translations, weights, or selectors use signed information from `G`, `theta`, or another arithmetic statistic, formulate the claimed gain directly as a source estimate and show that the selection rule does not already encode the desired stronger bound.

If the route uses phase/window growth, scale escape, nonlinear dependence, or an infinite representation, specify the growth parameter, convergence topology, truncation control, and the full destination repayment. Kill the route if the improvement disappears once those costs are charged or if it reduces to a stronger source estimate assumed rather than proved.

## Evidence boundary

`VIS-333`--`VIS-365` are exact representation, obstruction, conditioning, compactness, interpolation, and finite-dimensional negative-control results. `VIS-364` prices a maximally nested one-branch hierarchy; `VIS-365` prices arbitrary fixed finite positive weighted branching with stable power valuations through compound-matrix/Vandermonde subset energies.

These findings do not prove a stronger PNT remainder, a new pointwise estimate for `G`, an RH-equivalent localization theorem, or a destination-level improvement. `VIS-365` also does not classify growing `N` or `q`, genuinely non-power/non-comparable asymptotics, signed or non-diagonal coefficient geometries, source-dependent arithmetic selectors, infinite-dimensional limits, or global phase/window mechanisms.

The clue therefore remains `accepted`, but the fixed finite positive power-valued compact branch is now closed as a standalone escape. The unresolved question begins only outside that ledger.

## Research disposition

Outcome: **narrowed**.

Treat every fixed finite compact positive-diagonal Wang bank with stable power valuations of its normalized weights and pair separations as priced source-free geometry. Future work must exhibit growing support/depth, genuinely non-power asymptotics, a different coefficient topology, source-dependent signed arithmetic information, scale/phase/window escape, infinite-dimensional structure, or another mechanism that survives the unchanged Wang destination audit.