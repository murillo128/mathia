# MI-042 — Fixed polynomial spectral smoothing preserves the Korobov--Vinogradov envelope class

**Evidence level:** exact asymptotic synthesis from [VIS-341](../../findings/VIS-341-vk-scale-stable-under-finite-spectral-smoothing.md). The statement concerns the standard zero-free-width/truncation optimization with fixed polynomial tail power; it is not a pointwise theorem for Wang's `Q` and does not identify Wang's multiplier with any particular truncation exponent.

Write the Korobov--Vinogradov width in the usual form

`nu(t)=A (log t)^(-2/3) (log log t)^(-1/3)`

at large `t`. If a standard explicit-formula balance has a fixed polynomial tail `t^(-r)`, the corresponding exponent is governed by

`Omega_r(u)=inf_t {u nu(t)+r log t}`.

For every fixed `r>0`, optimization gives the same subpower scale

`Omega_r(u) ~ C_A r^(2/5) u^(3/5) (log u)^(-1/5)`,

with only the leading constant changed by `r^(2/5)`. A finite increase in polynomial high-frequency decay therefore does not alter the characteristic `3/5,-1/5` Korobov--Vinogradov exponent pair.

This is the correct control for one tempting Wang interpretation. VIS-333 shows a one-order high-frequency attenuation in the exact summatory multiplier, but treating that only as one additional fixed inverse-frequency factor cannot by itself generate a new PNT envelope class. A genuine asymptotic gain must use information not represented by the same zero-free width plus a fixed polynomial tail: for example source-specific signed cancellation, nonstationary frequency migration with growing effective order, or another quantitative property of the normalized theta remainder.

The distinction is important because a better constant and a better asymptotic class are different resources. A finite smoothing order may still improve constants or finite ranges, yet it does not explain a new exponent. Conversely a mechanism with an `r` that grows with the source scale lies outside VIS-341 and must pay whatever conditioning, localization or derivative cost accompanies that growth.

**Boundary.** VIS-341 does not prove a stronger or weaker bound for `G`, `Q`, or the prime-counting error, and it does not prove that Wang literally replaces a `t^(-1)` tail by `t^(-2)`. It classifies only the fixed-`r` optimization. Any proposed growing-order or source-specific cancellation mechanism requires a separate theorem and must still survive the exact inverse/derivative ledger from VIS-333--VIS-340.
