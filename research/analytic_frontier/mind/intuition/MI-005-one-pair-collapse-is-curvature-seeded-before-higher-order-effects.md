# MI-005 — One-pair vertical geometry now reduces to growing multiplicity-scale complexity

**Evidence level:** exact source reduction and literature-backed scalar certificates through ANF-079

## Core intuition

The one-pair vertical problem is no longer controlled by support cardinality alone. Fixed support, uniform occupancy, bounded maximum occupancy, and even arbitrarily large multiplicities distributed among only finitely many geometric occupancy bands can all be neutralized by the real central-notch certificate after the appropriate thinning/reweighting.

The surviving scalar difficulty is therefore more specific: a bad family must use **more and more genuinely different multiplicity scales** as the notch narrows, while also avoiding collapse to the already-closed fixed-support regimes. Large multiplicity without scale complexity is not enough.

## Strongest justified principle

ANF-075 proves that every fixed support cap can be escaped by narrowing the notch. ANF-076 proves that unbounded support with uniform occupancy is still controlled exactly. ANF-077 supplies the superlevel-set decomposition for arbitrary heterogeneous occupancies and isolates the explicit penalty `P(k)` together with the heterogeneity term that a central notch must absorb.

ANF-078 then removes every fixed maximum-occupancy class, uniformly in support cardinality, by Bernoulli thinning. ANF-079 sharpens the result further: if the nonzero multiplicities occupy only a fixed number of geometric bands, the certificate still closes uniformly even when both support size and maximum multiplicity diverge. Equivalently, the remaining scalar obstruction cannot be summarized by “many points” or “large weights”; it must have unbounded **multiplicative scale complexity**.

This is a stronger localization of the one-pair frontier than the earlier support-growth statement. It does not establish that an escaping family exists. It identifies what any such scalar family would have to do before complex height, ordering, or multi-pair structure becomes relevant.

## What remains possible

A scalar family whose occupied multiplicity bands proliferate with the notch scale may defeat all current bounded-complexity certificates. The correct next invariant might be an entropy, covering number, layer-cake complexity, or another scale-sensitive functional of the occupancy profile, but no particular choice is established yet.

Ordered carriers, complex height, and multi-pair geometry remain separate escape categories because they retain information that collapsed real multiplicity discards. They should be reopened only if the scalar scale-complexity envelope is either closed or shown by an explicit admissible family to be insufficient.

## Status / novelty

The thinning, layer-cake, and geometric-band ingredients are classical mechanisms specialized to the persisted one-pair scalar problem. The durable synthesis is the frontier classification: **bounded multiplicity-scale complexity is not enough to obstruct the real central-notch strategy; any surviving scalar obstruction must develop unbounded occupancy-scale complexity.** No RH consequence or novelty claim follows from that classification.

## Falsification criterion

Exhibit an admissible scalar one-pair family with uniformly bounded geometric occupancy-band complexity that defeats the ANF-079 certificate under its stated hypotheses; show that ANF-078 fails for a fixed maximum-occupancy class; or derive a new uniform certificate that also closes every growing-band occupancy profile. Any of those would materially change this intuition.
