# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Convert forced source-incidence cost into arithmetic endpoint coercivity beyond generic code geometry

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-037-source-incidence-cost-is-a-redundancy-scale-tradeoff`.

MC-307--MC-312 turn endpoint projection and source cuts into a hereditary generalized-Hamming support law. MC-313 identifies the coarse coding boundary: ordinary full-length rate-one-half binary codes can realize the required hierarchy to `O(R/log R)` precision, so generic linear-code geometry is not yet arithmetic coercivity.

MC-314 makes the missing precision exact. At `t_R=ceil(2 log_2(R+1))`, if the largest source prime obeys

`log Z <= ((1+eta_R)/R) log y`,

then the arithmetic source-cut inequality forces

`R-d_(t_R) <= R eta_R/(1+eta_R) + 2 + o(1)`.

At the natural equal-share scale `eta_R=0`, this becomes `d_(t_R)>=R-2+o(1)`, so a length-`2R` package must tolerate an erasure fraction approaching one half with only a constant second-order defect. By contrast, MC-313's proved generic matched control supplies only `R-d_t=O(R/log R)` at this rank.

The live theorem is therefore genuinely second-order. One route is a source-scale estimate with `eta_R=o(1/log R)`, which forces an arithmetic generalized-weight defect smaller than the currently proved generic guarantee. Another is a direct arithmetic-realizability obstruction on the Legendre-incidence columns or a joint hierarchy law. The conclusion is **not** that no generic code can meet the sharper profile; MC-314 only moves the arithmetic demand beyond what the existing generic construction proves.

## Keep target projection, source scale, generalized-weight defect and generic realizability distinct

A large number of expensive endpoint directions is not the same as expensive common support. The source package is priced simultaneously by its coordinate count, largest-prime scale and hereditary support profile. MC-314 shows that a first-order statement `log Z=(1+o(1))log y/R` is too coarse unless the error term is quantified on the `1/log R` scale: the small multiplicative slack becomes an additive generalized-weight defect of order `R eta_R`.

Any closing argument must state which source quotient is used, what representative package is fixed, how source supports overlap, what `eta_R` is actually proved, and what arithmetic feature prevents a generic binary code from realizing the same profile.

## Preserve matched controls through the second-order boundary

MC-313 remains the relevant matched control for coarse hereditary support. MC-314 does not refute it; it identifies the precision at which the arithmetic source requirement begins to outrun that **proved** control. Future work should either construct a generic control matching the `O(1)` defect, which would push the obstruction farther, or prove that realizable arithmetic incidence cannot attain it. Replacing Singleton by another one-weight coding inequality without new arithmetic input is no longer the live issue.