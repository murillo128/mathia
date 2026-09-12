# MI-005 — Stable tails are the uncancelled part of a future partial-correlation volume budget

**Evidence level:** supported by NB-063--NB-075. The stationary prediction/feedthrough criterion is exact for scalar branch filters, and NB-074--NB-075 give exact finite-dimensional necessary/sufficient continuation criteria for the nonstationary causal geometry; no arithmetic estimate closing those criteria is proved.

NB-066--NB-071 reduce a hypothetical persistent Nyman target to a global continuation problem and show that local memory, finite causal flags, exact branching, far-mass necessity, and ordinary global Gram conditioning do not decide it. NB-072--NB-073 identify the stationary mechanism: inner--outer factorization separates stable-tail geometry from conditioning, and the missing inner charge is a future-prediction/feedthrough ratio.

NB-074 gives the nonstationary analogue. For visible Gram `A_R` and the prefix Gram `S_(R,N)` left after optimally eliminating future innovations `D_R,...,D_N`, define

`J_(R,N)=log det(A_R^(-1/2) S_(R,N) A_R^(-1/2))`.

A nonzero stable-tail vector forces `J_(R,N(R))->infinity` for every finite horizon schedule. Conversely, bounded `J_(R_k,N_k)` along any unbounded sequence rules out the stable tail.

NB-075 resolves this determinant into an exact scalar cancellation ledger. Before future elimination let

`L_R=log(det H_(<R) / det A_R)`

be the raw continuation volume. Residualize each new `D_n` and the old prefix against the previously admitted future `D_R,...,D_(n-1)`, and let `beta_(R,n)` be the squared multiple correlation of the genuinely new part of `D_n` with the still-unresolved prefix. Then `0<=beta_(R,n)<1` and

`J_(R,N)=L_R-sum_(n=R)^N [-log(1-beta_(R,n))]`.

Thus later innovations remove raw continuation volume in nonnegative scalar increments, counted once after conditioning on the earlier future. Large raw tail energy or a large raw determinant ratio is not itself an obstruction: it may be cancelled completely by later innovations. The stable-tail currency is the **uncancelled remainder** after the whole future is allowed to explain the prefix.

For fixed `R`, the infinite cancellation sum converges and

`J_(R,infinity)=L_R-sum_(n>=R)[-log(1-beta_(R,n))] >= 0`.

Any nonzero stable tail forces this remainder to diverge as `R->infinity`. Conversely it is enough to find unbounded `R_k`, finite `N_k`, and fixed `C` with

`sum_(n=R_k)^N_k [-log(1-beta_(R_k,n))] >= L_(R_k)-C`.

Since `-log(1-x)>=x`, the stronger scalar condition `sum beta_(R_k,n)>=L_(R_k)-C` also suffices. The arithmetic target is therefore not “make the raw tail small”; it is to show that actual later Nyman innovations recover essentially all raw continuation volume, to `O(1)` accuracy along some unbounded sequence.

**Boundary.** Divergent uncancelled volume is necessary for a stable tail but not sufficient in a general growing-dimensional family; determinant growth can come from many moderate directions. The individual `beta_(R,n)` depend on elimination order even though their total logarithmic cancellation for a fixed future span is invariant. NB-075 supplies an exact source-facing scalarization, not the missing arithmetic bound.