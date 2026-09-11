# MI-007 — Robin normalization preserves the mass-one branch and critical fixed-row leakage

**Evidence level:** proved for the fixed-axis operator and fixed source/output row.

Fix `r,s>0`, `w=rs`, one parity sector `varphi_j=e_{2j+epsilon}`, `E_N=sum_{N<=j<2N}|varphi_j><varphi_j|` and `P_i=|varphi_i><varphi_i|`. The normalized Robin source is `B_w^*varphi_i=s^-1/2 g_w(L)z^(i)` with `g_w(lambda)=sqrt(sqrt(lambda)tanh(w sqrt(lambda)))` and the normalized vector `z^(i)` defined in [PF-278](../../findings/PF-278-mass-one-branch-forces-critical-normalized-fixed-row-leakage.md).

The square-root functional calculus puts Green mass arbitrarily close to the mass-one threshold. Robin inverse positivity leaves a strictly positive threshold moment `T_i^(epsilon)`, rather than cancelling it. The source is analytic across `xi=±i`, so multiplying by the square-root symbol leaves a nonremovable branch there. Its complete-axis tail `exp(-|tau|)|tau|^-3/2` becomes corridor coefficients of size `n^-3/2(log n)^-3/2` on the matching parity. Therefore

\[
\|P_iB_wE_N\|\asymp N^{-1}(\log N)^{-3/2},\qquad
N^q\|P_iB_wE_N\|\to\infty\quad(q>1).
\]

Any low-output window containing that row fails the supercritical estimate in [MI-006](MI-006-the-critical-endpoint-needs-structure-and-the-right-concentration-currency.md). Refining the same asymptotic cannot create a polynomial margin. This excludes the specified fixed-axis Robin-homotopy route, not arbitrary sheared/mixed sources or a different endpoint statistic for which critical decay suffices. The asymptotic is for fixed parameters and row; it is not a uniform statement over every simultaneous geometric limit.
