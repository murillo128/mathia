# NB-057 — canonical finite residuals cannot sustain large-shift semigroup leakage

**Status:** `EXACT-DERIVED + NESTED-PROJECTION + JOINT-FINITE-SECTION/LARGE-SHIFT + TARGET-ANGLE + NEGATIVE/METHOD-BOUNDARY`.

`NB-053` proves that every fixed defect in the orthogonal complement of the deflated natural Nyman space becomes asymptotically invisible to off-grid semigroup probes at large shift, but deliberately leaves a loophole: a finite-section residual changes with the section, and strong continuity of the shift semigroup is not uniform on the unit sphere. The present finding closes that loophole for the **canonical nested finite-section residuals themselves**.

Let

\[
\mathcal A_N:=\operatorname{span}\{\phi_{1/n}:2\le n\le N\},
\qquad
\mathcal A:=\overline{\bigcup_{N\ge2}\mathcal A_N},
\tag{1}
\]

inside `H^2(Re s>1/2)`, with orthogonal projections `P_N` and `P`. For the canonical target

\[
e(s)=k_1(s)=\frac1s,
\tag{2}
\]

define

\[
h_N=e-P_Ne,
\qquad
h_*=e-Pe,
\qquad
\delta_N=\|h_N\|,
\qquad
\delta_*=\|h_*\|=\delta_{\rm def}.
\tag{3}
\]

Then the finite residual has the orthogonal decomposition

\[
\boxed{
h_N=h_*+a_N,
\qquad
a_N:=(P-P_N)e\in\mathcal A\cap\mathcal A_N^\perp,
}
\tag{4}
\]

with

\[
\boxed{
\|a_N\|^2=\delta_N^2-\delta_*^2\longrightarrow0.
}
\tag{5}
\]

For the shift semigroup

\[
(U_tF)(s)=e^{-t(s-1/2)}F(s),
\tag{6}
\]

`NB-053` gives exact blindness of `h_*` on the integer-log grid and vectorwise large-shift decay off that grid. Combining those facts with (4)--(5) yields two uniform finite-section statements.

First,

\[
\boxed{
\sup_{m\ge1}
\|P U_{\log m}^*h_N\|
\le
\sqrt{\delta_N^2-\delta_*^2}
\longrightarrow0.
}
\tag{7}
\]

Second, if

\[
\gamma_T:=
\log\!\left(1+\frac1{\lfloor e^T\rfloor}\right)
\tag{8}
\]

and

\[
\omega_{h_*}(r):=
\sup_{0\le u\le r}\|U_u^*h_*-h_*\|,
\tag{9}
\]

then

\[
\boxed{
\sup_{t\ge T}\|P U_t^*h_N\|
\le
\omega_{h_*}(\gamma_T)
+
\sqrt{\delta_N^2-\delta_*^2}.
}
\tag{10}
\]

Consequently,

\[
\boxed{
\lim_{\substack{N\to\infty\\T\to\infty}}
\sup_{t\ge T}\|P U_t^*h_N\|=0.
}
\tag{11}
\]

In particular, for **every** pair of sequences `N_j -> infinity` and `t_j -> infinity`,

\[
\boxed{
\|P U_{t_j}^*h_{N_j}\|\longrightarrow0.
}
\tag{12}
\]

Thus the changing finite residual cannot evade the fixed-vector conclusion of `NB-053` merely by moving through vectors with progressively worse individual continuity moduli. The actual canonical residual sequence is forced by nested projection to converge strongly to the single limiting defect, and that convergence is uniform enough to survive arbitrary simultaneous passage to large section and large shift.

## 1. Nested projection gives an exact residual decomposition

Because the spaces `A_N` are nested and their union is dense in `A`, the orthogonal projections converge strongly,

\[
P_Nx\longrightarrow Px
\qquad(x\in H^2).
\tag{13}
\]

Apply this only to the fixed target `e`. Since `Pe` and `P_Ne` both lie in `A`,

\[
a_N=(P-P_N)e\in\mathcal A.
\tag{14}
\]

For every `v in A_N`,

\[
\langle a_N,v\rangle
=\langle Pe,v\rangle-\langle P_Ne,v\rangle
=\langle e,v\rangle-\langle e,v\rangle=0,
\tag{15}
\]

so `a_N in A_N^perp`. Meanwhile `h_* in A^perp`, hence `h_* perpendicular a_N`. Equation (4) follows from

\[
e-P_Ne=(e-Pe)+(Pe-P_Ne),
\tag{16}
\]

and Pythagoras gives

\[
\delta_N^2=\delta_*^2+\|a_N\|^2.
\tag{17}
\]

Strong convergence in (13) gives `||a_N||->0`, proving (5). No RH assumption is used: if the limiting defect is nonzero, the finite residuals converge to it; if it is zero, they converge to zero.

## 2. The entire integer-log grid becomes uniformly blind

`NB-053` proves

\[
P U_{\log m}^*h_*=0
\qquad(m\ge1).
\tag{18}
\]

Using (4), contractivity of `U_t^*`, and `||P||=1`,

\[
\begin{aligned}
\|P U_{\log m}^*h_N\|
&=\|P U_{\log m}^*a_N\|\\
&\le\|a_N\|.
\end{aligned}
\tag{19}
\]

The right side is independent of `m`. Taking the supremum over the **whole** multiplicative grid and using (5) proves (7).

This is stronger than checking each fixed integer dilation separately. Even if the grid index `m=m_N` tends arbitrarily quickly to infinity with the section size, the finite residual's visible component in the full natural space is at most the finite-to-infinite projection gap `sqrt(delta_N^2-delta_*^2)`.

## 3. Large off-grid shifts vanish jointly with the section limit

For the fixed limiting defect, `NB-053` gives

\[
\sup_{t\ge T}\|P U_t^*h_*\|
\le\omega_{h_*}(\gamma_T),
\tag{20}
\]

and strong continuity of the adjoint shift orbit gives

\[
\omega_{h_*}(r)\longrightarrow0
\qquad(r\downarrow0).
\tag{21}
\]

Since `gamma_T->0`, the first term on the right side of (10) tends to zero as `T->infinity`. For the moving correction,

\[
\sup_{t\ge T}\|P U_t^*a_N\|
\le\|a_N\|
=
\sqrt{\delta_N^2-\delta_*^2}.
\tag{22}
\]

Adding (20) and (22) proves (10). Given `epsilon>0`, choose `T_0` so that the first term is below `epsilon/2`, then choose `N_0` so that the second is below `epsilon/2`. The resulting estimate holds simultaneously for every `T>=T_0`, `N>=N_0`, and `t>=T`; this is exactly (11), and (12) is immediate.

The point is that no uniform modulus of continuity on the unit sphere is needed. The finite residuals do not explore the whole unit sphere: they converge strongly to the one canonical limiting residual, and the difference is controlled by the exact projection-distance gap (17).

## 4. Target-angle interpretation

Because `U_t` is an isometry, the orthogonal projection onto the shifted closed space `U_t A` is

\[
P_{U_t\mathcal A}=U_t P U_t^*.
\tag{23}
\]

Therefore

\[
\boxed{
\|P_{U_t\mathcal A}h_N\|
=
\|P U_t^*h_N\|.
}
\tag{24}
\]

Equations (7) and (11) are consequently target-angle statements, not merely semigroup-norm statements. The canonical finite residual becomes uniformly orthogonal to every integer-dilated copy of the full natural space as `N` grows, and it becomes uniformly orthogonal to each sufficiently late continuously shifted copy once both section and shift are large.

This narrows the live bridge after `NB-055`--`NB-056`. A persistent finite-section repair signal cannot be maintained by choosing one shifted natural block farther and farther into the large-ratio tail while simultaneously increasing the section. Any surviving obstruction must instead live at bounded/moderate shift, or arise from **collective geometry across many shifted blocks** rather than a single late block.

## 5. What this does not control

Equation (11) is not operator-norm decay on `A^perp`. `NB-053`'s warning remains valid for arbitrary unit vectors: the shift semigroup is not norm-continuous at zero, so one cannot replace the canonical sequence `h_N` by an arbitrary moving sequence in the orthogonal complement.

Nor does smallness of every individual late-shift projection imply smallness of the projection onto

\[
\overline{\operatorname{span}}\{U_t\mathcal A:t\ge T\}.
\tag{25}
\]

Many individually weak directions can collectively span a target-bearing sector. `NB-056` already shows why normalized multicolumn geometry and target occupation must be treated separately from raw one-column size. The present result therefore does **not** resolve `CLUE-early-cell-adjoint-duals-certify-target-tail` and does not estimate the full late quotient projector.

What it does remove is a specific escape route left open in `NB-053`: canonical finite residuals cannot preserve a positive single-shift leakage merely because their continuity moduli vary with `N`. The only large-ratio loophole left is genuinely multichannel/conditioning-based.

## 6. Prior-art boundary and frontier

The Hilbert-space input behind (13)--(17) is standard: projections onto an increasing family of closed subspaces converge strongly to the projection onto the closure of their union. Continuity of orthogonal projections has also been studied directly in the Nyman--Beurling setting, and the discrete semigroup formulation is classical in the Báez--Duarte/Bagchi framework. A targeted literature audit did not locate the specific joint estimate (10) for the Blaschke-deflated canonical finite residuals, but no priority claim follows from that bounded search.

No external result beyond those standard ingredients is load-bearing, so `SOURCES.md` is unchanged. The durable line-local delta is the combination of the exact nested residual decomposition with `NB-053`'s logarithmic-grid blindness: it upgrades fixed-witness large-shift decay to the actual moving finite-section target residuals and quantifies the correction by `sqrt(delta_N^2-delta_*^2)`.

The next useful theorem must therefore control one of two genuinely stronger objects: a bounded/moderate-ratio target sector, or the collective normalized span of many late quotient directions. The proposed early-cell adjoint-dual clue attacks the first/dual formulation; alternatively, a source-specific comparison between the actual zeta-outer quotient blocks and the stationary Brownian-bridge control of `NB-056` would attack the second.