# MI-005 — Persistent forward-memory leakage requires square-summably collapsing target transmission

**Evidence level:** supported by the exact one-cell recursion NB-063, the target near-kernel theorem NB-064, and the finite transmission budget NB-065; no vanishing theorem for the canonical collective tail is claimed.

The late Nyman--Beurling quotient is not blocked by missing rank. NB-062--NB-063 show that the visible natural spaces form a full causal flag and that old visible information can enter the new logarithmic cell only through the finite-rank continuation map

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ.
\]

For the distinguished target, the exact gain from enlarging the window is

\[
\delta_R^2-\delta_{R+1}^2
=\langle z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R\rangle.
\]

Writing `p_R=P_{\mathcal G_R}J_Rh_*`, `u_R=p_R/\|p_R\|`, and `T_R=\Gamma_R^*\Gamma_R`, NB-064 shows that a positive limiting defect forces `u_R` into singular values tending to zero. For every fixed `eta>0`,

\[
\|E_R^{\ge\eta}u_R\|\to0.
\]

Thus bad conditioning matters only when the distinguished target occupies the bad singular directions.

NB-065 strengthens this pointwise statement to a cumulative budget. The unnormalized filtered transmission

\[
\mathfrak t_R
=\langle p_R,T_R(I+T_R)^{-1}p_R\rangle
\]

is summable with the explicit bound

\[
\sum_R\mathfrak t_R
\le 2\|h_*\|^2+2\delta_2^2.
\]

If `\delta_R\to\delta_\infty>0`, then `\|p_R\|\to\delta_\infty`, so the normalized transmission

\[
q_R=\langle u_R,T_R(I+T_R)^{-1}u_R\rangle
\]

is summable too.

This gives a moving-threshold transversality test. Suppose on scales `R\in S` a fixed fraction of target mass satisfies

\[
\|E_R^{\ge\eta_R}u_R\|\ge\kappa>0.
\]

Then persistence requires

\[
\sum_{R\in S}\frac{\eta_R^2}{1+\eta_R^2}<\infty.
\]

For `\eta_R\le1`, divergence of `\sum_{R\in S}\eta_R^2` already forces `\delta_\infty=0`. The fixed-`eta` criterion from NB-064 is only the simplest special case. A target transmission floor may decay to zero and still be sufficient if it decays too slowly to be square-summable over the scales where a fixed target fraction is transmitted.

The reusable lesson is: **persistent leakage requires not merely near-kernel tracking, but a finite accumulated target-transmission budget**. Isolated good scales can coexist with persistence when their squared floors are summable; repeated weak transversality can kill persistence without any uniform spectral gap. The right arithmetic target is therefore a nonsummable target-aware transmission lower bound, not a global condition number.

**Boundary.** The criterion is one-sided. Summable transmission does not imply persistence, and the flat control `\Gamma_R=0` has zero transmission while its target tail still vanishes. The missing theorem must supply an oracle-free lower bound for the canonical target's occupation of transmitted sectors; NB-065 does not provide that arithmetic input.