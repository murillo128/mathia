# MI-010 — Absolute resolution and signed start-averaged cancellation have different thresholds

**Evidence level:** supported by deterministic/prime-pair transfer controls through VIS-192; the signed mean-square statement is exact under long Cesàro averaging in the start variable, but no uniform-in-start or finite-window theorem and no RH-sensitive signal is established.

VIS-187--VIS-190 remove endpoint artifacts and show that for a fixed endpoint-zero `C^2` taper the complete normalized **absolute** prime-pair off-diagonal is `O(y/(H log y))`. Hence absolute diagonalization holds uniformly in start whenever `H >> y/log y`.

VIS-191 proves the opposite side for the absolute method. If `H=o(y/log y)`, a positive-density population of ordinary top-half consecutive-prime gaps remains unresolved by the kernel and forces an order-one normalized absolute floor. Extra fixed smoothness cannot remove that floor because the obstruction is near frequency zero, where every normalized taper kernel tends to one.

VIS-192 then keeps the signs and averages only over the interval start. Distinct prime ratios `q/p` give distinct positive frequencies `log(q/p)`, so ordinary finite-frequency Cesàro orthogonality eliminates all cross terms exactly. The long-start variance is

`R_v(y,H)=2 Q_y^(-2) sum_(p<q<=y) p^(-2alpha) q^(-2alpha) |kappa_v(H log(q/p))|^2`.

Squaring the taper kernel makes the near-pair energy summable at scale `1/H`. For every `H->infinity` with `H<=y`,

`R_v(y,H) << 1/H`,

and when `H log y/y -> 0`, ordinary prime-pair lower control gives the matching `R_v(y,H) asymp 1/H`. Thus the signed off-diagonal has start-RMS size `H^(-1/2)` throughout the diverging subcritical regime, even though its absolute envelope is still order one.

The conceptual boundary has shifted. `y/log y` is the sharp threshold for **absolute** resolution, not for signed diagonalization after start averaging. The unresolved short-gap population is large in absolute mass but its distinct phase frequencies cancel in long-start `L^2`.

The next resource is start control. A downstream theorem that requires one deterministic start, uniformity in `T`, or an averaging interval whose length scales with `y` cannot import the infinite-Cesàro identity for free. One must either prove a quantitative finite-start-window orthogonality estimate, identify a source-selected start family with enough phase dispersion, or show that the final target only needs an averaged/density-one statement.

**Boundary.** VIS-192 is not a uniform-in-`T` bound and does not control start windows tied to the prime height. It uses exact uniqueness of prime-ratio frequencies but no random-phase hypothesis. The result closes the idea that macroscopic absolute short-gap mass by itself prevents signed subcritical diagonalization; it does not close the deterministic-start problem.
