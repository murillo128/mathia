# MI-017 — A transition-band Schur complement cancels raw corridor correlations without settling the normalized angle

**Evidence level:** exact finite-section variational synthesis from [PF-342](../../findings/PF-342-sharp-physical-cutoff-forces-order-one-direct-angle-correlation.md), [PF-344](../../findings/PF-344-positive-width-transition-shorting-removes-the-leading-corridor-cost.md), and [PF-345](../../findings/PF-345-growing-exterior-edge-strips-have-exponentially-small-shorted-trace.md).

The sharp fixed physical cutoff has adjacent cosine modes on opposite sides whose completed **direct** low/high angle remains order one on infinitely many modules (PF-342). If a fixed positive-width band `T` is instead retained in the full positive seam precision `M` and eliminated *first*, its Schur complement `S=M_XX-M_XT M_TT^(-1) M_TX` obeys `<x,Sx>=min_(t in T)<x+t,M(x+t)>`.

PF-344 uses transition-mode compensators to remove the raw order-`D_n` mixed corridor term, with exponentially small edge entries relative to `D_n=L_n^(-1)(s_(n-1)^(-1)+s_n^(-1))`. PF-345 extends this to a strip of `Theta(L_n)` low/high exterior modes whose *unnormalized positive compression* has `S_1` norm `O(D_n exp(-gamma L_n))`. This proves that the sharp-cutoff witness is not invariant under the change of split.

But `S_LL` and `S_HH` shrink at the same time as `S_LH`: a bound for `||P_E S P_E||_(S_1)/D_n` is not a bound for the singular values of `S_LL^(-1/2) S_LH S_HH^(-1/2)`. Compactness or a weak trace-ideal bound on the completed angle requires estimates *after* these inverse diagonal factors and uniform passage from finite sections. A normalized edge correlation can survive even if every raw entry tends to zero relative to the former corridor energy.
