# WI-338 — hypercontractive cube concentration closes the all-start ordinary-Gowers gap

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + CLASSICAL-IDENTITY`.

WI-337 shows that an almost-all short-interval theorem cannot cross the bow variance barrier merely by increasing the ordinary Gowers order: matched-energy Rademacher countermodels remain `U^s=o(1)` on density-one starts throughout every fixed margin below the diagonal threshold `R_s=2`, while retaining the full diagonal sliding variance. WI-336 left a narrower logical escape for **all-start/all-interval** information because its bounded-difference argument only produced simultaneous countermodels below `R_s=1`.

That remaining gap is not intrinsic. The random Gowers cube count has a much smaller `L^2` fluctuation than the worst-case single-sign sensitivity used in WI-335--WI-336. Expanding the cube count in Walsh characters, bounding the multiplicity of each nonconstant character by an elementary factorization argument over `F_2[X,X^{-1}]`, and then applying Bonami--Beckner hypercontractivity gives concentration essentially at the natural `1/L` expectation scale **simultaneously on every interval**.

Precisely, fix

\[
0<\kappa<1,\qquad K=N^{\kappa+o(1)},
\]

and any deterministic unit-modulus carrier `u_n`. Let `\delta_N\in(0,1]` satisfy

\[
\delta_N\log\log N\longrightarrow\infty.
\tag{1}
\]

Then for all sufficiently large `N` there is a real sequence

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\qquad \varepsilon_n\in\{-1,+1\},
\tag{2}
\]

such that, simultaneously for every integer interval `I\subset[1,N]` with `K\le |I|\le2K` and every integer `s\ge2` satisfying

\[
R_s(K,N):=\frac{2^s\log\log N}{\log K}
\le 2-\delta_N,
\tag{3}
\]

one has

\[
\boxed{
\|b\|_{U^s(I)}
\le
\exp\!\left(
-\frac{\delta_N}{4(2-\delta_N)}\log\log N+o(1)
\right)
=o(1),
}
\tag{4}
\]

while the same realization obeys

\[
\boxed{
\sum_{x=0}^{N-K}
\left|\sum_{j=1}^{K}b_{x+j}u_{x+j}\right|^2
=(1+o(1))NK\log N.
}
\tag{5}
\]

The scale in (1)--(4) matches the deterministic diagonal-cube floor from WI-336. For a source with energy `E\ge cL\log N`, that floor gives

\[
\log\|f\|_{U^s(I)}
\ge
\left(\frac12-\frac1{R_s(L,N)}\right)\log\log N+O_c(1).
\tag{6}
\]

Thus if `R_s=2-\delta_N` with `\delta_N\log\log N=O(1)`, ordinary normalized `U^s=o(1)` is already impossible for **every** comparable-energy source; whereas whenever the distance below `2` is large enough for the diagonal floor itself to tend to zero, namely `\delta_N\log\log N\to\infty`, the countermodel (2) realizes all-interval `o(1)` while preserving the full bow-scale variance.

So the ordinary-Gowers black-box interface is now closed at its natural critical scale. There is no remaining all-start hierarchy in which mere `U^s=o(1)` can force the WI-195 signed covariance saving. A continuation must use information that this interface discards: a diagonal-renormalized cube statistic, source-specific shifted-prime covariance/sign, a relative linear-forms statement retaining the `Lambda^sharp` structure, or another observable that couples directly to the distinguished bow variance.

## 1. Walsh expansion of the random cube count

Let `I` have length `L`, let `\varepsilon_n` be independent Rademacher signs on `I`, and use

\[
Q_{s,I}:=\|\varepsilon1_I\|_{U^s(\mathbb Z)}^{2^s},
\qquad
D_{s,I}:=\|1_I\|_{U^s(\mathbb Z)}^{2^s},
\qquad
F_{s,I}:=Q_{s,I}/D_{s,I}.
\tag{7}
\]

A cube is a tuple `c=(x,h_1,\ldots,h_s)` whose `2^s` vertices all lie in `I`. For real signs its monomial is

\[
\chi_{A(c)}(\varepsilon)
:=
\prod_{n\in A(c)}\varepsilon_n,
\tag{8}
\]

where `A(c)` is the set of vertex locations occurring with odd multiplicity. Over the Laurent polynomial ring `\mathbb F_2[X,X^{-1}]`, this parity support is encoded exactly by

\[
P_c(X)
=
X^x\prod_{j=1}^s(1+X^{h_j})
=
\sum_{n\in A(c)}X^n.
\tag{9}
\]

Because `\mathbb F_2[X,X^{-1}]` is an integral domain,

\[
A(c)=\varnothing
\quad\Longleftrightarrow\quad
h_j=0\text{ for at least one }j.
\tag{10}
\]

Hence the constant Walsh coefficient is exactly the number of zero-increment cubes. There are at most

\[
sL(2L)^{s-1}
\tag{11}
\]

such cubes. On the other hand, restricting `x` to the middle half of `I` and every `|h_j|` to `L/(8s)` gives, for all large `L` relative to `s`,

\[
D_{s,I}\ge\frac{L^{s+1}}{(Cs)^s}
\tag{12}
\]

for an absolute `C`. Therefore

\[
\boxed{
\mathbb EF_{s,I}
\le
\frac{(Cs)^s}{L}.
}
\tag{13}
\]

This recovers the scale used in WI-335, but the Walsh representation also exposes the variance rather than only the worst-case influence.

## 2. A cube character has only subpower multiplicity

For a nonempty parity set `A`, let `m_A` be the number of cubes in `I` with `A(c)=A`. The key counting fact is

\[
\boxed{
m_A\le
\bigl(2s(1+\log_2 L)\bigr)^s.
}
\tag{14}
\]

To prove it, suppose `A(c)=A\ne\varnothing`. Then no increment is zero. Put

\[
a_j:=|h_j|=2^{v_j}u_j,
\qquad u_j\text{ odd},
\tag{15}
\]

and normalize all increments to be positive. Since

\[
1+X^{-a}=X^{-a}(1+X^a),
\]

(9) becomes

\[
P_A(X)=X^m\prod_{j=1}^s(1+X^{a_j}),
\tag{16}
\]

where `m=\min A`; the endpoint coefficient cannot cancel because the product on the right has constant coefficient `1`. Thus the polynomial

\[
R_A(X):=X^{-m}P_A(X)
\tag{17}
\]

is fixed by `A` and satisfies

\[
R_A(X)=
\prod_{j=1}^s(1+X^{u_j})^{2^{v_j}}
\quad\text{in }\mathbb F_2[X].
\tag{18}
\]

For each odd integer `d`, take a primitive `d`-th root of unity in the algebraic closure of `\mathbb F_2`. Since `u` is odd, `1+X^u` is square-free, and the multiplicity of a primitive `d`-th root in `R_A` is

\[
e_d
=
\sum_{j:d\mid u_j}2^{v_j}.
\tag{19}
\]

These root multiplicities are determined by `R_A`. If

\[
W_u:=\sum_{j:u_j=u}2^{v_j},
\tag{20}
\]

then `e_d=\sum_{u:d\mid u}W_u`; descending inversion on the finite divisibility poset recovers every `W_u` uniquely. In particular the set of possible odd cores `u` is fixed by `A` and has cardinality at most `s`.

For each ordered position `j`, there are therefore at most `s` choices for `u_j` and at most `1+\log_2L` choices for `v_j`. Once the ordered positive tuple `(a_1,\ldots,a_s)` is chosen, there are at most `2^s` sign patterns for the increments. For each sign pattern, `x` is uniquely determined by `m` because

\[
m=x-\sum_{h_j<0}a_j.
\tag{21}
\]

This proves (14). The argument deliberately overcounts tuples that fail the interval constraint, which is harmless for an upper bound.

## 3. The `L^2` fluctuation is far below the mean scale

The Walsh characters form an orthonormal basis for independent Rademacher signs. From

\[
Q_{s,I}-\mathbb EQ_{s,I}
=
\sum_{A\ne\varnothing}m_A\chi_A
\tag{22}
\]

and Parseval,

\[
\operatorname{Var}(Q_{s,I})
=
\sum_{A\ne\varnothing}m_A^2
\le
\left(\max_A m_A\right)
\sum_A m_A.
\tag{23}
\]

There are at most `L(2L)^s` cubes in total, so (14) gives

\[
\operatorname{Var}(Q_{s,I})
\le
L(2L)^s
\bigl(2s(1+\log_2L)\bigr)^s.
\tag{24}
\]

Dividing by (12),

\[
\boxed{
\|F_{s,I}-\mathbb EF_{s,I}\|_2
\le
L^{-(s+1)/2}
\exp\!\bigl(O(s\log(s\log L))\bigr).
}
\tag{25}
\]

For `s=O(\log\log N)` and `L=N^{\kappa+o(1)}`, the prefactor hidden in (25) is `L^{o(1)}`. This is the gain that the McDiarmid estimate in WI-335 cannot see: worst-case sensitivity is of order `1/L`, whereas the actual random fluctuation is smaller by roughly `L^{-(s-1)/2}`.

## 4. Bonami--Beckner upgrades `L^2` control to a uniform all-interval event

The centered quantity

\[
P_{s,I}:=F_{s,I}-\mathbb EF_{s,I}
\tag{26}
\]

is a multilinear polynomial in the signs of Walsh degree at most

\[
d:=2^s.
\tag{27}
\]

The classical Bonami--Beckner hypercontractive inequality therefore gives, for every `q\ge2`,

\[
\boxed{
\|P_{s,I}\|_q
\le(q-1)^{d/2}\|P_{s,I}\|_2.
}
\tag{28}
\]

Let `\delta=\delta_N`, set

\[
a:=1-\frac\delta4,
\qquad
t:=K^{-a},
\qquad
q:=\lceil4\log N\rceil.
\tag{29}
\]

For every retained order in (3), `s=O(\log\log N)`. Combining (25), (28), `L\ge K`, and `\log q=\log\log N+O(1)` gives

\[
\log\frac{(q-1)^{d/2}\|P_{s,I}\|_2}{t}
\le
\frac d2\log q
-\left(\frac{s+1}{2}-a\right)\log K
+O(s\log(s\log K)).
\tag{30}
\]

For `s\ge3`, condition (3) implies

\[
\frac d2\log q
\le
\left(1-\frac\delta2\right)\log K+o(\delta\log K),
\tag{31}
\]

while the worst case of the second term is `s=3`. Hence

\[
\log\frac{(q-1)^{d/2}\|P_{s,I}\|_2}{t}
\le
-\frac{3\delta}{4}\log K+o(\delta\log K).
\tag{32}
\]

For `s=2`, the first term in (30) is only `O(\log\log N)` and one instead gets

\[
\log\frac{(q-1)^2\|P_{2,I}\|_2}{t}
\le
-\left(\frac12+\frac\delta4\right)\log K+o(\log K).
\tag{33}
\]

The hypothesis `\delta\log\log N\to\infty` makes the `O(s\log(s\log K))=O((\log\log N)^2)` term negligible compared with `\delta\log K`. Thus for some absolute `c>0`, uniformly over every retained `(s,I)`,

\[
(q-1)^{d/2}\|P_{s,I}\|_2/t
\le K^{-c\delta}
\tag{34}
\]

for all sufficiently large `N`. Markov applied to the `q`-th moment yields

\[
\mathbb P(|P_{s,I}|>t)
\le K^{-c\delta q}
=
\exp(-\Omega(\delta\log K\log N)).
\tag{35}
\]

There are only `O(NK)` integer intervals with length in `[K,2K]` and `O(\log\log N)` retained orders. The right side of (35) beats this union by an overwhelming margin. Consequently, with probability `1-o(1)`,

\[
|P_{s,I}|\le K^{-a}
\tag{36}
\]

for every such interval and order simultaneously.

Equation (13) is `K^{-1+o(1)}` uniformly in the same range. Since

\[
(1-a)\log K=\frac\delta4\log K
\gg(\log\log N)^2,
\tag{37}
\]

(13) is `o(K^{-a})`. Therefore the same event satisfies

\[
\boxed{
F_{s,I}\le2K^{-a}
}
\tag{38}
\]

simultaneously for every interval and retained order.

## 5. Energy normalization reaches exactly the diagonal threshold

Multiplying the signs by `\sqrt{\log N}` and taking the `2^{-s}` root of (38),

\[
\log\|b\|_{U^s(I)}
\le
\frac12\log\log N
-\frac{a\log K}{2^s}
+\frac{\log2}{2^s}.
\tag{39}
\]

Using (3),

\[
\frac{\log K}{2^s}
\ge
\frac{\log\log N}{2-\delta},
\tag{40}
\]

so

\[
\log\|b\|_{U^s(I)}
\le
-\frac{\delta}{4(2-\delta)}\log\log N+o(1).
\tag{41}
\]

Condition (1) makes the right side tend to `-\infty`, proving (4).

Now compare with the exact deterministic floor (6). If `R_s=2-\delta`, then

\[
\log\|f\|_{U^s(I)}
\ge
-\frac{\delta}{2(2-\delta)}\log\log N+O_c(1).
\tag{42}
\]

Therefore if `\delta\log\log N=O(1)`, the norm is bounded below by a positive constant and cannot be `o(1)`. In particular `R_s\ge2` already forbids ordinary smallness at comparable energy. Conversely (41) constructs a matched-energy all-interval model whenever `\delta\log\log N\to\infty`. Up to the inessential factor two between the exponents in (41) and (42), the random obstruction now reaches the full asymptotic region in which diagonal cubes permit `o(1)` at all.

This is stronger than the fixed-margin formulation of WI-337: the distance to the critical ratio may shrink to zero, provided it shrinks more slowly than `1/\log\log N`.

## 6. The full bow-scale sliding variance survives on the same realization

The concentration argument above has probability `1-o(1)`. Intersect it with the sliding-square event already used in WI-334--WI-337. Namely, for

\[
S_x:=\sum_{j=1}^{K}\varepsilon_{x+j}u_{x+j},
\qquad
V:=\sum_{x=0}^{N-K}|S_x|^2,
\tag{43}
\]

independence and `|u_n|=1` give

\[
\mathbb EV=(N-K+1)K,
\qquad
\operatorname{Var}(V)=O(NK^3).
\tag{44}
\]

Since `K=o(N)`, Chebyshev gives

\[
V=(1+o(1))NK
\tag{45}
\]

with probability `1-o(1)`. The two high-probability events intersect. Fix one realization in the intersection and multiply by `\sqrt{\log N}`; then (4) and (5) hold simultaneously.

The carrier is arbitrary and prescribed before the signs are chosen. Thus the construction applies to the distinguished bow carrier just as in the earlier interface countermodels.

## 7. Consequence for the accepted bow clue

WI-336 left open the possibility that a genuinely all-start theorem at the single critical Gowers order might outperform the almost-all result. WI-337 could not rule that out because its first-moment argument discarded an exceptional set of starts. Equations (22)--(38) remove exactly that quantifier gap.

At the level of **ordinary normalized Gowers smallness plus matched quadratic energy**, all-start control has no stronger black-box implication for the bow variance than density-one control. Whenever `U^s=o(1)` is compatible with the diagonal energy at a near-critical growing order, there are all-interval Rademacher models with the same output and with full diagonal sliding variance. When the diagonal floor stops those models, it also stops `U^s=o(1)` for the actual source before arithmetic enters.

This does not make the 2023 all-interval arithmetic theorem useless. It says only that its start quantifier cannot resolve the WI-195 gate if the theorem is consumed **solely as ordinary Gowers norm smallness**. Prime-specific signed covariance, the exact `Lambda-Lambda^sharp` decomposition, relative majorant information, or a statistic with diagonal cubes removed can still exploit all-start arithmetic structure in ways the present countermodel does not model.

Accordingly the accepted clue should no longer list “increase the ordinary Gowers order in an all-start theorem” as a live generic escape. The live destination remains its original decisive test: control the actual signed off-diagonal at the distinguished twist, or prove a pointwise structural obstruction.

## 8. Prior-art and novelty audit

The arithmetic theorem surface is established prior art. Matomäki, Shao, Tao and Teräväinen, **Higher uniformity of arithmetic functions in short intervals I. All intervals**, *Forum of Mathematics, Pi* 11 (2023), e29, DOI `10.1017/fmp.2023.28`, prove fixed-order higher-uniformity/nilsequence control in every interval in their stated range. Matomäki, Radziwiłł, Shao, Tao and Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Invent. Math.* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, prove the shorter-scale almost-all analogue, again for every fixed order rather than `s=s(N)`.

The analytic tool in (28) is the classical Bonami--Beckner hypercontractive inequality on the Boolean cube; a standard modern reference is Ryan O'Donnell, **Analysis of Boolean Functions**, Cambridge University Press (2014), Chapter 9 / the hypercontractive theorem. The fact that random functions have small fixed-order Gowers norms is classical and is explicitly used as a benchmark, for example, by Fouvry, Kowalski and Michel, **An inverse theorem for Gowers norms of trace functions over F_p**, *Math. Proc. Cambridge Philos. Soc.* 155 (2013), 277--295.

A targeted repository audit found no prior Mathia use of Bonami/hypercontractivity in this line, and the current frontier in WI-336--WI-337 explicitly leaves the all-start critical strip open. Fresh searches around random/Rademacher Gowers norms, growing-order concentration, and Boolean hypercontractivity located the standard random-function and hypercontractive ingredients but not the interval-uniform growing-order statement (4)--(5), the Laurent-polynomial multiplicity bound (14), or the matching of the all-start obstruction to the diagonal floor at the `1/\log\log N` critical scale. No priority claim is made for the classical ingredients.

The Mathia delta is their combination at the exact WI-195 information interface: the Walsh multiplicity estimate makes Bonami--Beckner strong enough to replace WI-335's worst-case bounded differences and removes the last quantifier-based ordinary-Gowers escape.

## 9. Boundary conditions and falsification tests

This finding must be narrowed or withdrawn if any of the following fails.

1. **Parity polynomial.** Verify that (9) records vertex multiplicities modulo two and that `A(c)=\varnothing` iff some `h_j=0`; this uses the integral-domain property of the Laurent ring and is false only if a nonzero factor `1+X^{h_j}` could vanish.
2. **Multiplicity inversion.** For odd `u`, verify that `1+X^u` is square-free in characteristic two and that primitive odd-order root multiplicities recover the weights `W_u` by descending divisibility inversion. This is the load-bearing step in (14).
3. **Variance.** Recompute Parseval in (22)--(25), including the fact that every nonconstant cube character has Walsh degree at most `2^s` and that the total number of admissible cubes is at most `L(2L)^s`.
4. **Hypercontractive range.** Check (30)--(35) separately for `s=2` and `s\ge3`; the shrinking-margin hypothesis (1) is needed so the subpower multiplicity factor is negligible relative to `\delta\log K`.
5. **Critical matching.** Check that (41) tends to `-\infty` exactly under (1), while the WI-336 lower bound (42) stays bounded away from zero when `\delta\log\log N=O(1)`.
6. **Variance coexistence.** Reproduce the `O(NK^3)` sliding-square variance and intersect its high-probability event with the all-interval hypercontractive event.

The model deliberately ignores prime singular-series identities, positivity of `Lambda`, the exact structured approximant, and signed shifted-prime arithmetic. Those are valid ways to evade the obstruction. The claim is only that **ordinary Gowers norm smallness, at any order where such smallness is compatible with matched energy, is not by itself enough to force the distinguished bow covariance saving even with an all-interval quantifier**.