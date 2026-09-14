# MI-015 — Prime-phase worst starts are a torus-frustration problem whose normalized magnetic relaxation fails in the subcritical regime

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, normalized magnetic-ground-state certificate from VIS-216, exact relaxation lower bound from VIS-217, and its prime-graph asymptotic specialization in [VIS-218](../../findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md). No lower bound for the exact torus optimum, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, the worst start is exactly the unit-modulus quadratic optimum `max_|z_p|=1 |z^*A_(y,H)z|`. Kronecker density settles existence of torus phases, not the size of this optimum or the time needed to approach it.

VIS-214 identifies cycle holonomy as the gauge-invariant obstruction to exact coefficient-envelope attainment. VIS-215 turns that obstruction into a weighted fractional cycle-packing lower bound on synchronization energy. VIS-216 adds a global normalized magnetic-Laplacian relaxation.

VIS-217 identifies the intrinsic ceiling of that spectral relaxation. On a connected component with `n` vertices, let `M=D^-1/2 A D^-1/2`. The VIS-216 certificate is exactly

`U_spec=B(A)||M||_op`,

and phase removal plus tracelessness force

`||M||_op >= 1/sqrt(n-1)`.

Equivalently, if

`N_eff=(sum_e w_e)^2/sum_e w_e^2`,

then

`U_spec/sqrt(R(A)) >= sqrt(2 N_eff/(n-1))`.

VIS-218 now prices this gate on the actual prime coefficient graph throughout the strictly subcritical regime `H log y/y -> 0`. There

`W_1 asymp y/(H log y)`,

`W_2 asymp 1/H`,

and hence

`N_eff asymp y^2/(H (log y)^2)`.

Since the number of active prime vertices is at most `pi(y)`,

`N_eff/n >> y/(H log y) -> infinity`.

Therefore

`U_spec/sqrt(R_v) >> sqrt(y/(H log y)) -> infinity`.

The normalized magnetic relaxation is thus **closed as a standalone Haar-RMS certificate on the entire strictly subcritical prime regime**. No choice of edge phases, cycle holonomies or magnetic ground state can repair that relaxation, because its phase-blind effective dimension is already too large.

The live static branch is now the stronger fractional cycle-packing/frustration route or the exact fixed-modulus torus optimization, both of which retain information discarded by the variable-amplitude normalized spectral relaxation. One-parameter access time remains a separate question and becomes relevant only after a pointwise static bound exists.

**Boundary.** VIS-218 limits the relaxation, not the exact torus optimum. A large spectral upper certificate does not prove that the true worst-start value is large. The conclusion is also restricted to the strictly subcritical scale; the constant critical transition `H asymp y/log y` is not covered by the same effective-edge-density asymptotic.