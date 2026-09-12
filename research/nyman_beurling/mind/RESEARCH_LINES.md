# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Exclude target-bearing near-kernel modes of the forward-memory map

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`, `MI-005-persistent-forward-memory-leakage-is-a-target-near-kernel-phenomenon`.

NB-049--NB-063 reduce the collective late quotient to a finite-rank forward-memory channel. Every compact-time defect sector is infinite-dimensional, every visible natural window has maximal causal rank, and the newly opened cell splits into an infinite-dimensional memory-free defect sector plus `span{C_R}+Ran Gamma_R`. The exact one-step capture law is

\[
\delta_R^2-\delta_{R+1}^2
=\langle z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R\rangle.
\]

NB-064 turns the remaining alignment possibility into a sharp spectral condition. If a nonzero collective tail persists and `p_R=P_{\mathcal G_R}J_Rh_*`, then the normalized target direction `u_R=p_R/\|p_R\|` must leave every singular sector of `Gamma_R` bounded away from zero. For every fixed `eta>0`,

\[
\|E_R^{\ge\eta}u_R\|\to0,
\]

and there are unit vectors `v_R` with `\|u_R-v_R\|\to0` and `\|\Gamma_Rv_R\|\to0`. Persistent leakage therefore requires the **distinguished target itself** to become an approximate right-kernel direction of the canonical forward-memory map.

The live theorem is now target-aware and one-sided. It is enough to prove that along an unbounded sequence a fixed fraction of `u_R` lies in a singular sector transmitted by at least some fixed `eta>0`; that already forces `\delta_R\to0`. A uniform lower singular bound for all of `\mathcal G_R` is much stronger than necessary, while an upper bound on `\|\Gamma_R\|` is not the intrinsic quantity at all.

## Treat individual disappearance, defect abundance, rank, forward memory, bad singular directions, and target occupation as separate gates

Late individual shifts can vanish while the collective family remains visible. Every finite window already has infinite-dimensional defect; every visible natural window already has maximal causal rank. NB-064 further shows that merely having poorly transmitted singular directions is cheap: they obstruct only if the canonical target projection asymptotically tracks them.

Near-kernel tracking is necessary for persistent leakage, not sufficient. In the flat control `\Gamma_R=0`, every visible direction is a kernel direction while the collective target tail still vanishes. Future progress must therefore prove arithmetic transversality of the actual `p_R`, or otherwise show that the canonical target cannot follow the moving near-kernel subspaces.