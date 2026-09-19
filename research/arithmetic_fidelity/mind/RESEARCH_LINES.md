# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

Arithmetic fidelity is not a scalar property of a representation. What matters is which source distinctions survive the exact observation map, at what scale they survive, and whether the admissible arithmetic source can actually occupy the formal directions that an asymptotic or inverse argument treats as continuously tunable.

The line should therefore keep source geometry, observation fidelity, conditioning, asymptotic scale and admissible parameter lattice separate. A formal coordinate that exists in the ambient analytic model is useful only after its pullback to the physical source class has been identified.

## Resolve the residual-null exceptional off-square source-lattice branch

**Linked intuitions:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-424 isolate a nested critical hierarchy in the full left-tail determinant. Fixed derivative shifts close to a positive Cauchy limit, moving derivative depth introduces the coordinate `s_n/n`, the complete partition family detects the critical value `2`, and the effective source/derivative coordinate becomes

`b_n(a)=a n^(s_n/n-2)`.

At the square collision fibers `b_n->m^2`, equality of exponential saddle rates is not enough. Rectangle balance is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and AF-424 shows that the derivative-offset term `m alpha_n` with `alpha_n=(s_n-2n)/n` is load-bearing before limits are taken.

AF-425 exposes the source-realizability gate. Its continuously tuned second-order cancellation equation lives in the integer coordinate `d_n=s_n-2n`; adjacent admissible depths are separated by `~log n` in the corrected target while the required alignment window shrinks by inverse powers of `n`. AF-426 then resolves every exact square-amplitude fiber pointwise: bounded complete-packet ratio forces `d_n=-1` eventually, and at that only admissible depth the packet ratio tends to `m K_m>1`, so the `o(n^-2)` target has no solutions there.

AF-427 resolves the displaced branch metrically. Writing `A=log(m^2/a)`, source compatibility is `d log n/n -> A`. On compact `A`-ranges there are only `O(n/log n)` admissible integer depths at scale `n`, while transversality makes an `n^-2` target window only `O(n^-3)` wide per source cell. The infinitely recurring exceptional set therefore has Lebesgue measure zero and Hausdorff dimension at most `2/3`.

AF-428 supplies the complementary category statement. For each fixed packet index `m`, the same exceptional set is a dense `G_delta`, hence residual. It is therefore simultaneously topologically generic and metrically thin. This does not contradict AF-426: `A=0` is excluded pointwise even though exceptional amplitudes occur arbitrarily close to it. Nor does residuality decide any distinguished amplitude forced by the original source.

The live source-lattice question is consequently **pointwise exceptional-set arithmetic**, not generic off-square tuning. Neighborhood, openness or perturbative-stability arguments cannot exclude the branch, and almost-everywhere/metric arguments cannot decide a fixed source-forced amplitude. The useful next step is to prove membership or nonmembership in the exact moving-center shrinking target for a concrete distinguished amplitude. Beyond-all-orders packet analysis becomes relevant only after such an amplitude survives this gate. Lower saddles, tall-column families, the omitted-`1` sector and the genuinely supercritical regime remain separate.

## Keep physical locality separate from transformed criticality

Source-local statements should be formulated in the physical arithmetic coordinate before they are interpreted through transforms, determinants or saddle geometry. A transform may make a critical exponent or collision surface visible while hiding the discrete source constraints that decide whether the surface is reachable.

The reusable control is to pull every proposed critical tuning back through the exact source map. If the pullback is discrete, constrained or nonuniform, its spacing and admissible quantifier are part of the mathematical claim rather than a technical afterthought. AF-426 adds the pointwise warning that a natural collision fiber can be empty at the required precision. AF-427--AF-428 add a second warning: the same moving target can be residual while still Lebesgue-null and Hausdorff-thin. Category, measure and pointwise source membership are different currencies and none can substitute for the exact arithmetic membership question.