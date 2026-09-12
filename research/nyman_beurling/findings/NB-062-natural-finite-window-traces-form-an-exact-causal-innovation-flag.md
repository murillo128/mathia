# NB-062 — natural finite-window traces form an exact causal innovation flag

**Status:** `EXACT-DERIVED + FULL-FINITE-WINDOW-RANK + CAUSAL-TRIANGULAR-BASIS + ONE-DIMENSIONAL-CELL-INNOVATIONS + TARGET-PAIRING-REDUCTION + FLAT-CONTROL + METHOD-ADVANCE`.

`NB-061` proves that the natural Nyman space visible before time `log R` is finite-dimensional,

\[
\mathcal G_R=J_R\mathcal A
=\operatorname{span}\{J_RF_n:2\le n\le R\},
\qquad \dim\mathcal G_R\le R-1,
\tag{1}
\]

where

\[
F_n:=F_{\log n}=Oq_{\log n},
\qquad
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)},
\qquad
\mathcal A=\overline{\operatorname{span}}\{F_n:n\ge2\}.
\tag{2}
\]

The rank bound could still have hidden exact dependencies, and therefore left open whether part of the finite-window difficulty was merely algebraic degeneracy. It is not. The rank bound is always sharp for the actual Blaschke-deflated arithmetic source, and the growing trace spaces form an exact causal flag with one new independent constraint on every logarithmic cell.

For `j>=1`, put `F_1:=0`,

\[
\Delta_j:=\log\frac{j+1}{j},
\qquad
D_j:=(j+1)F_{j+1}-jF_j.
\tag{3}
\]

Then

\[
\boxed{
D_j=\frac{j+1}{\sqrt j}\,
U_{\log j}F_{\Delta_j}.
}
\tag{4}
\]

Thus the Paley--Wiener representative of `D_j` starts at time `log j`. Its first-cell component

\[
C_j:=(J_{j+1}-J_j)D_j=J_{j+1}D_j
\in L^2\!\left([\log j,\log(j+1)]\right)
\tag{5}
\]

is nonzero. Consequently, for every integer `R>=2`,

\[
\boxed{
\mathcal G_R
=
\operatorname{span}\{J_RD_j:1\le j<R\},
\qquad
\dim\mathcal G_R=R-1.
}
\tag{6}
\]

Even more precisely, restriction to the previous window gives a short exact sequence

\[
\boxed{
0\longrightarrow
\operatorname{span}\{C_R\}
\longrightarrow
\mathcal G_{R+1}
\xrightarrow{\ J_R\ }
\mathcal G_R
\longrightarrow0.
}
\tag{7}
\]

So every new integer-log window contributes **exactly one** new visible natural direction, supported entirely on its newest cell. The arithmetic deformation from the flat `O=1` control is therefore not a rank defect. It lives in how each causal innovation continues into later cells and couples to the older ones.

For the canonical defect `h_*=Qe\in\mathcal A^\perp`, the same basis also gives an exact target-aware finite system. Since every `D_j` lies in `A`,

\[
\boxed{
\langle J_Rh_*,J_RD_j\rangle
=-\langle (I-J_R)h_*,(I-J_R)D_j\rangle
\qquad(1\le j<R).
}
\tag{8}
\]

Hence all finite-window target pairings are induced by **tail overlap of globally orthogonal vectors**. If `H_R` is the positive-definite Gram matrix of the basis `{J_RD_j}_{j<R}` and `b_R` is the vector in (8), then

\[
\boxed{
\|P_{\mathcal G_R}J_Rh_*\|^2
=b_R^*H_R^{-1}b_R.
}
\tag{9}
\]

This does not prove the leakage in `NB-061` tends to zero. It identifies its remaining carrier more sharply: exact rank loss is absent, while the only possible obstruction is quantitative conditioning of the causal trace flag together with the tail-induced target data.

## 1. Adjacent weighted differences are shifted shrinking-cell generators

For the continuous kernel

\[
q_a(s)=\frac{e^{-a}-e^{-as}}{s-1},
\qquad F_a:=Oq_a,
\tag{10}
\]

the natural point `a=log n` gives

\[
q_{\log n}(s)=\frac{n^{-1}-n^{-s}}{s-1}.
\tag{11}
\]

A direct subtraction yields

\[
\begin{aligned}
(j+1)q_{\log(j+1)}-jq_{\log j}
&=
\frac{j^{1-s}-(j+1)^{1-s}}{s-1}\\
&=(j+1)j^{-s}q_{\Delta_j}(s).
\end{aligned}
\tag{12}
\]

Since

\[
U_{\log j}F(s)=j^{1/2-s}F(s),
\tag{13}
\]

multiplying (12) by `O` proves (4). In Paley--Wiener coordinates `U_(log j)` is right translation by `log j`, so

\[
\operatorname{supp}D_j\subseteq[\log j,\infty).
\tag{14}
\]

The first-cell component in (5) cannot vanish. Indeed, if `C_j=0`, then (14) would force `D_j` to be supported after `log(j+1)`. Equation (4) would then force `F_(Delta_j)` to have a positive Paley--Wiener delay of at least `Delta_j`.

But `F_a=Oq_a` has no positive exponential delay. Burnol's deflated factor `O` is outer, while

\[
q_a\longleftrightarrow
 e^{-a+t/2}\mathbf1_{[0,a]}(t)
\tag{15}
\]

has left support endpoint zero. Equivalently, `q_a` has no positive exponential inner factor, and multiplication by the outer factor cannot create one. Thus

\[
\boxed{C_j\ne0\qquad(j\ge1).}
\tag{16}
\]

This use of outerness is only a support statement. No inverse of `O`, bounded or otherwise, is introduced.

## 2. The finite-window upper rank bound is always attained

The differences telescope:

\[
\sum_{j=1}^{n-1}D_j=nF_n,
\qquad n\ge2.
\tag{17}
\]

Therefore the algebraic spans agree,

\[
\operatorname{span}\{F_2,\ldots,F_R\}
=
\operatorname{span}\{D_1,\ldots,D_{R-1}\},
\tag{18}
\]

and `NB-061` gives the first equality in (6) after applying `J_R`.

To prove independence, suppose

\[
\sum_{j=1}^{R-1}c_jJ_RD_j=0
\tag{19}
\]

and choose the smallest `j_0` with `c_{j_0}\ne0`. On the cell

\[
I_{j_0}=[\log j_0,\log(j_0+1)],
\tag{20}
\]

every `D_j` with `j>j_0` vanishes by (14), while there is no term with smaller nonzero index by construction. Restriction of (19) to `I_{j_0}` therefore gives

\[
c_{j_0}C_{j_0}=0,
\tag{21}
\]

contradicting (16). Hence all coefficients vanish, proving

\[
\dim\mathcal G_R=R-1.
\tag{22}
\]

Combined with `NB-061`, this sharpens the defect-space statement to

\[
\boxed{
\operatorname{codim}_{\mathcal E_R}\mathcal K_R=R-1,
\qquad
\mathcal K_R=\mathcal E_R\ominus\mathcal G_R.
}
\tag{23}
\]

The compact-time defect sector remains infinite-dimensional, but it is cut out by exactly `R-1` independent natural constraints, not merely at most `R-1`.

## 3. Every new logarithmic cell contributes one and only one innovation

The restriction map

\[
r_R:=J_R|_{\mathcal G_{R+1}}:\mathcal G_{R+1}\to\mathcal G_R
\tag{24}
\]

is surjective: if `g=J_Ra` with `a in A`, then `J_(R+1)a in G_(R+1)` and

\[
r_R(J_{R+1}a)=J_Ra=g.
\tag{25}
\]

Equations (22) at `R` and `R+1` give

\[
\dim\ker r_R=1.
\tag{26}
\]

By (14), `J_RD_R=0`, while by (16)

\[
J_{R+1}D_R=C_R\ne0.
\tag{27}
\]

Thus `C_R` spans that kernel and proves (7).

This is an exact causal filtration. It is stronger than ordinary global linear independence of the natural generators: it says that after Blaschke deflation and restriction to every finite Paley--Wiener window, the constraints arrive one at a time and the new quotient direction is localized entirely in the newly opened cell.

The statement is also compatible with arbitrarily bad numerical conditioning. A triangular family can have every diagonal innovation nonzero while its smallest singular value tends rapidly to zero. Equations (6)--(7) therefore remove exact dependence as an explanation for the live `NB-061` leakage problem without pretending to solve its quantitative angle problem.

## 4. Canonical target data come entirely from truncating global orthogonality

Take

\[
h_*=Qe\in\mathcal D=\mathcal A^\perp.
\tag{28}
\]

For every `j`, `D_j in A`, hence

\[
\langle h_*,D_j\rangle=0.
\tag{29}
\]

Splitting both vectors at time `log R` gives

\[
0=
\langle J_Rh_*,J_RD_j\rangle
+
\langle(I-J_R)h_*,(I-J_R)D_j\rangle,
\tag{30}
\]

which is (8). Since (6) is a basis, its Gram matrix `H_R` is strictly positive definite and the standard finite projection formula gives (9).

Equation (9) is not a new oracle. The vector `b_R` still depends on the canonical residual, and `H_R^{-1}` can amplify very small tail pairings. Its value is structural: after `NB-061`, the target leakage cannot be blamed on hidden rank loss, and after (8) it cannot be viewed as independent early-window data either. It is precisely the result of globally vanishing target pairings being split across a causal finite-time boundary.

A useful next estimate would therefore control the **triangular extension/conditioning cost** of the basis `J_RD_j` strongly enough to dominate the ordinary tail norm `||(I-J_R)h_*||`. Merely proving `C_j!=0`, or bounding raw norms of the `D_j`, is insufficient.

## 5. The unit-outer model identifies the arithmetic deformation

For `O=1`, Paley--Wiener gives

\[
nq_{\log n}
\longleftrightarrow
 e^{t/2}\mathbf1_{[0,\log n]}(t).
\tag{31}
\]

Therefore

\[
D_j^{(0)}
\longleftrightarrow
 e^{t/2}\mathbf1_{I_j}(t).
\tag{32}
\]

The innovations have no forward tail at all, different cells are orthogonal, and

\[
\mathcal G_R^{(0)}
=
\bigoplus_{j<R}
\operatorname{span}\{D_j^{(0)}\}.
\tag{33}
\]

This recovers the exact flat decomposition used in `NB-056` and `NB-061`. For the actual arithmetic factor, write

\[
J_RD_j=C_j+T_{j,R},
\qquad
T_{j,R}:=(J_R-J_{j+1})D_j.
\tag{34}
\]

The `C_j` occupy disjoint cells, while all cross-cell coupling comes from the forward tails `T_{j,R}`. Thus the passage from the flat control to the actual deflated source preserves the number and causal ordering of finite-window constraints exactly; what changes is their **forward memory**.

This is the sharper mechanism boundary left by the finding. To improve (9), one must control those forward tails relative to the nonzero diagonal innovations, or obtain a target-specific cancellation that bypasses full conditioning. The flat cubic target law cannot be transferred merely from full rank or causal triangularity.

## 6. Prior-art and falsification boundary

The integer-dilation Báez--Duarte family, its linear independence phenomena, Burnol's Hardy/Blaschke factorization, and Paley--Wiener translation are classical. A targeted literature search found standard treatments of the discrete Nyman--Beurling strengthening and explicit statements of linear independence for related natural sawtooth families. No novelty is claimed for global linear independence itself.

The line-local delta is the conjunction of the exact adjacent weighted differences (3)--(4) with the finite-window identity of `NB-061`: after Blaschke deflation they furnish a causal triangular basis for every visible trace space, force the upper rank bound to be sharp, and identify the restriction kernel between consecutive windows as the single newest-cell innovation. The same basis turns the canonical target leakage into the tail-induced finite system (8)--(9). The bounded search did not locate this exact finite-window flag formulation, but no priority claim is made.

No new specialized external estimate is load-bearing beyond sources already anchored in `SOURCES.md`, so that file remains unchanged.

The falsification boundary is strict. This finding does **not** prove a uniform lower bound for `||C_j||`, a frame bound for the triangular family, decay of `b_R^*H_R^{-1}b_R`, density of the generalized kernels, or any improvement of the Nyman distance. It proves that the live obstruction is quantitative rather than algebraic: **every finite window contains the maximal possible number of independent natural constraints, arriving as one causal innovation per logarithmic cell, and only their forward coupling and target alignment remain capable of sustaining the `NB-061` leakage.**