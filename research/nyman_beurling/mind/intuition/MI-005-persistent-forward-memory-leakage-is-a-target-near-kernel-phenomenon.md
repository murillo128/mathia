# MI-005 — A persistent Nyman tail would be one fixed locally natural mode with square-summable transmission and divergent global extension cost

**Evidence level:** supported by the exact one-cell recursion NB-063, target near-kernel theorem NB-064, finite transmission budget NB-065, and stable-tail/extension theorem NB-066; no vanishing theorem for the canonical collective tail is claimed.

The late Nyman--Beurling quotient is not blocked by missing rank. NB-062--NB-063 show that the visible natural spaces form a full causal flag and that old visible information can enter the new logarithmic cell only through the finite-rank continuation map

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ.
\]

NB-064--NB-065 show that a positive limiting defect forces the normalized visible target into singular values tending to zero and gives its filtered transmission a finite total budget. If a fixed target fraction repeatedly lies above moving floors `eta_R`, persistence requires the corresponding squared floors to be summable. Thus no uniform singular gap is needed to kill persistence; a nonsummable weak transversality floor would already suffice.

NB-066 identifies the object that would have to realize this pathology. With

\[
\mathcal T_\infty
=\mathcal D\ominus\mathcal K_{\rm fin},
\]

one has the exact characterization

\[
\boxed{
\mathcal T_\infty
=\{t\in\mathcal D:J_Rt\in\mathcal G_R\text{ for every }R\}.
}
\]

For the canonical residual `h_*`, the moving tail projections converge strongly to

\[
t_*=P_{\mathcal T_\infty}h_*,
\qquad
\delta_\infty=\|t_*\|.
\]

Hence, on the persistence branch, the normalized visible targets converge to one **fixed nonzero stable-tail mode** rather than rotating indefinitely among unrelated near-kernel directions.

That fixed mode is locally indistinguishable from the natural space at every finite window but globally orthogonal to it. If `t in T_infinity` is nonzero and `E_R(t)` is the least future norm of a genuine natural vector `a` satisfying `J_Ra=J_Rt`, then global orthogonality gives

\[
\boxed{
\mathfrak E_R(t)\,\|(I-J_R)t\|
\ge\|J_Rt\|^2.
}
\]

Because `J_Rt->t` and `(I-J_R)t->0`, every exact natural continuation of the finite trace pays

\[
\mathfrak E_R(t)\to\infty.
\]

Thus persistence is stronger than bad local conditioning: it requires **perfect finite-window naturality together with catastrophic nonuniformity of all compatible global continuations**.

This yields a target-free source criterion. Let `Lambda_R` be the worst minimal future-extension norm over unit vectors in `G_R`. A nonzero stable tail forces `Lambda_R->infinity` along the full tail. Therefore a bounded `Lambda_R` on any unbounded sequence of windows implies `T_infinity={0}` and kills every possible stable tail at once. This is strictly stronger in scope than controlling the canonical target alone.

NB-066 also removes the spectral filter from the fixed-mode transmission statement. Writing `g_R=J_Rt`, the exact graph decomposition gives

\[
(J_{R+1}-J_R)t=\Gamma_Rg_R+\beta_RC_R
\]

orthogonally, and the cell energies telescope. For nonzero `t`,

\[
\sum_R\left\|\Gamma_R\frac{g_R}{\|g_R\|}\right\|^2<\infty.
\]

A persistent stable mode is therefore an **unfiltered square-summable approximate-kernel trajectory**, even while its globally natural continuation cost diverges.

The reusable lesson is sharper than “persistent leakage requires near-kernel tracking.” **Local exact representability, one-step transmission, and globally bounded continuation are different resources.** A vector can be represented exactly on every finite observation window while no compatible global realization remains norm-controlled. The remaining arithmetic task can attack either side: force enough target transmission to violate square summability, or prove a uniform/recurring causal-extension bound that prevents such a locally natural but globally singular mode.

**Boundary.** The criteria are one-sided. Square-summable transmission does not imply persistence, and the flat control can have zero transmission with no stable tail. NB-066 does not prove bounded causal-extension constants for the canonical arithmetic spaces; it identifies that bound as a sufficient source-only route. No RH conclusion follows without that missing arithmetic estimate.