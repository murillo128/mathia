# PC-251 — growing-lower shared-upper defect is a weighted Farey collision matching

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `NEGATIVE/OBSTRUCTION` for the growing-lower regime left open by PC-249. Let `p<r<q` be distinct primes and let `K_{p,q}` and `K_{r,q}` be the native integer overlap packets of PC-245/PC-246. Define the shared-upper cross-Gram defect

\[
D_{p,r;q}:=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T}.
\tag{1}
\]

PC-249 proved that this vanishes once `q>pr-p-r`. Below that Frobenius threshold the defect does not become an unstructured new carrier: it is exactly a sparse weighted matching of lower-grid boundary collisions. If

\[
\mathcal C_{p,r;q}
=
\left\{(i,j):1\le i<p,\ 1\le j<r,\
\left\lfloor\frac{qi}{p}\right\rfloor
=
\left\lfloor\frac{qj}{r}\right\rfloor
\right\},
\tag{2}
\]

then

\[
\boxed{
D_{p,r;q}
=
-pr\sum_{(i,j)\in\mathcal C_{p,r;q}}
G\!\left(\frac{a_i}{p},\frac{b_j}{r}\right)
\delta_i^{(p)}\bigl(\delta_j^{(r)}\bigr)^T,
}
\tag{3}
\]

where `a_i=qi mod p`, `b_j=qj mod r`, `G(x,y)=min(x,y)-xy`, and `\delta_i^{(p)}=e_{i-1}-e_i`. Since `q>r>p`, the collision set is a matching, so

\[
\boxed{
\operatorname{rank}D_{p,r;q}=|\mathcal C_{p,r;q}|.
}
\tag{4}
\]

Moreover every collision lies on a bounded rational determinant layer

\[
1\le |ri-pj|
\le
\left\lfloor\frac{pr-p-r}{q}\right\rfloor.
\tag{5}
\]

Thus the first pre-threshold band can only use determinant-one/Farey-neighbor collisions, and the native normalized defect is bounded by `sqrt(pr)/q`. Consequently a non-vanishing normalized pairwise shared-upper signal requires both lower scales to be comparable with the upper scale. Even there, the carrier itself is source-blind rational partition geometry rather than a prime-specific or zeta-specific invariant.

## 1. Exact setup: two lower partitions seen through one upper grid

Use the interval realization of PC-249. For `a<b`, the `b x a` packet satisfies

\[
K_{a,b}(u,t)
=
a\left|
[u,u+1)\cap
\left[\frac{bt}{a},\frac{b(t+1)}a\right)
\right|.
\tag{6}
\]

Fix `p<r<q` and write the lower cells in the common `q`-row coordinate as

\[
A_t=\left[\frac{qt}{p},\frac{q(t+1)}p\right),
\qquad
B_s=\left[\frac{qs}{r},\frac{q(s+1)}r\right).
\tag{7}
\]

Then

\[
(K_{p,q}^{*}K_{r,q})_{t,s}
=pr\sum_{u=0}^{q-1}
|[u,u+1)\cap A_t|\,
|[u,u+1)\cap B_s|,
\tag{8}
\]

whereas the direct lower-lower packet gives

\[
(qK_{p,r}^{T})_{t,s}
=pr|A_t\cap B_s|.
\tag{9}
\]

On a unit `q`-cell containing no boundary from one of the two lower meshes, the corresponding indicator is constant. Conditional averaging on that cell therefore preserves the direct pairing exactly. The only cells contributing to (1) are those containing simultaneously one interior `p`-boundary and one interior `r`-boundary.

Because consecutive `p`-boundaries are separated by `q/p>1`, and consecutive `r`-boundaries by `q/r>1`, a unit cell contains at most one boundary of each type. Hence the collision relation (2) is a matching: no `i` and no `j` can occur twice.

## 2. A double-boundary cell is exactly the Dirichlet Green kernel

Take a collision `(i,j)` in the common unit cell `C_u=[u,u+1)`. Since `q` is coprime to `p` and `r`, neither boundary is integral. Write

\[
qi=pu+a_i,
\qquad
qj=ru+b_j,
\qquad
1\le a_i<p,\quad 1\le b_j<r.
\tag{10}
\]

After translating `C_u` to `[0,1)`, the two cut positions are

\[
x=\frac{a_i}{p},
\qquad
y=\frac{b_j}{r}.
\tag{11}
\]

Suppose first that `x<y`. In the two adjacent `p`-cells and two adjacent `r`-cells, the product-of-averages matrix minus the exact overlap matrix is

\[
\begin{pmatrix}
xy-x & x(1-y)\\
(1-x)y-(y-x) & (1-x)(1-y)-(1-y)
\end{pmatrix}
=
-x(1-y)
\begin{pmatrix}
1&-1\\-1&1
\end{pmatrix}.
\tag{12}
\]

For `y<x` the same calculation gives `-y(1-x)` times the same signed incidence outer product. Both cases are

\[
-G(x,y)\,
\delta_i^{(p)}\bigl(\delta_j^{(r)}\bigr)^T,
\qquad
G(x,y)=\min(x,y)-xy.
\tag{13}
\]

Multiplying by the `pr` normalization in (8)--(9) and summing the disjoint collision cells proves (3). The kernel `G` is the standard Dirichlet Green kernel on the unit interval (equivalently the Brownian-bridge covariance); it is not new arithmetic structure introduced by the prime-circle construction.

The weights are in fact elementary integers after the native normalization:

\[
pr\,G\!\left(\frac{a}{p},\frac{b}{r}\right)
=
\begin{cases}
a(r-b),& ar<bp,\\
b(p-a),& bp<ar.
\end{cases}
\tag{14}
\]

Equality cannot occur for interior residues because `p` and `r` are coprime. Thus the complete pre-threshold correction consists only of positive integral edge weights attached to a sparse matching of path incidences.

## 3. Exact rank and bounded determinant layers

Let `B_p` be the oriented incidence matrix of the length-`p` path, whose `i`th column is `\delta_i^{(p)}`, and similarly for `B_r`. Restrict these matrices to the collision indices. Since every subset of path-incidence columns is linearly independent and the collision weights in (14) are strictly positive, (3) factors as

\[
D_{p,r;q}=-pr\,B_{p,\mathcal C}M_{\mathcal C}B_{r,\mathcal C}^{T},
\tag{15}
\]

where `M_C` is a positive diagonal matrix after ordering the matching. Both incidence factors have full column rank, so (4) follows immediately.

The same collision equations give a sharper arithmetic description of the support. Multiplying the two equations in (10) by `r` and `p` and subtracting yields

\[
\boxed{
q(ri-pj)=ra_i-pb_j.
}
\tag{16}
\]

The integer `h=ri-pj` is nonzero for interior indices. Since

\[
|ra_i-pb_j|\le pr-p-r,
\tag{17}
\]

every collision obeys (5). For any fixed nonzero `h`, the Diophantine equation `ri-pj=h` has at most one solution with `1\le i<p`, `1\le j<r`: two solutions would differ by `i-i'=pt`, impossible inside the proper index range unless `t=0`. Therefore

\[
\boxed{
|\mathcal C_{p,r;q}|
=
\operatorname{rank}D_{p,r;q}
\le
2\left\lfloor\frac{pr-p-r}{q}\right\rfloor.
}
\tag{18}
\]

Equation (18) recovers PC-249 as the zero-collision case: if `q>pr-p-r`, the right-hand side is zero and the shared-upper cross-Gram collapses exactly to `qK_{p,r}^T`.

## 4. The first pre-threshold band is Farey determinant-one geometry

Put `g=pr-p-r`. If

\[
\frac g2<q\le g,
\tag{19}
\]

then `floor(g/q)=1`. Hence any collision that exists in this band must satisfy

\[
|ri-pj|=1.
\tag{20}
\]

The fractions `i/p` and `j/r` are reduced, and (20) is the classical determinant-one condition. Since `p+r>r`, such a pair is adjacent in the Farey sequence of order `r`. Therefore the first possible deviation from the PC-249 collapse is supported only on Farey-neighbor edges. More generally, whenever

\[
\frac{g}{H+1}<q\le\frac gH,
\tag{21}
\]

the support lies inside the finite determinant layers `1\le|ri-pj|\le H`.

This is exactly the kind of classical rational geometry already encountered in PC-007: the reappearance of Farey determinant layers is a classicalization warning, not a new RH criterion. In particular, the present statement does **not** identify its defect with the Franel--Landau discrepancy or import their RH equivalences.

## 5. Native normalization forces all three scales to be comparable

Normalize the transfer packets by

\[
S_{a,b}=\frac{K_{a,b}}{\sqrt{ab}}
\tag{22}
\]

and define

\[
\Delta_{p,r;q}
:=
S_{p,q}^{*}S_{r,q}-S_{p,r}^{T}
=
\frac{D_{p,r;q}}{q\sqrt{pr}}.
\tag{23}
\]

From (3),

\[
\Delta_{p,r;q}
=-\frac{\sqrt{pr}}q
B_{p,\mathcal C}M_{\mathcal C}B_{r,\mathcal C}^{T},
\tag{24}
\]

where the diagonal entries of `M_C` are `G(x,y)`. The path incidence matrix has operator norm at most `2`, while `0<G(x,y)\le1/4`. Therefore

\[
\boxed{
\|\Delta_{p,r;q}\|_{2}
\le
\frac{\sqrt{pr}}q.
}
\tag{25}
\]

Thus `pr=o(q^2)` forces the complete normalized pairwise defect to zero. Since `p,r<q`, an `O(1)` native pairwise signal can survive only when `pr=Theta(q^2)`, which forces both lower scales to be comparable with the upper scale. In particular, merely allowing one lower prime to grow does not evade the fixed-lower collapse of PC-249 if the product of the two lower scales remains `o(q^2)`.

There is a useful tension between (18) and (25). Near the Frobenius threshold `pr` is only of order `q`, so the support has just begun to appear on small determinant layers while its normalized operator size is at most `O(q^{-1/2})`. By the time the normalized defect can be macroscopic, all three scales are comparable and many determinant layers may participate; the pairwise carrier has not acquired a distinguished critical normalization on the way.

## 6. Adversarial controls and novelty audit

The derivation used the prime-circle source only to obtain the native overlap packets. Once those packets are present, (3)--(25) use uniform rational partitions, coprimality, path incidences, floor collisions, and the elementary kernel `min(x,y)-xy`. The same statements hold for matched artificial all-one packets built from pairwise-coprime composite denominators. Therefore the collision carrier itself cannot distinguish the prime source from an admissible source-blind control.

The closest prior-art structures are classical rather than RH-specific. Intersections of floor/Beatty sequences study the same kind of coincident integer cells; rational mechanical and Christoffel-word theory organizes the associated grid paths; non-nested `L^2` projection theory studies transfer between unrelated partitions; and determinant-one rational pairs are Farey geometry. The exact packet identity (3) is a project-local specialization derived here, but absence of this notation in the literature is not evidence of mathematical novelty. No novelty is claimed for the Green kernel, Farey adjacency, floor collisions, or non-nested projection algebra.

The result also fails the direct RH-mechanism tests in the line mandate. No complex spectral parameter `s`, gamma factor, functional equation, critical-line symmetry, or zero-detecting analytic continuation appears. The matched composite control reproduces the entire pairwise defect. Accordingly this is an obstruction/frontier result, not evidence for a new zeta mechanism.

## 7. What remains open after PC-249 and PC-251

PC-249 closed fixed finite lower scales beyond a finite Frobenius threshold. PC-251 now resolves the immediate pre-threshold behavior and sharply narrows the generic growing-lower escape: the pairwise shared-upper defect is a weighted collision matching of rank at most `2 floor((pr-p-r)/q)`, and its native normalized norm vanishes whenever `pr=o(q^2)`.

The surviving regime for this particular pairwise construction is therefore the genuinely simultaneous one `p,r,q` all of comparable scale. Even there, equations (3), (16), and (18) show that its support is still classical rational determinant geometry and source-blind under matched controls. A future positive mechanism would have to use information not exhausted by this pairwise conditional-expectation defect: for example higher-order rectangular relations before pairwise Gram compression, several independent upper scales whose joint relation is not reducible to these matchings, a native non-uniform composite/source mask, or an infinite-dimensional limit retaining more than the finite determinant-layer data.

This finding does not rule out those regimes, and it does not prove that the comparable-scale collision family is useless after nonlinear or higher-order coupling. It rules out treating the mere appearance of pre-Frobenius shared-upper collisions, or the growth of their pairwise rank, as a new prime-circle/RH carrier by itself.
