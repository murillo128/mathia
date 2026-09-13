# MI-012 — Cutoff tuning cannot beat the four-form pointwise threshold

**Evidence level:** exact as a limitation of the VIS-197--VIS-199 proof architecture through VIS-200. It is not a lower bound on the true dephasing horizon or on the actual collision energy.

The four-form dephasing proof splits first-gap fibers at a cutoff `X=(y/H)L`. Below the cutoff, the pointwise local-factor majorant and dimension-four upper-bound sieve contribute roughly `B(y)(log y)^2/log(H/L)^4`; above it, endpoint-zero taper decay contributes `(log y)^2/L^3`. The conductor-zero branch is independent of `L`.

These two terms force incompatible demands if one hopes to beat the current threshold by cutoff choice alone. The tail needs `L/(log y)^(2/3) -> infinity`, while the sieve term still needs `log(H/L)` much larger than `(1+log log y)sqrt(log y)`. Choosing the smallest tail-safe `L` recovers only `O(log log y)` inside the sieve logarithm and does not change the leading barrier.

So the bottleneck is no longer where the proof is split. It is the use of a **pointwise worst-case local-factor bound followed by separate fiberwise summation**. Progress below the present corridor must average local factors, couple dangerous fibers before taking maxima, exploit cancellation/packing, or replace the weighted-spacing resource itself.

**Boundary.** A better aggregate sieve or a different dephasing resource can evade this obstruction. VIS-200 does not claim that the true prime collision geometry has the same threshold.