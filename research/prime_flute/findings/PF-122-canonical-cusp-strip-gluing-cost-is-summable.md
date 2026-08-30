# PF-122 — canonical cusp-strip gluing cost is summable

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. The upper-half-plane cusp calculation is elementary. The project-specific result is that the remaining deep-cusp coherence problem left by PF-119--PF-121 has an explicit two-dimensional solution for the exact prime/shift-clone pants: on the canonical cusp strip, the source split ray and both outer cusp rays can be matched by a piecewise-affine bilipschitz map whose logarithmic distortion is bounded by the **adjacent first difference** of the single-cuff chart-scale defects. PF-119 proves those first differences are in `ell^1`. Thus neither an extreme split ratio nor the nonsummable reciprocal-prime common scale creates a deep-cusp metric amplification. This does not yet construct the full pantwise/global comparison or prove compact relative resolvent.

## Claim

Let `P(2a,2b,0)` be the one-cusp right-angled pentagon normalization of PF-119. Put

\[
A=\cosh a,\qquad B=\cosh b,
\qquad
t=\frac{A}{A+B}.
\tag{1}
\]

The two outer cusp rays are `x=0` and `x=1`, and the canonical split ray is `x=t`. Let the target pentagon have parameters `a',b'` and define

\[
A'=\cosh a',\qquad B'=\cosh b',
\qquad
t'=\frac{A'}{A'+B'}.
\tag{2}
\]

Write the two logarithmic single-cuff scale changes as

\[
\varepsilon_a=\log\frac{A'}A,
\qquad
\varepsilon_b=\log\frac{B'}B.
\tag{3}
\]

For every `Y>=1`, the entire part of either pentagon above the horocycle `y=Y` is the full strip

\[
C_Y=\{(x,y):0\le x\le1,\ y\ge Y\}.
\tag{4}
\]

Define the increasing piecewise-affine map `phi:[0,1]->[0,1]` by

\[
\phi(x)=
\begin{cases}
\dfrac{t'}t x,&0\le x\le t,\\[6pt]
t'+\dfrac{1-t'}{1-t}(x-t),&t\le x\le1.
\end{cases}
\tag{5}
\]

Then

\[
\boxed{
F(x,y)=(\phi(x),y)
}
\tag{6}
\]

is a label-preserving piecewise-smooth homeomorphism of the source cusp strip onto the target cusp strip. It fixes the two outer rays pointwise, maps the split ray `x=t` pointwise in Busemann height to `x=t'`, and satisfies the exact uniform estimate

\[
\boxed{
\log \operatorname{Bilip}(F)
\le |\varepsilon_a-\varepsilon_b|.
}
\tag{7}
\]

The bound is independent of `t`; in particular it remains valid when `t->0` or `t->1`.

For the exact prime flute and its all-composite shift clone, put `a=a_n`, `b=a_{n+1}` and use superscript `+` for the target. With PF-119's notation

\[
\varepsilon_n=
\log\cosh a_n^+-\log\cosh a_n,
\qquad
\sigma_n=\log\cosh a_n-\log\cosh a_{n+1},
\tag{8}
\]

we have

\[
\varepsilon_n-\varepsilon_{n+1}
=\sigma_n^+-\sigma_n.
\tag{9}
\]

Hence PF-119 gives

\[
\boxed{
\sum_n \log \operatorname{Bilip}(F_n)
\le
\sum_n |\sigma_n^+-\sigma_n|<\infty.
}
\tag{10}
\]

In particular `Bilip(F_n)->1`. The deep-cusp gluing cost is not merely `o(1)` but summable in logarithmic bilipschitz scale.

## 1. Why `y>=1` is already a canonical full cusp strip

PF-119 gives the exact Euclidean radii in the normalization (1):

\[
r_a=\frac{\sinh a}{A+B},\qquad
r_b=\frac{\sinh b}{A+B},\qquad
R=\frac1{A+B}.
\tag{11}
\]

Every non-cusp boundary arc is a semicircle centered on the real axis with one of these radii. Since

\[
r_a<t<1,
\qquad
r_b<1-t<1,
\qquad
R<1,
\tag{12}
\]

all of those arcs lie below `y=1`. Thus no large-cuff or small-gap asymptotic is being inserted into (4): after the exact PF-119 normalization, `y>=1` is literally the same standard cusp strip for every pair `(a,b)`. The only marked datum visible there is the location `t` of the artificial split ray.

This is the correct place to test PF-120's synchronization constraint because the hyperbolic metric is exactly

\[
ds^2=\frac{dx^2+dy^2}{y^2}
\tag{13}
\]

with no parameter dependence.

## 2. Exact distortion bound

By (3),

\[
A'=Ae^{\varepsilon_a},
\qquad
B'=Be^{\varepsilon_b}.
\]

Since `t=A/(A+B)`, define

\[
D:=t e^{\varepsilon_a}+(1-t)e^{\varepsilon_b}.
\tag{14}
\]

A direct substitution gives the two slopes in (5):

\[
\boxed{
 m_L:=\frac{t'}t=\frac{e^{\varepsilon_a}}D,
\qquad
 m_R:=\frac{1-t'}{1-t}=\frac{e^{\varepsilon_b}}D.
}
\tag{15}
\]

Because `D` is a convex combination of `e^{epsilon_a}` and `e^{epsilon_b}`,

\[
\min(\varepsilon_a,\varepsilon_b)
\le \log D\le
\max(\varepsilon_a,\varepsilon_b).
\tag{16}
\]

Therefore

\[
|\log m_L|\le|\varepsilon_a-\varepsilon_b|,
\qquad
|\log m_R|\le|\varepsilon_a-\varepsilon_b|.
\tag{17}
\]

On either side of the split, the differential of (6) is `diag(m,1)`. Since the common conformal factor `1/y^2` in (13) is unchanged, the local singular values relative to the hyperbolic metric are exactly `m` and `1`. Hence

\[
\operatorname{Bilip}(F)
=\max\{m_L,m_L^{-1},m_R,m_R^{-1}\},
\]

and (17) proves (7).

This proof is insensitive to how close `t` is to `0` or `1`. That is important because extreme neighboring prime-gap ratios can push the canonical PF-119 split arbitrarily far to one side. No factor `1/t` or `1/(1-t)` survives in the distortion estimate.

## 3. The reciprocal-prime common mode cancels exactly

PF-107/PF-114 show that the single-cuff scale change carries a reciprocal-prime mode, and PF-119 writes it as

\[
\varepsilon_n=\frac1{p_n}+o(p_n^{-1})+r_n,
\qquad
\sum_n|r_n|<\infty,
\tag{18}
\]

in the relevant indexing. Its absolute sum diverges. A naive chart-by-chart gluing argument could therefore suggest an accumulated cusp distortion.

Equation (7) shows that the actual two-dimensional normalized cusp strip does not see this common mode. It sees only

\[
\varepsilon_n-\varepsilon_{n+1}.
\tag{19}
\]

Indeed, if `epsilon_a=epsilon_b` exactly, then (14)--(15) give `m_L=m_R=1`, `t'=t`, and the map (6) is the identity even though the common scale change itself may be nonzero. Thus the common Busemann/chart scale is a genuine gauge mode for the deep cusp.

For the shift clone, PF-119 proves that (19) is absolutely summable, yielding (10). This strengthens PF-119 from a scalar split-offset statement to an actual two-dimensional metric comparison on the complete cusp tail.

## 4. Relation to PF-120 and PF-121

PF-120 proves that two rays of the same cusp cannot be assigned different asymptotic Busemann shifts by a finite-bilipschitz map. The map (6) obeys that constraint in the strongest possible way: it preserves `y` on **all three** marked vertical rays. Thus no sidewise gauge synchronization remains to be solved above `y=1`.

PF-121 separately constructs `1+O(a'-a)` bilipschitz maps on each canonical ideal Lambert quadrilateral, uniformly through its ideal vertex. What PF-121 deliberately leaves open is whether the two independently normalized quadrilateral maps can be made to have the same trace on the PF-119 split ray and then glue into a pant/global map.

PF-122 removes the **deep-cusp** part of that problem. There is an exact common target trace on the split ray and an explicit interior extension with summable cost. The remaining local gate is confined to reconciling the PF-121 lower quadrilateral maps with (6) across a bounded-height transition region while preserving a cuff trace that depends only on the shared cuff. After that, one must still double the pentagons, glue the zero-twist pants, and verify that the resulting complete-surface metric tensor and volume density tend uniformly to the identity.

Therefore PF-122 proves only

\[
\boxed{
\text{deep cusp + extreme split ratios + reciprocal-prime gauge}
\not\Rightarrow
\text{metric amplification}.
}
\tag{20}
\]

It does not yet prove strong equivalence of the two complete Riemannian structures or compactness of the relative resolvent.

## 5. Prior-art and novelty audit

No novelty is claimed for piecewise-affine maps of a strip, the conformal upper-half-plane metric, or the general idea of synchronizing a cusp in Busemann coordinates. The hyperbolic pants/degenerate-hexagon comparison results already audited in the accepted clue remain the surrounding prior art: Minsky gives coarse bilipschitz comparisons including cusp limits, while Wu--Zhang give near-isometric piecewise-smooth maps in a different thick-boundary perturbation regime. PF-121 records the closest Lambert-quadrilateral comparison literature.

Directed searches for bilipschitz hyperbolic cusp-strip maps, boundary-controlled one-cusp pants comparisons, and Lambert-quadrilateral cusp maps did not locate the exact split-ray estimate (7), nor the shift-clone specialization (10). The project does not claim a new general cusp theorem. The durable Mathia content is the exact cancellation

\[
\boxed{
\log K_n
\le
|\varepsilon_n-\varepsilon_{n+1}|
=|\sigma_n^+-\sigma_n|
\in\ell^1,
}
\tag{21}
\]

for the canonical all-composite control.

The result is adversarial rather than RH-positive: it removes another natural place where the prime-specific surface might have amplified the clone's apparently small endpoint deformation.

## 6. Falsification core

The claim has five independent checks:

1. derive PF-119's exact radii (11) and verify that every finite boundary arc lies below `y=1`;
2. verify that (5) is increasing, fixes `0,1`, and sends `t` to `t'`;
3. substitute `A'=Ae^{epsilon_a}`, `B'=Be^{epsilon_b}` to obtain the exact slopes (15);
4. use the convex-combination bound (16) to prove (17) uniformly even for `t->0,1`;
5. specialize `epsilon_a-epsilon_b` to PF-119's exact first difference (9) and use its established `ell^1` theorem.

Failure of any one of these gates invalidates the project-specific conclusion. Even if all hold, no global operator statement follows until the bounded-height transition and cuff-coherent pant gluing are constructed.