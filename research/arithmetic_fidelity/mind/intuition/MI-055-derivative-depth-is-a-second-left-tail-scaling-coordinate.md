# MI-055 — Derivative depth, source selection, transport provenance, and probe amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-436](../../findings/AF-436-exact-euler-coefficients-retain-shell-ladder-at-exponential-resolution.md).

AF-416--AF-424 show that the reciprocal-order left-tail determinant has more than one scaling coordinate. A fixed derivative shift closes to a positive Cauchy limit, but moving depth enters through `s_n/n`; the complete partition family detects the critical value `2`, and in the critical window probe amplitude and depth combine as

`b_n(a)=a n^(s_n/n-2)`.

Near square values `b=m^2`, full-column rectangles can tie at leading exponential order while exact rectangle ratios, complete-packet drift and the discrete derivative offset remain visible at finer scales. AF-425--AF-432 show that continuous saddle tuning is therefore not enough: the physical depth variable is integral, exact-square fibres miss the required second-order cancellation, and the packet-corrected target lives at a finer scale than the first saddle window.

AF-433--AF-435 separate source selection from downstream transport. The reciprocal-order family `x_n(c)=c/n` permits every `c>0`, while coefficient-root neutrality selects the Taylor radius, hence `c=2pi` and `a=1` for the Bernoulli source, without inspecting determinant packets. That selector is genuinely source-native, but the present determinant has already aggregated shell labels into zeta factors before packet labels form, and the selected square fibre fails the adjacent-packet cancellation of AF-426.

AF-436 sharpens the transport diagnosis. The **exact even Euler coefficients have not lost the shell ladder**. After normalization,

`s_k=(-1)^k k R^(2k)c_(2k)=zeta(2k)=sum_(j>=1) j^(-2k)`.

Peeling shells below `m` leaves `r_(m,k)=sum_(j>=m)j^(-2k)`, with

`1 <= m^(2k) r_(m,k) <= 1+m/(2k-1)`.

Thus `m^(2k)r_(m,k)->1` and the residual root/ratio recovers the next shell. The loss in AF-434 is therefore not intrinsic to the source coefficients; it occurs when the downstream asymptotic representation compresses exponentially separated shell amplitudes into aggregate zeta factors. Shell `m` is present only at scale `m^(-2k)`, so stable recovery requires coefficient error `o(m^(-2k))`.

The reusable order is now five-stage. **First establish source selection. Second identify the exact source carrier and its resolution scale. Third verify that the downstream representation transports rather than aggregates that carrier. Fourth compare the physical source mesh with the target aperture. Fifth test the selected point rather than an optimized surrogate.** The current branch passes source selection and exact shell retention, but the present determinant fails shell-resolved transport and the selected square fibre fails its adjacent-packet mechanism.

**Boundary.** AF-436 is an exact-information statement, not a stability theorem at fixed precision. It does not show that a shell-resolved representation with usable conditioning exists, and it does not rescue the present determinant. AF-435 does not classify all possible source-side selectors. Nothing here selects rational primes or zeta zeros or implies RH.