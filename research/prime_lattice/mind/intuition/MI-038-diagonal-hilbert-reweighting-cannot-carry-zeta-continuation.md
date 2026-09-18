# MI-038 — Diagonal Hilbert reweighting cannot carry zeta continuation through bounded evaluation

**Evidence level:** exact synthesis from [PL-359](../../findings/PL-359-hamburger-functional-equation-h2-triviality.md) and [PL-360](../../findings/PL-360-diagonal-weighted-hilbert-spaces-cannot-carry-zeta-continuation.md), using the classical weighted Dirichlet-series RKHS framework audited in PL-360.

PL-359 shows that native Dirichlet `H^2` is too small for the nonzero conductor-one functional-equation solution: Hamburger rigidity selects zeta, but the all-ones coefficient vector is not square-summable. The obvious repair is to shrink the coefficient weights so that zeta becomes a finite-norm vector.

PL-360 shows why this fails for every positive diagonal coefficient metric. If

`||sum a_n n^-s||_w^2=sum |a_n|^2 w_n`,

then bounded point evaluation at `Re s=sigma` is equivalent to

`sum n^(-2sigma)/w_n < infinity`.

If a target coefficient vector `c=(c_n)` belongs to the same Hilbert space, Cauchy--Schwarz forces

`sum |c_n| n^-sigma < infinity`.

For zeta, `c_n=1`. Thus making the zeta vector finite norm while retaining ordinary bounded evaluation would imply absolute convergence of `sum n^-sigma`. No diagonal weight sequence can therefore support both requirements anywhere with `sigma<=1`, including the critical strip.

The reusable point is a **primal/dual topology tradeoff**. A completion is not useful merely because it contains the desired source vector. The dual destination functional must also remain continuous where the theorem needs to read it. In a diagonal RKHS, making a large coefficient vector cheaper automatically makes the corresponding evaluation kernels more expensive, and Cauchy--Schwarz reconstructs the original absolute-convergence wall.

This is stronger than the failure of one natural weight. It rules out every positive diagonal metric on the exponent-lattice monomial basis with ordinary continuous point evaluation. A viable completion must change the correlation structure, the destination pairing, or both: non-diagonal Gram geometry, target-relative/model/quotient spaces, rigged/distributional completions, or a controlled unbounded/renormalized continuation are qualitatively different possibilities.

**Boundary.** The obstruction does not rule out analytic continuation of an individual element by external means, non-diagonal Hilbert spaces, Banach/rigged spaces, or unbounded destination functionals. It says only that diagonal coefficient Hilbertization plus ordinary bounded evaluation cannot move zeta past its absolute-convergence boundary.