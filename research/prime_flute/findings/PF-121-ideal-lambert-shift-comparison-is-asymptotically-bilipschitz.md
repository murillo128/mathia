# PF-121 — ideal Lambert shift comparison is asymptotically bilipschitz

**Status:** `EXACT-DERIVED + POSITIVE/BOUNDARY`. The canonical ideal-Lambert geometry is classical. The project-specific result is that the one-parameter quadrilateral gate isolated in PF-119/PF-120 has a direct positive solution: if `a' - a -> 0` with `a -> infinity`, then `Q(a)` and `Q(a')` admit label-preserving piecewise-smooth bilipschitz homeomorphisms with constant tending to `1`, including the full ideal-cusp region. In particular, the collapsing `sech(a)` side does not force an `O(1)` interior distortion. This is still only a local building block: it does not prove that the two half-pant maps have identical traces on the shared PF-119 split ray, that the doubled pants glue globally, or that the complete prime/shift-clone Laplacians have compact relative resolvent.

## Claim

Let `Q(a)` be the canonical ideal Lambert quadrilateral of PF-119. There are absolute constants `A>1`, `epsilon>0`, and `C>0` such that, whenever

\[
a\ge A,\qquad 0\le\delta\le\epsilon,\qquad a'=a+\delta,
\]

there is a label-preserving piecewise smooth homeomorphism

\[
F_{a,a'}:Q(a)\longrightarrow Q(a')
\]

with

\[
\boxed{\operatorname{Bilip}(F_{a,a'})\le 1+C\delta.}
\tag{1}
\]

The same bound controls the inverse after increasing `C`. Hence

\[
\boxed{
a'-a\to0\quad\Longrightarrow\quad d_{\mathrm{Bilip}}(Q(a),Q(a'))\to0}
\tag{2}
\]

uniformly as `a -> infinity`.

For the exact prime/shift-clone cuffs, PF-107 gives

\[
a_n=\frac{\ell_n}{2},\qquad a_n^+=\frac{\ell_n^+}{2},\qquad
\delta_n:=a_n^+-a_n\longrightarrow0
\]

(and in its indexing `delta_n ~ 1/p`). Therefore

\[
\boxed{\operatorname{Bilip}(Q(a_n),Q(a_n^+))\to1.}
\tag{3}
\]

This removes the cheapest negative test in the accepted relative-operator clue: there is no local `O(1)` metric-tensor obstruction intrinsic to a single canonical `Q(a)`.

## 1. A canonical log-polar model

An ideal Lambert quadrilateral is determined by one finite side length. Normalize `Q(a)` isometrically so that two perpendicular finite-side geodesics meet at `i`, one is the positive imaginary axis, and the other is the unit semicircle. Put the endpoint of the length-`a` side at `i e^a`. The cusp ray perpendicular there is the semicircle `|z|=e^a`. The other cusp ray is the unique geodesic perpendicular to the unit semicircle and asymptotic to the first one at `e^a`; its endpoints are

\[
e^{-a},\qquad e^a,
\]

because orthogonality to the unit circle is equivalent to the product of the two real endpoints being `1`.

Use log-polar coordinates in the first quadrant,

\[
z=e^{u+i\theta},\qquad
w:=\frac\pi2-\theta.
\]

The hyperbolic metric becomes

\[
\boxed{
ds^2=\frac{du^2+dw^2}{\cos^2 w}.}
\tag{4}
\]

The remarkable point is that the metric tensor itself is independent of `a`. All parameter dependence is in the lower graph. Indeed the geodesic with endpoints `e^{-a},e^a` has equation

\[
\cosh u=\cosh a\cos\theta,
\]

so, writing

\[
W_a(u):=\arcsin\frac{\cosh u}{\cosh a},
\]

the quadrilateral is exactly

\[
\boxed{
D_a=\{(u,w):0\le u\le a,\ 0\le w\le W_a(u)\}.
}
\tag{5}
\]

Its four labeled sides are `w=0`, `u=0`, `u=a`, and `w=W_a(u)`. The ideal cusp is `(a,pi/2)`.

## 2. The whole cusp tail is compared by a diagonal map

Set

\[
c:=\frac{\cosh a'}{\cosh a}>1
\]

and, for `u>=1`, define

\[
\boxed{
f(u):=\operatorname{arcosh}(c\cosh u).}
\tag{6}
\]

Then

\[
f(a)=a'
\]

and, crucially,

\[
\boxed{W_{a'}(f(u))=W_a(u)}
\tag{7}
\]

exactly. Therefore

\[
F_{\mathrm{tail}}(u,w)=(f(u),w)
\tag{8}
\]

maps the full portion `D_a cap {u>=1}` onto the corresponding portion of `D_{a'}` and maps both cusp sides to their corresponding sides all the way to the ideal vertex. There is no separately chosen sidewise Busemann scaling: (8) is one genuine two-dimensional map, so the PF-120 synchronization constraint is built in.

Differentiate (6):

\[
f'(u)=\frac{c\sinh u}{\sinh f(u)}
\]

and hence

\[
\boxed{
1-f'(u)^2
=\frac{c^2-1}{c^2\cosh^2u-1}.}
\tag{9}
\]

For `0<=delta<=epsilon`, `c^2-1=O(delta)` uniformly in `a`, while for `u>=1` the denominator in (9) is bounded below by a positive absolute constant. Thus

\[
1-C_1\delta\le f'(u)\le1.
\tag{10}
\]

Because (8) preserves `w`, equations (4) and (10) immediately give

\[
\operatorname{Bilip}(F_{\mathrm{tail}})\le1+C_2\delta.
\tag{11}
\]

This estimate remains valid arbitrarily deep in the cusp. In particular, the shrinking Euclidean scale `sech(a)` has disappeared from the distortion bound.

## 3. The finite base strip also has uniform `1+O(delta)` distortion

Only the compact log-radial interval `0<=u<=1` remains. Put

\[
u_1:=f(1)=\operatorname{arcosh}(c\cosh1)=1+O(\delta)
\tag{12}
\]

and define

\[
U=u_1u,
\qquad
R(u):=\frac{W_{a'}(u_1u)}{W_a(u)},
\qquad
F_{\mathrm{base}}(u,w):=(U,R(u)w).
\tag{13}
\]

This maps `u=0` to `U=0`, maps the graph `w=W_a(u)` exactly to the target graph, and agrees continuously with (8) at `u=1` because (7) gives `R(1)=1`.

For `u in [0,1]` and large `a`,

\[
W_a(u)
=\frac{\cosh u}{\cosh a}\left(1+O(e^{-2a})\right).
\tag{14}
\]

Using (12)--(14), uniformly on the base strip,

\[
\boxed{
R(u)=1+O(\delta),
\qquad
R'(u)=O(\delta),
\qquad
u_1=1+O(\delta).}
\tag{15}
\]

Moreover `w<=W_a(1)=O(e^{-a})`. Pulling back the target metric gives

\[
F_{\mathrm{base}}^*ds_{a'}^2
=
\frac{
 u_1^2du^2+
 (R\,dw+wR'\,du)^2
}{\cos^2(Rw)}.
\tag{16}
\]

Equations (14)--(15) imply

\[
\frac{\cos w}{\cos(Rw)}=1+O(\delta e^{-2a})
\]

and the Euclidean matrix in the numerator of (16) differs from the identity by `O(delta)`. Hence

\[
\operatorname{Bilip}(F_{\mathrm{base}})\le1+C_3\delta.
\tag{17}
\]

The two formulas (8) and (13) therefore define a label-preserving piecewise smooth homeomorphism on all of `D_a` satisfying (1). The derivative may jump along `u=1`; this is harmless for the bilipschitz statement, and a standard interpolation in a fixed-width neighborhood would smooth it without changing the `1+O(delta)` estimate.

## 4. Consequence for the shift-clone operator program

PF-119 reduced the local pant comparison to a one-parameter ideal quadrilateral plus a scalar split offset. PF-120 then showed that independently canonical side isometries cannot simply be filled in: their cusp Busemann gauges disagree by the reciprocal-prime mode. PF-121 shows that this was a **boundary-data choice obstruction, not an intrinsic interior metric obstruction**.

For the actual shift clone,

\[
\boxed{
Q(a_n)\simeq_{1+o(1)}Q(a_n^+)
}
\tag{18}
\]

through genuine homeomorphisms whose estimates remain uniform through the ideal vertex. Therefore a negative resolution of the accepted relative-operator clue can no longer come from the assertion that every map of one canonical quadrilateral pays a fixed positive distortion because one side collapses.

The remaining gate is narrower and genuinely global. The two quadrilaterals making one PF-119 pentagon use different normalized cusp charts. Their boundary traces on the shared split ray must still be made identical after restoring the exact chart-scale ratio, then doubled pant maps must induce the same marked map on every cuff before zero-twist gluing. Only after that does one have a common-manifold identification on which compactness of the relative resolvent can be tested.

Thus PF-121 proves

\[
\boxed{
\text{collapsing Lambert geometry}
\not\Rightarrow
\text{local bilipschitz amplification},
}
\tag{19}
\]

but deliberately does **not** assert global strong metric equivalence or any spectral consequence.

## 5. Prior art and novelty audit

No novelty is claimed for ideal Lambert quadrilaterals, log-polar coordinates, or elementary bilipschitz interpolation. Vuorinen--Wang study metric inequalities and quasiconformal images of hyperbolic Lambert quadrilaterals; Minsky gives coarse bilipschitz comparison of pants/degenerate hexagons under bounded additive boundary-length changes; and the Wu--Zhang construction gives `1+o(1)` metric-tensor control for a different thick-boundary perturbation regime. None of those audited statements directly supplies the specific unbounded-cuff/collapsing-side map needed by the accepted clue.

The durable Mathia content is the explicit reduction (4)--(9): after a canonical isometry, the entire `a`-dependence of `Q(a)` sits in the graph `W_a`, and the tail change `a -> a'` is absorbed exactly by the diagonal coordinate change (6). Directed searches for this exact `Q(a)` comparison and its `arcosh((cosh a'/cosh a) cosh u)` map located no matching published theorem. This is therefore stored as a project-specific derived comparison lemma, not as a broad novelty claim about Lambert quadrilaterals.

## 6. Falsification core

The result has five independent checks:

1. verify the canonical right-angle normalization and that the second cusp geodesic has endpoints `e^{-a},e^a`;
2. transform with `z=e^{u+i theta}` and derive both the metric (4) and graph domain (5);
3. substitute (6) into `W_{a'}` and check the exact identity (7);
4. differentiate (6) to obtain (9), which gives the cusp-uniform `1+O(delta)` bound without any hidden `sech(a)^{-1}` factor;
5. on `0<=u<=1`, use the small-width expansion (14) to verify (15)--(17).

Failure of any one of these gates invalidates the claim. Even if all five hold, no operator conclusion follows until the PF-119 split-ray traces and the full infinite gluing problem are solved.