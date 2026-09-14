# MI-017 — Finite high-zero target access requires a target-bearing compression near-kernel

**Evidence level:** exact finite-section reduction from [NB-115](../../findings/NB-115-order-one-finite-high-zero-target-access-must-live-in-vanishing-cell-compression-modes.md), combined there with the Burnol target-mass bound of NB-114 and the current zeta zero-count input. This does not prove a lower bound on the cell-compression spectrum or a Nyman distance estimate.

Let `K_F` be a finite Burnol packet and `Q_R` the canonical orthogonal projection onto the first integer cells. In orthonormal coordinates on `K_F`, define

`H_(F,R)=A^* Q_R A`,

so its eigenvalues `lambda_j` are exactly the fractions of continuum packet energy retained by the finite arithmetic window. If `b_(F,R)=A^* e_R` are the finite target coordinates, then the target projection onto the compressed packet is not heuristic but exactly

`||P_(Q_R K_F)e_R||^2 = b_(F,R)^* H_(F,R)^+ b_(F,R)`.

The numerator remains controlled by continuum target mass:

`||b_(F,R)|| <= sqrt(tau(F)) + R^(-1/2)`.

Therefore a fixed positive finite target fraction cannot arise perturbatively from a target-poor continuum packet. NB-115 proves that at least half of that target projection must be carried by eigenmodes with

`lambda_j = O(tau(F)+1/R)`.

For `d` zeros above height `G`, `tau(F)<=d/G^2`, so the required retained-energy scale is `O(d/G^2+1/R)`. For the actual right-half zeta zeros in a fixed-ratio shell, `d=O_A(G log G)`, hence any order-one finite target access must load modes with

`lambda_j = O_A(log G/G + 1/R)`.

This separates **bad compression** from **target-bearing bad compression**. An irrelevant near-kernel of `H_(F,R)` does not rescue the Nyman target; the target coordinates themselves must concentrate spectrally in the vanishing-retention sector. Likewise large zero-state shear or a poorly conditioned raw Gram does not establish the required effect.

The live arithmetic question is now a spectral localization problem for the actual integer-cell map: can source structure rule out target weight on the low-retention modes, even if such modes exist? Any proposed finite high-zero rescue must exhibit the opposite mechanism explicitly.

**Boundary.** Abstract Hilbert geometry allows perfect target amplification by a projection whose sole retention eigenvalue equals the tiny continuum target mass, so no universal functional-analytic argument can remove this escape. The missing input must use the arithmetic cell structure and the actual zeta packet.
