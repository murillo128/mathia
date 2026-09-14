# MI-015 — Prime-phase worst starts outlive magnetic and cycle certificates; the correlation SDP is the next exact-scale test

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, normalized magnetic-ground-state certificate from VIS-216, exact relaxation lower bound from VIS-217, prime-graph asymptotics in VIS-218, destination pricing in VIS-219, universal simple-cycle packing ceiling in [VIS-220](../../findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling.md), and exact SDP hierarchy/stress certification in [VIS-221](../../findings/VIS-221-sdp-stress-certificate-retains-torus-interactions.md). No asymptotic SDP-tightness theorem, lower bound for the exact torus optimum, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, the worst start is exactly the unit-modulus quadratic optimum `max_|z_p|=1 |z^*A_(y,H)z|`. Kronecker density settles existence of torus phases, not the size of this optimum or the time needed to approach it.

VIS-214 identifies cycle holonomy as the gauge-invariant obstruction to exact coefficient-envelope attainment. VIS-215 turns that obstruction into weighted fractional cycle-packing certificates. VIS-216 adds a normalized magnetic-Laplacian relaxation. VIS-217--VIS-218 prove that this spectral certificate misses Haar-RMS scale by a diverging factor in the strictly subcritical prime regime, and VIS-219 shows that simple-cycle packing would need near-total envelope saturation. VIS-220 proves that impossible inside that LP: every simple support graph leaves at least `7B/9` residual, so the normalized certificate diverges like `sqrt(N_eff)`.

VIS-221 identifies a stronger global interaction class that is **not** closed by those failures. The standard correlation SDP

`U_+(A)=max Tr(AX),  X>=0, X_ii=1`

with dual `min sum_i d_i` subject to `Diag(d)-A>=0` upper-bounds the positive torus optimum; applying it to `-A` controls the negative side. The VIS-216 magnetic bound is one particular degree-proportional feasible dual point inside this SDP. Hence failure of the magnetic ansatz does not imply failure of the full correlation relaxation.

A stationary torus candidate carries an exact a-posteriori tightness test. If `d_i(z)=conj(z_i)(Az)_i` is real and

`S_z=Diag(d(z))-A >= 0`,

then `z` is a global maximizer and the SDP is rank-one exact. Conversely, an optimal rank-one SDP solution has this PSD stress. This separates “found a plausible phase pattern” from a finite-dimensional proof of the exact torus optimum.

The destination scale still controls whether the stronger certificate is useful. With `B=2 sum_e w_e`, `R=2 sum_e w_e^2`, `N_eff=(sum_e w_e)^2/(sum_e w_e^2)` and signed SDP deficits `Delta_±^SDP=B-U_±`,

`U_abs/sqrt(R)=sqrt(2N_eff)[1-min(Delta_+^SDP,Delta_-^SDP)/B]`.

Therefore the SDP proves Haar-RMS worst-start control only if its smaller signed deficit is `B-O(sqrt(R))`. A constant-factor improvement over the coefficient envelope is not enough.

The live fork is precise. If the canonical prime matrices have `U_abs=O(sqrt(R))`, the desired static upper bound follows even without rank-one exactness. If a rank-one optimizer with PSD stress appears, the exact finite torus optimum is certified. If instead the SDP value is large but the optimizer is high rank, only the relaxation has failed; that gives no lower bound on the exact unit-modulus problem.

**Boundary.** VIS-221 does not prove that the correlation SDP is asymptotically tight or that prime phases create enough frustration. The exact torus objective remains strictly below the SDP unless rank-one tightness is established. One-parameter access time is still separate and should not be mixed into the static certificate question.