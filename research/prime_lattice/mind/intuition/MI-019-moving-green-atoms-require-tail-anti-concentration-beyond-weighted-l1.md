# MI-019 — Moving Green atoms require source-specific tail anti-concentration beyond global regularity

**Evidence level:** exact moving-diagonal obstruction and sufficient tail criterion from [PL-314](../../findings/PL-314-moving-diagonal-tail-threshold.md), strengthened by [PL-315](../../findings/PL-315-moving-diagonal-survives-all-log-subcritical-sobolev.md)

A weak integrated tail norm can miss the exact region sampled by a singularly moving kernel. In the Prime-Lattice stretched coordinate, the Green measure develops an atom at fixed `q=r`, while the corresponding physical logarithmic distance moves to `Q=r/s`. The normalized transfer therefore probes `m(r/s)/s`, not just total tail mass.

PL-314 constructs one fixed smooth nonnegative `m in L^1(dQ)` whose sparse bumps have vanishing total mass but height `Theta(s_n)` at `Q=r/s_n`. The moving atom sees each selected bump with order-one weight, so the rank-one limit predicted from the integral alone fails. The simple source-independent condition

`m in L^1(dQ)` and `Q m(Q) -> 0`

is sufficient to kill the moving-diagonal contribution, but PL-314 does not claim necessity.

PL-315 shows that the obstruction is much more robust than weak `L^1` control suggests. The same kind of fixed mismatch can be chosen `C^infty` and in every `W^{k,1}(dQ)`, with arbitrarily small physical `W^{1,1}` norm, while satisfying the critical envelope `m(Q)=O(1/Q)` but still having `limsup Qm(Q)>0`. After pullback to the physical endpoint, its zero extension lies in every `H^alpha` with `alpha<1/2` and in every all-log Fourier moment space used by the existing bootstrap, with moment growth substantially smaller than the current source bound. Yet the moving Green atom still produces an order-one transfer along a sequence.

The reusable diagnostic is therefore stronger: **global smoothness, BV/`W^{1,1}`, all finite logarithmic Fourier moments, and every subcritical Sobolev gain can coexist with sparse saturation at the exact moving observation scale.** The needed control is not generic regularity but source-specific anti-concentration at `Q~1/s`.

For the completed-Weil branch, a useful theorem must force something genuinely sharper than `O(1/Q)`: for example `Qm(Q)->0`, an asymptotic expansion with an `o(1/Q)` remainder, monotone or one-sided tail structure, or a direct estimate of the moving samples `m(r/s)` strong enough to replace pointwise decay.

**Boundary.** PL-315 does not assert that the actual completed-Weil mismatch contains such spikes. It blocks deductions from broad regularity classes alone. The critical half derivative itself is not crossed, and the actual eigen-equation may impose additional structure that excludes the matched construction.