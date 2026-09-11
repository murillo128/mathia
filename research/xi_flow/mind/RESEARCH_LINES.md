# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert exact square-lattice identification into complexity-adaptive quantitative coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`, `MI-013-adapted-cusp-coordinates-separate-depth-from-conditioning`.

XF-154--XF-178 separate source identification, common-scale stability, and the topology seen at the spectral edge. Exact Jacobi reciprocity can identify the Xi square lattice, but fixed-height transform norms and every fixed power-weighted real-axis Jacobi topology can be defeated by remote moment-balanced packets.

XF-179 shows that this obstruction is finite-complexity rather than information-theoretic: a surgery moving exactly `m` positive atom pairs is identified by the cusp jet through order `m`, and depth `m-1` is sharp. XF-180 then removes remote location from the local inverse after affine normalization, while XF-181 removes the remaining monomial Vandermonde penalty by passing to packet-adapted orthogonal cusp coordinates. Once exact cusp data are supplied, the normalized local location inverse can be condition-one for every fixed packet size, uniformly in the remote index.

XF-182 identifies the cost hidden in the phrase **once exact cusp data are supplied**. For a fixed `m`-atom consecutive Xi packet, the orthogonal adapted modes have raw positive-heat visibility `Theta_m(N^-1),Theta_m(N^-2),...,Theta_m(N^-m)`. The hardest mode is exactly the linearized `N^-m` moment-cancellation scale behind XF-178. Sampling at `m` scales `x~N^-2` attains this hierarchy with acquisition inverse norm `Theta_m(N^m)` and matrix condition number `Theta_m(N^(m-1))`. The remote index is therefore absent from the algebraic cusp inverse but reappears, sharply and in graded form, in the forward acquisition map.

The live source-side target is now narrower. A useful theorem must either construct a **relative or multiscale acquisition observable** that compensates the known Gaussian/packet visibility factors without merely demanding `N^-m` absolute precision, or prove from arithmetic/modular source structure that the effective remote packet complexity is bounded or otherwise restricted. Further preconditioning of the exact finite-dimensional cusp inverse no longer addresses the active loss.

## Treat exact identification, adaptive depth, inverse coordinates, and positive-heat acquisition as separate gates

The square lattice is exactly rigid; finite packet surgeries are identifiable at sharp matched depth; and the exact cusp inverse can be locally isometric. Raw positive-heat data nevertheless resolve the `k`th adapted complexity mode only at order `N^(-(k+1))`. The unresolved transition problem is therefore whether the actual Xi source supplies a renormalized acquisition law strong enough to cross that graded visibility barrier before zero-sensitive estimates amplify the remaining error.