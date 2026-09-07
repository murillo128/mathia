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
  - research/visual_exploration/findings/VIS-072-fixed-prime-window-discrepancy-sinc-spectrum.md
  - research/visual_exploration/findings/VIS-074-additive-log-euler-window-corridor.md
  - research/visual_exploration/findings/VIS-075-holomorphic-euler-product-positive-cone-window-law.md
  - research/visual_exploration/findings/VIS-076-squared-euler-product-signed-mode-fixed-support-bound.md
  - research/visual_exploration/findings/VIS-078-signed-euler-product-l2-energy-certificate-gap.md
  - research/visual_exploration/findings/VIS-079-signed-euler-product-triangular-autocorrelation.md
  - research/visual_exploration/findings/VIS-080-signed-euler-product-coprime-ratio-support-crowding-floor.md
  - research/visual_exploration/findings/VIS-081-signed-euler-product-dickman-scaling-law.md
  - research/visual_exploration/findings/VIS-082-signed-euler-product-sharp-log-cutoff-threshold.md
  - research/visual_exploration/findings/VIS-083-gram-point-prime-phase-haar-equidistribution.md
  - research/visual_exploration/findings/VIS-084-gram-short-block-prime-phase-freezing.md
  - research/visual_exploration/findings/VIS-085-gram-local-arc-growing-support-collapse.md
---

# Can a zeta visual statistic leave the finite prime-torus information class?

## Observation

The prime-phase program has now closed several increasingly sophisticated apparent escape routes.

`VIS-064`--`VIS-066` show that once the explicit hybrid residual is retained, quotient compensation, prime/zero contrast, and deterministic recombination do not create a new information channel: the complete factor/residual field is related by an invertible shear. `VIS-071` identifies the long-height law of every fixed finite prime field with its shared-phase Haar control, while `VIS-072` gives the exact finite-window sinc filtering of the same torus frequencies.

The nonlinear Euler-product branch is also sharply classified. `VIS-074` removes additive cross-prime small divisors, `VIS-075` shows that the raw holomorphic finite Euler product stays in the positive exponent cone, and `VIS-076` closes fixed-support signed beats for `|P_X|^2`. `VIS-078`--`VIS-079` then replace misleading reciprocal-frequency certificates by the exact sinc-filtered energy and its one-variable triangular autocorrelation form.

The growing-support signed route is no longer open. `VIS-080` proves that nonvanishing energy outside `log X=o(L)` is already forced by generic coprime-ratio support crowding. `VIS-081` identifies the associated smooth-number support scaling with classical Dickman geometry. `VIS-082` proves the matching upper bound

`T_(X,L) << log(2X)/L`

and therefore the exact criterion

`T_(X(L),L)->0  <=>  log X(L)/L->0`.

`VIS-083` closes one natural externally anchored population route: for every fixed finite set of primes, Gram-point prime phases are Haar-equidistributed. `VIS-084` supplies the complementary local control: sublogarithmic consecutive Gram blocks freeze, while logarithmic-size blocks first trace a deterministic torus arc induced by Gram spacing.

`VIS-085` now closes the obvious growing-support loophole at that local scale. After subtracting the exact first-order Gram arc `pi h/theta'(g_n)`, the coordinatewise residual over `H=O(log g_n)` obeys

`max_(h<=H,p<=P) |R_(n,h)(p)-1| << H^2 log P/[g_n (log g_n)^3]`.

Thus the residual still collapses for every growing support with `log P=o(g_n log g_n)`, including all polynomial supports. Increasing prime dimension inside a logarithmic Gram block does not by itself create an independent local anchor channel.

## Research question

After these closures, does any **independently anchored** or **independently calibrated factor/residual** visual statistic expose information that is not already determined by the prime torus, its exact observation-window/sampling geometry, or an invertible coordinate change of the same underlying field?

Two residual routes remain admissible, but the external-anchor route is now substantially narrower.

First, a surviving external anchor must change the relevant law rather than merely resample the same prime field. For Gram points, neither global fixed-prime population sampling, sublogarithmic clustering, the deterministic logarithmic local arc, nor its broad growing-support curvature residual qualifies. A surviving Gram route therefore needs genuinely longer blocks, an observable/source law not explained by the matched torus arc, or an additional independently informative Gram/zero coordinate.

Second, a hybrid factor/residual statistic may be meaningful if it tests a joint law or dependence property that is not a deterministic consequence of the invertible factor/residual shear and is calibrated at the actual claim strength.

## Why it may matter

The Gram controls now illustrate how strongly visual geometry can depend on sampling scale without adding information. Globally the fixed-prime cloud becomes Haar; on sublogarithmic blocks it freezes; on logarithmic blocks it traces a deterministic arc; and after that arc is removed even a very broad growing prime support has vanishing coordinatewise sampling residual.

A surviving statistic would therefore have a much stronger interpretation: it would need an independently supplied reference coordinate that changes the relevant law, a genuinely larger-scale phenomenon beyond the local inverse-theta geometry, or a new joint-law statement rather than another rendering, nonlinear transformation, resampling schedule, dimension increase, or deterministic local correction of the same prime-torus data.

## Decisive test

For an externally anchored route, define the anchor without using the prime-torus statistic being tested. Freeze the anchor rule, window, scale, normalization, witness, and comparison before confirmation. Determine the **induced law and local sampling geometry of the admitted prime-phase field under that anchor** before interpreting a visual effect.

For consecutive Gram windows, first compare against `VIS-084` and `VIS-085`. If `H=o(log g_n)`, kill any claim whose signal is only clustering or lack of phase exploration. At `H=O(log g_n)`, match the deterministic first-order torus arc. If the prime support is bounded by `P_n` with `H_n^2 log P_n=o(g_n(log g_n)^3)`, also kill any claim whose residual is only the remaining Gram-clock curvature, because `VIS-085` forces that coordinatewise residual to zero. A positive Gram route must therefore operate outside those scale/support corridors or add information not determined by the prime phases and their sampling clock.

`VIS-083` still kills a population-level claim when the fixed-dimensional induced law is merely Haar. Do not infer a growing-dimensional Haar theorem from `VIS-085`: its conclusion is local arc-removal collapse, not global equidistribution.

For a factor/residual route, construct the hybrid prime factor, zero factor, and explicit residual independently. Reduce deterministic recombinations using `VIS-064`--`VIS-066`, then state the remaining claim as a property of the joint `(factor,residual)` law that would still be nontrivial after an invertible coordinate change. Calibrate that property with the finite-window and control uncertainty appropriate to its actual dimensionality. Kill the route if the claimed effect is forced by the shear, by marginal rescaling, by overlap/search selection, or by a null that preserves the same admitted joint information.

Do not reopen the signed `|P_X|^2` growing-support route merely by changing the cutoff law, plotting near-resonance density, or using a reciprocal-frequency certificate. `VIS-082` settles its vanishing threshold, and `VIS-080` explains persistence outside it by generic support crowding. Likewise, do not reopen Gram sampling merely by increasing prime dimension inside logarithmic blocks when the support remains inside the `VIS-085` corridor.

## Evidence boundary

The signed squared-Euler-product branch is **resolved negatively as a separator** by `VIS-080`--`VIS-082`: its normalized triangular energy vanishes exactly when `log X=o(L)`, and outside that corridor nonvanishing is already forced by ordinary reduced-ratio crowding.

`VIS-083` resolves Gram-point anchoring only for continuous observables of a fixed finite prime-phase vector in the asymptotic population sense. `VIS-084` resolves the local raw geometry for fixed prime support, and `VIS-085` resolves the arc-removed Gram-clock residual for growing supports satisfying its explicit scale condition.

None of these findings proves global Haar behavior uniformly in growing prime dimension, classifies much longer Gram blocks, removes information carried by zeta/zero/Gram analytic coordinates, yields a new prime/zero independence theorem, or has an RH consequence.

## Research disposition

Accepted in further narrowed form. The signed growing-support Euler-product route is closed; Gram points are closed as a positive fixed-prime population anchor; sublogarithmic Gram blocks are closed as a positive visual separator; and logarithmic Gram blocks remain locally explained by their deterministic torus arc even under broad growing prime support after arc subtraction. Continue only through a genuinely longer-scale external-anchor statistic, an independently informative added coordinate/source law, or an independently calibrated factor/residual joint-law question that passes the decisive tests above.