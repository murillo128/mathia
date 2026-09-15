# MI-018 — Dependent collision baselines are centered by lag-return profiles

**Evidence level:** exact stationary-Markov collision identity from [VIS-230](../../findings/VIS-230-stationary-markov-cell-collisions-have-lag-return-center.md), extending the independent categorical calibration in [VIS-229](../../findings/VIS-229-nonuniform-categorical-cell-collisions-have-third-moment-variance.md)

For a stationary cell process, pair collisions are not centered by the one-point law once temporal dependence is admitted. In the first-order Markov specialization with stationary law `pi`, transition matrix `P`, and

`c_r=P(X_0=X_r)=sum_i pi_i (P^r)_(ii)`,

the collision count

`S=sum_(a<b) 1_(X_a=X_b)`

has exact mean

`E[S]=sum_(r=1)^(m-1) (m-r)c_r`.

The independent categorical center `binom(m,2)q_2`, `q_2=sum_i pi_i^2`, is only the rank-one special case `c_r=q_2` for every lag. For a finite irreducible aperiodic chain, with `d_r=c_r-q_2`,

`E[S]-binom(m,2)q_2 = m A-B+o(1)`,

where `A=sum_(r>=1)d_r` and `B=sum_(r>=1) r d_r`. Ordinary short-range recurrence can therefore create an **extensive** collision shift while leaving the entire one-point occupancy law unchanged.

The reusable boundary is that matching marginals does not calibrate a dependent null. Once a control preserves local sequence structure, its own lag-return profile becomes part of the center before any residual can be called source-specific. The next independent quantity is the covariance of the collision U-statistic under that admitted dependence, not another recentering by one-point moments.

**Boundary.** The prime phase-cell sequence is not asserted to be Markov, and VIS-230 does not provide the dependent variance. A prime-specific residual requires a justified dependence model, its center and covariance fixed independently of the confirmation statistic, and a later bridge from the residual back to the signed phase objective.