---
type: adversarial-review
target: research/nyman_beurling/findings/NB-003-finite-semigroup-target-probes-have-no-quantitative-gap.md
---

# Adversarial review

## Adversary

The exact two-scale uniqueness claim for the compressed operators `A_m^*` is not established by Section 1. The proof shows that the full-space adjoints satisfy

`ker(T_2^*-2^{-1/2}I) ∩ ker(T_3^*-3^{-1/2}I) = C e`,

then transfers this to `A_m=T_m|_M` solely from invariance of `M` under `T_m`. But invariance gives

`A_m^* = P_M T_m^*|_M`,

not `A_m^*=T_m^*|_M` unless `M` is reducing for `T_m`. In general a compression of an adjoint can acquire eigenvectors that are not eigenvectors of the full adjoint, so full-space uniqueness does not imply uniqueness of the compressed joint eigenspace. For Bagchi's harmonic-interval space, `T_m^*h(y)=m^{-1/2}h(y/m)` does not obviously preserve piecewise constancy on the original harmonic intervals, so the missing reducing property cannot be assumed.

The projected-Mellin calculation in Sections 2--4 still appears to prove the quantitative aliasing obstruction around the target line itself: it constructs unit vectors asymptotically orthogonal to `e` with all fixed-scale defects tending to zero. What is currently unsupported is the stronger `EXACT-DERIVED` statement that `C e` is the complete exact joint eigenspace of `A_2^*,A_3^*`, and the repeated framing that the target is algebraically unique before the spectral-gap failure. To resolve the objection, either prove the compressed joint-eigenspace identity directly (for example from the explicit action on harmonic-interval coordinates), or weaken/remove that exact-uniqueness claim while retaining the independently valid approximate-aliasing result.
