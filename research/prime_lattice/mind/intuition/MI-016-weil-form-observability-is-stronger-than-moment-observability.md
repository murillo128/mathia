# MI-016 — Actual localized-Weil eigenstates have every fixed logarithmic moment; the remaining aperture gate is quantitative growth beyond the log hierarchy

**Evidence level:** proved for the one-dimensional source-static localized Weil eigen-equation through PL-291, conditional on the PL-283--PL-284 finite spectral certificate at `a=0.8` where that endpoint is invoked. Completed arithmetic positivity, positive-order Sobolev regularity and a quantitatively useful macroscopic aperture theorem remain open.

PL-285--PL-286 identify the sharp ambient obstruction: the logarithmic form ball has only inverse-log transport. PL-289 improves actual eigenstates to the graph domain of the principal logarithmic operator and obtains a squared-log Fourier moment. PL-290 proves that this is still the sharp generic endpoint on the **full graph ball**, even with the active `2,3,4` arithmetic comb; graph regularity alone cannot make the aperture family Lipschitz or differentiable.

PL-291 shows that the actual eigen-equation selects a much smaller class than the graph ball. On every compact source-static aperture interval, the bounded arithmetic remainder preserves every logarithmic Fourier scale, and the exterior cross-boundary piece of the logarithmic Laplacian does as well. Bootstrapping the eigen-equation therefore gives every fixed moment

`int log(2+|xi|)^(2m) |uhat(xi)|^2 dxi < infinity`.

Consequently, for each fixed `m`, actual eigenstate autocorrelations and the lowest eigenvalue have source-static aperture modulus `O(log^(-2m)(1/|delta|))`. The graph-ball `log^-2` obstruction is real for generic states but is **not** the regularity endpoint of the low spectral family.

The remaining bottleneck is quantitative. The constants in the all-log hierarchy may grow arbitrarily fast with `m`, so one cannot optimize `m=m(delta)` or infer any positive power-law modulus. All finite logarithmic moments remain weaker than a single positive-order Sobolev moment, and differentiating a moving translation still introduces the uncontrolled multiplier `xi`.

The next theorem must therefore control the growth of the logarithmic-moment constants, derive a genuine positive-order moment or source-specific cancellation identity, or certify positivity directly over a nontrivial aperture interval. **Another finite logarithmic regularity upgrade cannot change the problem.**

**Boundary.** PL-291 is source-static and its bootstrap mechanism is not uniquely arithmetic: matched finite-shift remainders can preserve the same logarithmic scales. Prime-source rigidity must enter through coefficients, activation structure, cancellation or a later positivity theorem. Source activation thresholds and global aperture continuation remain separate gates.