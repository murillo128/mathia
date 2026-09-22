# MI-063 — A remainder estimate is useful only if it crosses the repair threshold before cluster pruning expires

**Evidence level:** exact exponent synthesis from FD-278--[FD-281](../../findings/FD-281-classical-perron-error-pushes-repair-control-above-cluster-pruning-regime.md), under the same RH/simple-zero assumptions where the preceding spectral-height ledger uses them.

FD-281 prices the classical pointwise Perron remainder after the exact consecutive-difference and divisor-replication map used by the Farey destination. With `Y=2Nx`, the standard Mertens error gives transformed total size

`O(N x^2 log(2Nx)/T + x log(2x))`.

To make the leading term smaller than a repair target `N^theta x^(2-beta)`, where `beta=log_2(3/2)`, one needs

`T >> N^(1-theta) x^beta log(2Nx)`.

At polynomial depth `x=N^(lambda+o(1))`, this corresponds to Perron height exponent `tau=beta+(1-theta)/lambda`. The cluster-population obstruction from FD-278 already becomes unavoidable above `c_*=1-beta`. Since `tau>beta>c_*`, the classical pointwise Perron estimate only becomes harmless after the zero population has crossed the regime in which the existing cluster-pruning ledger can close.

The obstruction is therefore an **ordering mismatch between two tariffs**, not evidence that the true remainder is large. First taking a pointwise absolute Perron bound and only then feeding it through the repair map loses the signed/grouped structure too early. A viable spectral route must instead retain cancellation in a repair-aware remainder, group the contour with boundary clusters before absolute values, or prove a substantially stronger remainder estimate that crosses the physical repair threshold while the spectral population is still prunable.

This sharpens the hard-cut lesson of MI-062. Cluster completion can improve packet conditioning without controlling the complementary remainder, and the most immediate classical pointwise control of that remainder is quantitatively too late. The correct question is not simply whether a remainder tends to zero with `T`, but whether it becomes small in the exact destination norm **before** the auxiliary spectral resources needed to obtain that bound invalidate the rest of the proof ledger.

**Boundary.** FD-281 is a barrier for the classical pointwise Perron route followed by triangle inequality and the current replication architecture. It is not a lower bound for the exact remainder, does not rule out signed cancellation or smoothing, and does not prove that every cluster-complete contour decomposition has the same exponent cost.