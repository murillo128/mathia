# MI-044 — Deleting the ordinary Gowers diagonal centers the cube chaos but still does not create bow covariance

**Evidence level:** exact synthesis from [WI-332](../../findings/WI-332-u2-smallness-cannot-control-bow-sliding-variance.md) through [WI-339](../../findings/WI-339-diagonal-deleted-gowers-still-misses-bow-variance.md). The Gowers/Walsh and hypercontractive ingredients are classical; the Mathia content is the matched-energy all-interval countermodel after literal zero-increment deletion and its implication for the distinguished bow interface.

WI-338 closes ordinary normalized Gowers smallness at the natural diagonal wall `R_s=2`, where

`R_s(K,N)=2^s loglog N/log K`.

Below that wall, a matched-energy Rademacher source can be `U^s=o(1)` on every bow-scale interval while retaining full sliding variance. At the wall, zero-increment cubes themselves prevent `U^s=o(1)`. A natural repair was therefore to delete those cubes before taking the `2^-s` root.

WI-339 shows that this literal repair changes the threshold but not the missing information. For Rademacher signs, deleting all cubes with some `h_j=0` is exactly the same as subtracting the expectation of the Walsh cube polynomial. The diagonal-free statistic is the centered Rademacher cube chaos, not a new source-specific covariance observable.

For every fixed `eta in (0,1)` and bow scale `K=N^(kappa+o(1))`, one matched-energy realization can be chosen such that, simultaneously for every interval `I` with `K<=|I|<=2K` and every order satisfying

`R_s(K,N) <= (1-eta)(s+1)`, 

the diagonal-deleted amplitude obeys

`||b||_(dot U^s(I)) <= (log N)^(-eta/[4(1-eta)])`,

while the same source has distinguished sliding square

`(1+o(1)) N K log N`.

Thus removing the deterministic diagonal pushes the random-countermodel frontier from the fixed level `R_s=2` to the much higher curve `R_s=s+1`, reaching to within `O(1)` of `s=log_2 log N` for fixed-power bow windows. Yet the destination variance remains completely unsuppressed.

The conceptual point is that **centering a generic higher-order statistic removes its self-energy without manufacturing the signed two-point relation consumed by the destination**. The bow needs a macroscopic negative off-diagonal covariance against its distinguished carrier. The centered ordinary cube chaos is still compatible with generic matched-energy sign sources whose off-diagonal bow covariance does not provide that cancellation.

The surviving renormalization question is therefore narrower than “remove the Gowers diagonal.” A useful statistic must retain something absent from the centered cube chaos: the actual `Lambda-Lambda^sharp` shifted-prime relation, carrier-dependent covariance, a relative linear-forms structure, or another subtraction whose definition is tied to the distinguished destination rather than only to degenerate cube geometry.

**Boundary.** WI-339 does not rule out every diagonal-free higher-order method. Its countermodel covers every fixed margin below `R_s=s+1`, leaving a top growing-order strip where the present concentration argument no longer proves smallness. More importantly, source-dependent or carrier-dependent renormalizations and relative linear-forms statistics are outside the theorem. The durable conclusion is only that literal zero-increment deletion is not enough: changing the normalization without changing the information channel still misses the bow sign.