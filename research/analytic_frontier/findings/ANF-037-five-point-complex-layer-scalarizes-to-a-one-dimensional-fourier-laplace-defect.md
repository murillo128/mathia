# ANF-037 — the first five-point complex layer scalarizes to a one-dimensional Fourier–Laplace defect

**Status:** `EXACT-DERIVED + COMPLEX-FALSIFIER-REDUCTION + SHARP-FIVE-POINT-GATE + STRUCTURAL-BOUNDARY`. `ANF-036` proves that every conjugation-invariant multiset of cardinality at most four is dominated, for every compact-band spectrum `J>=0`, by collapsing nonreal points onto their real parts, and that five points are the first cardinality where spectral positivity alone permits a strict reversal. The remaining five-point search still appears three-dimensional if one varies the three real anchors independently. It is not: for the first nontrivial geometry, one conjugate pair plus three real points, the entire complex-vs-real question reduces exactly to a **one-dimensional Fourier minimum at each height**.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad
J\ge0,
\tag{1}
\]

with `J` real, even, continuous and compactly supported. Fix `y>0`, a horizontal center `x`, and distinct real anchors `r_1,\ldots,r_m` different from `x`. Put

\[
W_{m,y}
=\{x+iy,x-iy,r_1,\ldots,r_m\},
\]

and let `R(W_{m,y})` be its real-part collapse, so that the conjugate pair is replaced by two copies of `x`. Define

\[
t_j:=r_j-x,
\qquad
c_y(\alpha):=\cosh(2\pi\alpha y),
\tag{2}
\]

and the nonnegative spectral weight

\[
p_y(\alpha):=J(\alpha)(c_y(\alpha)-1).
\tag{3}
\]

Write

\[
L_y(t)
:=\int_{-B}^{B}p_y(\alpha)\cos(2\pi\alpha t)\,d\alpha
=\Re F(t+iy)-F(t),
\tag{4}
\]

and

\[
A_y
:=\int_{-B}^{B}J(\alpha)(c_y(\alpha)^2-1)\,d\alpha
=\frac{F(2iy)-F(0)}2.
\tag{5}
\]

Then the energy defect relative to real collapse is exactly

\[
\boxed{
E_F(W_{m,y})-E_F(R(W_{m,y}))
=4\left(A_y+\sum_{j=1}^mL_y(t_j)\right).
}
\tag{6}
\]

Consequently, if

\[
\ell_y:=\inf_{t\in\mathbb R}L_y(t),
\tag{7}
\]

then, allowing distinct anchors to approach the same minimizing displacement,

\[
\boxed{
\inf_{r_1,\ldots,r_m}
\bigl(E_F(W_{m,y})-E_F(R(W_{m,y}))\bigr)
=4(A_y+m\ell_y).
}
\tag{8}
\]

For the first genuinely new complex layer `m=3`, **all** five-point configurations consisting of one conjugate pair and three real anchors are collapse-dominated at height `y` if and only if

\[
\boxed{A_y+3\ell_y\ge0.}
\tag{9}
\]

If the left side is negative, three distinct anchors can be chosen arbitrarily close to a minimizer of `L_y` so that the five-point complex configuration has strictly smaller energy than its real collapse. Thus the post-`ANF-036` audit does not require a search over three independent real phases: it requires only the scalar function `L_y(t)` and its real minimum, followed by a one-parameter scan in `y`.

## 1. Exact structure-factor reduction

For fixed real frequency `alpha`, let

\[
z=e^{-2\pi i\alpha x},
\qquad
A=\sum_{j=1}^m e^{-2\pi i\alpha r_j},
\qquad
c=c_y(\alpha).
\]

Then

\[
S_{W_{m,y}}(\alpha)=A+2cz,
\qquad
S_{R(W_{m,y})}(\alpha)=A+2z.
\]

Expanding gives

\[
\begin{aligned}
|S_{W_{m,y}}|^2-|S_{R(W_{m,y})}|^2
&=4(c^2-1)+4(c-1)\Re(A\bar z)\\
&=4(c-1)\left(c+1+\sum_{j=1}^m\cos(2\pi\alpha t_j)\right).
\end{aligned}
\tag{10}
\]

Integrating (10) against `J(alpha)dalpha` gives (6). The two identities in (4)--(5) follow directly from the Fourier--Laplace representation:

\[
\Re F(t+iy)-F(t)
=\int J(\alpha)(\cosh(2\pi\alpha y)-1)
\cos(2\pi\alpha t)\,d\alpha,
\]

and `cosh(2u)-1=2sinh^2(u)`.

Because the `t_j` are otherwise independent, every term in the sum in (6) can approach the same infimum `ell_y`. Distinctness of the real anchors causes no loss: if an infimum is attained at `t_*`, take `t_*+epsilon_j` with distinct `epsilon_j->0`; if it is not attained, take three distinct points from a minimizing sequence. Continuity of `L_y` gives (8).

## 2. The four-point theorem reappears as the trivial `m<=2` range

Since `p_y>=0`,

\[
|L_y(t)|\le L_y(0)
=\int J(\alpha)(c_y(\alpha)-1)\,d\alpha.
\tag{11}
\]

Also

\[
A_y
=\int p_y(\alpha)(c_y(\alpha)+1)\,d\alpha
\ge2L_y(0).
\tag{12}
\]

Therefore

\[
A_y+m\ell_y
\ge A_y-mL_y(0)
\ge(2-m)L_y(0).
\tag{13}
\]

For `m=0,1,2` this is nonnegative for every height, every horizontal geometry and every `J>=0`. This recovers in one line the one-conjugate-pair portion of the `ANF-036` cardinality-four collapse theorem. The inequality loses its automatic sign exactly at `m=3`, i.e. total cardinality five.

The threshold is sharp. If the positive spectrum is concentrated near frequencies where all three anchor phases are close to `-1` and `1<c_y<2`, then (10) has negative sign on that concentration region. This is the same amplitude-budget mechanism behind the explicit five-point construction of `ANF-036`, now expressed as the failure of (9).

## 3. Small-height limit: an exact second-spectral-moment curvature gate

The fixed-height scalarization has a particularly simple infinitesimal limit. Define

\[
K(t)
:=\int_{-B}^{B}\alpha^2J(\alpha)
\cos(2\pi\alpha t)\,d\alpha
=-\frac{F''(t)}{4\pi^2}.
\tag{14}
\]

Because the support is compact, the Taylor expansion of `cosh` is uniform under the integral and uniform in `t` after taking absolute values. Hence

\[
\frac{L_y(t)}{2\pi^2y^2}\longrightarrow K(t)
\quad\text{uniformly in }t,
\tag{15}
\]

while

\[
\frac{A_y}{2\pi^2y^2}\longrightarrow2K(0).
\tag{16}
\]

It follows that

\[
\boxed{
\frac{A_y+3\ell_y}{2\pi^2y^2}
\longrightarrow
2K(0)+3\inf_{t\in\mathbb R}K(t).
}
\tag{17}
\]

Equivalently, when `K(0)>0`, put

\[
\rho_2(t):=\frac{K(t)}{K(0)}.
\]

Then the five-point layer has the sharp second-variation threshold

\[
\boxed{
\inf_t\rho_2(t)\ \gtrless\ -\frac23.
}
\tag{18}
\]

If `inf rho_2<-2/3`, arbitrarily small nonzero heights already produce a five-point complex configuration with lower energy than its real collapse. If `inf rho_2>-2/3`, all sufficiently small heights are uniformly collapse-dominated. Equality is the degenerate boundary where the fourth-order term must be inspected.

In physical-space language, (18) is

\[
\boxed{
2F''(0)+3\sup_{t\in\mathbb R}F''(t)\ \lessgtr\ 0,
}
\tag{19}
\]

with the inequality direction reversed relative to (18) because `K=-F''/(4pi^2)`. Thus the first complex instability is controlled by the **curvature profile** of the spatial kernel, not by its value profile alone.

## 4. Consequence for the central-notch ray of ANF-034

For

\[
J_s=J_{\rm MT}-s\phi_\eta
\]

from `ANF-034`, equations (4)--(9) give the exact five-point test with no new conceptual machinery:

\[
G_s(y)
:=A_{s,y}+3\inf_tL_{s,y}(t).
\tag{20}
\]

The finite-real separator survives the first complex geometry at height `y` precisely when `G_s(y)>=0`; a strict negative value supplies an explicit five-point energy reversal.

The perturbation is also quantitatively continuous. Since `phi_eta(c_y-1)>=0`,

\[
\sup_t L_{\phi,y}(t)=L_{\phi,y}(0),
\]

and therefore

\[
\boxed{
G_s(y)
\ge
G_{\rm MT}(y)
-s\left(A_{\phi,y}+3L_{\phi,y}(0)\right).
}
\tag{21}
\]

At infinitesimal height, the tent has the exact second spectral moment

\[
K_\phi(0)
=\int\alpha^2\phi_\eta(\alpha)\,d\alpha
=\frac{b_\eta\eta^3}{6}.
\tag{22}
\]

Hence, if

\[
m_5(J):=2K_J(0)+3\inf_tK_J(t),
\]

then

\[
\boxed{
m_5(J_s)
\ge
m_5(J_{\rm MT})-
\frac56\,s b_\eta\eta^3.
}
\tag{23}
\]

Equation (23) is only a perturbative lower bound; it does not assert that `m_5(J_MT)` is positive, nor that the notch ray passes the full finite-height gate. Its value is methodological: **subtracting a narrow central notch does not by itself imply an immediate five-point failure.** The exact next quantity is now `G_s(y)`, with (17)--(23) giving its small-height control.

## 5. Affine-counting relevance and boundary

For the five-point geometry with three distinct real anchors, both `W_{3,y}` and its real collapse have exactly three simple real points: the collapsed pair becomes a double point and contributes no simple point. They also have the same total cardinality. Therefore any strict inequality

\[
E_F(W_{3,y})<E_F(R(W_{3,y}))
\]

makes the complex configuration a strictly stronger constraint on a universal affine certificate at the same spectral amplitude. This is exactly the residual complex-geometric issue left by `ANF-034`--`ANF-036`.

The reduction does **not** prove that the central-notch separator yields a better unconditional zeta-zero proportion, and it does not prove that a five-point witness kills it. Passing (9) for every `y` would only clear the first genuinely complex cardinality layer. Larger conjugation-invariant multisets, multiple nonreal fibers, normalization slack from `ANF-005`, and the full universal affine inequality remain separate constraints.

Conversely, a negative value of `G_s(y)` is not yet by itself a complete scalar-branch no-go: one must compare the resulting stronger five-point affine constraint with the finite-real gain and amplitude optimization. What (9) accomplishes is to remove the unnecessary three-anchor search from that comparison and expose the exact complex energy decrement that must be paid.

## 6. Prior art and audit boundary

The Fourier--Laplace representation of holomorphic positive-definite strip functions is classical and already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides; `ANF-012`, `ANF-035` and `ANF-036` already use the same positive-spectrum structure. A targeted search of that literature and of structure-factor/positive-definite kernel formulations found the expected general representation theory but no matching theorem for the finite-cardinality real-collapse defect (8)--(9). No publication-level novelty claim is made.

The new content is elementary but structural: the first nontrivial complex layer is exactly the scalar Fourier-minimum problem (9), and its local boundary is the curvature ratio (18). No new external source is load-bearing, so `SOURCES.md` requires no change.

The audit points are explicit. Equation (6) can be checked either from structure factors or directly from pair energies. Equation (8) depends only on continuity and independent choice of distinct anchors. Uniformity in (15) follows from compact support and the uniform `O(y^4 alpha^4)` Taylor remainder. A counterexample to any of those three steps would invalidate the reduction.

## 7. Next decisive test

For the explicit central-notch family of `ANF-034`, the next scalar-complex audit is now two-dimensional rather than four-dimensional: determine

\[
\boxed{
\inf_{y>0}G_s(y)
=
\inf_{y>0}\left[
\frac{F_s(2iy)-F_s(0)}2
+3\inf_{t\in\mathbb R}
\bigl(\Re F_s(t+iy)-F_s(t)\bigr)
\right].
}
\tag{24}
\]

A negative certified value identifies the first complex energy reversal for the notch ray and gives the exact geometry from a minimizing `t`. A nonnegative proof for all `y` clears the complete one-pair-plus-three-real five-point layer and forces the next obstruction to use either a different five-point fiber pattern or larger genuinely coupled complex configurations.