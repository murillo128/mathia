# MC-311 — Bose–Burton forces exponentially many Page-expensive reciprocal directions

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the reciprocal one-defect endpoint of `MC-295`–`MC-310`. Thus

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\qquad R\ge2,
\tag{1}
\]

and for a coefficient mask `a\in\mathbf F_2^R` of Hamming weight `j(a)` the exact shell bias is

\[
x_{\lambda_a}=(-1)^{j(a)}\left(1-\frac{2j(a)}R\right).
\tag{2}
\]

Let

\[
D_y=\exp\!\left(\kappa\frac{\log y}{\log\log y}\right)
\tag{3}
\]

be the Landau–Page source threshold of `MC-293`, and assume the discrete-resolution regime of `MC-310`,

\[
R\varepsilon_y<1,
\qquad
\varepsilon_y=O((\log y)^{-2}).
\tag{4}
\]

Write

\[
v:=\nu_2(R),
\tag{5}
\]

and define the Page-cheap and Page-expensive reciprocal directions by

\[
S_y:=\{0\ne\lambda\in L:\mathcal Q(\lambda)\le D_y\},
\qquad
E_y:=\{0\ne\lambda\in L:\mathcal Q(\lambda)>D_y\}.
\tag{6}
\]

Let `\lambda_*(y)` denote the possible unique Landau–Page exceptional shell functional. Remove it from the cheap set when it is present:

\[
S_y^0:=
\begin{cases}
S_y\setminus\{\lambda_*(y)\},&\lambda_*(y)\in S_y,\\
S_y,&\lambda_*(y)\notin S_y.
\end{cases}
\tag{7}
\]

Then the classical Bose–Burton extremal theorem, combined with the no-exception part of `MC-310`, gives

\[
\boxed{
|S_y^0|
\le
2^R-2^{R-v}.
}
\tag{8}
\]

Equivalently, the complement of the nonexceptional cheap spectrum is a blocking set for all `(v+1)`-dimensional vector subspaces and has size at least

\[
\boxed{
\left|(L\setminus\{0\})\setminus S_y^0\right|
\ge
2^{R-v}-1.
}
\tag{9}
\]

Since the complement in `(9)` consists of the Page-expensive directions together with at most the single cheap Page exception,

\[
\boxed{
|E_y|
\ge
2^{R-v}-2.
}
\tag{10}
\]

If the possible Page-exceptional functional is not cheap — in particular if there is no exceptional mode in the reciprocal span — the stronger bound is

\[
\boxed{
|E_y|
\ge
2^{R-v}-1.
}
\tag{11}
\]

Because `2^v\le R`, `(10)` has the uniform consequence

\[
\boxed{
|E_y|
\ge
\frac{2^R}{R}-2.
}
\tag{12}
\]

Thus the 2-adic cheap-subspace rank ceiling of `MC-310` is not merely a statement that no *single large linear sector* can remain below the Page source scale. It forces an exponentially large family of reciprocal endpoint directions to be Page-expensive. The density depends sharply on the 2-adic valuation of the endpoint rank:

- if `R` is odd, every nonexceptional direction is Page-expensive and `|E_y|\ge2^R-2`;
- if `R\equiv2\pmod4`, at least `2^{R-1}-2` directions are Page-expensive;
- more generally the expensive fraction is at least `2^{-v}-o(1)`.

This answers one part of the frontier left after `MC-310`: **the complementary high-source sector is necessarily large in cardinality**. It does not yet force many distinct source primes, a large common source radical, or a Mertens bound. Exponentially many expensive functionals may still reuse highly overlapping expensive source geometry.

## 1. The nonexceptional cheap spectrum contains no `(v+1)`-flat

Suppose that there were a vector subspace

\[
C\le L,
\qquad
\dim C=v+1,
\tag{13}
\]

such that

\[
C\setminus\{0\}\subseteq S_y^0.
\tag{14}
\]

Then every nonzero element of `C` has source cost at most `D_y`, so `C` is uniformly Page-cheap in the sense of `MC-310`. By construction `C` contains no Page-exceptional functional. The no-exception conclusion of `MC-310` therefore gives

\[
2^{\dim C}\mid R,
\qquad
\dim C\le\nu_2(R)=v.
\tag{15}
\]

This contradicts `\dim C=v+1`.

Hence

\[
\boxed{
S_y^0\text{ contains no nonzero point set of a }(v+1)\text{-dimensional subspace of }L.
}
\tag{16}
\]

Over `\mathbf F_2` projective points are represented by unique nonzero vectors, so `(16)` says exactly that `S_y^0`, viewed as a simple binary matroid of rank at most `R`, is `PG(v,2)`-free.

For `v=0` this statement is elementary rather than an invocation of a nontrivial extremal theorem: a one-dimensional vector subspace has one nonzero point, so `(16)` says simply `S_y^0=\varnothing`. This also follows directly from `MC-310`, since a nonexceptional cheap direction would require the impossible integral Hamming weight `R/2` when `R` is odd.

## 2. Bose–Burton converts forbidden cheap flats into a density bound

The classical binary Bose–Burton theorem states that, for `t\ge2`, if a simple binary matroid `M` of rank `r` satisfies

\[
|M|>
\left(1-2\cdot2^{-t}\right)2^r,
\tag{17}
\]

then `M` contains a copy of `PG(t-1,2)`. Equivalently, a `PG(t-1,2)`-free point set in `\mathbf F_2^r\setminus\{0\}` has cardinality at most

\[
\left(1-2^{1-t}\right)2^r.
\tag{18}
\]

Apply `(18)` to `S_y^0\subseteq L\setminus\{0\}` with

\[
r=R,
\qquad
t=v+1.
\tag{19}
\]

When `v\ge1`, `(16)` supplies the required `PG(v,2)`-freeness, and therefore

\[
|S_y^0|
\le
\left(1-2^{-v}\right)2^R
=
2^R-2^{R-v},
\tag{20}
\]

which is `(8)`. The same formula for `v=0` reduces to `|S_y^0|\le0`, already proved directly.

Since `L\setminus\{0\}` has `2^R-1` points,

\[
\left|(L\setminus\{0\})\setminus S_y^0\right|
\ge
(2^R-1)-(2^R-2^{R-v})
=
2^{R-v}-1,
\tag{21}
\]

proving `(9)`.

The only point in this complement that need not be Page-expensive is the single Page-exceptional functional removed in `(7)`. Subtracting that one possible point gives `(10)`. If it was not removed because it is absent or already expensive, no subtraction is needed and `(11)` follows.

## 3. Blocking-set language identifies the sharp combinatorial escape

The same theorem has a useful dual interpretation. Let

\[
B_y:=(L\setminus\{0\})\setminus S_y^0.
\tag{22}
\]

Equation `(16)` is equivalent to saying that **every `(v+1)`-dimensional vector subspace of `L` meets `B_y` nontrivially**. Thus `B_y` is a blocking set for the corresponding projective `v`-flats.

Bose and Burton's original finite-geometry theorem identifies the minimum-size blocking sets of this type with projective flats. In the binary vector formulation, the extremal size in `(9)` is attained by taking

\[
B_y=H\setminus\{0\}
\tag{23}
\]

for an `(R-v)`-dimensional vector subspace `H\le L`, which has

\[
|H\setminus\{0\}|=2^{R-v}-1.
\tag{24}
\]

Therefore the cardinality bound is combinatorially sharp given only the forbidden-subspace information from `MC-310`. One cannot improve `(9)` by an abstract dimension-counting argument alone.

This extremizer is also an adversarial warning for the arithmetic program. Even after proving that exponentially many endpoint directions are expensive, the expensive set could in principle be concentrated in one large linear flat while the cheap set is its complement. Any stronger arithmetic conclusion must show that the actual minimum-source-cost geometry cannot realize, or cannot effectively imitate, this Bose–Burton extremal organization.

## 4. The 2-adic valuation controls how much of the endpoint spectrum must escape Page scale

The bound is strongest when `R` has small 2-adic valuation. From `(10)`,

\[
\frac{|E_y|}{2^R-1}
\ge
2^{-v}-o(1).
\tag{25}
\]

For odd `R`, `v=0`, so after removing the possible Page exception there are no cheap directions at all. For `R\equiv2\pmod4`, `v=1`, so essentially half of the whole reciprocal spectrum must be expensive. If `R\equiv4\pmod8`, at least a quarter must be expensive.

The weakest case is when `R` is itself a large power of two. Even then `2^v=R`, so `(12)` forces at least `2^R/R-O(1)` expensive directions. Thus no reciprocal endpoint of growing rank can put all but a polynomially small number of its directions below `D_y`.

This is qualitatively stronger than the statement “the maximum cheap subspace has small dimension.” A subset of `\mathbf F_2^R` can be exponentially large while having no large linear subspace; Bose–Burton is exactly what converts the specific forbidden projective geometry here into an exponential complement bound.

At the same time, `(10)` is weaker than the source-incidence closure sought by the line. It charges *directions* rather than *source resources*. If many expensive functionals share the same costly lower-prime coordinates, cardinality alone gives no additive conductor budget. This is the next obstruction that must be overcome rather than silently treating expensive directions as independent costs.

## 5. Prior art and novelty boundary

The finite-geometry input is classical. R. C. Bose and R. C. Burton, *A characterization of flat spaces in a finite geometry and the uniqueness of the Hamming and the MacDonald codes*, Journal of Combinatorial Theory **1** (1966), 96–104, DOI `10.1016/S0021-9800(66)80007-8`, proves the foundational blocking-set/extremal flat theorem. Klaus Metsch, *Bose–Burton Type Theorems for Finite Projective, Affine and Polar Spaces*, in *Surveys in Combinatorics, 1999*, pp. 137–166, DOI `10.1017/CBO9780511721335.006`, surveys the theorem as the minimum blocking-set result for projective spaces.

For the exact modern binary-matroid density formulation used in `(17)`, see Theorem 4.1 (Bose–Burton) in Jonathan Tidor, *Dense binary PG(t−1,2)-free matroids have critical number t−1 or t*, Journal of Combinatorial Theory, Series B **124** (2017), 165–179, DOI `10.1016/j.jctb.2017.01.003`: density above `(1-2\cdot2^{-t})2^r` forces `PG(t-1,2)`.

A targeted literature search on 15 September 2026 for Bose–Burton/blocking-set arguments combined with Landau–Page exceptional characters, Dirichlet-character source cost, Möbius cancellation, or the reciprocal Legendre endpoint found the classical finite-geometry ingredients but no source asserting this arithmetic composition. **No standalone novelty claim is made.** The new durable content for this line is the exact bridge from `MC-310`'s arithmetic 2-adic cheap-rank law to the global count `(10)` of Page-expensive reciprocal directions.

## Boundaries and falsification tests

- **`MC-310` is load-bearing.** The finding uses its exact reciprocal masses, Landau–Page balance, uniform cheapness definition, and discrete-resolution condition `R\varepsilon_y<1`. It does not extend automatically to unequal defect partitions.
- **The Page exception is removed before applying Bose–Burton.** Treating all cheap directions as nonexceptional would incorrectly improve `(10)` by one point. The stronger `(11)` is valid only when no cheap exceptional direction is present.
- **Expensive directions are not independent source costs.** Equation `(10)` counts functionals with `\mathcal Q(\lambda)>D_y`; it does not sum those costs, force disjoint representatives, or even force many distinct source primes.
- **The Bose–Burton extremizer survives the abstract audit.** A flat blocking set attains `(9)`, so no argument using only the absence of `(v+1)`-dimensional nonexceptional cheap subspaces can improve the cardinality threshold.
- **Projective versus vector dimensions are aligned explicitly.** A `PG(v,2)` copy is the set of nonzero points of a `(v+1)`-dimensional binary vector subspace. No scalar-multiplicity correction is hidden over `\mathbf F_2`.
- **The result remains non-RH.** Neither `(10)` nor `(12)` estimates `M(x)`, produces a zeta zero-free region, or supplies critical-strip continuation for `1/\zeta`.

## Consequence for the research line

`MC-310` left three live possibilities: force a cheap subspace above the 2-adic ceiling, remove/control the one Page exception, or extract coercive information from the complementary high-source sector. The present result establishes the first genuinely global coercive fact about that complement: **at least `2^{R-\nu_2(R)}-2` reciprocal endpoint directions must lie above the Page source scale.**

The next useful theorem cannot merely recount those directions. It must convert this exponential expensive set into a source-incidence cost that cannot be shared away — for example, by proving that minimum representatives of a Bose–Burton-sized expensive family require many distinct lower-prime coordinates, large hereditary union radical, or another subadditive resource. Conversely, an explicit arithmetic or matched-control construction in which a flat-sized expensive set reuses a small common source package would show that the new density theorem is still noncoercive for Möbius cancellation.