# MI-007 — Stable fidelity is distance from the admitted collision boundary, and repair is category-relative

**Evidence level:** supported by exact Hilbert, Euclidean, smooth strongly-convex, polyhedral, Lipschitz, finite-channel, metric-refinement, powered-lift, horofunction, finite-moment class-separation, and infinite-dimensional Gaussian nuisance-closure results through AF-534

## Core intuition

Exact recoverability, stable recoverability, and distance to a repaired target are different claims. Stability is controlled by distance from the relevant collision set in the **specific perturbation geometry**, while a repair radius becomes intrinsic only after both target transport and the source metric category are fixed.

AF-444 gives a sharp arithmetic-fidelity instance of this distinction. For positive unit-weight atoms, one consecutive surplus moment globally forbids the `K`- versus `(K+1)`-atom collision, yet on compact positive nuisance classes the distance between the two observation images is only `Theta(y)` as the extra atom coordinate `y` tends to zero. In the reciprocal-square shell model this is `Theta(m^-2)`. Exact target purity can therefore hold at every finite depth while the stable margin still collapses at the physical tail scale.

AF-534 gives the infinite-dimensional Gaussian form of the same separation. If the target carrier is `u` and the linear nuisance directions form a possibly nonclosed subspace `N` of the Cameron--Martin Hilbert space `H`, exact target aliasing is controlled by membership in `N`, while robust distinguishability is controlled by `dist_H(u, closure(N))`. Thus `u in closure(N) \ N` is an exact example of injectivity without a positive minimax margin: no nuisance value produces an equal law for a distinct target, but nuisance sequences can make the corresponding laws arbitrarily close. For a moving family the effective information is `J_A=delta_A^2 dist_H(u_A,closure(N_A))^2`, and uniform recovery on a fixed compact target interval occurs exactly when `J_A -> infinity`.

The safe-lift results sharpen the same category dependence in a different geometry. Smooth strongly-convex norms recover a robust convex-hull phase diagram and a genuine higher-order boundary exponent, whereas polyhedral norms retain first-order provenance through norming faces and collapse every finite powered threshold to one dual-face coherence test. There is no category-free meaning to a critical repair exponent.

## Strongest justified principle

AF-041--AF-054 identify stable fidelity with quantitative distance from admitted collisions and isolate target transport. In particular the maximal safe envelope under an isometric refinement characterizes exactly which target enlargements preserve every source repair radius.

AF-055--AF-063 show that higher-order repair is controlled by weighted positive distance excess and that the first smooth horofunction layer sees only signed distance to `conv(S)`. Arbitrarily small renorming can change fixed-base liftability, and an `ell^r` source moves the critical product exponent to `r`.

AF-064--AF-065 show that this instability narrows under genuine geometric hypotheses. In finite-dimensional strongly convex reversible Minkowski spaces the Euclidean phase diagram is restored: power `1` admits every base point, `1<p<=2` admits exactly `conv(S)`, and `p>2` admits `S union int(conv(S))`. On the hull boundary, the exact support-contact profile controls the residual excess and therefore the critical higher-order exponent.

AF-066--AF-068 give the nonsmooth counter-regime. For polyhedral norms, first-order safe lifting is governed by the whole norming face, not merely the convex hull. The safe kernel is an exact finite cone hull, its inclusion order is generator cofinality, and every finite power `p>1` has the same pass/fail boundary. Nonsmooth geometry can therefore preserve target provenance that smooth first-order convexification erases.

AF-443--AF-444 add the finite-moment analogue: a collision fibre can exist at equal observation/nuisance dimension and disappear completely after one source-law-sensitive surplus coordinate, while the resulting class margin still tends to zero with the disappearing target atom. The topology of exact identification and the scale of robust identification must be audited separately even when the separating invariant is algebraic and global.

AF-534 adds the completion rule needed in infinite-dimensional nuisance problems: the collision geometry relevant to stability is the **closed** nuisance geometry in the metric selected by the experiment. Algebraic non-membership in an unclosed nuisance span can certify exact identifiability while leaving distance zero, so completion is not a technical convenience but part of the stable-fidelity boundary.

## What remains possible

The live problem is to identify representation categories in which collision geometry, target transport, norming-face data, source-law certificates, nuisance closure and any higher-order contact exponent are forced by the mathematical construction. An exact discriminator is useful only if its distance from the admitted **closed** collision set remains large enough at the destination scale.

For arithmetic applications, a discriminator should pass three independent tests: exact separation from matched-control collisions on the declared source class; target descent through information-preserving equivalences; and a quantitative margin in the perturbation geometry consumed downstream. AF-444 shows why the first test cannot substitute for the third, and AF-534 shows why exact separation from the raw nuisance span does not even imply positive distance from its closure.

## Status / novelty

The functional-analytic, coapproximation, convex-hull, horofunction, polyhedral duality, norm-comparison, Newton--Girard, Cameron--Martin and semiparametric projection mechanisms are classical or direct. The Mathia synthesis is the joint gate: **exact fidelity is relative to a source class; robust fidelity is relative to a closed collision geometry in the experiment's metric; robust repair is additionally relative to target transport; and the form of higher-order boundary fidelity is category-dependent**.

## Falsification criterion

Exhibit a covered category where the stated distance or safe-envelope classifier fails, a smooth strongly-convex example violating the AF-064 phase diagram/contact-profile law, a polyhedral example where powered liftability depends on the exponent despite the same dual-face coherence data, a compact positive unit-atom moment class for which AF-444's exact separation holds but the inter-class distance is not linear in the disappearing atom coordinate up to class-dependent constants, or an AF-534 Gaussian shift family in which uniform nuisance-robust recovery does not follow the stated Cameron--Martin closure distance criterion.

## Lean-formalizable core

- Range-kernel transversality and closed-secant stability.
- Maximal safe target envelope under isometric refinement.
- Strongly-convex Minkowski powered-lift phase diagram.
- Support-contact profile criterion.
- Polyhedral dual-face coherence and finite cone hulls.
- Weighted-distance-excess equivalence and horofunction margins.
- Compact-class `Theta(y)` separation from the Newton--Girard certificate.
