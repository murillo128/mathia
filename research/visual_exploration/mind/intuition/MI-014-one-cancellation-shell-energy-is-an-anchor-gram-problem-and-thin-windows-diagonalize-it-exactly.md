# MI-014 — The one-cancellation anchor Gram is negligible in the strictly subcritical long-start regime

**Evidence level:** supported by VIS-204, [VIS-209](../../findings/VIS-209-one-cancellation-shell-anchor-gram-kernel.md) and [VIS-211](../../findings/VIS-211-brun-titchmarsh-schur-closes-one-cancellation.md). The withdrawn VIS-210 finite-support diagonalization supplies no current evidence. No worst-start, higher-cancellation or critical-scale theorem is claimed.

VIS-209 identifies the first surviving one-cancellation layer with one positive semidefinite prime-anchor Gram kernel. If `G` is the Gram matrix of anchor profiles, then

`E_1=4[tr(G^2)-sum_u G_(u,u)^2]`.

This exact reduction makes cross-anchor concentration, not raw shell multiplicity, the relevant quantity. The former VIS-210 claim that thin windows diagonalize the anchor family was withdrawn, so any valid estimate has to retain the true prime-ratio couplings.

VIS-211 does exactly that for the autocorrelation taper. With

`Psi_(u,t)=Q_y^(-1)(ut)^(-alpha) rho(H log(u/t))`,

weighted Schur reduces the operator norm to one translated prime-window supremum. A location-uniform Brun--Titchmarsh bound plus rapid taper decay gives, throughout every diverging strictly subcritical scale `H log y/y -> 0`,

`||Psi||_op=o(H^(-1/2))`.

Since `R_v(y,H) asymp 1/H` in the same regime, the exact VIS-209 inequality implies

`E_1=o(R_v^2)`.

The one-cancellation anchor geometry is therefore no longer merely a candidate concentration problem: **its full long-start mean-square contribution is asymptotically negligible in the whole diverging strictly subcritical window**. This closure uses the coupled kernel itself and does not resurrect any unsupported diagonalization.

The research frontier moves one layer outward. Higher cancellation classes may contain new coupled combinatorics not reduced by the same one-anchor Schur estimate. Separately, long-start mean-square suppression does not control every starting height; rare coherent starts could survive even when their density tends to zero. The critical `H asymp y/log y` scale also remains outside the theorem.

**Boundary.** VIS-211 assumes a fixed autocorrelation taper with nonnegative rapidly decaying spectrum and `0<=alpha<1/2`. It proves neither a sharper uniform `Q_y/H` Schur law nor any worst-start estimate. The durable conclusion is only that the one-cancellation shell is closed for the stated long-start strictly subcritical problem.
