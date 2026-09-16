# MI-038 — Block-stationary arithmetic rescue is density-sparse at sublogarithmic capped transport

**Evidence level:** literature+derived synthesis from [NB-167](../../findings/NB-167-capped-poisson-transport-unifies-conditioning-and-wasserstein-conservation.md) and [NB-168](../../findings/NB-168-block-stationary-templates-make-logarithmic-euler-rescue-sparse.md). Montgomery--Vaughan mean-value theory is classical external input; the capped-transport coefficient reduction and its use against the NB-167 arithmetic-rescue loophole are line-specific.

NB-167 leaves a genuine source-specific possibility after generic Poisson geometry is exhausted: the actual values of `zeta'/zeta` could align with a signed compact sampler and produce a completed conservation defect much larger than the worst-case bounded-Lipschitz estimate suggests.

NB-168 separates **persistent mechanism** from **rare resonance**. Let one signed offset template `nu_T` be fixed while its center `t` ranges across `[T,2T]`, and let `T_T` be its Jordan transport cost in the one-Poisson-width metric `min{1,|u-v|/a_T}`. The Fourier transform of the signed template obeys

`|nu_hat_T(xi)| <= 2 T_T (1+a_T|xi|)`.

After inserting the absolutely convergent Euler series for `zeta'/zeta(1+a_T+it)`, Montgomery--Vaughan mean-value theory gives

`int_T^(2T) |E_T(t)|^2 dt << T_T^2 (T+a_T^(-2))`.

If `Xi_T=T_T/q_T`, Chebyshev therefore bounds the relative set of centers with arithmetic defect at least `eta q_T log T` by

`<< Xi_T^2/(eta^2 log^2 T) * (1+(T a_T^2)^(-1))`.

Thus in the broad high-ordinate regime `T a_T^2 -> infinity`, the condition `Xi_T=o(log T)` forces logarithmic Euler rescue onto a set of relative measure `o(1)`. A compact shape can have much larger capped mismatch than the pointwise NB-167 conservation threshold and still fail to exploit arithmetic phases persistently across the block.

The reusable distinction is between **source-specific adaptation** and **source-specific coincidence**. A fixed observation geometry that occasionally aligns with the arithmetic source does not constitute a stable mechanism unless the alignment survives the relevant family quantifier. Mean-square control can rule out persistence even when it cannot rule out isolated exceptional centers.

This narrows the surviving compact sampler routes. A mechanism must adapt its signed shape to height, concentrate on a genuinely sparse exceptional sequence, spend logarithmic capped transport, or enter the ultra-thin `a_T \lesssim T^(-1/2)` regime where the current weighted mean-square remainder becomes comparable. The first two possibilities are now explicitly selective rather than consequences of generic fixed-template geometry.

**Boundary.** Density-zero exceptional centers are not pointwise exclusion. A sparse zero-selected architecture could still place all of its targets inside the exceptional set unless a separate theorem gives a robustness interval or another counting/spacing bridge. The result also permits the template to change between dyadic blocks and does not cover a shape chosen adaptively from the local values of the source inside a block.
