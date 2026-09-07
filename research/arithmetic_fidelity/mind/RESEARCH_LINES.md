# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the admissible provenance code only after the endpoint quotient is fixed

**Linked intuitions:** `MI-001-recovery-has-a-source-relative-and-a-target-relative-layer`, `MI-015-endpoint-fidelity-is-a-quotient-problem-before-a-coding-problem`, and `MI-016-provenance-must-be-transported-coherently-not-recomputed-after-compression`.

Continue to measure retained information only modulo distinctions that the downstream theorem cannot see. A symmetric compressed coefficient can already transport both radial and angular endpoint information, so an orientation mark must not be added merely because a chosen real slice forgot it. Family-wide recovery still requires one common reverse channel and coherent provenance transport.

## Declare quotient, metric, source regularity, scale, and observation bandwidth together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision` and `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-179 separate exact sufficiency from stable inversion on finite Blaschke data. After quotienting the output gauge, the interpolation/separation modulus is the intrinsic local conditioning scale on the simple stratum, while collision retains only Hölder regularity.

AF-180--AF-184 add an independent asymptotic axis. Exact Euler-product injectivity in `Re(s)>1` does not imply stable recovery from a finite vertical window when generator scale and source complexity vary. For a fixed order-`m` parity-split cluster, AF-183 identifies the sharp transition `T ~ delta^(-(m-1)/m)` inside the small-phase regime. AF-184 then shows that allowing the cancellation order to grow is much worse: if `delta sqrt(sigma^2+T^2) log(1/delta) -> 0` — equivalently, for growing bandwidth, `T=o(1/(delta log(1/delta)))` — one can choose a shrinking positive generalized-prime cluster with exact source separation `W_1=delta` whose Euler-log discrepancy is smaller than every fixed algebraic power of `delta`.

Thus no fixed finite moment/derivative order captures the family-wide stability problem below this logarithmic Rayleigh scale. A stable-fidelity theorem must state destination quotient and metric, source regularity/complexity, source scale, and observation bandwidth in one quantitative claim.

## Prove stable inversion in the exact metric consumed downstream

Exact injectivity is only the first gate. For growing families, derive a recovery modulus with explicit dependence on multiplicity, interpolation/separation, forward attenuation, output gauge, observation bandwidth, and the complexity of source clusters that can cancel low-order observations. When a compressed coordinate is visible, compare the downstream endpoint to that coordinate rather than to an arbitrary presentation metric.

The adaptive Euler controls require testing the whole joint law rather than extrapolating from any fixed cancellation order. A proposed inverse theorem should survive clusters whose matching order grows while their support still collapses to one source point.

## Match reference complexity, provenance transport, endpoint loss, inverse conditioning, and resolution

A useful fidelity claim should state separately the information surviving the endpoint quotient, the source-relative reference/provenance code, stability of transporting that code through compression, conditioning of the inverse on the actual source stratum, and the bandwidth/resolution needed to see the distinguishing source modes. None is implied by the others.
