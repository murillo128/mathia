# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert exact square-lattice identification into complexity-adaptive quantitative coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`, `MI-013-adapted-cusp-coordinates-separate-depth-from-conditioning`.

XF-154--XF-178 separate source identification, common-scale stability, and the topology seen at the spectral edge. Exact Jacobi reciprocity can identify the Xi square lattice, but fixed-height transform norms and every fixed power-weighted real-axis Jacobi topology can be defeated by remote moment-balanced packets.

XF-179 shows that this obstruction is finite-complexity rather than information-theoretic: a surgery moving exactly `m` positive atom pairs is identified by the cusp jet through order `m`, and depth `m-1` is sharp. XF-180 then removes remote location from the local inverse after affine normalization, but monomial power-moment coordinates have an inverse norm growing at least exponentially with `m`.

XF-181 proves that this exponential local conditioning is **not intrinsic**. Orthogonalizing polynomials on the known reference packet and integrating that basis gives `m` adapted cusp observables using the same jet depth whose normalized location Jacobian is exactly orthogonal. For every fixed packet size, consecutive remote Xi packets therefore have a locally bi-Lipschitz inverse with constants independent of the remote index.

The live source-side target is now cleaner. Complexity remains in the **required adaptive jet depth**, the radius of the nonlinear inverse neighborhood, and the cost of extracting the packet-adapted cusp observables from positive heat-scale data when the relevant packet/support is not already known. Better local coordinates alone no longer explain the difficulty.

A useful theorem must either bound the effective surgery complexity from arithmetic/modular source structure, recover the needed adapted cusp data with an error budget compatible with the zero-sensitive region, or show that high-complexity balanced surgery is impossible for the actual source. Exact uniqueness, fixed-complexity observability, and coordinate conditioning are separate gates.

## Treat exact modular identification, adaptive depth, coordinate conditioning, and observable acquisition as separate gates

The square lattice is exactly rigid; finite packet surgeries are exactly identifiable at matched depth; monomial ill-conditioning can be preconditioned away locally. The unresolved issue is whether the source supplies the **right depth-adaptive observables cheaply and uniformly enough** for transition coercivity, not whether a mathematically invertible coordinate system exists.