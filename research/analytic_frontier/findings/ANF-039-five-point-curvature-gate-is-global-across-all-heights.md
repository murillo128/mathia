# ANF-039 — the five-point curvature gate is global across all heights

**Status:** `EXACT-DERIVED + FIVE-POINT-COMPLEX-CLOSURE + GLOBAL-CURVATURE-GATE + CENTRAL-NOTCH-SURVIVOR`. `ANF-037` reduces the first genuinely new complex geometry — one conjugate pair plus three real anchors — to

\[
G_J(y)=A_y+3\inf_{t\in\mathbb R}L_y(t),
\]

and identifies the infinitesimal coefficient

\[
m_5(J)=2K_J(0)+3\inf_{t\in\mathbb R}K_J(t),
\qquad
K_J(t)=\int \alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha.
\]

`ANF-038` proves `m_5(J_MT)>0.0078` for the exact Montgomery--Taylor spectrum and therefore clears only a sufficiently small-height neighborhood. The finite-height problem left there is in fact illusory for this geometry. For every nonnegative compact-band spectrum,

\[
\boxed{
G_J(y)\ge 2\pi^2y^2m_5(J)
\qquad(y>0).
}
\tag{1}
\]

Consequently

\[
\boxed{
G_J(y)\ge0\text{ for every }y>0
\quad\Longleftrightarrow\quad
m_5(J)\ge0.
}
\tag{2}
\]

Thus the second-spectral-moment curvature test from `ANF-037` is not merely an infinitesimal necessary condition: it is the **complete all-height criterion** for the one-pair-plus-three-real five-point layer. In particular the equality case `m_5(J)=0`, previously left as a fourth-order boundary, is automatically stable rather than undecided.

Applied to `ANF-038`, this proves that `J_MT` is strictly collapse-dominating for this complete five-point geometry at every positive conjugate height. More importantly, the central-notch separator `J_s=J_MT-s\phi_\eta` from `ANF-034` can be chosen to retain its strict finite-real gain while also passing this entire complex layer globally, not merely near `y=0`.

## 1. Exact defect and the quantity that must be controlled

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\]

with `J` real, even, continuous and compactly supported. Following `ANF-037`, set

\[
c_y(\alpha)=\cosh(2\pi\alpha y),
\]

\[
L_y(t)=\int J(\alpha)(c_y(\alpha)-1)
\cos(2\pi\alpha t)\,d\alpha,
\tag{3}
\]

and

\[
A_y=\int J(\alpha)(c_y(\alpha)^2-1)\,d\alpha.
\tag{4}
\]

For

\[
W=\{x+iy,x-iy,r_1,r_2,r_3\}
\]

and its real-part collapse `R(W)`, write `t_j=r_j-x`. Then `ANF-037` gives exactly

\[
E_F(W)-E_F(R(W))
=4\left(A_y+\sum_{j=1}^3L_y(t_j)\right).
\tag{5}
\]

Because the three real anchors can approach the same minimizing displacement while remaining distinct,

\[
\inf_{r_1,r_2,r_3}
\frac{E_F(W)-E_F(R(W))}{4}
=A_y+3\ell_y,
\qquad
\ell_y:=\inf_tL_y(t).
\tag{6}
\]

Hence the complete collapse question for this geometry is exactly the sign of `G_J(y)=A_y+3\ell_y`.

Since `A_y` is independent of `t`,

\[
G_J(y)
=\inf_{t\in\mathbb R}\bigl(A_y+3L_y(t)\bigr).
\tag{7}
\]

The point is therefore to control the single-anchor expression uniformly in `t`; no finite-height minimization is actually needed once its power-series structure is exposed.

## 2. Every nonlinear height correction has the favorable sign

Fix `y>0` and `t\in\mathbb R`, and for each frequency put

\[
u:=2\pi\alpha y,
\qquad
v:=2\pi\alpha t.
\]

Since `c_y^2-1=\sinh^2u`, equations (3)--(4) give

\[
A_y+3L_y(t)
=\int J(\alpha)
\left[
\sinh^2u+3(\cosh u-1)\cos v
\right]d\alpha.
\tag{8}
\]

Use the absolutely convergent even-power expansions

\[
\sinh^2u
=\frac{\cosh(2u)-1}{2}
=\sum_{n\ge1}
\frac{2^{2n-1}u^{2n}}{(2n)!},
\tag{9}
\]

and

\[
\cosh u-1
=\sum_{n\ge1}\frac{u^{2n}}{(2n)!}.
\tag{10}
\]

Substitution into the bracket in (8) gives the exact pointwise identity

\[
\sinh^2u+3(\cosh u-1)\cos v
=
\sum_{n\ge1}
\frac{u^{2n}}{(2n)!}
\left(2^{2n-1}+3\cos v\right).
\tag{11}
\]

The `n=1` term is

\[
\frac{u^2}{2}(2+3\cos v).
\tag{12}
\]

Every higher term is nonnegative **pointwise**, because for `n\ge2`

\[
2^{2n-1}+3\cos v
\ge 2^{2n-1}-3
\ge 8-3
=5>0.
\tag{13}
\]

Therefore

\[
\boxed{
\sinh^2u+3(\cosh u-1)\cos v
\ge
\frac{u^2}{2}(2+3\cos v)
}
\tag{14}
\]

for all real `u,v`. Multiplying by the nonnegative spectrum `J(\alpha)` and integrating yields

\[
\begin{aligned}
A_y+3L_y(t)
&\ge
2\pi^2y^2
\int \alpha^2J(\alpha)
\left(2+3\cos(2\pi\alpha t)\right)d\alpha\\
&=
\boxed{
2\pi^2y^2\left(2K_J(0)+3K_J(t)\right).
}
\end{aligned}
\tag{15}
\]

Taking the infimum over `t` proves (1).

The mechanism is stronger than a Taylor remainder estimate. Vertical displacement contributes higher even powers with coefficient `2^{2n-1}` through `sinh^2u`, whereas the potentially destructive real-anchor interference contributes only coefficient `3`. Starting already at the quartic term, the vertical self-energy coefficient is at least `8`, so **every correction beyond the quadratic curvature layer can only improve the collapse inequality**.

## 3. The curvature gate is necessary and sufficient

If `m_5(J)\ge0`, equation (1) immediately gives

\[
G_J(y)\ge0
\qquad\text{for every }y>0.
\tag{16}
\]

This includes the boundary case `m_5(J)=0`: the higher-order terms in (11) cannot reverse the sign.

Conversely, if `m_5(J)<0`, choose a real `t_*` with

\[
2K_J(0)+3K_J(t_*)<0.
\]

Compact spectral support makes the expansion in `y` uniform under the integral, so from (8)--(12)

\[
\frac{A_y+3L_y(t_*)}{2\pi^2y^2}
\longrightarrow
2K_J(0)+3K_J(t_*)<0
\qquad(y\downarrow0).
\tag{17}
\]

Hence `A_y+3L_y(t_*)<0` for all sufficiently small positive `y`, and therefore by (7)

\[
G_J(y)<0
\]

there. This is the instability direction already isolated in `ANF-037`. Combining both implications proves (2).

Thus the first five-point geometry has no separate finite-height phase transition. Once the quadratic curvature profile passes, all nonlinear height corrections have the favorable sign; once it fails, arbitrarily small height already detects the failure.

## 4. Montgomery--Taylor is globally stable in this complete geometry

`ANF-038` proves rigorously that

\[
m_5(J_{\rm MT})>0.0078.
\tag{18}
\]

Substituting (18) into (1) gives the explicit all-height margin

\[
\boxed{
G_{J_{\rm MT}}(y)
>2\pi^2(0.0078)y^2
>0
\qquad(y>0).
}
\tag{19}
\]

Therefore every five-point configuration consisting of one conjugate pair and three distinct real anchors has energy at least that of its real-part collapse for the exact Montgomery--Taylor spectrum, at **every** conjugate height. The finite-height optimization proposed at the end of `ANF-038` is unnecessary for this geometry.

Because the simple-real-point count and total cardinality are unchanged by this collapse, the same conclusion holds at the affine counting level: no configuration of this form adds a stronger universal affine constraint than its real multiplicity counterpart.

This does not yet clear all five-point conjugation-invariant configurations. Besides the all-real case, cardinality five has one further genuinely coupled pattern: **two conjugate pairs plus one real point**. The argument above does not factor that geometry into three independent copies of one Fourier minimum, so it remains the next five-point complex gate.

## 5. The central-notch separator survives the whole layer

For the explicit separator family

\[
J_s=J_{\rm MT}-s\phi_\eta
\]

constructed in `ANF-034`, `ANF-038` proves

\[
m_5(J_s)
\ge
m_5(J_{\rm MT})-
\frac56s b_\eta\eta^3.
\tag{20}
\]

Since `0<b_\eta\le1`, the additional choice

\[
s\eta^3<0.009
\tag{21}
\]

implies

\[
m_5(J_s)>0.0078-0.0075=0.0003.
\tag{22}
\]

`ANF-034` allows `s>0` to be chosen arbitrarily small after the admissible notch width is fixed, so (21) is compatible with its strict uniform finite-real separation. Applying (1) now upgrades the local conclusion of `ANF-038` to

\[
\boxed{
G_{J_s}(y)
>2\pi^2(0.0003)y^2
>0
\qquad\text{for every }y>0.
}
\tag{23}
\]

Hence there exist explicit central-notch spectra that simultaneously

\[
\frac{C(J_s)}{q_{\rm real}(J_s)}<C_{\rm MT}
\]

and dominate the real-part collapse throughout the **entire one-conjugate-pair-plus-three-real five-point layer**. The separator therefore survives the first sharp complex geometry from `ANF-036` not only infinitesimally but globally.

This materially narrows the universal affine scalar branch. A complex falsifier for such a chosen notch can no longer come from any cardinality-four configuration (`ANF-036`) or from the complete one-pair-plus-three-real cardinality-five family. The cheapest unresolved geometry is now two conjugate pairs plus one real point, where the two vertical amplifications interact rather than contributing through independent anchor terms.

## 6. Prior art, audit boundary, and next test

The only external analytic input remains the classical positive Fourier--Laplace representation already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides and used throughout `ANF-012`, `ANF-035`--`ANF-038`. A targeted search of positive-definite strip functions and Fourier--Laplace representations found the expected representation theory but no result matching the finite-configuration equivalence (2). No publication-level novelty claim is made, and no new source entry is required.

The proof is exact and has no numerical component. Its load-bearing points are (6), already proved in `ANF-037`; the series identity (11); spectral nonnegativity `J\ge0`; and the coefficient inequality (13). Compact support is used only to justify the Fourier--Laplace quantities and the small-height converse without integrability issues. A sign error can be audited directly by expanding the structure factor or by checking the first two even powers: the quadratic coefficient is `2+3 cos v`, while the quartic coefficient is `8+3 cos v>0`.

The theorem does **not** prove the full universal affine certificate for `J_s`, does not address two-conjugate-pair-plus-one-real five-point configurations, and does not control larger coupled complex multisets. It also does not replace the finite-real normalization/slack analysis of `ANF-034`; it only shows that one complete complex layer adds no new obstruction once the curvature gate passes.

The next decisive five-point test is therefore the remaining geometry

\[
\{x_1+iy_1,x_1-iy_1,x_2+iy_2,x_2-iy_2,r\}.
\]

Its structure-factor defect contains a coupled term proportional to

\[
\bigl(\cosh(2\pi\alpha y_1)\cosh(2\pi\alpha y_2)-1\bigr)
\cos(2\pi\alpha(x_1-x_2)),
\]

so the one-dimensional independent-anchor reduction of `ANF-037` no longer applies. Deriving the exact minimal coupled criterion for that pattern is now the cheapest route either to kill the central-notch separator or to clear all cardinality-five complex constraints.