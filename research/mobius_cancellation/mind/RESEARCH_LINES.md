# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Convert forced source-incidence cost into arithmetic endpoint coercivity beyond the diagonal projective cap frontier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-037-source-incidence-cost-is-a-redundancy-scale-tradeoff`.

MC-307--MC-312 turn endpoint projection and source cuts into a hereditary generalized-Hamming support law. MC-313 identifies the coarse coding boundary: ordinary full-length rate-one-half binary codes can realize the required hierarchy to `O(R/log R)` precision, so generic linear-code geometry is not yet arithmetic coercivity.

MC-314 makes the missing precision exact. At `t_R=ceil(2 log_2(R+1))`, if the largest source prime obeys

`log Z <= ((1+eta_R)/R) log y`,

then the arithmetic source-cut inequality forces

`R-d_(t_R) <= R eta_R/(1+eta_R) + 2 + o(1)`.

At the natural equal-share scale `eta_R=0`, this becomes the constant-defect demand `d_(t_R)>=R-2+o(1)`.

MC-315 identifies the exact generic combinatorial question behind that endpoint. For a full `[2R,R]` binary code, regard the generator columns as a spanning multiset of `2R` points in `PG(R-1,2)`. Then

`2R-d_t(C)=max_(codim U=t) M(U)`.

At `t=t_R`, the desired constant-defect profile is therefore equivalent to asking whether a spanning `2R`-point multiset can place at most `R+2` points in every codimension-`t_R` projective subspace. If `N_R` denotes the corresponding diagonal generalized-cap envelope, the generic source control exists exactly when `N_R>=2R` eventually; proving `N_R<2R` would kill it. Standard incidence, Singleton and Griesmer estimates are too weak in this diagonal regime.

The live theorem has consequently split cleanly. On the arithmetic side, prove a source scale sharp enough to enter the constant-defect regime or a Legendre-incidence constraint stronger than generic projective geometry. On the matched-control side, settle the diagonal finite-geometry envelope `N_R`. Until that generic frontier is known, the constant-defect arithmetic demand is not itself an arithmetic discriminator.

## Keep target projection, source scale, generalized-weight defect and projective realizability distinct

A large number of expensive endpoint directions is not the same as expensive common support. The source package is priced simultaneously by its coordinate count, largest-prime scale and hereditary support profile. MC-314 shows that a first-order statement `log Z=(1+o(1))log y/R` is too coarse unless the error is quantified on the `1/log R` scale; MC-315 then shows that the resulting support endpoint is exactly a projective incidence problem, not merely another coding-rate inequality.

Any closing argument must state which source quotient is used, what representative package is fixed, how source supports overlap, what `eta_R` is actually proved, and whether the resulting projective multiset lies outside the diagonal generalized-cap envelope available to arbitrary binary codes.

## Preserve matched controls through the second-order boundary

MC-313 remains the coarse matched control, while MC-315 is the exact constant-defect generic frontier that MC-314 exposes. Future work should settle that frontier rather than infer generic impossibility from the gap between `O(R/log R)` and `O(1)`. If `N_R>=2R`, generic projective geometry survives the sharper demand and arithmetic structure must be sought elsewhere; if `N_R<2R`, the source-cut endpoint acquires a genuine non-generic combinatorial obstruction. Either outcome materially sharpens what arithmetic information is still missing.