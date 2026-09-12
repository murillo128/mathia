# MI-010 — Weighted prime-gap nulls have separate shell, cross-scale, and window-endpoint coherence regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer/control theorems through VIS-187; no prime-pair asymptotic or arithmetic cross-scale term is claimed.

For positive prime weights, the effective dimensions controlling concentration and normalized shape are distinct. VIS-173--VIS-178 make that separation explicit, while VIS-179 shows that continuous quadratic variance is matched for every strictly sublinear support law. VIS-180 warns that arbitrary sparse subsets can still retain an order-one slow beat at linear support.

The diffuse full-prime prefix behaves differently. VIS-181--VIS-184 progressively kill fixed and slowly growing close-gap families. VIS-185 uses the actual interval-average kernel, and VIS-186 sharpens the polynomial boundary: every fixed mesoscopic polynomial gap shell `d asymp y^delta`, `0<delta<1`, vanishes individually at linear observation scale. No single polynomial octave carries an order-one normalized contribution.

VIS-187 shows why the remaining cross-scale question needs a stronger null. For the flat deterministic even-gap profile, with `H=cp`, `T=tau p`, and `M=o(p^(1/2))`, the cumulative kernel sum is

`[S_M(2(tau+c))-S_M(2tau)]/(2ci) + O(M^2/p)`,

where `S_M(theta)=sum_(m<=M) exp(i theta m)/m`. A logarithmic term appears precisely when exactly one scaled window endpoint is resonant modulo `pi`. In particular, an anchored window can produce order-`log M` accumulation from a completely source-free even-gap profile.

Thus the shellwise picture and the cumulative picture are separated by a new deterministic currency: **window-endpoint coherence**. Small contributions from many octaves can add coherently because of the readout kernel itself, without any prime-dependent cross-scale correlation. An order-one cumulative signal is not arithmetic evidence until a matched control preserves the same scaled endpoints and coarse gap density, or the endpoint-resonant component is removed explicitly.

The surviving positive question is correspondingly narrower. After endpoint resonance is controlled, does the actual prime-weighted off-diagonal kernel retain a residual cross-scale term that a flat/equidensity gap null cannot reproduce? Alternatively, does the nonresonant or endpoint-centered residual cancel across octaves, leaving only genuinely macroscopic separations `d asymp y`?

The reusable separation is: weight concentration, support scale, functional order, observation horizon, local spacing, one-shell mass, cross-scale accumulation, and endpoint resonance are different currencies. A dense family of close frequencies matters only after its mass survives both the destination kernel and the normalization, and coherent accumulation itself must be tested against the exact deterministic window geometry.

**Boundary.** VIS-187 uses equal deterministic weight per even gap, fixed scaled endpoints, and `M=o(p^(1/2))`. It does not describe actual prime-pair multiplicities or singular-series weights, does not treat larger cumulative gap ranges or macroscopic `d comparable to y`, and does not show that subtracting the endpoint null removes every non-arithmetic contribution.