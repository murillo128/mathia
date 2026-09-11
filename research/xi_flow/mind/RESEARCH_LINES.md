# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert holomorphic packet acquisition into global source coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`, `MI-013-adapted-cusp-coordinates-separate-depth-from-conditioning`.

XF-154--XF-182 separate exact source identification, adaptive packet depth, inverse conditioning, and positive-real heat acquisition. Fixed-complexity real-axis topologies can be defeated by remote moment-balanced packets; an `m`-atom surgery needs depth `m`; and packet-adapted cusp coordinates make the exact local inverse well conditioned while raw positive heat sees the `k`th mode only at `N^(-(k+1))`.

XF-183 shows that this ladder is not intrinsic to the finite packet geometry. Dividing by the reference packet heat mass at resolving real scale removes the remote power loss and yields a uniformly conditioned relative inverse—but the denominator is `exp(-Theta(N))`, so extracting that relative observable from additive absolute heat estimates requires exponentially small error.

XF-184 then shows that even this exponential tradeoff is specific to **positive-real acquisition**. In the holomorphic right half-plane one may take `Re x~N^-2` to keep the remote Gaussian carrier at constant modulus and `Im x~N^-1` to resolve the packet. A fixed bank of complex Jacobi samples then has absolute linearized singular values bounded above and below uniformly in `N`; after bounded row normalization it converges to a discrete Fourier transform, while the reciprocal image is exponentially negligible.

The local finite-packet acquisition barrier is therefore crossed once complex Jacobi phase is allowed. The live theorem is now global/source-side: show that the actual Xi/Jacobi object supplies these mesoscopic complex samples with the analytic control needed for a **nonlinear, support-unknown, complexity-adaptive coercivity theorem**, or identify a new obstruction when packet complexity grows.

## Treat positive-real acquisition and holomorphic acquisition as different information models

The `N^-m` ladder and the XF-183 exponential normalization cost are sharp for positive-real data but are not information-theoretic barriers for the holomorphic Jacobi source. Future no-go statements must specify the allowed complex sampling geometry; future positive results must propagate the uniformly conditioned local complex acquisition into a global source theorem rather than further precondition the already-solved finite packet inverse.