# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Upgrade the four-adic projective gap to a pointwise or cofinal linear-prefix gap

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-024--FD-030 show that squarefree ternary data and every unbounded sublinear prime-ancestry prefix can coexist with square-root GCD-duality saturation. FD-031 identifies the first genuinely different regime: at linear ancestry breadth, saturation is equivalent to projective alignment of the physical Mertens tail with one Schur-complement equality direction.

FD-032 finds an unconditional absolute obstruction: the equality ray vanishes on nonsquarefree coordinates while the physical tail is forced nonzero on a macroscopic terminal block, giving squared Schur distance `Omega(H)`. FD-033 shows why that alone does not yield a uniform angle gap. Critical-line zeros force the physical Schur-tail energy itself to be superlinear, so the absolute transverse defect may be diluted projectively; the tempting route `E=O(H)` is impossible.

FD-034 then recovers a genuine normalized obstruction from the square-divisor Jordan modes. The projective residual at horizon `H` controls a scaled copy of the physical energy at `floor(H/4)`, and iteration forces a positive geometric/Cesaro lower bound for the normalized defect along every complete `4`-adic chain. In particular, half-linear ancestry has a strict average saturation gap even when a different admissible source is chosen at every horizon.

The live theorem is now to upgrade this multiscale average rigidity. Prove a pointwise/cofinal lower bound on the normalized Schur defect, extend the square-divisor renormalization to enough multiplicative scales to prevent sparse escape, or combine it with endpoint reachability so that a saturating subsequence cannot hide between the forced `4`-adic defects.

## Treat absolute tail distance and superlinear energy as separate controls

Linear-scale support mismatch is real, but absolute distance alone is not coercive because the physical Mertens energy is unconditionally superlinear. The useful invariant is normalized/projective defect. Conversely, FD-034 shows that this projective escape cannot persist densely along a full multiplicative chain. Future arguments should preserve that normalization rather than return to raw tail norms or sublinear ancestry counts.
