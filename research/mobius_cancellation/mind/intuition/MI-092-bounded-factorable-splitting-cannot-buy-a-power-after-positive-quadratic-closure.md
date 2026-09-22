# MI-092 — Bounded factorable splitting cannot buy a power after positive quadratic closure

**Evidence level:** exact Hilbert-space obstruction plus the persisted classical bounded-component sieve decomposition in [MC-453](../../findings/MC-453-bounded-factorable-splitting-cannot-dilute-quadratic-diagonal.md), sharpening the auxiliary-factorability requirement of MI-091.

Suppose an auxiliary sieve coefficient is decomposed as `lambda=sum_(j<=J) lambda^(j)` and every component is sent through the same linear observable `T` before being estimated by a separate positive quadratic energy. Then

`sum_j ||T lambda^(j)||^2 >= J^(-1) ||T lambda||^2`.

This is just Cauchy--Schwarz, but it fixes the exponent accounting. A bounded number of components can dilute the recombined diagonal only by a constant, and `J=D^(o(1))` only by a subpower factor. A fixed power saving cannot come from the decomposition index itself unless the component count is polynomially large.

For the classical Iwaniec linear-sieve surrogate relevant to the live q-vdC route, the persisted literature audit in MC-453 places the standard well-factorable replacement in exactly this bounded-component regime. Therefore replacing one sieve weight by boundedly many well-factorable pieces and then squaring or taking absolute values componentwise does **not** defeat the MC-415 quadratic diagonal. It merely reorganizes that positive cost.

Well-factorability remains potentially useful only before this positive closure. Inside a component, a representation `lambda^(j)=beta_j*gamma_j` exposes factor variables whose ranges can be matched to a bilinear, dispersion or Type I/II estimate. Alternatively, if the component sum remains coherent through an oscillatory transform, cross terms between distinct components may cancel. Both possibilities require retaining structure that the separate-energy step discards.

Combined with MI-091, the representation gate is now sharper. The needed factor variables are neither latent in raw truncated Möbius nor supplied by the mere existence of a bounded decomposition. They must be used internally, before recombination/majorization destroys them, and the resulting signed estimate must still transfer quantitatively back to the Möbius target.

**Boundary.** The inequality compares components under the same linear map and controls only the sum of separately squared norms. It does not rule out gains from the internal convolution variables, operator changes induced before the quadratic step, or explicit cross-component interference. No improved bound for `M(x)` follows from the obstruction itself.