# MI-015 — Prime-phase worst starts are a torus-frustration problem whose magnetic relaxation has a dimension floor

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, normalized magnetic-ground-state certificate from VIS-216, and the exact relaxation lower bound from [VIS-217](../../findings/VIS-217-normalized-spectral-certificate-dimension-floor.md). No asymptotic theorem for the actual prime graph, exact torus optimum, recurrence time or RH consequence is claimed.

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

This makes the first spectral gate purely structural: **the normalized magnetic relaxation can reach Haar-RMS scale only if `N_eff=O(n)`.** When effective edge mass is superlinear in the number of active vertices, no choice of phases or holonomies can repair the spectral certificate; its Frobenius mass already enforces too large an operator norm.

The live arithmetic problem therefore branches cleanly. First determine the actual scale of `N_eff(y,H)/n(y,H)`. If it diverges, the normalized spectral route is closed as a standalone RMS certificate and one must use stronger cycle packing or the exact fixed-modulus torus constraint. If it stays bounded, the dimension floor does not kill the route, but one still needs the near-extremal eigenvalue control demanded by VIS-216.

Only after a static pointwise bound is established does one-parameter access time become relevant.

**Boundary.** VIS-217 limits the relaxation, not the exact torus optimum. A weak spectral certificate does not prove a large worst-start value, and `N_eff=O(n)` is only necessary, not sufficient, for RMS-scale spectral suppression.
