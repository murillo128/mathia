# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Prove target transversality to the finite-rank forward-memory channel

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-049--NB-061 reduce the collective late quotient to compact-time arithmetic defect sectors `\mathcal K_R=\mathcal E_R\ominus\mathcal G_R`; every `\mathcal K_R` is infinite-dimensional and the canonical question is whether the visible leakage `\|P_{\mathcal G_R}J_Rh_*\|` vanishes.

NB-062 closes hidden rank loss: `\dim\mathcal G_R=R-1`, consecutive windows form a causal flag, and every new logarithmic cell adds exactly one natural innovation `C_R`. The arithmetic deformation is therefore forward memory, not missing rank.

NB-063 localizes that memory exactly. On the new cell `\mathcal X_R`, the old visible space continues through a canonical finite-rank map

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ,
\]

and

\[
\mathcal N_R=\mathcal X_R\ominus
(\operatorname{span}\{C_R\}+\operatorname{Ran}\Gamma_R)
\]

is infinite-dimensional. The channel that can retain old natural-space memory has dimension at most `R`; all target energy in `\mathcal N_R` is absorbed into the enlarged defect space with unit efficiency.

For `x_R=(J_{R+1}-J_R)h_*`, `p_R=P_{\mathcal G_R}J_Rh_*`, and `z_R=P_{\mathcal X_R^\circ}x_R-\Gamma_Rp_R`, the exact one-step capture law is

\[
\delta_R^2-\delta_{R+1}^2
=\langle z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R\rangle.
\]

The live theorem is no longer a generic frame bound. Persistent leakage requires repeated target alignment with the finite-dimensional channel `span{C_R}+Ran Gamma_R`. Prove quantitative transversality of the canonical cell `x_R`, or control `\Gamma_R` and the mismatch `z_R` strongly enough to force cumulative capture. Another rank theorem or another infinite-dimensional defect construction cannot move the bottleneck.

## Treat individual disappearance, defect abundance, rank, forward memory, and target alignment as separate gates

Late individual shifts can vanish while the collective family remains visible. Every finite window already has infinite-dimensional defect; every visible natural window already has maximal causal rank. NB-063 now shows that most of each newly opened cell is exact memory-free defect space as well.

The surviving arithmetic content is exceptionally narrow: one new innovation plus the finite-rank forward continuation of old natural traces must repeatedly align with the distinguished target. In the flat control `\Gamma_R=0` and cellwise absorption is perfect. Any claimed arithmetic obstruction should therefore be expressed through the actual forward-memory map and target mismatch, not through dimension or conditioning language alone.