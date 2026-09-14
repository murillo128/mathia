# MI-026 — Low-source-cost near-negative spectrum collapses to one Landau--Page mode, while the generic high-cost quotient escape is saturable

**Evidence level:** exact line-specific consequence of [MC-293](../../findings/MC-293-landau-page-low-source-cost-near-negative-spectrum.md)--[MC-295](../../findings/MC-295-fixed-weight-defect-shell-saturates-quotient-escape.md). MC-293--MC-294 combine the Legendre-shell quotient with classical Landau--Page uniqueness, a uniform prime-number theorem for low-conductor real characters and the classical binary Hamming sphere-packing bound. MC-295 is a finite matched control, not an arithmetic realization of the actual shell and not a bound for `M(x)`.

For a nonzero shell functional `lambda`, let `Q(lambda)` be the minimum product of lower-prime coordinates whose quadratic product character realizes that functional on the actual shell. For sufficiently small absolute `kappa`, put

`D_y = exp(kappa log y / loglog y)`.

MC-293 proves that among all nonzero generated shell functionals with `Q(lambda)<=D_y`, every mode is asymptotically balanced except possibly the unique functional induced by the Landau--Page exceptional primitive real character. Outside that possible singleton,

`|A_lambda|/N << (log y)^-2`.

At the live defect scale `tau~1/loglog y`, a large family of independent near-negative modes therefore cannot be assembled from individually cheap source characters: all but possibly one have `Q(lambda)>D_y`. If the possible singleton has defect `d_lambda<=tau`, its exceptional real zero must satisfy `1-beta_* << (tau+(log y)^-2)/log y`.

MC-294 adds the collective statement. Let `W<=H*` be uniformly Page-cheap and let `lambda_1,...,lambda_R` be independent near-negative directions with defects at most `tau`. If `2t tau+epsilon_y<1`, then every short quotient relation among their images in `H*/W` would lift to a strongly biased cheap character. After deleting at most one exceptional direction, the quotient vectors have no nonempty zero-sum subset of size at most `t`, and Hamming sphere packing forces a quantitative lower bound on `r-dim W`.

MC-295 shows that this quotient-dimension tax is a **necessary bill, not an impossibility theorem**. In a fixed-weight defect-shell model, take `R` quotient-independent selected characters and choose the weight-one shell. Then every nonzero cheap direction is perfectly balanced, each selected quotient direction has defect `tau=1/R`, the participation is `eta=R2^-R`, and no nonempty selected combination lands in the cheap subspace. The common preferred-sign cell is empty even though the entropy inequality and the live boundary `R tau=1` are saturated.

This matched control simultaneously pays the generic finite costs isolated by MC-291--MC-294. It has large independent bias rank, small participation, no cheap biased leakage, high quotient girth and full high-cost quotient dimension. Therefore one cannot close the actual Möbius branch by combining the existing defect, participation, entropy, Page-balance and Hamming inequalities more cleverly while keeping the same abstract admissible class.

The next resource is arithmetic realizability of the expensive quotient. The actual Legendre shell may forbid the fixed-weight defect pattern, force substantially larger occupancy, couple source cost to multiplicity, restrict which high-cost quotient codes can occur, or make the possible Landau--Page singleton unusable at the endpoint. Any such theorem would be genuinely new arithmetic input rather than another generic Fourier/coding consequence.

**Boundary.** MC-295 does not realize its fixed-weight shell from primes or quadratic characters and does not prove that the actual shell has a large high-cost quotient. It proves the converse methodological point: the full generic constraint package through MC-294 still admits an endpoint-scale extremizer. The live theorem must exploit a source property that the matched control fails to reproduce.