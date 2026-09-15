# VIS-230 — stationary Markov cell collisions are centered by a lag-weighted return profile

## Claim

Let `X_1,...,X_m` be a stationary Markov chain on cells `1,...,J` with stationary law `pi=(pi_i)` and transition matrix `P`. Define

`S = sum_(1<=a<b<=m) 1_{X_a=X_b}`

and

`q_2 = sum_i pi_i^2`.

For every lag `r>=1`, put

`c_r = P(X_0=X_r) = sum_i pi_i (P^r)_(ii)`.

Then the collision count has the exact mean

`E[S] = sum_(r=1)^(m-1) (m-r) c_r`.

Hence its displacement from the independent-categorical center with the same one-point law is exactly

`Delta_m = E[S] - binom(m,2) q_2`
`        = sum_(r=1)^(m-1) (m-r)(c_r-q_2)`.

For the independent categorical process, `P_(ij)=pi_j`, so `c_r=q_2` for every `r>=1` and `Delta_m=0`, recovering `VIS-229`.

If the finite-state chain is irreducible and aperiodic, then `c_r-q_2` decays exponentially. Therefore the absolutely convergent constants

`A = sum_(r>=1) (c_r-q_2)`,

`B = sum_(r>=1) r(c_r-q_2)`

exist and

`Delta_m = m A - B + o(1)`.

Thus matching the full one-point cell law does **not** center a dependent occupancy control. Even a simple stationary Markov dependence can create an extensive collision shift when `A != 0`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL MARKOV/U-STATISTIC SPECIALIZATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that prime phase-cell labels form a Markov chain, that a first-order Markov control is sufficient for the prime problem, or that the actual critical prime collision residual is nonzero.

## 1. Exact lag decomposition

Write

`I_ab = 1_{X_a=X_b}`

for `a<b`. Stationarity gives

`E[I_ab] = P(X_a=X_b) = P(X_0=X_(b-a)) = c_(b-a)`.

For a fixed lag `r`, exactly `m-r` unordered sample pairs satisfy `b-a=r`. Summing the pair expectations therefore gives

`E[S] = sum_(r=1)^(m-1) (m-r)c_r`.

The Markov property is not needed for this counting step; it is used only to express the lag collision probability as

`c_r = sum_i P(X_0=i) P(X_r=i | X_0=i)`
`    = sum_i pi_i (P^r)_(ii)`.

So a dependent null is centered by its complete lag-return profile, not merely by its stationary occupancy probabilities.

## 2. Independent categorical centering is the rank-one special case

For independent draws with common law `pi`, the transition matrix has identical rows,

`P_(ij)=pi_j`.

Then `P^r=P` for every `r>=1`, and hence

`c_r = sum_i pi_i^2 = q_2`.

Substituting this constant return profile yields

`E[S] = q_2 sum_(r=1)^(m-1)(m-r)`
`     = binom(m,2)q_2`,

exactly the center in `VIS-229`.

The distinction is therefore precise: `VIS-229` calibrates arbitrary **one-point heterogeneity** under independence, whereas the present result shows that dependence changes the center through lagged recurrence even when the stationary one-point law is held fixed.

## 3. Integrated return bias under ergodic Markov dependence

Set

`d_r = c_r-q_2`.

For a finite irreducible aperiodic Markov chain, `P^r_(ij) -> pi_j` geometrically, so `d_r` and `r d_r` are absolutely summable. The exact correction is

`Delta_m = m sum_(r=1)^(m-1)d_r - sum_(r=1)^(m-1) r d_r`.

Absolute geometric convergence gives

`m sum_(r>=m)d_r -> 0`

and

`sum_(r>=m) r d_r -> 0`,

which proves

`Delta_m = mA-B+o(1)`.

The coefficient `A` is the integrated excess same-cell return probability over the independent stationary baseline. Positive short-lag persistence can therefore create a positive linear collision excess without any change in the one-point cell histogram. Negative or oscillatory dependence can reduce the center instead.

For a critical family in which the number of sampled prime cells and the number of available cells grow together, the corresponding family of integrated-return coefficients must be calibrated rather than assumed negligible. If that coefficient remains order one, the induced center shift is extensive and can dominate the square-root fluctuation scale of the independent categorical null.

## 4. Consequence for the critical prime-phase occupancy clue

The active clue asks whether critical prime phase cells retain non-generic structure after one-point occupancy calibration. `VIS-229` supplies the exact independent categorical center and variance for that stage. The present finding establishes the next control boundary before any prime-specific inference:

**once a stronger control preserves local dependence, the independent-categorical center is no longer valid even when the control has exactly the same stationary cell probabilities.**

A first-order Markov surrogate should therefore be centered by

`sum_(r=1)^(m-1)(m-r)c_r`,

with the return probabilities measured or specified by the admitted surrogate itself. A residual against `binom(m,2)q_2` would otherwise mix the intended prime signal with ordinary serial recurrence.

This finding does not provide the dependent variance. Under dependence, covariances between pair indicators involve overlapping triples and separated quadruples, so the `q_2,q_3` variance formula from `VIS-229` cannot simply be reused. That covariance calibration is a distinct next question and is not needed to establish the centering obstruction proved here.

## Prior art and novelty boundary

Collision counts are degree-two U-statistics with kernel `h(x,y)=1_{x=y}`. U-statistics under ergodic Markov dependence are established classical territory; in particular, Gersende Fort, Eric Moulines, Pierre Priouret, and Pierre Vandekerkhove, **A simple variance inequality for U-statistics of a Markov chain with applications**, *Statistics & Probability Letters* 82:6 (2012), 1193–1201, DOI `10.1016/j.spl.2012.02.001`, develops variance control for Markov-chain U-statistics.

No new probability theorem is claimed. The contribution here is the elementary exact specialization needed by Mathia's current critical phase-cell control: it isolates the lag-return center explicitly and shows why preserving the one-point law alone is insufficient after dependence is introduced.

## Boundaries and falsification

The formula `E[S]=sum_r(m-r)c_r` needs stationarity only to make collision probabilities depend on lag. Without stationarity the exact mean is still the sum of the pair-specific probabilities `P(X_a=X_b)`, but there is no single lag profile.

The representation `c_r=sum_i pi_i(P^r)_(ii)` assumes a stationary Markov chain. The asymptotic `Delta_m=mA-B+o(1)` additionally uses finite-state irreducible aperiodic mixing; periodic, reducible, nonstationary, or triangular-array controls require their own analysis.

The finding says nothing about the variance under dependence and nothing about whether a Markov surrogate preserves the correct prime logarithmic-gap structure. Falsify it by finding an error in the lag counting, the Markov return identity, the iid reduction, or the summability argument for the ergodic finite-state asymptotic.

## Research consequence

The critical collision route has now crossed four control boundaries: deterministic balanced occupancy, uniform independent occupancy, nonuniform independent occupancy, and dependent centering. Any future gap-preserving control must calibrate its lag-return profile before a collision residual can be interpreted as prime-specific. Only after that center is fixed does it make sense to study the dependent covariance and ask whether any surviving standardized residual couples to the signed prime-phase Hamiltonian.