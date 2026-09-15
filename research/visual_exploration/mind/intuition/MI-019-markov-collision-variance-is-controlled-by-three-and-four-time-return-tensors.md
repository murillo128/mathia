# MI-019 — Markov collision variance is controlled by three- and four-time return tensors

**Evidence level:** exact finite-state stationary-Markov variance identity from [VIS-231](../../findings/VIS-231-stationary-markov-cell-collisions-have-exact-triple-quadruple-variance.md), completing the dependent-center calibration of [VIS-230](../../findings/VIS-230-stationary-markov-cell-collisions-have-lag-return-center.md)

For a stationary finite-state Markov chain with law `pi`, transition matrix `P`, and collision count

`S=sum_(a<b) 1_(X_a=X_b)`,

VIS-230 shows that the exact center is determined by the lag-return profile

`c_r=P(X_0=X_r)=sum_i pi_i(P^r)_(ii)`.

VIS-231 identifies what the covariance additionally needs. Define

`T_(r,s)=sum_i pi_i(P^r)_(ii)(P^s)_(ii)`

for three-time coincidences and three four-time pair-pair tensors `D1_(r,s,t), D2_(r,s,t), D3_(r,s,t)` corresponding to the disjoint pairings of four ordered times. Then `Var(S)` is an exact finite sum of the diagonal mean term, the `T` contributions from overlapping collision pairs, the three `D` contributions from disjoint pairs, minus `E[S]^2`.

The combinatorial reason is complete: after squaring a degree-two collision U-statistic, two distinct pair indicators either share one sample index or are disjoint. The former probes a three-time equality event; the latter probes one of three four-time pairings. No one-point or pair-return summary can determine the variance in general.

For the independent categorical chain `P_(ij)=pi_j`, the tensors collapse to `T=q_3` and `D1=D2=D3=q_2^2`, recovering exactly the VIS-229 variance. Thus the Markov formula is a strict dependent extension rather than a new normalization of the independent control.

The reusable calibration rule is now explicit: **matching the marginal law does not determine the dependent center, and matching the lag-return center does not determine the dependent covariance.** Once a first-order stationary Markov null is independently admitted, both finite-sample moments are computable exactly from `pi` and `P`; a claimed prime residual should be standardized only after those higher joint terms are included.

**Boundary.** This does not assert that prime phase cells are Markov, establish a central limit theorem, justify estimating `pi,P` from the same confirmation statistic, or calibrate renewal, higher-order, nonstationary or growing-state controls. For those models the three-/four-time topology remains diagnostic, but the stationary first-order matrix formulas do not automatically apply.