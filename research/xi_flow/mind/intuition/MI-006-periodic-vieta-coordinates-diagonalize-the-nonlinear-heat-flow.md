# MI-006 — Periodic Vieta coordinates diagonalize the nonlinear zero heat flow, and their source-visible conditioning is benign

**Evidence level:** exact periodic nonlinear theorem through XF-067, quantitative Newton conditioning through XF-068, and exact translated-window extraction through XF-069

## Core intuition

The Cauchy multiplier seen in the arithmetic-lattice tangent flow is not merely a linear artifact. On a periodic zero system, symmetric Vieta coordinates of the unit-circle root variables diagonalize the full backward heat evolution exactly and remain regular through collisions and complex-root intervals. The two obvious algebraic conditioning concerns are also now removed: source-small power sums do not blow up under the forward Newton map, and a translated compact selector recovers source-visible periodic power sums without a growing period-length penalty.

The hard issue has moved from periodic algebra to **which Vieta sector the source can actually see and how accurately the real Xi window can be replaced by a periodic carrier**.

## Strongest justified principle

XF-064--XF-066 show that the destination measurement no longer requires infinitesimal dynamics: after quotienting translation, sufficiently slow gap distortion and local finite-difference control make the exact moved-point selector a perturbation of the established lower frame.

XF-067 supplies the collision-safe nonlinear state representation. Each periodic Vieta coefficient evolves autonomously with rate `4 pi^2 k(N-k)/L^2`; at the arithmetic lattice its first variation is exactly one discrete root-displacement Fourier mode, recovering the XF-062 tangent semigroup.

XF-068 makes the growing Newton bridge quantitative. If raw power sums are uniformly source-small, every corresponding low Vieta coefficient is at most the same smallness, independently of the number of controlled modes. After fixed positive heat time, reconstructing low power sums from the damped Vieta coefficients costs only a polynomial factor in the reciprocal Cauchy rate, hence only a fixed power of `log T` at the Xi scaling.

XF-069 then shows that the compact taper is not an inverse problem. Translating its center through one period and taking the matching center-Fourier coefficient recovers each periodic power sum exactly with a constant depending only on the fixed window value `chi(0)`, not on the growing period. The remaining nonperiodic error is the center-averaged mismatch between the actual Xi statistic and its periodic surrogate.

## What remains possible

The source-visible band starts above the fixed Vieta modes, so the full `P_1,...,P_K` smallness hypothesis used conditionally in XF-068 is stronger than the current Xi source theorem. XF-069 shows that this need not be fatal: fixed ultra-infrared modes can be order one while the destination third-difference transition energy tends to zero. The next state should therefore weight or quotient Vieta coordinates by their destination relevance rather than demand source control of every low mode.

A separate localization theorem must bound the Xi/periodic interface mismatch on the source-visible band, and a positive-`Lambda` transition must still be shown to produce nontrivial mass in the destination-weighted Vieta resource.

## Status / novelty

Fourier heat evolution, Vieta/Newton identities, symmetric collision-safe coordinates, and periodic convolution/Fourier extraction are classical ingredients. The durable line-specific synthesis is: **the periodic nonlinear zero flow has an exact diagonal collision-safe state space, and neither Newton combinatorics nor compact-window inversion is the remaining bottleneck; source visibility and nonperiodic interface control are.**

## Falsification criterion

Invalidate the exact Vieta heat rates, their collision-safe analytic continuation, the XF-068 Newton majorants, or the XF-069 translated-center extraction identity; or show that the destination transition necessarily depends on the source-unresolved ultra-infrared modes in a way not captured by the current third-difference controls.
