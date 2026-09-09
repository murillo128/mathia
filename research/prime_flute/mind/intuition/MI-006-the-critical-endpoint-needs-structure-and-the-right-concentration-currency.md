# MI-006 — The critical endpoint has a Bessel-four smoothing window; the remaining gate is polar transport in the actual seam

**Evidence level:** exact Jacobi reduction, zero-edge branch, ground-state transform, sharp actual-chain fractional kernels, and finite/Galerkin noncommutative Robin factorization through PF-254

## Core intuition

The prime-flute endpoint is controlled by a specific inverse-square Jacobi edge, not by generic half-line perturbation theory. That local model is now substantially resolved. The actual positive zero mode generates a Bessel-four weighted chain, and its fractional powers have a sharp separated smoothing window that is stronger than the earlier free-chain calibration.

The remaining local obstruction is no longer the positive square-root edge itself. For a noncommuting Robin seam, normalization separates a universal favorable positive amplitude from a polar transport operator that can rotate high input into cheap modes. **Orientation transport, not scalar amplitude, is now the load-bearing variable.**

## Strongest justified principle

PF-247--PF-251 identify the parity Jacobi chains and the actual growing inverse-square zero-energy branch. PF-252 uses that exact positive branch as a ground-state transform: the resulting weighted path has mass and conductance of order `j^3` and diffusive limit equal to the radial four-dimensional Laplacian scaled by `1/4`.

PF-253 proves the corresponding actual-chain fractional kernel. In the separated cone,

`|<e_i,J^sigma e_j>| \asymp (i+1)^(3/2)(j+1)^(-5/2-2sigma)`,

and the weighted separated window is sharply `R<2+2sigma`. In particular, the square-root channel admits `R<3`, so the inverse-square critical edge does not destroy the supercritical margin needed by the route.

PF-254 gives the exact noncommutative algebraic split on finite/Galerkin regularizations. With relative seam `R=K^{-1/2}QK^{-1/2}`,

`(K+Q)^(-1)Q^(1/2) = K^(-1/2) h(R) U`,

where `h(lambda)=sqrt(lambda)/(1+lambda)` and `U` is the polar partial isometry of `K^{-1/2}Q^{1/2}`. The positive amplitude therefore always has a square-root edge; all unsmoothed input-orientation information is isolated in `U`.

## Program consequence

The next theorem should identify the actual complete-lift relative seam with enough precision to import the PF-253 Bessel-four functional calculus and then prove that its polar transport `U` is sufficiently local, banded, weighted-bounded, or otherwise controlled in the `K_a`/corridor spectral basis. Only that result can convert the positive square-root amplitude into the PF-243 separated Robin-Poisson estimate.

Afterward the established margin must still survive physical recoupling and global reassembly. A fixed-axis kernel theorem is not the final concentration theorem.

## Counterevidence / boundary

PF-253 is a fixed-axis fractional-power theorem, not a theorem for the complete normalized Robin source map. PF-254 is exact for bounded positive operators and finite/Galerkin regularizations; it deliberately does not claim the required full unbounded passage. A badly delocalized polar transport can still reproduce the PF-244 failure mode despite favorable singular values/output Gram geometry.

## Epistemic status

**Exact Bessel-four threshold model and sharp positive fractional smoothing are established; the noncommutative polar transport and physical/global reassembly remain open.**

## Falsification criterion

Refute the PF-252 ground-state/Bessel-four scaling, violate the PF-253 sharp separated window, or show that PF-254's polar factorization does not isolate the noncommuting input orientation. A valid continuation should prove source-specific control of the actual polar transport and carry the resulting margin into the final Robin/physical norm.