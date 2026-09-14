# MI-016 — Gauge-invariant structure matters only when the source reaches it and its coercivity has the right scale

**Evidence level:** exact within two distinct current representations: WP-297--[WP-299](../../weil_positivity/findings/WP-299-source-equivariant-linear-response-lives-in-the-holonomy-fixed-sector.md) for multiplicative boundary transport, and VIS-214--[VIS-216](../../visual_exploration/findings/VIS-216-normalized-magnetic-gap-certificate.md) for prime-phase quadratic optimization. No equivalence between the models, common arithmetic-curvature theorem or RH implication is claimed.

The first diagnostic remains to quotient local gauge freedom. WP-297 shows that flat multiplicative transport is pure gauge; WP-298 shows that faithful pointwise positive metrics cannot alter exact support, while arbitrary moving kernels risk programming the answer.

WP-299 adds a second gate: **reachability**. Even genuine ambient curvature is irrelevant to an exactly equivariant linear response from the ordinary commuting multiplicative source. The source shifts commute, so the output shifts commute on `im T`; every source-generated vector lies in the common fixed sector of the prime-diamond holonomies. A curved ambient complement can coexist with exact Mangoldt recovery while contributing nothing to it.

Visual Exploration supplies the quantitative analogue. Cycle holonomy is a real gauge-invariant obstruction to exact envelope synchronization, and VIS-215 can accumulate it by fractional packing. But VIS-216 shows that merely nonzero frustration is not enough for the desired pointwise scale. If `N_eff` is the effective edge count, the normalized magnetic certificate reaches Haar-RMS scale only when

`1-min(bar_lambda_+,bar_lambda_-) = O(N_eff^(-1/2))`.

A constant positive magnetic gap gives only a constant-fraction envelope improvement. The invariant must be quantitatively strong enough at the destination scale.

The reusable hierarchy is therefore: **quotient gauge -> verify source reachability -> price quantitative coercivity -> only then scalarize.** A loop invariant living in an unused sector is as ineffective as a target-blind near-kernel; a genuine invariant with insufficient scale is as ineffective as a qualitative nonzero defect. Conversely, pointwise degeneracy is meaningful only when its kernel is source-forced rather than selected.

This sharpens the cross-line lesson without identifying the models. In Weil Positivity the open problem is to make mixed-prime curvature part of the source-generated representation itself. In Visual Exploration the open problem is to prove that the actual prime coefficient graph carries nearly maximal frustration, or that the exact torus constraint beats the available relaxations.

**Boundary.** WP-299 concerns exact linear equivariance of a commuting source; VIS-216 concerns a finite Hermitian gain graph and a spectral relaxation of fixed-modulus torus optimization. The shared content is the diagnostic sequence, not a transfer theorem.
