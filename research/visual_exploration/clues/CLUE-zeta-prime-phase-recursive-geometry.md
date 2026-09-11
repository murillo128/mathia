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
  - research/visual_exploration/findings/VIS-163-omitted-prime-phase-no-continuous-finite-support-decoder.md
---

# Can a zeta visual statistic leave the regular prime-torus representation class after the full Gram-clock quotient?

## Observation

The prime-phase program has progressively removed representation and sampling effects that can look arithmetically structured without adding a new usable mechanism. `VIS-064`--`VIS-066` show that invertible hybrid factor/residual recombinations do not create information, while `VIS-083`--`VIS-091` and `VIS-150`--`VIS-156` show that the deterministic Gram clock can generate Haar populations, coherent lag fields, critical Haar fibers, irregular-delay geometry, and sparse affine samples from the same fixed-prime state.

`VIS-157`--`VIS-159` classify increasingly rich fixed-complexity index selectors. A degree-`d` polynomial selector is Haar through `d` fixed samples and exposes a deterministic moment-null character at `d+1`; the full fixed power family `floor(n^alpha)` has the corresponding threshold `ceil(alpha)`. `VIS-160` then diagonally glues polynomial stages of increasing degree into one strictly increasing deterministic selector `K(n)` such that every fixed finite sample-order/fixed-prime character test is eventually Haar. Selector complexity growing with height is therefore not itself a new information source.

`VIS-161` adds a different representation boundary. For any two distinct primes `p,q`, the exact phase pair `(p^(-it),q^(-it))` is already injective in the real height `t`, even though its dense-orbit inverse is nowhere continuous. Consequently every same-height analytic coordinate is set-theoretically a function of two exact prime phases. Raw information or unrestricted measurability is therefore too permissive a discriminator: the unresolved content lies in stable, regular, complexity-controlled recoverability from the admitted phase/clock representation.

`VIS-162` closes the Lipschitz decoder search itself. For a fixed finite prime set `P` with chordal torus metric, the smallest exact Lipschitz-decoder constant of an observable is exactly the worst phase-collision quotient. Decoder architecture is therefore not the issue; the live quantity is recurrence geometry.

`VIS-163` adds the decisive fixed-support control. If `r` is a prime omitted from `P`, then the held-out phase `r^(-it)` has **no continuous decoder at all** from `Phi_P(t)`, its orbit decoder is nowhere continuous, and its global Lipschitz collision quotient is infinite, even though exact retained phases still identify height set-theoretically. Hence absolute failure of continuous/Lipschitz decoding from fixed support is not source-sensitive: ordinary omission of one prime frequency already produces it.

## Research question

After quotienting the prime-torus population law, the full fixed-complexity Gram-clock hierarchy, pathological exact-height encoding, the Lipschitz collision criterion, and the held-out-prime fixed-support obstruction, does any zeta-facing statistic exhibit **regular-decoder complexity beyond a matched omitted-prime baseline** or a separation that persists as retained prime support grows?

A remaining sampling route must contain quantitative structure that the diagonal construction cannot absorb: for example a pre-specified natural selector together with a test whose order, prime support, character complexity, or resolution grows with height at a controlled rate. For analytic-coordinate routes, the decoder class, support-growth law, observable normalization, and matched source control must be frozen before favorable residuals are inspected.

## Why it may matter

The control class is now stronger than any collection of fixed-dimensional scatter plots, finite-order Haar tests, or an absolute decoder-failure claim. `VIS-160` can absorb every fixed finite-order phase-mixing test, `VIS-161` shows exact phases can encode height pathologically, `VIS-162` reduces Lipschitz recovery to collisions, and `VIS-163` shows that **a completely ordinary held-out prime phase already escapes every continuous decoder from fixed retained support**.

Therefore a zeta-facing observable is interesting only if its regularity/complexity profile distinguishes it from a source that was merely left out of the representation. This converts the route from “can the finite prime torus decode `A`?” to the sharper question “does `A` require more stable complexity than a matched omitted-prime source, or does the separation survive a controlled growth of the retained source representation?”

## Decisive test

For a Lipschitz analytic-coordinate test, freeze before inspection:

- the retained finite prime set `P` or an explicit growth law `P=P(T)`;
- the chordal torus metric or another justified metric;
- the zeta-facing observable `A` and normalization;
- expanding height windows;
- one or more held-out-prime controls `A_r(t)=r^(-it)` selected by a predeclared frequency/scale rule;
- the comparison functional and decision rule.

For fixed `P`, study

`Lambda_P(A;T)=sup_(t!=u in [-T,T]) |A(t)-A(u)|/||Phi_P(t)-Phi_P(u)||_2`

and the corresponding `Lambda_P(A_r;T)` controls under identical windows and metric. `VIS-162` gives the exact decoder meaning of the first quantity; `VIS-163` proves that every held-out-prime control diverges globally, so **divergence alone is a failed discriminator**.

A positive result must instead prove a predeclared separation in growth, normalized collision geometry, approximation error at matched decoder budget, or another regularity/complexity quantity that the held-out-prime controls do not share. If support grows, prove the statement uniformly enough that ordinary frequency omission is not simply moved to the next unrepresented prime.

For non-Lipschitz decoder classes, formulate the corresponding frozen complexity budget and include the analogous omitted-source control. For sampling-based escapes, specify a selector independently of success and prove a quantitative theorem for a jointly growing test family, with enough uniformity to prevent the `VIS-160` diagonal clock from postponing each fixed test.

Kill the route if the apparent zeta separation is reproduced by held-out prime phases under the same representation budget, disappears when `P` grows according to the frozen rule, or depends on choosing the support/control only after inspecting the candidate residual.

## Evidence boundary

`VIS-150`--`VIS-160` are deterministic clock/sampling controls. `VIS-161` is a representation boundary showing exact injectivity with nowhere-continuous height recovery. `VIS-162` exactly characterizes finite-prime Lipschitz decoding by phase collisions.

`VIS-163` is a classical Kronecker--Weyl specialization and a **negative control**, not a zeta theorem. It proves that a held-out prime phase cannot be continuously or globally Lipschitz decoded from fixed retained prime support and that its finite-window Lipschitz constants diverge. It does not give a divergence rate, and it does not compare that rate with Hardy `Z`, derivatives, zero occupancy, or nearby-zero geometry.

Accordingly, the corpus still does not establish a source-sensitive regularity separation for any zeta-facing observable, a quantitative jointly growing sampling law beyond the diagonal clock, or a uniform decoder theorem under growing prime support. None of these results is a stronger zeta criterion or an RH consequence.

## Research disposition

Accepted in further narrowed form. Fixed finite commensurate lag geometry, fixed affine thinning, all fixed polynomial/power-law selectors, generic selector-complexity growth, raw-information absence, and **absolute continuous/Lipschitz decoder failure from a fixed finite prime support** are now closed as positive discriminators.

Continue only through a genuinely quantitative changing-complexity law under pre-specified controls, a separately derived nonclock sampling mechanism that survives the same audit, a zeta-facing decoder/collision profile that separates from matched held-out-prime controls, or a theorem whose separation persists under a predeclared growth of the retained prime support.