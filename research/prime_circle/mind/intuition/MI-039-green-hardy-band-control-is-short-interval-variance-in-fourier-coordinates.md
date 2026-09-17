# MI-039 — Green-Hardy band control is short-interval variance in Fourier coordinates

**Evidence level:** exact synthesis from [PC-330](../../findings/PC-330-li-subtraction-removes-low-mode-mean-not-prime-hilbert-energy.md) through [PC-333](../../findings/PC-333-green-hardy-band-is-cyclic-short-interval-prime-variance.md).

PC-331--PC-332 isolate the source-sensitive Green excess as a positive functional of the Fourier magnitude-square profile and reduce its growth to cumulative low-frequency energy. PC-333 identifies the remaining band theorem: after reciprocal change of scale, it is the cyclic short-interval variance problem for the same prime residual.

For a cyclic window of length `L`, Parseval gives

`M_q(L)=(1/q) sum_h |d_hat_q(h)|^2 |D_L(h)|^2`.

At reciprocal frequency scale `H asymp q/L`, a natural short-window variance estimate implies `E_q(H) lesssim H mu_q^res`. Conversely, uniform band control over the needed dyadic range implies the corresponding window variance up to absolute constants. Hard and Fejer frequency cutoffs make the same equivalence at neighboring scales.

Thus the scalar Green-Hardy band target is not an independent spectral mechanism. Once the construction has quotiented away phase and retained only Fourier magnitudes, its surviving analytic content is classical short-interval prime-discrepancy energy in finite cyclic coordinates. A proof by ordinary analytic-number-theory means would therefore solve the classical variance problem in another representation rather than bypass it.

The reusable test is concrete: when a positive spectral quantity factors through `|d_hat|^2`, apply the reciprocal-scale window transform before assigning new spectral meaning. If the resulting functional is a standard moving-window variance, geometry has not yet supplied additional arithmetic leverage.

**Boundary.** This classicalizes the scalar band estimate; it does not prove the required short-interval variance. Prime Circle could still add genuine information through a geometry-forced proof, a stronger range/asymptotic, phase or cross-level structure, or a separate zero-sensitive theorem not determined by the magnitude-square quotient.