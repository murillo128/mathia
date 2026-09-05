# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Classify complete retained interaction support before proposing repair

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-005-test-family-fidelity-has-scale-and-dimension-gates`, and `MI-006-interaction-support-governs-marginal-fidelity`.

Linear span, generated sigma-algebra, multiplicative closure, and source-dependent interaction depth are different information categories. A useful repair must target the exact missing interaction rather than add more channels of the same order.

## Quantify stability and cross-scale non-escape, not only exact recoverability

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision` and `MI-008-compact-fidelity-needs-cross-scale-witness-compactness`.

Exact recovery can coexist with arbitrarily bad conditioning, and per-scale witnesses can escape every compact set. A concrete application must supply a source-natural stability modulus, coherent approximant tower, compact-transversal margin, or equivalent width decay.

## Derive the source metric/statistical category, then prove the relevant score or spectral mass survives compression

**Linked intuitions:** `MI-003-fidelity-endpoints-are-category-dependent`, `MI-010-spectral-fidelity-needs-ideal-budget-and-relative-scale-tightness`, `MI-012-regular-recovery-orders-the-full-multiscale-information-profile`, and `MI-014-target-relative-spectral-fidelity-is-projection-geometry`.

AF-135--AF-138 show that fixed-target fidelity under full generator gauge is projection geometry until an independently source-specified metric upgrades the invariant to the generalized pencil `(G,M)`. AF-139 closes the covariance-only choice: full affine naturality forces `M` to be proportional to `C^{-1}`, making the generalized spectrum exactly output PCA geometry and imposing a second-order information ceiling.

AF-140 opens a strictly richer but category-sensitive route. A source-natural smooth translation law supplies the full-law Fisher metric `J`, with `J>=C^{-1}` and equality only at the Gaussian boundary. AF-141 then gives the exact downstream gate: under a parameter-independent observation the retained score is the conditional score and Fisher loss is `E[Cov(S|Y)]`.

A decisive arithmetic application must therefore derive its probability/statistical family from source structure rather than arbitrary smoothing, identify the tangent/score directions carrying the intended discriminator, and prove those directions survive the actual compression quantitatively. Metric canonicity without score non-escape is not fidelity.

## Construct the minimal witness saturation required for composition, then justify why that witness class is natural

**Linked intuitions:** `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-009-quotient-repair-has-category-regularity-and-naturality-gates`, and `MI-013-witness-relative-recovery-geometry-needs-natural-composition`.

AF-126--AF-134 make approximate fidelity witness-relative and show exactly why stagewise recovery need not compose. Backward witness saturation gives the minimal convex symmetric family making every stage visible to all downstream tests.

The remaining burden is concrete rather than abstract: derive the destination witness body and its pullbacks from the source and show the resulting saturation remains tractable and natural rather than becoming an after-the-fact encoding of the desired answer.
