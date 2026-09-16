# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Only pursue reciprocal-endpoint variants that escape the prime-family energy and source-saturation obstruction

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-041-smooth-modulus-zero-free-control-stops-above-the-dyadic-shell-scale`.

MC-307--MC-317 reduce the generic endpoint to a constant-defect generalized-Hamming/code problem and show that generic half-rate binary codes can realize the required profile. MC-319 then finds genuine arithmetic structure in the natural source: a smooth common radical gives strong family zero-free information, but the available Rodosskii conversion is too coarse for the one-dyadic-shell endpoint. MC-320 proves that even almost-perfect cancellation on ordinary integer intervals can coexist with maximal bias on the exact prime shell.

MC-321 closes the natural reciprocal endpoint without the primitive-conductor theorem that MC-320 appeared to demand. The endpoint supplies distinct characters with a fixed nonvanishing bias on the **same dyadic prime shell**, all embedded in one controlled common modulus. The prime Halász--Montgomery estimate applies directly to arbitrary prime-supported coefficients and makes that simultaneous bias impossible.

MC-322 sharpens the obstruction from a fixed-bias family count to an explicit `ell^2` energy budget and extends the common-modulus horizon. For a dense dyadic prime shell, distinct characters modulo one `q<=y^(3-delta)` satisfy

`sum_(chi in Xi) beta_chi^2 <<_delta 1 + |Xi| y^(-delta/24) log y`.

Hence every subpolynomial family has bounded total squared shell bias, and characters with bias at least `tau` obey `|B_tau|<<_delta tau^(-2)` once `tau^2` dominates the error scale. The natural endpoint with common modulus of order `y^2` lies well inside this obstruction.

MC-323 now closes the simplest “drop the common modulus” escape throughout every fixed subquadratic individual-conductor range. Schlage-Puchta's varying-modulus theorem gives, for distinct characters of cubefree moduli `q_chi<=y^(2-delta)`,

`sum_(chi in Xi)|beta_chi|^2 <= C_delta(1+|Xi|y^(-c_delta)log y)`.

So only `O_delta(1)` fixed-bias characters can live below `y^(2-delta)`. Applied to the exact endpoint generators, all but `O_delta(1)` directions must have primitive conductor exceeding that scale. In the natural `2R`-coordinate source package, whose radical satisfies `P<=y^2`, this forces

`P=y^(2-o(1))`,

and almost every source-coordinate prime must lie near its maximal `y^(1/R)` logarithmic scale. The common-modulus-free route therefore survives only by saturating essentially the whole quadratic source budget.

The live boundary is now two-tiered rather than “common modulus versus no common modulus.” A controlled common modulus is blocked throughout cubic-minus powers; varying individual cubefree conductors are already forced to the quadratic boundary. A surviving reciprocal-endpoint variant must change a load-bearing hypothesis: cross the relevant conductor frontier, lose the cubefree/Burgess regime in a way that matters, make the demanded shell-bias vector collectively `ell^2`-small, abandon dense dyadic prime-shell localization, or change the endpoint defect geometry itself. Merely distributing a fixed amount of defect across independently sourced subquadratic characters does not evade the obstruction.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before any delicate asymptotic estimate: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the proposed auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an auxiliary observable whose exact multiplicative simplification still leaves information beyond `M(x)`.

## Treat observation category, family energy and conductor capacity as separate source currencies

The endpoint history now gives a precise hierarchy. Generic coding capacity does not distinguish the source. Smooth-modulus zero-free information can be too coarse in resolution. Ordinary interval cancellation can target the wrong population. A prime-supported family mean-square theorem can close the endpoint because it sees exactly the population and simultaneous coherence the construction consumes. MC-322 shows that the natural common-modulus currency is total squared bias rather than family cardinality alone; MC-323 shows that varying-modulus provenance adds a separate individual-conductor/package-capacity bill.

Future arguments should therefore simplify source observables first, retain matched controls, then ask whether the available theorem is stated in the **same observation category** as the endpoint, whether it controls the whole family-energy profile, and which conductor/source budget is required to realize that profile. “Zero-free,” “small interval sums,” “primitive,” “different moduli,” or “source-generated” are not useful labels until that transfer and capacity accounting are explicit.
