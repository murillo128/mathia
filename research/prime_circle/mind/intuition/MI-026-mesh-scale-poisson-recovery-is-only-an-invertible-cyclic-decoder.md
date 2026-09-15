# MI-026 — Mesh-scale Poisson recovery is only an invertible cyclic decoder

**Evidence level:** exact-derived and classicalized by [PC-310](../../findings/PC-310-mesh-scale-poisson-boundary-layer-is-an-invertible-cyclic-filter.md), completing the first unresolved radial regime left by PC-309.

Let `f` be centered data on `Z/qZ`, `T` the one-step shift, and sample the disk Poisson extension on the `q` polygon angles. Roots-of-unity aliasing gives

`hat(P_r f)_samp(h) = hat f(h) sum_(m in Z) r^|h+mq|`.

At the mesh boundary layer `r=e^(-a/q)` the matched difference `Tf-f` therefore has multiplier

`M_(q,a)(h)=(e^(-2 pi i h/q)-1) * (e^(-a h/q)+e^(-a(1-h/q)))/(1-e^(-a))`.

For every `h=1,...,q-1`, `M_(q,a)(h)!=0`. Hence the complete sampled response is invertible on the centered subspace. Since the source mass is already known, the mesh-scale field determines the whole finite source.

This is intrinsic to the logarithmic-potential representation, not an imported smoothing model: for centered data the Poisson field is `-2r partial_r V_f`. Thus the first radial layer not covered by PC-309 does preserve all information, but it does so as a **universal circulant Fourier filter**.

The conditioning explains the transition. Fixed/sublinear low modes have gain `Theta(h/q)` and still collapse. Interior frequencies `h/q->x in (0,1)` have order-one gain, while the smallest nonzero gain is `Theta(1/q)`. Therefore the decoder condition number is `Theta(q)`, exactly the mesh-resolution cost predicted from transport stability.

The key distinction is between *information becoming invertible* and *new arithmetic structure appearing*. PC-310 crosses the first threshold without crossing the second: no independent spectral parameter, Gamma factor, functional-equation orientation or zero-sensitive sign is created by the inversion.

**Boundary.** This closes the linear single-level Poisson/radial-flux route. It does not close mixed-conductor coupling, nonlinear operations before cyclic diagonalization, shell-dependent/non-circulant interactions, or a separate theorem mapping the recovered source into a zero-sensitive destination.