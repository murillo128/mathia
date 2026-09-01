# MI-003 — Scalarizing the Yang lock moves the hard part into signed finite-window Ramanujan leakage

**Evidence level:** supported for the exact source reductions, positive/unweighted scalar-energy obstructions, Ramanujan projector decomposition, and pairwise boundary-rank theorems; the remaining signed many-modulus/source-weighted analytic bridge is open

## Core intuition

The unresolved Yang--Yang fourth-moment obstruction is a source-faithful representation problem with a conservation law. Freeing physical shifts produces a power-sparse two-dimensional selector; scalar LCM projection removes that sparsity but produces a near-linear, maximally additively energetic positive family; and using signs does not help inside the existing positive large-sieve interface. After scalarization, genuine sign cancellation can occur only through finite-window leakage between otherwise orthogonal Ramanujan subspaces.

## Strongest justified principle

WI-068--WI-076 establish the representation boundary. Free independent shifts expose finite-complexity prime patterns only after projecting back to a thin exact slope slice. The physical two-dimensional incidence lies in an `lcm << X` envelope of density `X^{-1+o(1)}`, so every source-agnostic fixed finite `L^p` restriction pays a power and Cartesian reboxing cannot remove the long-shift GCD sparsity. Scalar LCM projection behaves oppositely: one fixed source slope already gives at least `X/(log X)^4` effective nonzero scalar moduli.

WI-077 closes the ordinary unweighted additive-energy repair. A near-linear scalar family inside an `O(X)` interval has symmetric and asymmetric additive energy `Q^{3-o(1)}`, the maximal exponent, so the Baker--Munsch--Shparlinski sparse-moduli theorem gives no fixed-power gain at the natural density. WI-078 strengthens this to the actual positive Yang weights: their weighted energies have the maximal exponent, and every pruning that retains a subpolynomial fraction of positive source mass keeps that exponent. Positive support/energy reduction is therefore not the missing theorem.

WI-079 identifies what the surviving signed route would have to estimate. The published scalar large sieve is a positive sum of squared modulus blocks, so passing a centered signed combination through it replaces the weights by their absolute values. Before that positivity projection, the signed operator is the Toeplitz Ramanujan sum

`R_omega(h) = sum_m omega_m c_m(h)`,

and small operator norm forces simultaneous cancellation of the totient diagonal and low-divisor Möbius marginals. Ordinary signed additive energy is not an input to this operator problem.

WI-080 then diagonalizes the complete-period model exactly. On any common period, the Ramanujan modulus blocks are pairwise orthogonal projections; signs merely change the signs of spectral blocks and give **no** operator/Schatten/rank cancellation. Hence every cross-modulus signed gain is created solely by restriction to a finite consecutive source window.

WI-081 localizes that leakage further. For a pair `m,n`, the cross-Gram rank is bounded by the distance `delta_N(m,n)` from the window length to the nearest multiple of `lcm(m,n)`, and this bound is exact whenever `delta` is at most both Ramanujan dimensions. For separated prime moduli it is generically maximal once the boundary defect reaches the smaller dimension. Only a close-prime phase strip admits additional rank deficiency. Thus even the pairwise finite-window route has little generic rank room left.

The scalar conservation law is now sharp: two-dimensional source fidelity costs sparse incidence; positive scalarization costs maximal density/energy; signed scalarization avoids that positive obstruction only by relying on nonperiodic time-limiting interaction among Ramanujan subspaces.

## What remains possible

The viable scalar route must use the **actual centered signed Yang coefficients** and prove cancellation in the finite-window Ramanujan operator beyond what pairwise rank alone can supply — for example through singular values, coherent dependencies across many modulus pairs, or a source-forced structure in the close-modulus phase. A labelled transform retaining reduced slopes, a direct weighted two-dimensional incidence theorem, or the base-aggregated multivariate polynomial representation remain distinct source-faithful alternatives.

Any argument that restores complete residue periods before estimating, applies a positive scalar large sieve after absolute values, prunes only positive mass, or relies only on scalar support/additive energy is now closed as a cheap interface.

## Status / novelty

Ramanujan sums/subspaces, additive-energy inequalities, large-sieve positivity, Fourier truncation, and Vandermonde rank are classical. The persisted Mathia content is the exact placement of the Yang source inside these models and the resulting identification of finite-window Ramanujan leakage as the only remaining sign-sensitive scalar channel.

## Falsification criterion

Find a power-saving positive/unweighted scalar-energy interface contradicting WI-077--WI-078, cross-modulus norm cancellation on a complete common period contradicting WI-080, or a stronger generic pairwise rank saving in the exact WI-081 regime. A positive advance should estimate the signed finite-window operator with the exact source coefficients rather than a support surrogate.

## Lean-formalizable core

- Positive weighted energy lower bounds on interval-supported measures.
- Loewner majorization of signed modulus blocks by absolute weights.
- Ramanujan-projector orthogonality on common periods.
- Pairwise LCM-boundary factorization and exact small-boundary rank.
