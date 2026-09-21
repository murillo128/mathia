# MI-059 — Fixed regular refinement weights collapse to the universal disk

**Evidence level:** exact/asymptotic operator synthesis from [PC-380](../../findings/PC-380-common-anchor-chord-weighted-refinement-is-a-universal-qmf-shift.md), [PC-381](../../findings/PC-381-fixed-finite-bandwidth-refinement-weights-collapse-to-universal-qmf.md), and [PC-382](../../findings/PC-382-fixed-continuous-refinement-weights-have-universal-disk-limit.md), following the Chebyshev/tent reductions PC-372--PC-379. The transfer/QMF and periodic quadrature mechanisms are classical; the line-specific content is the boundary they impose on fixed Prime-Circle branch profiles.

For the circle power map `V_m f(z)=f(z^m)` and a fixed bounded scalar weight `q`, set `S_(m,q)=M_q V_m`. The exact identity

`S_(m,q)^* S_(m,q) = M_(E_m(|q|^2))`

reduces the norm geometry to the average of `|q|^2` over each `m`-root fiber. PC-381 shows exact collapse when `|q|^2` has finite Fourier bandwidth `D`: for every `m>D`, the fiber average is constant, the normalized operator is a proper isometry, and its adjoint spectrum is the universal closed disk. Every fixed positive integer chord power is included.

PC-382 shows that finite bandwidth was not the essential hypothesis. If `q` is any fixed nonzero continuous profile, uniform continuity of `|q|^2` and the equally spaced root fibers give

`||T_(m,q)^* T_(m,q)-I|| <= omega_(|q|^2)(2pi/m)/||q||_2^2 -> 0`.

The actual adjoint spectrum is squeezed between disks of radii `sqrt(1-delta_m)` and `sqrt(1+delta_m)`, so it converges in Hausdorff distance to the unit disk along primes, composites or any `m->infinity`. A fixed continuous infinite Fourier tail therefore does not retain an order-one arithmetic spectral shape either.

The durable boundary is that **fixed regular one-point geometry is asymptotically averaged away at the inverse-image mesh scale**. A scalar escape must vary with the conductor on scale `1/m`, become genuinely singular or use a shrinking regularization, magnify the vanishing defect with an independently forced scale, or leave the scalar one-fiber setting through nonlinear/tensor/cross-level coupling or a source-dependent domain.

**Boundary.** PC-382 requires one fixed continuous profile; it does not cover conductor-dependent families without a uniform modulus of continuity, unbounded inverse-chord weights on the canonical Haar `L^2` space, mesh-scale singular regularizations, matrix/nonlinear branch data or cross-level nonseparable operators. Universal disk convergence is a no-go for this fixed regular scalar class, not for every weighted refinement.