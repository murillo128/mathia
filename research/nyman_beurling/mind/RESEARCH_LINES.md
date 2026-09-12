# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Exclude square-summably collapsing target transmission in the forward-memory map

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-049--NB-063 reduce the collective late quotient to a finite-rank forward-memory channel. Every compact-time defect sector is infinite-dimensional, every visible natural window has maximal causal rank, and the newly opened cell splits into an infinite-dimensional memory-free defect sector plus `span{C_R}+Ran Gamma_R`. The exact one-step capture law is

\[
\delta_R^2-\delta_{R+1}^2
=\langle z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R\rangle.
\]

NB-064 shows that if a nonzero collective tail persists and `p_R=P_{\mathcal G_R}J_Rh_*`, then the normalized target direction `u_R=p_R/\|p_R\|` must asymptotically leave every fixed singular sector of `\Gamma_R` bounded away from zero. Persistent leakage therefore requires the **distinguished target itself** to track approximate right-kernel directions.

NB-065 strengthens this from a pointwise condition to a finite total transmission budget. With `T_R=\Gamma_R^*\Gamma_R`,

\[
\mathfrak t_R
=\langle p_R,T_R(I+T_R)^{-1}p_R\rangle
\]

satisfies

\[
\sum_R\mathfrak t_R<\infty
\]

unconditionally. On the persistence branch `\delta_\infty>0`, the normalized quantities

\[
q_R=\langle u_R,T_R(I+T_R)^{-1}u_R\rangle
\]

are summable as well.

Consequently the live transversality theorem can be weaker than a fixed singular gap. If, on a set of scales `S`, a fixed fraction `\kappa` of `u_R` lies in singular values at least `\eta_R`, persistence forces

\[
\sum_{R\in S}\frac{\eta_R^2}{1+\eta_R^2}<\infty.
\]

For `\eta_R\le1`, it is enough to prove a **nonsummable squared transmission floor**

\[
\sum_{R\in S}\eta_R^2=\infty
\]

together with the fixed target-mass lower bound. For example, an eventually recurring floor `\eta_R\gg R^{-\alpha}` rules out persistence whenever `\alpha\le1/2`.

The remaining theorem is therefore quantitative target transversality: show that the canonical target cannot track the moving near-kernel subspaces with transmission collapsing at a square-summable rate across every sufficiently rich set of cells. A uniform lower singular bound on the whole visible space remains far stronger than necessary.

## Treat individual disappearance, defect abundance, rank, forward memory, bad singular directions, target occupation, and accumulated transmission as separate gates

Late individual shifts can vanish while the collective family remains visible. Every finite window already has infinite-dimensional defect; every visible natural window already has maximal causal rank. Merely having poorly transmitted singular directions is cheap: they obstruct only if the canonical target occupies them.

NB-065 adds a cumulative gate. Even target occupation of shrinking singular sectors is not enough for persistence unless the corresponding transmission floors collapse quickly enough for their squared strengths to be summable over the recurrence scales. Sparse good scales can be harmless if their transmission budget is summable; repeated weak transversality can be decisive if its total squared budget diverges.

Near-kernel tracking remains necessary, not sufficient. In the flat control `\Gamma_R=0`, every visible direction is a kernel direction while the collective target tail still vanishes. Future progress must therefore establish an oracle-free arithmetic lower bound on the target's **accumulated transmitted mass**, not merely existence or absence of abstract small singular values.