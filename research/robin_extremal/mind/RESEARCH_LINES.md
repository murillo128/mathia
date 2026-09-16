# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the terminal moment hierarchy with both growing order and growing precision

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-033-growing-moment-order-requires-a-factorial-precision-staircase`.

RE-153 turns the source side of a regular self-tangent Robin counterexample into the normalized Pareto-weighted Chebyshev-deficit average. RE-154--RE-158 progressively show that terminal source modifications can move this exact destination at order one unless count, first placement information and Chebyshev mass are controlled at the relevant shrinking scale.

RE-159 gives the fixed-order hierarchy: exact matching through order `r-1` moves the first unresolved influence to order `r`. RE-160 supplies the growing-order correction. With `eta_p=epsilon_PNT(p)` and exact lower-moment matching, the factorial stability width is

`tau_r=(r! eta_p)^(1/r)`,

and the crossover is `L asymp r eta_p^(1/r)` up to universal constants.

RE-161 shows that **moment order alone is not a fidelity resource**. With approximate lower moments, leakage enters before the factorial remainder with weight `b_1~1`, `b_k~1/k!`. The robust cost is

`E_r=sum_(k<r) |mu_k|/k!`.

Retaining the `RE-160` gain requires `E_r=O(L^r/r!)`; at `L=tau_r` this is the factorial precision staircase `E_r=O(eta_p)`. Even uniform relative errors tending to zero simultaneously across all moment orders can leave order-one Robin ambiguity.

The source-side question is now exact: does the ordinary-prime/CA structure provide the required **weighted precision profile**, or a signed arithmetic coupling that cancels `sum b_k mu_k`, at a cost below the destination threshold? Merely retaining more moments, or proving qualitative moment convergence, is exhausted as a route.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch must still control target-conditioned exceptional geometry rather than typical-center averages.

## Keep source-moment and zero-packet gates distinct

RE-153--RE-161 expose a source-side hierarchy of terminal resources: supply, placement, exact moment order, factorial remainder and now approximate-moment precision. RE-151--RE-152 give a zero-side matched obstruction to one reciprocal-scale observation route. Neither subsumes the other. Progress should be credited only when it changes the exact quantity consumed by its own destination.
