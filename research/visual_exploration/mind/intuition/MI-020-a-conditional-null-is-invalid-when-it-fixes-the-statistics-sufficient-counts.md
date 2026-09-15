# MI-020 — A conditional null is invalid when it fixes the statistic's sufficient counts

**Evidence level:** exact finite counting obstruction from [VIS-232](../../findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md), refining the Markov center/variance calibration in VIS-230--VIS-231

For phase-cell labels `x_1,...,x_m`, the unordered same-cell collision count is

`S=sum_j binom(N_j,2)`,

where `N_j` are the occupancy counts. Thus any confirmation-sample surrogate that preserves the realized occupancy histogram has `Var(S | N_1,...,N_J)=0`: it has conditioned away the statistic rather than supplied a stronger null.

Exact first-order transition-count preservation is almost as restrictive. The transition row and column sums determine the occupancies once the endpoint is fixed; for a nonclosed path the transition imbalance even determines both endpoints. Hence a transition-table-preserving randomization with matched endpoints also fixes `S` exactly. In the balanced closed-path case, the only remaining variation is the choice of common endpoint, not the interior ordering.

This sharply separates two operations that can look like the same “dependence control.” Fitting a stochastic Markov law on independent calibration data and resampling from it leaves confirmation occupancies random, so the VIS-230/VIS-231 center and variance remain meaningful. Conditioning on the realized transition table is different: for the scalar collision statistic it removes essentially all variability.

The reusable admission rule is **the null must leave the tested observable outside the sigma-field being conditioned on**. If scientific credibility requires preserving realized local transition counts or the exact label multiset, then the confirmation statistic must change to an order-sensitive observable that varies within that conditional class, such as lag-weighted or direction-sensitive return structure.

**Boundary.** The degeneracy is specific to occupancy-measurable `S`. It does not invalidate transition-preserving controls for order-sensitive statistics, nor does it establish that any particular Markov, renewal or higher-order stochastic model is a faithful prime surrogate.