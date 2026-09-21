# MI-074 — Rank-adaptive compact cutoffs reach the logarithmic Ford coverage endpoint in aggregate

**Evidence level:** exact reconstruction synthesis from [NB-267](../../findings/NB-267-rank-adaptive-spline-cutoffs-reach-logarithmic-ford-mesh-coercivity.md), extending NB-264--NB-266. Finite box convolutions, sinc powers and Fourier-series reconstruction are classical; the line-specific content is the rank-coupled Euler normalization, Ford mesh placement and conversion of logarithmic-frequency aggregate response into the matched residue.

The superlogarithmic losses in NB-265--NB-266 were consequences of choosing one compact smooth cutoff before sending the carrier rank `K` to infinity. NB-267 allows the auxiliary dual certificate to depend on `K`: take a compact plateau formed from `N_K asymp log K` repeated box convolutions, all with uniformly bounded support.

Its Fourier transform is a sinc power. Beyond frequency `O(N_K)` the discrete dual tail is exponentially small in `N_K`, so after choosing the convolution order with a sufficiently large constant one obtains

`sum_(|n Delta_m|>C log K) |d_(n,K)| = o(K^(-1/2))`.

Combined with the exact Euler-anchor identity and the universal carrier bound `|D_n|<=M sqrt(K)`, the omitted contribution is `o(1)`. Since the retained dual coefficients remain `O(1/m)`, the logarithmic window must carry aggregate response

`sum_(|n Delta_m|<=C log K) |D_n| >= c m`.

Thus **pure logarithmic rank-coupled coverage is sufficient to force the aggregate coercivity used by the matched Ford residue**. The fixed-cutoff near-exponential barrier was a restriction on the certificate family, not evidence that an iterated-log loss is intrinsic to the source geometry.

The endpoint theorem is deliberately aggregate. The sharpening cutoff no longer gives the uniform full-dual `ell^1` control used in NB-266, so this proof yields only the crude pointwise consequence `sup |D_n| >= c/log K`, not an order-one atom. The auxiliary certificate also becomes increasingly smooth/complex with rank even though its support stays fixed.

**Boundary.** NB-267 is still a matched carrier/Ford compatibility result, not a theorem about actual zeta-zero locations or the final Nyman--Beurling distance. It does not prove that `O(log K)` is minimal, rule out `o(log K)` coverage under the same resolved-cost model, or show that the aggregate response survives the true Hardy/Nyman projection without additional loss.