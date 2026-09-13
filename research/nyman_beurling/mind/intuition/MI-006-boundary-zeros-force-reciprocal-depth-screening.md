# MI-006 — Finite-prediction affordability is controlled by inverse boundary singularity, not qualitative outerness

**Evidence level:** exact for the stationary outer-polynomial matched-control class through NB-083, combined with the exact branch-charge comparison of NB-082. No corresponding rate for the actual nonstationary Nyman innovations is proved.

NB-082 identifies the normalized finite-prediction excess `a_(psi,L)` as the scalar resource controlling the depth-`L` prediction-volume charge. Qualitative outerness says only `a_(psi,L)->0`; it does not determine how much future depth is needed to reach the destination scale `1/R`.

NB-083 classifies that rate sharply for outer polynomial filters. After normalizing `f=psi/psi(0)`, the anchored inverse problem is

`a_(psi,L)=inf ||f p-1||_(H^2)^2`

among degree-`L` polynomials with `p(0)=1`. If `f` has boundary zeros of multiplicities `k_r`, then

`a_(psi,L) = [sum_r k_r^2]/L + o(1/L)`.

Zeros strictly outside the closed disk do not change that leading boundary law. If instead every zero lies strictly outside the unit circle, the inverse is analytic across the boundary and `a_(psi,L)` decays geometrically.

Branching amplifies this analytic distinction into a future-horizon dichotomy. The charge is comparable to `R a_(psi,L)`: a boundary zero forces depth `L=Omega(R)` merely for bounded screening and `L/R->infinity` for vanishing screening, so the physical horizon `m^L R` is exponential or worse. With a strictly exterior zero set, logarithmic depth `L=O(log R)` suffices and the physical horizon remains polynomial.

The durable point is that **forward smoothness, polynomiality and outerness can coexist with an exponentially expensive inverse-prediction boundary layer**. What matters is quantitative inverse stability at the unit-circle boundary. An affordable arithmetic Nyman theorem must therefore prove more than cyclicity: it must supply a source-specific prediction rate strong enough to beat the boundary-zero control, or avoid finite prediction entirely.

**Boundary.** NB-083 is a stationary polynomial calibration. It does not assert that the actual Nyman innovation filter has a boundary zero, a polynomial symbol, or reciprocal-depth prediction error. The arithmetic source is nonstationary, so transferring the rate requires a proved source dictionary rather than analogy.
