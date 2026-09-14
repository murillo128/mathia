# MI-015 — Prime-phase worst starts are a torus-frustration problem whose spectral relaxation must become nearly maximal

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and fractional cycle-packing certificates from VIS-214--VIS-215, and normalized magnetic-ground-state certificate from [VIS-216](../../findings/VIS-216-normalized-magnetic-gap-certificate.md). No asymptotic certificate for the actual prime graph, useful recurrence-time bound or RH consequence is claimed.

For fixed `y,H`, the worst start is exactly the unit-modulus quadratic optimum `max_|z_p|=1 |z^*A_(y,H)z|`. Kronecker density settles existence of torus phases, not the size of this optimum or the time needed to approach it.

VIS-214 identifies cycle holonomy as the gauge-invariant obstruction to exact coefficient-envelope attainment. VIS-215 turns that obstruction into a weighted fractional cycle-packing lower bound on the positive and negative synchronization energies.

VIS-216 adds a global spectral relaxation. With normalized connection Laplacians `calL_+=D^(-1/2)(D-A)D^(-1/2)` and `calL_-=D^(-1/2)(D+A)D^(-1/2)`, let `bar_lambda_±` be the coefficient-mass-weighted component ground-state averages. Then

`max |z^*Az| / B(A) <= 1-min(bar_lambda_+,bar_lambda_-)`.

This is quantitatively calibrated by the exact Haar variance. If

`N_eff=(sum_e w_e)^2/sum_e w_e^2`,

then `B(A)/sqrt(R(A))=sqrt(2 N_eff)`. Therefore the magnetic relaxation alone reaches RMS scale only if

`1-min(bar_lambda_+,bar_lambda_-) = O(N_eff^(-1/2))`.

A merely positive or constant-size magnetic gap is far too weak when `N_eff` grows: it improves the absolute envelope by only a constant fraction. Static frustration strong enough for the desired pointwise suppression must become **almost maximally coercive** on the effective-edge scale, or the fixed-modulus torus minimum must substantially beat its spectral relaxation.

The live arithmetic problem is thus to determine the actual asymptotic scale of the cycle-packing reward, the normalized magnetic ground states, and—if those relaxations remain weak—the gap between them and the true torus optimum. Only after static suppression is established does one-parameter access time become relevant.

**Boundary.** Magnetic spectra and cycle packing are lower bounds on torus frustration, not exact formulas. A strong graph-theoretic certificate does not by itself control access time, and a weak relaxation does not prove that the exact torus optimum is large.
