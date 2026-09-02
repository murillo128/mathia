# MI-007 — Stable fidelity is distance from the admitted collision boundary, and repair is category-relative

**Evidence level:** supported by exact Hilbert, Euclidean, smooth strongly-convex, polyhedral, Lipschitz, finite-channel, metric-refinement, powered-lift, and horofunction classifications

## Core intuition

Exact recoverability, stable recoverability, and distance to a repaired target are different claims. Stability is controlled by distance from the relevant collision set in the **specific perturbation geometry**, while a repair radius becomes intrinsic only after both target transport and the source metric category are fixed.

The newer safe-lift results sharpen the category dependence. Smooth strongly-convex norms recover a robust convex-hull phase diagram and a genuine higher-order boundary exponent, whereas polyhedral norms retain first-order provenance through norming faces and collapse every finite powered threshold to one dual-face coherence test. There is therefore no category-free meaning to a critical repair exponent.

## Strongest justified principle

AF-041--AF-054 identify stable fidelity with quantitative distance from admitted collisions and isolate target transport. In particular the maximal safe envelope under an isometric refinement characterizes exactly which target enlargements preserve every source repair radius.

AF-055--AF-063 show that higher-order repair is controlled by weighted positive distance excess and that the first smooth horofunction layer sees only signed distance to `conv(S)`. Arbitrarily small renorming can change fixed-base liftability, and an `ell^r` source moves the critical product exponent to `r`.

AF-064--AF-065 show that this instability narrows under genuine geometric hypotheses. In finite-dimensional strongly convex reversible Minkowski spaces the Euclidean phase diagram is restored: power `1` admits every base point, `1<p<=2` admits exactly `conv(S)`, and `p>2` admits `S union int(conv(S))`. On the hull boundary, the exact support-contact profile controls the residual excess and therefore the critical higher-order exponent.

AF-066--AF-068 give the nonsmooth counter-regime. For polyhedral norms, first-order safe lifting is governed by the whole norming face, not merely the convex hull. The safe kernel is an exact finite cone hull, its inclusion order is generator cofinality, and every finite power `p>1` has the same pass/fail boundary. Nonsmooth geometry can therefore preserve target provenance that smooth first-order convexification erases.

## What remains possible

The live problem is to identify representation categories in which collision geometry, target transport, norming-face data, and any higher-order contact exponent are all forced by the mathematical construction. A higher-order invariant is meaningful only after proving it stable under the declared equivalences; conversely, a polyhedral face invariant is meaningful only if the nonsmooth structure itself is intrinsic rather than a chosen encoding.

For arithmetic applications, a discriminator should pass three independent tests: positive distance from matched-control collisions; target descent through information-preserving equivalences; and invariance of the relevant smooth-contact or nonsmooth-face boundary under the admitted representation class.

## Status / novelty

The functional-analytic, coapproximation, convex-hull, horofunction, polyhedral duality, and norm-comparison mechanisms are classical or direct. The Mathia synthesis is the joint gate: **robust fidelity is relative to a collision geometry; robust repair is additionally relative to target transport; and the form of higher-order boundary fidelity is itself category-dependent**.

## Falsification criterion

Exhibit a covered category where the stated distance or safe-envelope classifier fails, a smooth strongly-convex example violating the AF-064 phase diagram/contact-profile law, or a polyhedral example where powered liftability depends on the exponent despite the same dual-face coherence data.

## Lean-formalizable core

- Range-kernel transversality and closed-secant stability.
- Maximal safe target envelope under isometric refinement.
- Strongly-convex Minkowski powered-lift phase diagram.
- Support-contact profile criterion.
- Polyhedral dual-face coherence and finite cone hulls.
- Weighted-distance-excess equivalence and horofunction margins.