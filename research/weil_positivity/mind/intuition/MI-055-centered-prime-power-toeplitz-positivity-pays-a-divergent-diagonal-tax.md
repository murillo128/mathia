# MI-055 — Centered prime-power Toeplitz positivity pays a divergent diagonal tax

**Evidence level:** exact synthesis from [WP-371](../../findings/WP-371-exact-prime-power-toeplitz-carrier-is-indefinite-and-every-positive-completion-pays-a-divergent-diagonal-tax.md), interpreted as the first non-diagonal continuation of the critical-scale obstruction in WP-369--WP-370.

The critical prime-power half-density does admit a canonical translation representation, but it appears in the wrong part of the canonical positive kernel.

Let `U` be a bilateral unitary shift and

`C_r=sum_(k>=1) r^k(U^k+U^(-k))`, `0<r<1`.

For `r=p^(-1/2)`, multiplying by `log p` gives the exact symmetric prime-power coefficient pattern

`(log p) p^(-k/2)`

on the nonzero translates. The Fourier symbol is

`c_r(theta)=P_r(theta)-1`,

where `P_r` is the positive Poisson kernel. Thus the exact Weil-shaped carrier is the **centered** part of a positive harmonic object, not the positive object itself.

This distinction has an exact completion cost. Since

`min_theta c_r(theta)=-2r/(1+r)`,

the scalar translation-invariant completion

`a I + C_r`

is positive if and only if

`a >= 2r/(1+r)`.

At the critical prime scale, even the optimal local diagonal repair therefore costs

`2 log p/(sqrt(p)+1)`.

The sum of these minimal costs over the primes diverges. Keeping the full Poisson kernel is no escape: it adds the larger zero Fourier coefficient `1` at every prime. Removing the accumulated diagonal after the local positivity argument is likewise not intrinsic positivity; it is a subtraction outside the sign theorem.

The reusable mechanism is a **positive-completion audit**. When the desired arithmetic coefficients are off-diagonal Fourier coefficients of a familiar positive kernel, identify whether they belong to the full kernel or only to its centered/sign-indefinite part. If positivity requires adding a diagonal direction, compute the smallest allowed completion before treating that direction as normalization. Here the local completion is exact and the resulting global zero-mode mass is infinite.

This sharpens the surviving operator-valued route from WP-370. Cross-index coupling by itself is insufficient if it decomposes prime-by-prime into scalar positive Toeplitz blocks. A successful sign mechanism must cancel, quotient or absorb the accumulated diagonal **inside one source-forced global finite--archimedean or cross-prime structure before positivity is asserted**. The compensation must itself preserve the positive form on the admissible global subspace; subtracting local baselines afterwards only restores the original indefiniteness.

**Boundary.** WP-371 classifies scalar translation-invariant diagonal completions that preserve the exact nonzero prime-power coefficients. It does not classify matrix-valued, cross-prime, finite--archimedean or constrained-subspace completions. It does not prove that no global positive operator exists, supply the archimedean term, or imply RH. The divergence is a no-go for independent local scalar completion, not for every global operator-valued construction.
