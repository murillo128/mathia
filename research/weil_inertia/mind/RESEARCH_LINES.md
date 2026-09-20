# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Reconstruct the full diagonal transport and a source-aware quantitative reserve

**Linked intuitions:** `MI-010-pair-correlation-slack-is-a-shared-exceptional-budget`, `MI-029-post-threshold-compact-positivity-needs-noncompact-tail-retention-not-a-canonical-finite-rank-correction`, `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing`, `MI-051-local-threshold-continuity-does-not-bootstrap-cofinally-from-an-energy-budget-alone`, `MI-052-common-cut-short-preserves-inherited-pivot-without-double-spending`, and `MI-053-odd-parity-couples-difference-and-image-kernels-before-half-density-transport`.

WI-363--WI-364 expose two independent source-to-cell bookkeeping channels missing from a termwise kernel transport: the half-density change of a quadratic difference form creates a nonconstant diagonal multiplier `W_A`, and odd parity creates a regular gamma image term alongside the singular Carleman image.

WI-365 settles the sign of the latter in the favorable direction. The exact gamma image is positive in the localized form, so it may be discarded when proving a lower bound. That does **not** establish the quantitative Carleman/OSPR reserve used downstream. WI-366 proves that the obvious repair cannot work uniformly: the true image `J_A` becomes a boundary-layer Hankel channel as `A` grows and cannot dominate a fixed positive multiple of the scale-invariant bare Carleman operator.

The source-to-cell audit therefore has two sharp remaining obligations. First, reconstruct every diagonal/scalar/endpoint term through the full odd-fold plus half-density transport and determine the actual fate of `W_A`. Second, establish the provenance of the quantitative rebound required by the cofinal induction: exhibit a genuinely surviving bare-Carleman channel, prove a source-aware `A`-dependent reserve for `J_A`, or reorganize the induction so the printed fixed reserve is unnecessary.

Until both are established, the common-cut/inherited-pivot algebra of WI-362 remains a useful **conditional** theorem, while the later finite certificate, tail and cofinal RH steps remain downstream of an unverified normalization/reserve bridge.

## Keep positivity of an omitted term, quantitative reserve, exact form transport and global positivity distinct

A positive image term can safely be dropped for sign and still be far too weak to finance a fixed coercive reserve. Conversely, failure of the comparison `J_A >= cK` does not prove that the full theorem or every source-aware reserve is false. WI-366 closes one repair mechanism, not the whole rooted-operator program.

Future audits should work with the complete quadratic form on a common core and keep the boundary-layer scaling explicit. No downstream numerical certificate should inherit a Carleman constant until its exact source channel has been derived after parity, Jacobian and endpoint bookkeeping.