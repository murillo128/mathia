# MI-014 — The exact pair-difference cancellation taxonomy closes after the one-cancellation Schur bound

**Evidence level:** supported by VIS-204, [VIS-209](../../findings/VIS-209-one-cancellation-shell-anchor-gram-kernel.md) and [VIS-211](../../findings/VIS-211-brun-titchmarsh-schur-closes-one-cancellation.md). The withdrawn VIS-210 finite-support diagonalization supplies no current evidence. No worst-start or critical-scale theorem is claimed.

VIS-204 gives an exact trichotomy for the current pair-difference shell expansion: zero cancellations produce the four-prime shells, one cancellation produces prime/prime shells, and two cancellations force only `xi=0`, the diagonal already removed from the off-diagonal problem. There is therefore no further nonzero “higher-cancellation shell” hidden inside this exact representation.

VIS-209 identifies the one-cancellation family with a positive semidefinite prime-anchor Gram kernel. For the autocorrelation taper,

`Psi_(u,t)=Q_y^(-1)(ut)^(-alpha) rho(H log(u/t))`,

and the exact energy is controlled by its coupled anchor geometry rather than individual shell counts. VIS-211 keeps those true couplings and uses weighted Schur plus translated Brun--Titchmarsh to prove, throughout every diverging strictly subcritical scale `H log y/y -> 0`,

`||Psi||_op=o(H^(-1/2))`.

Since `R_v(y,H) asymp 1/H` in the same regime, the exact VIS-209 inequality yields

`E_1=o(R_v^2)`.

Thus the complete nonzero cancellation taxonomy of the present pair-difference model is exhausted in the long-start strictly subcritical regime: the one-cancellation family is negligible, while the two-cancellation family contains no off-diagonal shell at all. Continuing to search for a “next cancellation class” inside this same expansion would invent a nonexistent object.

The unresolved directions are orthogonal to that taxonomy. First, the theorem is start-averaged/long-start; it does not exclude rare coherent starting heights. Second, the critical scale `H asymp y/log y` is outside the strictly subcritical estimate. A genuinely higher cancellation hierarchy could still appear after changing the observable to a higher moment or higher-degree expansion, but that would require a new representation dictionary and new exact shell classification rather than being a continuation of VIS-204.

**Boundary.** VIS-211 fixes `0<=alpha<1/2` and a smooth autocorrelation taper with nonnegative rapidly decaying spectrum. It proves neither worst-start uniformity nor the critical-scale estimate. The closure here is representation-specific: it says the current exact pair-difference shell has no unanalysed nonzero higher-cancellation class.