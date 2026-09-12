# MI-010 — Smooth endpoint regularity diagonalizes the quadratic prime-pair channel above the `y/log y` resolution scale

**Evidence level:** supported by weighted-Haar calculations and deterministic/prime-pair transfer controls through VIS-190; no statement is made for the critical boundary, higher moments, discrete sampling, hard windows, or RH.

VIS-181--VIS-186 show that the diffuse full-prime prefix suppresses every fixed and polynomial mesoscopic gap shell at linear observation scale. VIS-187 then reveals that summing many shells under a rectangular window can still produce a deterministic logarithmic resonance, while VIS-188 identifies that resonance as endpoint leakage and removes it with an endpoint-zero taper.

VIS-189 proves that for a fixed endpoint-zero `C^2` taper the complete absolute normalized prime-pair off-diagonal is `O(1/log y)` at linear observation length `H~y`. VIS-190 sharpens the scale by combining the trivial kernel bound with the `1/(H|log(q/p)|)^2` tail before summing prime pairs.

The resulting envelope is

`O_v(y;H,T) << y/(H log y)` for `1<=H<=y`,

and `<< y^2/(H^2 log y)` for `H>=y`, uniformly in the interval start. Hence every regime with `H log y / y -> infinity` already has `M_v(y;H,T)=1+o(1)`. Linear observation length was sufficient but not the actual resolution threshold of this absolute method.

The obstruction is now localized. At the boundary `H~y/log y`, top-scale prime gaps `d<=y/H` remain unresolved by the taper kernel, so only the trivial `O(1)` kernel estimate applies; their average singular-series mass produces an `O(1)` envelope. Extra fixed smoothness only improves the resolved tail `d>y/H` and cannot remove this zone.

The reusable conclusion is therefore: **for this smooth quadratic full-prefix observable, source information can survive below `y/log y` only through arithmetic structure or signed cancellation inside the kernel-unresolved short-gap population, or by changing the observable itself.** Refining gap scales or making the same fixed taper smoother cannot by itself reopen a channel already killed by the absolute envelope.

**Boundary.** VIS-190 gives a sufficient diagonalization scale and an absolute-method barrier, not a sharp theorem for the actual oscillatory mean at `H~y/log y`. Constants are for fixed `alpha<1/2` and a fixed taper; higher/growing-order observables, discrete sampling, nonlinear statistics, adaptive windows and signed cancellation remain outside the claim.