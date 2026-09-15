# MI-022 — One-level sparsity cannot exclude growing reciprocal clusters on fixed-relative windows

**Evidence level:** exact formal matched-control construction from [RE-133](../../findings/RE-133-growing-reciprocal-clusters-hide-dominant-atoms-on-fixed-relative-windows.md)

RE-132 shows that a single reciprocal-scale cancelling doublet can hide a dominant atom on every sublinear observation window but becomes visible on a fixed-relative window. RE-133 closes the tempting inference that macroscopic observation alone therefore defeats the formal control class.

For any fixed `0<kappa<1/2`, choose `0<r<1` so that

`q = max_(|s|<=kappa) |1-r^(1+s) exp(i pi s)| < 1`.

At stage `j`, RE-133 places a simple `2^j`-point subset cluster whose horizontal and ordinate increments are both reciprocal in the observation scale. After normalizing by the empty-subset dominant atom, the stage packet factors approximately as a product of `j` copies of the contractive factor above. Hence its full contribution on `u=U_j(1+s)`, `|s|<=kappa`, is suppressed like `q^j` while the dominant atom itself remains algebraically large.

The phases can be chosen sufficiently lacunary that other stages are negligible and, simultaneously, the entire right-half-strip counting function satisfies

`N_ctl(sigma_0,T) <= L(T)`

for any prescribed divergent envelope `L(T)->infinity` (up to an immaterial fixed factor in the counting convention). Thus **arbitrarily strong one-level sparsity is compatible with enough microscopic local cluster complexity to hide a dominant atom uniformly on a fixed-relative window**.

This does not contradict RE-131. That result identifies necessary local companion geometry for macroscopic hiding; the RE-133 cluster deliberately realizes that geometry at growing multiplicity. Nor does the construction claim such clusters occur among actual zeta zeros: it preserves simplicity, functional-equation symmetry and the finite-order coefficient kernel but not the Euler product or explicit-formula constraints of zeta.

The reusable boundary is sharper than the doublet obstruction of MI-021. Global one-level counting cannot close the attained-edge branch even after the observation window becomes macroscopic. A successful exclusion must control **local cluster complexity, relative phases or source compatibility of actual zeros**, not only how many off-critical zeros exist below height `T`.
