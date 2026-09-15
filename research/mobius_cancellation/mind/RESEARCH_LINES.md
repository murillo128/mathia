# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Convert forced source-incidence cost into arithmetic endpoint coercivity beyond the diagonal projective rank-profile frontier

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-038-systematic-dualization-does-not-add-a-second-coercive-endpoint-it-transposes-the-same-rank-profile`.

MC-307--MC-312 turn endpoint projection and source cuts into a hereditary generalized-Hamming support law. MC-313 identifies the coarse coding boundary: ordinary full-length rate-one-half binary codes can realize the required hierarchy to `O(R/log R)` precision, so generic linear-code geometry is not yet arithmetic coercivity.

MC-314 makes the missing precision exact. At `t_R=ceil(2 log_2(R+1))`, if the largest source prime obeys

`log Z <= ((1+eta_R)/R) log y`,

then the arithmetic source-cut inequality forces

`R-d_(t_R) <= R eta_R/(1+eta_R) + 2 + o(1)`.

At the natural equal-share scale `eta_R=0`, this becomes the constant-defect demand `d_(t_R)>=R-2+o(1)`.

MC-315 identifies the exact generic combinatorial question behind that endpoint. For a full `[2R,R]` binary code, regard the generator columns as a spanning multiset of `2R` points in `PG(R-1,2)`. Then

`2R-d_t(C)=max_(codim U=t) M(U)`.

At `t=t_R`, the desired constant-defect profile is therefore equivalent to asking whether a spanning `2R`-point multiset can place at most `R+2` points in every codimension-`t_R` projective subspace. If `N_R` denotes the corresponding diagonal generalized-cap envelope, the generic source control exists exactly when `N_R>=2R` eventually; proving `N_R<2R` would kill it. Standard incidence, Singleton and Griesmer estimates are too weak in this diagonal regime.

MC-316 shows that passing to a systematic generator `G=[I|P]` does not create a second independent endpoint. The generalized-weight hierarchy is exactly a uniform rectangular submatrix-rank condition on `P`; the dual code has generator `[P^T|I]`, and Wei duality reflects the same condition through transposition. Primal weights, dual weights, systematic submatrix rank and the mirrored erasure-capacity formulation are therefore equivalent presentations of one generic frontier.

The live theorem has consequently narrowed again. On the arithmetic side, prove a source scale sharp enough to enter the constant-defect regime or a Legendre/source-incidence restriction on the realized matrices `P_R` that arbitrary binary matrices need not satisfy. On the matched-control side, settle existence of binary `R x R` matrices with the required **full submatrix rank profile**. A second Griesmer/Wei-dual calculation cannot supply extra coercivity because MC-316 proves it is the same constraint in reflected coordinates.

## Settle the systematic matrix existence problem rather than adding equivalent coding descriptions

**Linked intuition:** `MI-038-systematic-dualization-does-not-add-a-second-coercive-endpoint-it-transposes-the-same-rank-profile`.

At the live logarithmic rank `t_R`, the generic endpoint can now be stated without coding-language ambiguity: construct or rule out systematic matrices whose every required `(g+a+1) x g` submatrix has rank at least `g-t+1` across the full parameter range. A construction would show that the constant-defect demand is still generically realizable; an impossibility theorem would make the obstruction finite-geometric before arithmetic specialization.

Useful progress must strengthen this matrix existence question or prove that the arithmetic matrices occupy a stricter subclass. Rephrasing it through the dual hierarchy, Wei partition, erasure patterns, or a second standard coding bound is not new leverage unless the reformulation adds a constraint not implied by the same submatrix ranks.

## Keep target projection, source scale, generalized-weight defect and projective realizability distinct

A large number of expensive endpoint directions is not the same as expensive common support. The source package is priced simultaneously by its coordinate count, largest-prime scale and hereditary support profile. MC-314 shows that a first-order statement `log Z=(1+o(1))log y/R` is too coarse unless the error is quantified on the `1/log R` scale; MC-315--MC-316 then show that the resulting support endpoint is exactly a projective/systematic rank problem, not merely another coding-rate inequality.

Any closing argument must state which source quotient is used, what representative package is fixed, how source supports overlap, what `eta_R` is actually proved, and whether the resulting systematic matrix lies outside the exact rank-profile envelope available to arbitrary binary codes.

## Preserve matched controls through the second-order boundary

MC-313 remains the coarse matched control, while MC-315 identifies the exact constant-defect generic frontier and MC-316 removes duality as a possible source of extra generic pressure. Future work should settle that frontier rather than infer generic impossibility from the gap between `O(R/log R)` and `O(1)` or count primal and dual constraints twice. If the required systematic matrices exist, generic projective geometry survives the sharper demand and arithmetic structure must be sought elsewhere; if they do not, the source-cut endpoint acquires a genuine non-generic combinatorial obstruction. Either outcome materially sharpens what arithmetic information is still missing.