# MI-015 — Count-matched one-profile spectra are classically reproducible throughout every sub-square-root bandwidth

**Evidence level:** unconditional classicalization from PC-282--PC-285 and conditional RH sharpening through [PC-290](../../findings/PC-290-count-matched-l2-transport-reaches-square-root-boundary.md). The count-matched control is deliberately given the scalar source cardinality `M_q`; no converse RH criterion or theorem at `B~sqrt(q)` is claimed.

After selector subtraction, the complete-domain remainder is a classical logarithmic/digamma Green symbol. Prime dependence in this branch survives only through source placement inside the finite section. PC-285 reproduces that placement with a matched Li-grid control through the unconditional Vinogradov--Korobov range.

PC-287--PC-289 progressively remove artificial transport losses under RH: one-dimensional path variation replaces global Lipschitz control, and source-aware short-interval charging removes the clipping atom loss. The remaining `log^2 q` factor in PC-289 came from the pointwise normalized prime-to-Li source discrepancy.

PC-290 shows that this factor is exactly the cost of spreading the scalar endpoint count mismatch through the normalized CDF. Give the control only the total prime-source count `M_q` in addition to the Li profile, and localize the correction near `q`. The RH mean-square PNT estimate then gives

`||F_prime-F_control||_2 = O(q^-1/2)`

up to lower-order terms. This norm matches the existing spectral path derivative estimate

`||F_y'||_2 << B/sqrt(epsilon)`.

With `epsilon=B q^-1/2`, the normalized boundary-log singular-spectrum laws collapse for every

`B=o(sqrt(q))`.

The reusable lesson is now three-layered. Integrated output-path variation is cheaper than global Lipschitz control; source-aware mass inside the singular set is cheaper than worst-atom charging; and **a pointwise source discrepancy can still be the wrong transport norm once the destination already supplies an `L^2` path-energy estimate**. Matching the scalar endpoint mass exposes the actual positional discrepancy seen by that duality.

The interpretation is correspondingly stronger. Under RH, below the rational square-root resolution boundary, the exact prime locations do not create order-one separation in this one-profile observable once total source count is fixed. If the desired RH signature is persistent prime-specific separation, the architecture must retain richer information or operate at the true denominator-microscopic boundary rather than another sub-square-root refinement of the same statistic.

**Boundary.** The count-matched control is not arithmetic-free: it receives `M_q`. PC-290 therefore falsifies positional information conditional on total count; it does not show that the source count itself is irrelevant. No claim is made at `B` comparable with `sqrt(q)`.
