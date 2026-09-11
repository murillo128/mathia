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
  - research/visual_exploration/findings/VIS-164-anchored-heldout-prime-collision-haar-tail.md
---

# Can a zeta visual statistic leave the regular prime-torus representation class after the full Gram-clock quotient?

## Observation

The prime-phase program has progressively removed representation and sampling effects that can look arithmetically structured without adding a new usable mechanism. `VIS-064`--`VIS-066` show that invertible hybrid factor/residual recombinations do not create information, while `VIS-083`--`VIS-091` and `VIS-150`--`VIS-156` show that the deterministic Gram clock can generate Haar populations, coherent lag fields, critical Haar fibers, irregular-delay geometry, and sparse affine samples from the same fixed-prime state.

`VIS-157`--`VIS-159` classify increasingly rich fixed-complexity index selectors. A degree-`d` polynomial selector is Haar through `d` fixed samples and exposes a deterministic moment-null character at `d+1`; the full fixed power family `floor(n^alpha)` has the corresponding threshold `ceil(alpha)`. `VIS-160` then diagonally glues polynomial stages of increasing degree into one strictly increasing deterministic selector `K(n)` such that every fixed finite sample-order/fixed-prime character test is eventually Haar. Selector complexity growing with height is therefore not itself a new information source.

`VIS-161` adds a different representation boundary. For any two distinct primes `p,q`, the exact phase pair `(p^(-it),q^(-it))` is already injective in the real height `t`, even though its dense-orbit inverse is nowhere continuous. Consequently every same-height analytic coordinate is set-theoretically a function of two exact prime phases. Raw information or unrestricted measurability is therefore too permissive a discriminator: the unresolved content lies in stable, regular, complexity-controlled recoverability from the admitted phase/clock representation.

`VIS-162` closes the Lipschitz decoder search itself. For a fixed finite prime set `P` with chordal torus metric, the smallest exact Lipschitz-decoder constant of an observable is exactly the worst phase-collision quotient. Decoder architecture is therefore not the issue; the live quantity is recurrence geometry.

`VIS-163` adds the decisive fixed-support control. If `r` is a prime omitted from `P`, then the held-out phase `r^(-it)` has **no continuous decoder at all** from `Phi_P(t)`, its orbit decoder is nowhere continuous, and its global Lipschitz collision quotient is infinite, even though exact retained phases still identify height set-theoretically. Hence absolute failure of continuous/Lipschitz decoding from fixed support is not source-sensitive: ordinary omission of one prime frequency already produces it.

`VIS-164` makes that omitted-source control quantitative on a canonical recurrence slice. Anchor one retained prime `p_0` and inspect the exact-return lags `Delta_q=2 pi q/log p_0`. If `d=|P|-1`, the held-out-prime collision score on those lags is a pushforward of a `(d+1)`-dimensional Kronecker sequence. Its fixed-threshold exceedance frequency converges to a Haar law whose large-threshold tail is exactly `c_d L^(-d)`. The exponent therefore changes automatically with retained support dimension; adding more represented primes suppresses large matched-control collisions even before any zeta-specific information enters.

## Research question

After quotienting the prime-torus population law, the full fixed-complexity Gram-clock hierarchy, pathological exact-height encoding, the Lipschitz collision criterion, and the dimension-coded held-out-prime collision baseline, does any zeta-facing statistic exhibit **regular-decoder complexity beyond a matched omitted-prime control** or a separation that persists as retained prime support grows?

A remaining sampling route must contain quantitative structure that the diagonal construction cannot absorb: for example a pre-specified natural selector together with a test whose order, prime support, character complexity, or resolution grows with height at a controlled rate. For analytic-coordinate routes, the decoder class, support-growth law, observable normalization, recurrence slice, and matched source control must be frozen before favorable residuals are inspected.

## Why it may matter

The control class is now stronger than any collection of fixed-dimensional scatter plots, finite-order Haar tests, or an absolute decoder-failure claim. `VIS-160` can absorb every fixed finite-order phase-mixing test, `VIS-161` shows exact phases can encode height pathologically, `VIS-162` reduces Lipschitz recovery to collisions, and `VIS-163` shows that **a completely ordinary held-out prime phase already escapes every continuous decoder from fixed retained support**.

`VIS-164` further shows that this null has nontrivial quantitative geometry: on exact returns of one retained phase, its collision exceedance tail is not arbitrary but follows a support-dimension power law. Consequently neither divergence nor a raw decrease in collision frequency under larger support is source evidence. A zeta-facing observable is interesting only if its normalized regularity/complexity profile separates from the omitted-source law under the same representation budget.

This converts the route from “can the finite prime torus decode `A`?” to the sharper question “does `A` require more stable complexity than a matched omitted-prime source after the recurrence geometry and support dimension have been normalized away?”

## Decisive test

For a Lipschitz analytic-coordinate test, freeze before inspection:

- the retained finite prime set `P` or an explicit growth law `P=P(T)`;
- an anchor `p_0 in P` when using the exact-return slice;
- the chordal torus metric or another justified metric;
- the zeta-facing observable `A` and normalization;
- the base-height/window rule and expanding height windows;
- one or more held-out-prime controls `A_r(t)=r^(-it)` selected by a predeclared frequency/scale rule;
- the collision statistic, thresholds, comparison functional, and decision rule.

For fixed `P`, the full-window quantity remains

`Lambda_P(A;T)=sup_(t!=u in [-T,T]) |A(t)-A(u)|/||Phi_P(t)-Phi_P(u)||_2`,

with corresponding held-out-prime controls. `VIS-163` proves that every held-out-prime control diverges globally, so **divergence alone is a failed discriminator**.

The first sharper matched test is the anchored recurrence family from `VIS-164`. On lags `Delta_q=2 pi q/log p_0`, compare the candidate collision-score distribution with the omitted-prime baseline under the same support and normalization. For the control, every fixed threshold has an exact limiting Haar exceedance probability `mu_d(L)`, with `mu_d(L)~c_d L^(-d)` and `d=|P|-1` at high threshold. A candidate separation must therefore concern a predeclared distributional functional, normalized tail, approximation error at matched decoder budget, or another quantity not already explained by this dimension law.

Do not infer an extreme-value rate such as `max_(q<=Q) C_q ~ Q^(1/d)` from `VIS-164`; its theorem is fixed-threshold equidistribution and a separate Haar-tail asymptotic. If the positive test needs thresholds growing with the observation window, establish the corresponding quantitative Kronecker/discrepancy control first.

If support grows, prove the statement uniformly enough that ordinary frequency omission and the changing null dimension are not simply moved to the next unrepresented prime. For non-Lipschitz decoder classes, formulate the corresponding frozen complexity budget and include the analogous omitted-source control. For sampling-based escapes, specify a selector independently of success and prove a quantitative theorem for a jointly growing test family, with enough uniformity to prevent the `VIS-160` diagonal clock from postponing each fixed test.

Kill the route if the apparent zeta separation is reproduced by held-out prime phases under the same representation budget, collapses to the `VIS-164` support-dimension tail after normalization, disappears when `P` grows according to the frozen rule, or depends on choosing the support/control only after inspecting the candidate residual.

## Evidence boundary

`VIS-150`--`VIS-160` are deterministic clock/sampling controls. `VIS-161` is a representation boundary showing exact injectivity with nowhere-continuous height recovery. `VIS-162` exactly characterizes finite-prime Lipschitz decoding by phase collisions.

`VIS-163` is a classical Kronecker--Weyl specialization and a **negative control**, not a zeta theorem. It proves that a held-out prime phase cannot be continuously or globally Lipschitz decoded from fixed retained prime support and that its finite-window Lipschitz constants diverge.

`VIS-164` adds a fixed-support distributional control: on exact returns of one retained phase, held-out-prime collision scores have a fixed-threshold Haar law and a large-threshold tail `c_d L^(-d)`. It does **not** give a finite-window convergence rate, an extreme-value theorem, a joint `Q,L(Q)` limit, or a theorem uniform in growing support.

Accordingly, the corpus still does not establish a source-sensitive regularity separation for any zeta-facing observable, a quantitative jointly growing sampling law beyond the diagonal clock, or a uniform decoder theorem under growing prime support. None of these results is a stronger zeta criterion or an RH consequence.

## Research disposition

Accepted in further narrowed form. Fixed finite commensurate lag geometry, fixed affine thinning, all fixed polynomial/power-law selectors, generic selector-complexity growth, raw-information absence, **absolute continuous/Lipschitz decoder failure from fixed support**, and unnormalized large-collision frequency under changing support are now closed as positive discriminators.

Continue only through a predeclared zeta-versus-held-out-prime separation after the `VIS-164` recurrence/dimension baseline is accounted for, a genuinely quantitative changing-complexity law under pre-specified controls, a separately derived nonclock sampling mechanism that survives the same audit, or a theorem whose separation persists uniformly under a predeclared growth of the retained prime support.