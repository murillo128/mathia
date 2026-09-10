# PC-253 — growing shared-upper collision rank is an oriented modular-triangle discrepancy

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the comparable-scale collision regime left open by PC-251. Let

\[
2<p<r<q
\]

be distinct primes and let

\[
D_{p,r;q}:=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T}
\tag{1}
\]

be the native shared-upper cross-Gram defect of PC-251. Write

\[
H:=\left\lfloor\frac{pr-p-r}{q}\right\rfloor,
\qquad
\ell\equiv-q r^{-1}\pmod p,
\qquad 1\le \ell<p,
\tag{2}
\]

and for `1<=h<p` let

\[
y_h:=\langle \ell h\rangle_p\in\{1,\ldots,p-1\}
\tag{3}
\]

be the least positive residue. Then the positive determinant layers supporting the PC-251 collision matching are exactly

\[
\boxed{
1\le h\le H,
\qquad
qh+r y_h<pr.
}
\tag{4}
\]

Equivalently, if

\[
\Lambda_\ell:=\{(x,y)\in\mathbb Z^2:y\equiv \ell x\pmod p\}
\tag{5}
\]

and

\[
T_{p,r,q}:=\{(x,y)\in\mathbb R_{>0}^2:qx+ry<pr\},
\tag{6}
\]

then

\[
\boxed{
\operatorname{rank}D_{p,r;q}
=2\,\#(\Lambda_\ell\cap T_{p,r,q}).
}
\tag{7}
\]

Thus the first scalar statistic of the genuinely growing PC-251 carrier is not an unstructured three-prime quantity: it is an **oriented rank-one congruence-lattice discrepancy in a rational triangle**. The orientation matters sharply. If `q≡r (mod p)`, the defect vanishes exactly, even far below the Frobenius threshold and with all three scales comparable. If `q≡-r (mod p)`, its rank and weights admit closed forms and can be macroscopic. This recovers a sign/orientation channel that the centered pairwise `p`-based singular spectra of PC-246 erase, but the resulting support/counting problem is itself classical rational-lattice geometry rather than a new RH mechanism.

## 1. Reparameterizing the PC-251 collision matching

PC-251 proves that a collision is a pair

\[
(i,j),\qquad 1\le i<p,\quad 1\le j<r,
\tag{8}
\]

for which

\[
\left\lfloor\frac{qi}{p}\right\rfloor
=
\left\lfloor\frac{qj}{r}\right\rfloor,
\tag{9}
\]

and that its determinant layer

\[
h:=ri-pj
\tag{10}
\]

is nonzero and obeys

\[
1\le |h|\le H.
\tag{11}
\]

For a positive layer `h`, the Diophantine equation `ri-pj=h` has at most one solution in the ranges (8). Because `h<p<r`, it in fact has the unique candidate

\[
i_h=\langle r^{-1}h\rangle_p,
\qquad
j_h=\frac{ri_h-h}{p},
\tag{12}
\]

with both coordinates interior.

Assume that this candidate is a collision and put

\[
u=\left\lfloor\frac{qi_h}{p}\right\rfloor
=
\left\lfloor\frac{qj_h}{r}\right\rfloor,
\tag{13}
\]

\[
a_h:=qi_h-pu\in\{1,\ldots,p-1\},
\qquad
b_h:=qj_h-ru\in\{1,\ldots,r-1\}.
\tag{14}
\]

The residue identity from PC-251 is

\[
qh=ra_h-pb_h.
\tag{15}
\]

Reducing modulo `p` gives

\[
a_h\equiv q r^{-1}h\pmod p.
\tag{16}
\]

With `y_h=p-a_h`, equations (2)--(3) therefore give exactly

\[
a_h=p-y_h.
\tag{17}
\]

Substituting into (15),

\[
\boxed{
b_h=\frac{r(p-y_h)-qh}{p}.}
\tag{18}
\]

The numerator is automatically divisible by `p`. The upper bound `b_h<r` is automatic because `y_h,h>0`; hence the candidate is a genuine collision precisely when `b_h>0`, which is (4).

Conversely, if (4) holds, equations (12), (17), and (18) give positive interior residues and

\[
qi_h=pu+a_h,
\qquad
qj_h=ru+b_h
\tag{19}
\]

for the same integer `u`, so (9) follows. Thus (4) is an if-and-only-if characterization, not only a necessary bound.

## 2. The support is a modular lattice inside one rational triangle

The condition `y_h≡ell h (mod p)` places `(h,y_h)` in `Lambda_ell`, while (4) places it in `T_{p,r,q}`. Conversely every lattice point in the triangle has

\[
0<x<\frac{pr}{q}<p,
\qquad
0<y<p,
\tag{20}
\]

because `q>r`. Hence its coordinates are exactly one of the pairs `(h,y_h)` above. Positive collisions are therefore in bijection with

\[
\Lambda_\ell\cap T_{p,r,q}.
\tag{21}
\]

Reflection in the two lower partitions,

\[
(i,j)\longmapsto(p-i,r-j),
\tag{22}
\]

sends determinant layer `h` to `-h` and preserves the collision condition. There is no zero determinant layer for interior reduced fractions. PC-251 proves that the collision set is a matching and that its cardinality equals the rank of `D_{p,r;q}`. Thus positive and negative layers occur in pairs and (7) follows.

The lattice `Lambda_ell` has covolume `p`, whereas

\[
\operatorname{area}(T_{p,r,q})
=\frac12\frac{pr}{q}\,p
=\frac{p^2r}{2q}.
\tag{23}
\]

If

\[
E_{p,r,q}(\ell)
:=\#(\Lambda_\ell\cap T_{p,r,q})-\frac{pr}{2q},
\tag{24}
\]

then the exact rank identity can be written

\[
\boxed{
\operatorname{rank}D_{p,r;q}
=\frac{pr}{q}+2E_{p,r,q}(\ell).
}
\tag{25}
\]

Equation (25) is a decomposition into the area/covolume main term and a genuine lattice-point discrepancy. It does **not** assert that the discrepancy is small uniformly in this moving-modulus regime.

## 3. The collision weights are polynomially weighted lattice data

For a positive collision, equation (15) gives `ra_h>pb_h`, so the PC-251 Green-kernel coefficient is

\[
pr\,G\!\left(\frac{a_h}{p},\frac{b_h}{r}\right)
=b_h(p-a_h).
\tag{26}
\]

Using (17)--(18), its positive integer weight is therefore

\[
\boxed{
w_h
=y_h b_h
=\frac{y_h\bigl(r(p-y_h)-qh\bigr)}{p}.
}
\tag{27}
\]

The reflected `-h` collision has residues `(p-a_h,r-b_h)`. Since

\[
G(1-x,1-y)=G(x,y),
\tag{28}
\]

it carries exactly the same weight. Hence not only the rank but the complete unordered weight packet is a polynomially weighted statistic of the same modular-triangle lattice points. The remaining matrix information is where the corresponding path-incidence vectors indexed by `(i_h,j_h)` are placed.

This distinction matters: (7) classicalizes collision **multiplicity**, and (27) classicalizes scalar moments that depend only on the lattice points and polynomial weights. It does not identify every ordered/noncommutative statistic of the full matching matrix with a scalar lattice count.

## 4. Two exact congruence sectors show that orientation is load-bearing

The phase `ell=-q r^{-1} mod p` immediately gives two opposite extremes.

### Same-sign sector: `q≡r (mod p)`

Here `ell=p-1`, so for `1<=h<p`,

\[
y_h=p-h.
\tag{29}
\]

Condition (4) becomes

\[
qh+r(p-h)<pr
\iff
(q-r)h<0,
\tag{30}
\]

which is impossible because `q>r`. Therefore

\[
\boxed{
q\equiv r\pmod p
\quad\Longrightarrow\quad
D_{p,r;q}=0.
}
\tag{31}
\]

This is strictly stronger than the PC-249/PC-251 Frobenius-threshold collapse: no assumption `q>pr-p-r` is needed. For example,

\[
(p,r,q)=(5,37,47)
\tag{32}
\]

has `q≡r (mod 5)` and `47<5\cdot37-5-37=143`, yet the exact overlap matrices give `D_{5,37;47}=0`.

### Opposite-sign sector: `q≡-r (mod p)`

Here `ell=1`, so `y_h=h`. Condition (4) reduces to

\[
(q+r)h<pr.
\tag{33}
\]

Consequently

\[
\boxed{
\operatorname{rank}D_{p,r;q}
=2\left\lfloor\frac{pr-1}{q+r}\right\rfloor.
}
\tag{34}
\]

Since `p | q+r`, put

\[
m:=\frac{q+r}{p}\in\mathbb N.
\tag{35}
\]

The active positive layers are

\[
1\le h\le \left\lfloor\frac{pr-1}{q+r}\right\rfloor,
\tag{36}
\]

and (27) becomes the elementary quadratic profile

\[
\boxed{
w_h=h(r-mh).}
\tag{37}
\]

For `(p,r,q)=(17,31,37)`, one has `q≡-r (mod 17)`, `m=4`, seven positive collision layers, and therefore rank `14`; the positive weights are

\[
27,46,57,60,55,42,21.
\tag{38}
\]

Thus even when `p,r,q` are all in the simultaneous-growth regime, comparable size alone does not control whether the shared-upper defect survives. The oriented modular ratio `-q/r (mod p)` can force complete cancellation or a macroscopic collision family.

## 5. A relational sign channel absent from the centered pairwise `p`-spectra

PC-246 proves that for a prime pair `p<s`, the centered Gram packet is the weighted path `L_{p,s mod p}` and satisfies

\[
L_{p,h}=L_{p,-h}.
\tag{39}
\]

Therefore the centered `p`-based singular spectrum of `K_{p,s}` determines `s mod p` only up to sign. Fixing `p` and `r`, an upper prime with

\[
q\equiv r\pmod p
\tag{40}
\]

and one with

\[
q\equiv-r\pmod p
\tag{41}
\]

occupy the same signed residue class as far as the individual centered `p`-based pairwise packet is concerned. Equations (31) and (34), however, can give radically different shared-upper defects.

Hence the three-scale relation recovers an **orientation/sign correlation between two residue channels that pairwise centered singular spectra erase**. This is genuine relational information in the sense demanded by the line mandate: it is not reconstructible from those two centered `p`-spectra separately. The statement is deliberately narrow. It does not claim that the full collection of all pairwise packets at every lower modulus loses the same information, nor that the recovered sign correlation is by itself RH-sensitive.

## 6. Prior-art and novelty audit

The new project-local step is the exact reduction of the PC-251 collision matching to the moving congruence lattice (5) and triangle (6), together with the congruence-sector consequences (31), (34), and the weight formula (27). The ambient mathematics of the resulting scalar count is classical.

Matthias Beck and Sinai Robins, **Explicit and efficient formulas for the lattice point count in rational polygons using Dedekind-Rademacher sums**, *Discrete & Computational Geometry* 27 (2002), 443–459, DOI `10.1007/s00454-001-0082-3`, arXiv:`math/0111329`, give explicit rational-polygon lattice counts whose building blocks are Dedekind-Rademacher finite Fourier sums. Related Fourier-Dedekind and rational-cone methods treat precisely the general class into which (21) falls after choosing a basis for `Lambda_ell`. Thus the appearance of a modular-triangle discrepancy is a **classicalization warning**, not a claim of a new arithmetic species.

There is also established RH-adjacent prior art for cotangent/Dedekind-type sums. Sandro Bettin and J. Brian Conrey, **A Reciprocity Formula for a Cotangent Sum**, *International Mathematics Research Notices* 2013:24 (2013), 5709–5726, DOI `10.1093/imrn/rns211`, prove reciprocity for a cotangent sum arising in the Nyman-Beurling approach to RH. This makes the neighborhood mathematically relevant, but no identity has been derived here equating (24) or (27) with a Vasyunin/Bettin-Conrey sum. Importing such an established RH criterion after the fact would not by itself provide a new Prime-Circle mechanism.

The matched-control test is also negative for prime specificity. Once the PC-251 overlap packets have been represented as uniform rational partitions, the derivation above uses only coprimality, floor collisions, congruences, and interval geometry. Pairwise-coprime composite denominators equipped with the same artificial all-one uniform masks obey the same modular-triangle reduction. Prime cyclotomy supplies the packets canonically; the triangle discrepancy itself is source-blind.

## 7. Consequence for the live comparable-scale branch

PC-251 showed that a nonvanishing normalized pairwise shared-upper signal requires lower scales comparable with the upper one, and left the growing collision matching as a live relational carrier. The present result sharpens that frontier in two directions.

First, **comparability is necessary but far from sufficient**: an infinite arithmetic subsector can collapse exactly because of oriented residue alignment, as (31) shows. Second, collision count, rank, unordered collision weights, and fixed polynomial moments of those weights now lie inside a standard moving rational-lattice counting problem. Merely obtaining a growing rank or a nontrivial lattice discrepancy therefore does not cross the novelty/RH gate.

What remains genuinely unclassified is narrower: a source-forced statistic that retains more of the **ordered weighted matching** than scalar lattice counting does, or a simultaneous growing-limit/nonlocal coupling whose analytic structure survives the matched uniform-partition control. Any such proposal must explain why the information is not reducible to rational-polygon/Dedekind-Rademacher data and must derive, rather than import, the complex parameter, functional equation, zero detector, or critical normalization needed for an RH bridge.

Accordingly PC-253 is a boundary result, not evidence of a new zeta spectral law. It identifies one real relational information gain over the pairwise signed-spectrum quotient while classicalizing the simplest growing statistic of that gain.
