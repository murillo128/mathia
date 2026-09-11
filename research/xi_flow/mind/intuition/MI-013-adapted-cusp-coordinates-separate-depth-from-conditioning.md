# MI-013 — Xi packet complexity costs samples, not remote conditioning, in the holomorphic acquisition category

**Evidence level:** proved local growing-packet linearized acquisition; global nonlinear source coercivity remains open

## Core intuition

Remote packet location is not a fundamental instability of the Xi inverse. Adapted coordinates remove inverse conditioning, and mesoscopic complex Jacobi phase removes the positive-real acquisition loss. The newest result shows that this remains true when packet complexity itself grows through the natural lattice-scale regime: a packet of `m<=N` consecutive remote atoms can be observed with uniform conditioning using only `O(m)` complex samples.

The durable separation is now between **model complexity/sample count** and **conditioning**. The remaining obstacle is global source uncertainty—unknown support, nonlinear deformation, and analytic control of the actual Xi/Jacobi object—not deterioration of the known-packet linear acquisition matrix.

## Strongest justified claim

XF-177--XF-184 show that depth `m` is necessary for `m` moved atom pairs, packet-adapted coordinates remove remote inverse conditioning, positive-real acquisition has a graded/exponential visibility cost, and fixed-complexity complex Jacobi sampling turns the local linearized map into a DFT-like uniformly conditioned system.

XF-185 removes the fixed-`m` caveat on the natural lattice scale. For a known consecutive packet of `m` atoms beginning near `N` with `2<=m<=N`, an explicit Fejer-overcomplete bank of at most `6m-1` anisotropic complex Jacobi samples has linearized singular values comparable to `sqrt(m)` with constants independent of both `N` and `m`. Reciprocal-image contamination remains exponentially small even across the full bank, and the row normalization is uniformly bounded, so the raw complex samples already contain the same lower visibility.

## Synthesis of evidence

Growing packet width no longer creates an intrinsic local conditioning barrier as long as sample count is allowed to scale linearly with complexity. A no-go based only on remote location or growing `m` is therefore too weak in the holomorphic category.

The live theorem must handle **support discovery and nonlinear/global assembly**: show that the true Xi/Jacobi source supplies a feasible multiscale complex-sampling family from which unknown packets of varying location/width can be identified and controlled without importing zero data equivalent to the target.

## Counterevidence / boundary cases

XF-185 is linearized and assumes a known consecutive packet. It does not solve sparse support search among many possible locations, interaction between multiple packets, nonlinear displacement radius, or analytic bounds needed to evaluate the true source at all required complex sample points.

The `O(m)` sample cost is real; the result removes condition-number growth, not information-theoretic complexity.

## Epistemic status

**Exact local complexity boundary:** for known lattice-scale packets, growing complexity costs linearly many holomorphic samples but does not worsen remote conditioning. The remaining problem is nonlinear unknown-support source coercivity and global acquisition.

## Novelty/prior-art status

Fourier frames, Fejer kernels, Jacobi transforms, and finite-dimensional conditioning retain their finding-level boundaries.

## Falsification criterion

Invalidate the XF-185 uniform frame bounds or show reciprocal Jacobi contamination grows enough across the bank to destroy the stated lower singular-value bound. Strategically, prove a support-unknown nonlinear source theorem using such banks.
