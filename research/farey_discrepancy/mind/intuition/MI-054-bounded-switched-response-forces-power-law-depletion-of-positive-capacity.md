# MI-054 — Bounded switched response depletes positive capacity; monotone response sharpens the rate to inverse-linear

**Evidence level:** exact quantitative synthesis from [FD-257](../../findings/FD-257-bounded-switched-rows-force-polynomial-nonnegative-capacity-depletion.md) and [FD-259](../../findings/FD-259-monotone-divisor-response-forces-sharp-inverse-linear-capacity-depletion.md), strengthening the qualitative positive-cushion boundary of FD-230.

Positivity already turns bounded switched response into a quantitative loss of source capacity. If `0<=b_d<=Cd` and the period-three switched rows remain uniformly bounded, FD-257 proves that the normalized coefficient mass on the dyadic band `[2^k,2^(k+1))` is at most

`A(C+B)(23/24)^k`.

Equivalently, at divisor scale `x=2^k`, the relative band capacity is `O((C+B)x^(-beta))` with `beta=log_2(24/23)>0`. This rate is not sharp in the full positive class, but it is unconditional under the stated envelope and switched-row hypotheses.

FD-259 identifies a source-side subclass where the exact rate becomes much stronger. Write `g=mu*b`. If in addition `g(n)>=0`, then the divisor response

`(A b)(m)=sum_(n<=m) g(n)`

is monotone. The order-one and neighboring order-four switched stencils then trap every dyadic response increment by `O(B)`. Consequently

`sum_(n<=x)b_n = O((C+B)x)`

and the relative mass of a dyadic band is `O((C+B)/x)`. The exponent `1` is sharp in this monotone-response cone: the constant cushion `b_n=1` has relative dyadic capacity of order `1/x` while all switched rows vanish.

This separates two levels of positivity. Nonnegativity of `b` alone gives the FD-257 fixed-power depletion. Nonnegativity of the Möbius increments `mu*b` removes oscillation in the response itself and upgrades the aggregate loss to inverse-linear. A positive cushion seeking polynomially more slack than the common-cushion scale must therefore leave the monotone-response cone and create sign changes in `mu*b`; raw positivity of the source coefficients does not prevent that possibility.

For the FD-226 scale-adapted reservoirs, after normalizing by `L_N=N/(D log N)`, the monotone-response subclass can use only `O(L_N x)` aggregate occupancy in a divisor band of scale `x`, against available capacity `asymp L_N x^2`. This closes any attempt to recover a polynomial fraction of the growing cell capacity while keeping `mu*b>=0` and bounded switched response.

The decisive remaining comparison is still source-specific. The actual Mertens repair is not known to lie in the monotone-response cone, so FD-259 does not replace the need to quantify the slack it really requires. If the repair necessarily forces signed Möbius increments, the relevant frontier returns to the weaker FD-257 class or to a new signed structural estimate.

**Boundary.** FD-259's extra hypothesis `mu*b>=0` is load-bearing and is not automatic for a physical nonnegative occupancy. The inverse-linear rate is an exact aggregate statement for that subclass, not an RH statement and not a universal positive-cushion theorem. FD-257 remains the general bounded-switched positive-capacity control.
