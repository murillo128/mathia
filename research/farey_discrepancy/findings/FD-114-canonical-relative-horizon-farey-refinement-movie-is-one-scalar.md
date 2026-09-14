# FD-114 — canonical relative-horizon Farey refinement movie is one-scalar

**Status:** `EXACT-DERIVED + REPRESENTATION-CLASSIFICATION + HORIZON-DEPENDENT-ANCESTRY + ONE-SCALAR-REFINEMENT-MOVIE + NEGATIVE/ROUTE-RESTRICTION`.

`FD-113` shows that any fixed or predeclared finite Stern--Brocot descendant template inside one Farey parent edge has only one affine-normalized shape parameter, even though a nonlinear embedding of that parameter can produce nonzero Plücker minors. It deliberately leaves open a natural escape: let the visible ancestry template vary with the Farey horizon itself.

For the canonical variation generated solely by the ordinary denominator cutoff, that escape also collapses. If

\[
A=\frac ab<B=\frac cd,
\qquad bc-ad=1,
\qquad H:=\max(b,d),
\tag{1}
\]

then the entire future local Farey refinement of the interval `[A,B]`, with insertion time normalized by the first Farey order containing both parents, is determined by the single denominator ratio

\[
r:=\frac bd,
\tag{2}
\]

or equivalently by the root split scalar from `FD-112`,

\[
s=\frac{d-b}{d+b},
\qquad
r=\frac{1-s}{1+s}.
\tag{3}
\]

More precisely, primitive rays `(u,v)\in\mathbb Z_{\ge0}^2` parameterize **all** reduced rationals in `[A,B]` by

\[
x_{u,v}=\frac{ua+vc}{ub+vd}.
\tag{4}
\]

Their denominator, relative birth time, and affine-normalized position are

\[
q_{u,v}=ub+vd,
\tag{5}
\]

\[
\boxed{
\tau_{u,v}:=\frac{q_{u,v}}H
=\frac{ur+v}{\max(r,1)},
}
\tag{6}
\]

and

\[
\boxed{
y_{u,v}:=\frac{x_{u,v}-A}{B-A}
=\frac{v}{ur+v}.
}
\tag{7}
\]

Consequently, at every relative horizon `t>=1`, the complete visible local packet is exactly

\[
\boxed{
\mathcal P_t(r)
=
\left\{(u,v):
\gcd(u,v)=1,
\ u,v\ge0,
\ \frac{ur+v}{\max(r,1)}\le t
\right\},
}
\tag{8}
\]

with order inside the interval determined by (7). Thus not only every fixed descendant fan but the **whole denominator-truncated refinement movie**—which rays have appeared, their insertion times, their order, normalized positions, normalized gaps, and every deterministic local statistic built from those data—factors through one scalar `r` once parent translation and scale are quotiented in the same way as `FD-113`.

The immediate consequence for `CLUE-ordered-plucker-refinement-transfer.md` is a sharper representation gate: **state-dependent ancestry does not become an independent residual coordinate merely because the state dependence is produced by the canonical Farey denominator cutoff.** A surviving second coordinate must depend on information outside this local cutoff movie, such as an independently defined discrepancy/source residual, global rank placement, cross-horizon source state, or another selection law not reconstructible from the parent edge and the canonical denominator threshold.

## 1. Unimodularity gives an exact primitive-ray parameterization

Let

\[
M=
\begin{pmatrix}
a&c\\
b&d
\end{pmatrix}.
\tag{9}
\]

Since `bc-ad=1`, we have `det M=-1`; hence `M` is unimodular over the integers. Equation (4) is simply the projectivization of

\[
\binom pq=M\binom uv
=
\binom{ua+vc}{ub+vd}.
\tag{10}
\]

A primitive ray `(u,v)` therefore maps to a primitive integer vector `(p,q)`: a common divisor of `p,q` would, after applying the integral inverse `M^{-1}`, divide both `u,v`.

Conversely, take any reduced fraction `p/q\in[A,B]`. The inverse coordinates are

\[
\boxed{
u=cq-dp,
\qquad
v=bp-aq.
}
\tag{11}
\]

The inequalities `p/q<=c/d` and `p/q>=a/b` imply `u,v>=0`. Because `M^{-1}` is integral and unimodular, `(u,v)` is primitive whenever `(p,q)` is primitive. Hence (4) is a bijection between primitive nonnegative rays and reduced rationals in the closed parent interval. The two axis rays give the endpoints; every interior fraction has `u,v>0`.

The same formula also proves that the parents are consecutive in `F_H`. Every interior reduced fraction has

\[
q=ub+vd\ge b+d>\max(b,d)=H,
\tag{12}
\]

so no interior rational is present when both endpoints first coexist. The canonical local refinement therefore starts at the intrinsic parent order `H` in (1), without an additional choice of ancestry template.

## 2. Denominator truncation makes the changing ancestry itself one-scalar

A reduced fraction `p/q` belongs to `F_Q` exactly when `q<=Q`; it first appears at order `Q=q`. Applying this to (5), the descendant ray `(u,v)` is visible at absolute horizon `Q` exactly when

\[
ub+vd\le Q.
\tag{13}
\]

Now write `b=rd` and divide by the canonical parent order

\[
H=d\max(r,1).
\tag{14}
\]

Then (13), with `Q=tH`, becomes exactly the scalar inequality in (8). Its birth time is (6), while its normalized position follows from `B-A=1/(bd)`:

\[
\begin{aligned}
\frac{x_{u,v}-A}{B-A}
&=
\frac{v}{ur+v}.
\end{aligned}
\tag{15}
\]

For `u>0`, putting `z=v/u` gives

\[
y=\frac{z}{r+z},
\tag{16}
\]

which is strictly increasing in `z`. Thus the ordered packet is also determined by `r`; no hidden numerator coordinate remains after the local affine quotient.

This yields an exact event-level factorization. Define the complete relative-horizon movie

\[
\mathfrak M(r)
:=
\left\{
\left(
\frac{ur+v}{\max(r,1)},
\frac{v}{ur+v},
(u,v)
\right):
\gcd(u,v)=1,\ u,v\ge0
\right\}.
\tag{17}
\]

The ray label is universal combinatorial control data; both physical coordinates of every event are functions of the same scalar `r`. Therefore any ancestry template obtained by retaining precisely those descendants born before a relative horizon `t`, even if its cardinality and tree shape change discontinuously with `t`, is a deterministic function of `(r,t)`.

This is the point not covered by `FD-113`. A fixed template there was conditioned on as control data. Here the canonical state-dependent template need not be conditioned on separately: its **selection law and complete change schedule** already factor through the same root split scalar.

## 3. At a fixed absolute horizon, the only extra parameter is parent scale

Using a common absolute Farey order `Q` instead of relative time does reintroduce a second local parameter, but it is not new ancestry information. Let

\[
G:=B-A=\frac1{bd}.
\tag{18}
\]

The visibility condition (13) becomes

\[
ur+v\le\frac Qd.
\tag{19}
\]

Since

\[
\left(\frac Qd\right)^2
=Q^2\frac{b}{d}\frac1{bd}
=Q^2rG,
\tag{20}
\]

we may write

\[
\boxed{
ur+v\le\sqrt{r\,Q^2G}.}
\tag{21}
\]

Thus at fixed `Q` the entire normalized local packet factors through `(r,Q^2G)`, equivalently through root split plus parent scale. The moving template can reveal scale if scale was previously discarded, but it does not manufacture a third local coordinate beyond information already carried by the parent edge.

This distinction matters for the clue's nuisance control. Parent scale is not globally irrelevant to Franel--Landau discrepancy, and the present theorem does not quotient it away universally. The claim is narrower: **ordinary horizon-dependent Stern--Brocot ancestry is a deterministic re-encoding of the parent ratio and scale.** Treating that changing template as an additional independent coordinate would double-count parent-edge information.

For example, the root mediant `(u,v)=(1,1)` has

\[
\tau_{1,1}=\frac{r+1}{\max(r,1)}\in(1,2],
\tag{22}
\]

which matches the elementary fact that its denominator is `b+d`: it appears strictly after the parent order and by twice that order. Deeper births satisfy the same exact rule, with no asymptotic approximation.

## 4. Stress tests, prior-art boundary, and surviving route

The result survives the main representation stress tests relevant to `FD-113`.

First, it does not rely on a finite-depth truncation: every primitive ray is present in (17), and (8) recovers any finite relative-horizon packet. Second, ties in the same relative birth time cause no ambiguity; they are still selected by the same scalar inequality and their spatial order is fixed by (16). Third, the argument is not a dimension count: the full event set can be combinatorially complicated, but its dependence on the parent state is explicitly one-parameter after relative normalization.

The boundaries are equally important. The theorem does **not** remove absolute parent location, global Farey rank, parent scale at a fixed absolute horizon, a discrepancy residual defined using the rest of `F_Q`, or a source-conditioned template chosen by data other than the denominator cutoff. It also does not prove that a nonlocal functional of the ordered split sequence is useless. It only closes the most canonical state-dependent-ancestry escape from `FD-113`.

The underlying ingredients are classical. Stern--Brocot/Farey mediant geometry, unimodular `SL_2(Z)` coordinates, and the interpretation of Farey points as primitive/visible lattice directions are standard; see, for example, Christophe Reutenauer, *On the Stern--Brocot expansion of real numbers*, Journal de théorie des nombres de Bordeaux **31** (2019), 697--722, DOI `10.5802/jtnb.1104`, and Florin P. Boca, Cristian Cobeli and Alexandru Zaharescu, *Distribution of lattice points visible from the origin*, Communications in Mathematical Physics **213** (2000), 433--470, DOI `10.1007/s002200000250`. No novelty is claimed for the cone parameterization, primitive-ray criterion, or denominator truncation themselves.

The Mathia-specific durable content is the representation classification relevant to the current refinement route: after `FD-113`, allowing the descendant template to vary **canonically with Farey order** still does not supply an independent shape coordinate. The complete normalized birth-and-position movie is already generated by the root split scalar, and at absolute order its extra dependence is exactly parent scale.

No Franel--Landau estimate or RH consequence follows from this classification. A viable continuation of the Plücker clue must now define the second coordinate outside the canonical local refinement movie and prove that it remains independent under the strongest realizable controls. An independently defined discrepancy/source residual remains the clearest version of that test; a globally conditioned ancestry rule may also survive if its selection cannot be reconstructed from `(r,G,Q)`.

All load-bearing identities above are derived directly, so no new external theorem is required in `SOURCES.md`.
