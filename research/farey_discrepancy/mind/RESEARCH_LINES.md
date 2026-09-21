# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the divisibility-poset geometry of growing exact omissions

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`.

FD-241--FD-245 separate qualitative density-one sampling, approximate residual cost, the sharp arbitrary-sparse reciprocal-divisor envelope and the exact triangular omission columns. FD-246 then shows that exact support reach is controlled by harmonic location: high-scale `K=o(N)` omissions cost only `O(K/N)` after normalization.

FD-247 shows that low absolute scale is still not enough to make exact omissions dangerous. If the active increments `g=Delta Y` form a divisibility antichain, then divisor inversion is diagonal on their support and coefficient mass is at most `CN|supp(g)|<=2CNK`. Every omission set contained in one multiplicative octave has this property, at any absolute scale, and the `K/N` normalized cost is sharp.

The live response-side question is therefore the **incidence-conditioned inverse norm of the divisibility poset on `supp(Delta Y)`**. How much amplification can genuine cross-scale divisibility chains or dense divisibility incidence create, and what structural statistic interpolates between primitive support and the worst relaxed sparse envelope? The independent source-side question remains whether positivity, finite reservoir capacity or arithmetic coherence excludes the surviving signed directions. Approximate residual control remains separate.

## Separate boundary/source admissibility from interior integrality

Response-space rounding makes bulk integrality cheap once a real reservoir profile is safely inside its capacity box. The remaining discrete obstruction is source admissibility and exact defect geometry.

The current exact hierarchy is now sharper than a cardinality or location ledger: arbitrary sparse defects pay reciprocal-divisor mass; bounded omissions have triangular column structure; absolute locations bound reachable support; and primitive active increments eliminate the location penalty entirely. A future coercivity theorem should preserve the full divisibility incidence image before relaxing it to any sparse-set norm.