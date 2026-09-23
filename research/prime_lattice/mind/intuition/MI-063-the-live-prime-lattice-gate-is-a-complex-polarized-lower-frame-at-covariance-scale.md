# MI-063 — The live prime-lattice gate is a complex-polarized lower frame at covariance scale

**Evidence level:** supported by the exact cone criterion of PL-421, the polarization obstruction of PL-428, and the theorem-strength refinements [PL-435](../../findings/PL-435-mrstt-hardy-littlewood-second-order-variance-gap.md) and [PL-436](../../findings/PL-436-scalar-variance-lower-bounds-do-not-close-oriented-cone.md).

The local-factor deletion problem does not require a full asymptotic formula for the residue covariance. At `p=5`, the actual gate is the Loewner lower bound encoded by the normalized correlation matrix,

`lambda_min(C_X) >= 1/4`,

or equivalently a uniform lower-frame inequality for every complex polarization `z in C^4`. PL-436 makes this distinction operational: trace bounds, separate diagonal variances, or lower bounds restricted to real probes can all hold while the least Hermitian eigenvalue still fails the cone test. The imaginary coherences identified in PL-428 are part of the required observable.

PL-435 simultaneously sharpens the scale at which such a theorem must act. After the Hardy--Littlewood main terms cancel in the triangular covariance, the residual has the weighted form

`R_H = 2 sum_(h<H) (H-h) E(h)`.

A first-order averaged estimate such as `sum |E(h)| = o(HX)` only gives `o(XH^2)`, whereas the covariance to be protected lives at scale `X H L_X`, with `L_X` of logarithmic size in the present regime. The missing factor is therefore polynomial in `H/L_X`; arbitrarily strong fixed logarithmic savings at density scale do not by themselves reach the spectral-margin scale.

Taken together, these findings identify a more economical but more precise theorem target than “compute the whole covariance.” A viable unconditional prime-side result may prove only a one-sided lower frame, but it must do so for complex polarizations and at the natural covariance scale, including the oriented quarter-turn information required by the source representation. Conversely, a theorem that is scalar, all-real, or only first-moment accurate is aimed at the wrong gate even if its error term looks very strong in isolation.

This separates two kinds of difficulty that were previously easy to conflate. Representation theory says which matrix directions must survive; second-order arithmetic says how accurately the source must be controlled. The live route needs both simultaneously, but it need not pay for a full entrywise asymptotic if a direct complex-polarized lower-frame estimate is available.

**Boundary.** No such unconditional lower-frame theorem is established here. PL-435 is a theorem-strength obstruction to a particular first-order Hardy--Littlewood transfer, and PL-436 identifies the sufficient cone observable; neither proves that the actual prime covariance satisfies the required lower bound.