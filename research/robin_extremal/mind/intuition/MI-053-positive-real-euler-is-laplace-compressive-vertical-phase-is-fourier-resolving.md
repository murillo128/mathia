# MI-053 — Positive-real Euler is Laplace-compressive; vertical phase is Fourier-resolving

**Evidence level:** exact synthesis from [RE-193](../../findings/RE-193-dyadic-laplace-compression-makes-euler-stable-dimension-logarithmic.md), [RE-199](../../findings/RE-199-full-real-euler-collapse-persists-through-sub-quarter-linear-depth.md), and [RE-200](../../findings/RE-200-vertical-euler-phase-supports-linear-stable-dimension-on-one-prime-shell.md). The Laplace/Fourier distinction is classical; the Mathia content is its exact realization by ordinary-prime Euler atoms with controlled prime-power error.

The same logarithmic prime coordinate can be either erased or resolved depending on the spectral direction in which the Euler product is observed. Write `q=Qe^x`. After the common selector-shell normalization, the first Euler harmonic on the positive real ray contributes essentially

`e^(-u x)`,

whereas on a vertical line it contributes

`e^(-sigma x)e^(-it x)`.

The real parameter `u` therefore produces Laplace damping. Large products `ux` are exponentially suppressed, so source locations far enough into the shell become redundant at finite precision. RE-193 makes this quantitative: the positive-real channel has a separated approximation whose rank grows only logarithmically in the spectral-logwidth rectangle and requested precision. RE-196--RE-199 then show that exact moment cancellation can exploit that geometry strongly enough to make the complete positive real ray almost blind while a Robin-scale transient survives.

Imaginary motion is different. The factor `e^(-itx)` keeps unit modulus and converts logarithmic prime position directly into Fourier phase. RE-200 places actual ordinary primes near an equally spaced log grid and samples the dual frequency grid. The exact Euler response matrix is a diagonally weighted DFT plus a vanishing perturbation from prime placement and prime powers, so `K` prime atoms on one fixed shell retain `K` uniformly conditioned Euclidean directions up to height `t=O(K)`.

The reusable lesson is that **sample count is not the resource; spectral geometry is**. A continuum of positive-real samples may have very small stable dimension because all rows point along a Laplace-compressed manifold. A comparable number of vertical samples can instead resolve log-location through phase. Results about positive-real inverse conditioning should therefore not be extrapolated to complex Euler data without a separate argument.

This does not make complex sampling automatically source-rigid. High representation rank only says that the observation family has room to distinguish many source directions. A matched `{0,1,2}` control may still arrange cancellation across those directions, and a Robin proof still needs a source-native reason why some vertical Fourier coefficient must survive. The next useful question is therefore not whether complex samples contain more formal information, but whether the specific matched controls that defeat the real ray can also defeat a growing vertical Fourier frame.

**Boundary.** The exact RE-200 conditioning statement is for a fixed multiplicative shell, where one common normalization keeps all honest one-prime columns comparable. Growing source width, bounded-height vertical resolution and integer-multiplicity matching require separate analysis. The intuition records the representation distinction, not a claim that complex phase already closes the Robin matched-control escape.