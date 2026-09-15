# MI-033 — Sparse same-source Julia coherence is still matched-control realizable by block grafting

**Evidence level:** exact/literature-audited matched-control obstruction from [WP-320](../../findings/WP-320-sparse-gap-family-coherence-is-still-one-source-matched-control.md), extending the one-tangent universality of WP-318--WP-319.

WP-319 leaves a natural family-level hope: perhaps individual gap-normalized Mangoldt Julia laws are matched-control universal, but requiring infinitely many of them to arise from one common source forces arithmetic coherence. WP-320 shows that this requirement is still too weak after sufficiently sparse thinning.

Along a fixed bounded prime-gap family, choose a sparse subsequence of midpoint nodes `t_k`, gap scales `g_k`, derivative normalizations `D_k` and derivative-biased arithmetic laws `rho_k`. Tightness lets each `rho_k` be approximated by a compactly supported non-atomic law `sigma_k` away from the Julia node. Because `D_k g_k^2 -> 0`, the block

`mu_k = D_k g_k^2 (A_k)_#(u^2 sigma_k(du))`,  `A_k(u)=t_k+g_k u`,

can be chosen with summable total mass while reproducing its own derivative exactly.

Placing the nodes far apart and summing the blocks gives one finite non-atomic positive measure `mu_ctrl`. Remote blocks contribute only `O(1)` to the derivative at `t_k`, while `D_k->infinity`, so

`Dhat_k/D_k -> 1`.

After derivative biasing, the remote mass has vanishing relative weight and

`d_BL(rhohat_k,rho_k) -> 0`.

The Cauchy-transform kernels are bounded and Lipschitz on compact subsets of the upper half-plane, so this convergence is strong enough to make the normalized Boolean self-energy/Julia profiles converge locally uniformly. The matched control therefore copies the actual scalar observable, not merely a weak measure-theoretic decoration.

The reusable obstruction is precise: **common-source provenance does not create rigidity when the local charts can be separated and their required block masses are summable**. An infinite family can still be assembled independently inside one positive source. A surviving scalar theorem must couple charts strongly enough to forbid this grafting — for example through non-sparse/overlapping nodes, an exact cross-gap invariant, or a global finite--archimedean constraint.

**Boundary.** The construction is deliberately sparse and target-engineered. It does not reproduce every bounded gap, a positive-density family, the Mangoldt counting law, multiplicative correlations, or the global Weil form. It is therefore not a no-go for all family rigidity. It closes only the weak claim that infinitely many scalar Julia tangents sharing one source are automatically arithmetic-selective.