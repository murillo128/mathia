# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

Arithmetic fidelity is not a scalar property of a representation. What matters is which source distinctions survive the exact observation map, at what scale they survive, and whether the admissible arithmetic source can actually occupy the formal directions that an asymptotic or inverse argument treats as continuously tunable.

The line should therefore keep source geometry, observation fidelity, conditioning, asymptotic scale and admissible parameter lattice separate. A formal coordinate that exists in the ambient analytic model is useful only after its pullback to the physical source class has been identified.

## Resolve the metrically thin exceptional off-square source-lattice branch

**Linked intuitions:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-424 isolate a nested critical hierarchy in the full left-tail determinant. Fixed derivative shifts close to a positive Cauchy limit, moving derivative depth introduces the coordinate `s_n/n`, the complete partition family detects the critical value `2`, and the effective source/derivative coordinate becomes

`b_n(a)=a n^(s_n/n-2)`.

At the square collision fibers `b_n->m^2`, equality of exponential saddle rates is not enough. Rectangle balance is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and AF-424 shows that the derivative-offset term `m alpha_n` with `alpha_n=(s_n-2n)/n` is load-bearing before limits are taken.

AF-425 pushes the same odd square fiber one order further and exposes the source-realizability gate. Its continuously tuned cancellation equation lives in the integer coordinate `d_n=s_n-2n`; adjacent admissible depths are separated by `~log n` in the corrected target function while the required alignment window shrinks by inverse powers of `n`.

AF-426 resolves the exact square-amplitude fiber pointwise. On `a=m^2`, bounded complete-packet ratio forces `d_n=-1` eventually, and at that only admissible depth the packet ratio tends to `m K_m>1`. Hence the ratio cannot approach one and the `o(n^-2)` shrinking target has no solutions on any exact square-amplitude fiber.

AF-427 resolves most of the displaced branch metrically. Writing the amplitude displacement as `A=log(m^2/a)`, source compatibility is `d log n/n -> A`. On every compact `A`-interval only `O(n/log n)` integer depths are admissible at scale `n`, while the second-order cancellation target is transverse to `A` with derivative of size `~n`; an `n^-2` target window therefore occupies only `O(n^-3)` amplitude width per source cell. The resulting limsup cover has finite total length and `s`-mass for every `s>2/3`. Thus the amplitudes admitting infinitely many second-order hits form a set of Lebesgue measure zero and Hausdorff dimension at most `2/3`.

The live source-lattice question is no longer generic off-square tuning. It is **pointwise exceptional-set arithmetic**: determine whether any distinguished amplitudes forced by the original source construction can lie in AF-427's thin limsup set, and whether the exact moving centers admit infinitely many `o(n^-2)` hits there. Beyond-all-orders packet analysis is relevant only after a specific exceptional amplitude survives this gate. Lower saddles, tall-column families, the omitted-`1` sector and the genuinely supercritical regime remain separate.

## Keep physical locality separate from transformed criticality

Source-local statements should be formulated in the physical arithmetic coordinate before they are interpreted through transforms, determinants or saddle geometry. A transform may make a critical exponent or collision surface visible while hiding the discrete source constraints that decide whether the surface is reachable.

The reusable control is to pull every proposed critical tuning back through the exact source map. If the pullback is discrete, constrained or nonuniform, its spacing and admissible quantifier are part of the mathematical claim rather than a technical afterthought. AF-426 adds the pointwise warning that a natural collision fiber can be empty at the required precision; AF-427 adds the metric warning that allowing the fiber to drift continuously still leaves the infinitely recurring source hits confined to a Hausdorff-thin exceptional set.