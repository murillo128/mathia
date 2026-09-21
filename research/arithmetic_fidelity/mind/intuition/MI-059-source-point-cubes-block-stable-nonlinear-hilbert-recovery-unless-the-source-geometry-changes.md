# MI-059 — Source-point cubes block stable nonlinear Hilbert recovery unless the source geometry changes

**Evidence level:** exact metric synthesis from [AF-464](../../findings/AF-464-enflo-type-blocks-nonlinear-hilbert-escape-on-sparse-mixtures.md), interpreted against the affine/secant obstructions AF-457--AF-463. The metric-type ingredient is classical; the line-specific content is the paired-mixture cube inside the sparse probability simplex under TV.

For `k`-sparse probability laws on an alphabet containing `2k` paired atoms, the source itself contains a Hamming cube: choosing one atom from each pair gives laws `mu_epsilon` with

`||mu_epsilon-mu_eta||_1 = (2/k) d_H(epsilon,eta)`.

Therefore linearity of the encoder is not needed for the square-root obstruction. If `F` maps this source into a metric/Banach target of Enflo type `p` and has finite upper TV-Lipschitz modulus `L(F)`, then its lower TV modulus satisfies

`kappa(F) <= T_p^E(Y) L(F) k^(1/p-1)`.

For Hilbert targets this becomes `kappa(F) <= L(F)/sqrt(k)`, equivalently distortion at least `sqrt(k)`. The same conclusion holds on any restricted source class that actually contains the paired-mixture source-point cube. This is stronger in operator category than the earlier affine/secant results but stronger in its source hypothesis: AF-458--AF-459 need rich normalized secants, whereas AF-464 needs all cube vertices to be admissible source points.

The reusable distinction is that **nonlinearity alone is not a stable-fidelity resource once the physical source contains growing `ell^1` metric cubes and the destination has nontrivial metric type**. A genuine escape must remove those source-point cubes, change the source metric, move to a type-1 target, allow upper sensitivity to grow with complexity, or narrow the task to a comparison geometry that does not require pairwise TV recovery.

**Boundary.** This is a bi-Lipschitz/conditioning obstruction, not an injectivity theorem. The upper modulus is load-bearing, and unrestricted simplex cubes do not prove that a particular arithmetic source contains comparable cubes. Different intrinsic metrics, singular/thin source laws, anchored tasks and discontinuous or increasingly steep codes remain outside the conclusion.