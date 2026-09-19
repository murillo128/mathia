# MI-055 — Prime-power Toeplitz positivity has a sparse-sum versus mixed-max completion boundary

**Evidence level:** exact synthesis from [WP-371](../../findings/WP-371-exact-prime-power-toeplitz-carrier-is-indefinite-and-every-positive-completion-pays-a-divergent-diagonal-tax.md) and [WP-372](../../findings/WP-372-mixed-prime-completion-collapses-the-wp-371-diagonal-tax-to-a-finite-sharp-mass.md), interpreted against the critical-scale obstructions in WP-369--WP-370.

The critical prime-power half-density appears as the nonzero Fourier coefficients of a centered Poisson kernel. On a single prime ray, positivity of `aI+C_r` with `r=p^(-1/2)` requires the exact local diagonal

`a >= 2/(sqrt(p)+1)`.

After multiplication by `log p`, independent scalar completion of every prime therefore pays

`c_p^+=2 log p/(sqrt(p)+1)`,

and `sum_p c_p^+` diverges. WP-371 correctly identifies this as the sharp cost of **sparse/separable** local completion.

WP-372 shows that it is not the sharp cost of arbitrary global scalar positivity. On `G=Q_+^x` with prime-torus dual, allow unconstrained mixed-prime Fourier coefficients while fixing every one-prime ray to the positive critical coefficients. A finite positive measure exists exactly when its total mass satisfies

`C >= C_+^* := sup_p c_p^+`,

and this supremum is finite, attained at `p=13`. An explicit product measure realizes the completion, with mixed coefficients equal to products of the prescribed one-prime moments scaled by powers of `C`.

The distinction is exact. If mixed-prime coefficients are forced to vanish, positivity on each finite prime set again requires the **sum** of the local minima and diverges. The same sparse sum obstruction survives when the carrier is assembled first on the common prime-log translation line, because multiplicative independence makes that line dense in each finite prime torus. Thus mixed-prime freedom changes the completion cost from a divergent sum to a finite maximum.

The reusable audit is therefore global. A divergent local positive-completion tax is not fundamental until the allowed cross-coordinate coefficients are specified and the full positive-definite extension problem is solved. Conversely, a finite mixed completion is not arithmetic leverage when its cross-prime coefficients are freely engineered from the target moments and reproduced by a universal product control.

The surviving Weil route must sit between these extremes: it needs mixed-prime coefficients **forced by the arithmetic/archimedean source construction**, enough freedom to keep global positivity finite, and an independently fixed sign/orientation not present in the universal product completion.

**Boundary.** WP-372 classifies the positive-sign scalar completion with unconstrained mixed-prime coefficients and the sparse/common-line control. It does not construct a Weil-positive form, supply the archimedean term, make the mixed coefficients source-specific, or imply RH. The product completion is a matched control, not a successful sign mechanism.
