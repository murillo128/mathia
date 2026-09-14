# MI-017 — Finite high-zero target access requires target weight at inverse-height compression retention

**Evidence level:** exact finite-section reduction from [NB-115](../../findings/NB-115-order-one-finite-high-zero-target-access-must-live-in-vanishing-cell-compression-modes.md), sharpened by [NB-116](../../findings/NB-116-selberg-density-upgrades-the-high-zero-burnol-tail-to-inverse-height.md) using classical Selberg zero density. This does not prove a lower bound on the cell-compression spectrum or a Nyman distance estimate.

Let `K_F` be a finite Burnol packet and `Q_R` the canonical orthogonal projection onto the first integer cells. In orthonormal packet coordinates, `H_(F,R)=A^*Q_RA` records retained continuum energy, while the finite target projection is exactly

`b_(F,R)^* H_(F,R)^+ b_(F,R)`.

NB-115 proves that if a target-poor continuum packet nevertheless captures a fixed positive fraction of the finite Nyman target, at least half of that finite target projection must lie in eigenmodes with

`lambda = O(tau(F)+1/R)`.

NB-116 identifies the correct source scale for actual high zeta zeros. The Burnol defect weights a zero by its horizontal displacement, and Selberg density controls the first horizontal moment:

`sum_(0<gamma<=T, beta>1/2) (beta-1/2) = O(T)`.

Consequently the **entire** actual right-half Blaschke tail above height `G` has `tau=O(1/G)`, uniformly over packet cardinality, multiplicity and ordinate spread. Therefore any order-one finite target access from any finite packet above `G` must load compression modes with

`lambda = O(1/G+1/R)`.

For `R/G -> infinity`, the live threshold is inverse height. The earlier `log G/G` scale was an artifact of charging every high zero equally through raw zero counting. Adding wider packets or more zero rank cannot recover that logarithm because their total target mass is already bounded by the horizontal first moment.

The remaining escape is sharply target-specific: the actual integer-cell compression would need to place substantial target spectral weight on modes retaining only `O(1/G)` of their packet energy. Small Gram eigenvalues, severe internal shear or large high-zero rank are irrelevant unless the target occupies precisely those near-kernel directions.

**Boundary.** Abstract Hilbert geometry permits such target-bearing near-kernels. Ruling them out requires arithmetic structure of the integer-cell map and the actual zeta packet; Selberg density alone reaches the `1/G` endpoint but does not control the compression eigenvectors.
