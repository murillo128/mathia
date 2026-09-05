# WP-155 — Canonical resultant cell completions cannot create mixed-prime curvature

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + HAMMING-SUPPORT + FLAG-COMPLEX + CARTESIAN-CELL-COMPLETION + MIXED-PRIME-ABSENCE + QUOTIENT-NON-L2 + PRIOR-ART-CLASSICALIZATION` for ordinary Hodge/cell-complex completions of the normalized zero-order resultant carrier.

`WP-154` leaves a precise escape after showing that the normalized resultant `1`-cochain is exact on prime-step edges, positively curved on same-prime chord triangles, flat on mixed-prime rectangles, and non-square-summable because every curvature cell has infinitely many spectator copies. One could hope that the problem is only the choice of cells or the spectator multiplicity: take the support graph seriously, build its canonical higher-dimensional completion, or quotient away spectator directions before applying Hodge positivity.

Both repairs fail more sharply than the raw spectator argument suggests. On every finite prime/exponent box, the support graph of the nonzero cyclotomic resultants is exactly a Cartesian product of complete graphs. Therefore its flag complex has **no mixed-prime `2`-simplices at all**: every simplex of dimension at least two lies inside one prime coordinate. If instead one adds the equally natural Cartesian squares expressing commutation of distinct prime moves, the resultant cochain has exactly zero circulation on every such square. Thus the two source-forced higher-cell completions either omit mixed-prime `2`-cells or add only mixed-prime cells on which the arithmetic curvature vanishes.

Moreover, quotienting away spectators does not make the surviving same-prime curvature into a natural Hilbert `2`-cochain. Even after the stronger quotient that also forgets the starting depth along a stable prime tower, the curvature cell types are indexed by the two chord lengths `(k,l)`, and for every fixed `k` their curvature tends to the nonzero Weil ray coefficient as `l -> infinity`. Hence the counting `ell^2` norm diverges already in the chord-length variable. The same boundary behavior that recovers `(log p)p^{-k/2}` prevents an unweighted finite-energy Hodge completion.

So the higher-cohomological escape is narrower than `WP-154` left it: **changing only the cell completion or quotient of the existing resultant support cannot manufacture the missing global coupling.** A surviving construction must add a new source-forced correspondence/cell structure or finite--archimedean interaction that is nonzero in mixed directions *before* ordinary Hodge positivity is formed, together with its own non-arbitrary cell measure/domain.

## 1. The resultant support graph is a Cartesian product of complete coordinate graphs

Use the normalized zero-order resultant interaction from `WP-145`, `WP-148`, and `WP-154`,

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}
\qquad(m\ne n).
\tag{1}
\]

Its support is exact:

\[
J_{m,n}\ne0
\quad\Longleftrightarrow\quad
\frac{\max(m,n)}{\min(m,n)}=p^k
\text{ for some prime }p\text{ and }k\ge1.
\tag{2}
\]

Fix a finite prime set `P` and exponent bounds `A_p>=1`, and consider the full exponent box

\[
V(P,A)
=
\left\{
\prod_{p\in P}p^{a_p}:0\le a_p\le A_p
\right\}.
\tag{3}
\]

Two distinct vertices in this box are adjacent in the support graph exactly when their exponent vectors differ in **one** coordinate, by an arbitrary nonzero amount. Therefore the induced support graph is exactly

\[
\boxed{
G(P,A)
\cong
\mathop{\square}_{p\in P}K_{A_p+1},
}
\tag{4}
\]

where `square` is the Cartesian graph product. In other words, every finite exponent box is a generalized Hamming graph: along one prime coordinate every pair of exponent levels is connected, while changing two prime coordinates at once is never a resultant edge.

This statement uses only the exact Apostol support law already audited in `WP-145`/`WP-154`; no positivity theorem is involved.

## 2. The flag completion has no mixed-prime `2`-simplices

Let `Cl(G)` be the flag/clique complex of the full resultant support graph. A `2`-simplex is a triangle of pairwise nonzero resultant edges.

Take three distinct vertices in such a triangle and order them by divisibility,

\[
a\mid b\mid c.
\tag{5}
\]

The first two edges give

\[
\frac ba=p^k,
\qquad
\frac cb=q^\ell
\tag{6}
\]

for primes `p,q`. The third edge requires

\[
\frac ca=p^kq^\ell
\tag{7}
\]

to be a prime power. Hence necessarily

\[
\boxed{p=q.}
\tag{8}
\]

Thus every triangle varies a single prime coordinate. The same argument applied to every three vertices of a larger clique gives

\[
\boxed{
\text{every simplex of dimension }\ge2
\text{ in }Cl(G)
\text{ is contained in one prime-coordinate fiber.}
}
\tag{9}
\]

This is also the standard coordinate geometry visible directly from (4): a clique in a Cartesian product of complete graphs can vary in only one coordinate.

Consequently the **support-determined flag complex contains no higher cell that directly couples two distinct primes**. Its nonzero `2`-coboundary can only live on same-prime chord triangles, exactly as observed experimentally and then derived in `WP-154`.

## 3. Adding the missing Cartesian squares produces zero mixed curvature

The flag completion is not the only canonical choice. Equation (4) also suggests the Cartesian cell structure in which commuting moves in two coordinates bound a square. For distinct primes `p!=q`, arbitrary jump lengths `k,l>=1`, and any base shell `m`, use the oriented square

\[
m
\to mp^k
\to mp^kq^\ell
\to mq^\ell
\to m.
\tag{10}
\]

The exact resultant edge law of `WP-154` depends on the changed prime coordinate, the jump length, and whether **that same coordinate** was previously zero. Other prime exponents are spectators. Therefore opposite edges in (10) agree:

\[
J_{m,mp^k}
=J_{mq^\ell,mp^kq^\ell},
\qquad
J_{m,mq^\ell}
=J_{mp^k,mp^kq^\ell}.
\tag{11}
\]

Hence

\[
\boxed{
(dJ)\bigl(\square(p^k,q^\ell)\bigr)=0
\qquad(p\ne q).
}
\tag{12}
\]

There is therefore a sharp completion dichotomy:

\[
\boxed{
\begin{array}{ll}
\text{flag completion:}&\text{mixed-prime `2`-cells are absent},\\[2mm]
\text{Cartesian completion:}&\text{mixed-prime `2`-cells are present but }dJ=0.
\end{array}}
\tag{13}
\]

Changing from simplicial to cubical bookkeeping does not create the missing global arithmetic curvature.

## 4. The surviving same-prime curvature remains non-`ell^2` after spectator quotient

The remaining curvature lies on same-prime chord triangles. On a stable repeated-prime ray `p|m`, put

\[
q=p^{-1/2},
\qquad
j_p(k)=(\log p)q^k.
\tag{14}
\]

For the compositional triangle

\[
m\to mp^k\to mp^{k+\ell},
\qquad
m\to mp^{k+\ell},
\tag{15}
\]

`WP-154` derives

\[
\boxed{
\kappa_p(k,\ell)
:=(dJ)(k,\ell)
=(\log p)(q^k+q^\ell-q^{k+\ell})>0.
}
\tag{16}
\]

The spectator divergence in `WP-154` came from copying one fixed cell by infinitely many fresh primes. Remove that multiplicity completely: identify all cells differing only in exponents of primes other than `p`. Go further and identify all stable starting depths `v_p(m)>=1`, since (16) is independent of the starting depth. This is a **stronger quotient than merely removing spectators**. The remaining cell types are still indexed by

\[
(p,k,\ell),
\qquad k,\ell\ge1.
\tag{17}
\]

Now fix `p` and `k`. The exact boundary limit is

\[
\boxed{
\lim_{\ell\to\infty}\kappa_p(k,\ell)
=(\log p)q^k
=j_p(k)>0.
}
\tag{18}
\]

Therefore there is `L=L(p,k)` such that for all `ell>=L`,

\[
\kappa_p(k,\ell)\ge\frac12j_p(k),
\tag{19}
\]

and hence

\[
\boxed{
\sum_{\ell\ge1}|\kappa_p(k,\ell)|^2
=\infty.
}
\tag{20}
\]

Indeed the same proof gives divergence of every finite counting `ell^s`, `s>0`.

This is strictly stronger than spectator replication. Even after removing **all** base-shell multiplicity and keeping only intrinsic chord-length types, the raw resultant curvature is not a finite-energy counting `2`-cochain.

## 5. The divergence is tied exactly to recovering the Weil ray

Equation (20) is not an unrelated pathology. It is forced by the same feature that made the curvature route interesting in `WP-154`: its boundary value is the exact critical finite-place coefficient.

For each fixed prime-power depth `k`, retaining

\[
\frac{\log p}{p^{k/2}}
\tag{21}
\]

as the `ell -> infinity` limit means the family of compositional curvature cells cannot decay in the second chord-length direction. Thus one cannot simultaneously demand all three of the following from the unweighted source complex:

1. retain all compositional chord triangles;
2. place the raw curvature in the ordinary counting `ell^2` Hodge cell space;
3. preserve the nonzero boundary value (21).

A positive weighted Hodge norm

\[
\sum_{p,k,\ell}w_{p,k,\ell}|\kappa_p(k,\ell)|^2,
\qquad w_{p,k,\ell}\ge0,
\tag{22}
\]

can of course be made finite by choosing summable weights in `ell`. But those weights are new geometric data. The resultant support and coefficient law do not choose them, and fitting them after seeing (21) would be exactly the measure/regularization freedom this research line must audit rather than assume.

At the opposite extreme, taking the boundary limit (18) **before** forming the cell energy simply returns the original edge coefficient `j_p(k)`. Using those values as positive conductances gives the graph-Dirichlet completion already closed by `WP-148`--`WP-150`: infinite all-prime degree, spectator short-circuiting, and erasure of fixed arithmetic edges under local finite-energy normalization.

So the two obvious repairs meet the earlier no-go results on both sides:

\[
\boxed{
\text{keep all curvature cells}
\Rightarrow
\text{non-`ell^2`};
\qquad
\text{take the boundary first}
\Rightarrow
\text{collapsed Dirichlet route}.
}
\tag{23}
\]

## 6. Ordinary Hodge positivity after the quotient is still placewise

Suppose one nevertheless supplies a positive cell measure and forms an ordinary Hodge energy from the surviving curvature. By (9)--(13), every nonzero source curvature cell is labelled by one prime `p`. After spectator/basepoint quotient the curvature carrier decomposes as

\[
\mathcal C^2
=\bigoplus_p\mathcal C^2_p,
\tag{24}
\]

and an ordinary diagonal cell inner product gives a direct sum of positive prime-local energies.

This does not solve the branch objective. `WP-001` already shows that the exact finite-prime terms are not independently positive Weil summands, and `WP-154` shows that the local positive triangle defect is generic exponential-chord geometry. Adding an archimedean complex as another direct summand merely appends one more placewise positive block; it does not generate the finite--archimedean counterterms or the global sign mechanism of the explicit formula.

A non-diagonal cell metric could introduce cross-prime couplings, but then those couplings are **not supplied by the resultant cell incidence**. They become the new candidate structure and must be independently forced and checked against the exact Weil normalization.

## 7. Matched control: the obstruction is coordinate geometry, not special arithmetic

Replace primes by independent labels `alpha`, let each coordinate have exponent levels, connect two vertices exactly when they differ in one coordinate, and assign a same-coordinate chord law

\[
j_\alpha(k)=c_\alpha r_\alpha^k,
\qquad
c_\alpha>0,
\quad 0<r_\alpha<1.
\tag{25}
\]

Every finite exponent box is again a Cartesian product of complete graphs. Its flag simplices are coordinate-local, Cartesian mixed squares have zero circulation for any coordinate-separable edge law, and the same-coordinate triangle defect is

\[
\kappa_\alpha(k,\ell)
=c_\alpha(r_\alpha^k+r_\alpha^\ell-r_\alpha^{k+\ell}).
\tag{26}
\]

For fixed `k`,

\[
\kappa_\alpha(k,\ell)\longrightarrow c_\alpha r_\alpha^k>0,
\tag{27}
\]

so the quotient counting `ell^2` divergence is identical.

Thus neither the topology nor the sign/norm obstruction distinguishes the arithmetic values `c_p=log p`, `r_p=p^{-1/2}` from a generic separable exponential coordinate model. Arithmetic remains in the parameter values; the existing cell architecture does not turn it into a global sign theorem.

## 8. Prior art and novelty audit

No new general theorem about flag complexes, Cartesian graph products, Hamming graphs, cubical complexes, or combinatorial Hodge theory is claimed. Those constructions are classical. The number-theoretic graph/cohomology prior art already anchored in `SOURCES.md`, especially Knill's *On Primes, Graphs and Cohomology*, is a direct warning that merely packaging a divisibility graph cohomologically is not a new RH mechanism.

Likewise the cyclotomic-resultant support law is classical Apostol theory already audited in `WP-145` and reused in `WP-148`/`WP-154`.

The durable Mathia-specific content is the exact synthesis

\[
\boxed{
\begin{aligned}
&\text{resultant support on exponent boxes}
=\text{Cartesian products of complete graphs},\\
&\text{flag higher cells are prime-local},\\
&\text{Cartesian mixed-prime cells have zero }dJ,\\
&\text{maximally quotienting base multiplicity still leaves}
\ \sum_\ell|\kappa_p(k,\ell)|^2=\infty.
\end{aligned}}
\tag{28}
\]

The last line is tied exactly to the boundary identity `lim_{ell->infinity} kappa_p(k,ell)=j_p(k)`, so it is not a generic complaint about infinite complexes: preserving the desired critical ray coefficient forces the non-decay that defeats counting-Hodge finite energy.

## Consequence for the research line

`WP-154` required global coupling to precede positivity/cohomology. The present result rules out obtaining that coupling merely by choosing the most canonical higher cells or by quotienting spectator copies of the **existing** resultant support.

The next cohomological candidate must therefore change the incidence itself. It needs a source-forced correspondence or cell whose boundary genuinely mixes distinct prime coordinates or a finite prime with the real place and on which the arithmetic carrier has a nonzero response before positivity is imposed. It must also supply its cell measure/domain intrinsically; ordinary counting already fails even after the maximal obvious quotient.

In particular, a successful route cannot consist only of

\[
\text{resultant graph}
\to
\text{flag/cubical completion or spectator quotient}
\to
\text{ordinary Hodge norm}.
\tag{29}
\]

The missing ingredient is now localized one stage earlier: **the global finite--finite or finite--archimedean incidence/correspondence itself is absent from the current resultant geometry.**