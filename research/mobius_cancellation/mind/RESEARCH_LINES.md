# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify the superpolynomial endpoint source cost and test whether the proof rate can be improved

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-067-exact-endpoints-force-superpolynomial-common-source-cost`.

MC-366--MC-370 separate exact-real source leakage, finite-resolution Hamming quotienting and average shell stability. MC-371--MC-376 then analyze the geometry of a hypothetical quartic-efficient exact endpoint. In that conditional regime, source incidence must be balanced and delocalized, almost every central mode has near-quadratic minimum primitive conductor, and a positive fraction of the Fourier cube still carries endpoint bias at least of order `R^(-1/2)`.

MC-377 changes the actual frontier. Using the source-incidence kernel, a large smooth mode subspace, smooth-modulus incomplete character sums and the Selberg/Bombieri frame bound, it proves for every exact endpoint source package

`log P / log y -> infinity`,

where `P` is the common lower-prime radical. Hence every fixed-power common-radical regime is impossible for an actual exact endpoint.

MC-378 gives the first moving quantitative contradiction. Its generic smooth-modulus input rules out `P<=y^A` when `A^2=o(R)` and `A 2^(C A)=o(log log y)`, yielding a rank-sensitive lower bound of order

`log P/log y >= c min{sqrt(R/log(R+2)), log log log y}`.

MC-379 uses the primitive rough-squarefree structure of the actual endpoint modes to lift the analytic ceiling to `log log y`, but its preliminary removal of tiny source primes costs `2^(O(A))` codimension and therefore weakens the rank-side condition to exponential-in-`A`.

MC-380 shows that this tradeoff was not intrinsic. Under `P<=y^A`, place the product `S` of source primes below `T_A=2^(K A)` into a **preliminary factor** before terminal differencing. The primorial estimate makes `S=y^(o(1))` in the moving range, while the terminal conductor remains primitive, squarefree and rough enough for the fixed-power complete-sum saving. Tiny primes therefore need not be killed by a codimension projection.

The resulting contradiction combines the strong rank geometry of MC-378 with the `log log y` analytic ceiling of MC-379: for an absolute nonoptimized constant `c>0`, every exact endpoint package satisfies

`log P/log y >= c min{sqrt(R/log(R+2)), log log y}`.

Equivalently, a hypothetical bound `P<=y^A` is incompatible with `A^2=o(R)` together with `2^(C A) log log y=o(log y)`. The important structural improvement is not merely the displayed minimum: nuisance source coordinates can sometimes be **packed into an early exact factor rather than deleted**, preserving the rank budget for the terminal cancellation mechanism.

The remaining question is now closer to the intrinsic endpoint architecture. Which losses in the terminal differencing/character-sum argument are unavoidable, and can the `log log y` analytic ceiling or the `sqrt(R/log R)` rank scale be sharpened without changing the exact endpoint representation? A stronger theorem should identify a genuinely new source-specific saving, not reintroduce a pruning loss already removed by MC-380.

## Keep resolution, source incidence, conductor, common-radical cost and bias amplitude distinct

The current resource ledger separates exact-real subset-sum conditioning, finite-resolution quotienting, `l1` worst-case shell displacement, `l2` average dephasing stability, source-incidence balance, incidence-signature delocalization, package conductor, minimum primitive conductor, common-radical size and endpoint bias amplitude. These are not interchangeable.

MC-377--MC-380 are especially important for interpretation: lower bounds on individual primitive conductors inside a hypothetical fixed-power package are weaker than proving that the **entire common source package must escape the polynomial hierarchy at a quantitative moving rate**. MC-380 additionally separates small-coordinate handling from rank loss: a bad local factor need not consume codimension if it can be absorbed before the cancellation step that actually requires roughness.

None of these source-cost bounds imply Möbius cancellation or establish an optimal source tariff. The endpoint argument must still specify which physical quotient is observed and how its source-cost obstruction reaches a destination quantity relevant to `M(x)`.

## Repair probabilistic comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

The source-cost results add another control: a plausible endpoint comparator must not hide the exact architecture inside a common source package whose cost violates MC-377--MC-380. Conditional finite-power models may still diagnose which modes or amplitudes would become expensive, but they cannot be used as evidence that an exact endpoint can actually inhabit that source regime.