# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove a gauge-invariant source covariance without reconstructing Mertens

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`.

MC-188--MC-213 show that canonical equivariant, CRT, character, support-shift, and completion routes either remain sector-diagonal, collapse to sparse defects, or reconstruct a principal mode whose stable control is already Mertens/RH-hard. The surviving quantity is signed principal-centered interference at the source-selected residue.

MC-214 prices the obvious norm upgrade. Replacing centered variance by a fixed `2k` moment reduces the point-evaluation tax from order `d^2` to `d^(2/k)`, but for every fixed primorial scale parameter `c<1/3` a sufficiently high fixed moment together with diagonal-scale raw source control already forces the critical Mertens exponent. Higher invariant moments therefore approach the selected coordinate only by moving toward an RH-complete hypothesis; they do not create its sign.

MC-215 then removes an apparent phase resource. The explicit character factors `chi(-q)` at the prescribed residue are gauge: translating residue labels sends that residue to the identity and absorbs the phases into the Fourier coefficients while preserving every all-residue norm and magnitude spectrum. The invariant live datum is the **principal/transverse covariance at the distinguished coordinate**, or an equivalent relation retaining the integer lift `n+q=d^2 m`, interval ordering, or another source structure not erased by relabeling.

The next theorem should therefore control that gauge-invariant covariance directly and demonstrate why the estimate is cheaper than reconstructing the principal Mertens mode. All-residue higher moments, character magnitudes, and bare prescribed-residue phase multipliers are matched controls rather than new source information.

## Treat support defects, completion, moment order, and residue gauge as information-loss controls

Permutation symmetry can erase source order, support shifts can become small on rare holes, completion can reconstruct Mertens, higher centered moments can become RH-complete before yielding useful pointwise control, and the visible character phase of a selected residue can be gauged away. A viable nonlinear escape must retain an invariant signed relation that survives all five controls.