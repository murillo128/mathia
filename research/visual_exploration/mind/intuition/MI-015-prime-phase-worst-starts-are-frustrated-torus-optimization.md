# MI-015 — Prime-phase worst starts require near-saturating frustration before the exact torus problem is touched

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, normalized magnetic-ground-state certificate from VIS-216, exact relaxation lower bound from VIS-217, prime-graph asymptotics in VIS-218, and the exact packing-normalization threshold in [VIS-219](../../findings/VIS-219-cycle-packing-must-saturate-envelope-to-rms.md). No lower bound for the exact torus optimum, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, the worst start is exactly the unit-modulus quadratic optimum `max_|z_p|=1 |z^*A_(y,H)z|`. Kronecker density settles existence of torus phases, not the size of this optimum or the time needed to approach it.

VIS-214 identifies cycle holonomy as the gauge-invariant obstruction to exact coefficient-envelope attainment. VIS-215 turns that obstruction into weighted fractional cycle-packing certificates `P_+` and `P_-`. VIS-216 adds a global normalized magnetic-Laplacian relaxation.

VIS-217--VIS-218 close that spectral relaxation in the whole strictly subcritical prime regime. The actual coefficient graph satisfies `N_eff~y^2/[H(log y)^2]` while the active vertex count is at most `pi(y)`, so `N_eff/n->infinity`; the normalized magnetic certificate therefore misses Haar-RMS scale by a diverging factor regardless of edge phases.

VIS-219 identifies the quantitative burden on the stronger packing route. With `P=min(P_+,P_-)`, `B=2 sum_e w_e`, and `R=2 sum_e w_e^2`, the packing certificate satisfies the exact identity

`(B-P)/sqrt(R)=sqrt(2 N_eff)(1-P/B)`.

Hence a fixed positive fraction of packed frustration is not a meaningful RMS criterion when `N_eff` grows. To prove `max |G|=O(sqrt(R))` through this certificate one needs

`B-P=O(sqrt(R))`,

or `1-P/B=O(N_eff^-1/2)`. In the strictly subcritical prime graph the required relative deficit is `O(sqrt(H) log y/y)->0`: **the two signed cycle packings must asymptotically saturate almost the entire weighted envelope**.

This replaces the vague question “is there extensive magnetic frustration?” by a destination-priced one. The raw quantity `P/|E|` is not even invariant under coefficient rescaling. The live static test is the scale-free residual `D_pack=(B-P)/sqrt(R)`: boundedness would make the deterministic packing certificate strong enough for Haar-RMS suppression; divergence would close this relaxation without saying anything by itself about the exact torus optimum.

The exact fixed-modulus torus problem remains strictly stronger because it retains amplitude constraints discarded by both magnetic and packing relaxations. One-parameter access time is separate and becomes relevant only after a useful static pointwise bound exists.

**Boundary.** VIS-219 states what the `VIS-215` certificate must achieve, not whether it can achieve it. A weak packing certificate can coexist with a much smaller exact torus optimum. The conclusion remains restricted to the static finite graph problem; no recurrence or RH implication follows.