# MI-055 — Derivative depth, source selection, joint shell transport, conditioning, and probe amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) through [AF-438](../../findings/AF-438-stieltjes-generating-transform-transports-shell-ladder-jointly.md).

AF-416--AF-424 show that the reciprocal-order left-tail determinant has more than one scaling coordinate. A fixed derivative shift closes to a positive Cauchy limit, but moving depth enters through `s_n/n`; the complete partition family detects the critical value `2`, and in the critical window probe amplitude and depth combine as

`b_n(a)=a n^(s_n/n-2)`.

Near square values `b=m^2`, full-column rectangles can tie at leading exponential order while exact rectangle ratios, complete-packet drift and the discrete derivative offset remain visible at finer scales. AF-425--AF-432 show that continuous saddle tuning is therefore not enough: the physical depth variable is integral, exact-square fibres miss the required second-order cancellation, and the packet-corrected target lives at a finer scale than the first saddle window.

AF-433--AF-435 separate source selection from downstream transport. The reciprocal-order family `x_n(c)=c/n` permits every `c>0`, while coefficient-root neutrality selects the Taylor radius, hence `c=2pi` and `a=1` for the Bernoulli source, without inspecting determinant packets. That selector is genuinely source-native, but the present determinant has already aggregated shell labels into zeta factors before packet labels form, and the selected square fibre fails the adjacent-packet cancellation of AF-426.

AF-436 shows that the **exact even Euler coefficients have not lost the shell ladder**. After normalization,

`s_k=(-1)^k k R^(2k)c_(2k)=zeta(2k)=sum_(j>=1) j^(-2k)`.

AF-437 supplies the stability calculation for sequential exposure. If earlier shell `j` is peeled with relative location error `eta_(j,k)` and weight error `omega_(j,k)`, while the observed moment has additive error `e_k`, then the target-scale error budget contains

`m^(2k)|e_k| + sum_(j<m)(m/j)^(2k)(|omega_(j,k)| + k|eta_(j,k)|)`.

Thus the triangular peeling inverse is exponentially sensitive to earlier-shell errors even though the exact sequence is shell-determinate.

AF-438 shows that this sequential inverse is not forced by the information itself. The ordinary generating transform

`F(z)=sum_(k>=1) zeta(2k)z^(k-1)=sum_(m>=1)1/(m^2-z)`

extends meromorphically as `(1-pi sqrt(z)cot(pi sqrt(z)))/(2z)` and has one simple pole at every `m^2` with residue `-1`. All shell identities therefore coexist in one exact Stieltjes carrier. Removing shell `m` subtracts exactly `1/(m^2-z)`; no earlier shell must first be estimated and cancelled.

The reusable order is now more precise. **First establish source selection. Second identify an exact carrier and whether it is sequential or joint. Third price the inverse conditioning under the actual finite/noisy observation model. Fourth verify that the downstream representation transports rather than aggregates the recovered provenance. Fifth compare the physical source mesh with the target aperture. Sixth test the selected point rather than an optimized surrogate.** AF-438 passes the exact joint-carrier step but does not pass the conditioning or determinant-transport steps.

**Boundary.** The Stieltjes/cotangent representation is classical and exact only with the complete exact coefficient data. It does not prove that truncated/noisy Padé, Hankel, Prony or continued-fraction recovery is well conditioned, and analytic continuation may recreate a severe instability. Nothing here transports the shell poles through the present determinant, selects rational primes or zeta zeros, or implies RH.