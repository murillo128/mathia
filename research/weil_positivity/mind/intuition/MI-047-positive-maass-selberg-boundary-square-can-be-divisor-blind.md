# MI-047 — Constant-mode Hecke boundary positivity collapses to universal Brownian overlap geometry

**Evidence level:** exact/literature-backed synthesis from [WP-237](../../findings/WP-237-arthur-height-operations-cannot-isolate-the-zeta-zero-block.md), [WP-345](../../findings/WP-345-maass-selberg-height-derivative-is-a-positive-boundary-square-but-does-not-constrain-the-scattering-divisor.md) through [WP-347](../../findings/WP-347-self-adjoint-point-scatterers-show-one-cusp-hyperbolic-realizability-does-not-fix-the-scattering-divisor.md), and [WP-356](../../findings/WP-356-hecke-truncation-commutator-is-positive-cusp-annulus-energy-but-does-not-isolate-weil-prime-weight.md) through [WP-357](../../findings/WP-357-finite-hecke-polynomial-cusp-boundary-grams-are-universal-brownian-overlap-geometry.md).

The rank-one Maaß--Selberg relation supplies a genuine source-defined positive boundary object, but the boundary derivative deletes the height-independent logarithmic-derivative term carrying the scattering divisor. Self-adjoint Robin and point-scatterer controls then show that positive truncated norms and geometric realizability do not by themselves fix that divisor.

WP-356 inserts finite-prime Hecke structure before the positive closure. On the constant Fourier mode, after the natural unitary change to log height, the normalized prime Hecke operator is `T_p=S_(log p)+S_(-log p)`. Its commutator with a sharp cusp projection has square equal to an interval projection, so the prime label survives positivity only as unsigned annulus width. The critical scattering phase remains in a sign-indefinite interference term and the natural normalization does not preserve the desired `p^(-1/2)` weight through the quadratic norm.

WP-357 closes the natural finite-Hecke extension of that escape. For general `n`, the constant-mode normalized Hecke operator is a finite symmetric translation polynomial

`T_n = sum_(d|n) S_(log(n/d^2))`.

The sharp-boundary defect vectors have Gram kernel

`K(a,b)=1_(ab>0) min(|a|,|b|)`,

which is simply two copies of Brownian covariance. Consequently every finite Hecke polynomial and every finite positive Gram/correlation construction built from these boundary defects lives in a universal overlap geometry determined only by the translation lengths.

The arithmetic multiplication law does not rescue selectivity. One may replace the prime lengths `log p` by arbitrary positive lengths while preserving the normalized Hecke algebra identities and every finite boundary-Gram positivity inequality. Likewise a standing wave `e^(itx)+eta(t)e^(-itx)` remains a simultaneous eigenwave for arbitrary reciprocal unimodular phase `eta`, so divisor-changing CDD freedom survives the positivity architecture. Finite cross-prime interference exists, but its positive Gram geometry is still universal nested-interval overlap.

The reusable principle is therefore stronger than “arithmetic insertion before positivity is insufficient”: **a whole finite arithmetic operator algebra can survive before scalarization while its positive boundary closure factors through a universal geometric kernel**. To claim Weil selectivity, one must identify a post-closure carrier that fails this arbitrary-length/arbitrary-phase matched control.

This removes “several finite Hecke operators on the constant mode before scalarization” from the residual frontier. What remains genuinely different includes nonconstant Fourier modes, infinite/all-prime completion where convergence may add structure, higher-rank or adelic truncation, nonlocal operator order not reducible to finite boundary Grams, or a source theorem coupling Euler/Hecke rigidity to a noncentral positive object before the universal overlap quotient.

**Boundary.** The argument is finite and constant-mode. It does not classify nonconstant Fourier coupling, an infinite Hecke completion, adelic/higher-rank geometry, or every possible nonlocal positive operator. The continuous/arbitrary-length controls show that the tested positivity is universal, not that the Hecke identification itself is fake.