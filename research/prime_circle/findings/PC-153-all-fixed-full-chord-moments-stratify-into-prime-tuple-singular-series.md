# PC-153 — all fixed full-chord moments stratify into prime-tuple singular series

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. PC-149 classifies every fixed finite chord word and every fixed-radius polynomial moment by generalized totients / Hardy--Littlewood tuple densities. PC-151 then passes the first Mertens-scale spectral displacement to the complete all-chord inverse-square operator, and PC-152 proves that the complete three-vertex part of the second moment is an absolutely convergent prime-triple singular-series functional. The remaining natural question is whether higher **fixed** polynomial moments acquire a new arithmetic species when the chord radius grows all the way with the conductor.

They do not. For every fixed moment order `r`, the exact trace expansion of the full normalized primitive-shell inverse-square chord Laplacian splits by the number `v` of distinct primitive vertices visited by the contributing edge word, with

\[
2\le v\le r+1.
\]

Each `v`-vertex stratum has a natural Mertens scale `1/(log x)^{v-1}`. After multiplying by `(log x)^{v-1}/phi(N_x)`, the **complete all-chord stratum** converges to an absolutely convergent finite linear combination of inverse-square weighted Hardy--Littlewood `v`-tuple singular-series sums. Thus PC-152 is the `r=2, v=3` member of a general full-radius hierarchy, not an isolated accident.

This closes all fixed-degree polynomial spectral moments of the single-level full-chord operator as a source of new RH structure. It does not control moment order growing with the conductor, a non-polynomial object that requires a genuinely uniform resummation of infinitely many moments, eigenvectors/projectors, or cross-level coherent transport.

## 1. Every nonzero edge word has finite connected support

As in PC-151/PC-152, put

\[
N_x:=\prod_{p\le x}p,
\qquad
\phi_x:=\varphi(N_x),
\qquad
U_x:=(\mathbb Z/N_x\mathbb Z)^\times,
\]

and let

\[
A_x:=N_x^{-2}L_{N_x}^{\rm int}.
\]

For two distinct primitive residues `a,b`, write

\[
q_{ab}:=e_a-e_b,
\qquad
g_{N,a-b}:=
\frac{1}{4N^2\sin^2(\pi(a-b)/N)}.
\]

Using ordered endpoints only to avoid choosing an orientation for each unordered edge,

\[
\boxed{
A_x=
\frac12
\sum_{\substack{a,b\in U_x\\a\ne b}}
g_{N_x,a-b}\,q_{ab}q_{ab}^*.
}
\tag{1}
\]

For every fixed integer `r>=1`, rank-one multiplication gives

\[
\boxed{
\operatorname{Tr}(A_x^r)
=
2^{-r}
\sum_{(a_j,b_j)}
\left(\prod_{j=1}^r g_{N_x,a_j-b_j}\right)
\left(\prod_{j=1}^r
\langle q_{a_jb_j},q_{a_{j+1}b_{j+1}}\rangle\right),
}
\tag{2}
\]

where `j` is cyclic and every `a_j!=b_j`. The incidence factor is

\[
\langle q_{ab},q_{cd}\rangle
=
\mathbf 1_{a=c}-\mathbf 1_{a=d}
-\mathbf 1_{b=c}+\mathbf 1_{b=d}.
\tag{3}
\]

Hence a term in (2) can be nonzero only when every pair of consecutive edges intersects. The support graph of the edge word is therefore connected. Since it has `r` edge occurrences, a nonzero word can involve at most `r+1` distinct vertices.

Let `M_{r,v}(x)` denote the sum of terms in (2) whose endpoint set contains exactly `v` distinct primitive residues. Equality of endpoints is an exact finite combinatorial condition, so

\[
\boxed{
\operatorname{Tr}(A_x^r)
=
\sum_{v=2}^{r+1}M_{r,v}(x).
}
\tag{4}
\]

No asymptotic subtraction is involved. For `r=2`, the `v=2` stratum is the repeated-edge term and the `v=3` stratum is exactly the wedge correction `W_x` of PC-152.

Equivalently, for fixed `r,v` there is a finite set `Pi_{r,v}` of canonical endpoint-equality patterns. A pattern `pi` specifies `r` oriented edge occurrences on `v` canonical labels, has a fixed incidence coefficient `c_pi` from (2)--(3), and has a connected support graph. Thus

\[
M_{r,v}(x)=\sum_{\pi\in\Pi_{r,v}}M_{\pi}(x).
\tag{5}
\]

All conductor growth is now in the placements of one fixed finite connected pattern.

## 2. A support pattern is exactly a translated reduced-residue tuple count

Fix `pi in Pi_{r,v}` and choose once and for all a spanning tree `T_pi` of its support graph, rooted at label `0`. For a placement of the labels in `U_x`, assign to every oriented tree edge its unique signed canonical displacement

\[
d_e\in D_x:=
\{d\in\mathbb Z:-N_x/2<d<N_x/2,\ d\ne0\}.
\]

The antipodal displacement cannot occur between two units of the even primorial: `N_x/2` is odd while every primitive residue is odd. The `v-1` tree displacements reconstruct every vertex modulo `N_x`. If they are regarded temporarily as ordinary integers, they give lifted rooted offsets

\[
H_\pi(\mathbf d)=
\{h_0(\mathbf d)=0,h_1(\mathbf d),\ldots,h_{v-1}(\mathbf d)\},
\tag{6}
\]

where every `h_i` is an integer linear combination with coefficients `0,±1` of the tree increments. Let `D_{pi,x}` be the set of tree-increment vectors for which these reconstructed vertices are pairwise distinct modulo `N_x`.

For such a vector define the exact translation count

\[
J_{H_\pi(\mathbf d)}(N_x)
:=
\#\{a\bmod N_x:
 a+h_i(\mathbf d)\in U_x\text{ for all }0\le i<v\}.
\tag{7}
\]

Every injective placement of the canonical labels has one root `a` and one canonical tree-increment vector, so this parametrization is neither a cutoff nor an approximation. If `delta_{pi,j}(d)` is the nonzero cyclic displacement carried by the `j`-th edge occurrence, the pattern contribution has the exact form

\[
\boxed{
M_\pi(x)
=
c_\pi
\sum_{\mathbf d\in D_{\pi,x}}
J_{H_\pi(\mathbf d)}(N_x)
\prod_{j=1}^r
g_{N_x,\delta_{\pi,j}(\mathbf d)}.
}
\tag{8}
\]

For a finite offset set `H={h_0,...,h_{v-1}}`, put

\[
\nu_p(H):=\#\{h_0,\ldots,h_{v-1}\pmod p\}.
\tag{9}
\]

CRT gives, exactly as in PC-149 and PC-152,

\[
\boxed{
\frac{J_H(N_x)}{\phi_x}
=
\prod_{p\le x}\frac{p-\nu_p(H)}{p-1}.
}
\tag{10}
\]

Writing

\[
M(x):=\prod_{p\le x}\left(1-\frac1p\right)
\]

and

\[
\mathfrak S_v(H)
:=
\prod_p
\frac{1-\nu_p(H)/p}{(1-1/p)^v},
\tag{11}
\]

with value `0` for a locally inadmissible tuple, equation (10) is

\[
\frac{J_H(N_x)}{\phi_x}
=
M(x)^{v-1}
\prod_{p\le x}
\frac{1-\nu_p(H)/p}{(1-1/p)^v}.
\tag{12}
\]

For every fixed admissible integer offset set `H`, the partial product tends to the ordinary Hardy--Littlewood `v`-tuple singular series. Mertens' product theorem therefore yields

\[
\boxed{
(\log x)^{v-1}
\frac{J_H(N_x)}{\phi_x}
\longrightarrow
 e^{-(v-1)\gamma}\mathfrak S_v(H).
}
\tag{13}
\]

The support size, rather than the moment order itself, is what fixes the Mertens exponent.

## 3. Inverse-square decay makes the complete all-chord hierarchy summable

The missing step beyond PC-149 is uniform control when every tree displacement is allowed to grow with `N_x`. Fix a valid lifted offset set `H` and put

\[
\Delta(H):=
\prod_{0\le i<j<v}|h_i-h_j|.
\tag{14}
\]

For every prime `p>2v` not dividing `Delta(H)`, all `v` residues are distinct and the local factor in (11) is

\[
\frac{1-v/p}{(1-1/p)^v}=1+O_v(p^{-2}).
\]

If `p|Delta(H)`, then `1<=nu_p(H)<=v-1` for an admissible local tuple, and

\[
\frac{1-\nu_p(H)/p}{(1-1/p)^v}
\le
(1-1/p)^{1-v}
=1+O_v(p^{-1}).
\]

The finitely many primes `p<=2v` contribute only a `v`-dependent constant. Consequently every partial singular-series product satisfies the uniform elementary bound

\[
\boxed{
\prod_{p\le x}
\frac{1-\nu_p(H)/p}{(1-1/p)^v}
\ll_v
\prod_{p\mid\Delta(H)}
\left(1+\frac{C_v}{p}\right)
\ll_v
\bigl(\log\log(3\Delta(H))\bigr)^{C_v}.
}
\tag{15}
\]

The last estimate is the standard maximal-order bound obtained by concentrating the prime divisors of `Delta` at the smallest primes. The same inequality is harmless when a local obstruction makes the left side zero.

Now use the tree itself as the summability skeleton. For every nonzero canonical chord displacement,

\[
\boxed{
0<g_{N,d}\le\frac1{16d^2}}
\tag{16}
\]

by `sin t >= 2t/pi` on `[0,pi/2]`, and `g_{N,d}<=1/16` trivially. Every tree edge occurs at least once among the `r` edge factors in (8). Keeping one inverse-square factor for each of the `v-1` tree edges and bounding all remaining factors by `1/16` gives

\[
\boxed{
\prod_{j=1}^r
g_{N_x,\delta_{\pi,j}(\mathbf d)}
\le
16^{-r}
\prod_{e\in T_\pi}|d_e|^{-2}.
}
\tag{17}
\]

Moreover each lifted pair difference in (14) is a tree-path sum, so for fixed `r`

\[
\Delta(H_\pi(\mathbf d))
\le
C_r\left(1+\sum_{e\in T_\pi}|d_e|\right)^{\binom v2}.
\tag{18}
\]

Since `(log x)M(x)` is bounded, equations (12), (15), (17), and (18) imply that the absolute value of the scaled summand in (8) is bounded, for any fixed `0<epsilon<1`, by

\[
C_{r,\epsilon}
\prod_{e\in T_\pi}|d_e|^{-2+\epsilon}.
\tag{19}
\]

This is summable on `(Z\setminus\{0\})^{v-1}`. Thus the all-chord limit is not a formal interchange: dominated convergence is available for every fixed support pattern.

For fixed `d`, once `N_x` is larger than all relevant lifted path differences, no wraparound remains and

\[
g_{N_x,\delta_{\pi,j}(\mathbf d)}
\longrightarrow
\frac{1}{4\pi^2|\delta_{\pi,j}(\mathbf d)|^2}.
\tag{20}
\]

Let `D_pi` denote the integer tree-increment vectors for which the lifted offsets are pairwise distinct, and interpret `S_v=0` on inadmissible tuples. Equations (8), (13), and (19)--(20) give

\[
\boxed{
\lim_{x\to\infty}
\frac{(\log x)^{v-1}}{\phi_x}M_\pi(x)
=
\frac{e^{-(v-1)\gamma}c_\pi}{(4\pi^2)^r}
\sum_{\mathbf d\in D_\pi}
\mathfrak S_v(H_\pi(\mathbf d))
\prod_{j=1}^r
\frac{1}{|\delta_{\pi,j}(\mathbf d)|^2},
}
\tag{21}
\]

and the series is absolutely convergent.

Summing over the finite pattern set finally yields, for every fixed `r>=1` and every `2<=v<=r+1`,

\[
\boxed{
\lim_{x\to\infty}
\frac{(\log x)^{v-1}}{\phi_x}M_{r,v}(x)
=C_{r,v},
}
\tag{22}
\]

where `C_{r,v}` is an explicit absolutely convergent finite linear combination of inverse-square weighted Hardy--Littlewood `v`-tuple singular-series sums. Cancellations can make a particular `C_{r,v}` vanish; they cannot introduce a different arithmetic coefficient class.

## 4. The first new case is the four-vertex part of the cubic moment

The `r=3` case makes the hierarchy concrete:

\[
\operatorname{Tr}(A_x^3)
=M_{3,2}(x)+M_{3,3}(x)+M_{3,4}(x).
\tag{23}
\]

Three distinct edges with four support vertices must form a three-star: cyclic nonvanishing of the three incidence inner products makes the three edges pairwise intersect, and the only four-vertex possibility is a common center with three distinct neighbors. If `h,k,l in D_x` are their signed offsets from the center, all six orderings of the three unordered star edges are exactly the ordered triples already present in the sum below. Hence

\[
\boxed{
M_{3,4}(x)
=
\sum_{\substack{h,k,l\in D_x\\
 h,k,l\text{ pairwise distinct}}}
J_{h,k,l}(N_x)
\,g_{N_x,h}g_{N_x,k}g_{N_x,l},
}
\tag{24}
\]

where

\[
J_{h,k,l}(N_x)
=
\#\{a\bmod N_x:a,a+h,a+k,a+l\in U_x\}.
\]

Therefore the first support layer beyond PC-152 has the explicit full-radius limit

\[
\boxed{
\lim_{x\to\infty}
\frac{(\log x)^3}{\phi_x}M_{3,4}(x)
=
\frac{e^{-3\gamma}}{64\pi^6}
\sum_{\substack{h,k,l\in\mathbb Z\setminus\{0\}\\
 h,k,l\text{ pairwise distinct}}}
\frac{\mathfrak S_4(0,h,k,l)}{h^2k^2l^2}.
}
\tag{25}
\]

The series is absolutely convergent by the preceding argument. Thus the next genuinely larger vertex support does appear, but it is exactly the classical prime-quadruple local density completed by the geometric inverse-square weight.

## 5. Prior-art and novelty audit

The arithmetic ingredients are classical. Pabhapote--Laohakosol, **Combinatorial Aspects of the Generalized Euler's Totient**, *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165, DOI `10.1155/2010/648165`, supplies the generalized-totient / simultaneous-coprimality counting framework already used in PC-148/PC-149. Equation (11) is the ordinary Hardy--Littlewood finite-tuple singular series. Gallagher's classical fixed-size singular-series averages and modern constrained or smoothly weighted singular-series work such as Kuperberg's show that weighted tuple-series aggregation is itself established analytic-number-theory territory.

The graph-algebra ingredient is also standard: powers of a weighted graph Laplacian expand into finite incidence-edge words, and their trace is determined by closed support patterns. Directed searches across reduced-residue spectral moments, primorial graphs, weighted Hardy--Littlewood singular-series sums, and graph/spectral formulations did not locate the exact full-chord Prime-Circle specialization (21)--(25). No theorem-level novelty is claimed for that specialization. Its durable value is as an internal **classification theorem** connecting the already-proved fixed-word result PC-149 to the full-radius cases PC-151/PC-152 for every fixed polynomial degree.

The closest RH-sensitive neighboring source already anchored in `SOURCES.md` is Goldston--Suriajaya, **A singular series average and the zeros of the Riemann zeta-function**, *Acta Arithmetica* 200 (2021), 71--90, DOI `10.4064/aa200821-24-2`. PC-151 uses its prime-pair Dirichlet generating function to show that zeta zeros can re-enter after an external Mellin/Dirichlet transform of the pair singular series. The present theorem does not change that audit: equations (21)--(25) themselves contain no free complex spectral parameter, analytic continuation, gamma factor, functional equation, or critical-line involution. Applying an external transform to a `v`-tuple coefficient sum would require a separate classical-number-theory audit and is not an RH mechanism generated by the fixed moment.

## 6. Boundary and falsification surface

1. At `r=2`, the `v=3` specialization of (21) must reproduce PC-152's exact wedge formula and its `e^{-2 gamma}/(16 pi^4)` weighted prime-triple limit. Any mismatch falsifies the pattern normalization.
2. At `r=3`, direct expansion must give the exact star identity (24). In particular, every four-vertex nonzero cubic word is a star and no path on four vertices can survive the cyclic incidence product.
3. For every fixed pattern and finite primorial, CRT enumeration of its rooted support must agree with (10); local inadmissibility must kill the placement count exactly.
4. The full-radius passage depends essentially on the inverse-square decay and on fixed `r`. The spanning-tree majorant (17)--(19) must remain summable; without it PC-149 does not justify allowing the chord radius to grow with `N_x`.
5. Equation (22) is a support-stratified family of limits, **not** a complete asymptotic power series for `Tr(A_x^r)`: quantitative corrections inside a lower-support stratum may be larger than the leading term of a higher-support stratum.
6. Fixed moment order is essential. Knowing the theorem separately for every fixed `r` does not justify interchanging `r->infinity` with `x->infinity`, reconstructing a resolvent or determinant from the limiting constants, or controlling moment order comparable with `phi_x`. Such an infinite-depth resummation remains outside this result.
7. The theorem concerns scalar polynomial traces. It does not classify eigenvectors/projectors, non-polynomial spectral observables lacking a justified uniform moment expansion, or cross-level coherent transport. Those are the remaining places where a genuinely different Prime-Circle mechanism would have to live.
