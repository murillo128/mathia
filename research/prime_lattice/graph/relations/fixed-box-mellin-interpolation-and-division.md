---
id: RG-fixed-box-mellin-interpolation-and-division
type: research-graph-relation
scope: prime_lattice
derived: true
---

# Fixed-box Mellin interpolation and division

[[research/prime_lattice/graph/prime-lattice|Prime Lattice]] · [[research/graph/atlas/territories/RA-A1-zero-free-regions-pnt-error|Analytic localization territory]]

These sources distinguish unrestricted sparse-zero annihilation, universal preservation of a box range, and one specially compatible interpolant. The relationships are explicitly stated in the findings; no fixed-box solution is inferred.

- [[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]], §1, constructs compact smooth Mellin annihilators from Gevrey inputs using a genus-zero product of order below one. Its subsequent finite box inverse gives a controlled approximation, not exact membership in a prescribed fixed-box range.
- [[research/prime_lattice/findings/PL-486-subunit-order-mellin-filters-cannot-preserve-a-fixed-box-range|PL-486]], §§1–3, explicitly tests that construction as a universal repair. For a fixed nonzero box harmonic, preservation for every mean-zero Gevrey input forces the entire Mellin symbol to be constant. This does not exclude a specially chosen input depending on the zero set.
- [[research/prime_lattice/findings/PL-487-sparse-mellin-division-preserves-gevrey-decay-and-support|PL-487]], §§1–4, removes one obligation from that special-input question. For multiplicity-counted zero growth \(n(R)=O((1+R)^a)\), \(0<a<1\), a compact Gevrey input of order \(1<q<1/a\) whose transform cancels every required multiplicity has an entire quotient with strip decay \(\exp(-c|\tau|^{1/q})\). Division preserves the Gevrey order and the closed convex hull of support.

The division proof uses a surrounding-circle product lower bound with loss \(O(R^a\log R)\), absorbed by the stronger exponent \(1/q>a\), then the [[research/prior_art/incremental/PA-paley-wiener-l2-exponential-type|classical L2 Paley–Wiener theorem]] for support containment. No zero-spacing assumption is added. Full Hermite cancellation, not simple cancellation at multiple poles, is essential. Constants may depend on the full product.

For an already existing box-range interpolant, the quotient decay is therefore automatic in this Gevrey class. The resulting factorization does not put the divided function back in the box range, make arbitrary filtered inputs compatible, or upgrade a smooth interpolant to Gevrey. PL-486's universal obstruction survives. Infinite fixed-box interpolation, arithmetic variance ceilings, and independent adversarial approval remain absent. This is a conditional analytic reduction using classical ingredients, without an external novelty or RH/GRH claim. A1 remains `active` with unchanged mass.
