# MI-004 — The collective late Nyman quotient is a finite-window target-leakage problem, not a defect-existence problem

**Evidence level:** proved structural identities through NB-061; whether the visible natural leakage of the canonical residual vanishes remains open.

After removing the common off-critical Blaschke factor, the natural Nyman closure is `\mathcal A` and its defect space is

\[
\mathcal D=\mathcal A^\perp.
\]

NB-053--NB-058 show that raw late quotient columns shrink and that the canonical finite residual becomes invisible to every sufficiently late **individual** shifted block. The collective loophole is the family of finite-time defect sectors

\[
\mathcal K_R=\mathcal D\cap\ker U_{\log R}^*.
\]

NB-060 turns this into a one-operator generalized-root problem. With `B_2=U_{\log2}^*|_\mathcal D`, dyadic cofinality gives

\[
\mathcal K_{2^k}=\ker B_2^k,
\qquad
\mathcal K_{\rm fin}=\overline{\bigcup_{k\ge1}\ker B_2^k}.
\]

NB-061 now eliminates the unresolved existence branch. Let `J_R` be time truncation to `[0,\log R]` and set `\mathcal G_R=J_R\mathcal A`. The exact integer-log cocycle forces

\[
\mathcal G_R=\operatorname{span}\{J_RF_n:2\le n\le R\},
\qquad \dim\mathcal G_R\le R-1.
\]

Inside the infinite-dimensional window space `\mathcal E_R=\ker U_{\log R}^*`, one has

\[
\mathcal K_R=\mathcal E_R\ominus\mathcal G_R.
\]

Therefore every `\mathcal K_R` is infinite-dimensional; in particular `\ker B_2=\mathcal K_2\ne0`. Compact-time arithmetic defects are abundant already in the first dyadic window.

Abundance is still not the target theorem. For every `h\in\mathcal D`, NB-061 gives the exact orthogonal decomposition

\[
\operatorname{dist}(h,\mathcal K_R)^2
=
\|(I-J_R)h\|^2
+
\|P_{\mathcal G_R}J_Rh\|^2.
\]

For the canonical residual `h_*=Qe`, the ordinary time tail tends to zero, so

\[
h_*\in\mathcal K_{\rm fin}
\iff
\|P_{\mathcal G_R}J_Rh_*\|\to0.
\]

The moving collective problem has therefore become a **finite-window leakage problem**: at scale `R`, only at most `R-1` natural directions are visible, but those directions may still retain a fixed component of the target. Finite rank is not quantitative decay.

The reusable distinction is now sharper. Individual-column disappearance does not settle a collective span; nonzero localized kernels do not settle target approximation; and an infinite-dimensional defect sector can still fail to absorb a distinguished vector because a moving finite-dimensional complement captures it. A useful next theorem must estimate the target projection onto `\mathcal G_R` or provide an equivalent source-controlled dual certificate.

**Boundary.** NB-061 proves neither density of the generalized nullspace in the full defect space nor decay for a generic vector. It closes only the compact-time existence gate and isolates the remaining canonical-target quantity.