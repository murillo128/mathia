# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

Arithmetic fidelity is not a scalar property of a representation. What matters is which source distinctions survive the exact observation map, at what scale they survive, and whether the admissible arithmetic source can actually occupy the formal directions that an asymptotic or inverse argument treats as continuously tunable.

The line should therefore keep source geometry, observation fidelity, conditioning, asymptotic scale and admissible parameter lattice separate. A formal coordinate that exists in the ambient analytic model is useful only after its pullback to the physical source class has been identified.

## Resolve shrinking integer windows before promoting continuous left-tail saddles

**Linked intuitions:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-424 isolate a nested critical hierarchy in the full left-tail determinant. Fixed derivative shifts close to a positive Cauchy limit, moving derivative depth introduces the coordinate `s_n/n`, the complete partition family detects the critical value `2`, and the effective source/derivative coordinate becomes

`b_n(a)=a n^(s_n/n-2)`.

At the square collision fibers `b_n->m^2`, equality of exponential saddle rates is not enough. Rectangle balance is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and AF-424 shows that the derivative-offset term `m alpha_n` with `alpha_n=(s_n-2n)/n` is load-bearing before limits are taken.

AF-425 exposes the source-realizability gate. Its continuously tuned second-order cancellation equation lives in the integer coordinate `d_n=s_n-2n`; adjacent admissible depths are separated by `~log n` in the corrected target while the required alignment window shrinks by inverse powers of `n`. AF-426 resolves every exact square-amplitude fiber pointwise: bounded complete-packet ratio forces `d_n=-1` eventually, and at that only admissible depth the packet ratio tends to `m K_m>1`, so the `o(n^-2)` target has no solutions there.

AF-427 resolves the displaced critical branch metrically. Writing `A=log(m^2/a)`, source compatibility is `d log n/n -> A`. On compact `A`-ranges there are only `O(n/log n)` admissible integer depths at scale `n`, while transversality makes an `n^-2` target window only `O(n^-3)` wide per source cell. The infinitely recurring exceptional set therefore has Lebesgue measure zero and Hausdorff dimension at most `2/3`. AF-428 supplies the complementary category statement: the same set is a dense `G_delta`, hence residual. Pointwise membership of a distinguished source amplitude remains undecided by either notion of genericity.

AF-429 opens the genuinely supercritical side without removing the source-lattice obstruction. If `q_n=s_n/n->sigma>2`, full-height rectangles develop a moving saddle at

`R_n=a^(1/q_n)n^(1-2/q_n)`,

with logarithmic profile `sigma t(1-log t)` at widths `r~tR_n`. The exact adjacent-width ratio crosses one at a real center `tau_n~R_n` with slope of order `n/R_n`. Neighbouring integer rectangles can therefore be comparable only if

`dist(tau_n,Z)=O(R_n/n)=O(n^(-2/sigma+o(1)))`.

AF-430 closes the first nonrectangular escape inside that candidate window. Conditional on an integer width reaching `|r_n-tau_n|=O(R_n/n)`, the complete residual packets attached to the two adjacent rectangles both converge to `exp(-a e^sigma)`, while their relative logarithmic drift is only `sigma a e^sigma/n+o(n^-1)`. The real complete-packet balance point is shifted from `tau_n` by only `a e^sigma R_n/n^2(1+o(1))`, a factor `1/n` below the already shrinking integer-comparability window. Nonrectangular residual shapes therefore do not broaden the source lattice gate.

So both the critical displaced branch and the supercritical moving saddle end at **shrinking integer targets** before signed cancellation is available. In the supercritical branch this remains true after complete residual-packet resummation. The live question is pointwise arithmetic recurrence for the actual source-forced parameters, followed—only on any surviving subsequence—by the finer `R_n/n^2` packet correction and control of omitted determinant sectors. Continuous saddle existence, residuality or almost-everywhere statements are insufficient substitutes.

## Keep physical locality separate from transformed criticality

Source-local statements should be formulated in the physical arithmetic coordinate before they are interpreted through transforms, determinants or saddle geometry. A transform may make a critical exponent or collision surface visible while hiding the discrete source constraints that decide whether the surface is reachable.

The reusable control is to pull every proposed critical tuning back through the exact source map. If the pullback is discrete, constrained or nonuniform, its spacing and admissible quantifier are part of the mathematical claim rather than a technical afterthought. AF-426 adds the pointwise warning that a natural collision fiber can be empty at the required precision. AF-427--AF-428 add that the same moving target can be residual while still Lebesgue-null and Hausdorff-thin. AF-429 adds that even a smooth supercritical saddle can require lattice accuracy `R_n/n=o(1)` before adjacent signed sectors become comparable. AF-430 shows that summing the complete residual partition packet preserves that scale and moves the refined balance center only at `R_n/n^2`. Category, measure, continuous optimization, packet resummation and pointwise source membership are different currencies.
