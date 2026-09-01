---
id: RGR-AF-CATEGORY-001
type: research-graph-relation
scope: arithmetic_fidelity
relation: category-dependent-fidelity-endpoints
derived: true
---

# Category-dependent fidelity endpoints

Central intuition: [[research/arithmetic_fidelity/mind/intuition/MI-003-fidelity-endpoints-are-category-dependent]]. The current findings make the retained category itself part of an exact fidelity statement.

[[research/arithmetic_fidelity/findings/AF-012-strictly-convex-f-divergence-equality-is-binary-statistical-fidelity|AF-012]]--[[research/arithmetic_fidelity/findings/AF-019-exact-logarithmic-derivative-retains-zero-free-factor|AF-019]] establish the earlier category boundary across statistical sufficiency, Gram compression, multiplicative monoids and analytic layers.

The zero-error stochastic branch now makes the metric dependence explicit. [[research/arithmetic_fidelity/findings/AF-046-zero-error-fidelity-has-zero-tv-robustness|AF-046]] separates ordinary distribution-law row separation from exact support-disjoint zero-error fidelity: the former has an exact positive TV margin while the latter is generically nonrobust. [[research/arithmetic_fidelity/findings/AF-047-zero-error-tv-repair-is-bayes-error-plus-hall-coverage|AF-047]] and [[research/arithmetic_fidelity/findings/AF-048-row-sup-zero-error-repair-is-max-min-allocation|AF-048]] show that the same zero-error target has different exact projection geometry under average and worst-row TV. [[research/arithmetic_fidelity/findings/AF-049-kl-direction-separates-support-barrier-from-nash-repair|AF-049]] makes even divergence direction decisive: forward KL gives an infinite support barrier while reverse KL becomes a Nash-welfare partition problem.

[[research/arithmetic_fidelity/findings/AF-050-f-divergence-zero-error-repair-reduces-to-binary-penalties|AF-050]] proves that row-separable Csiszár divergences share one class-partition combinatorics with divergence-specific retained-mass penalties. [[research/arithmetic_fidelity/findings/AF-051-quadratic-zero-error-repair-is-clone-granularity-sensitive|AF-051]] then marks the boundary of that reduction: quadratic/Brier repair remains partition-exact but depends on discarded concentration and support cardinality and changes under statistically reversible output cloning.

Together these support only the scoped rule that a fidelity claim must specify the retained observable class, gauge, topology/language, metric/divergence and analytic layer before recovery, robustness or repair cost is asserted.
