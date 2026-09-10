# MI-007 — Bow cancellation is source alignment inside a Fejer-controlled fixed spectral geometry

**Evidence level:** exact post-sieve normal forms, unitary-gauge reduction, sharp near-kernel scale, spectral multiplicity, and positive finite-rank Fejer reduction through ANF-156

## Core intuition

The distinguished bow twist does not create a distinguished Gram spectrum. After the exact gauge reduction, the moving-window operator has one fixed geometry and the arithmetic question is how the demodulated prime innovation sits inside its low singular sector.

That sector is neither thin nor geometrically mysterious. It contains a growing ladder of low positive directions, and after dualization its bulk is the classical Fejer Toeplitz finite section with only a positive `O(K)`-rank boundary correction. The hard step is therefore directional source alignment, not existence or scarcity of near-null directions.

## Strongest justified principle

ANF-150--ANF-152 show that matched post-sieve controls can reproduce available local prime statistics while retaining diagonal bow variance, and that fixed source mass above a positive Gram level obstructs subdiagonal cancellation. ANF-153 freezes the geometry by diagonal unitary gauge and ANF-154 places the first positive normalized scale at `Theta(K/N^2)` while showing that small energy need not imply closeness to the exact periodic kernel.

ANF-155 strengthens the geometry on the cofinal family `N=mK`: detuned box-null Fourier characters span trial spaces giving `nu_+(4 pi^2 J^2 K/N^2) >= J(K-2)`. Thus already at the bottom scale there are `Omega(K)` positive directions, and by scale `1/K` there are `Omega(N)`.

ANF-156 identifies the exact positive spectrum with the dual Gram `B=AD^{-1}A*` and decomposes it as the Fejer Toeplitz matrix `T_N(F_K)` plus a positive boundary correction `E` with `rank(E)<=2K-2` and `tr(E)=K-1`. Positive eigenvalue counts differ from the Toeplitz counts by at most `2K-2` at every threshold. Its quadratic-form formula further shows that a low dual mode must put Fourier mass near the nonzero box-filter nulls while simultaneously paying little nested prefix/suffix boundary energy.

## Program consequence

Translate the actual demodulated source projection into this dual geometry. The next useful theorem should convert low-singular-sector mass into an explicit twisted prime/Ramanujan correlation statement, or prove that the source necessarily leaves a fixed fraction of its positive component either away from the Fejer null tubes or in the boundary tax. Geometry-only eigenvalue counting is no longer the missing step.

## Counterevidence / boundary

The Fejer comparison is a counting statement, not projector convergence, and the rank-`O(K)` boundary correction can still control the very bottom `Omega(K)` directions. ANF-155 uses the cofinal divisibility model `N=mK`; ANF-156 removes that restriction only for bulk counting. None of these results shows that the actual prime source aligns with the true low eigenspaces.

## Epistemic status

**Exact fixed bow geometry with a thick low-spectrum ladder and a Fejer-plus-boundary description of its positive sector; source-specific spectral placement remains open.**

## Falsification criterion

Invalidate the unitary-gauge reduction, the min--max multiplicity bound, or the dual Fejer-plus-positive-boundary decomposition; or derive the required bow cancellation while retaining quantitatively incompatible source mass in the positive sector. A positive continuation should prove the source-to-low-projector correlation estimate itself.
