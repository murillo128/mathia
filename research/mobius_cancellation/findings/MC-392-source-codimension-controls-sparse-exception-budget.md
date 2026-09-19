# MC-392 — Source codimension controls the sparse-exception budget

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `STRUCTURAL-OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint/source-frame setup of `MC-388`--`MC-391`. Let

\[
W\le \mathbf F_2^R,
\qquad H:=|W|,
\qquad C:=W^\perp,
\qquad c:=\dim C=R-\dim W.
\]

After the exact duplicate-character quotient of `MC-391`, write

\[
Q:=\mathbf F_2^R/C\cong \widehat W,
\qquad
A=\{\alpha_z\}\subset Q
\]

for the set of distinct projected endpoint coordinate characters and let

\[
p=\sum_{a\in A}w_a\delta_a,
\qquad
w_a>0,
\qquad
\sum_aw_a=1,
\qquad
\sigma^2:=\|p\|_2^2=\sum_aw_a^2.
\]

The endpoint kernel is the Fourier transform

\[
g(I)=\widehat p(I),
\qquad I\in W.
\]

Then the quotient codimension alone gives the weighted fourth-moment bound

\[
\boxed{
\|p*p\|_2^2
\le
\sigma^4+2(c+1)\left(\sigma^4-\sum_aw_a^4\right)
\le
(2c+3)\sigma^4.
}
\tag{1}
\]

Equivalently, by finite-group Plancherel,

\[
\boxed{
\frac1H\sum_{I\in W}|g(I)|^4
\le
(2c+3)
\left(
\frac1H\sum_{I\in W}|g(I)|^2
\right)^2.
}
\tag{2}
\]

This converts directly into an exceptional-set lower bound. Let `B\subset W\setminus\{0\}` and suppose every other nonzero mode satisfies

\[
|g(I)|\le\varepsilon.
\tag{3}
\]

Because `|A|\le R`, one has `\sigma^2\ge1/R`. Whenever `R\varepsilon^2\le1`,

\[
\boxed{
|B|+1
\ge
\frac{H}{2c+3}
\left(1-R\varepsilon^2\right)^2.
}
\tag{4}
\]

In particular, if `\varepsilon_R=o(R^{-1/2})`, then

\[
\boxed{
|B|+1
\ge
(1-o(1))\frac{H}{2c+3}.
}
\tag{5}
\]

Thus a fixed `O(H/R)` exceptional budget is possible only if the physical source subspace loses a fixed linear fraction of the endpoint dimensions. More precisely, if

\[
|B|\le K\frac HR,
\qquad K=O(1),
\qquad H/R\to\infty,
\]

then `(5)` forces

\[
\boxed{
K\ge(1-o(1))\frac{R}{2c+3},
}
\tag{6}
\]

or equivalently

\[
\boxed{
c\ge(1-o(1))\frac{R}{2K}-\frac32.}
\tag{7}
\]

This is stronger than the coarse low-dual-distance escape left by `MC-390` and the quartic-mass requirement of `MC-391`. If `c=o(R)`, **no fixed `K`** can support an `o(R^{-1/2})` good-mode theorem outside `K H/R` exceptions. In the high-rank branch `\dim W\ge3R/4`, so `c\le R/4`, equation `(5)` already gives

\[
|B|\ge(2-o(1))\frac HR,
\tag{8}
\]

improving the explicit `(1+1/4096)H/R` structural gap of `MC-389` for this exact endpoint quotient.

For the source subspace used in `MC-381`, where the fixed-power cutoff gives

\[
c\le A/\beta,
\qquad \beta=1/100,
\]

one obtains the concrete source-cost form

\[
|B|+1
\ge
(1-o(1))\frac{H}{200A+3}.
\tag{9}
\]

Hence if `A=o(R)`, the unavoidable exceptional population is larger than `H/R` by a factor tending to infinity. If `A=c_0R`, any analytic theorem with fixed exception constant `K` contradicts the exact endpoint frame once `c_0` is chosen below the corresponding fixed threshold, asymptotically `1/(200K)` before safety margins.

No estimate for `M(x)` and no RH consequence follows.

## 1. Every nonzero quotient shift is only a small matching

Let

\[
r:=|A|,
\qquad
k:=\dim\operatorname{aff}(A).
\]

Choose one original endpoint coordinate representative for each distinct class in `A`. Differences of `r` such representatives span an `(r-1)`-dimensional coordinate-difference space before quotienting by `C`. Therefore

\[
\boxed{k\ge r-1-c.}
\tag{10}
\]

Now fix `0\ne s\in Q`. Translation by `s` is a fixed-point-free involution, so

\[
A\cap(A+s)
\]

splits into disjoint two-point pairs `{a,a+s}`. Let `E_s` be this matching and let `m_s:=|E_s|`.

Choose one representative from each of those `m_s` pairs and retain all `r-2m_s` points outside the overlap. These `r-m_s` points, together with the single direction `s`, affinely span `A`. Hence

\[
k\le r-m_s,
\]

and `(10)` gives

\[
\boxed{m_s\le r-k\le c+1.}
\tag{11}
\]

This is the weighted form of the translate-overlap geometry already exposed in `MC-389`: after quotienting by a `c`-dimensional source relation space, no nonzero pair-sum can pair more than `c+1` distinct projected endpoint characters.

## 2. Matching size bounds the full weighted convolution energy

For `s\ne0`, put

\[
b_s:=\sum_{\{a,a+s\}\in E_s}w_aw_{a+s}.
\]

Because every matching edge is counted twice in the directed convolution,

\[
(p*p)(s)=2b_s.
\tag{12}
\]

By Cauchy--Schwarz and `(11)`,

\[
b_s^2
\le
(c+1)
\sum_{\{a,a+s\}\in E_s}w_a^2w_{a+s}^2.
\tag{13}
\]

Every unordered pair `{a,b}` of distinct elements of `A` belongs to exactly one matching, namely the one indexed by `s=a+b`. Summing `(13)` over all nonzero `s` therefore gives

\[
\sum_{s\ne0}b_s^2
\le
(c+1)\sum_{a<b}w_a^2w_b^2
=
\frac{c+1}{2}
\left(
\sigma^4-\sum_aw_a^4
\right).
\tag{14}
\]

Since the group has exponent two,

\[
(p*p)(0)=\sum_aw_a^2=\sigma^2.
\]

Combining this with `(12)`--`(14)` yields

\[
\begin{aligned}
\|p*p\|_2^2
&=\sigma^4+4\sum_{s\ne0}b_s^2\\
&\le
\sigma^4+2(c+1)
\left(
\sigma^4-\sum_aw_a^4
\right),
\end{aligned}
\]

which proves `(1)`. No uniformity assumption on the endpoint masses is used.

For `c=0`, `(1)` reduces to the familiar Rademacher fourth-moment ceiling `\|p*p\|_2^2\le3\sigma^4`. Positive source codimension raises that ceiling only linearly in the number of independent quotient relations.

## 3. Fourth-moment concentration forces many exceptional physical modes

Finite-group Plancherel gives

\[
\sum_{I\in W}|g(I)|^2=H\sigma^2,
\qquad
\sum_{I\in W}|g(I)|^4=H\|p*p\|_2^2.
\tag{15}
\]

The good modes in `(3)` contribute at most `H\varepsilon^2` to the first sum. Hence the zero mode together with `B` carries squared mass at least

\[
H(\sigma^2-\varepsilon^2).
\tag{16}
\]

Cauchy--Schwarz on those `|B|+1` modes and `(1)` give

\[
H^2(\sigma^2-\varepsilon^2)^2
\le
(|B|+1)H(2c+3)\sigma^4.
\tag{17}
\]

Because `\sigma^2\ge1/R`,

\[
1-\frac{\varepsilon^2}{\sigma^2}
\ge1-R\varepsilon^2.
\]

Equation `(4)` follows immediately, and `(5)`--`(7)` are its asymptotic consequences.

This argument avoids the threshold loss in the Paley--Zygmund step of `MC-391`: it uses the fact that an `o(R^{-1/2})` good family contributes negligible **total second-moment mass**, then compares that concentration directly with the exact fourth-moment ceiling `(1)`.

## 4. Relation to the current endpoint frontier

`MC-386` proves that arbitrary rank-`R` PSD Cayley frames can concentrate their unavoidable off-diagonal energy on the abstract `H/R` scale. `MC-387` classifies near-extremizers, and `MC-388`--`MC-389` show that the exact endpoint simplex is too high-dimensional to attain the sharp annihilator geometry, yielding a fixed factor above `H/R`.

`MC-390` then shows that high dual distance forces a positive-density population at the critical frame scale, while `MC-391` identifies weighted genuine four-character collisions as the only even-moment escape after duplicate-character quotienting.

The present result quantifies that escape directly in terms of **source codimension**. Many quartic collisions cannot be distributed arbitrarily: every nonzero quotient difference is a matching of size at most `c+1`. Summed over all shifts, this caps the entire weighted fourth moment by `(2c+3)` times the square of the second moment. Consequently an endpoint route with only `O(H/R)` exceptional physical differences must pay `c=\Omega(R)` independent source relations. Low-weight relations are therefore not merely required to exist; enough independent quotient structure must be present to support the desired sparse exceptional geometry.

For the actual fixed-power source annihilator of `MC-381`, this gives a direct quantitative dictionary from the trial source exponent `A` to the smallest possible source-frame exceptional population through `(9)`.

## Prior art and novelty boundary

The ingredients are classical or already audited locally. Finite-group Plancherel, convolution energy, Cauchy--Schwarz, and the representation of additive energy by translate overlaps are standard additive-combinatorial identities. `MC-389` already audits the neighboring additive-energy literature and proves the unweighted binary translate-overlap inequality from affine rank. `MC-391` already audits the weighted four-collision expansion and the code/Sidon boundary.

A targeted mechanism-level search on 19 September 2026 for weighted additive energy, affine dimension, binary-vector-space translate overlap, and codimension did not identify a source needed to treat `(1)`--`(9)` as prior literature. That absence is not evidence of novelty. The new Mathia delta is the elementary composition of the exact projected endpoint simplex with weighted matching energy, producing the explicit codimension/exception tradeoff `(4)`--`(9)`. No standalone novelty claim is made.

## Boundaries and falsification tests

- **The exponent-two quotient is load-bearing.** Translation by nonzero `s` is a fixed-point-free involution, each unordered pair has the unique sum `s=a+b`, and `(p*p)(0)=\sum_aw_a^2`.
- **Duplicate coordinate characters must be merged first.** The set `A` is the distinct projected support from `MC-391`; weight-2 dual words are absorbed into the positive masses `w_a` before `(10)`--`(14)` are applied.
- **The endpoint simplex origin is load-bearing.** Inequality `(10)` uses that `A` is a quotient of distinct coordinate vertices by the `c`-dimensional relation space `C`. A generic probability measure on an arbitrary subset of `Q` need not satisfy the matching bound `(11)`.
- **Weights may be arbitrarily nonuniform.** No balanced-cell or near-Welch assumption is used in `(1)`--`(5)`.
- **The good-mode scale is explicit.** Formula `(4)` is useful whenever `R\varepsilon^2<1`; the asymptotic sparse-exception conclusions require `\varepsilon=o(R^{-1/2})`.
- **The `+1` is the zero mode.** It is retained explicitly in `(4)` and is negligible only when the relevant exceptional scale tends to infinity.
- **Source codimension is not conductor size.** Equation `(9)` uses only the codimension bound supplied by the fixed-power source cutoff of `MC-381`; it does not identify every source prime with an independent relation.
- **No analytic character-sum theorem is supplied.** The result prices the exceptional geometry that such a theorem would have to beat; it does not itself prove good-mode cancellation.
- **No Möbius or RH conclusion.** The theorem narrows the internal endpoint/source-frame mechanism only.

## Consequence for the research line

The immediate frontier is no longer merely to count weighted quartic collisions. The exact endpoint quotient now has a universal resource inequality: concentrating almost all physical correlations below the `R^{-1/2}` frame scale while leaving only `K H/R` exceptions requires roughly `R/(2K)` independent source relations.

In particular, sublinear source codimension is incompatible with every fixed sparse-exception constant `K`. Any future analytic source-frame estimate should therefore be compared directly with `(4)` or `(9)` rather than only with the generic Welch floor or the existence of low-weight dual words.