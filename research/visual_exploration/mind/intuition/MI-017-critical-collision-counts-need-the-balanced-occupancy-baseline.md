# MI-017 — Critical collision counts need a stochastic occupancy baseline

**Evidence level:** exact deterministic occupancy minimization and exact independent-multinomial collision moments from [VIS-227](../../findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md) and [VIS-228](../../findings/VIS-228-multinomial-cell-collisions-have-extensive-excess-above-balanced-floor.md)

At the critical prime-phase scale, neither a positive same-cell collision count nor a positive **linear excess above the balanced occupancy minimum** is automatically evidence of arithmetic clustering.

If `m` points occupy `J` cells with counts `n_j` and

`S=sum_j binom(n_j,2)`,

then writing `m=qJ+r`, `0<=r<J`, gives the deterministic minimum

`S_min(m,J)=J binom(q,2)+rq`.

VIS-228 adds the missing stochastic calibration. Under independent uniform allocation of the same `m` labelled points to the same `J` cells,

`E[S]=binom(m,2)/J`,

`Var(S)=binom(m,2)(1/J)(1-1/J)`,

and

`E[S-S_min]=q(J-1)/2+r(r-1)/(2J)`.

If `m/J->rho>0`, the expected excess above the deterministic floor is `Theta(J)`, whereas the standard deviation is only `Theta(sqrt(J))`. Thus `S-S_min` being extensive is itself generic under the simplest independent null.

For the VIS coherence cells at `H=lambda y/log y`, `m/J->eta_v/(8lambda)`, so the critical pair-collision discriminator begins only after **stochastic centering**. Under the equal-cell null a natural preliminary normalization is

`Z=[S-binom(m,2)/J]/sqrt(binom(m,2)(1/J)(1-1/J))`.

Even that is not yet a prime-specific theorem. If the intended one-point cell probabilities are nonuniform, the independent null mean becomes `binom(m,2) sum_j p_j^2`; stronger controls may also need to preserve logarithmic-gap or cell-origin structure. A residual is interpretable only after those admitted structures are matched.

The reusable boundary is therefore: **deterministic extremality and stochastic typicality are different baselines**. Subtracting a pigeonhole floor removes forced geometry but can leave an order-`J` generic random contribution. If matched stochastic controls absorb the centered pair statistic too, the next observable must retain information not already encoded by one-point occupancy, rather than re-normalize the same collision count again.
