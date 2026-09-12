# MI-013 — Xi packet complexity costs samples, not local nonlinear conditioning, in the holomorphic category

**Evidence level:** proved growing-packet nonlinear local acquisition through XF-186; global unknown-support source coercivity remains open.

Adapted coordinates remove remote inverse conditioning, and mesoscopic complex Jacobi phase removes the positive-real acquisition loss. XF-185 shows that this survives growing packet complexity: a known consecutive packet of `m<=N` remote atoms is observed by an explicit `O(m)` Fejer-overcomplete complex bank whose linearized singular values are comparable to `sqrt(m)` uniformly in both `N` and `m`.

XF-186 closes the corresponding local nonlinear gap. On the cube

\[
\|h\|_\infty\le\frac{\kappa_\alpha}{m},
\]

the same normalized Jacobi packet map is uniformly bi-Lipschitz, with constants independent of `N` and `m`. In physical lattice coordinates this cube contains displacements of a fixed size independent of both parameters. The reciprocal Jacobi image stays exponentially small across the moving frame, so the lower bound is not merely an infinitesimal statement.

Consequently, once the ambient consecutive packet window is known, the inverse can recover zero and nonzero atom displacements together on a constant physical neighborhood. Growing lattice-scale complexity costs sample count, but it does not reintroduce a remote or local nonlinear condition-number penalty.

The remaining source problem is global: locate and recenter unknown windows, assemble multiple or multiscale packets, treat regimes outside `m<=N`, handle unknown weights only if the Xi source permits them, and justify the required complex samples from the physical Jacobi/Xi object. Even successful source reconstruction must then be transported to a zero-sensitive observable or de Bruijn--Newman constraint; reconstructing theta-side deformation alone is not an RH-facing theorem.

**Boundary.** XF-186 is local to a known consecutive ambient window and a fixed physical displacement radius. It does not solve global support search, multiple-packet interference, arbitrary weights, source-side sample accessibility, or the final Xi-zero bridge.
