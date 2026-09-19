# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve each shrinking target against the actual source mesh

**Linked intuitions:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-424 isolate a nested critical hierarchy in the full left-tail determinant. Fixed derivative shifts close to a positive Cauchy limit, moving derivative depth introduces `s_n/n`, the complete partition family detects the critical value `2`, and the effective critical coordinate becomes

`b_n(a)=a n^(s_n/n-2)`.

At square collision fibers `b_n->m^2`, equality of exponential saddle rates is not enough. Rectangle balance is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and AF-424 shows that the derivative-offset term remains load-bearing before limits are taken.

AF-425--AF-428 expose the first source-realizability split. On the critical displaced branch the formal cancellation target lives in the integer depth `d_n=s_n-2n`. Exact square amplitude has no solution at the required second-order precision, while the moving-amplitude exceptional set is simultaneously Lebesgue-null/Hausdorff-thin and residual. Metric genericity, Baire genericity and pointwise membership are therefore different questions.

AF-429--AF-430 move above the critical transition. If `q_n=s_n/n->sigma>2`, full-height rectangles have a moving saddle

`R_n=a^(1/q_n)n^(1-2/q_n)`,

and adjacent integer packets are comparable only when the real balance center `tau_n~R_n` lies within `O(R_n/n)` of `Z`. Complete residual-packet resummation does not enlarge that aperture; it only shifts the refined balance center by `Theta(R_n/n^2)`.

AF-431 now shows that the first supercritical window is **source-sensitive rather than intrinsically obstructed**. For every fixed rational density `q=u/v>2` on its exact source progression `n=vk, s=uk`, the saddle is eventually increasing with

`tau'(n)=((q-2)/q) R(n)/n (1+o(1))`.

Its inter-source spacing is therefore of the same order as the AF-429 comparability window. A monotone crossing argument forces infinitely many `O(R_n/n)` integer hits; when `v` is odd the same remains true on an odd-`n` sign-alternating progression. The first lattice gate is automatic for this class, but the packet-corrected `R_n/n^2` target is still a factor `n` finer than the source step.

The live question is consequently conditional on the source class. For a distinguished or varying source sequence, first compare its induced saddle mesh with the target aperture: monotone divergent sampling with mesh `O(R_n/n)` already passes the first gate, whereas coarser jumps or additional compatibility conditions can still obstruct it. For fixed rational supercritical densities, stop reproving first-window membership and attack the genuinely finer `R_n/n^2` packet alignment together with the omitted determinant sectors.

## Keep physical locality separate from transformed criticality

Source-local statements should be formulated in the physical arithmetic coordinate before being interpreted through transforms, determinants or saddle geometry. A transform may make a critical exponent or collision surface visible while hiding the discrete source constraints that decide whether that surface is reachable.

The reusable control is to pull every proposed tuning back through the exact source map and compare **source mesh to required target width at the same asymptotic order**. AF-426 shows that a natural critical fiber can be empty at the required precision. AF-427--AF-428 show that residuality and measure-zero thinness do not decide a distinguished point. AF-429--AF-430 show that a smooth supercritical saddle can still demand shrinking integer accuracy. AF-431 adds the converse control: when the allowed source mesh itself shrinks at the required first-window rate, the lattice is no obstruction at that scale. Continuous optimization, category, measure, source sampling and packet corrections are separate currencies.