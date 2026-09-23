# MI-063 — A remainder estimate is useful only if it crosses the repair threshold before cluster pruning expires

**Evidence level:** exact exponent synthesis from FD-278--[FD-282](../../findings/FD-282-absolute-grouped-perron-contours-retain-a-self-divisor-depth-plateau.md), under the same RH/simple-zero assumptions where the preceding spectral-height ledger uses them; FD-282's grouped-contour collar obstruction itself is unconditional apart from the standard zeta estimate used there.

FD-281 prices the classical pointwise Perron remainder after the exact consecutive-difference and divisor-replication map used by the Farey destination. With `Y=2Nx`, the standard Mertens error gives transformed total size

`O(N x^2 log(2Nx)/T + x log(2x))`.

To make the leading term smaller than a repair target `N^theta x^(2-beta)`, where `beta=log_2(3/2)`, one needs

`T >> N^(1-theta) x^beta log(2Nx)`.

At polynomial depth `x=N^(lambda+o(1))`, this corresponds to Perron height exponent `tau=beta+(1-theta)/lambda`. The cluster-population obstruction from FD-278 already becomes unavoidable above `c_*=1-beta`. Since `tau>beta>c_*`, the classical pointwise Perron estimate only becomes harmless after the zero population has crossed the regime in which the existing cluster-pruning ledger can close.

FD-282 shows that merely regrouping the physical operations before taking absolute values does not repair this ordering mismatch at low height. For the grouped kernel `K_s(d)` obtained after consecutive differencing and divisor replication, prime physical coordinates retain their self-divisor term. Uniformly on the right horizontal collar `1<=Re(s)<=1+1/log(2Nx)` and `2<=T<=x/4`,

`sum_(x<d<=2x) |K_(sigma+iT)(d)| >> x/log x`.

Consequently the absolute horizontal-collar certificate is at least `Nx` up to logarithms. Relative to the same repair target its forced exponent is `1-theta-lambda(1-beta)`, so this proof architecture is power-inadequate whenever `lambda<(1-theta)/(1-beta)`. At the critical calibration `theta=1/2`, the boundary is about `1.20471`, covering the first-row scale and every `lambda<=1`.

The obstruction is therefore not simply “take absolute values later.” The location of that interface matters. Grouping the exact divisor kernel first recovers real `T^(-1/2)` decay on the critical line, yet pointwise absolute control of the horizontal collar still destroys the signed information needed before the low-height spectral ledger can be useful. A viable contour route must retain cancellation in `sigma`, cancellation between horizontal edges, or another signed/smoothed structure through the collar itself; alternatively it must change the remainder architecture enough to alter the depth/frequency tariff rather than merely repartition the same hard contour.

This sharpens the hard-cut lesson of MI-062. Cluster completion can improve packet conditioning without controlling the complementary remainder, and the most immediate classical pointwise control of that remainder is quantitatively too late. FD-282 adds that even repair-aware contour grouping is insufficient if the next proof interface immediately replaces the grouped collar by its physical-coordinate and contourwise absolute envelope. The correct question is whether the remainder becomes small in the exact destination norm **before** the auxiliary spectral resources needed to obtain that bound invalidate the rest of the proof ledger, while retaining whatever signed structure is supposed to produce the saving.

**Boundary.** FD-281 is a barrier for the classical pointwise Perron route followed by triangle inequality and the current replication architecture. FD-282 is a barrier for the more refined route that groups the physical kernel but then takes pointwise absolute values along the right horizontal collar. Neither is a lower bound for the true Perron remainder. They do not rule out signed horizontal integration, upper/lower-edge cancellation, smoothing or modified Perron formulas, or a different repair architecture; nor do they prove that every cluster-complete contour decomposition has the same exponent cost.