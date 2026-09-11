# MI-004 — The collective late Nyman quotient is exactly a finite-time defect problem

**Evidence level:** proved structural identities in NB-049--NB-058; whether the arithmetic defect is exhausted by finite-time sectors remains open.

After removing the common off-critical Blaschke factor, the natural Nyman closure is `\mathcal A` and its defect space is

\[
\mathcal D=\mathcal A^\perp.
\]

NB-053--NB-057 show that raw late quotient columns shrink and that the actual canonical finite residual becomes invisible to every sufficiently late **individual** shifted block. NB-058 identifies what remains when all late directions are taken collectively.

For `R>=2`, let

\[
\mathcal T_R=
\overline{\operatorname{span}}\{v_a:a\ge\log R\},
\qquad
V_R=Q U_{\log R}|_{\mathcal D}.
\]

The late quotient tail is exactly

\[
\mathcal T_R=\overline{\operatorname{Ran}V_R}.
\]

Its orthogonal complement inside the arithmetic defect is

\[
\mathcal K_R
=\mathcal D\cap\mathcal T_R^\perp
=\mathcal D\cap\ker U_{\log R}^*.
\]

Under the Paley--Wiener representation, this has the concrete meaning

\[
\mathcal K_R=
\{h\in\mathcal D:
\operatorname{supp}(\mathcal P^{-1}h)\subseteq[0,\log R]\}.
\]

So the surviving multichannel question is no longer vague “conditioning of many weak columns.” It is whether the **actual arithmetic defect space contains enough compact-time vectors**.

For the canonical limiting residual `h_*=Qe`, the collective late target mass satisfies the exact dual identity

\[
\|P_{\mathcal T_R}h_*\|^2
=
\operatorname{dist}(h_*,\mathcal K_R)^2.
\]

Hence the late-tail contribution tends to zero iff `h_*` lies in the norm closure of defect vectors with finite Paley--Wiener support. The unit-outer control realizes this mechanism explicitly and gives its familiar `1/(36R^3)+O(R^{-4})` tail through finite-cell detail spaces.

This sharply separates individual and collective disappearance. It is consistent with all current results that `\mathcal K_R={0}` for every finite `R`, in which case `\mathcal T_R=\mathcal D` for every cutoff even though every sufficiently late individual block has vanishing projection against the canonical moving residual.

The next source theorem should therefore construct quantitative compact-time arithmetic defects approximating `h_*`, or prove that these localized sectors are too small. Another one-column estimate cannot decide the repair distance.

**Boundary.** This reduction does not prove that finite-time defects are dense, that the collective tail vanishes, or that the flat cubic rate transfers to zeta. It identifies the exact source-specific object whose geometry decides those questions.