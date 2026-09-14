# FD-115 — centered global discrepancy on a Farey parent cone is local-movie determined

**Status:** `EXACT-DERIVED + REPRESENTATION-CLASSIFICATION + GLOBAL-RANK-DECOMPOSITION + COMMON-MODE-BOUNDARY + NEGATIVE/ROUTE-RESTRICTION`.

`FD-114` shows that the complete denominator-truncated Stern--Brocot refinement movie inside one unimodular Farey parent interval is determined by the parent denominator ratio and scale at a fixed absolute horizon. It deliberately leaves an independently defined discrepancy residual or global rank placement as a possible second coordinate for `CLUE-ordered-plucker-refinement-transfer.md`.

There is a sharper exact restriction on that escape. Fix an interior unimodular parent edge

\[
A=\frac ab<B=\frac cd,
\qquad bc-ad=1,
\tag{1}
\]

and a Farey order `Q>=max(b,d)`. Let

\[
C_Q:=\sum_{q=2}^Q\varphi(q)
\tag{2}
\]

be the number of interior Farey fractions, let

\[
I_Q(x):=\#\{y\in\mathcal F_Q^\circ:y\le x\},
\tag{3}
\]

and use the `FD-001` discrepancy convention

\[
D_Q(x):=I_Q(x)-C_Qx.
\tag{4}
\]

Every visible fraction in `[A,B]` is represented uniquely by a primitive nonnegative ray

\[
x_{u,v}=\frac{ua+vc}{ub+vd},
\qquad
q_{u,v}=ub+vd\le Q.
\tag{5}
\]

Order these visible rays by their positions and define the local rank from the left parent

\[
\Lambda_Q(u,v)
:=
\#\left\{
(m,n):
\gcd(m,n)=1,
\ mb+nd\le Q,
\ A<x_{m,n}\le x_{u,v}
\right\}.
\tag{6}
\]

Then the global discrepancy on the entire visible descendant packet has the exact affine decomposition

\[
\boxed{
D_Q(x_{u,v})
=
D_Q(A)
+
\Lambda_Q(u,v)
-
C_Q\frac{v}{b(ub+vd)}.
}
\tag{7}
\]

Equivalently, if

\[
G:=B-A=\frac1{bd},
\qquad
y_{u,v}:=\frac{x_{u,v}-A}{G}
=\frac{vd}{ub+vd},
\tag{8}
\]

then

\[
\boxed{
D_Q(x_{u,v})
=
D_Q(A)+\Lambda_Q(u,v)-C_QG\,y_{u,v}.
}
\tag{9}
\]

The terms after `D_Q(A)` are already determined by the absolute-horizon local movie of `FD-114`: the visible primitive rays determine `Lambda_Q`, their order and normalized positions determine `y_(u,v)`, and `G,Q` determine the deterministic baseline `C_QG`. Therefore **the restriction of global Farey discrepancy to one parent cone is a common global offset plus a local-movie-determined profile**.

In particular, for any visible descendants `x_1,...,x_m` and coefficients with

\[
\sum_{j=1}^m\alpha_j=0,
\tag{10}
\]

we have

\[
\boxed{
\sum_{j=1}^m\alpha_jD_Q(x_j)
=
\sum_{j=1}^m\alpha_j
\bigl(\Lambda_Q(x_j)-C_QG\,y_j\bigr),
}
\tag{11}
\]

with no dependence on the absolute rank/discrepancy anchor at `A`. Thus pairwise discrepancy differences, parent-centered discrepancy, mean-centered descendant discrepancy, finite differences along the packet, and any other zero-sum linear discrepancy residual add **no independent coordinate** beyond the canonical local refinement movie. A Pluecker carrier built from such centered local discrepancy increments cannot escape the representation collapses of `FD-112`--`FD-114` merely by calling the second coordinate “global discrepancy”.

The surviving channel is narrower: a translation-sensitive construction may retain the single common-mode anchor `D_Q(A)` (equivalently the absolute rank placement `I_Q(A)`), and cross-horizon changes of that anchor remain genuinely outside the one-cone identity. The theorem does not remove those global channels.

## 1. The global rank increment is exactly the local visible-ray count

The unimodular parameterization in `FD-114` is a bijection between primitive nonnegative rays `(u,v)` and reduced fractions in `[A,B]`. At order `Q`, visibility is exactly

\[
ub+vd\le Q.
\tag{12}
\]

Hence every Farey fraction in the half-open interval `(A,x_(u,v)]` is one and only one ray counted by (6). No fraction outside the parent cone can lie numerically between the two endpoints. Therefore

\[
\boxed{
I_Q(x_{u,v})-I_Q(A)=\Lambda_Q(u,v).
}
\tag{13}
\]

This is the only rank input needed. Subtracting (4) at `A` from (4) at `x_(u,v)` gives

\[
D_Q(x_{u,v})-D_Q(A)
=
\Lambda_Q(u,v)-C_Q(x_{u,v}-A).
\tag{14}
\]

The displacement is also local. Using `bc-ad=1`,

\[
\begin{aligned}
x_{u,v}-A
&=
\frac{ua+vc}{ub+vd}-\frac ab\\
&=
\frac{v(bc-ad)}{b(ub+vd)}\\
&=
\frac{v}{b(ub+vd)}.
\end{aligned}
\tag{15}
\]

Equations (14) and (15) prove (7). Multiplying the displacement by `bd` gives the normalized position in (8), proving (9).

The right endpoint `B` is simply the ray `(0,1)`, so the same identity gives

\[
D_Q(B)-D_Q(A)
=
\Lambda_Q(0,1)-C_QG.
\tag{16}
\]

Thus even the total discrepancy change across the coarse parent interval is a primitive-ray count minus its deterministic uniform baseline. The only part of the absolute discrepancy vector not supplied by this local increment law is the common left-endpoint anchor.

## 2. Quotienting the common mode leaves no discrepancy degree of freedom

Let the visible descendants in `(A,B]` be

\[
x_1<\cdots<x_m,
\tag{17}
\]

and write

\[
L_j:=\Lambda_Q(x_j)-C_QG\,y_j.
\tag{18}
\]

Then (9) is the vector identity

\[
\boxed{
(D_Q(x_1),\ldots,D_Q(x_m))
=
D_Q(A)\,(1,\ldots,1)+(L_1,\ldots,L_m).
}
\tag{19}
\]

The second vector is determined by the visible packet. Passing to the quotient by the common translation direction `span{(1,...,1)}` therefore leaves a single predetermined point, not an additional residual family. Equivalently,

\[
D_Q(x_j)-D_Q(x_k)=L_j-L_k
\tag{20}
\]

for every pair.

This is the relevant representation kill test. If a proposed refinement vector contains a coordinate such as

\[
D_Q(x_{j+1})-D_Q(x_j),
\qquad
D_Q(x_j)-D_Q(A),
\tag{21}
\]

or a centered version `D_Q(x_j)-mean(D_Q(x_l))`, that coordinate is already a deterministic functional of the same local movie used for the Euclidean/refinement coordinates. Increasing the ambient vector dimension with several such residuals does not create a second independent information channel. Nonzero minors after a nonlinear embedding would again measure geometry of a deterministic image, not new arithmetic input.

A raw, translation-sensitive coordinate `D_Q(x_j)` is different. Equation (19) shows exactly what it can add: the common anchor `D_Q(A)`. A determinant or other antisymmetric statistic that changes under adding the same constant to all discrepancy coordinates may therefore retain that anchor. Such a construction is not killed here, but its claimed extra information must be attributed explicitly to the global common mode rather than to the descendant residual profile.

## 3. Representation scope and stress tests

The retained local data are the absolute Farey horizon `Q`, the parent edge scale/ratio encoded by `(b,d)` or equivalently `(r,G)`, and the canonical visible primitive-ray packet from `FD-114`. The nuisance tested here is only a common translation of the discrepancy coordinate. Under those controls, the centered global discrepancy profile is exactly fixed by (19).

Several scope points are essential.

First, this is not a claim that global Farey rank is “local” in general. Computing `D_Q(A)` can require information outside the cone, and correlations among the anchors of many parent intervals can retain global order. Equation (19) says only that **within one fixed parent cone**, all relative rank/discrepancy variation is local once the left anchor is given.

Second, the result does not declare the anchor independent in an information-theoretic sense. For a concrete Farey edge and `Q`, every quantity is ultimately arithmetic data determined by the edge and horizon. The operational statement is narrower and useful: the cone-counting identity supplies every centered descendant discrepancy without consulting any external rank placement, while one common absolute anchor remains outside that identity. No artificial matched pair of distinct Farey intervals with identical `(b,d,Q)` is asserted or required.

Third, cross-horizon observables remain open. For the same parent `A`, the difference `D_(Q_2)(A)-D_(Q_1)(A)` does not cancel in (19) unless a separate theorem controls it. Likewise a globally selected collection of parent cones can use the pattern of their anchors, and a source-conditioned selection rule can inject information not present in the canonical denominator cutoff.

Fourth, the interior convention avoids deterministic endpoint bookkeeping. Parent intervals touching `0/1` or `1/1` satisfy the same cone identity after the corresponding endpoint-count correction. No asymptotic estimate depends on that convention.

As a finite exact check, the identities were evaluated with rational arithmetic over every interior adjacent parent edge of `F_H` for `2<=H<=12`, every `H<=Q<=30`, and every visible descendant in the parent interval: 20,410 descendant instances satisfied (13)--(15) exactly. This computation is only a regression check; the proof is the algebra above.

## 4. Prior-art boundary and surviving route

The ingredients behind (13) are classical. Farey/Stern--Brocot intervals are unimodular cones, and ranking Farey fractions is naturally equivalent to counting primitive lattice points. Pawlewicz and Patrascu, *Order Statistics in the Farey Sequences in Sublinear Time and Counting Primitive Lattice Points in Polygons*, Algorithmica **55** (2009), 271--282, DOI `10.1007/s00453-008-9221-z`, is a direct algorithmic prior-art boundary for the rank/lattice-point connection. Rogelio Tomas Garcia, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140, DOI `10.3390/math13010140`, gives modern exact formulas and estimates for Farey rank and local discrepancy. The unimodular ray parameterization itself is already treated as classical in `FD-114`.

No novelty is claimed for primitive lattice counting, Farey rank, the elementary identity “rank difference minus uniform mass equals discrepancy difference”, or the fact that consecutive gaps determine adjacent discrepancy increments. The Mathia-specific durable content is the representation classification needed by the live Pluecker clue: **even when the discrepancy coordinate is defined globally using the full `F_Q`, its entire centered restriction to a canonical parent refinement packet is already determined by that packet.** The proposed “independent discrepancy residual” survives only if it retains the absolute common mode, couples different cones/horizons, or uses another source-conditioned quantity not erased by (11).

This does not yield a stronger Franel--Landau estimate, Möbius cancellation, or an RH consequence. It narrows the next representation test. A viable second coordinate must now be something like the absolute anchor `D_Q(A)` with a theorem that uses its cross-cone/cross-horizon structure, a source residual not reconstructible from local rank increments, or a genuinely nonlocal selection law. Repackaging parent-centered or mean-centered descendant discrepancy as a second local coordinate no longer passes the algebraic gate.

All load-bearing identities are derived directly from the definitions and `FD-114`'s exact unimodular parameterization, so no new external theorem is required in `SOURCES.md`.
