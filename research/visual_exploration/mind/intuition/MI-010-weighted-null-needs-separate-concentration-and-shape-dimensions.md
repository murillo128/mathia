# MI-010 — Smooth endpoint regularity collapses the entire linear-scale quadratic prime-pair channel

**Evidence level:** supported by weighted-Haar calculations and deterministic/prime-pair transfer controls through VIS-189; no statement is made for higher moments, discrete sampling, hard windows, or RH.

VIS-181--VIS-186 show that the diffuse full-prime prefix suppresses every fixed and polynomial mesoscopic gap shell at linear observation scale. VIS-187 then reveals that summing many such shells under a rectangular window can still produce a deterministic `log M` resonance from a flat even-gap source when exactly one hard endpoint is resonant.

VIS-188 identifies that logarithm as endpoint leakage. Making the window vanish at both ends removes the first Fourier boundary term and improves the kernel tail from `1/z` to `1/z^2`; the flat-gap cumulative resonance becomes uniformly bounded.

VIS-189 shows that this is not merely a matched-null cleanup. Combining the same tapered kernel with standard prime-pair upper-bound sieve input yields, for fixed `alpha<1/2`,

`Q_y^(-1) sum_(p<q<=y) p^(-alpha) q^(-alpha) |K_v(p,q)| << y^2/(H^2 log y)`.

At `H>=c y` the entire absolute off-diagonal is therefore `O(1/log y)`. Near gaps are summable because the taper changes the gap weight from harmonic `1/d` to `1/d^2`; far multiplicative pairs are even smaller without pair-correlation input.

The reusable intuition is now stronger than “control endpoint resonance”: **for a fixed endpoint-zero smooth window, the whole linear-scale quadratic full-prefix prime-log field asymptotically diagonalizes**. No choice of gap scale within that same observable can recover an order-one quadratic source signal once the absolute envelope already vanishes.

This redirects the positive search. A surviving mechanism must change observation order, sampling, normalization/support geometry, or source coordinates rather than refine the quadratic gap decomposition. A hard rectangular window remains a different observable, but its slow Fourier leakage is a load-bearing feature that must be controlled explicitly.

**Boundary.** VIS-189 assumes fixed `alpha<1/2`, a fixed endpoint-zero `C^2` taper, continuous averaging, and the full-prefix quadratic normalization. Constants are not uniform at the critical `alpha=1/2`, and the result does not cover growing-order moments, discrete Gram sampling, nonlinear statistics, adaptive tapers with growing derivative norms, or sparse adversarial support normalizations.