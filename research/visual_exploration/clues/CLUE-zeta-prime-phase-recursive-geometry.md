---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
  - research/visual_exploration/findings/VIS-064-hybrid-independent-scale-transfer-error-bound.md
  - research/visual_exploration/findings/VIS-065-hybrid-contrast-single-factor-residual-coordinate.md
  - research/visual_exploration/findings/VIS-066-hybrid-joint-field-factor-residual-shear.md
  - research/visual_exploration/findings/VIS-071-finite-prime-vertical-flow-shared-phase-haar-law.md
  - research/visual_exploration/findings/VIS-083-gram-point-prime-phase-haar-equidistribution.md
  - research/visual_exploration/findings/VIS-084-gram-short-block-prime-phase-freezing.md
  - research/visual_exploration/findings/VIS-085-gram-local-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-086-quadratic-gram-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-087-finite-order-gram-clock-null-hierarchy.md
  - research/visual_exploration/findings/VIS-088-polynomial-sensitivity-observables-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-089-inverse-polynomial-decision-margins-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-090-consecutive-gram-superlog-prime-torus-haar.md
  - research/visual_exploration/findings/VIS-091-gram-log-lag-increment-clock-collapse.md
  - research/visual_exploration/findings/VIS-150-gram-superlog-lag-second-clock-transition.md
  - research/visual_exploration/findings/VIS-151-gram-exact-lag-shear-haar.md
  - research/visual_exploration/findings/VIS-152-gram-joint-lag-finite-difference-threshold.md
  - research/visual_exploration/findings/VIS-153-gram-critical-lag-newton-product-law.md
  - research/visual_exploration/findings/VIS-154-gram-fixed-irregular-lag-vandermonde-threshold.md
  - research/visual_exploration/findings/VIS-155-gram-irregular-critical-haar-fiber-curve.md
  - research/visual_exploration/findings/VIS-156-gram-fixed-affine-subsampling-clock-null.md
  - research/visual_exploration/findings/VIS-157-quadratic-gram-index-pairwise-haar-triple-clock.md
  - research/visual_exploration/findings/VIS-158-polynomial-gram-index-d-wise-haar-threshold.md
  - research/visual_exploration/findings/VIS-159-power-law-gram-index-ceiling-haar-threshold.md
  - research/visual_exploration/findings/VIS-160-growing-degree-diagonal-gram-selector-complete-haar.md
  - research/visual_exploration/findings/VIS-161-two-prime-phase-height-injective-noncontinuous.md
  - research/visual_exploration/findings/VIS-162-prime-phase-lipschitz-decoder-collision-quotient.md
---

# Can a zeta visual statistic leave the regular prime-torus representation class after the full Gram-clock quotient?

## Observation

The prime-phase program has progressively removed representation and sampling effects that can look arithmetically structured without adding a new usable mechanism. `VIS-064`--`VIS-066` show that invertible hybrid factor/residual recombinations do not create information, while `VIS-083`--`VIS-091` and `VIS-150`--`VIS-156` show that the deterministic Gram clock can generate Haar populations, coherent lag fields, critical Haar fibers, irregular-delay geometry, and sparse affine samples from the same fixed-prime state.

`VIS-157`--`VIS-159` classify increasingly rich fixed-complexity index selectors. A degree-`d` polynomial selector is Haar through `d` fixed samples and exposes a deterministic moment-null character at `d+1`; the full fixed power family `floor(n^alpha)` has the corresponding threshold `ceil(alpha)`. `VIS-160` then diagonally glues polynomial stages of increasing degree into one strictly increasing deterministic selector `K(n)` such that every fixed finite sample-order/fixed-prime character test is eventually Haar. Selector complexity growing with height is therefore not itself a new information source.

`VIS-161` adds a different representation boundary. For any two distinct primes `p,q`, the exact phase pair `(p^(-it),q^(-it))` is already injective in the real height `t`, even though its dense-orbit inverse is nowhere continuous. Consequently every same-height analytic coordinate is set-theoretically a function of two exact prime phases. Raw information or unrestricted measurability is therefore too permissive a discriminator: the unresolved content lies in stable, regular, complexity-controlled recoverability from the admitted phase/clock representation.

`VIS-162` now closes one regularity subproblem exactly. For any fixed finite prime set `P` with at least two primes and the chordal Euclidean torus metric, the smallest Lipschitz constant of an exact decoder for an observable `A` on a height set `S` is

`Lambda_P(A;S)=sup_(t!=u in S) |A(t)-A(u)|/||Phi_P(t)-Phi_P(u)||_2`.

Kirszbraun extension makes this pairwise collision bound sufficient as well as necessary. Thus the Lipschitz branch does not require searching over decoder architectures: it reduces exactly to the growth of a phase-collision quotient. The remaining difficulty is source-side — proving that a zeta-facing coordinate has a collision profile that cannot be explained by the same phase/clock recurrence and normalization effects.

## Research question

After quotienting the prime-torus population law, the fixed finite Gram-clock hierarchy, fixed affine thinning, fixed polynomial/power selectors, the `VIS-160` diagonal growing-complexity control, the pathological exact-height encoding of `VIS-161`, and the exact Lipschitz-decoder reduction of `VIS-162`, does any zeta-facing visual statistic escape a predeclared **regular prime-phase/clock representation class** in a source-sensitive way?

A remaining sampling route must contain quantitative structure that the diagonal construction cannot absorb: for example a pre-specified natural selector together with a test whose order, prime support, character complexity, or resolution grows with height at a controlled rate. For analytic-coordinate routes, the decoder class and observable normalization must be frozen before inspecting favorable residuals. Lipschitz recovery is now one explicit solved representation class; bounded Fourier/character complexity, finite-resolution recovery, controlled moduli of continuity, computational complexity, or other stable classes remain legitimate alternatives when stated precisely.

## Why it may matter

The control class is stronger than any collection of fixed-dimensional scatter plots or finite-order Haar tests. Even seeing correct Haar behavior at every fixed finite order, considered one order at a time, does not force stochasticity or a new arithmetic source; deterministic completely-uniform-distribution phenomena and `VIS-160` give exact controls of that inference.

At the same time, `VIS-161` shows that demanding an analytic coordinate be absent from the exact phase state is impossible in a raw information sense: infinite-precision phase data can encode height through a violently discontinuous inverse. `VIS-162` sharpens the next boundary: for Lipschitz recovery, the entire decoder problem is equivalent to one collision profile. A useful positive result therefore has to be quantitative and source-sensitive, not merely visually different from an Euler-product picture or difficult for a chosen decoder implementation.

## Decisive test

Use `VIS-150`--`VIS-156` for fixed lag geometry and affine thinning, `VIS-157`--`VIS-159` for fixed polynomial/power selectors, `VIS-160` for arbitrary fixed finite-order tests under an adversarial deterministic selector whose local degree grows with height, `VIS-161` for the distinction between exact set-theoretic encoding and regular recoverability, and `VIS-162` for the exact Lipschitz-decoder criterion.

Do **not** treat any fixed collection of Haar, decorrelation, scatter, lag, or product-character tests as source evidence merely because all of them pass. `VIS-160` can absorb every such fixed test eventually. Likewise, do not claim that Hardy `Z`, zero occupancy, or another same-height coordinate is informationally independent merely because no simple formula from a few prime phases is known: `VIS-161` shows that exact phase pairs already identify height.

For a Lipschitz analytic-coordinate test, freeze before inspection: the finite prime set `P`, chordal metric, observable and normalization, expanding height windows, and matched controls. Then study

`Lambda_P(A;T)=sup_(t!=u in [-T,T]) |A(t)-A(u)|/||Phi_P(t)-Phi_P(u)||_2`.

A global bounded Lipschitz decoder exists exactly when this profile stays bounded. At finite decoder budget `L`, any proposed uniform approximation with error `epsilon` must also satisfy the collision-excess lower bound from `VIS-162`. A positive source claim requires more than growth of `Lambda_P`: the same frozen statistic must separate the zeta observable from the matched deterministic phase/clock controls or from an explicitly justified source-free baseline.

For non-Lipschitz decoder classes, formulate the corresponding frozen complexity budget before examining the positive residual and prove a reconstruction lower bound or representation invariant that the class cannot reproduce. For sampling-based escapes, specify a selector independently of success and prove a quantitative theorem for a jointly growing test family, with enough uniformity to prevent the `VIS-160` diagonal clock from postponing each fixed test.

## Evidence boundary

`VIS-150`--`VIS-159` are fixed-complexity asymptotic controls. `VIS-160` is an existential diagonal construction: it shows that one deterministic increasing selector can pass every fixed finite-dimensional character test, but it supplies no useful convergence rate and no uniform theorem when test complexity grows with height.

`VIS-161` is a representation boundary, not an analytic reconstruction theorem. It proves exact injectivity of a two-prime phase coordinate and the nowhere continuity of its inverse; it does not provide a stable decoder for zeta values, Hardy `Z`, derivatives, zero occupancy, or zero geometry.

`VIS-162` is an exact **class characterization**, not a zeta-specific separation theorem. It proves that finite-prime chordal Lipschitz decoding is equivalent to a pairwise collision quotient and gives a necessary approximate-decoding lower bound. It does not prove that any chosen zeta observable has a divergent or unusually large collision profile, nor that such growth would be arithmetic-specific without matched controls.

Accordingly, the current corpus does not rule out a natural explicit changing-complexity selector with strong quantitative uniformity, a jointly growing statistic that outruns the diagonal clock, or a stable analytic coordinate that provably requires more regular complexity than a matched phase representation. None of these Gram-clock, phase-injectivity, or decoder-classification results is a stronger zeta criterion or an RH consequence.

## Research disposition

Accepted in further narrowed form. Fixed finite commensurate lag geometry, fixed affine thinning, all fixed polynomial/power-law selectors, and generic growth of selector complexity by itself are closed as positive information escapes on fixed prime support. `VIS-161` closes raw information absence as a useful analytic-coordinate criterion, and `VIS-162` closes the abstract **exact Lipschitz decoder search**: under the fixed chordal finite-prime representation its optimal constant is already the explicit collision quotient.

Continue only through a genuinely quantitative changing-complexity law under pre-specified controls, a separately derived nonclock sampling mechanism that survives the same quantitative audit, a zeta-facing collision profile that separates from matched phase/clock controls, or an analytic coordinate separated within another explicitly frozen regularity, stability, resolution, or computational-complexity class.
