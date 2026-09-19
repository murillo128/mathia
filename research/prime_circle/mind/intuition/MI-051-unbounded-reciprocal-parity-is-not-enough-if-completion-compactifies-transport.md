# MI-051 — Unbounded reciprocal parity is not enough if the completion compactifies transport

**Evidence level:** exact synthesis from `PC-358`--`PC-359` plus classical compact-operator theory.

PC-358 isolates the necessary infinite-dimensional escape from finite reciprocal-control similarity: if the algebraic parity intertwiner remains bounded on the chosen completion, source and control remain similar and ordinary spectral data cannot separate them.

PC-359 shows that violating this boundedness condition is only one gate. In a scalar grade-weighted word completion, reciprocal parity on grade `m` has norm `||J||^m`, so it can become genuinely unbounded. At the same time, a positive-degree creation block of lag `k` has norm proportional to

`sqrt(w_(m+k)/w_m)`.

If every fixed-lag ratio tends to zero, all such creation blocks are compact. A norm-convergent strictly grade-raising multiplier is then compact and has no nonzero eigenvalues; compact spectral theory forces its entire spectrum to be `{0}`. Adding the identity gives the singleton spectrum `{1}`.

Thus the two relevant completion coordinates are independent: **the control intertwiner must become non-bounded, while the source operator must retain noncompact high-grade transport**. A completion can pass the first test and fail the second so strongly that the desired spectrum disappears before any source/control comparison is made.

This gives a practical audit for infinite-dimensional spectral constructions. First test bounded similarity or domain transport under the source/control involution. Separately test the asymptotic block norms of the actual multiplier. If those block norms vanish and the operator is a norm-convergent positive-degree sum, stronger regularization is moving in the wrong direction even though it breaks the finite-cutoff similarity proof.

**Boundary.** The obstruction is specific to scalar grade weights with fixed-lag ratio decay, bounded positive-degree creation blocks, and operator-norm convergence of their sum. Borderline noncompact weights, unbounded/closed multipliers, non-scalar grade couplings, two-sided operators and non-spectral observables remain open. Nothing here selects zeta zeros or implies RH.
