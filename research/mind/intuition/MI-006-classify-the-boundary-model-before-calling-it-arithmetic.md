# MI-006 — Singular fresh-fiber normalization yields at most two boundary phases

**Evidence level:** supported; the endpoint statement is for the specified symmetric regularization and fixed packet sectors.

For `0<sigma<1`, set `g_sigma(j)=sin(pi sigma)/(pi(j+sigma))` in `ell^2(Z)` and let `S` be the bilateral shift. [PC-237](../../prime_circle/findings/PC-237-singular-fresh-fiber-weighting-collapses-to-two-sided-boundary-phase-data.md) proves that every `g_sigma` has exactly Haar spectral measure for `S`. Hence

\[
g_\sigma\in\operatorname{Dom}V(S)\iff V\in L^2(\mathbb T),
\qquad
|1-S|^{-\alpha}g_\sigma\in\ell^2\iff\alpha<1/2.
\]

For `V_(alpha,epsilon)(e^(i theta))=(4 sin^2(theta/2)+epsilon^2)^(-alpha/2)` and normalized weighted packets `h_(sigma,epsilon)`, every `alpha>=1/2` has

\[
\lim_{\varepsilon\downarrow0}\langle h_{\sigma,\varepsilon},h_{\tau,\varepsilon}\rangle
=\cos\bigl(\pi(\tau-\sigma)\bigr).
\]

This kernel has rank at most two. At fixed finite sector count, increasing the singular power does not create an expanding spectral carrier; the normalized limit retains only the two one-sided boundary phases. This does not classify growing-sector, noncommuting or differently regularized constructions.

The corresponding calculation must be redone, not transferred by analogy, for a different singularity. In the flute's normalized Robin source, [PF-278](../../prime_flute/findings/PF-278-mass-one-branch-forces-critical-normalized-fixed-row-leakage.md) instead retains a nonremovable square-root branch and produces fixed-row leakage `N^-1(log N)^-3/2`. That is an infinite-tail obstruction to a supercritical estimate, not a rank-two collapse. Both are concrete limits of a normalization, but their output categories and consequences differ.
