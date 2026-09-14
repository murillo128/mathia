# MI-016 — Gauge-invariant structure matters only when the source reaches it, it is source-specific, and the readout preserves the needed scale

**Evidence level:** exact within two distinct current representations: WP-297--[WP-301](../../weil_positivity/findings/WP-301-frustration-free-holonomy-zero-modes-are-universal-kernel-intersections.md) for multiplicative/operator source geometry, and VIS-214--[VIS-218](../../visual_exploration/findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md) for prime-phase quadratic optimization. No equivalence between the models, common arithmetic-curvature theorem or RH implication is claimed.

The first diagnostic is to quotient local gauge freedom. WP-297 shows flat multiplicative transport is pure gauge; WP-298 shows faithful pointwise positive metrics cannot alter exact support, while arbitrary moving kernels risk programming the answer.

WP-299 adds **reachability**. Genuine ambient output curvature is irrelevant to an exactly equivariant linear response from the ordinary commuting multiplicative source: the source-generated image lies in the common holonomy-fixed sector.

WP-300 adds **source specificity**. Moving curvature upstream into a fully prime-symmetric scalar projective source makes it reachable, but symmetry leaves only flat holonomy or the universal fermionic/Koszul sign. The latter is real curvature and yields a positive Boolean prime-power selector, yet generalized-prime free monoids reproduce it exactly.

WP-301 adds a fourth gate: **readout fidelity**. Replacing the scalar sign by arbitrary noncommuting matrix holonomies does not enrich a frustration-free zero-mode selector, because

`ker(sum_j c_j B_j^*B_j)=intersection_j ker B_j`.

Mixed-prime rejection is already decided by two-prime fixed spaces; higher matrix coherence and excited spectra vanish from the harmonic predicate. If a positive archimedean term belongs to the same sum, the zero-mode projector satisfies `P f(Q_infty)P=f(0)P`, so the nonzero spectrum that could carry Gamma information is erased. Rich geometry can therefore be source-reachable and non-scalar yet still become inert because the chosen observable keeps only a universal kernel.

Visual Exploration supplies the quantitative version of the same diagnostic without identifying the models. VIS-214--VIS-216 show that cycle holonomy is genuine and give packing/spectral relaxations. VIS-217 proves the normalized magnetic relaxation can reach Haar-RMS scale only if `N_eff=O(n)`. VIS-218 then computes the actual subcritical prime graph and finds

`N_eff/n >> y/(H log y) -> infinity`.

Hence the normalized magnetic certificate misses the required RMS scale by a diverging factor throughout `H log y/y ->0`, regardless of edge phases or magnetic ground states. The exact fixed-modulus torus problem can still behave differently because the relaxation has discarded a constraint the destination may need.

The reusable hierarchy is therefore: **quotient gauge -> verify source reachability -> verify source specificity -> audit what the readout discards -> price quantitative coercivity in the destination currency -> only then scalarize.** Unreachable curvature, universal fermionic curvature, non-scalar curvature collapsed to a common kernel, and genuine frustration weakened by a dimension-losing relaxation are distinct failure modes.

This sharpens the cross-line lesson without asserting a transfer theorem. Weil Positivity now needs moving-kernel, boundary/cohomological, or non-frustration-free finite--archimedean structure whose informative spectrum survives the final observable. Visual Exploration has closed normalized magnetic spectra as a standalone RMS route in the strictly subcritical regime and must use stronger cycle packing or the exact torus constraint there.

**Boundary.** WP-301 concerns positive frustration-free sums read through zero modes; VIS-218 concerns a finite Hermitian normalized-adjacency relaxation. The shared content is the diagnostic sequence: genuine gauge-invariant structure helps only if the source reaches it and the final readout retains the information and scale consumed by the target theorem.