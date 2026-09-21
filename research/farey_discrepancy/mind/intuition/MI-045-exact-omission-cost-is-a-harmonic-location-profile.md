# MI-045 — Exact omission cost is a harmonic location profile

**Evidence level:** exact finite-horizon synthesis from [FD-246](../../findings/FD-246-harmonic-omission-location-gives-sharp-linear-high-scale-cost.md), refining the finite-column picture in FD-245. The statement is for the relaxed signed divisor-response inverse under `|b_n|<=Cn`.

If exact response zeros fail only on `E_N`, the column identity

`b_n = sum_(m in E_N) Y(m)(1_(m|n)-1_((m+1)|n))`

does more than make the omitted amplitudes triangular: it confines coefficient support to the divisor footprints of `m` and `m+1`. Hence

`sum_(n<=N)|b_n| <= 2 C N^2 sum_(m in E_N) 1/m`.

The omission budget is therefore location-sensitive. If all `K` omissions lie in a fixed high-scale annulus `[alpha N,N]`, the coefficient mass is `O_alpha(C N K)`, so normalized top-octave mass is `O_alpha(K/N)`. This remains coercive for every `K=o(N)`, and the `K/N` scale is sharp for top-half omissions.

The reusable point is that **defect cardinality is not the right exact-sampling complexity parameter**. An omission at scale `N/2^r` can reach only `O(2^r)` coefficient locations, so the natural profile is `sum_r 2^r K_r` or equivalently the harmonic location mass `sum_(m in E_N)1/m`. Low-scale defects are the only ones that can create a large footprint from few missing responses.

**Boundary.** This support argument does not control approximate residuals, positivity, reservoir capacity or arithmetic coherence, and it can be weak for low-scale omission sets. The remaining exact response problem is to understand overlap/cancellation/conditioning among those low-scale adjacent divisor columns, not to seek a sharper bound depending on `K` alone.