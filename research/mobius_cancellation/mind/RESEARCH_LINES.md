# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify the superpolynomial endpoint source cost and test whether the proof rate can be improved

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-067-exact-endpoints-force-superpolynomial-common-source-cost`.

MC-366--MC-370 separate exact-real source leakage, finite-resolution Hamming quotienting and average shell stability. MC-371--MC-376 then analyze the geometry of a hypothetical quartic-efficient exact endpoint. In that conditional regime, source incidence must be balanced and delocalized, almost every central mode has near-quadratic minimum primitive conductor, and a positive fraction of the Fourier cube still carries endpoint bias at least of order `R^(-1/2)`.

MC-377 changes the actual frontier. Using the source-incidence kernel, a large smooth mode subspace, smooth-modulus incomplete character sums and the Selberg/Bombieri frame bound, it proves for every exact endpoint source package

`log P / log y -> infinity`,

where `P` is the common lower-prime radical. Hence `P=y^(4+o(1))`, the near-quadratic primitive-conductor saturation analysis, and indeed **every fixed-power common-radical regime are impossible for an actual exact endpoint**. MC-372--MC-376 remain useful conditional anatomy of a finite-power near-equality model, but they are no longer the live source-cost regime.

MC-378 gives the first moving quantitative contradiction. Its generic smooth-modulus input rules out `P<=y^A` when `A^2=o(R)` and `A 2^(C A)=o(log log y)`, yielding a rank-sensitive lower bound of order

`log P/log y >= c min{sqrt(R/log(R+2)), log log log y}`.

MC-379 removes the generic analytic `log log log y` ceiling for the actual endpoint source class. After pruning both large and very small source primes at codimension `2^(O(A))`, the surviving canonical conductors are primitive, squarefree and rough from below. Multiplying the prime-local complete-sum estimate over the terminal squarefree block gives a fixed power saving before the final differencing root, without the generic condition `k 2^k << log log Q`. Consequently `P<=y^A` is impossible whenever

`2^(C A)=o(R)` and `2^(C A) log log y=o(log y)`,

and hence

`log P/log y >= c min{log(R+2), log log y}`

for an absolute nonoptimized `c>0`. This does not supersede the rank side of MC-378: `sqrt(R/log R)` may be stronger than `log R`. The two theorems are complementary and the strongest current source-cost statement uses whichever lower bound is larger in the regime at hand.

The live quantitative question has therefore shifted again. The generic moving-character `log log Q` absorption step is no longer the active analytic bottleneck for primitive rough squarefree endpoint modes. Remaining losses include the `2^(O(A))` cost of pruning small source coordinates, the exponential-in-depth loss surviving the final differencing root, and the separation between the logarithmic rank bound of MC-379 and the stronger rank geometry retained by MC-378. A stronger theorem must reduce those source-specific costs, combine the two regimes more efficiently, or bypass realization through one common lower-prime radical altogether.

## Keep resolution, source incidence, conductor, common-radical cost and bias amplitude distinct

The current resource ledger separates exact-real subset-sum conditioning, finite-resolution quotienting, `l1` worst-case shell displacement, `l2` average dephasing stability, source-incidence balance, incidence-signature delocalization, package conductor, minimum primitive conductor, common-radical size and endpoint bias amplitude. These are not interchangeable.

MC-377--MC-379 are especially important for interpretation: lower bounds on individual primitive conductors inside a hypothetical fixed-power package are weaker than proving that the **entire common source package must escape the polynomial hierarchy at a quantitative moving rate**. Conversely, neither the iterated-log/rank lower bounds nor the rough-squarefree improvement imply Möbius cancellation or establish an optimal source tariff. The endpoint argument must still specify which physical quotient is observed and how its source-cost obstruction reaches a destination quantity relevant to `M(x)`.

## Repair probabilistic comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

The source-cost results add another control: a plausible endpoint comparator must not hide the exact architecture inside a common source package whose cost violates MC-377--MC-379. Conditional finite-power models may still diagnose which modes or amplitudes would become expensive, but they cannot be used as evidence that an exact endpoint can actually inhabit that source regime.