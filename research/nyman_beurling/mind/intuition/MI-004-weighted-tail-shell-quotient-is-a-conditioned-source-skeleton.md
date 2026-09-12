# MI-004 — The late Nyman quotient is a causal conditioning and target-leakage problem, not a rank problem

**Evidence level:** proved structural identities through NB-062; whether the visible natural leakage of the canonical residual vanishes remains open.

After removing the common off-critical Blaschke factor, the natural Nyman closure is `\mathcal A` and its defect space is

\[
\mathcal D=\mathcal A^\perp.
\]

NB-053--NB-060 show that raw late quotient columns shrink and that the canonical residual becomes invisible to every sufficiently late **individual** shifted block, while the collective loophole is the family of finite-time defect sectors

\[
\mathcal K_R=\mathcal D\cap\ker U_{\log R}^*.
\]

NB-061 eliminates defect existence as a bottleneck. Let `J_R` truncate to `[0,\log R]`, `\mathcal E_R=\ker U_{\log R}^*`, and `\mathcal G_R=J_R\mathcal A`. Then

\[
\mathcal K_R=\mathcal E_R\ominus\mathcal G_R,
\]

and every `\mathcal K_R` is infinite-dimensional. For the canonical residual `h_*=Qe`,

\[
\operatorname{dist}(h_*,\mathcal K_R)^2
=\|(I-J_R)h_*\|^2
+\|P_{\mathcal G_R}J_Rh_*\|^2.
\]

The ordinary tail tends to zero, so the live question is the visible target leakage.

NB-062 closes the next possible escape: hidden algebraic dependence in `\mathcal G_R`. Define

\[
D_j=(j+1)F_{j+1}-jF_j.
\]

The integer-log cocycle gives an exact shifted-cell representation for `D_j`, and outerness of the deflated factor guarantees that its first cell

\[
C_j=(J_{j+1}-J_j)D_j
\]

is nonzero. The family is causally triangular, hence

\[
\boxed{
\mathcal G_R=\operatorname{span}\{J_RD_j:1\le j<R\},
\qquad \dim\mathcal G_R=R-1.
}
\]

Moreover each new window adds exactly one innovation:

\[
0\to\operatorname{span}\{C_R\}
\to\mathcal G_{R+1}
\xrightarrow{J_R}\mathcal G_R
\to0.
\]

Thus the actual arithmetic source and the flat `O=1` control have the same innovation count and causal ordering. In the flat case the innovations are orthogonal cell indicators; in the arithmetic case they acquire **forward tails**. The source deformation lives in this forward memory, not in a missing rank.

The target pairing also becomes exact. Global orthogonality `h_*\perp D_j` implies

\[
\langle J_Rh_*,J_RD_j\rangle
=-\langle(I-J_R)h_*,(I-J_R)D_j\rangle.
\]

If `H_R` is the positive-definite Gram matrix of `{J_RD_j}_{j<R}` and `b_R` this tail-induced pairing vector, then

\[
\boxed{
\|P_{\mathcal G_R}J_Rh_*\|^2=b_R^*H_R^{-1}b_R.
}
\]

This identifies the remaining mechanism precisely: very small tail pairings can still be amplified by poor triangular conditioning. A useful theorem must control the forward-tail/innovation ratio strongly enough to bound `H_R^{-1}` in the target direction, or exploit cancellation special to `b_R`. Full rank, nonzero `C_j`, and abundance of compact defects are no longer informative enough.

**Boundary.** NB-062 proves no uniform frame bound, no lower bound on innovation size, no decay of `b_R^*H_R^{-1}b_R`, and no Nyman-distance estimate. It converts the live obstruction from algebraic rank to quantitative causal conditioning plus target alignment.