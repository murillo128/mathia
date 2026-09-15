# MI-026 — Fixed boundary Julia reduction either creates log-over-linear contamination or worsens the Gamma curvature

**Evidence level:** exact finite-chain boundary Julia–Nevanlinna obstruction from [WP-312](../../findings/WP-312-fixed-boundary-julia-nevanlinna-reduction-cannot-repair-gamma-asymptotic.md), complementing the fixed-interior Schur obstruction in [WP-311](../../findings/WP-311-finite-interior-schur-stripping-introduces-log-over-linear-gamma-contamination.md)

WP-312 closes the canonical fixed real boundary version of scalar Pick/Herglotz reduction for the reflected pole-normalized Mangoldt response. Classical Julia–Nevanlinna reduction has two cases, and both move the asymptotic in the wrong direction after preserving positivity.

At a regular real boundary node `x`, with `w=f(x)` and `d=f'(x)>0`, the reduced Pick function tends to the boundary point `0`. Returning it to the unit logarithmic end fixes the half-plane automorphism uniquely up to a real translation. If

`Re f(iy)=log y+c+A log(y)/y+O(1/y)` and `Im f(iy)=q+O((log y)^2/y)`, `q>0`,

the normalized boundary reduction changes

`A -> A + 2q/d`.

For the reflected Mangoldt source `q=pi/2`, every regular fixed node therefore creates a strictly positive `log(y)/y` term. The Riemann Gamma channel has no term at that order, so the comparison is already contaminated before its `y^-2` curvature is reached.

At a Mangoldt pole the classical reduction instead subtracts the negative-residue pole. This creates no `log(y)/y` defect, but its first real correction changes the arithmetic curvature by

`A_M -> A_M + Lambda(n) log n/(n+1)`.

Since `A_M>0` while the Gamma coefficient is `-1/24`, every pole removal makes the existing sign mismatch strictly worse.

Hence every finite chain of fixed boundary reductions has an exact dichotomy: one regular node permanently introduces the larger positive `log(y)/y` scale; an all-pole chain preserves that scale at zero but pushes the positive `y^-2` curvature farther from the negative Gamma value. Combined with WP-310 and WP-311, the natural **fixed scalar Schur/Julia orbit** is exhausted by admissibility or asymptotic-orientation obstructions.

The surviving scalar-looking escapes are genuinely scale dependent: moving boundary nodes, an infinite chain with separately proved convergence, or an independently justified renormalization. Operator/matrix-valued boundary structure, generalized resolvents, noninvertible maps, added archimedean structure and nonseparable finite–archimedean coupling remain outside the no-go class.

**Boundary.** The theorem is for finite chains at fixed real boundary nodes and the canonical positivity-preserving normalization back to unit logarithmic growth. It does not cover nodes moving with the high-energy scale, infinite boundary chains, operator-valued reductions or any mechanism that changes the finite–archimedean geometry before scalar comparison.