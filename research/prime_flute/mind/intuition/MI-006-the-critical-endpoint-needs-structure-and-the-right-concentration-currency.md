# MI-006 — The lowest finite-seam pole kills every bare supercritical separated weight

**Evidence level:** exact positive mass decomposition, Green asymptotics, and lowest-pole obstruction through PF-268

## Core intuition

The finite seam does not inherit the fixed-axis `R>1` smoothing margin in the bare separated endpoint norm. The reason is not a difficult high-mass summation: positivity makes the very first odd mass pole permanent, and its two-index Green asymptotic leaves an order `N^-2` floor on proportional separated blocks.

Therefore any successful endpoint argument must perform the normalized Robin/spatial operation before asking for a supercritical weight, so that the lowest-pole contribution is changed or cancelled in the actual composed map.

## Strongest justified principle

PF-258--PF-260 establish the intrinsic-six tangent and the fixed-axis fractional window. PF-261 expresses the finite seam as a positive odd-mass mixture, and PF-262--PF-267 obtain the fixed-mass asymptotics plus a path identity coupling sharp amplitude and decay uniformly.

PF-268 uses those results adversarially. Since all massive Green terms have the same sign, the lowest pole alone supplies a lower bound of order `N^-2` on large proportional separated blocks. After multiplying the input by `N^R`, a normalized block witness grows like `N^(R-1)`, so the separated bare finite-seam operator is unbounded for every `R>1`. The same holds with the physical `K_s^0` weight and any fixed high-mode cutoff.

## Program consequence

Stop trying to recover a strict supercritical margin from the bare mass ladder. Estimate the combined normalized Robin map of PF-257 and the spatially separated Robin--Poisson transport of PF-243 before endpoint weighting. A viable mechanism must explain exactly how that composition removes, cancels, or redistributes the positive lowest-pole floor.

## Counterevidence / boundary

PF-268 does not rule out the combined normalized Robin transform, separated Poisson propagation, the exact endpoint `R=1`, or boundedness for `R<1`. The obstruction is specific to demanding `R>1` from the unnormalized finite-seam crossover on the separated cone.

## Epistemic status

**Exact route closure for bare finite-seam supercritical weighting; the remaining opportunity lies in structure applied before the endpoint weight, not in sharper mass summation.**

## Falsification criterion

Produce a bounded `R>1` separated bare finite-seam operator under the same PF-268 definitions, or show that one of the positivity/asymptotic hypotheses used to obtain the lowest-pole block floor fails for the physical seam.