# MI-010 — Weighted prime-phase nulls have separate concentration, support, kernel, and crowding-scale regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems through VIS-185.

For positive prime weights, the effective dimensions controlling concentration and normalized shape are distinct. VIS-173--VIS-178 make that separation explicit, while VIS-179 shows that continuous quadratic variance is matched for every strictly sublinear support law. VIS-180 warns that arbitrary sparse subsets can still retain an order-one slow beat at linear support.

The full-prime prefix behaves differently. VIS-181--VIS-184 show progressively that diffuse normalization kills fixed and slowly growing close-gap families. VIS-184 gave the first explicit coefficient-mass rate: every `D=o(log y)` band is negligible for fixed power weights `p^-alpha`, `alpha<1/2`.

VIS-185 strengthens the boundary by using the actual interval-average kernel. For a pair gap `d` on a high dyadic block, the kernel supplies an additional factor comparable to `1/d` at linear observation scale. Combined with the averaged singular-series bound, the total normalized contribution of gaps up to `D` is controlled by

`D y^(-(1-2alpha)/2) + log(2D)/log y`.

Consequently **every subpolynomial gap band `D=y^(o(1))` is null** at `H comparable to y`, uniformly in interval start. The earlier logarithmic frontier was an artifact of discarding kernel decay, not a surviving arithmetic scale.

The first scale not removed by this mechanism is polynomial breadth. For `D=y^delta`, the current bound no longer vanishes, but this is only a proof gap. Stronger cancellation or the full all-gap structure may still kill it. The natural next object is therefore the complete kernel-weighted off-diagonal aggregate rather than another subpolynomial local-gap cutoff.

The reusable separation is: weight concentration, support scale, functional order, observation horizon, local spacing, band breadth, and the exact readout kernel are different currencies. A dense family of close frequencies matters only after its mass survives the destination kernel and normalization.

**Boundary.** VIS-185 concerns continuous second moments for full-prime power weights with fixed `alpha<1/2`. It does not establish survival at polynomial gap breadth and does not transfer to discrete Gram sampling or higher moments.