# MI-042 — Sparse even endpoint layers saturate the quartic source floor under columnwise incidence accounting

**Evidence level:** proved for the reciprocal-endpoint architecture of MC-323--MC-325, with the new layer ceiling established in [MC-325](../../findings/MC-325-sparse-even-layer-averaging-saturates-quartic-source-floor.md).

The reciprocal endpoint contains many more fixed-bias characters than its generator and pair modes. That cardinality does not by itself buy a stronger source lower bound.

For an even Hamming layer `|I|=r=o(sqrt R)`, every selected mode keeps asymptotically fixed shell bias, so MC-323 forces all but `O_delta(1)` individual primitive conductors above `y^(2-delta)`. But a source prime whose generator column has support size `a` belongs to exactly

`B_(R,r)(a)`

of the `r`-fold symmetric-difference representatives, where `B` is the odd-intersection/Krawtchouk slice. Uniformly in `a`,

`B_(R,r)(a) / binom(R,r) <= 1/2 + binom(r,2)/R`,

and the `1/2` is asymptotically sharp.

Consequently the enormous layer size cancels between conductor demand and source-coordinate incidence capacity. Summing the individual near-quadratic conductor bills yields the same common-radical frontier

`liminf log P / log y >= 4`

already attained by the pair layer. Passing from pairs to `4`-, `6`-, or any sparse even modes does not improve the exponent under this accounting architecture.

The reusable lesson is precise: **higher-mode multiplicity is useful only if it changes the per-coordinate loading law or creates a genuinely joint conductor constraint.** Counting more fixed-bias modes while allowing each source coordinate to serve asymptotically half of them cannot beat the pair-spectrum bill.

A route past exponent `4` must therefore violate at least one load-bearing ingredient: obtain conductor information stronger than independent per-mode lower bounds, exploit correlations among conductors/characters, find a mode family with uniformly smaller source-column incidence, or change the endpoint/source representation so the Krawtchouk half-balance no longer describes its loading.

This is a ceiling for the stated proof architecture, not a universal upper bound on arithmetic source complexity and not an estimate for `M(x)`.
