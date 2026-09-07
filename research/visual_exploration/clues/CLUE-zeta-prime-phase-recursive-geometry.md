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
  - research/visual_exploration/findings/VIS-086-quadratic-gram-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-087-finite-order-gram-clock-null-hierarchy.md
  - research/visual_exploration/findings/VIS-088-polynomial-sensitivity-observables-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-089-inverse-polynomial-decision-margins-inherit-gram-clock-null.md
---

# Can a zeta visual statistic leave the prime-torus information class?

## Observation

The prime-phase program has closed several increasingly sophisticated apparent escape routes.

`VIS-064`--`VIS-066` show that once the explicit hybrid residual is retained, quotient compensation, prime/zero contrast, and deterministic recombination do not create a new information channel: the complete factor/residual field is related by an invertible shear. `VIS-071` identifies the long-height law of every fixed finite prime field with its shared-phase Haar control, while `VIS-072` gives the exact finite-window sinc filtering of the same torus frequencies.

The nonlinear Euler-product branch is also sharply classified. `VIS-074` removes additive cross-prime small divisors, `VIS-075` shows that the raw holomorphic finite Euler product stays in the positive exponent cone, and `VIS-076` closes fixed-support signed beats for `|P_X|^2`. `VIS-078`--`VIS-079` replace misleading reciprocal-frequency certificates by the exact sinc-filtered energy and its one-variable triangular autocorrelation form. `VIS-080`--`VIS-082` then close the growing-support signed route: the normalized triangular energy tends to zero exactly when `log X/L -> 0`, while persistence outside that corridor is already forced by ordinary coprime-ratio support crowding.

Gram sampling supplies complementary global and local controls. `VIS-083` proves Haar equidistribution for every fixed finite prime-phase vector over the Gram population. `VIS-084` shows that consecutive sublogarithmic Gram blocks freeze and logarithmic blocks first trace a deterministic torus arc. `VIS-085` and `VIS-086` then showed that subtracting the linear and quadratic inverse-theta clock terms extends coordinatewise collapse through the square-root and two-thirds-power corridors for polynomial prime support.

`VIS-087` closes the apparent finite-order loophole. If the degree-`m` Taylor polynomial of the inverse Gram clock is subtracted, then

`max_(h<=H_n,p<=P_n) |R_(m,n,h)(p)-1|`
` <<_m H_n^(m+1) log P_n/[g_n^m(log g_n)^(m+2)]`.

For polynomial prime support this collapses whenever

`H_n=o(g_n^(m/(m+1)) log g_n)`.

Because `m/(m+1)->1`, every fixed sublinear power scale `H_n=O(g_n^alpha(log g_n)^B)` with `alpha<1` and fixed `B` is swallowed by some fixed finite-order deterministic sampling null.

`VIS-088` closes most of the generic growing-dimensional loophole left by coordinatewise convergence. If a block observable `F_n` is `Lambda_n`-Lipschitz in the chord sup metric of the complete corrected phase block, then its deviation from the clock-null value is at most `Lambda_n` times the `VIS-087` coordinatewise error. On every fixed sublinear power-law block with polynomial prime support, **any fixed-polynomial sensitivity budget `Lambda_n` is swallowed by a sufficiently high but still fixed clock order**. Increasing the number of primes, block coordinates, or an ordinary unnormalized aggregation by a polynomial amount therefore does not by itself create an escape channel.

`VIS-089` closes the robust discontinuous counterpart. For an arbitrary categorical or hard-threshold readout `Q_n`, define the metric decision margin `mu_n` as the distance from the null block to the nearest input that changes the output. If `mu_n` has any fixed inverse-polynomial lower bound in `g_n`, the same finite-order clock hierarchy eventually places the whole corrected block strictly inside that decision neighborhood. Hard binning, signs, nearest-template labels, or other discontinuous readouts therefore do not escape merely by discarding continuity when their decision is quantitatively robust.

## Research question

After these closures, does any **independently anchored** or **independently calibrated factor/residual** visual statistic expose information that is not already determined by the prime torus, its exact observation-window/sampling geometry, or an invertible coordinate change of the same underlying field?

Three possibilities remain materially distinct.

First, a Gram/prime-phase route may move into a genuinely different sampling regime: nearly linear or nonlocal Gram blocks, a statistic with quantitatively justified super-polynomial sensitivity, or a discontinuous decision whose boundary has no inverse-polynomially robust neighborhood and whose extreme sensitivity is independently meaningful. Merely increasing a fixed sublinear power exponent, the finite Taylor order, the block dimension, polynomial aggregation sensitivity, or adding an ordinary robust hard threshold is no longer an escape route.

Second, an externally anchored observable may add a source coordinate not determined by the prime phases and the Gram clock — for example a genuinely informative zero/Gram analytic quantity — and then test a joint law that survives the matched prime-phase sampling null.

Third, a hybrid factor/residual statistic may be meaningful if it tests a joint law or dependence property that is not a deterministic consequence of the invertible factor/residual shear and is calibrated at the actual claim strength.

## Why it may matter

The current sequence of controls shows how easily visual structure can be generated by representation and sampling alone. The same prime field is globally Haar on fixed support, locally frozen on very short Gram blocks, organized into a deterministic arc at the first motion scale, controlled by a hierarchy of deterministic inverse-theta clock corrections on every fixed sublinear power-law block with polynomial prime support, remains collapsed after any observable whose total Lipschitz sensitivity grows only polynomially, and also preserves every hard decision whose null region has an inverse-polynomial metric margin.

A surviving statistic therefore needs a genuinely new source law, sampling regime, or mathematically justified amplification mechanism rather than another rendering, ordinary high-dimensional summary, or stable thresholding of the same local clocked prime phases.

## Decisive test

For an externally anchored route, define the anchor without using the prime-torus statistic being tested. Freeze the anchor rule, window, scale, normalization, witness, and comparison before confirmation. Determine the induced law and sampling geometry of the admitted prime-phase field under that anchor before interpreting a visual effect.

For consecutive Gram windows with polynomial prime support, compare against `VIS-084`--`VIS-089`. If the block has a fixed sublinear power scale `H_n=O(g_n^alpha(log g_n)^B)` with `alpha<1`, first derive the sensitivity of the complete proposed observable in a metric strong enough for the claimed separation. If the readout is Lipschitz with fixed-polynomial sensitivity, `VIS-088` applies after a sufficiently high fixed clock order. If the readout is discontinuous, compute or bound its metric decision margin about the deterministic null. Any inverse-polynomial lower margin is likewise swallowed by `VIS-089` after a sufficiently high fixed clock order.

Do not treat increasing `m`, `alpha`, the number of sampled Gram points, the prime cutoff within polynomial support, an unnormalized polynomial-size aggregation, or hard thresholding as confirmation. A discontinuous route that relies on a margin smaller than every admitted inverse-polynomial scale must independently justify why that extreme sensitivity is stable and arithmetically meaningful rather than a magnifier of residual clock error. A nearly linear or nonlocal Gram route requires its own sampling theorem rather than extrapolation from failure of the fixed-sublinear estimate.

`VIS-083` still kills population-level fixed-prime claims when the induced law is merely Haar. Do not infer growing-dimensional Haar behavior from the local inverse-theta bounds.

For a factor/residual route, construct the hybrid prime factor, zero factor, and explicit residual independently. Reduce deterministic recombinations using `VIS-064`--`VIS-066`, then state the remaining claim as a property of the joint `(factor,residual)` law that would still be nontrivial after an invertible coordinate change. Calibrate that property with the finite-window and control uncertainty appropriate to its actual dimensionality. Kill the route if the claimed effect is forced by the shear, by marginal rescaling, by overlap/search selection, or by a null that preserves the same admitted joint information.

## Evidence boundary

The signed squared-Euler-product branch is resolved negatively as a separator by `VIS-080`--`VIS-082`. Gram-point anchoring is classified at several levels: `VIS-083` gives fixed-prime population Haar behavior, `VIS-084` gives raw short-block freezing and the first deterministic local arc, `VIS-085` and `VIS-086` give first- and second-order corrected collapse, `VIS-087` proves the fixed finite-order hierarchy covering every fixed sublinear power scale for polynomial prime support, `VIS-088` lifts that hierarchy to every full-block observable with a fixed-polynomial Lipschitz sensitivity budget, and `VIS-089` freezes arbitrary hard decisions whenever their null decision margin has an inverse-polynomial lower bound.

None of these findings controls nearly linear or genuinely nonlocal Gram sampling, proves that a super-polynomial or vanishing-margin amplifier is stable or arithmetically meaningful, establishes growing-dimensional Haar equidistribution, approximates zeta strongly enough for the intended inference, proves independence of prime and zero data, or has an RH consequence. Failure of a particular upper bound remains only an absence of that control unless a surviving law is established independently.

## Research disposition

Accepted in further narrowed form. Continue only through a genuinely different nearly linear/nonlocal sampling regime with its own control, a quantitatively justified super-polynomial or vanishing-margin amplification mechanism, an independently informative added coordinate/source law, or an independently calibrated factor/residual joint-law question. Do not reopen fixed sublinear power-law Gram blocks by raising the correction order, adding polynomially many coordinates, increasing polynomial aggregation sensitivity, applying a robust hard threshold/binning rule, or changing the rendering.