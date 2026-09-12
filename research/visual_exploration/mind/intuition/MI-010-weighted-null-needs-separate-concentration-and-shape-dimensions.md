# MI-010 — Smooth quadratic observation has a sharp absolute-envelope resolution barrier at `y/log y`

**Evidence level:** supported by weighted-Haar calculations and deterministic/prime-pair transfer controls through VIS-191; no statement is made that the signed tapered mean fails to diagonalize at or below the boundary, nor is any RH-sensitive signal established.

VIS-181--VIS-186 show that the diffuse full-prime prefix suppresses every fixed and polynomial mesoscopic gap shell at linear observation scale. VIS-187 reveals a deterministic logarithmic accumulation under a rectangular window, while VIS-188 identifies that effect as endpoint leakage and removes it with an endpoint-zero taper.

VIS-189 proves that for a fixed endpoint-zero `C^2` taper the complete absolute normalized prime-pair off-diagonal is `O(1/log y)` at linear observation length. VIS-190 sharpens the upper scale to

`O_v(y;H,T) << y/(H log y)` for `1<=H<=y`,

uniformly in interval start, so every regime `H log y/y -> infinity` has quadratic diagonalization by absolute control.

VIS-191 proves that this threshold is not merely a weakness of that upper bound. For every fixed `0<=alpha<1/2`, if `H log y/y -> 0`, ordinary consecutive prime pairs in `(y/2,y]` already contribute

`liminf O_v(y;H,T) >= (1-2alpha)/2`.

The input is only the prime number theorem, telescoping of top-half consecutive gaps, and continuity of the taper Fourier kernel at zero. A positive proportion of consecutive gaps are `O(log y)`; at subcritical `H` their frequencies satisfy `H log(q/p)=o(1)`, so the kernel sees them with modulus tending to one. Their normalized absolute mass is order one.

Hence `y/log y` is a genuine Fourier-resolution boundary for the **absolute-value method**: above it by a diverging factor the full envelope vanishes, while below it by a vanishing factor the envelope is bounded away from zero. Extra fixed smoothness cannot repair the unresolved consecutive-prime population because the obstruction comes from kernel continuity near frequency zero, not tail decay.

The remaining route inside this observable is therefore specifically **signed cancellation** among kernel-unresolved short-gap pairs at the critical/subcritical scale. The order-one absolute envelope does not imply that the signed mean `M_v-1` stays large. If such signed cancellation cannot be proved from the arithmetic source, the observable must change—through higher/growing-order information, source-adapted/discrete sampling, nonlinear statistics, or another controlled representation.

**Boundary.** VIS-191 does not prove a critical-scale constant, signed prime-pair correlation, failure of mean-square diagonalization below `y/log y`, or any RH consequence. It closes only the idea that stronger absolute prime-pair estimates or a smoother fixed taper can push the same absolute-envelope argument below that scale.