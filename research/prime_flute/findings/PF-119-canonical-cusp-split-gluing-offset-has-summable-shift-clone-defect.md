# PF-119 — canonical cusp-split gluing offset has summable shift-clone defect

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. The upper-half-plane normalization of a one-cusp pair of pants and the right-angled pentagon geometry used below are classical. The project-specific result is that the exact prime/shift-clone deformation has a canonical cusp-split **gluing-offset defect in `ell^1`**, even though the underlying single-cuff scale defect is of reciprocal-prime size and is not in `ell^1`. This removes one natural scalar boundary-coherence obstruction from the accepted relative-operator program. No homeomorphic/bilipschitz global comparison, compact relative resolvent, scattering, determinant, or RH conclusion is claimed.

## Claim

Let `P(2a,2b,0)` be a hyperbolic pair of pants with one cusp and finite cuff lengths `2a,2b`, where `a,b>0`. Cut it along its standard seams and take one of the two congruent ideal right-angled pentagons. Send the ideal vertex to `infinity` in the upper half-plane and normalize the two geodesic rays from the finite cuffs to that cusp to the vertical lines

\[
x=0,\qquad x=1.
\]

Let the two finite-cuff sides be semicircles centered at `0` and `1`, and let their common perpendicular be the semicircle centered at `t` with radius `R`. Then the normalization is exact:

\[
\boxed{
 t=\frac{\cosh a}{\cosh a+\cosh b},\qquad
 R=\frac1{\cosh a+\cosh b},
}
\tag{1}
\]

and the finite-cuff semicircle radii are

\[
\boxed{
 r_a=\frac{\sinh a}{\cosh a+\cosh b},\qquad
 r_b=\frac{\sinh b}{\cosh a+\cosh b}.
}
\tag{2}
\]

The vertical geodesic `x=t`, from the cusp to the top point `t+iR` of the common perpendicular, canonically splits the pentagon into two ideal Lambert quadrilaterals. After the hyperbolic dilations `z -> z/t` on the left and `z -> (1-z)/(1-t)` on the right, the pieces are the one-parameter models

\[
Q(a),\qquad Q(b),
\]

where `Q(c)` is bounded by the verticals `x=0,1` and the two orthogonal semicircles

\[
|z|=\tanh c,
\qquad
|z-1|=\operatorname{sech}c.
\tag{3}
\]

Thus all dependence on the *other* cuff has disappeared from each normalized quadrilateral. The only scalar needed to place the two normalized cusp charts back against each other is the horocyclic split ratio

\[
\boxed{
\Theta(a,b)=\frac{t}{1-t}=\frac{\cosh a}{\cosh b},
\qquad
\sigma(a,b):=\log\Theta(a,b)=\log\cosh a-\log\cosh b.
}
\tag{4}
\]

The ratio `Theta` is independent of the chosen horocycle: on `y=Y`, the hyperbolic horocyclic distances between the three asymptotic verticals are `t/Y` and `(1-t)/Y`. It is also unchanged by the residual affine normalization fixing the cusp at `infinity`.

Now specialize to the exact prime flute and the all-composite shift clone `p -> p+1`. Let

\[
a_n=\frac{\ell_n}{2},
\qquad
\sigma_n=\log\cosh a_n-\log\cosh a_{n+1},
\]

with superscript `+` for the shift clone. Then

\[
\boxed{
\sum_n |\sigma_n^+-\sigma_n|<\infty.
}
\tag{5}
\]

By contrast, the single-cuff chart-scale changes

\[
\varepsilon_n:=\log\cosh a_n^+-\log\cosh a_n
\]

satisfy

\[
\varepsilon_n=\frac1{p_n}+o(p_n^{-1})+r_n,
\qquad
\sum_n|r_n|<\infty,
\tag{6}
\]

in the PF-114 indexing, so

\[
\boxed{
\sum_n\varepsilon_n=\infty
\quad\text{but}\quad
\sum_n|\varepsilon_n-\varepsilon_{n+1}|<\infty.
}
\tag{7}
\]

Equation (5) is exactly the second statement in (7), because

\[
\sigma_n^+-\sigma_n
=\varepsilon_n-\varepsilon_{n+1}.
\tag{8}
\]

So the reciprocal-prime common scale exposed by PF-107/PF-114 is present in each individual cusp chart, but the **canonical adjacent gluing offset differentiates it and makes it summable**.

## 1. Exact upper-half-plane normalization

Write the left finite-cuff geodesic as the semicircle of radius `r_a` centered at `0`. Parameterize it from its intersection `i r_a` with `x=0`. A point at hyperbolic arclength `a` has Euclidean coordinates

\[
\boxed{
(x,y)=\bigl(r_a\tanh a,\ r_a\operatorname{sech}a\bigr).
}
\tag{9}
\]

Indeed, writing `x=r_a sin(theta)`, `y=r_a cos(theta)`, the hyperbolic line element on the semicircle is `sec(theta) dtheta`, whose integral from `0` is `artanh(sin(theta))`.

Let the common-perpendicular semicircle have center `t` and radius `R`. Orthogonality of the two semicircles gives

\[
t^2=r_a^2+R^2.
\tag{10}
\]

For two orthogonal circles with centers `0,t`, the intersection has horizontal coordinate `r_a^2/t`. Comparing with (9) yields

\[
r_a=t\tanh a,
\qquad
R=t\operatorname{sech}a.
\tag{11}
\]

The same argument on the right gives

\[
r_b=(1-t)\tanh b,
\qquad
R=(1-t)\operatorname{sech}b.
\tag{12}
\]

Equating the two expressions for `R` proves

\[
\frac{t}{\cosh a}=\frac{1-t}{\cosh b},
\]

which is exactly (1); substituting back gives (2).

No prime arithmetic enters this calculation. It is a coordinate form of the standard one-cusp right-angled-pentagon geometry.

## 2. The ideal-pentagon factorization is one-parameter on each side

The vertical `x=t` meets the common-perpendicular circle at its top point `t+iR` and is perpendicular to it there. It therefore cuts the normalized ideal pentagon into two limiting Lambert quadrilaterals sharing that vertical.

On the left, the dilation

\[
z\longmapsto z/t
\]

is a hyperbolic isometry. Equations (11) give

\[
\frac{r_a}{t}=\tanh a,
\qquad
\frac{R}{t}=\operatorname{sech}a,
\]

so the image is precisely `Q(a)` in (3). On the right, reflection followed by dilation,

\[
z\longmapsto \frac{1-z}{1-t},
\]

produces `Q(b)`.

The same physical point of the central vertical has normalized heights `y/t` and `y/(1-t)` in the two charts. Their logarithmic relative scale is therefore, up to the choice of orientation,

\[
\log\frac{t}{1-t}
=\log\cosh a-\log\cosh b.
\]

Equivalently, it is the logarithm of the ratio of the two horocyclic spacings from the central split ray to the outer cusp rays. This proves (4).

The factorization is useful because it separates two questions that were mixed in the accepted clue:

\[
\boxed{
P(2a,2b,0)
\quad\rightsquigarrow\quad
Q(a)\ +\ \text{one cusp offset}\ +\ Q(b).
}
\tag{13}
\]

The local shape problem is one-parameter on each side; boundary coherence contributes the single scalar `sigma(a,b)`.

## 3. Exact collar conversion turns the clone offset into a first difference

Use the PF-114 indexing for the logarithmic meshes `h_n` and their shift-clone counterparts `h_n^+`. PF-032 gives the exact standard-collar identity

\[
\sinh\frac{\ell_n}{2}\,\sinh\frac{h_n}{2}=1.
\tag{14}
\]

Hence

\[
\boxed{
\cosh\frac{\ell_n}{2}=\coth\frac{h_n}{2}.
}
\tag{15}
\]

Define

\[
J(h)=\log\coth\frac h2.
\]

Then

\[
\log\cosh a_n=J(h_n),
\qquad
\sigma_n=J(h_n)-J(h_{n+1}).
\tag{16}
\]

Let

\[
R_n=\frac{h_n^+}{h_n},
\qquad
\delta_n=\log R_n.
\tag{17}
\]

PF-114 proves on a tail that

\[
0<R_n<R_{n+1}<1,
\qquad
\delta_n\nearrow0,
\qquad
\sum_n|\delta_{n+1}-\delta_n|<\infty,
\tag{18}
\]

and also

\[
\sum_n h_n^2<\infty.
\tag{19}
\]

Now split the universal collar function into its singular scale and a regular remainder:

\[
J(h)=\log\frac2h+E(h),
\qquad
E(h):=\log\!\left(\frac h2\coth\frac h2\right)
=\frac{h^2}{12}+O(h^4).
\tag{20}
\]

Therefore

\[
\begin{aligned}
\varepsilon_n
&:=J(h_n^+)-J(h_n)\\
&=-\delta_n+r_n,
\end{aligned}
\tag{21}
\]

where

\[
r_n=E(h_n^+)-E(h_n).
\]

Since `0<h_n^+<h_n` on the tail and `E(h)=O(h^2)`, (19) gives

\[
\boxed{
\sum_n|r_n|<\infty.
}
\tag{22}
\]

Combining (18), (21), and (22),

\[
\begin{aligned}
\sum_n|\varepsilon_n-\varepsilon_{n+1}|
&\le
\sum_n|\delta_{n+1}-\delta_n|
+\sum_n|r_n-r_{n+1}|\\
&<\infty.
\end{aligned}
\tag{23}
\]

Finally (16) gives the exact identity (8), so (23) proves (5).

PF-114 also proves

\[
\delta_n=-\frac1{p_n}+o(p_n^{-1}).
\tag{24}
\]

Thus (21)--(22), together with Euler's divergence of the reciprocal-prime sum, imply (6)--(7). The nonsummable part is the **single-chart common scale** `-delta_n`; the marked cusp interface sees only its adjacent difference.

## 4. Consequence for the accepted relative-operator clue

PF-114 identified the cross-cuff seam as the first pant-local object whose shift-clone **logarithmic** distortion keeps the nonsummable common mode `~1/p_n`. That made boundary coherence across infinitely many pants a plausible place where the mode might accumulate.

PF-119 removes the most direct scalar version of that obstruction. In the canonical cusp-normalized split (13), the interface placement is not controlled by the absolute chart scale `epsilon_n`; it is controlled by the difference

\[
\varepsilon_n-\varepsilon_{n+1},
\]

which is in `ell^1`. Therefore

\[
\boxed{
\text{nonsummable seam/common scale}
\not\Rightarrow
\text{nonsummable canonical cusp gluing offset}.
}
\tag{25}
\]

This is deliberately not a proof that the matched pants admit boundary-coherent `(1+o(1))`-bilipschitz homeomorphisms. The remaining local gate is now more specific: construct or obstruct maps

\[
Q(a_n)\longrightarrow Q(a_n^+)
\]

with controlled metric tensor and prescribed maps on the finite-cuff and central-vertical boundaries, uniformly as `a_n -> infinity`. If such one-parameter maps exist with distortion tending to one, (5) shows that their canonical cusp-interface translations themselves do not accumulate a new nonsummable scalar defect. One must still glue the doubled quadrilaterals, control the complete cusp/collar metric and volume density, and only then invoke a relative-Laplacian theorem.

So any negative answer to the accepted clue must now expose an **interior Jacobian/energy or genuinely nonlocal operator amplification**, not merely the additive accumulation of the natural cusp-split offset.

## 5. Prior art and novelty audit

The general geometry is classical, and no novelty is claimed for:

- the decomposition of a one-cusp pair of pants into degenerate right-angled hexagons/pentagons;
- upper-half-plane semicircle orthogonality or the formulas `tanh`, `sech`, `coth` arising from hyperbolic arclength and collars;
- the fact that hyperbolic pants are determined by their boundary lengths.

The closest comparison results remain broader but hypothesis-mismatched:

- Y. Minsky, *Bounded geometry for Kleinian groups*, Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`, Lemmas 8.2--8.3, treats degenerate right-angled hexagons with ideal vertices and gives coarse bilipschitz control for bounded additive changes of pants lengths. It does not provide the `K -> 1` modulus or the exact cusp-interface cancellation proved here.
- Y. Wu and H. Zhang, *Spectral gaps on thick part of moduli spaces*, arXiv:2501.09266 (2025), Propositions 8.15 and 8.18, construct explicit piecewise smooth Fermi-coordinate maps with metric-tensor error tending to zero when two boundary components stay fixed and uniformly thick while a bounded third component varies. Their theorem does not cover one cusp with both unbounded finite cuffs varying.
- PF-118 already imports Alessandrini--Disarlo's exact arc-distance/optimal continuous Lipschitz theorem, but that theorem does not supply the homeomorphic or boundary-parametrized map still required here.

Directed searches for the exact cotangent prime flute, the all-composite shift `p_n -> p_n+1`, the cusp split ratio (4), and an `ell^1` gluing-offset cancellation of the form (5) located no matching statement. The durable Mathia content is not a new theorem about arbitrary pants; it is the exact specialization

\[
\boxed{
\text{shift-clone cuff scale }\sim1/p_n
\quad\xrightarrow{\text{canonical cusp split}}\quad
\text{adjacent first difference in }\ell^1.
}
\tag{26}
\]

This is a negative/boundary result for the all-composite control. It weakens, rather than strengthens, any claim that the surviving local mode is intrinsically prime-specific or RH-relevant.

## 6. Audit / falsification core

The result has six independent gates:

1. normalize the ideal pentagon by sending its cusp to `infinity` and its two outer cusp rays to `x=0,1`; verify the half-cuff arclength parametrization (9);
2. use Euclidean orthogonality of hyperbolic geodesic semicircles to derive (11)--(12), hence the exact formulas (1)--(2);
3. split along `x=t` and check the two hyperbolic dilations give the one-parameter quadrilaterals (3), while the horocyclic spacing ratio gives (4);
4. use only PF-032's exact collar identity to rewrite the split offset as the discrete difference (16);
5. use PF-114's already-proved finite variation of `delta_n` and square summability of `h_n`, together with the elementary expansion (20), to obtain (23) and hence (5);
6. do **not** infer a homeomorphic/bilipschitz global identification, compact resolvent difference, Schatten class, scattering equivalence, determinant, or RH statement from the scalar offset summability alone.

A refutation of PF-119 must break one of steps 1--5. An operator-level obstruction remains entirely possible, but it must survive after this canonical boundary-offset cancellation is taken into account.

## References

- Y. N. Minsky, *Bounded geometry for Kleinian groups*, Invent. Math. 146 (2001), 143--192. DOI `10.1007/s002220100163`; arXiv:math/0105078.
- Y. Wu, H. Zhang, *Spectral gaps on thick part of moduli spaces*, arXiv:2501.09266 (2025), Section 8.3.
- D. Alessandrini, V. Disarlo, *Generalizing Stretch Lines for Surfaces with Boundary*, Int. Math. Res. Not. 2022 (23), 18919--18991. DOI `10.1093/imrn/rnab222`.
- PF-032, PF-107, PF-114, and PF-118 in this research ledger.
