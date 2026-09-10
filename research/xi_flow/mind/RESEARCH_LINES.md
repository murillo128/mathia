# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Force single-square-lattice support, then connect that rigidity to the heat transition

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`.

XF-154--XF-166 show that target-side enrichment, Xi-tail asymptotics, arbitrary finite local source jets, positive prekernels, and exact real-axis Jacobi reflection do not fix the de Bruijn--Newman heat origin. XF-167 closes the next obvious repair: complete monotonicity of the Jacobi-reflecting prekernel is still insufficient. A positive symmetric mixture of translated Xi sources has a completely monotone Laplace representation supported on several scaled square lattices, satisfies the same real-axis reciprocity, yet has a strictly positive de Bruijn--Newman threshold.

XF-168 identifies the exact coefficient-level boundary. If the inverse-Laplace support is fixed to the single Xi lattice `pi n^2`, absolute Dirichlet convergence plus the standard Jacobi reciprocity and constant term force all weights to equal one by Hamburger's converse theorem. Thus weight freedom on the exact square lattice is not a surviving escape; the XF-167 counterexample works by contaminating the support with scaled lattices.

The source-identification question is therefore sharply separated from the RH question. Single-lattice Jacobi rigidity can identify the Xi theta source, but identification alone does not prove that its distinguished heat slice is real-rooted. The live theorem must turn this exact coefficient/support rigidity into a quantitative restriction on the mesoscopic source mass or collision geometry that controls the transition, rather than merely recover Xi uniquely.

## Treat complete monotonicity and source identification as separate gates

Positive Laplace structure plus real-axis modular reflection still permits wrong heat origins when scaled square lattices are allowed. Conversely, fixing the exact square-lattice support makes the coefficients Hamburger-rigid. Future work should not search for more local/tail descriptors between those two levels; it should either derive the single-lattice law from a cheaper intrinsic condition or propagate that already-identified source law into transition coercivity.
