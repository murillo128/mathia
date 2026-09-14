# MI-026 — Low-source-cost near-negative spectrum collapses to one Landau--Page mode, and endpoint partitions force almost all selected combinations high-cost

**Evidence level:** exact line-specific consequence of [MC-293](../../findings/MC-293-landau-page-low-source-cost-near-negative-spectrum.md)--[MC-296](../../findings/MC-296-endpoint-defect-partitions-force-source-cost-inflation.md). MC-293--MC-294 combine the Legendre-shell quotient with classical Landau--Page uniqueness, a uniform prime-number theorem for low-conductor real characters and classical coding bounds. MC-295 is a finite matched control. MC-296 adds an exact endpoint-partition identity plus Sperner's theorem; it is still not an arithmetic impossibility theorem for the actual shell and gives no bound for `M(x)`.

For a nonzero shell functional `lambda`, let `Q(lambda)` be the minimum product of lower-prime coordinates whose quadratic product character realizes that functional on the actual shell. For sufficiently small absolute `kappa`, put

`D_y = exp(kappa log y / loglog y)`.

MC-293 proves that among all nonzero generated shell functionals with `Q(lambda)<=D_y`, every mode is asymptotically balanced except possibly the unique functional induced by the Landau--Page exceptional primitive real character. MC-294 adds the collective statement: many independent near-negative directions have images in the quotient by the uniformly cheap subspace with no short dependencies, forcing a quantitative high-cost quotient-dimension bill.

MC-295 shows why that quotient bill alone is not a contradiction. A fixed-weight defect-shell model can realize the live endpoint with full high-cost quotient dimension, small participation, no common preferred-sign cell and perfectly balanced cheap directions. Generic Fourier, entropy, Page-balance and Hamming constraints are therefore jointly satisfiable.

MC-296 reveals a stronger invariant hidden in the endpoint geometry. Suppose independent selected functionals `lambda_1,...,lambda_R` have defect sets `D_i` that partition the shell, with defect masses `d_i`. For every subset `I`, the subset-sum functional satisfies exactly

`x_(lambda_I)=(-1)^|I| (1-2 d(I))`, `d(I)=sum_(i in I)d_i`.

Thus every nonempty subset outside the Page half-mass window `|d(I)-1/2|<=epsilon_y/2` is forced above `D_y`, apart from at most the single exceptional functional. If `d_min>epsilon_y`, the subsets remaining in the half-mass window form an antichain, so at most `binom(R,floor(R/2))+1` nonzero selected combinations can be low-cost.

For the equal-defect extremizer `d_i=1/R` with `R=o((log y)^2)`, this becomes especially sharp. If `R` is odd, every nonzero selected combination is high-cost except possibly the Page mode. If `R` is even, only the middle Hamming layer can escape. Consequently a proportion `1-O(R^-1/2)` of the whole selected Fourier subspace is forced above the quasi-subpower source-cost threshold.

The surviving resource is therefore not merely expensive **basis rank**. Endpoint saturation demands a large **expensive subset spectrum**. The actual arithmetic question is whether the Legendre shell can realize so many high-cost characters simultaneously, and what collective source resource that realization consumes. An upper bound on high-cost quotient dimension would suffice, but so would a weaker source-cost/multiplicity law showing that an exponential family of expensive subset characters forces too much lower-prime incidence, occupancy, conductor mass or another arithmetic budget.

This also sharpens the role of the MC-295 matched control. It is free to assign the entire selected span as expensive, so MC-296 does not falsify it. Rather, MC-296 identifies the exact additional bill that any arithmetic realization of that control must pay: almost all noncentral subset sums must be expensive, not only the selected generators.

**Boundary.** Source cost of many individual functionals is not the same as quotient dimension, and neither MC-293 nor MC-296 supplies a theorem bounding the number of high-cost characters available in the actual shell. The exact endpoint partition is load-bearing; overlapping or incomplete defect sets introduce higher intersection data. The durable frontier is collective arithmetic realizability of the expensive spectrum, not another generic finite-coding inequality.