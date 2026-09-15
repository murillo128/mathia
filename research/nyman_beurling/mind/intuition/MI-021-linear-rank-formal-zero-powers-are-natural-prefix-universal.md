# MI-021 — Linear-rank formal zero powers are natural-prefix universal

**Evidence level:** exact Vandermonde interpolation obstruction from [NB-130](../../findings/NB-130-linear-rank-formal-zero-power-packets-interpolate-arbitrary-natural-prefix-data.md)

Finite recurrence and zero-power analyticity become nonrestrictive on a length-`R` natural prefix when the formal packet is allowed rank `R`. Choose distinct exponents

`rho_j = beta + i(T+j delta)`, `0<=j<R`,

with `1/2<beta<1` and `delta` small enough that the nodes `n^(i delta)`, `1<=n<=R`, are distinct. After factoring the common row weights, evaluation on the prefix is an ordinary Vandermonde matrix. Hence **every** vector in `C^R` is represented exactly by these `R` simple right-half zero powers, even with arbitrarily high `T` and arbitrarily narrow ordinate support.

The same interpolant obeys the expected finite recurrence on every geometric grid. There is no contradiction with the earlier recurrence obstruction: its order is `R`, while a natural prefix of length `R` exposes only `O(log R)` samples on any fixed geometric grid. The recurrence exists but cannot constrain arbitrary prefix data in this rank regime.

The cost is conditioning. As the ordinate spacing shrinks, the Vandermonde determinant decays like `delta^(R(R-1)/2)`, and NB-130 provides no useful uniform coefficient or model-space norm. This is precisely where actual zeta-zero geometry may still matter.

The durable separator is therefore quantitative: a source theorem must bound **effective rank, coefficient/model-space conditioning, or the allowed zero geometry relative to visible prefix depth**. Analyticity, finite recurrence, high ordinate, and narrow spectral support alone do not distinguish genuine zero-power behavior from an arbitrary finite matched control. NB-130 is formal; it does not assert that the freely placed exponents are actual zeta zeros.