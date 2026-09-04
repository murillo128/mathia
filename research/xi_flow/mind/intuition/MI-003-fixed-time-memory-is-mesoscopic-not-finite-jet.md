# MI-003 — Fixed-time Xi memory is mesoscopic; finite-range scale-invariant shape bulk has geometric-ramp null modes that source counting can only partially remove

**Evidence level:** supported through XF-034; finite-range null-mode and Xi nested-span statements are exact in their stated regimes

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. The normalized-discriminant route localizes taper loss well, but its finite-range scale-invariant bulk cannot control every shape direction: affine profiles in log gaps, equivalently geometric gap ramps, are exact null modes.

This null family is universal algebraically but not fully source-admissible. Xi zero counting on super-mesoscopic nested buffers forces any exact or uniformly near-geometric ramp persisting across that scale to flatten. The remaining theorem is therefore a stability/coercivity bridge: show that small bulk force makes a general source-valid profile close enough to the geometric null family for counting rigidity to apply.

## Strongest justified principle

XF-006--XF-031 establish the mesoscopic carrier, collision-safe normalized discriminants, positive overlap, exact nonlinear taper product rule, and the two-conductance bulk-alignment formulation.

XF-032 identifies the exact nonlinear kernel for the triple assembly. If the nearest-neighbor shape operator vanishes throughout a block, then `log g_j` is affine and `g_j=C r^j`; constant-weight bulk derivatives reduce to endpoint flux. The missing scalar is the mean logarithmic contrast, equivalently the endpoint gap ratio.

XF-033 proves that this is structural rather than triple-specific. Every finite-range translation-invariant sliding assembly of a scale-invariant local shape observable has zero interior first variation on a geometric ramp; its coefficient is a discrete derivative of the taper. Increasing the fixed block size cannot create bulk sensitivity to the affine log-gap slope.

XF-034 then brings in source rigidity. On a super-mesoscopic Xi block `M=R(T)log^2 T`, nested span laws at `M` and `2M` force an exact geometric ramp to satisfy `r_T^M=1+o(1)`, and the same holds under uniformly vanishing multiplicative perturbations. Thus persistent source-valid geometric null modes become asymptotically arithmetic. This does not control arbitrary profiles with the same spans.

## What remains possible

A positive theorem should establish a quantitative near-kernel statement: small aggregate shape force or adverse bulk production must imply closeness to a geometric ramp in a norm strong enough to combine with XF-034. Alternatively, add a genuinely nonlocal/source-sensitive observable that sees mean logarithmic contrast directly.

A negative should construct source-compatible profiles with small finite-range shape force that stay far from every geometric ramp while retaining order-one adverse bulk effect across the growing buffer.

## Status / novelty

Patch-test/affine null modes, graph Laplacians, and zero-counting asymptotics are classical ingredients. The synthesis is the sharpened frontier: **the universal finite-range bulk has an exact affine-log-gap blind mode, while Xi counting kills only sufficiently coherent realizations of that mode; quantitative stability toward the null family is now the missing bridge**.

## Falsification criterion

Construct a super-mesoscopic exact/near-geometric Xi block violating the XF-034 flattening conclusion, or prove a source-valid coercive near-kernel theorem that turns small shape force into geometric-ramp proximity and closes the remaining alignment gate.

## Lean-formalizable core

- Geometric-ramp null classification.
- Finite-range scale-invariant patch-test factorization.
- Nested-span ratio for geometric ramps.
- Source flattening `r_T^M=1+o(1)`.
