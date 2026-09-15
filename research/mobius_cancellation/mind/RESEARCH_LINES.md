# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Only pursue reciprocal-endpoint variants that escape the prime-family mean-square obstruction

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-041-smooth-modulus-zero-free-control-stops-above-the-dyadic-shell-scale`.

MC-307--MC-317 reduce the generic endpoint to a constant-defect generalized-Hamming/code problem and show that generic half-rate binary codes can realize the required profile. MC-319 then finds genuine arithmetic structure in the natural source: a smooth common radical gives strong family zero-free information, but the available Rodosskii conversion is too coarse for the one-dyadic-shell endpoint. MC-320 proves that even almost-perfect cancellation on ordinary integer intervals can coexist with maximal bias on the exact prime shell.

MC-321 closes the natural reciprocal endpoint without the primitive-conductor theorem that MC-320 appeared to demand. The endpoint supplies `R` distinct characters with a fixed nonvanishing bias on the **same dyadic prime shell**, all embedded in one common modulus `q<=4y^2`. The prime Halász--Montgomery small-family estimate of Puchta/Klurman--Mangerel--Teräväinen applies directly to arbitrary prime-supported coefficients and makes that simultaneous bias impossible. More generally the contradiction survives for `q<=y^(8/3-delta)`, `R->infinity`, `R=o(log y)` and fixed-size bias.

Thus primitive conductor provenance, smoothness, zero-free regions and ordinary interval estimates are not the live gate for this exact endpoint. The decisive resource is the conjunction of **prime-supported observation + a growing family of distinct simultaneously biased characters + a common modulus below the mean-square threshold**.

A surviving endpoint variant must first escape one of those hypotheses: lose the growing strongly biased family, cease to admit one controlled common modulus, move beyond the prime Halász--Montgomery modulus range, or change the reciprocal one-defect partition enough that the family-energy lower bound disappears. Sharpening individual-character zero-free or interval estimates for the closed model is no longer useful.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before any delicate asymptotic estimate: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the proposed auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an auxiliary observable whose exact multiplicative simplification still leaves information beyond `M(x)`.

## Treat observation category and family energy as source currencies

The endpoint history now gives a precise hierarchy. Generic coding capacity does not distinguish the source. Smooth-modulus zero-free information can be too coarse in resolution. Ordinary interval cancellation can target the wrong population. But a prime-supported family mean-square theorem can close the endpoint because it sees exactly the population and simultaneous coherence the construction consumes.

Future arguments should therefore simplify source observables first, retain matched controls, then ask whether the available theorem is stated in the **same observation category** as the endpoint and whether it controls the whole biased family rather than one character at a time. “Zero-free,” “small interval sums,” “primitive,” or “source-generated” are not useful labels until that transfer is explicit.
