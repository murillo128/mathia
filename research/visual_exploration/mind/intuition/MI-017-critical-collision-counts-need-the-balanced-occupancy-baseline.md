# MI-017 — Critical collision counts need a stochastic occupancy baseline

**Evidence level:** exact deterministic occupancy minimization and exact independent categorical collision moments from [VIS-227](../../findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md), [VIS-228](../../findings/VIS-228-multinomial-cell-collisions-have-extensive-excess-above-balanced-floor.md), and [VIS-229](../../findings/VIS-229-nonuniform-categorical-cell-collisions-have-third-moment-variance.md)

At the critical prime-phase scale, neither a positive same-cell collision count nor a positive **linear excess above the balanced occupancy minimum** is automatically evidence of arithmetic clustering.

If `m` points occupy `J` cells with counts `n_j` and

`S=sum_j binom(n_j,2)`,

then writing `m=qJ+r`, `0<=r<J`, gives the deterministic minimum

`S_min(m,J)=J binom(q,2)+rq`.

VIS-228 adds the first stochastic calibration. Under independent uniform allocation of the same `m` labelled points to the same `J` cells,

`E[S]=binom(m,2)/J`,

`Var(S)=binom(m,2)(1/J)(1-1/J)`,

and `E[S-S_min]=Theta(J)` when `m/J` tends to a positive constant, while the standard deviation is only `Theta(sqrt(J))`. Thus an extensive excess above the deterministic floor is generic under the simplest independent null.

VIS-229 shows that replacing the uniform law by an independent nonuniform categorical law changes **both** center and fluctuation scale. If cell probabilities are `(p_j)` and

`q_2=sum_j p_j^2`, `q_3=sum_j p_j^3`,

then exactly

`E[S]=binom(m,2) q_2`,

`Var(S)=binom(m,2)(q_2-q_2^2)+6 binom(m,3)(q_3-q_2^2)`.

The extra term is already present without pair dependence because `q_3-q_2^2=Var(p_X)>=0`. The uniform law is exceptional: there `q_3=q_2^2`, so the shared-index covariance vanishes. Matching only an effective cell count or `q_2` can therefore manufacture a false residual from one-point heterogeneity.

For a fixed independent categorical null, the natural preliminary normalization is

`Z_p=[S-binom(m,2)q_2]/sqrt(binom(m,2)(q_2-q_2^2)+6binom(m,3)(q_3-q_2^2))`,

when the denominator is nonzero. Even this is not yet a prime-specific theorem. A logarithmic-gap-preserving or other structurally matched control may introduce genuine dependence, requiring additional covariance calibration beyond `(q_2,q_3)`; estimated one-point probabilities also carry their own uncertainty.

The reusable boundary is therefore: **deterministic extremality, independent stochastic typicality, and source-dependent dependence are three different baselines**. A critical pair statistic becomes arithmetic evidence only after it survives the deterministic floor, the matched one-point law including its third-moment fluctuation correction, and whatever dependent control structure the hypothesis admits.

If that calibration absorbs the pair statistic, the next observable must retain information not already encoded by one-point occupancy and generic categorical fluctuations rather than re-normalize the same collision count again.