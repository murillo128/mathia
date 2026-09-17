# MI-024 — Complete Farey-field inversion is uniformly conditioned on the square-root prefix

**Evidence level:** exact synthesis from [FD-117](../../findings/FD-117-full-farey-discrepancy-field-is-invertibly-equivalent-to-the-quotient-mertens-staircase.md), [FD-166](../../findings/FD-166-unbounded-exact-farey-horizons-rigidify-a-permanent-source.md), and [FD-167](../../findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md).

The complete Farey discrepancy field is not merely injective on the floor-quotient Mertens data. Its inverse is uniformly stable on the consecutive prefix that matters for permanent-source rigidity. If `E_H` is the `L^2(0,1)` difference between a real source-controlled complete field and the physical Farey field, then the divisor/Fourier inversion gives

`max_(1<=r<=floor(sqrt H)) |A(r)-M(r)| <= sqrt(30) ||E_H||_2`.

The modulus is independent of `H` and of the recovered coordinate. No long triangular error accumulation appears: each quotient coordinate is a bounded divisor functional of the field Fourier coefficients, and Parseval controls all of those functionals at once.

For integer-valued sources this analytic modulus becomes a discrete exact lock. If `||E_H||_2<1/sqrt(30)`, every cumulative difference on the square-root prefix has absolute value below one and is therefore zero; consecutive differencing gives `a(r)=mu(r)` on the whole prefix. A fixed first defect at `n_0` consequently stays at least `1/sqrt(30)` away in complete-field `L^2` for every `H>=n_0^2`.

Thus the dense finite-cutoff kernels from FD-164--FD-165 are not evidence of bad conditioning of the **complete** observation. They survive by moving source freedom outside the currently exposed prefix. Once one measures the full field, the visible prefix is both exact and uniformly conditioned.

The remaining information question is therefore genuinely about observation loss: which Fourier modes, samples, quotient shells or coarsened field data can be removed before the stable growing prefix collapses, and what inverse modulus replaces the constant `sqrt(30)`? That question should be asked before invoking a generic information-counting barrier, because the complete transform already demonstrates that a growing number of source coordinates can have a uniform inverse modulus in the natural field norm.

**Boundary.** This is a complete-field `L^2` theorem. It gives no conditioning guarantee for sparse Fourier data, point samples, finite-dimensional sketches or another norm, and coefficient recovery remains separate from coercivity of the Franel--Landau destination. The constant `sqrt(30)` is explicit but not claimed optimal.