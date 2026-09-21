# MI-054 — Bounded switched response forces power-law depletion of positive capacity

**Evidence level:** exact quantitative synthesis from [FD-257](../../findings/FD-257-bounded-switched-rows-force-polynomial-nonnegative-capacity-depletion.md), strengthening the qualitative positive-cushion boundary of FD-230.

Positivity turns bounded switched response into a quantitative loss of source capacity. If `0<=b_d<=Cd` and the period-three switched rows remain uniformly bounded, FD-257 proves that the normalized coefficient mass on the dyadic band `[2^k,2^(k+1))` is at most

`A(C+B)(23/24)^k`.

Equivalently, at divisor scale `x=2^k`, the relative band capacity is `O((C+B)x^(-beta))` with `beta=log_2(24/23)>0`. The particular exponent is not claimed sharp; the durable fact is the existence of a fixed positive power.

Two independent mechanisms combine. The normalized switched recurrence is strictly stable, so bounded unnormalized rows force the normalized response to decay geometrically. Nonnegativity then converts the Mertens tail relation into a one-sided convolution inequality whose weighted kernel has total mass below one. Signed cancellation cannot imitate this step: positivity is the resource that turns response stability into capacity depletion.

This sharply separates the physical source problem from the signed exact-omission problem. A positive cushion that remains invisible at bounded switched scale cannot retain slowly decaying relative slack such as `1/log x` on every deep band, even though signed coefficient profiles can remain much larger.

The decisive remaining comparison is one-sided: quantify how much nonnegative slack the concrete Mertens repair must consume on deep bands. If that requirement eventually exceeds the FD-257 power-law ceiling, the current positive reservoir route is obstructed; without such a lower bound, the depletion theorem alone does not close the repair.

**Boundary.** The result assumes a linear nonnegative envelope and the specified bounded switched rows. It is a source-side necessary condition, not an RH statement, and it does not establish the required lower bound for the canonical correction. The same rate applies causally to eligible bands in finite growing blocks.