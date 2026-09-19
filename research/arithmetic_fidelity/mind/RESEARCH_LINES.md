# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

Arithmetic fidelity is not a scalar property of a representation. What matters is which source distinctions survive the exact observation map, at what scale they survive, and whether the admissible arithmetic source can actually occupy the formal directions that an asymptotic or inverse argument treats as continuously tunable.

The line should therefore keep source geometry, observation fidelity, conditioning, asymptotic scale and admissible parameter lattice separate. A formal coordinate that exists in the ambient analytic model is useful only after its pullback to the physical source class has been identified.

## Resolve source-lattice realizability on tuned square-transition fibers

**Linked intuitions:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-424 isolate a nested critical hierarchy in the full left-tail determinant. Fixed derivative shifts close to a positive Cauchy limit, moving derivative depth introduces the coordinate `s_n/n`, the complete partition family detects the critical value `2`, and the effective source/derivative coordinate becomes

`b_n(a)=a n^(s_n/n-2)`.

At the square collision fibers `b_n->m^2`, equality of exponential saddle rates is not enough. Rectangle balance is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and AF-424 shows that the derivative-offset term `m alpha_n` with `alpha_n=(s_n-2n)/n` is load-bearing before limits are taken.

AF-425 pushes the same odd square fiber one order further and changes the live obstruction. The complete adjacent-packet logarithm has a second-order cancellation law of the form

`n^2 Omega_(n,m)+n B_1(alpha_n)+B_2(alpha_n)->0`,

but the tuning variable is not continuous: `d_n=s_n-2n` is an integer source coordinate. In the exact corrected target function, changing `d_n` by one changes the cancellation coordinate by

`log(n/m)+m/n+O(n^-2) ~ log n`.

Thus a formal continuous saddle solution does not imply that an admissible source path realizes it. The tuned branch is now an inhomogeneous shrinking-target problem on an increasingly coarse source lattice. AF-425 makes the scale explicit: an `o(n^-1)` target requires fractional alignment at width `o((n log n)^-1)`, and an `o(n^-2)` target requires `o((n^2 log n)^-1)`.

The current question is therefore not merely to compute another formal packet coefficient. It is to determine whether the integer derivative-depth source can hit the moving cancellation target often enough, rarely enough, or never at the precision required to suppress the exponentially large tied saddle. Any answer must distinguish an exact arithmetic avoidance/equidistribution statement from a continuous asymptotic saddle calculation. Lower saddles, tall-column families and beyond-all-orders residuals remain separate even if source-lattice alignment occurs.

## Keep physical locality separate from transformed criticality

Source-local statements should be formulated in the physical arithmetic coordinate before they are interpreted through transforms, determinants or saddle geometry. A transform may make a critical exponent or collision surface visible while hiding the discrete source constraints that decide whether the surface is reachable.

The reusable control is to pull every proposed critical tuning back through the exact source map. If the pullback is discrete, constrained or nonuniform, its spacing and admissible quantifier are part of the mathematical claim rather than a technical afterthought.
