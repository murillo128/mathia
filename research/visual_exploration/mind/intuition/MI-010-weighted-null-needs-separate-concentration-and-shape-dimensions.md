# MI-010 — Weighted prime-phase nulls have separate concentration, support, kernel, and cross-scale accumulation regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems through VIS-186.

For positive prime weights, the effective dimensions controlling concentration and normalized shape are distinct. VIS-173--VIS-178 make that separation explicit, while VIS-179 shows that continuous quadratic variance is matched for every strictly sublinear support law. VIS-180 warns that arbitrary sparse subsets can still retain an order-one slow beat at linear support.

The diffuse full-prime prefix behaves differently. VIS-181--VIS-184 progressively kill fixed and slowly growing close-gap families. VIS-185 uses the actual interval-average kernel: on high dyadic prime blocks the kernel contributes a `1/d` factor, reducing the cumulative singular-series cost to `log D`. Consequently every subpolynomial band `D=y^(o(1))` is null at `H comparable to y`, uniformly in interval start.

VIS-186 sharpens the polynomial boundary. For every fixed `epsilon>0`, `alpha<1/2`, and one dyadic gap octave `y^epsilon<=D<=y^(1-epsilon)`, the normalized shell obeys

`R_shell(D;y,H,T) << (D/y)^(2-2alpha) (log y/log D) + 1/log y`

for `H>=c y`. Hence **every fixed polynomial mesoscopic shell `d asymp y^delta`, `0<delta<1`, vanishes individually**. Polynomial breadth is not a surviving local scale.

The unresolved possibility is now genuinely multiscale. A cumulative band up to `y^delta` contains `Theta(log y)` logarithmic gap octaves, each allowed only `O(1/log y)` by the present absolute shell estimate; those small contributions can still accumulate to an order-one upper bound. A surviving quadratic full-prefix mechanism must therefore use coherent accumulation across a growing number of scales, exploit cancellation/structure invisible to shellwise absolute values, or move to genuinely macroscopic separations `d asymp y`.

The reusable separation is: weight concentration, support scale, functional order, observation horizon, local spacing, one-shell mass, cross-scale accumulation, and the exact readout kernel are different currencies. A dense family of close frequencies matters only after its mass survives both the destination kernel and the normalization, and no single mesoscopic polynomial octave now passes that test.

**Boundary.** VIS-186 is shellwise and uses absolute values. It does not show the cumulative polynomial range is negligible, does not treat macroscopic `d comparable to y`, and does not transfer to discrete Gram sampling or higher moments.