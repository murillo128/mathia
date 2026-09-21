# MI-066 — Simultaneous Kron deletions add only a thin contrast sector beyond independent stars

**Evidence level:** exact/asymptotic synthesis from [PC-391](../../findings/PC-391-multi-deletion-kron-interaction-is-a-vanishing-rank-contrast-correction.md).

Let `S` be the surviving boundary, `T` the `k` vertices deleted at one refinement step, `B` the survivor-to-deleted conductance matrix, `D` the diagonal matrix of deleted-to-survivor degrees, and `K` the Laplacian induced on `T`. Compare the true Kron response with the response obtained after switching off the internal edges of `T`. The irreducible multi-deletion term is exactly

`Delta_T = B[D^(-1)-(D+K)^(-1)]B^*`.

Writing `A=D^(-1/2) K D^(-1/2)` gives

`Delta_T = B D^(-1/2) A(I+A)^(-1) D^(-1/2) B^* >= 0`,

so

`rank(Delta_T) <= rank(K) = k-c_T`,

where `c_T` is the number of connected components of the deleted graph. For the positive complete chord kernels of the prime-circle model, `rank(Delta_T)<=k-1`. The missing common mode is structural: only contrasts among the deleted vertices survive beyond the independent one-vertex star responses.

For two deleted vertices the entire correction is rank one and depends only on the contrast between their normalized incident profiles. Thus multiple deletion does create information not present in isolated stars, but that new information is not a free `k`-dimensional boundary operator; it lives in the deleted-vertex contrast sector.

On every fixed polynomial primorial window `H=p^u`, `u>1`, the deletion count is at most `H/q` while the survivor boundary already has order at least `H/log H`. Hence

`rank(Delta_T)/|S| = O(log p/p) -> 0`.

The multi-deletion correction therefore cannot generate a different limiting empirical bulk spectrum from the independent-star baseline. This does **not** say the full Kron response is low rank: the independent-star terms can be full rank on the survivor space.

The remaining spectral leverage of simultaneous deletion must be sought in observables that can retain a vanishing-rank contrast sector—outliers, determinant/log-determinant effects, exceptional modes, or cross-level evolution of those contrast subspaces—or in a state/operator that is not exhausted by graph-Laplacian Schur complementation.

**Boundary.** The bulk conclusion is for ordinary positive weighted graph Laplacians on fixed polynomial primorial windows. Vanishing rank fraction does not bound individual outlier motion or determinant effects, and PC-391 does not classify signed kernels, nonlinear elimination rules, exponentially growing windows, or non-Schur state spaces.