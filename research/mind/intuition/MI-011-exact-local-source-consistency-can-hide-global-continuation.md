# MI-011 — Exact local source consistency can hide a renormalized continuation charge or a coupled reset surcharge

**Evidence level:** supported by NB-066--NB-074 and RE-068--RE-077; no operator or estimate is transferred between the lines.

Nyman--Beurling and Robin Extremal expose complementary failures of “local matching implies global harmlessness.” In both cases the useful advance is to identify and price the surviving global datum rather than strengthen local matching.

In Nyman, NB-066--NB-072 make the stable-tail obstruction a global continuation problem and show that local flags, branching and ordinary conditioning can all miss it. NB-073 identifies the stationary inner defect as a prediction/feedthrough gap. NB-074 then supplies the correct nonstationary renormalization for the actual causal geometry:

`J_(R,N)=log det(A_R^(-1/2) S_(R,N) A_R^(-1/2))`.

This charge is nonnegative and factorizes as a sum of nonnegative gaps between full finite-future prediction error and the prediction error already visible inside the current window. Every persistent stable tail forces `J_(R,N(R))->infinity` for every finite horizon schedule; bounded charge on any unbounded sequence is enough to exclude the tail. The visible-memory normalization is essential: raw prediction relative to newest-cell feedthrough can grow for benign causal memory that is not a continuation defect.

In Robin, RE-068--RE-073 show that endpoint matching and summable direct timing coexist with a span-free Chebyshev--Mertens source budget. RE-075 identifies the reciprocal reset currency: substantial recovery requires many new first-layer supports and physical fan span. RE-076 makes `Z-log rad(C)` a strict corrected-Chebyshev Lyapunov coordinate through arbitrary packets.

RE-077 couples those two currencies quantitatively. The corrected coordinate is coercive in physical span, so the span required for a fixed-fraction reciprocal recovery forces an additional surcharge `>> W^(1-2b_1)w(log W)^2`. Repairing one source ledger necessarily pushes the other farther in its costly direction; higher-layer packet complexity cannot subsidize the bill.

The common discipline is concrete: **after exact local consistency, subtract what is already explained locally, isolate the genuinely global survivor, and price the exact source operation that could remove it.** Nyman subtracts visible forward memory before measuring unseen continuation volume. Robin prices reciprocal recovery in support births and then charges the induced physical span to a second monotone source coordinate.

**Boundary.** No Nyman determinant/prediction identity transfers to Robin prime errors, and no Robin reset surcharge transfers to Nyman continuation. NB-074 gives a sufficient no-tail criterion but not its arithmetic boundedness; RE-077 gives a necessary reset surcharge but not an upper-capacity contradiction. The synthesis is staged source/destination accounting, not a shared theorem.