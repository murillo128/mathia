# MI-055 — Derivative depth, source selection, transport provenance, conditioning, and probe amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-437](../../findings/AF-437-recursive-shell-peeling-amplifies-earlier-errors-exponentially.md).

AF-416--AF-424 show that the reciprocal-order left-tail determinant has more than one scaling coordinate. A fixed derivative shift closes to a positive Cauchy limit, but moving depth enters through `s_n/n`; the complete partition family detects the critical value `2`, and in the critical window probe amplitude and depth combine as

`b_n(a)=a n^(s_n/n-2)`.

Near square values `b=m^2`, full-column rectangles can tie at leading exponential order while exact rectangle ratios, complete-packet drift and the discrete derivative offset remain visible at finer scales. AF-425--AF-432 show that continuous saddle tuning is therefore not enough: the physical depth variable is integral, exact-square fibres miss the required second-order cancellation, and the packet-corrected target lives at a finer scale than the first saddle window.

AF-433--AF-435 separate source selection from downstream transport. The reciprocal-order family `x_n(c)=c/n` permits every `c>0`, while coefficient-root neutrality selects the Taylor radius, hence `c=2pi` and `a=1` for the Bernoulli source, without inspecting determinant packets. That selector is genuinely source-native, but the present determinant has already aggregated shell labels into zeta factors before packet labels form, and the selected square fibre fails the adjacent-packet cancellation of AF-426.

AF-436 shows that the **exact even Euler coefficients have not lost the shell ladder**. After normalization,

`s_k=(-1)^k k R^(2k)c_(2k)=zeta(2k)=sum_(j>=1) j^(-2k)`.

Exact peeling below shell `m` leaves `r_(m,k)=sum_(j>=m)j^(-2k)` with `m^(2k)r_(m,k)->1`, so the next shell can be recovered in exact arithmetic.

AF-437 supplies the missing stability calculation for that representation. If earlier shell `j` is peeled with relative location error `eta_(j,k)` and weight error `omega_(j,k)`, while the observed moment has additive error `e_k`, the target-scale error budget is controlled by

`m^(2k)|e_k| + sum_(j<m)(m/j)^(2k)(|omega_(j,k)| + k|eta_(j,k)|)`.

For worst-case independent peeling errors, stable shell-`m` recovery therefore needs `|omega_(j,k)|=o((j/m)^(2k))` and `|eta_(j,k)|=o(k^(-1)(j/m)^(2k))`. If the common radius is estimated rather than supplied exactly, its relative error must be `o(m^(-2k)/k)` along this normalization route. Deeper provenance is not merely small; recursive reconstruction amplifies every earlier-shell error exponentially relative to the new target scale.

The reusable order is now six-stage. **First establish source selection. Second identify the exact source carrier and its resolution scale. Third price the conditioning of any inverse used to expose that carrier. Fourth verify that the downstream representation transports rather than aggregates it. Fifth compare the physical source mesh with the target aperture. Sixth test the selected point rather than an optimized surrogate.** The current branch passes source selection and exact shell retention, but the present determinant fails shell-resolved transport and the selected square fibre fails its adjacent-packet mechanism.

**Boundary.** AF-437 is a sharp conditioning statement for sequential dominant-shell peeling, not a universal minimax lower bound for every joint Prony/Hankel or symbolic reconstruction. Exact symbolic shell locations and exact `R=2pi` remove the corresponding estimation errors. Nothing here constructs a well-conditioned shell-resolved destination, selects rational primes or zeta zeros, or implies RH.