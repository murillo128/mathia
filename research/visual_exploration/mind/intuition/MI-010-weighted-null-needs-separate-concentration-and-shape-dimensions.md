# MI-010 — Signed prime-ratio cancellation has a uniform finite-start window; its coarse horizon is set by worst frequency spacing

**Evidence level:** supported by deterministic/prime-pair transfer controls through VIS-193. Uniform finite-window mean-square cancellation is proved at window length `L>=C y^2`, but no pointwise-in-start bound, optimal window scale, or RH-sensitive signal is established.

VIS-187--VIS-191 show that for a fixed endpoint-zero taper the complete normalized **absolute** prime-pair off-diagonal diagonalizes only above the sharp scale `y/log y`; below that scale ordinary consecutive-prime gaps force an order-one absolute floor.

VIS-192 keeps the signs and averages over the interval start. Distinct prime ratios `q/p` give distinct frequencies `log(q/p)`, so long-start Cesaro orthogonality eliminates all cross terms. For every diverging `H<=y`, the signed variance satisfies `R_v(y,H)<<1/H`, with matching `asymp 1/H` when `H log y/y->0`. Thus the absolute short-gap barrier is not a signed start-averaged barrier.

VIS-193 removes the qualitative dependence on an infinite start average. Writing the signed statistic as a finite exponential polynomial with frequencies `+/-log(q/p)`, distinct frequencies are separated uniformly by at least `log(1+y^(-2))`. Montgomery--Vaughan then yields, for every deterministic start `T0`,

`|R_(v,L)(T0;y,H)-R_v(y,H)| <= 2 pi (y^2+1) R_v(y,H)/L`.

Therefore `L>=C y^2` gives uniform `O(1/H)` mean-square cancellation on every start interval, while `L/y^2->infinity` recovers the Cesaro variance with vanishing relative error. The finite-start existence problem is solved at a coarse universal scale.

The new boundary is not “deterministic versus averaged” but **worst spacing versus energy-weighted spacing**. The `y^2` horizon is obtained by protecting against the closest possible pair of prime-ratio frequencies regardless of how little coefficient mass that pair carries. It is only a sufficient scale. A substantially shorter window requires information about the weighted near-collision distribution of `log(q/p)`, a large-sieve/frame bound adapted to the tapered coefficients, or a theorem that the downstream target naturally supplies enough start length.

**Boundary.** VIS-193 is an `L^2` finite-window theorem, not a pointwise bound on `M_v(y;H,T)`. It proves no lower bound showing that `y^2` is necessary and uses no random-phase hypothesis. The durable separation is now among absolute resolution (`y/log y`), signed Cesaro variance (`1/H`), uniform deterministic-window recovery (currently `y^2`), and the still-open optimal weighted dephasing horizon.
