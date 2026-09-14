# MI-026 — Low-source-cost near-negative shell spectrum collapses to one Landau--Page mode

**Evidence level:** exact line-specific consequence of [MC-293](../../findings/MC-293-landau-page-low-source-cost-near-negative-spectrum.md), combining the current Legendre-shell quotient with classical Landau--Page uniqueness and a uniform prime-number theorem for low-conductor real characters. It does not control high-source-cost modes, prove a lower bound for effective occupancy, exclude a Landau--Siegel zero or imply a bound for `M(x)`.

For a nonzero shell functional `lambda`, let `Q(lambda)` be the minimum product of lower-prime coordinates whose quadratic product character realizes that functional on the actual shell. This is a source-complexity variable different from dual rank, exceptional-family cardinality, entropy deficit and joint coordinate conductor.

For sufficiently small absolute `kappa`, put

`D_y = exp(kappa log y / loglog y)`.

MC-293 proves that among all nonzero generated shell functionals with `Q(lambda)<=D_y`, every mode is asymptotically balanced except possibly the unique functional induced by the Landau--Page exceptional primitive real character. Quantitatively, outside that possible singleton,

`|A_lambda|/N << (log y)^-2`.

Hence for any near-negative threshold `tau` separated from `1/2` by more than this error, the set

`{lambda != 0 : Q(lambda)<=D_y, d_lambda<=tau}`

has size at most one. At the live defect scale `tau~1/loglog y`, a large family of independent near-negative modes therefore cannot be assembled from cheap source characters: all but possibly one must have `Q(lambda)>D_y`.

The possible singleton is itself rigid. If its preferred-sign defect is `d_lambda<=tau<=1/4`, then the associated exceptional real zero `beta_*=1-delta_*` satisfies

`delta_* << (tau+(log y)^-2)/log y`.

At `tau~1/loglog y`, near-affinity requires

`1-beta_* << 1/(log y loglog y)`.

Thus the low-cost obstruction is no longer an arbitrary exceptional family; it is either absent or concentrated in one classical Landau--Page mode whose required zero is exceptionally close to `1`.

This complements, rather than replaces, [MI-025](MI-025-small-exceptional-character-family-is-forced-toward-an-affine-halfspace.md). MC-291--MC-292 constrain the finite geometry and entropy rank of biased modes without seeing source cost. MC-293 says that sufficiently cheap modes cannot populate that geometry except for one possible exceptional direction. If `lambda_1,...,lambda_R` are independent and all near-negative, at least `R-1` of them must therefore lie beyond the quasi-subpower source-cost threshold.

**Boundary.** High source cost is not itself a contradiction. A functional can have large minimum lower-prime product cost and still, for all that is proved here, have extreme shell bias. Nor does the theorem show that the endpoint requires many independent near-negative modes. The remaining arithmetic task is to connect high source cost to multiplicity/participation or cancellation, or to show that the single Landau--Page mode cannot carry the endpoint mechanism by itself.