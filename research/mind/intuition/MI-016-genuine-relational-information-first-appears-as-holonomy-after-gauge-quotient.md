# MI-016 — Gauge-invariant structure matters only when the source reaches it, it is source-specific, and its coercivity has the right scale

**Evidence level:** exact within two distinct current representations: WP-297--[WP-300](../../weil_positivity/findings/WP-300-prime-symmetric-projective-source-curvature-is-fermionic-and-boolean.md) for multiplicative/projective source geometry, and VIS-214--[VIS-217](../../visual_exploration/findings/VIS-217-normalized-spectral-certificate-dimension-floor.md) for prime-phase quadratic optimization. No equivalence between the models, common arithmetic-curvature theorem or RH implication is claimed.

The first diagnostic is to quotient local gauge freedom. WP-297 shows flat multiplicative transport is pure gauge; WP-298 shows faithful pointwise positive metrics cannot alter exact support, while arbitrary moving kernels risk programming the answer.

WP-299 adds **reachability**. Genuine ambient output curvature is irrelevant to an exactly equivariant linear response from the ordinary commuting multiplicative source: the source-generated image lies in the common holonomy-fixed sector.

WP-300 adds a third gate, **source specificity**. Moving curvature upstream into a fully prime-symmetric scalar projective source does make it reachable, but symmetry leaves only flat holonomy or the universal fermionic/Koszul sign. The latter is real curvature and even yields a positive Boolean prime-power selector, yet generalized-prime free monoids reproduce it exactly and it does not couple naturally to the archimedean completion or repair the global Weil sign. Reachable curvature can therefore still be mathematically inert if it is only universal grading structure.

Visual Exploration supplies the quantitative gate. VIS-214--VIS-216 show that cycle holonomy is a genuine obstruction and give packing/spectral relaxations. VIS-217 proves that the normalized magnetic relaxation itself obeys

`U_spec/sqrt(R(A)) >= sqrt(2 N_eff/(n-1))`

on a connected component. Thus it can reach Haar-RMS scale only if `N_eff=O(n)`. If effective edge mass is superlinear in vertex count, no phase arrangement can make that relaxation strong enough; one must use a stronger certificate or the exact torus constraint.

The reusable hierarchy is therefore: **quotient gauge -> verify source reachability -> verify source specificity -> price quantitative coercivity -> only then scalarize.** A loop invariant in an unused sector, a universal fermionic invariant reproduced by controls, and a genuine invariant whose relaxation has the wrong dimension scaling are three distinct ways for real geometry to miss the target conclusion.

This sharpens the cross-line lesson without identifying the models. Weil Positivity now needs arithmetic non-scalar/projective/cohomological structure or nonseparable finite--archimedean geometry beyond the universal scalar sign. Visual Exploration must first price `N_eff/n`; if that ratio diverges, normalized magnetic spectra are closed as a standalone RMS route even though the exact torus problem remains open.

**Boundary.** WP-300 concerns scalar projective commutator laws under full prime-relabeling symmetry; VIS-217 concerns a finite Hermitian normalized-adjacency relaxation. The shared content is the diagnostic sequence, not a transfer theorem between the mathematical objects.
