# MI-018 — Stretched Volterra amplitude selection is a rank-one corner matching problem

**Evidence level:** exact consequence of [PL-310](../../findings/PL-310-stretched-fractional-green-limit-is-a-volterra-plus-diagonal-fixed-profile.md)--[PL-313](../../findings/PL-313-corner-to-outer-rank-one-transfer.md). The limiting regular range and the compact-corner Green transfer are exact. No complete finite-`s` expansion for the actual completed-Weil eigenbranch, amplitude formula, arithmetic sign or RH consequence is claimed.

PL-310 shows that the small-order fractional Green geometry has a universal fixed-`r` limit with one singular homogeneous profile `C/sqrt(e^(2r)-1)`. PL-311--PL-312 show that regular outer corrections have exactly one solvability obstruction: for `C^1` forcing, `(I-T)f=h` is solvable in the continuous gauge iff `h(0)=0`. Once that scalar is cancelled, the regular correction is unique.

PL-313 identifies how the physical `r=O(s)` corner reaches this one-dimensional cokernel. If `m` is a compact physical mismatch and `F_(s,m)=s^(-1/2)m(x_s(.))`, then locally for `r>0`,

`(1/sqrt(s))(T_s F_(s,m))(r) -> e^(-r) M_+(m)`,
`M_+(m)=integral_(-1)^1 m(y)/(1-y) dy`.

Reflection gives `M_-(m)=integral m(y)/(1+y)dy`. The full compact corner shape is therefore compressed to one weighted scalar per endpoint, carried by the very outer direction whose endpoint value violates the PL-312 range condition.

This is the missing structural match: the physical corner does not feed an uncontrolled functional family into the outer problem. At first regular order it communicates through a **rank-one endpoint channel**. Under a justified expansion with no other endpoint-active `O(sqrt(s))` term, solvability would force a scalar balance between `M_±` and the completed source.

The remaining difficulty is not conceptual but genuinely analytic. The actual singular profile behaves like `C/sqrt(2r)`; in the overlap `r=sQ` it corresponds to a physical `Q^-1/2` boundary law. Before `M_±` is finite for the actual mismatch, the amplitude `C` must be matched strongly enough that this leading boundary tail cancels and the residual lies in `L^1(dQ)`. Then all other `O(sqrt(s))` errors must be shown not to create an additional endpoint-active scalar.

**Boundary.** PL-313 proves the transfer for compact physical mismatches and identifies the canonical functional; it does not prove the weighted decomposition of the actual eigenbranch or the illustrative identity `M_+(m)=2g_+`. The arithmetic sign remains completely open after matching.
