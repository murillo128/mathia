# MI-005 — Stable tails force a renormalized nonstationary prediction-volume charge, not merely a raw prediction/feedthrough gap

**Evidence level:** supported by NB-063--NB-074. The stationary prediction/feedthrough criterion is exact for scalar branch filters, while NB-074 gives an exact finite-dimensional necessary divergence law and sufficient no-tail certificate for the actual nonstationary causal geometry; no arithmetic boundedness theorem for that charge is proved.

NB-066--NB-071 reduce a hypothetical persistent Nyman target to a global continuation problem and rule out local memory, finite causal flags, exact branching, far-mass necessity, and ordinary global Gram conditioning as sufficient invariants. NB-072--NB-073 identify the stationary mechanism: for `psi=theta g`, the stable tail is the inner model space, the global Gram sees only the outer factor, and comparing future-prediction energy `|g(0)|^2` with causal feedthrough `|psi(0)|^2` recovers the missing inner charge.

NB-074 gives the nonstationary analogue without pretending that the actual innovations form one stationary Wold ray. For the visible Gram `A_R` and finite-future Schur complement `S_(R,N)`, define

`J_(R,N)=log det(A_R^(-1/2) S_(R,N) A_R^(-1/2))`.

The exact positive decomposition `S_(R,N)=A_R+E_(R,N)`, `E_(R,N)>=0`, makes `J_(R,N)>=0`, and the previous generalized-eigenvalue certificate satisfies

`1+Lambda_R^2 <= Xi_(R,N) <= exp(J_(R,N))`.

Hence any nonzero stable-tail vector forces `J_(R,N(R))->infinity` for **every** finite horizon schedule `N(R)>=R`. Conversely, bounded `J_(R_k,N_k)` along any unbounded sequence of windows is already enough to rule out the entire stable tail. Even the one-step quantity `J_(R,R)` is a finite determinant ratio built from the source Gram.

The determinant is not a cancellation artifact. Reverse prediction factorizes it as a sum of nonnegative coordinate charges,

`J_(R,N)=sum_(j<R) log(Pi_(j,N)^2 / PiHat_(j,R)^2)`,

where `PiHat_(j,R)` is the prediction error already visible inside the current window. This denominator is load-bearing: raw comparison with the newest-cell feedthrough `||C_j||` would mix benign finite-window forward memory with genuinely unresolved continuation. NB-074 makes the correction explicit as

`J_(R,N)=F_(R,N)-V_R`,

where `F` is global prediction relative to feedthrough and `V` is the already-visible memory charge.

On a stationary Wold ray this renormalized charge collapses exactly to the NB-073 inner charge: `J_L = -2L log|theta(0)|`. It vanishes for outer controls even at a conditioning-degenerate boundary such as `psi=1-z`, while nontrivial inner mass gives positive linear growth. Thus **conditioning, visible causal memory, unseen continuation, and stable-tail charge are separate resources**.

The arithmetic target is now scalar and finite: prove that `J_(R,N(R))` stays bounded on some unbounded sequence for a legitimate finite future schedule, or derive a comparable source estimate strong enough to control the same renormalized quantity. This would rule out the stable tail without importing an RH-equivalent target norm.

**Boundary.** Divergent `J_(R,N)` is necessary for a stable tail but not sufficient in a general nonstationary family; many moderate generalized eigenvalues can make the log determinant diverge while the largest stays bounded. The matrix certificate remains sharper. NB-074 identifies a usable sufficient no-tail criterion and the correct causal renormalization; it does not prove that the arithmetic Nyman source satisfies it.