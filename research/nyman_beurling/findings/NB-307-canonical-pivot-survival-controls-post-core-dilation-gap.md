# NB-307 — canonical pivot survival controls the post-core projected-dilation gap

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-014, NB-290, NB-303, NB-306
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + PROJECTED-DILATION + SINGULAR-SPECTRUM + GENERALIZED-EIGENVALUES + GRAM-SCHMIDT-PIVOTS + DETERMINANT-LOWER-BOUND + POST-CORE-GAP + TARGET-RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-306` identifies the complete unit right-singular subspace of the projected integer-dilation operator

\[
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\]

as

\[
U_q,
\qquad
q:=\left\lfloor\frac Nm\right\rfloor,
\qquad 2\le m\le N.
\]

Thus the exact norm-one core disappears when `m>N/2`, but `NB-306` does not quantify how far the remaining singular spectrum lies below one.

The present finding gives an exact defect pencil on the orthogonal complement of that core and ties its determinant to the canonical Gram--Schmidt pivots of `NB-290`.

Let

\[
J_{N,m}:=(I-P_{U_N})A_m|_{U_N},
\qquad
H_{N,m}:=U_N\ominus U_q.
\tag{1}
\]

Since `A_m` is an isometry,

\[
\boxed{
I-T_{N,m}^*T_{N,m}=J_{N,m}^*J_{N,m}.
}
\tag{2}
\]

For `j=q+1,...,N`, define

\[
r_j:=(I-P_{U_q})g_j\in H_{N,m},
\qquad
s_j:=(I-P_{U_N})g_{mj}\in U_N^\perp,
\tag{3}
\]

and the Gram matrices

\[
S=(\langle r_i,r_j\rangle)_{i,j=q+1}^N,
\qquad
R=(\langle s_i,s_j\rangle)_{i,j=q+1}^N.
\tag{4}
\]

Then `S,R` are positive definite, and the positive spectrum of the singular-value defect on `H_(N,m)` is exactly the generalized spectrum of `(mR,S)`:

\[
\boxed{
\operatorname{spec}\!\left((I-T_{N,m}^*T_{N,m})|_{H_{N,m}}\right)
=
\operatorname{spec}_{\rm gen}(mR,S).
}
\tag{5}
\]

In particular, writing `s_post(N,m)` for the largest singular value of `T_(N,m)` on `H_(N,m)`,

\[
\boxed{
1-s_{\rm post}(N,m)^2
=
m\,\lambda_{\min}(R,S).
}
\tag{6}
\]

For the canonical innovations

\[
w_n=(I-P_{U_{n-1}})g_n,
\qquad
\sigma_n=\|w_n\|>0,
\]

and the multiplicative survival coefficients of `NB-290`,

\[
c_{m,n}:=\frac{\sqrt m\,\sigma_{mn}}{\sigma_n}\in(0,1],
\tag{7}
\]

one moreover has the determinant bound

\[
\boxed{
\det\!\left((I-T_{N,m}^*T_{N,m})|_{H_{N,m}}\right)
\ge
\prod_{j=q+1}^N c_{m,j}^2.
}
\tag{8}
\]

Because every defect eigenvalue lies in `(0,1]`, equation (8) yields the pointwise post-core spectral gap

\[
\boxed{
1-s_{\rm post}(N,m)^2
\ge
\prod_{j=q+1}^N c_{m,j}^2.
}
\tag{9}
\]

In the first post-core strip `N/2<m<=N`, one has `q=1` and `U_1={0}`, so `H_(N,m)=U_N` and `s_post(N,m)=beta_(N+1)(m)`. Hence

\[
\boxed{
1-\beta_{N+1}(m)^2
=
m\lambda_{\min}(R,S)
\ge
\prod_{j=2}^N c_{m,j}^2,
\qquad \frac N2<m\le N.
}
\tag{10}
\]

Thus the first quantitative obstruction after the exact unit plateau is no longer an unspecified cross-Gram singular value: it is controlled by the multiplicative survival of the canonical Nyman pivots. A useful lower bound on the product in (10), equivalently an upper bound on

\[
-\sum_{j=2}^N\log c_{m,j},
\]

would force an explicit gap below one immediately after the core disappears.

`NB-290` alone supplies only `0<c_(m,j)<=1`; it does not give the lower bounds required here. The result remains entirely source-side and does not establish target occupation, a finite-section Nyman-distance rate, or the Riemann hypothesis.

## 1. The defect operator is exactly the escaped dilation energy

For `v in U_N`, orthogonal decomposition across `U_N` gives

\[
A_mv=P_{U_N}A_mv+(I-P_{U_N})A_mv
=T_{N,m}v+J_{N,m}v.
\]

Since `A_m` is an isometry,

\[
\|v\|^2
=
\|T_{N,m}v\|^2+\|J_{N,m}v\|^2.
\tag{11}
\]

Polarization yields equation (2):

\[
I-T_{N,m}^*T_{N,m}=J_{N,m}^*J_{N,m}.
\]

`NB-306` proved

\[
\ker(I-T_{N,m}^*T_{N,m})=U_q.
\]

Equation (2) therefore also gives

\[
\ker J_{N,m}=U_q.
\tag{12}
\]

Because `J^*J` is self-adjoint, the orthogonal complement

\[
H_{N,m}=U_N\ominus U_q
\]

is invariant, and `J^*J` is positive definite there. This is precisely the part of the source on which the unit singular-value core has disappeared.

## 2. An exact generalized-eigenvalue pencil on the post-core quotient

Finite independence of the canonical generators, established in `NB-014` and used in `NB-290`, gives `sigma_j>0`. Consequently

\[
r_{q+1},\ldots,r_N
\]

form a basis of `H_(N,m)`: they are the images of the successive independent generators modulo `U_q`.

The exact covariance identity from `NB-290` is

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right).
\tag{13}
\]

Since `m<=N`, the compensator `g_m` lies in `U_N`. Therefore

\[
J_{N,m}g_j
=
\sqrt m\,(I-P_{U_N})g_{mj}
=
\sqrt m\,s_j.
\tag{14}
\]

Moreover `J` vanishes on `U_q`, so

\[
\boxed{J_{N,m}r_j=\sqrt m\,s_j.}
\tag{15}
\]

For

\[
v=\sum_{j=q+1}^Na_jr_j,
\]

we have

\[
\|v\|^2=a^*Sa,
\qquad
\|Jv\|^2=m\,a^*Ra.
\tag{16}
\]

Combining (11) and (16),

\[
\frac{\|v\|^2-\|T_{N,m}v\|^2}{\|v\|^2}
=
m\frac{a^*Ra}{a^*Sa}.
\tag{17}
\]

This proves the generalized-spectrum identity (5), and minimization of the Rayleigh quotient proves (6).

Notice that this is an exact finite-dimensional description, not a norm estimate. Once the unit core is quotiented out, every singular-value defect is encoded by the pair of residual Gram matrices `(R,S)`.

## 3. Canonical pivots lower-bound the defect determinant

The denominator Gram `S` has an exact pivot factorization. Orthogonalizing

\[
r_{q+1},r_{q+2},\ldots,r_N
\]

inside `H_(N,m)` gives the same successive distances as orthogonalizing

\[
g_{q+1},g_{q+2},\ldots,g_N
\]

against the preceding canonical sections. Therefore

\[
\boxed{
\det S=\prod_{j=q+1}^N\sigma_j^2.
}
\tag{18}
\]

For `R`, orthogonalize the vectors

\[
s_j=P_{U_N^\perp}g_{mj}
\]

in increasing `j`. The Gram--Schmidt residual of `s_j` relative to the previous `s_i` has norm equal to

\[
\operatorname{dist}\!\left(
 g_{mj},
 U_N+\operatorname{span}\{g_{m(q+1)},\ldots,g_{m(j-1)}\}
\right).
\tag{19}
\]

Because `j>=q+1` and `q=floor(N/m)`, one has `mj>N`. Also every previous product index is strictly below `mj`. Hence

\[
U_N+\operatorname{span}\{g_{m(q+1)},\ldots,g_{m(j-1)}\}
\subseteq U_{mj-1}.
\tag{20}
\]

Distance to the smaller subspace in (20) is at least distance to `U_(mj-1)`, so the residual norm in (19) is at least

\[
\operatorname{dist}(g_{mj},U_{mj-1})=\sigma_{mj}.
\]

Multiplying the squared Gram--Schmidt pivots gives

\[
\boxed{
\det R\ge\prod_{j=q+1}^N\sigma_{mj}^2.
}
\tag{21}
\]

Let

\[
d:=\dim H_{N,m}=N-q,
\]

and let `delta_1,...,delta_d` be the eigenvalues of the positive defect operator `(I-T^*T)|_H`. Equation (5) gives

\[
\prod_{\ell=1}^d\delta_\ell
=
m^d\frac{\det R}{\det S}.
\tag{22}
\]

Using (18), (21), and (7),

\[
\prod_{\ell=1}^d\delta_\ell
\ge
\prod_{j=q+1}^N
\frac{m\sigma_{mj}^2}{\sigma_j^2}
=
\boxed{
\prod_{j=q+1}^Nc_{m,j}^2.
}
\tag{23}
\]

This proves (8).

Finally, `T_(N,m)` is a contraction, so every `delta_l` belongs to `(0,1]`. For numbers in `(0,1]`, their product is no larger than their minimum. Therefore

\[
\delta_{\min}
\ge
\prod_{\ell=1}^d\delta_\ell
\ge
\prod_{j=q+1}^Nc_{m,j}^2,
\]

which proves (9).

## 4. The first post-core strip

Suppose

\[
\frac N2<m\le N.
\]

Then `q=floor(N/m)=1`, and by convention `U_1={0}`. `NB-306` says there is no exact unit singular direction at all, so

\[
H_{N,m}=U_N,
\qquad
s_{\rm post}(N,m)=\|T_{N,m}\|=\beta_{N+1}(m).
\]

Equation (6) becomes the exact identity

\[
\boxed{
1-\beta_{N+1}(m)^2
=m\lambda_{\min}(R,S).
}
\tag{24}
\]

Equation (9) then yields

\[
\boxed{
1-\beta_{N+1}(m)^2
\ge
\prod_{j=2}^Nc_{m,j}^2.
}
\tag{25}
\]

This is the first explicit bridge between the endpoint geometry of `NB-306` and the canonical multiplicative-pivot contraction of `NB-290`.

The bound can be weak: a single very small `c_(m,j)` can make the product tiny. That is not a defect in the proof but a precise statement of the remaining quantitative source problem. The relevant question is whether the actual Nyman pivots satisfy enough *lower* multiplicative survival across the moving band to stop

\[
\sum_{j=q+1}^N -\log c_{m,j}
\]

from becoming too large.

## 5. Relation to the current source transition

The source-side picture is now more structured than the interval left by `NB-306` alone.

At the left endpoint, `NB-306` gives an exact unit singular core `U_(floor(N/m))`. On the orthogonal quotient, the complete defect spectrum is the generalized spectrum of `(mR,S)`. Its determinant is bounded below by the product of canonical pivot-survival coefficients. At the right endpoint, `NB-303` still gives generic decay once `m/N^2 -> infinity`.

Thus any attempt to quantify the transition through

\[
N/2<m\lesssim N^2
\]

can now attack a concrete multiplicative metric invariant rather than an opaque projected-dilation matrix. Two possible outcomes are informative:

1. A lower bound on `prod c_(m,j)^2` in a useful moving regime would force a spectral gap below one there.
2. A construction showing that the product can collapse rapidly would identify canonical pivot absorption as a genuine mechanism allowing near-isometric post-core directions.

The result does not make either assertion yet.

## 6. What this does not prove

The finding is source-side. In particular it does **not** show that the moving first-free Ford datum occupies the singular directions detected here. It does not remove the sample conditioning or null-space issues isolated in `NB-284`--`NB-299`, does not bound the finite-section excess `mathfrak A_M`, and does not produce an Nyman-distance rate.

It also does not follow from `NB-290` that the product in (25) is bounded away from zero. `NB-290` gives the upper bound `c_(m,j)<=1`; the present application requires lower control. Reversing that inequality would invalidate the argument.

Finally, equation (25) is deliberately a determinant-based certificate. It may be much smaller than the true least defect eigenvalue. The exact pencil (24), rather than the product lower bound alone, is the sharper object if additional information on the residual Grams becomes available.

## 7. Prior-art audit

A fresh search on 2026-09-23 again found the standard Nyman--Beurling/Baez-Duarte Hilbert-space and semigroup background, including Bagchi's survey and Baez-Duarte's arithmetical reformulations, together with recent work of Carvill on Gram structure and decay along multiplicative ladders. Those sources motivate the setting but are not load-bearing for the proof above.

The audit did not identify, in the material reviewed, this specific finite-section statement: quotienting the exact unit core of projected integer dilation, representing the remaining singular-value defect by the generalized residual-Gram pencil `(mR,S)`, and lower-bounding its determinant by the canonical pivot-survival product. This is an audit statement, not a claim of bibliographic novelty.

No new external proof dependency is introduced, so `SOURCES.md` does not require an update.

## 8. Next discriminant

The immediate source-side discriminant is now

\[
\boxed{
\mathcal P_{N,m}
:=
\prod_{j=q+1}^Nc_{m,j}^2
=
\exp\!\left(-2\sum_{j=q+1}^N[-\log c_{m,j}]\right).
}
\tag{26}
\]

The next useful pass should determine whether the actual Nyman system admits a nontrivial lower bound for `mathcal P_(N,m)` in any moving portion of the post-core strip, or whether explicit arithmetic structure forces it to collapse. Either result would sharpen the currently wide gap between the exact linear-scale plateau of `NB-306` and the superquadratic decay regime of `NB-303`.
