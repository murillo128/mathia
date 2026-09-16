# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Only pursue reciprocal-endpoint variants that escape the prime-family energy and source-saturation obstruction

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-041-smooth-modulus-zero-free-control-stops-above-the-dyadic-shell-scale`.

MC-307--MC-317 reduce the generic endpoint to a constant-defect generalized-Hamming/code problem and show that generic half-rate binary codes can realize the required profile. MC-319 then finds genuine arithmetic structure in the natural source: a smooth common radical gives strong family zero-free information, but the available Rodosskii conversion is too coarse for the one-dyadic-shell endpoint. MC-320 proves that even almost-perfect cancellation on ordinary integer intervals can coexist with maximal bias on the exact prime shell.

MC-321 closes the natural reciprocal endpoint without the primitive-conductor theorem that MC-320 appeared to demand. The endpoint supplies distinct characters with a fixed nonvanishing bias on the **same dyadic prime shell**, all embedded in one controlled common modulus. The prime Halász--Montgomery estimate applies directly to arbitrary prime-supported coefficients and makes that simultaneous bias impossible.

MC-322 sharpens the obstruction from a fixed-bias family count to an explicit `ell^2` energy budget and extends the common-modulus horizon. For a dense dyadic prime shell, distinct characters modulo one `q<=y^(3-delta)` satisfy

`sum_(chi in Xi) beta_chi^2 <<_delta 1 + |Xi| y^(-delta/24) log y`.

Hence every subpolynomial family has bounded total squared shell bias, and characters with bias at least `tau` obey `|B_tau|<<_delta tau^(-2)` once `tau^2` dominates the error scale. The natural endpoint with common modulus of order `y^2` lies well inside this obstruction.

MC-323 closes the simplest “drop the common modulus” escape throughout every fixed subquadratic individual-conductor range. Schlage-Puchta's varying-modulus theorem gives, for distinct characters of cubefree moduli `q_chi<=y^(2-delta)`,

`sum_(chi in Xi)|beta_chi|^2 <= C_delta(1+|Xi|y^(-c_delta)log y)`.

So only `O_delta(1)` fixed-bias characters can live below `y^(2-delta)`. Applied to the endpoint generators, all but `O_delta(1)` directions must have primitive conductor above that scale; in the natural `2R`-coordinate source package this already forced the common radical to the quadratic boundary.

MC-324 shows that the generator-level accounting is still too weak. The exact endpoint profile also gives every pair mode `lambda_i+lambda_j` the fixed bias `1-4/R`. Applying the varying-modulus obstruction to the `binom(R,2)` distinct pair characters and then double-counting their symmetric-difference representatives gives a weighted Plotkin inequality

`liminf log P/log y >= 4`.

Thus every fixed common-source radical bound `P<=y^(4-eta)` is eventually impossible, even though the analytic estimate is applied only to the individual primitive pair conductors rather than to `P` as a common modulus. Under the natural source-prime cap this forces at least `(4-o(1))R` source coordinates. The endpoint's **pair spectrum amplifies individual conductor pressure into a quartic package-capacity bill**.

The live boundary is therefore stricter than “common modulus versus different moduli.” Controlled common moduli are blocked below the cubic horizon; varying individual fixed-bias characters are forced to the quadratic conductor frontier; and the complete endpoint pair geometry forces the aggregate common source package to the quartic radical frontier. A surviving reciprocal-endpoint variant must change a load-bearing hypothesis: weaken or decorrelate the pair-bias spectrum, cross the relevant conductor/package frontier, lose the cubefree/Burgess regime in a way that matters, abandon dense dyadic prime-shell localization, or change the endpoint defect geometry itself. Merely distributing a fixed amount of defect across independently sourced characters does not evade the obstruction.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before any delicate asymptotic estimate: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the proposed auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an auxiliary observable whose exact multiplicative simplification still leaves information beyond `M(x)`.

## Treat observation category, family energy, conductor capacity and source-code geometry as separate currencies

The endpoint history gives a precise hierarchy. Generic coding capacity does not distinguish the source. Smooth-modulus zero-free information can be too coarse in resolution. Ordinary interval cancellation can target the wrong population. A prime-supported family mean-square theorem can close the endpoint because it sees exactly the population and simultaneous coherence the construction consumes. MC-322 shows that the common-modulus currency is total squared bias rather than family cardinality alone; MC-323 adds the individual-conductor bill; MC-324 shows that higher endpoint spectra plus source-code incidence can convert those individual bills into a stronger aggregate radical constraint.

Future arguments should simplify source observables first, retain matched controls, then ask whether the available theorem is stated in the **same observation category** as the endpoint, whether it controls the whole family-energy profile, which conductor budget each demanded mode requires, and how the endpoint's higher-order mode geometry loads those conductors onto the common source package. “Zero-free,” “small interval sums,” “primitive,” “different moduli,” or “source-generated” are not useful labels until that transfer and capacity accounting are explicit.
