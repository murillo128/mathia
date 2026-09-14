# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Break fixed-base aliasing before coupling the annihilator and compression budgets

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`, `MI-007-aliased-radial-prediction-has-a-positive-szego-floor`, `MI-008-finite-blaschke-defects-are-silent-in-terminal-scalar-energy`, `MI-009-summable-horizontal-zero-mass-keeps-full-terminal-gram-entropy-bounded`, `MI-010-growing-depth-mobius-annulus-exposes-off-critical-blaschke-amplification`, `MI-011-canonical-deflation-cancels-raw-cauchy-crowding-volume`, `MI-012-three-state-transverse-confluence-exposes-collective-shear`, `MI-013-absolute-height-and-global-zero-counts-are-invisible-to-the-collective-shear-obstruction`, `MI-014-quadratic-horizontal-tangency-is-the-three-state-conditioning-threshold`, `MI-015-confluent-volume-is-curvature-blind-and-controlled-by-radial-depth`, `MI-016-growing-confluent-rank-is-limited-by-endpoint-extrapolation-cost`, `MI-017-finite-high-zero-target-access-requires-a-target-bearing-compression-near-kernel`, `MI-018-actual-zero-power-packets-pay-logarithmic-confluent-rank-for-perfect-harmonic-profile-capture`.

NB-115--NB-122 localize the finite-section escape and show that increasingly rich exact Nyman source equations, including the entire nested cutoff prefix, still admit one generic inverse-section repair with perfect visible target capture. Ordinary nested same-source coherence is therefore exhausted as an independent resource.

NB-123 supplies the first exact source-faithful separator. On a geometric grid, a finite actual zero-power primitive obeys an annihilating recurrence whose order is at most its total confluent multiplicity `d(F)`. Perfect target capture forces the missing harmonic root `q^-1`, which is not a characteristic root of any actual nontrivial zero. NB-124 stabilizes that separator with the normalized annihilator margin `mathfrak s_(F,q)`, giving every fixed finite packet a cutoff-uniform positive target-angle gap.

NB-125 removes the coarse dependence on only the rightmost zero. Keeping the product structure of the annihilator and its natural weighted coefficient norm gives the rootwise lower bound

`mathfrak s_(F,q) >= (1-q^-1) D_q^(2d) product_(rho in F)(1-Re rho)^2`,

with `D_q=(log q)/(2sqrt(q))`. Hence polynomially near-perfect capture forces an additive bill in the individual horizontal depths. Combining this with the explicit Vinogradov--Korobov zero-free region yields

`(alpha/2) log R <= d log(K_VK/D_q) + (2/3)sum loglog|gamma| + (1/3)sum logloglog|gamma| + O_q(1)`

whenever `chi_(F,R)>=1-R^-alpha` and the recurrence is visible.

Rank and height are therefore not independent escape variables. If all packet ordinates are polynomial in `R`, then near-perfect capture forces

`d(F) >= (3alpha/4+o(1)) log R/loglog R`.

At fixed rank, the same capture forces maximum height at least `exp(R^(3alpha/(4d)-o(1)))`. Horizontal approach to `Re s=1` is no longer free: actual zeta zeros must pay for it root by root through height entropy.

NB-126 shows that the previously proposed direct scalar bridge to `NB-116` is still too coarse at one fixed geometric base. A vertical shift by `2pi/log q` leaves every `q`-geometric zero-power trace, the annihilator polynomial and `mathfrak s_(F,q)` exactly unchanged, while the elementary Burnol defect decays like `1/gamma^2`. Formal alias lifts can therefore drive the packet target mass arbitrarily close to zero without moving the fixed-base recurrence geometry; they can also be placed high enough to satisfy the same one-sided Vinogradov--Korobov and horizontal-first-moment numerical envelopes. This is a representation-level matched control, not an actual-zero construction.

The remaining bridge must therefore break aliasing **before** the recurrence and height information are scalarized. Two multiplicatively independent bases have no common nonzero vertical alias period, so a joint `q=2,3` annihilator/target certificate, or a statistic retaining the full natural-grid primitive, can in principle see absolute ordinate information that one fixed base loses. The live theorem is to derive a target-bearing compression lower bound from such a joint non-aliased statistic while keeping enough phase/root identity to combine with actual zero-density and zero-free information. Applying separate rootwise radial bounds first will simply discard the information that NB-126 says is needed.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep target baseline, continuum mass, recurrence rank, rootwise horizontal depth and height entropy separate

NB-118--NB-122 separate exact source equations from source representation. NB-123 identifies finite recurrence rank as a genuine source constraint. NB-124 makes the missing-root annihilator margin the stable destination-aware separator. NB-125 then decomposes that margin rootwise and converts horizontal depth into an explicit rank--height budget for actual zeta zeros. NB-126 adds a second separation: a fixed-base recurrence margin is periodic in ordinate, while Burnol target mass is an absolute-height observable.

A fixed packet is quantitatively separated from the inverse-section extremizer, and even growing packets cannot trade all horizontal depth to one exceptional rightward zero for free. But a one-base scalar recurrence summary cannot itself be coupled coercively to the high-zero Burnol tail, because exact alias lifts preserve the former while erasing the latter. The next source-faithful interface must retain non-aliased joint information—multiple multiplicatively independent bases, the full integer-cell primitive, or an equivalent rootwise compression statistic—before converting it to scalar energy or height budgets.