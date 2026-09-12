# MI-011 — Exact local source consistency can hide an uncancelled continuation budget or a coupled reset surcharge

**Evidence level:** supported by NB-066--NB-075 and RE-068--RE-077; no operator or estimate is transferred between the lines.

Nyman--Beurling and Robin Extremal expose complementary failures of “local matching implies global harmlessness.” In both cases the useful advance is to subtract what local structure already explains, isolate the surviving global datum, and price the exact source operation that could remove it.

In Nyman, NB-066--NB-073 reduce a persistent target to a global continuation problem and separate it from local flags, branching, ordinary conditioning, and stationary prediction/feedthrough controls. NB-074 introduces the nonstationary renormalized continuation charge

`J_(R,N)=log det(A_R^(-1/2) S_(R,N) A_R^(-1/2))`.

Every persistent stable tail forces this charge to diverge for every finite horizon schedule; bounded charge along any unbounded sequence excludes the tail.

NB-075 now factorizes the charge into an exact source-facing scalar ledger. With raw continuation volume

`L_R=log(det H_(<R)/det A_R)`

and future-conditioned squared multiple correlations `beta_(R,n)`, one has

`J_(R,N)=L_R-sum_(n=R)^N[-log(1-beta_(R,n))]`.

The subtraction is load-bearing. A large raw tail or raw determinant ratio can be harmless if later innovations explain it. The surviving global datum is precisely the **uncancelled continuation volume** after all admitted future innovations have been residualized and credited once. A sufficient no-tail theorem may therefore prove that the future cancellation budget tracks `L_R` to within `O(1)`; it need not keep `L_R` itself bounded.

In Robin, RE-068--RE-073 show that endpoint matching and summable direct timing coexist with a span-free Chebyshev--Mertens source budget. RE-075 identifies the reciprocal reset currency: substantial recovery requires many new first-layer supports and physical fan span. RE-076 makes `Z-log rad(C)` a strict corrected-Chebyshev Lyapunov coordinate, and RE-077 couples the two currencies: the span required for a fixed-fraction reciprocal recovery forces an additional surcharge `>> W^(1-2b_1) w(log W)^2`.

The common discipline is therefore sharper: **do not price the unrenormalized global quantity if later source operations can cancel it for free in the target geometry. First factor out locally/futurally explained structure, then bound the residual source debt.** Nyman now does this sequentially through conditional partial correlations; Robin does it by charging reset span to a second monotone source coordinate.

**Boundary.** No Nyman determinant/correlation identity transfers to Robin prime errors, and no Robin reset surcharge transfers to Nyman continuation. NB-075 gives an exact scalar cancellation budget but not the arithmetic lower bound needed to cancel it; RE-077 gives a necessary reset surcharge but not an upper-capacity contradiction. The synthesis is staged accounting, not a shared theorem.