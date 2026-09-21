# MI-054 — Bounded switched response depletes positive capacity; finite arithmetic sharpens the general exponent past one half

**Evidence level:** exact quantitative synthesis from [FD-257](../../findings/FD-257-bounded-switched-rows-force-polynomial-nonnegative-capacity-depletion.md), [FD-259](../../findings/FD-259-monotone-divisor-response-forces-sharp-inverse-linear-capacity-depletion.md), and [FD-260](../../findings/FD-260-finite-mertens-blocks-push-nonnegative-switched-depletion-past-square-root-scale.md), strengthening the qualitative positive-cushion boundary of FD-230.

Positivity already turns bounded switched response into a quantitative loss of source capacity. If `0<=b_d<=Cd` and the period-three switched rows remain uniformly bounded, FD-257 reduces the dyadic band masses to a positive Volterra recurrence whose kernel is built from dyadic Mertens maxima. The original proof retained only the first blocks exactly and then used the trivial bound `|M(q)|<=q`, producing a small positive depletion exponent.

FD-260 shows that the weak numerical exponent was mostly a bookkeeping artifact rather than a structural limit. Recomputing only the first nineteen dyadic Mertens blocks exactly makes the same positive Volterra kernel contract at weight `r=2/3`; all later blocks may still be bounded trivially. Consequently the relative coefficient mass on a divisor band of scale `x` satisfies

`O((C+B)x^(-log_2(3/2))) = O((C+B)x^(-0.58496...))`.

No sign assumption on `mu*b` is used. The same kernel method cannot contract as far as `r=0.65` from the exact prefix alone, so this calculation also separates the proved source bound from an unsupported claim of an inverse-linear rate. The important reusable lesson is that a finite amount of exact arithmetic information can materially strengthen a global positive recurrence even when the infinite tail remains under a trivial estimate.

FD-259 identifies a genuinely different source-side subclass. If `g=mu*b` is nonnegative, the divisor response is monotone, neighboring switched stencils trap every dyadic response increment, and

`sum_(n<=x)b_n = O((C+B)x)`.

The relative dyadic capacity is then `O((C+B)/x)`, and exponent `1` is sharp in that monotone-response cone. Thus nonnegativity of `b` plus bounded switched response already forces more-than-square-root depletion after FD-260, while nonnegativity of the Möbius increments supplies an additional structural mechanism that upgrades the rate to inverse-linear.

For the FD-226 source geometry, the practical frontier is therefore narrower. Any physical nonnegative repair with bounded switched rows has less than inverse-square-root relative capacity on sufficiently deep bands, even if `mu*b` changes sign. If the actual repair also lies in the monotone-response cone, only inverse-linear capacity remains. A complete obstruction still needs a lower bound showing that the concrete repair consumes more positive slack than the applicable ceiling; neither FD-257 nor FD-260 supplies that source-specific lower bound.

**Boundary.** FD-260 sharpens the existing positive-kernel mechanism; it does not prove the optimal exponent for arbitrary signed `mu*b`, and its `0.65<r_c<2/3` bracket concerns only that kernel method. FD-259's hypothesis `mu*b>=0` is load-bearing. None of these depletion estimates proves an RH statement or shows that the actual Mertens repair satisfies the needed lower bound.
