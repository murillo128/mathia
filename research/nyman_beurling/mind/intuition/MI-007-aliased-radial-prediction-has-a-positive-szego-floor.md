# MI-007 — Radial Szegő charge now has a scalar q-adic visible-energy obstruction

**Evidence level:** exact for the single-integer-dilation radial certificate through NB-087. Whether the resulting q-adic visible-energy distortions have divergent squared mass, or the full aggregate floor charge stays bounded on an unbounded sequence, remains open; failure of the radial certificate does not classify the full nonstationary future.

NB-084 turns each integer-dilation descendant ray into an anchored Toeplitz prediction problem with the actual periodized spectral density `W_(j,q)`. NB-085 proves `log W_(j,q) in L^1(T)`, so Szegő--Kolmogorov gives a strictly positive geometric-mean floor `G_(j,q)`. NB-086 then avoids estimating those floors individually: on the terminal visible block, radial descendants are already beyond the cutoff, and the aggregate radial charge dominates the normalized terminal Gram determinant deficit.

NB-087 uses exact q-adic branching to compress a substantial part of that determinant test from `O(R^2)` pairwise correlations to one scalar ratio per complete terminal sibling block. For

`eta_(j,R)^(q)= q ||J_(R/q)D_j||^2 / sum_(k=qj)^(q(j+1)-1) ||J_R D_k||^2 - 1`,

there is a constant `c_q>0` such that

`S_(R,q) >= c_q sum_(j in P_(R,q)) |eta_(j,R)^(q)|^2`.

The scalar is canonical rather than an arbitrary compression: exact branching identifies it as the Rayleigh defect of the sibling correlation matrix in the average coefficient direction. Fischer's determinant inequality then makes each sibling defect pay a compulsory portion of the full terminal entropy.

Bounded fixed-`q` radial charge therefore forces an `l^2` budget on these visible two-scale distortions. Since there are `asymp R` complete terminal sibling blocks, their mean square must be `O(R^-1)` and their RMS `O(R^-1/2)`; only `O_(q,epsilon)(1)` blocks may have distortion above any fixed `epsilon`. Conversely, divergent squared distortion mass kills the fixed-`q` radial certificate without reconstructing the full correlation matrix or any aliased Szegő floor.

The live source test is now substantially cheaper: estimate the matched truncated norms in these q-adic parent/child ratios for `j asymp R`. Distortion systematically larger than the `R^-1/2` RMS scale rules out the radial route. A bounded scalar budget only passes this necessary test; within-block contrast directions, cross-block correlations, earlier indices and the remaining floor charge may still obstruct prediction.

**Boundary.** NB-087 is a necessary-condition reduction, not a converse. The unit-outer memory-free control has `eta=0` identically, so the scalar test does not manufacture entropy by itself. Failure of one fixed-`q` radial geometry redirects the problem toward cross-ray/nonradial cancellation rather than proving a nonzero Nyman stable tail.