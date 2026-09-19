# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve shrinking targets only after the source has selected the parameter

**Linked intuition:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-424 isolate a nested critical hierarchy in the full left-tail determinant. Fixed derivative shifts close to a positive Cauchy limit, moving derivative depth introduces `s_n/n`, the complete partition family detects the critical value `2`, and the effective critical coordinate becomes

`b_n(a)=a n^(s_n/n-2)`.

At square collision fibres `b_n->m^2`, equality of exponential saddle rates is not enough. Rectangle balance is controlled by `Xi_(n,m)`, complete packets add an inverse-`n` drift, and AF-424 shows that the derivative-offset term remains load-bearing before limits are taken.

AF-425--AF-428 expose the first source-realizability split. On the critical displaced branch the formal cancellation target lives in the integer depth `d_n=s_n-2n`. Exact square amplitude has no solution at the required second-order precision, while the moving-amplitude exceptional set is simultaneously Lebesgue-null/Hausdorff-thin and residual. Metric genericity, Baire genericity and pointwise membership are therefore different questions.

AF-429--AF-431 move above the critical transition. If `q_n=s_n/n->sigma>2`, full-height rectangles have a moving saddle

`R_n=a^(1/q_n)n^(1-2/q_n)`,

and adjacent integer packets are comparable only when the real balance center `tau_n~R_n` lies within `O(R_n/n)` of `Z`. Complete residual-packet resummation does not enlarge that aperture; it shifts the first refined balance center only by `Theta(R_n/n^2)`. For every fixed rational density `q=u/v>2` on its exact source progression `n=vk, s=uk`, AF-431 shows that the saddle mesh itself is `Theta(R_n/n)`, so monotone crossing forces infinitely many first-window hits; when `v` is odd the same remains true on an odd sign-alternating progression.

AF-432 classifies the factor-`n` refinement that AF-431 left open at the level of amplitude genericity. For the packet-corrected center

`hat(tau)_n(a)=tau_n(a)+a e^q R_n(a)/n^2`,

the amplitudes hitting `dist(hat(tau)_n(a),Z)=o(R_n/n^2)` infinitely often form a dense `G_delta`, but have Lebesgue measure zero and Hausdorff dimension at most `1-1/q`. First-order complete-packet balance can occur only inside this set.

AF-433 changes the order of the remaining question. In the canonical source chain, `x_n(c)=c/n` allows every `c>0`, and `a=c^2/(4pi^2)` is a bijective coordinate on that free probe family. Therefore AF-432 classifies exceptional **probe paths**, not distinguished intrinsic source amplitudes. The square amplitudes are likewise target-side saddle collisions, not source-side selections.

The live question is now upstream of pointwise shrinking-target membership: **find a source-intrinsic rule that selects `c` or `a` independently of the desired saddle cancellation or exceptional-set outcome, or prove that the present construction supplies no such selector.** Only after a selector is established does it become meaningful to prove or disprove membership of its selected amplitude in the AF-432 target. Without that provenance step, further pointwise amplitude analysis refines the geometry of an externally tunable probe family rather than arithmetic fidelity.

## Keep physical locality separate from transformed criticality

Source-local statements should be formulated in the physical arithmetic coordinate before being interpreted through transforms, determinants or saddle geometry. A transform may make a critical exponent or collision surface visible while hiding both the discrete source constraints and whether the supposedly critical parameter was selected by the source at all.

The reusable control is to pull every proposed tuning back through the exact source map in two steps. First determine whether the parameter is source-intrinsic or freely chosen in the probe/normalization. If it is intrinsic, compare its admissible source mesh with the required target width at the same asymptotic order. AF-426 shows that a natural critical fibre can be empty at the required precision. AF-427--AF-428 and AF-432 show that residuality and metric thinness can coexist and therefore do not decide a distinguished point. AF-429--AF-431 show that a smooth supercritical saddle can be sampled finely enough to pass one lattice gate while missing the next by a factor `n`. AF-433 shows that even this pointwise hierarchy is not source-discriminating until the amplitude itself has independent provenance. Continuous optimization, category, measure, source selection, source sampling and packet corrections are separate currencies.
