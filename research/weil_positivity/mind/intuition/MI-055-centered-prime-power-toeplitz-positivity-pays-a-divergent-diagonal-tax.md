# MI-055 — Prime-power Toeplitz positivity has a mixed-completion escape but no continuous scalar sparsification

**Evidence level:** exact synthesis from `WP-371`--`WP-373`, interpreted against the critical-scale obstructions in WP-369--WP-370.

The critical prime-power half-density appears as the nonzero Fourier coefficients of a centered Poisson kernel. On a single prime ray, positivity of `aI+C_r` with `r=p^(-1/2)` requires the exact local diagonal `a>=2/(sqrt(p)+1)`. After multiplication by `log p`, independent scalar completion of every prime therefore pays `c_p^+=2 log p/(sqrt(p)+1)`, and `sum_p c_p^+` diverges. WP-371 correctly identifies this as the sharp cost of **sparse/separable** local completion.

WP-372 shows that it is not the sharp cost of arbitrary global scalar positivity. On `G=Q_+^x` with prime-torus dual, allow unconstrained mixed-prime Fourier coefficients while fixing every one-prime ray to the positive critical coefficients. A finite positive measure exists exactly when its total mass satisfies `C>=C_+^*:=sup_p c_p^+`, and this supremum is finite. An explicit product measure realizes the completion, with mixed coefficients given by products of the prescribed one-prime moments.

The distinction is exact. If mixed-prime coefficients are forced to vanish, positivity on each finite prime set again requires the **sum** of the local minima and diverges. The same sparse sum obstruction survives when the carrier is assembled first on the common prime-log translation line. Thus mixed-prime freedom changes the completion cost from a divergent sum to a finite maximum.

WP-373 then tests the natural two-stage repair: take the finite positive mixed completion and use a regular scalar common-line response to delete mixed modes afterward. For the explicit product completion, already the mixed two-prime frequencies `m log 2+n log 3` with `m,n!=0` are dense in `R`. Any continuous scalar multiplier `M` that kills all of them must satisfy `M=0` on a dense set and hence `M≡0`; it cannot retain any pure prime-power frequency. Ordinary `L^1` convolution kernels and finite-measure convolutions are therefore excluded.

This obstruction is genuinely infinite rather than a finite algebraic collision. For every finite set of mixed frequencies to erase and pure frequencies to retain, one can interpolate the desired `0/1` values with `M in C_c^infinity(R)`, whose inverse Fourier transform is Schwartz. Bounded-frequency experiments can therefore realize perfect post-selection even though no continuous scalar limit performs the full infinite sparsification.

The reusable audit now has two stages. First solve the **global positive-definite extension** problem rather than summing local taxes. Then audit the topology of any proposed quotient back to the sparse arithmetic carrier. A positive mixed completion is not useful merely because it exists, and a finite exact selector does not imply an infinite regular selector.

The surviving Weil route must either keep a source-forced mixed-prime sector in the final pairing and derive its orientation from arithmetic/archimedean structure, or use a post-processing mechanism outside the continuous scalar common-line class—non-scalar, nonlinear, source-dependent, genuinely rough or geometric—with an independent positivity theorem.

**Boundary.** WP-373 does not rule out arbitrary distributional multipliers, non-scalar responses or criteria that retain mixed modes. WP-372 still does not supply Gamma/polar terms or make the mixed coefficients source-specific. None of WP-371--WP-373 proves a Weil-positive form or RH.
