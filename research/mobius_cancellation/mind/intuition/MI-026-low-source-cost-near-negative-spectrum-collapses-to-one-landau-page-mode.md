# MI-026 — Low-source-cost near-negative spectrum collapses to one Landau--Page mode, and cheap corrections cannot hide many high-cost directions

**Evidence level:** exact line-specific consequence of [MC-293](../../findings/MC-293-landau-page-low-source-cost-near-negative-spectrum.md) and [MC-294](../../findings/MC-294-page-cheap-subspace-quotient-girth-tax.md), combining the current Legendre-shell quotient with classical Landau--Page uniqueness, a uniform prime-number theorem for low-conductor real characters, and the classical binary Hamming sphere-packing bound. It does not control the dimension of the high-source-cost quotient, prove a lower bound for effective occupancy, exclude a Landau--Siegel zero or imply a bound for `M(x)`.

For a nonzero shell functional `lambda`, let `Q(lambda)` be the minimum product of lower-prime coordinates whose quadratic product character realizes that functional on the actual shell. This is a source-complexity variable different from dual rank, exceptional-family cardinality, entropy deficit and joint coordinate conductor.

For sufficiently small absolute `kappa`, put

`D_y = exp(kappa log y / loglog y)`.

MC-293 proves that among all nonzero generated shell functionals with `Q(lambda)<=D_y`, every mode is asymptotically balanced except possibly the unique functional induced by the Landau--Page exceptional primitive real character. Quantitatively, outside that possible singleton,

`|A_lambda|/N << (log y)^-2`.

Hence for any near-negative threshold `tau` separated from `1/2` by more than this error, the set

`{lambda != 0 : Q(lambda)<=D_y, d_lambda<=tau}`

has size at most one. At the live defect scale `tau~1/loglog y`, a large family of independent near-negative modes therefore cannot be assembled from individually cheap source characters: all but possibly one have `Q(lambda)>D_y`.

The possible singleton is itself rigid. If its preferred-sign defect is `d_lambda<=tau<=1/4`, then the associated exceptional real zero `beta_*=1-delta_*` satisfies

`delta_* << (tau+(log y)^-2)/log y`.

At `tau~1/loglog y`, near-affinity requires

`1-beta_* << 1/(log y loglog y)`.

MC-294 adds the collective statement missing from individual source cost. Let `W<=H*` be **uniformly Page-cheap**, meaning every nonzero `w in W` has `Q(w)<=D_y`, and let `lambda_1,...,lambda_R` be independent near-negative directions with `d_(lambda_i)<=tau`. If `2t tau+epsilon_y<1`, then every quotient relation of length at most `t` among the images of the `lambda_i` in `H*/W` would lift to a strongly biased cheap character. Page theory permits at most one such relation, corresponding to the possible exceptional mode. After deleting at most one `lambda_i`, the quotient vectors have no nonempty zero-sum subset of size at most `t`.

Thus, with `d=dim W` and `m=floor(t/2)`, their quotient span must satisfy the Hamming sphere-packing tax

`2^(r-d) >= sum_(j=0)^m binom(R-1,j)`,

and in particular `r-d >= m log_2((R-1)/m)` when `R-1>=m>=1`. Many near-negative modes therefore cannot evade MC-293 by sharing one or a few expensive directions and differing only by cheap corrections. They require genuine **high-source-complexity quotient dimension**.

This complements, rather than replaces, [MI-025](MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace.md). MC-291--MC-292 constrain finite geometry and entropy rank without seeing source cost. MC-293 collapses the cheap near-negative spectrum to one possible Landau--Page mode. MC-294 then shows that modding out any certified cheap subspace does not make a large independent near-negative family low-dimensional unless it develops short quotient dependencies forbidden by the same Page balance.

**Boundary.** High-source-cost quotient dimension is not itself a contradiction. MC-294 gives a necessary redundancy/girth bill but no arithmetic upper bound on `r-d`, and the generic Hamming bound may be far from sharp for the actual shell. Nor do MC-293--MC-294 show that the endpoint requires many independent near-negative modes or that the possible Landau--Page singleton is irrelevant. The remaining arithmetic task is to bound the available high-cost quotient dimension, prove stronger arithmetic restrictions on its code, connect it to multiplicity/participation, or show that the singleton cannot carry the endpoint mechanism by itself.