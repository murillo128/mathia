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
  - research/visual_exploration/findings/VIS-090-consecutive-gram-superlog-prime-torus-haar.md
---

# Can a zeta visual statistic leave the prime-torus information class?

## Observation

The prime-phase program has closed several increasingly sophisticated apparent escape routes.

`VIS-064`--`VIS-066` show that once the explicit hybrid residual is retained, quotient compensation, prime/zero contrast, and deterministic recombination do not create a new information channel: the complete factor/residual field is related by an invertible shear. `VIS-071` identifies the long-height law of every fixed finite prime field with its shared-phase Haar control, while `VIS-072` gives the exact finite-window sinc filtering of the same torus frequencies.

The nonlinear Euler-product branch is also sharply classified. `VIS-074` removes additive cross-prime small divisors, `VIS-075` shows that the raw holomorphic finite Euler product stays in the positive exponent cone, and `VIS-076` closes fixed-support signed beats for `|P_X|^2`. `VIS-078`--`VIS-079` replace misleading reciprocal-frequency certificates by the exact sinc-filtered energy and its one-variable triangular autocorrelation form. `VIS-080`--`VIS-082` then close the growing-support signed route: the normalized triangular energy tends to zero exactly when `log X/L -> 0`, while persistence outside that corridor is already forced by ordinary coprime-ratio support crowding.

Gram sampling supplies complementary global and local controls. `VIS-083` proves Haar equidistribution for every fixed finite prime-phase vector over the full Gram population. `VIS-084` shows that consecutive sublogarithmic Gram blocks freeze and logarithmic blocks first trace a deterministic torus arc. `VIS-085` and `VIS-086` then show that subtracting the linear and quadratic inverse-theta clock terms extends coordinatewise collapse through the square-root and two-thirds-power corridors for polynomial prime support.

`VIS-087` closes the apparent finite-order loophole. If the degree-`m` Taylor polynomial of the inverse Gram clock is subtracted, then

`max_(h<=H_n,p<=P_n) |R_(m,n,h)(p)-1|`
` <<_m H_n^(m+1) log P_n/[g_n^m(log g_n)^(m+2)]`.

For polynomial prime support this collapses whenever

`H_n=o(g_n^(m/(m+1)) log g_n)`.

Because `m/(m+1)->1`, every fixed sublinear power scale `H_n=O(g_n^alpha(log g_n)^B)` with `alpha<1` and fixed `B` is swallowed by some fixed finite-order deterministic sampling null.

`VIS-088` lifts that coordinatewise hierarchy to every full-block observable with fixed-polynomial Lipschitz sensitivity. `VIS-089` closes the robust discontinuous counterpart: an arbitrary categorical or threshold readout is frozen whenever its decision margin around the deterministic clock-null block has an inverse-polynomial lower bound.

`VIS-090` now closes the complementary long consecutive-block population loophole. For the empirical prime-phase measure on indices `N<=k<=N+M`, every fixed nontrivial prime-torus Fourier coefficient is `O_m(log N/M)`. Hence, whenever `M/log N->infinity` and `M<=N-1`, the entire infinite prime-torus empirical measure converges weakly to Haar. Together with `VIS-084`, raw fixed-prime consecutive blocks are therefore classified across the Gram-spacing scale: sublogarithmic blocks freeze, logarithmic blocks trace the deterministic local clock arc, and superlogarithmic blocks return to Haar at the population level.

## Research question

After these closures, does any **independently anchored**, **ordered/path-sensitive**, or **independently calibrated factor/residual** visual statistic expose information that is not already determined by the prime torus, its exact observation-window/sampling geometry, or an invertible coordinate change of the same underlying field?

Three possibilities remain materially distinct.

First, a Gram/prime-phase route must now use information that the raw consecutive-block empirical measure discards: a genuinely ordered or nonconsecutive sampling statistic, prime support or Fourier complexity growing with height under a uniform analysis, a quantitatively justified super-polynomial/vanishing-margin amplifier, or another sampling regime with its own theorem. Merely lengthening a consecutive fixed-prime block — even toward a nearly linear block — does not create a new population law, because `VIS-090` sends every superlogarithmic block back to Haar.

Second, an externally anchored observable may add a source coordinate not determined by the prime phases and the Gram clock — for example a genuinely informative zero/Gram analytic quantity — and then test a joint law that survives the matched prime-phase sampling null.

Third, a hybrid factor/residual statistic may be meaningful if it tests a joint law or dependence property that is not a deterministic consequence of the invertible factor/residual shear and is calibrated at the actual claim strength.

## Why it may matter

The current sequence of controls shows how easily visual structure can be generated by representation and sampling alone. The same prime field is globally Haar on fixed support, locally frozen on very short Gram blocks, organized into a deterministic arc at the first motion scale, controlled by a hierarchy of deterministic inverse-theta clock corrections on fixed sublinear power-law blocks, stable under polynomial-sensitivity and robust-threshold readouts after sufficient correction, and again Haar as a raw population on every superlogarithmic consecutive block.

A surviving statistic therefore needs a genuinely new source law, retained ordering information, growing-dimensional structure with uniform control, or a mathematically justified amplification mechanism rather than another rendering or ordinary population summary of the same Gram-sampled prime phases.

## Decisive test

For an externally anchored route, define the anchor without using the prime-torus statistic being tested. Freeze the anchor rule, window, scale, normalization, witness, and comparison before confirmation. Determine the induced law and sampling geometry of the admitted prime-phase field under that anchor before interpreting a visual effect.

For consecutive Gram windows, first classify which regime the proposed statistic actually uses. Fixed-prime raw population statistics are already controlled: `VIS-084` gives freezing for `H=o(log g_n)` and the deterministic arc at `H=Theta(log g_n)`, while `VIS-090` gives Haar population convergence when `H/log n->infinity` with `H<=n-1`.

For growing-support fixed-sublinear power-law blocks, compare against `VIS-085`--`VIS-089`. If the complete readout is Lipschitz with fixed-polynomial sensitivity, a sufficiently high fixed clock order forces it to the null. If it is discontinuous, compute its metric decision margin; any inverse-polynomial lower margin is likewise swallowed. Do not treat increasing the correction order, block dimension, prime cutoff within polynomial support, polynomial aggregation sensitivity, or applying a robust hard threshold as confirmation.

A proposed escape must therefore identify the missing information explicitly. For an ordered/path-sensitive route, state the order statistic and derive a null that preserves the already-classified empirical population law and Gram clock. For a growing-dimensional route, prove uniformity in the changing support/character class rather than invoking fixed-character Haar convergence. For a nonconsecutive route, derive the induced sampling law. For a vanishing-margin or super-polynomial amplifier, justify why the extreme sensitivity is stable and arithmetically meaningful rather than a magnifier of residual clock error.

For a factor/residual route, construct the hybrid prime factor, zero factor, and explicit residual independently. Reduce deterministic recombinations using `VIS-064`--`VIS-066`, then state the remaining claim as a property of the joint `(factor,residual)` law that would still be nontrivial after an invertible coordinate change. Calibrate that property with the finite-window and control uncertainty appropriate to its actual dimensionality.

## Evidence boundary

The signed squared-Euler-product branch is resolved negatively as a separator by `VIS-080`--`VIS-082`. Gram-point anchoring is classified at several levels: `VIS-083` gives full-population fixed-prime Haar behavior; `VIS-084` gives raw short-block freezing and the first deterministic local arc; `VIS-085`--`VIS-087` give the finite-order corrected hierarchy through every fixed sublinear power scale for polynomial support; `VIS-088` and `VIS-089` lift that hierarchy to polynomial-sensitivity observables and inverse-polynomial-margin hard decisions; and `VIS-090` proves superlogarithmic consecutive-block Haar convergence at the empirical-population level.

None of these findings establishes growing-dimensional Haar equidistribution uniform in a changing prime support, classifies arbitrary ordered/path-sensitive or nonconsecutive Gram statistics, proves that a super-polynomial or vanishing-margin amplifier is stable or arithmetically meaningful, approximates zeta strongly enough for the intended inference, proves independence of prime and zero data, or has an RH consequence. Fixed-character weak Haar convergence must not be silently upgraded to an `N`-dependent high-dimensional law.

## Research disposition

Accepted in further narrowed form. Continue only through information that survives the complete consecutive-block population/clock controls: genuinely ordered or nonconsecutive sampling with its own null, growing support with a uniform theorem, a quantitatively justified super-polynomial or vanishing-margin mechanism, an independently informative added coordinate/source law, or an independently calibrated factor/residual joint-law question. Do not reopen raw fixed-prime consecutive Gram blocks by changing their length or rendering.