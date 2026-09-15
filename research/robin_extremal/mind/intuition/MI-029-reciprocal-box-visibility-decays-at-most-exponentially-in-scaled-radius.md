# MI-029 — Reciprocal-box visibility decays at most exponentially in scaled radius

**Evidence level:** exact quantitative positive-measure visibility theorem and Robin packet consequence from [RE-145](../../findings/RE-145-reciprocal-box-visibility-has-an-exponential-scaled-radius-floor.md), sharpening the qualitative fixed-box floor of RE-135 and the growing-radius matched obstruction of [RE-144](../../findings/RE-144-one-sided-slowly-diverging-clusters-defeat-target-anchored-turan-with-one-rightward-mode.md).

For the positive empirical-measure representation of a finite Robin packet, confinement to a reciprocal-scale box of radius `R` controls visibility independently of how many atoms occupy the box. If `mu` is any probability measure supported in that box, its Laplace transform on the fixed observation interval satisfies a lower bound of the form

`sup |F_mu| >= c_kappa exp(-C_kappa R)`.

The mechanism is quantitative analytic continuation from the normalization `F_mu(0)=1`: high-order interpolation reaches the observation interval at a cost exponential in the allowed scaled radius, while positivity removes any dependence on packet cardinality. Passing back to Robin coefficients preserves the same functional order as long as the coefficient perturbation and carrier scale are controlled.

Consequently a packet with `R(U)=o(log U)` retains normalized local visibility at least `U^{-o(1)}` relative to its natural packet scale. This does **not** restore the fixed positive floor available for bounded `R`; it prices how quickly the floor is allowed to collapse as reciprocal geometry spreads.

RE-144 shows that the exponential dependence is the correct functional order in the matched class. Its product packets achieve normalized suppression `exp(-Omega(R))` while allowing `R(U)` to diverge arbitrarily slowly. Thus cardinality is not the primary local currency once positivity has been normalized: the decisive variable is the scaled radius, and its visibility price is exponential up to constants.

The reusable diagnostic is therefore a rate comparison. If an external/source theorem can force actual zeros into a reciprocal radius `R(U)` whose exponential visibility floor dominates every exterior error term, the local packet cannot hide the target. Merely proving `R(U)->infinity` slowly, or bounding packet cardinality without radius, is not enough.

**Boundary.** RE-145 is a representation-level lower bound for positive empirical packet mass and the corresponding finite Robin coefficient regime. It does not prove that actual zeta zeros satisfy a useful radius law, does not contradict RE-144's qualitative hiding construction, and does not by itself compare the local floor with the full exterior Robin budget.