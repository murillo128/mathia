# NB-059 — every finite-time arithmetic defect sector is trivial

**Status:** `LITERATURE+DERIVED + EXACT-CONSEQUENCE + LOCAL-DIRICHLET-RIGIDITY + DECISIVE-NEGATIVE + COLLECTIVE-TAIL-RIGIDITY`.

`NB-058` reduces the complete late off-grid quotient to a finite-time localization question in the Blaschke-deflated arithmetic defect space

\[
\mathcal D=\mathcal A^\perp,
\qquad
\mathcal A=
\overline{\operatorname{span}}\{Oq_{\log n}:n\ge2\},
\]

where

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)},
\qquad
q_a(s)=\frac{e^{-a}-e^{-as}}{s-1}.
\]

It left open whether

\[
\mathcal K_R=
\mathcal D\cap\ker U_{\log R}^*
\]

contains enough vectors to approximate the canonical defect. The answer is stronger and negative: **there are no nonzero finite-time vectors in the arithmetic defect at all.** For every finite `T>0`,

\[
\boxed{
\mathcal D\cap\ker U_T^*=\{0\}.
}
\tag{1}
\]

Equivalently, no nonzero vector of `A^perp` has a Paley--Wiener representative supported in a bounded interval. Combining (1) with `NB-058`, for every integer `R>=2`,

\[
\boxed{
\mathcal K_R=\{0\},
\qquad
\mathcal T_R=\mathcal D.
}
\tag{2}
\]

Thus the complete collective late quotient does not become smaller as the cutoff moves outward: at every finite cutoff its closed span is already the **entire arithmetic defect space**. For the canonical limiting residual `h_*=Qe`,

\[
\boxed{
\|P_{\mathcal T_R}h_*\|^2
=\|h_*\|^2
=\delta_{\rm def}^2
\qquad(R\ge2).
}
\tag{3}
\]

This is compatible with `NB-057`, which proves vanishing leakage into every sufficiently late *individual* shifted block. The arithmetic Nyman defect is therefore an exact example where one-dimensional angles vanish while the closed span of all late directions remains maximal.

## 1. Compact Paley--Wiener support makes a defect entire

Use the Paley--Wiener normalization of `NB-056`--`NB-058`, under which the right-shift semigroup on `L^2(0,\infty)` is unitarily equivalent to

\[
(U_tF)(s)=e^{-t(s-1/2)}F(s)
\]

on `H^2(Re s>1/2)`. If

\[
h\in\ker U_T^*,
\]

then its inverse Paley--Wiener representative is supported in `[0,T]`. Hence, up to the fixed unitary normalization,

\[
h(s)=\int_0^T \psi(t)e^{-t(s-1/2)}\,dt
\tag{4}
\]

for some `psi in L^2(0,T)`. Because the integration interval is compact, Cauchy--Schwarz gives locally uniform domination for every complex `s`; differentiation under the integral is legitimate to all orders. Therefore

\[
\boxed{h\text{ extends to an entire function of }s.}
\tag{5}
\]

No zeta estimate enters this step.

## 2. Remultiplication by Burnol's Blaschke factor returns to the standard natural Nyman space

Let

\[
F_a=Oq_a.
\]

For a natural grid point `a=log n`, Burnol's inner factor gives the exact identity

\[
\begin{aligned}
B(s)F_{\log n}(s)
&=
B(s)\frac{s-1}{s}\frac{\zeta(s)}{B(s)}
\frac{n^{-1}-n^{-s}}{s-1}\\
&=
\frac{\zeta(s)}s\bigl(n^{-1}-n^{-s}\bigr).
\end{aligned}
\tag{6}
\]

Up to an irrelevant sign, the right side is the usual Hardy/Mellin Báez--Duarte generator. If `mathcal N` denotes the closed natural Nyman span in the half-plane Hardy space, then

\[
\boxed{\mathcal N=B\mathcal A.}
\tag{7}
\]

Multiplication by the inner function `B` is an isometry. Consequently, for every `h in D=A^perp`,

\[
\langle Bh,Ba\rangle=\langle h,a\rangle=0
\qquad(a\in\mathcal A),
\]

so

\[
\boxed{Bh\in\mathcal N^\perp.}
\tag{8}
\]

Burnol's Blaschke product is meromorphic beyond the critical boundary, with possible reflected poles at `1-conj(rho)` for zeros `rho` with `Re rho>1/2`. Those poles lie strictly to the left of `Re s=1/2`. Hence at any fixed finite boundary point

\[
s_0=\frac12+i\tau_0
\]

there is a neighborhood across the boundary on which `B` is holomorphic. Together with (5), this implies that `Bh` extends holomorphically through every such finite boundary point.

## 3. Local Dirichlet rigidity forces the compact-time defect to vanish

Calderaro, Manzur, Noor and Santos prove, for the disk Hardy realization of the Báez--Duarte natural Nyman space `N`, that for every boundary point `zeta in T`,

\[
\boxed{
N^\perp\cap\mathcal D_{\delta_\zeta}=\{0\}.
}
\tag{9}
\]

Here `D_(delta_zeta)` is the corresponding local Dirichlet space. Their local characterization is

\[
f\in\mathcal D_{\delta_\zeta}
\quad\Longleftrightarrow\quad
f=a+(z-\zeta)g,
\qquad g\in H^2.
\tag{10}
\]

The standard Cayley unitary carries the half-plane natural Nyman span `mathcal N` to their disk space, up to harmless nonzero generator normalizations. Choose any finite half-plane boundary point whose disk image is not the Cayley pole. By the preceding section, the Cayley image `f` of `Bh` extends holomorphically across the corresponding `zeta`.

Such an `H^2` function automatically satisfies (10): take `a=f(zeta)` and

\[
g(z)=\frac{f(z)-f(\zeta)}{z-\zeta}.
\tag{11}
\]

Near `zeta`, holomorphic extendability makes `g` bounded; away from that neighborhood the denominator is bounded from zero, so the `H^2` boundary norm of `g` is controlled by that of `f` plus a constant. Thus `g in H^2`, hence `f in D_(delta_zeta)`.

But (8) puts the same `f` in `N^perp`. Equation (9) therefore forces `f=0`, hence `Bh=0`. Since the nonzero inner function `B` cannot annihilate a nonzero analytic function identically,

\[
\boxed{h=0.}
\tag{12}
\]

This proves (1).

## 4. The `NB-058` collective tail is therefore maximal at every finite scale

For integer `R>=2`, `NB-058` proved

\[
\mathcal K_R
=
\mathcal D\cap\ker U_{\log R}^*
=
\mathcal D\cap\mathcal T_R^\perp
\]

and

\[
\mathcal T_R=
\overline{\operatorname{Ran}(Q U_{\log R}|_{\mathcal D})}.
\]

Equation (1) gives `K_R={0}`. Since `T_R` is a closed subspace of `D` and its orthogonal complement inside `D` is zero,

\[
\boxed{\mathcal T_R=\mathcal D.}
\tag{13}
\]

The abstract approximation identity from `NB-058` collapses accordingly:

\[
\inf_{u\in\mathcal A,\ h\in\mathcal K_R}
\|e-u-h\|^2
=
\inf_{u\in\mathcal A}\|e-u\|^2
=
\delta_{\rm def}^2.
\tag{14}
\]

Thus finite-time dual defects cannot provide a cheaper certificate for the late quotient. Any nonzero arithmetic defect is necessarily nonlocal in Paley--Wiener time, and arbitrarily late off-grid quotient directions collectively reconstruct all of it.

This gives a sharp separation between the two tail notions now present in the line:

- `NB-057`: every sufficiently late **individual** shifted block becomes asymptotically blind to the canonical finite residual;
- `NB-059`: the closed span of **all** shifts beyond any finite cutoff equals the full limiting defect space.

There is no contradiction: a complete family can consist entirely of vectors having individually small angle with a fixed target.

## 5. The unit-outer control fails precisely at this arithmetic rigidity gate

For the `O=1` control of `NB-056`, finite-time defect spaces are large: `K_R^(0)` is the direct sum of all early logarithmic cell-detail spaces, and their union exhausts the flat defect. That is why the flat canonical target has the cubic collective tail

\[
\|P_{\mathcal T_R^{(0)}}Q_0e\|^2
=\frac1{36R^3}+O(R^{-4}).
\]

Equation (1) shows that this localization mechanism does **not** survive the actual zeta source. The difference is not a perturbative deformation of the flat cell geometry. The natural arithmetic orthogonal complement has a boundary-regularity rigidity absent from the unit-outer model: any compact-time vector would become an orthogonal Nyman function with local Dirichlet regularity, which is forbidden by (9).

This also resolves the accepted clue `CLUE-early-cell-adjoint-duals-certify-target-tail` negatively in its specified form. An `h_R` orthogonal to both `A` and `T_R` must lie in `K_R`, hence must be zero. The proposed adjoint/cell-moment lift therefore cannot produce a nontrivial early-time arithmetic dual. With `h_R=0`, its certificate reduces to approximating `e` directly by `A`, which is the original deflated Nyman approximation problem rather than a new tail mechanism.

## 6. Prior-art and audit boundary

The load-bearing external input is Theorem 10 of Francisco Calderaro, Juan Manzur, Waleed Noor and Charles F. Santos, *Orthogonality questions in the Hardy space related to zeta-zeros* (arXiv:2203.05030), together with their local Dirichlet characterization. Their theorem already proves the strong boundary singularity of every nonzero natural-Nyman orthogonal vector; **that theorem is prior art and no novelty is claimed for it**. Burnol's Blaschke factorization and the half-plane Nyman generators are likewise standard and already anchored in this line.

The line-local derivation is the combination of that regularity theorem with the exact deflated dictionary (6)--(8) and the `NB-058` compact-time duality. A targeted literature search located the Calderaro--Manzur--Noor--Santos theorem as the decisive neighboring result; no source was found stating the specific consequence (1)--(3) for the Blaschke-deflated late off-grid quotient. No priority claim is made for that consequence.

The decisive audit points are exact rather than numerical:

1. verify the generator normalization in (6), noting that an overall sign does not change the closed span;
2. verify that compact Paley--Wiener support gives the entire extension (5);
3. verify that Burnol's `B` is holomorphic across at least one finite point of the critical boundary;
4. verify that the Cayley image is the natural Hardy Nyman family to which (9) applies;
5. verify the local Dirichlet implication (10)--(11).

Failure of any of these bridges would invalidate (1). The unit-outer matched control is not a counterexample because it is not the natural Nyman orthogonal complement and does not satisfy the local Dirichlet rigidity theorem.

## Consequence for the research line

`NB-058` posed a dichotomy: finite-time arithmetic defects might exhaust the canonical residual, or the localized sectors might be too small. `NB-059` closes that dichotomy at the strongest possible negative endpoint:

\[
\boxed{
\text{every finite-time arithmetic defect sector is zero.}
}
\]

Therefore the collective late-tail route cannot be controlled by constructing compact-time dual certificates. Future progress on the deflated repair gap must use genuinely nonlocal defect structure, a different target functional, or a quantitative relation among the late directions themselves. Raw tail decay and individual-shift invisibility remain true but cannot be upgraded to collective target-tail decay by finite-time localization.