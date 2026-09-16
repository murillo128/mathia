# MI-033 — Growing terminal moment order requires a factorial precision staircase, not merely vanishing relative errors

**Evidence level:** proved for the generalized terminal-insertion model of RE-153--RE-161, with the approximate-moment leakage law in [RE-161](../../findings/RE-161-approximate-terminal-moment-matching-requires-a-factorial-precision-staircase.md).

RE-159--RE-160 show that exact matching of logarithmic placement moments through order `r-1` pushes the first unresolved Robin influence to factorial remainder scale

`L^r/r!`

and gives the growing-order width `tau_r=(r! eta_p)^(1/r)`.

RE-161 exposes what exact matching was buying. If the average moment discrepancies are `mu_k`, then before the `r`-th remainder the Robin coordinate contains the weighted leakage

`sum_(k<r) b_k(U) mu_k`

with `b_1(U)=1+o(1)` and, uniformly for `2<=k<r` in the growing-order regime,

`b_k(U)=(1+o(1))/k!`.

Thus robust separate control is governed by

`E_r = sum_(k<r) |mu_k|/k!`.

To retain the exact-match gain one needs `E_r=O(L^r/r!)`. At the factorial stability width `L=tau_r`, this becomes the precision staircase

`sum_(k<r) |mu_k|/k! = O(eta_p)`,

so an individual `k`-th moment can be tolerated only at scale `|mu_k| <= k! eta_p` absent source-forced cancellation between moment errors.

The qualitative obstruction is stronger than a bad constant. RE-161 constructs PNT-small generalized sources for which

`sup_(k>=1) |mu_k|/L^k -> 0`

while the normalized Robin coordinates remain separated by order one. Hence even **simultaneous vanishing relative error in every finite or growing lower moment is noncoercive**. Moment count and moment precision are separate resources.

A positive source theorem may still beat the absolute staircase by forcing signed cancellation in `sum b_k mu_k`; RE-161 does not exclude that. But a proposal that only says “many moments are approximately matched” is incomplete. It must provide the weighted precision profile, or an arithmetic identity controlling the signed combination actually consumed by the Robin coordinate.

**Boundary.** The obstruction is a generalized-source information test. It does not assert that ordinary primes realize the matched controls; it identifies the quantitative source information an ordinary-prime theorem must supply to distinguish them.
