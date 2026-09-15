# MI-019 — Moving Green atoms require tail anti-concentration beyond weighted L1

**Evidence level:** exact obstruction and sufficient tail criterion from [PL-314](../../findings/PL-314-moving-diagonal-tail-threshold.md)

A weak integrated tail norm can miss the exact region sampled by a singularly moving kernel. In the Prime-Lattice stretched coordinate, the Green measure develops an atom at fixed `q=r`, while the corresponding physical logarithmic distance moves to `Q=r/s`. The normalized transfer therefore probes `m(r/s)/s`, not just the total `L^1(dQ)` mass of the mismatch.

PL-314 constructs one fixed smooth nonnegative `m in L^1(dQ)` whose sparse bumps have vanishing total mass but height `Theta(s_n)` at `Q=r/s_n`. The moving atom sees each selected bump with order-one weight, so the rank-one limit predicted from the integral alone fails. This is a genuine concentration obstruction, not a failure of the limiting Green measure.

The simple source-independent condition

`Q m(Q) -> 0`

together with `m in L^1(dQ)` is sufficient: it forces `m(r/s)=o(s)` uniformly in the tail and kills the moving-diagonal contribution. No necessity is claimed.

The reusable diagnostic is to distinguish **integrated tail smallness from anti-concentration at the moving observation scale**. A terminal operator with a concentrating atom may require pointwise decay, BV/monotonicity, a quantitative asymptotic expansion, or another source-structured estimate even when the natural weighted moment is finite. PL-314 does not yet prove that the actual completed-Weil branch satisfies any such condition.