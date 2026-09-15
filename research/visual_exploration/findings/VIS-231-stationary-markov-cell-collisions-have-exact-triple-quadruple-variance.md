# VIS-231 — stationary Markov cell collisions have an exact triple/quadruple variance decomposition

## Claim

Let `X_1,...,X_m` be a stationary Markov chain on cells `1,...,J` with stationary law `pi=(pi_i)` and transition matrix `P`. Define

`S = sum_(1<=a<b<=m) 1_{X_a=X_b}`

and, as in `VIS-230`,

`c_r = P(X_0=X_r) = sum_i pi_i(P^r)_(ii)`.

Write

`M_m = sum_(r=1)^(m-1) (m-r)c_r = E[S]`.

For positive lags define the triple coincidence probability

`T_(r,s) = sum_i pi_i (P^r)_(ii) (P^s)_(ii)`,

and the three four-time pair-pair probabilities

`D1_(r,s,t) = sum_(i,j) pi_i (P^r)_(ii) (P^s)_(ij) (P^t)_(jj)`,

`D2_(r,s,t) = sum_(i,j) pi_i (P^r)_(ij) (P^s)_(ji) (P^t)_(ij)`,

`D3_(r,s,t) = sum_(i,j) pi_i (P^r)_(ij) (P^s)_(jj) (P^t)_(ji)`.

Then the collision variance is exactly

`Var(S)`
` = M_m`
`   + 6 sum_(r,s>=1; r+s<=m-1) (m-r-s) T_(r,s)`
`   + 2 sum_(r,s,t>=1; r+s+t<=m-1) (m-r-s-t)`
`       * [D1_(r,s,t)+D2_(r,s,t)+D3_(r,s,t)]`
`   - M_m^2`.

Thus the dependent covariance gate left open by `VIS-230` is finite and explicit for every specified finite-state Markov surrogate. The lag-return center `(c_r)` alone is not the whole calibration: overlapping pair indicators require three-time coincidence probabilities and disjoint pair indicators require four-time pair-pair probabilities.

For the independent categorical chain `P_(ij)=pi_j`, put

`q_2=sum_i pi_i^2`, `q_3=sum_i pi_i^3`.

Then `c_r=q_2`, `T_(r,s)=q_3`, and `D1=D2=D3=q_2^2`, so the formula reduces exactly to

`Var(S)=binom(m,2)(q_2-q_2^2)+6binom(m,3)(q_3-q_2^2)`,

the `VIS-229` variance.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL MARKOV/U-STATISTIC SPECIALIZATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that a first-order Markov chain is a faithful model of prime phase cells, that these tensors are small, or that the actual prime collision statistic is non-generic after this calibration.

## 1. Square the collision count by pair topology

For `a<b` write

`I_ab = 1_{X_a=X_b}`.

Since `I_ab^2=I_ab`,

`E[S^2] = E[S] + 2 sum_(e<f) E[I_e I_f]`,

where `e,f` range over distinct unordered index pairs. Two distinct pairs have only two possible intersection types: they share one sample index, or they are disjoint.

This topological split is exact and exhausts the covariance problem. It also explains why the center from `VIS-230` is insufficient for standardization: a variance necessarily sees at least three- and four-time joint events.

## 2. Overlapping pairs give the triple term

Take three ordered times `a<b<c` and put

`r=b-a`, `s=c-b`.

There are exactly three unordered pairs of collision indicators supported on these three times:

`(I_ab,I_ac)`, `(I_ab,I_bc)`, `(I_ac,I_bc)`.

Every product is the indicator of the same event

`X_a=X_b=X_c`.

By stationarity and the Markov property,

`P(X_a=X_b=X_c)`
` = sum_i pi_i (P^r)_(ii)(P^s)_(ii)`
` = T_(r,s)`.

For fixed positive `r,s`, there are `m-r-s` possible starting times `a`. Therefore the contribution of overlapping pair-indicators to `E[S^2]` is

`6 sum_(r,s>=1; r+s<=m-1)(m-r-s)T_(r,s)`.

The factor `6` is `2` from expanding the square times `3` pairings on each triple of sample times.

## 3. Disjoint pairs give three four-time pairings

Take four ordered times `a<b<c<d` with consecutive spacings

`r=b-a`, `s=c-b`, `t=d-c`.

The six pair indicators on these times can be grouped into three unordered disjoint pairings:

`(I_ab,I_cd)`, `(I_ac,I_bd)`, `(I_ad,I_bc)`.

For the first pairing, the path has the form

`i --r--> i --s--> j --t--> j`,

so

`E[I_ab I_cd]=D1_(r,s,t)`.

For the crossing pairing, the path is

`i --r--> j --s--> i --t--> j`,

so

`E[I_ac I_bd]=D2_(r,s,t)`.

For the nested pairing, the path is

`i --r--> j --s--> j --t--> i`,

so

`E[I_ad I_bc]=D3_(r,s,t)`.

For fixed positive `r,s,t`, there are `m-r-s-t` choices of `a`. Multiplication by the factor `2` from the square expansion gives the stated four-time term.

Combining the diagonal, triple, and quadruple contributions yields the exact formula for `E[S^2]`; subtracting `M_m^2` proves the variance identity.

## 4. Independent categorical reduction

For the rank-one transition matrix

`P_(ij)=pi_j`,

all positive powers equal `P`. Hence

`c_r=q_2`,

`T_(r,s)=sum_i pi_i^3=q_3`,

and direct substitution gives

`D1_(r,s,t)=D2_(r,s,t)=D3_(r,s,t)=q_2^2`.

There are `binom(m,3)` ordered triples of sample times and `binom(m,4)` ordered quadruples, so

`E[S^2]`
` = binom(m,2)q_2 + 6binom(m,3)q_3 + 6binom(m,4)q_2^2`.

Using

`binom(m,2)^2 = binom(m,2)+6binom(m,3)+6binom(m,4)`

and subtracting `E[S]^2=binom(m,2)^2 q_2^2` gives exactly the `VIS-229` formula. This reduction is an internal consistency check on every combinatorial coefficient in the dependent identity.

## 5. Consequence for the critical prime-phase occupancy clue

`VIS-230` showed that a dependent control must replace the independent center by its lag-return sum. The present finding closes the corresponding covariance question for any **specified stationary finite-state Markov null**: once `pi` and `P` are fixed independently of the confirmation statistic, the center and variance of `S` are both exact finite sums.

This does not validate a Markov null for prime phases. It sharpens the next gate instead. A proposed logarithmic-gap or short-interval preserving surrogate must first justify what state and dependence model it preserves. If a first-order Markov approximation is admitted, it can no longer use simulation noise or the independent variance as an excuse for an uncalibrated z-score; the exact tensors above provide the finite-sample standardization.

Conversely, if the intended surrogate is renewal, higher-order Markov, nonstationary, or a triangular array whose state space changes with scale, this formula is a diagnostic boundary rather than a license to force that surrogate into first-order Markov form.

## Prior art and novelty boundary

Collision counts are degree-two U-statistics with kernel `h(x,y)=1_{x=y}`, and variance theory for U-statistics under Markov dependence is classical. Gersende Fort, Eric Moulines, Pierre Priouret, and Pierre Vandekerkhove, **A simple variance inequality for U-statistics of a Markov chain with applications**, *Statistics & Probability Letters* 82:6 (2012), 1193–1201, DOI `10.1016/j.spl.2012.02.001`, gives explicit variance control for Markov-chain U-statistics. Yves F. Atchadé and Matias D. Cattaneo, **A martingale decomposition for quadratic forms of Markov chains (with applications)**, *Stochastic Processes and their Applications* 124:1 (2014), 646–677, DOI `10.1016/j.spa.2013.09.001`, develops a general decomposition for quadratic forms of Markov chains and dependent U-statistic-type objects.

No new probability theorem is claimed. The contribution here is the elementary exact finite-state specialization needed by the current Mathia control: classify the pair-indicator covariance by its three- and four-time index topology and write every term directly in `pi` and powers of `P`.

## Boundaries and falsification

The finite-sample identity requires stationarity and the first-order Markov property only to express the joint probabilities by lag powers of one transition matrix. The initial square expansion and overlap/disjoint classification are purely combinatorial. Nonstationary or non-Markov controls still admit a corresponding sum over pair-specific three- and four-time probabilities, but not these stationary matrix formulas.

Irreducibility, aperiodicity, reversibility, and spectral-gap assumptions are **not** needed for the exact variance identity. They become relevant only for asymptotic simplification or estimation of the tensors.

The formula does not say that `(c_r)` determines `T,D1,D2,D3`; those higher joint terms must be computed from the admitted transition model or otherwise calibrated. It also does not establish a central limit theorem, a Gaussian z-score, or the effect of estimating `pi,P` from data.

Falsify the finding by finding a missing pair topology, an incorrect multiplicity, an error in one of the Markov path products, or a failure of the independent-categorical reduction.

## Research consequence

For a predeclared stationary Markov control, the critical collision statistic now has an exact finite-sample center (`VIS-230`) and variance (this finding). The unresolved prime-specific question moves downstream: choose and justify the dependent control independently of confirmation, carry any parameter-estimation uncertainty honestly, then test whether the prime collision residual survives that calibrated null and representation perturbations before attempting any connection to the signed critical phase energy.