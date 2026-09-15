# MI-037 — Source-incidence cost is a redundancy/scale tradeoff whose live boundary is second-order

**Evidence level:** exact/literature-derived source-incidence consequence from [MC-312](../../findings/MC-312-generalized-hamming-source-redundancy-scale-tradeoff.md), with generic coding boundary from [MC-313](../../findings/MC-313-generalized-griesmer-erasure-list-boundary.md) and second-order sharpening from [MC-314](../../findings/MC-314-second-order-source-scale-near-capacity-erasure-boundary.md).

For fixed lower-prime representatives of `R` independent endpoint generators, let `A` be the binary source-incidence matrix, `n` its number of source coordinates, `Z` its largest source prime, and `d_t` the generalized Hamming weights of its row space. The source-cut theorem gives

`d_t log Z >= (1-(2+o(1))(R+1)/2^t) log y - O(1)`.

MC-313 shows why the first-order consequence is not yet arithmetic. At `t_R=ceil(2 log_2(R+1))`, generic full-length `[2R,R]` binary codes can realize `d_t=R-O(R/log R)` across the relevant hierarchy. Thus near-half erasure resilience at coarse precision is compatible with ordinary code geometry.

MC-314 isolates the next currency. If

`log Z <= ((1+eta_R)/R) log y`,

then at `t_R`

`R-d_(t_R) <= R eta_R/(1+eta_R)+2+o(1)`.

At the exact equal-share scale `eta_R=0`, the allowed defect is only `2+o(1)`. More generally, a source-scale error `eta_R=o(1/log R)` forces `R-d_t=o(R/log R)`, beyond the slack supplied by the current generic matched-control theorem.

The reusable lesson is that **source scale and hereditary redundancy couple at second order**. Saying only `Z=y^((1+o(1))/R)` loses the quantity that determines whether the arithmetic demand separates from the generic control. The endpoint argument needs a quantified `eta_R`, not another first-order redundancy count.

This changes the proof obligation without overclaiming it. One may prove a sufficiently sharp arithmetic source-prime scale, show that actual Legendre-incidence columns cannot realize the resulting near-capacity erasure profile, or find a joint generalized-weight constraint absent from generic codes. MC-314 does **not** prove that arbitrary binary codes cannot achieve the sharper constant-defect profile; it proves only that the arithmetic requirement has moved beyond what MC-313's generic construction currently guarantees.

**Boundary.** The representation code remains an abstraction of fixed lower-prime representatives. None of MC-312--MC-314 proves that the arithmetic source realizes a generic code, nor that generic codes fail the second-order demand. The result prices the next discriminating scale; it does not estimate `M(x)` or close the Möbius endpoint.