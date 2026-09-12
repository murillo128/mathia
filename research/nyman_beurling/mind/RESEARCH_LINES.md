# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Control the conditioning and target leakage of the causal finite-window innovation flag

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-049--NB-061 identify the finite repair gap, remove the common off-critical Blaschke factor, close the moving-single-shift escape, and reduce the collective late quotient to the finite-time arithmetic defect sectors

\[
\mathcal K_R=\mathcal E_R\ominus\mathcal G_R,
\qquad
\mathcal G_R=J_R\mathcal A.
\]

NB-061 proves every `\mathcal K_R` is infinite-dimensional and leaves the canonical target question as

\[
\|P_{\mathcal G_R}J_Rh_*\|\longrightarrow0,
\qquad h_*=Qe.
\]

NB-062 now closes hidden finite-window rank loss completely. With `F_1=0` and

\[
D_j=(j+1)F_{j+1}-jF_j,
\]

the exact cocycle identity writes `D_j` as a shifted shrinking-cell generator whose first visible cell is nonzero. Consequently

\[
\mathcal G_R=\operatorname{span}\{J_RD_j:1\le j<R\},
\qquad
\dim\mathcal G_R=R-1,
\]

and consecutive windows form the short exact sequence

\[
0\to\operatorname{span}\{C_R\}
\to\mathcal G_{R+1}
\xrightarrow{J_R}\mathcal G_R
\to0.
\]

Every newly opened logarithmic cell contributes exactly one independent causal innovation. The arithmetic deformation is therefore **not a rank defect**. Relative to the flat `O=1` control, the innovation count and causal order are unchanged; the new information is entirely in the forward tails of those innovations and their coupling to earlier cells.

The same basis makes the target leakage finite and explicit. Since `h_*\perp\mathcal A`, the early-window pairings are exactly the negatives of tail pairings. If `H_R` is the Gram matrix of `{J_RD_j}_{j<R}` and `b_R` the tail-induced pairing vector, then

\[
\|P_{\mathcal G_R}J_Rh_*\|^2=b_R^*H_R^{-1}b_R.
\]

The live theorem is therefore quantitative: control the triangular extension/conditioning cost strongly enough that the ordinary tail of `h_*` dominates this amplification, or find a target-specific cancellation that bypasses a full frame bound. Proving another innovation is nonzero or another localized annihilator exists no longer advances the bottleneck.

## Treat individual-shift disappearance, defect existence, finite-window rank, causal conditioning, and target leakage as separate gates

Large-ratio raw columns can be small, and every sufficiently late individual shifted block can be invisible to the canonical residual. NB-061 closes defect existence; NB-062 closes finite-window algebraic degeneracy and shows the visible natural space has maximal rank `R-1` with one innovation per cell.

A triangular family can still be arbitrarily ill-conditioned. The surviving arithmetic content is forward memory plus target alignment. Future work should attack `H_R^{-1}` against the tail-induced vector `b_R`, not rank or defect abundance.