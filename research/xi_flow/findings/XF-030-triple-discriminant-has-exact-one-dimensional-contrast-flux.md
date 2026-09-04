# XF-030 — triple discriminant has an exact one-dimensional contrast flux with signed cubic exterior kernel

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE` + `STRUCTURAL/BOUNDARY`. XF-027 gives the normalized block discriminant an exact square production and affine exterior cancellation, XF-028 shows that positive overlap protects covered collision walls, and XF-029 identifies the Cauchy taper commutator at lattice quadratic order. For the smallest nontrivial block, `n=3`, the full finite-gap shape dynamics can be compressed further: the affine shape space is one-dimensional, and the complete exterior coupling is an exact signed cubic divided-difference kernel.

Let three consecutive real roots be
\[
x_0<x_1<x_2,
\qquad
p=x_1-x_0>0,
\qquad
q=x_2-x_1>0,
\]
and let
\[
d=\log\frac q p,
\qquad
r=e^d=\frac q p.
\]
For the XF-027 normalized discriminant
\[
\mathcal J
=
2\log p+2\log q+2\log(p+q)
-3\log\!\left[\frac23(p^2+pq+q^2)\right],
\]
one has
\[
\boxed{\mathcal J=F(d)}
\]
with
\[
\boxed{
F'(d)=\phi(r)
=
-\frac{(r-1)(r+2)(2r+1)}
{(r+1)(r^2+r+1)}.
}
\tag{1}
\]
Moreover
\[
\boxed{
F''(d)
=
-\frac{r(r^4+14r^3+24r^2+14r+1)}
{(r+1)^2(r^2+r+1)^2}<0.
}
\tag{2}
\]
Thus the triple shape entropy is strictly concave in the logarithmic gap contrast, has its unique maximum at `p=q`, and has no secondary finite-gap shape well.

Write
\[
S=p^2+pq+q^2.
\]
On any real-simple logarithmic zero-flow slice, split the reciprocal field at the three roots into the field of the other two roots plus the field of all exterior roots. Then the contrast satisfies the exact scalar equation
\[
\boxed{
d'
=
\frac{2\phi(r)S}{p^2q^2}
+
2(p+q)
\sum_{z\notin\{x_0,x_1,x_2\}}'
\frac{1}
{(x_0-z)(x_1-z)(x_2-z)}.
}
\tag{3}
\]
Consequently
\[
\boxed{
\mathcal J'
=
\frac{2\phi(r)^2S}{p^2q^2}
+
2\phi(r)(p+q)
\sum_{z\notin\{x_0,x_1,x_2\}}'
\frac{1}
{(x_0-z)(x_1-z)(x_2-z)}.
}
\tag{4}
\]
For Xi zeros the exterior sum in (3)--(4) is absolutely convergent: the affine pieces have disappeared exactly and every exterior root is charged by a cubic denominator.

The sign is also exact. Every exterior root to the left of the triple contributes positively to `d'`, while every exterior root to the right contributes negatively. Since `phi(r)` has the opposite sign to `d`, exterior mass on the side of the **smaller adjacent gap** pushes the contrast away from zero and decreases `J`; exterior mass on the side of the larger gap pushes it toward zero and increases `J`. This identifies the nonlinear hard-boundary defect much more sharply than a norm bound on the non-affine exterior field.

## 1. The triple shape space is exactly one-dimensional

For three roots, translation and scale remove two of the three positional degrees of freedom. A convenient bounded coordinate is
\[
t=\frac{q-p}{q+p}\in(-1,1).
\]
Substituting `p=s(1-t)` and `q=s(1+t)` into the scale-free discriminant cancels `s` and gives the exact form
\[
\boxed{
\mathcal J(t)
=
-\log2
+2\log(1-t^2)
-3\log\!\left(1+\frac{t^2}{3}\right).
}
\tag{5}
\]
Thus `J=-log 2` at the arithmetic triple and `J -> -infinity` at either collision face `|t| -> 1`.

Equivalently, substituting `q=rp` and differentiating with respect to `d=log r` gives (1). A second differentiation yields (2). In particular,
\[
\phi(1)=0,
\qquad
\operatorname{sgn}\phi(r)=-\operatorname{sgn}(\log r),
\tag{6}
\]
and near `d=0`,
\[
\phi(e^d)=-\frac32d+O(d^3),
\qquad
\mathcal J=-\log2-\frac34d^2+O(d^4).
\tag{7}
\]
Equation (7) recovers the Hessian used in XF-029, but (1)--(5) hold at arbitrary positive gaps.

## 2. The shape gradient has one exact barycentric direction

Let `q^(I)` denote the XF-027 half-gradient,
\[
\frac12\nabla\mathcal J=q^{(I)}.
\]
The logarithmic contrast has gradient
\[
\nabla d
=
\left(
\frac1p,
-\frac{p+q}{pq},
\frac1q
\right)
=
\frac1{pq}
\left(q,-(p+q),p\right).
\tag{8}
\]
Since `J=F(d)`, equations (1) and (8) give
\[
\boxed{
q^{(I)}
=
\frac{\phi(r)}{2pq}
\left(q,-(p+q),p\right).
}
\tag{9}
\]
This vector annihilates both affine directions:
\[
q-(p+q)+p=0,
\]
and, after centering the roots, its first positional moment also vanishes. For `n=3` there is no additional shape direction: (9) is the complete XF-027 projection, not an approximation.

Its norm is
\[
\left\|q^{(I)}\right\|_2^2
=
\frac{\phi(r)^2S}{2p^2q^2},
\tag{10}
\]
because
\[
q^2+(p+q)^2+p^2=2S.
\]
Hence the internal square production of XF-027 becomes
\[
\boxed{
4\left\|q^{(I)}\right\|_2^2
=
\frac{2\phi(r)^2S}{p^2q^2}.
}
\tag{11}
\]

## 3. One exterior root is an exact cubic divided difference

Let `z` be any root outside the triple. Its reciprocal field on the block is
\[
e_z=
\left(
\frac1{x_0-z},
\frac1{x_1-z},
\frac1{x_2-z}
\right).
\]
The barycentric vector in (9) has the exact identity
\[
\boxed{
\left(q,-(p+q),p\right)\!\cdot e_z
=
\frac{pq(p+q)}
{(x_0-z)(x_1-z)(x_2-z)}.
}
\tag{12}
\]
This is the second divided difference of the reciprocal kernel written in the nonuniform three-node barycentric normalization. It is precisely the two-moment cancellation of XF-027 with no remainder estimate.

Using `x_i'=2b_i` and (8), the contribution of this one exterior root to the contrast velocity is therefore
\[
\boxed{
(d')_z
=
\frac{2(p+q)}
{(x_0-z)(x_1-z)(x_2-z)}.
}
\tag{13}
\]
If `z<x_0`, all three factors in the denominator are positive, so `(d')_z>0`. If `z>x_2`, all three are negative, so `(d')_z<0`. The sign does not depend on the distance or on any linearization.

For the Xi zero set, `|x_k|` grows on the order `|k|/log_+|k|`, so the tail in (13) is absolutely summable. The principal-value issue in the root velocities has disappeared after the three-point affine cancellation.

## 4. Internal repulsion and exterior imbalance give the scalar flux law

Let `b^I` be the reciprocal field generated only by the other two roots of the triple. XF-027 gives
\[
\langle q^{(I)},b^I\rangle
=
\|q^{(I)}\|_2^2.
\tag{14}
\]
Combining (9)--(10) with (14),
\[
\left(q,-(p+q),p\right)\!\cdot b^I
=
\frac{\phi(r)S}{pq}.
\tag{15}
\]
Because
\[
d'
=
2\nabla d\cdot b
=
\frac{2}{pq}
\left(q,-(p+q),p\right)\!\cdot b,
\tag{16}
\]
equations (12) and (15) give the exact contrast equation (3). Multiplying by `F'(d)=phi(r)` gives (4).

This separates the two mechanisms without an inequality. The first term in (3) always drives `d` toward zero because `phi` has sign `-sign(d)`. The second is a signed left-minus-right cubic field. A triple can move away from equal spacing only if that exterior imbalance overcomes the internal restoring term.

## 5. The formula interpolates exactly between XF-028 and XF-029

At the arithmetic lattice, (7) turns (4) into the quadratic shape production used by XF-029. The exterior kernel in (13), evaluated on an arithmetic background and summed over translated triples, is the nonlinear ancestor of the Cauchy commutator that appears after linearization and summation by parts.

At a collision, say `q -> 0` with `p` fixed,
\[
\phi(q/p)\longrightarrow 2,
\]
and (11) gives
\[
4\|q^{(I)}\|_2^2
=
\frac8{q^2}+O\!\left(\frac1q\right).
\tag{17}
\]
This is exactly the positive `8/epsilon^2` internal collision production used by XF-028. Thus the same scalar function `phi` connects the lattice Hessian regime and the collision barrier regime without an intermediate asymptotic ansatz.

The exterior hard-edge term is one order weaker. If a left exterior root sits at `z=x_0-delta`, then
\[
(\mathcal J')_z
=
\frac{2\phi(r)(p+q)}
{\delta(\delta+p)(\delta+p+q)}
=
\frac{2\phi(r)}{p\,\delta}+O(1).
\tag{18}
\]
If `q>p`, then `phi(r)<0`, so (18) is the negative `1/delta` membership spike of XF-027. The analogous right-edge spike is
\[
(\mathcal J')_z
=
-\frac{2\phi(r)}{q\,\delta}+O(1)
\tag{19}
\]
for `z=x_2+delta`, and is negative when `p>q`. In both cases the dangerous exterior collision is on the side of the smaller internal gap.

Equations (17)--(19) also explain the overlap mechanism of XF-028 at full nonlinear contrast level: a neighboring block that contains the colliding pair gains positive `1/delta^2` production, while a block that sees the pair only across its boundary pays at worst `1/delta`.

## 6. Stress tests and limits

The scalar reduction does **not** make one triple a Lyapunov observable inside a larger system. Fix `p<q` and place a root at `x_0-delta`. Then `phi(q/p)<0`, the negative term (18) diverges like `-1/delta`, while the internal production (11) remains finite. Hence `J' -> -infinity`. This reproduces the hard-block obstruction without relying on a special numerical configuration.

Nor is (3) Xi-specific. The same identity holds for any ordered logarithmic-repulsion system for which the reciprocal root law is meaningful. Its Xi value is localization: the full exterior field has been reduced to an absolutely convergent signed cubic statistic whose side and scale are explicit.

The formula also does not prove that a constant or slowly tapered sum of translated triples is monotone. Different triples see the same root on opposite sides, and the coefficients `phi(g_{j+1}/g_j)` vary with local shape. A nonlinear overlap proof must exploit cancellation among these signed cubic kernels; positivity of the individual internal terms alone is insufficient.

## 7. Prior-art and novelty boundary

The Vandermonde/Stieltjes structure and logarithmic-particle flow are classical and already anchored in `SOURCES.md`. Three-point divided differences and the fact that an affine shape space of three ordered points is one-dimensional are likewise elementary classical structure. No external theorem is load-bearing in (1)--(19), and no new general log-gas theorem is claimed.

The durable line-specific content is the exact compression of the XF-027 triple observable into a **single logarithmic contrast with a signed cubic exterior flux**, together with the exact interpolation between the XF-028 collision coefficient and the XF-029 lattice Hessian. This is stronger than the previous cubic tail bound because it retains the full coefficient and sign rather than estimating the non-affine field by a norm.

## 8. Consequence for the taper route

The accepted overlap/taper clue now has an exact nonlinear three-root primitive. For
\[
\mathcal K_a=\sum_j a_j\mathcal J_j,
\qquad
d_j=\log\frac{g_{j+1}}{g_j},
\]
one may write exactly
\[
\mathcal K_a'
=
\sum_j a_j\phi(e^{d_j})\,d_j',
\tag{20}
\]
with each `d_j'` given by (3) on its translated triple. The remaining obstruction is no longer the single-block shape algebra: it is whether the signed cubic exterior terms in (20) admit a discrete overlap/summation-by-parts estimate whose localization cost is controlled by taper variation, uniformly away from both the lattice and collision asymptotics already covered by XF-029 and XF-028.

A successful nonlinear estimate should therefore act directly on the kernel in (13). A decisive negative result would be a growing-buffer configuration for which those signed cubic terms retain an order-one adverse aggregate despite vanishing taper variation. Either outcome is now a precise finite-gap test.
