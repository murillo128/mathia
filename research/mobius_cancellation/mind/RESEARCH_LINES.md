# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Only pursue reciprocal-endpoint variants that escape the prime-family energy obstruction

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-041-smooth-modulus-zero-free-control-stops-above-the-dyadic-shell-scale`.

MC-307--MC-317 reduce the generic endpoint to a constant-defect generalized-Hamming/code problem and show that generic half-rate binary codes can realize the required profile. MC-319 then finds genuine arithmetic structure in the natural source: a smooth common radical gives strong family zero-free information, but the available Rodosskii conversion is too coarse for the one-dyadic-shell endpoint. MC-320 proves that even almost-perfect cancellation on ordinary integer intervals can coexist with maximal bias on the exact prime shell.

MC-321 closes the natural reciprocal endpoint without the primitive-conductor theorem that MC-320 appeared to demand. The endpoint supplies distinct characters with a fixed nonvanishing bias on the **same dyadic prime shell**, all embedded in one controlled common modulus. The prime Halász--Montgomery estimate of Puchta/Klurman--Mangerel--Teräväinen applies directly to arbitrary prime-supported coefficients and makes that simultaneous bias impossible.

MC-322 sharpens the obstruction from a fixed-bias family count to an explicit `ell^2` energy budget and extends the fixed-power modulus horizon. For a dense dyadic prime shell, distinct characters modulo one `q<=y^(3-delta)` satisfy

`sum_(chi in Xi) beta_chi^2 <<_delta 1 + |Xi| y^(-delta/24) log y`.

Hence every subpolynomial family has bounded total squared shell bias, and characters with bias at least `tau` obey `|B_tau|<<_delta tau^(-2)` once `tau^2` dominates the error scale. The earlier `y^(8/3-delta)` range was only the `k=2` specialization; `k=3` of the same classical theorem pushes the neutral power balance to the cubic boundary.

Thus primitive conductor provenance, smoothness, zero-free regions and ordinary interval estimates are not the live gate for this endpoint family. The decisive resource is **prime-supported family energy in the exact observation category**.

A surviving reciprocal-endpoint variant must now escape at least one load-bearing hypothesis: approach or exceed the cubic common-modulus scale, lose a controlled common-modulus embedding, make the relevant shell biases collectively `ell^2`-small, abandon dense dyadic prime-shell localization, or change the defect geometry enough that the endpoint no longer demands that energy. Simply redistributing a fixed amount of defect unevenly across many characters does not evade MC-322.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before any delicate asymptotic estimate: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the proposed auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an auxiliary observable whose exact multiplicative simplification still leaves information beyond `M(x)`.

## Treat observation category and family energy as source currencies

The endpoint history now gives a precise hierarchy. Generic coding capacity does not distinguish the source. Smooth-modulus zero-free information can be too coarse in resolution. Ordinary interval cancellation can target the wrong population. But a prime-supported family mean-square theorem can close the endpoint because it sees exactly the population and simultaneous coherence the construction consumes, and MC-322 shows that the natural currency is total squared bias rather than family cardinality alone.

Future arguments should therefore simplify source observables first, retain matched controls, then ask whether the available theorem is stated in the **same observation category** as the endpoint and whether it controls the whole family-energy profile rather than one character at a time. “Zero-free,” “small interval sums,” “primitive,” or “source-generated” are not useful labels until that transfer is explicit.
