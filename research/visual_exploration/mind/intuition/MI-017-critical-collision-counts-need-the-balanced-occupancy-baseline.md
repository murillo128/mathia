# MI-017 — Critical collision counts need the exact balanced-occupancy baseline

**Evidence level:** exact finite occupancy minimization plus critical-scale specialization from [VIS-227](../../findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md)

At the critical prime-phase scale, a positive same-cell collision count is not automatically evidence of arithmetic clustering. If `N` points occupy `M` cells with counts `n_j` and

`S=sum_j binom(n_j,2)`, 

then writing `N=qM+r`, `0<=r<M`, gives the exact deterministic floor

`S_min(N,M)=M binom(q,2)+rq`,

attained exactly by balanced occupancies `q` and `q+1`.

For the VIS coherence cells at `H=lambda y/log y`, the prime count and cell count satisfy

`m/J -> rho_lambda = eta_v/(8 lambda)`.

Thus the critical family has a real combinatorial phase boundary before any arithmetic organization is examined. If `lambda>eta_v/8`, occupancy alone forces no positive linear collision floor. If `lambda<eta_v/8`, it does; in the first nontrivial band `eta_v/16<lambda<eta_v/8`,

`S_min = (1/2-4lambda/eta_v+o(1)) y/log y`.

The reusable discriminator is therefore not raw collision mass but **excess over the balanced floor**, `S-S_min(m,J)`, or a matched control conditioned on the same `(m,J)`. Otherwise a universal pigeonhole effect can be mistaken for prime-specific coherence exactly at the transition where cell occupancy becomes order one.

This does not determine the critical Ising/torus/SDP objective, a sharp constant, optimizer geometry, a stochastic control law, or dynamical access time. It only calibrates one proposed critical statistic and removes its forced combinatorial component before arithmetic interpretation.
