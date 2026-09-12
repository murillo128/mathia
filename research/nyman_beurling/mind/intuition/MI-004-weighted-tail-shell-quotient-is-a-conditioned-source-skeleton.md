# MI-004 — Each new Nyman log cell is mostly exact defect space; only a finite-rank memory channel can retain target leakage

**Evidence level:** proved structural identities through NB-063; decay of the canonical visible leakage remains open.

After removing the common off-critical Blaschke factor, NB-053--NB-060 show that raw late quotient columns shrink and that the canonical residual becomes invisible to every sufficiently late **individual** shifted block. NB-061 reduces the collective loophole to finite-time defect sectors

\[
\mathcal K_R=\mathcal E_R\ominus\mathcal G_R,
\qquad
\mathcal G_R=J_R\mathcal A,
\]

with every `\mathcal K_R` infinite-dimensional. For the canonical residual `h_*=Qe`,

\[
\operatorname{dist}(h_*,\mathcal K_R)^2
=\|(I-J_R)h_*\|^2+\|P_{\mathcal G_R}J_Rh_*\|^2.
\]

NB-062 shows that the visible natural spaces form an exact causal flag. With `D_j=(j+1)F_{j+1}-jF_j`,

\[
\mathcal G_R=\operatorname{span}\{J_RD_j:1\le j<R\},
\qquad \dim\mathcal G_R=R-1,
\]

and each new logarithmic cell contributes one nonzero innovation `C_R`.

NB-063 resolves what happens **inside one newly opened cell**. Let

\[
\mathcal X_R=(J_{R+1}-J_R)H^2,
\qquad
\mathcal X_R^\circ=\mathcal X_R\ominus\operatorname{span}\{C_R\}.
\]

There is a canonical finite-rank forward-memory map

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ
\]

such that

\[
\mathcal G_{R+1}
=\{g+\Gamma_Rg:g\in\mathcal G_R\}
\oplus\operatorname{span}\{C_R\}.
\]

Consequently the memory-free cell subspace

\[
\mathcal N_R
=\mathcal X_R\ominus
\bigl(\operatorname{span}\{C_R\}+\operatorname{Ran}\Gamma_R\bigr)
\]

is infinite-dimensional, while the channel capable of carrying old natural-space memory has dimension at most `R`. Thus every new cell is not merely accompanied by some defect: **all but a finite-rank memory channel is exact defect space immediately**.

For the target, write `p_R=P_{\mathcal G_R}J_Rh_*`, `x_R=(J_{R+1}-J_R)h_*`, and `x_R^\circ=P_{\mathcal X_R^\circ}x_R`. With `z_R=x_R^\circ-\Gamma_Rp_R`, NB-063 gives the exact capture law

\[
\boxed{
\delta_R^2-\delta_{R+1}^2
=\left\langle z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R\right\rangle,
}
\]

where `\delta_R=dist(h_*,\mathcal K_R)`, and in particular

\[
\delta_R^2-\delta_{R+1}^2\ge\|P_{\mathcal N_R}x_R\|^2.
\]

So target energy outside the finite-rank memory channel is captured with **no conditioning loss at all**. Persistent leakage cannot be explained by generic ill-conditioning of a large Gram matrix. Scale after scale, the distinguished target cell must stay aligned with `span{C_R}+Ran Gamma_R`, and the old visible component must couple through `Gamma_R` so that `z_R` remains small or is strongly attenuated.

The flat `O=1` control makes the distinction exact: `\Gamma_R=0`, the canonical target cell lies in the memory-free sector, and every new-cell contribution is absorbed perfectly. The arithmetic deformation therefore lives precisely in forward memory plus the new-innovation component, not in rank, defect abundance, or causal ordering.

The useful next theorem is correspondingly local and target-aware: prove transversality of the canonical `x_R` to the source-generated memory channel, or obtain quantitative control of `\Gamma_R` and `z_R` strong enough to force summable/vanishing leakage. A dimension bound alone cannot do this because one distinguished vector may lie entirely inside a finite-dimensional channel.

**Boundary.** NB-063 proves no decay of the leakage, no uniform bound on `||\Gamma_R||`, no lower angle for the target, and no improved Nyman approximation rate. It replaces the global phrase “bad conditioning may amplify tails” by an exact one-cell mechanism and energy recursion.