# MI-015 — Prime-phase worst starts survive both magnetic and simple-cycle relaxations; the exact torus problem remains

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, normalized magnetic-ground-state certificate from VIS-216, exact relaxation lower bound from VIS-217, prime-graph asymptotics in VIS-218, destination pricing in VIS-219, and the universal simple-cycle packing ceiling in [VIS-220](../../findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling.md). No lower bound for the exact torus optimum, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, the worst start is exactly the unit-modulus quadratic optimum `max_|z_p|=1 |z^*A_(y,H)z|`. Kronecker density settles existence of torus phases, not the size of this optimum or the time needed to approach it.

VIS-214 identifies cycle holonomy as the gauge-invariant obstruction to exact coefficient-envelope attainment. VIS-215 turns that obstruction into weighted fractional cycle-packing certificates `P_+` and `P_-`. VIS-216 adds a global normalized magnetic-Laplacian relaxation.

VIS-217--VIS-218 close the normalized spectral relaxation in the whole strictly subcritical prime regime. The actual coefficient graph satisfies `N_eff~y^2/[H(log y)^2]` while the active vertex count is at most `pi(y)`, so `N_eff/n->infinity`; the normalized magnetic certificate therefore misses Haar-RMS scale by a diverging factor regardless of edge phases.

VIS-219 identifies what the stronger packing route would have to achieve. With `P=min(P_+,P_-)`, `B=2 sum_e w_e`, and `R=2 sum_e w_e^2`,

`(B-P)/sqrt(R)=sqrt(2 N_eff)(1-P/B)`.

So a useful RMS certificate would require `1-P/B=O(N_eff^-1/2)`: almost the entire weighted absolute envelope would have to be consumed by both signed packings.

VIS-220 proves this is impossible for the exact `VIS-215` simple-cycle LP. For every support graph of girth `g`, weighted Cauchy--Schwarz on each cycle and the unit edge-capacity constraint give

`P_+,P_- <= (2/g^2)B`.

For an ordinary simple graph `g>=3`, this yields `P_+,P_-<=2B/9`, hence

`B-min(P_+,P_-) >= 7B/9`

and

`D_pack=(B-P)/sqrt(R) >= (7/9)sqrt(2N_eff)`.

Thus the simple-cycle packing certificate stays on the absolute-envelope scale and diverges from Haar-RMS scale whenever `N_eff->infinity`. This is a **certificate-family ceiling**, not a statement that the prime phases lack frustration. No amount of cycle enumeration or better optimization inside the same reward/capacity LP can remove it.

The exact fixed-modulus torus problem therefore remains strictly stronger than both exhausted relaxations. A useful continuation must attack that amplitude-constrained optimization directly or construct a genuinely stronger certificate that couples information discarded by magnetic spectra and independent simple-cycle packing. Only after a static pointwise bound exists does one-parameter access time become the next resource.

**Boundary.** VIS-220 does not lower-bound the exact torus optimum and does not apply automatically to a different nonlinear, overlapping-cycle or non-packing certificate. Failure of a relaxation is not evidence that the exact problem is hard at the same scale. The conclusion is only that the current magnetic and simple-cycle certificates cannot certify Haar-RMS worst-start suppression in the subcritical regime.