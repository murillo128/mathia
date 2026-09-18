# MI-065 — Hamming-shell quantization has a sharp `L^1` resolution tariff

**Evidence level:** exact synthesis from [MC-368](../../findings/MC-368-prime-shell-bias-subset-sum-side-channel.md) and [MC-369](../../findings/MC-369-hamming-shell-quantization-stabilizes-near-balance.md).

For the even-rank punctured-cube endpoint source, write the prime-shell masses as

`d_i = 1/R + epsilon_i`, with `sum_i epsilon_i=0`,

and let `K` be the number of negative source coordinates. The exact-real shell bias decomposes as

`T = b_K - 2 epsilon(J)`, where `b_K=1-2K/R`.

The perturbation geometry is exact:

`max_J |epsilon(J)| = ||epsilon||_1/2`.

Balanced Hamming levels are spaced by `2/R`, so the nearest-level quotient is uniformly stable exactly below the half-gap. If

`||d-R^(-1)1||_1 < 1/R`,

then every source state satisfies `Q_R(T)=b_K`. The quotient destroys all subset identity and retains only Hamming weight. Consequently

`||E[X_i | Q_R(T)]||_2^2 = (2^R-R)/(R(2^R-1)) = 1/R+O(2^-R)`,

and the MC-338 leakage-energy inequality again forces exact dephasing energy at least

`R(2^R-1)/(2^R-R) = R+o(1)`.

The threshold is sharp for uniform nearest-shell decoding: once the `L^1` imbalance exceeds `1/R`, some subset perturbation crosses a half-gap; at equality a tie may occur. Thus the right stability currency is not coordinatewise closeness but aggregate subset-collectable imbalance.

This resolves the discontinuity exposed by MC-368 only after an observation model is specified. Exact-real access to `T` can still encode the entire source arbitrarily close to balance. The finite-resolution theorem says instead that **if** the physical coefficient architecture canonically identifies values within one balanced-shell Voronoi cell, then near-balance becomes information-stable with a precise tariff.

The remaining arithmetic obligation is therefore two independent statements: an endpoint estimate strong enough to force `||d-R^(-1)1||_1<1/R` at the relevant rank, and a structural reason the actual observable cannot resolve below the Hamming half-gap. Neither follows from the other, and MC-369 supplies neither an `M(x)` estimate nor a zero-free theorem.
