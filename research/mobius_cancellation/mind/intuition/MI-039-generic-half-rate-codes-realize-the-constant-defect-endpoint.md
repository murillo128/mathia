# MI-039 — Generic half-rate binary codes realize the constant-defect endpoint; the missing obstruction is arithmetic realizability

**Evidence level:** literature-assisted exact matched-control closure from [MC-317](../../findings/MC-317-random-linear-erasure-augmentation-closes-generic-endpoint.md), resolving the generic frontier isolated by [MC-315](../../findings/MC-315-diagonal-projective-generalized-cap-frontier.md) and [MC-316](../../findings/MC-316-systematic-submatrix-rank-wei-dual-reflection.md).

At the live rank

`t_R=ceil(2 log_2(R+1))`,

MC-314's natural equal-share source scale asks for generalized-weight defect bounded by a constant, specifically `d_(t_R)>=R-2+o(1)`. MC-315--MC-316 show that, for a full binary `[2R,R]` code, this is exactly the same generic constraint whether expressed as projective codimension occupancy, systematic rectangular submatrix ranks, erasure ambiguity, primal generalized weights or the Wei-dual reflected hierarchy.

MC-317 proves that this generic constraint is actually feasible. A 2025 finite-blocklength random-linear erasure list-recovery theorem remains effective when the gap from erasure capacity is only `epsilon_R=Theta(1/R)`. It yields a full-length code a constant number of dimensions below half rate with erasure lists of size `O(R)`. Extending by those `O(1)` dimensions multiplies every list by only a constant, while the target permits a quadratic list. Hence for all sufficiently large `R` there exists a full `[2R,R]` code satisfying

`d_(t_R)>=R-2`.

Equivalently, the diagonal projective generalized-cap envelope has `N_R>=2R` eventually, and systematic matrices satisfying the complete MC-316 submatrix-rank profile exist. The exact natural-scale endpoint is therefore **not** forbidden by generic binary coding or finite projective geometry.

This reverses the role of the matched-control question. There is no longer a useful generic impossibility theorem to seek at this endpoint. Any obstruction strong enough for the Möbius source must use a property of the reciprocal-prime/Legendre source-incidence matrices that the random-linear controls are not required to satisfy. Calling the arithmetic matrices structured, deterministic or source-generated is not enough; the property must quantitatively exclude the known endpoint code family in the same support/rank currency or create a genuinely different endpoint invariant.

The practical audit is now sharp: when a new inequality is proposed, first ask whether it follows only from length `2R`, dimension `R`, generalized weights, projective occupancy, erasure list size, systematic submatrix ranks or their duals. If yes, MC-317's controls already show that it cannot rule out the constant-defect target asymptotically unless the inequality adds genuinely new information beyond those quantities.

**Boundary.** MC-317 is an asymptotic probabilistic existence result; it does not construct the arithmetic source matrices, identify the smallest admissible `R`, or show that reciprocal-prime incidence behaves randomly. It closes only the generic matched-control obstruction. Arithmetic realizability remains completely open and is now the place where a coercive theorem must live.