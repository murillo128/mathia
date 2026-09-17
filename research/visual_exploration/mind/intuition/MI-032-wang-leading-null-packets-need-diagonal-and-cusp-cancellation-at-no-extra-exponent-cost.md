# MI-032 — Wang leading-null packets need both diagonal and cusp cancellation

**Evidence level:** exact synthesis from [VIS-266](../../findings/VIS-266-wang-proof-allows-slowly-moving-tests-under-a-fixed-support-margin.md) through [VIS-268](../../findings/VIS-268-wang-diagonal-safe-packets-preserve-bandwidth-exponent.md).

The moving-test interface has two independent leading nuisances. Wang's normalized pair-correlation functional contains both the point evaluation `g(0)` and the cusp pairing `int |alpha|g(alpha)dalpha`. Cancelling only the cusp term does not make a packet leading-null.

VIS-268 shows that the extra diagonal condition `g_b(0)=0` is compatible with the mass, cusp and even-moment constraints needed for a normalized order-`2m` packet. Finite-dimensional linear independence supplies a fixed smooth profile with all those constraints, and dilation preserves them.

Crucially, diagonal safety costs no new bandwidth exponent. The sharp packet scales remain

`||g_b||_inf = Theta_m(b^(-(2m+1)))`,

`||g_b'||_inf = Theta_m(b^(-(2m+2)))`.

Therefore Wang's present proof still admits the same sufficient shrinking-window condition `1/(L b^(2m+2))->0`. For `b=L^(-q)`, the gate remains `q<1/(2m+2)`: quadratic extraction requires `q<1/4`, quartic extraction `q<1/6`.

The reusable interface rule is exact: a test designed to expose a lower-order residual must annihilate the **whole leading functional of the theorem being transferred**, not only the nuisance term suggested by the downstream observable. Missing one independent leading coordinate can dominate the intended residual even when all moment conditioning calculations are otherwise correct.

**Boundary.** The repaired packet class only removes Wang's leading diagonal and cusp terms. It does not produce a nonzero arithmetic residual, improve the theorem remainder, move the support edge to `theta`, or supply higher-order covariance.