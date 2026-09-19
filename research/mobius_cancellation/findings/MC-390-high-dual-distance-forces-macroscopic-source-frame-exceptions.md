# MC-390 — High dual distance forces macroscopic source-frame exceptions

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `DECISIVE-NEGATIVE` · `STRUCTURAL-OBSTRUCTION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint partition and source-frame setup of `MC-381`, `MC-386`, `MC-388`, and `MC-389`. Let

\[
W\le \mathbf F_2^R,
\qquad d:=\dim W,
\qquad H:=|W|,
\]

and let the nonempty endpoint defect cells have normalized masses

\[
d_z>0,
\qquad \sum_{z=1}^R d_z=1.
\tag{1}
\]

For `I\in W`, the exact endpoint Cayley kernel is

\[
g(I)=\sum_{z=1}^R d_z(-1)^{\langle I,\mathbf1+e_z\rangle}.
\tag{2}
\]

Write

\[
C:=W^\perp\le\mathbf F_2^R
\]

and denote its minimum nonzero Hamming weight by

\[
d^\perp(W):=\min_{0\ne c\in C}\operatorname{wt}(c).
\tag{3}
\]

If

\[
\boxed{d^\perp(W)\ge5,}
\tag{4}
\]

then the endpoint frame necessarily has **macroscopically many** correlations at the natural `R^{-1/2}` scale. More precisely, put

\[
\sigma^2:=\sum_{z=1}^R d_z^2.
\tag{5}
\]

Then

\[
\boxed{
\frac1H\#\left\{I\in W:
|g(I)|\ge\sqrt{\sigma^2/2}
\right\}
\ge\frac1{12}.
}
\tag{6}
\]

Since `\sigma^2\ge1/R`, this implies

\[
\boxed{
\#\left\{I\in W\setminus\{0\}:
|g(I)|\ge\frac1{\sqrt{2R}}
\right\}
\ge\frac H{12}-1.
}
\tag{7}
\]

Thus the live analytic target left by `MC-386` and sharpened by `MC-389` cannot hold in the high-dual-distance regime. In particular, there is no sequence satisfying `(4)` for which all but `o(H/R)` nonzero source differences obey

\[
|g(I)|=o(R^{-1/2}).
\tag{8}
\]

Indeed `(7)` forces `\Omega(H)` exceptions, larger than the admissible `H/R` scale by a factor `\Theta(R)`.

Equivalently, any endpoint source-frame route that hopes to prove the good-mode estimate `(8)` must first enter the opposite structural regime:

\[
\boxed{
W^\perp\text{ contains a nonzero word of Hamming weight at most }4.
}
\tag{9}
\]

For the specific subspace constructed in `MC-381`,

\[
W=\{I:\langle I,c_p\rangle=0
\text{ for every source prime }p>y^{1/100}\},
\tag{10}
\]

so

\[
W^\perp
=\operatorname{span}_{\mathbf F_2}\{c_p:p>y^{1/100}\}.
\tag{11}
\]

Therefore `(9)` has a concrete arithmetic meaning: some binary combination of the incidence columns of the large source primes must be supported on at most four endpoint generators. A future successful `R^{-1/2}` good-mode theorem cannot treat those source incidences as a generic high-dual-distance code; it must exploit, force, classify, or otherwise account for **low-weight source-incidence parity relations**.

This is a stronger obstruction than the generic Welch threshold alone. `MC-386` shows that an abstract rank-`R` PSD Cayley frame can concentrate its unavoidable energy on `H/R` differences; `MC-388` and `MC-389` exclude the sharp low-dimensional coset geometry and obtain a fixed improvement over `H/R` for actual high-rank endpoint simplices. The present result isolates a complementary regime in which the exceptional set jumps all the way to positive density.

No estimate for `M(x)` and no RH consequence follows.

## 1. The endpoint kernel is a weighted Rademacher sum on `W`

Equation `(2)` factors as

\[
g(I)
=(-1)^{\langle I,\mathbf1\rangle}
\sum_{z=1}^R d_z(-1)^{I_z}.
\tag{12}
\]

Hence absolute values are governed by

\[
Z(I):=\sum_{z=1}^R d_z X_z(I),
\qquad
X_z(I):=(-1)^{I_z},
\qquad
|g(I)|=|Z(I)|.
\tag{13}
\]

Choose `I` uniformly from `W`. For any subset `A\subseteq[R]`, character orthogonality on the subspace gives the exact identity

\[
\mathbf E_I\prod_{z\in A}X_z(I)
=
\mathbf 1_{\{\sum_{z\in A}e_z\in W^\perp\}}.
\tag{14}
\]

If `(4)` holds, no nonempty set `A` of size at most four has its incidence vector in `W^\perp`. Therefore every collection of at most four coordinate signs is uniform on `\{\pm1\}^{|A|}`: the variables `X_1,\ldots,X_R` are unbiased and 4-wise independent under uniform `I\in W`.

This is exactly the classical code/orthogonal-array correspondence specialized to the binary code `W`: dual distance at least five means that the codewords of `W` form an orthogonal array of strength at least four.

## 2. Exact second and fourth moments force anti-concentration

Under `(4)`, pairwise independence gives

\[
\mathbf E Z^2
=\sum_z d_z^2
=\sigma^2.
\tag{15}
\]

Four-wise independence gives the same fourth moment as independent Rademacher signs:

\[
\begin{aligned}
\mathbf E Z^4
&=\sum_z d_z^4
+6\sum_{z<w}d_z^2d_w^2\\
&=3\left(\sum_zd_z^2\right)^2
-2\sum_zd_z^4\\
&\le3\sigma^4.
\end{aligned}
\tag{16}
\]

Apply Paley--Zygmund to the nonnegative random variable `Y=Z^2` with threshold `\theta=1/2`. Equations `(15)`--`(16)` give

\[
\Pr\!\left(
Z^2\ge\frac12\sigma^2
\right)
\ge
\frac{(1-1/2)^2(\mathbf E Z^2)^2}{\mathbf E Z^4}
\ge\frac1{12},
\tag{17}
\]

which proves `(6)`.

Finally Cauchy--Schwarz and `(1)` give

\[
1=\left(\sum_zd_z\right)^2
\le R\sum_zd_z^2
=R\sigma^2,
\tag{18}
\]

so `\sigma^2\ge1/R`. Equation `(7)` follows from `(6)` after removing the zero mode if necessary.

The scale is not an artifact of equal defect cells. Unequal endpoint masses only increase `\sigma^2` above its minimum `1/R`, so the anti-concentration threshold can only become larger.

## 3. The general fourth moment exposes the only escape

The high-dual-distance hypothesis can be seen directly in the exact fourth-moment identity. Expanding `(13)` before imposing `(4)` gives

\[
\boxed{
\mathbf E Z^4
=
\sum_{z_1,z_2,z_3,z_4}
 d_{z_1}d_{z_2}d_{z_3}d_{z_4}
\mathbf1_{\{e_{z_1}+e_{z_2}+e_{z_3}+e_{z_4}\in W^\perp\}}.
}
\tag{19}
\]

The all-paired terms are exactly the Rademacher contribution in `(16)`. Any extra contribution comes from low-weight dual relations visible after reducing the four coordinate indices modulo two. Thus the fourth-moment route itself identifies the escape from `(17)`: `W^\perp` must contain sufficiently low-weight structure for the coordinate signs to cease behaving as a strength-four orthogonal array.

Equation `(19)` does **not** show that the existence of one low-weight word is sufficient to make `(8)` possible. It establishes only the necessary dichotomy `(9)`. Quantifying how many low-weight words, with what supports and arithmetic provenance, are needed to reduce the positive-density lower bound to the `H/R` scale is a separate problem.

For the source subspace `(10)`, this reframes the analytic frontier. The remaining obstacle is not merely to improve a character-sum exponent. One must either derive cancellation while retaining the localized parity structure of `(11)`, or prove that the actual large-source incidence span cannot contain the required low-weight words. Treating the source columns as generic pseudorandom coordinates points in the wrong direction: sufficiently high dual distance would make the desired small-correlation conclusion impossible by `(7)`.

## 4. Relation to the current source-frame frontier

`MC-386` derives the exact Welch energy lower bound

\[
\sum_{I\in W}|g(I)|^2\ge H/R
\]

and shows that the generic abstract threshold for an exceptional set is `H/R` when the good correlations are `o(R^{-1/2})`. Its subgroup/annihilator example proves that scale is sharp in the category of arbitrary PSD Cayley frames of rank at most `R`.

`MC-388` then identifies the actual endpoint Bochner support as the projection of the translated coordinate simplex, and `MC-389` uses its high affine rank and additive-energy deficit to prove a fixed arithmetic gap above the abstract `H/R` exception floor.

The present result is orthogonal to that additive-energy argument. It conditions on the **dual distance of the physical row subspace `W`**, not on the additive energy of the endpoint Bochner support. When `d^\perp(W)\ge5`, the coordinate signs seen by uniform physical differences are already four-wise independent, and the endpoint kernel is a weighted Rademacher sum with a fixed small-ball lower bound. The exceptional set must then occupy at least `1/12+o(1)` of the entire physical group.

Consequently the source-frame frontier splits into two sharply different regimes:

- high dual distance (`d^\perp(W)\ge5`): positive-density `R^{-1/2}` correlations are unavoidable, so the desired good-mode theorem is impossible;
- low dual distance (`d^\perp(W)\le4`): the desired theorem is not ruled out by this argument, but it must exploit a concrete low-weight relation in the span of large-source incidence columns.

This dichotomy is stronger information than an undifferentiated exceptional-count target and gives the analytic side a finite structural object to classify.

## 5. Prior art and novelty boundary

The coding-theory and probability mechanisms are classical. MacWilliams and Sloane, *The Theory of Error-Correcting Codes* (1977), Chapter 5, Section 5, Theorem 8, state that a binary linear code of dual distance `d^\perp` is an orthogonal array of strength `d^\perp-1`. The same code/array correspondence is reviewed explicitly in Hongquan Lin, *Orthogonal Arrays: A Review*, WIREs Computational Statistics (2025), DOI `10.1002/wics.70029`, Theorem 4.1, which traces the linear relationship to Bose. Thus the implication `(4) ->` four-wise independent coordinate signs is standard prior art.

The fourth-moment calculation and Paley--Zygmund small-ball argument for four-wise independent Rademacher signs are also standard. Equation `(16)` is derived here directly, and `MC-375` already audited the neighboring MacWilliams/Pless full-cube moment machinery for endpoint source-incidence columns. No novelty is claimed for orthogonal arrays, dual distance, limited independence, Rademacher moments, or Paley--Zygmund.

A targeted mechanism-level search on 19 September 2026 found the standard dual-distance/orthogonal-array theorem and standard four-wise-independent small-ball arguments, but no source is needed to claim those general ingredients as new. The durable Mathia delta is the endpoint-specific composition: applying them to the exact kernel `(2)` shows that **high dual distance is hostile, not helpful, to the live `R^{-1/2}` source-frame cancellation target**, and forces any successful route into the low-weight arithmetic source-incidence regime `(9)`--`(11)`.

No standalone novelty claim is made.

## Boundaries and falsification tests

- **Exact endpoint partition is load-bearing.** Equation `(2)` uses the one-defect endpoint rule of `MC-296`. A different shell model can change the weighted Rademacher representation.
- **The dual distance is that of the physical source-annihilator subspace `W`.** It is not the minimum distance of the endpoint defect code from `MC-243`, nor the near-negative spectral odd-girth quantity of `MC-291`.
- **`d^\perp(W)\ge5` is sufficient, not claimed necessary, for the positive-density bound.** Some low-dual-distance subspaces may still have the same or stronger anti-concentration.
- **Low-weight dual structure is only a necessary escape.** Equation `(9)` does not prove that one weight-`<=4` word is enough to obtain `o(R^{-1/2})` correlations outside `o(H/R)` modes.
- **The arithmetic interpretation permits long source combinations.** A weight-`<=4` word in `(11)` may be the sum of many source incidence columns; the conclusion is localization in endpoint-generator support, not a bound on the number of source primes used.
- **The zero mode is harmless.** Removing `I=0` changes `(6)` by at most one mode, yielding `(7)`.
- **No probabilistic model for the arithmetic source is assumed.** Uniformity is only over the finite vector space `W`, and all moment identities follow from exact character orthogonality.
- **No global Möbius conclusion.** The theorem narrows an internal endpoint/source-frame strategy and does not estimate `M(x)` or establish a zeta zero-free region.

## Consequence for the research line

The current endpoint program cannot obtain its desired source-frame contradiction by making the large-source incidence span look increasingly pseudorandom in the ordinary coding sense. If that span has dual distance at least five, the endpoint kernel itself anti-concentrates at the critical frame scale and produces `\Omega(H)` bad differences.

The next structural question is therefore concrete: classify or bound the weight-`2`, weight-`3`, and weight-`4` words of the span generated by the source-incidence columns removed in `MC-381`, and determine whether their arithmetic origin can support the analytic cancellations demanded by `MC-386`--`MC-389`. Any future good-mode theorem at `o(R^{-1/2})` must interact with that low-weight source geometry rather than average it away.