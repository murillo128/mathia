# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Control the actual aliased descendant spectra at the `1/R` prediction scale

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`, `MI-006-boundary-zeros-force-reciprocal-depth-screening`.

NB-066--NB-082 reduce persistent continuation to a finite-future prediction charge and show that qualitative outerness is insufficient: a depth-`L` stationary excess must reach the destination scale `O(1/R)`. NB-083 calibrates the stationary boundary: a unit-circle zero gives only `Theta(1/L)` prediction improvement and forces linear depth, whereas a strictly exterior zero set gives geometric prediction.

NB-084 now identifies the corresponding **actual-source** finite certificate along every integer-dilation descendant ray. Exact Nyman branching makes `U_(r log q)D_j` an admissible combination of genuine later innovations, and the radial prediction error is an anchored Toeplitz problem with periodized boundary density

`W_(j,q)(theta)=(1/log q) sum_k |D_j(1/2+i(theta+2pi k)/log q)|^2`.

This changes the boundary-zero test. An individual critical-line zero removes only one alias; a zero of `W_(j,q)` would require an entire two-sided alias class to vanish. Moreover `W_(j,q)>0` almost everywhere. Thus the reciprocal-depth law of NB-083 cannot be transferred to the arithmetic source merely from ordinary zeta zeros.

The live theorem is now quantitative and source-specific: estimate the Toeplitz errors `E_(j,q,L)` relative to the visible causal prediction errors strongly enough that `sum_(j<R) log(E_(j,q,L)/PiHat_(j,R)^2)=O(1)` on an affordable choice of `L(R)`, or improve the certificate using cross-ray combinations. Positivity almost everywhere of the aliased spectrum is only qualitative; deep valleys may still make prediction expensive.

## Keep stationary inverse singularities, aliasing, prediction rate and future cost separate

NB-083 remains the correct matched control for a genuine unit-circle zero of a stationary symbol. NB-084 shows that the actual integer-descendant symbol is not the unaliased Mellin factor but its nonnegative alias-periodized energy. Source zeros, aliased spectral valleys, Toeplitz conditioning and total future cost are therefore distinct gates.

The radial certificate is one-sided: a good bound excludes a stable tail, while a poor radial bound does not rule out stronger prediction from the full nonstationary future. The next advance should estimate the actual periodized spectra rather than transplant stationary zero heuristics.