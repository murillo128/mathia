# MC-242 — Iterated shell differencing forces a double-log blind-support floor

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the `MC-238`–`MC-241` shell-character setup. Let

\[
T\subset\{r\text{ prime}:y<r\le 2y\}
\]

be the active local support of a nonprincipal smooth-dilation blind character, let

\[
q_\chi=\prod_{r\in T}r,
\qquad
m(\chi)=|T|,
\]

and assume

\[
\chi(p)=1
\qquad (p\le y\text{ prime}).
\tag{1}
\]

`MC-241` proves only that `m(chi)->infinity`. The explicit iterated differencing inequalities in Cochrane–Granville–Zheng sharpen this to a quantitative support floor. With natural logarithms,

\[
\boxed{
\liminf_{y\to\infty}
\frac{m(\chi)}{\log\log y}
\ge \frac1{\log 2}
}
\tag{2}
\]

along any sequence of nonprincipal blind shell characters. Equivalently, for every fixed

\[
0<\theta<\frac1{\log 2},
\]

all sufficiently large `y` satisfy

\[
\boxed{
m(\chi)>\theta\log\log y.}
\tag{3}
\]

A representation-free equivalent form is

\[
\boxed{
2^{m(\chi)}\ge (\log y)^{1-o(1)}.
}
\tag{4}
\]

Thus a surviving annihilator relation cannot merely have support tending slowly to infinity. It must couple at least logarithmically many shell factors on the `log y` scale.

The argument does **not** invoke Theorem 3 of Cochrane–Granville–Zheng as a black box with a growing differencing depth. Their theorem is stated after fixing that depth. Instead, the proof below returns to their explicit Proposition 7 and the prime-modulus complete-sum estimate in Proposition 6, where all dependence on the number of differencing steps is visible. This avoids a hidden uniformity assumption.

No annihilator-triviality statement, Möbius progression estimate, bound for `M(X)`, or consequence for the zeta zero set is proved.

## 1. Blindness again forces a linear character sum just above `y`

Fix once and for all

\[
1<u<\sqrt e,
\qquad
N=y^u.
\tag{5}
\]

Exactly as in `MC-241`, `(1)` implies

\[
\chi(n)=1
\qquad\text{for every }y\text{-smooth }n.
\tag{6}
\]

Every such integer is coprime to `q_chi`, since all conductor primes lie above `y`. For `1<u<2`, the elementary reciprocal-prime calculation in `MC-241` gives

\[
\Psi(y^u,y)
=
(1-\log u+o(1))N.
\tag{7}
\]

Using only `Re chi(n)>=-1` off the smooth set,

\[
\operatorname{Re}\sum_{n\le N}\chi(n)
\ge
\bigl(1-2\log u+o(1)\bigr)N.
\tag{8}
\]

Since `u<sqrt(e)`, the coefficient in `(8)` is positive. Therefore every blind character has

\[
\boxed{
\left|\frac1N\sum_{n\le N}\chi(n)\right|\gg_u 1.
}
\tag{9}
\]

Any upper bound tending to zero at this same scale gives a contradiction.

## 2. Expose one shell prime after `k=m-1` explicit differencing steps

Write

\[
m=m(\chi),
\qquad
k=m-1.
\]

Choose one active shell prime `Q in T` and enumerate the remaining active primes as

\[
q_1,\dots,q_k.
\]

Then

\[
q_\chi=q_1\cdots q_kQ,
\qquad
y<q_i,Q\le2y,
\tag{10}
\]

and the factors are pairwise coprime. Put

\[
a_{q_\chi}(n)=\chi(n).
\]

Cochrane–Granville–Zheng Proposition 7 applies the `q`-analogue of van der Corput differencing to this factorization. With

\[
M_i=\left\lfloor\left(\frac N{q_i}\right)^{2/3}\right\rfloor,
\tag{11}
\]

it gives the explicit normalized estimate

\[
\left|\frac1N\sum_{n\le N}\chi(n)\right|
\le
4\sum_{i=1}^k M_i^{-2^{-i}}
+
4\,\mathbf E_Q^{\,2^{-k}},
\tag{12}
\]

where `mathbf E_Q` is the average, over all differencing displacement tuples, of the remaining normalized `Q`-periodic correlation sum.

Because `q_i<=2y` and `N=y^u`, there is a fixed constant `c_u>0` such that, uniformly in `i`,

\[
\log M_i\ge c_u\log y
\tag{13}
\]

for all sufficiently large `y`. Hence

\[
\sum_{i=1}^k M_i^{-2^{-i}}
\le
k\exp\!\left(-\frac{c_u\log y}{2^k}\right).
\tag{14}
\]

The only remaining issue is to bound the exposed prime-modulus term uniformly in the growing depth `k`.

## 3. A prime remainder costs only `2^k Q^{-1/2}` before the final root

Specialize the complete-sum estimate of Cochrane–Granville–Zheng Proposition 6 to

\[
f(x)=x,
\qquad
g(x)=0,
\]

and to the nonprincipal active local component `chi_Q` modulo the prime `Q`. For a fixed displacement tuple `\mathbf h`, the prime-modulus estimate gives, after capping by the trivial bound when a displacement collision occurs,

\[
\max_{b\bmod Q}
\left|
\frac1Q
\sum_{n\bmod Q}
\chi_Q(f^*_{\mathbf h}(n))
 e\!\left(\frac{bn}{Q}\right)
\right|
\ll
2^k Q^{-\frac12\max\{0,1-v_Q(\mathbf h)\}}.
\tag{15}
\]

Here the harmless absolute factor hidden in `<<` includes the fixed base degree `2(deg f+deg g)=2`.

The algebraic exclusion in Proposition 6 is also harmless in this regime. Its exceptional integer `Delta(f,g,k)` contains only fixed algebraic factors and primes below `k+O(1)`. Under the contradiction range used below, `k=O(log log y)`, whereas `Q>y`, so

\[
(Q,\Delta(f,g,k))=1
\tag{16}
\]

for sufficiently large `y`.

Now average `(15)` over the displacement tuples. If no difference `h_{i,1}-h_{i,0}` is divisible by `Q`, the factor in `(15)` contributes `Q^{-1/2}`. By Lemma 7 of the same paper, for each coordinate the proportion of pairs with

\[
Q\mid h_{i,1}-h_{i,0}
\]

is `<1/Q`. A union bound therefore gives exceptional proportion `<k/Q`. Lemma 5 contributes only

\[
1+\frac{Q\log Q}{N}=1+o(1),
\tag{17}
\]

because `Q<=2y` and `u>1`. Consequently

\[
\boxed{
\mathbf E_Q
\ll
2^k\left(Q^{-1/2}+\frac{k}{Q}\right)
\ll
2^kQ^{-1/2}
}
\tag{18}
\]

whenever `k=O(log log y)`. Taking the `2^{-k}` root required by `(12)`,

\[
\mathbf E_Q^{\,2^{-k}}
\ll
\exp\!\left(
-\frac{\log Q}{2^{k+1}}
+O\!\left(\frac{k}{2^k}\right)
\right).
\tag{19}
\]

This is the quantitative gain that is lost if one uses only a fixed-`k` theorem statement.

## 4. The differencing depth cannot stay below `(1/log 2) log log y`

Fix

\[
\theta<\frac1{\log 2}
\]

and suppose, toward contradiction, that a sequence of blind characters satisfies

\[
m\le\theta\log\log y.
\tag{20}
\]

Then also `k=m-1<=theta log log y`, and if

\[
\delta:=1-\theta\log 2>0,
\]

we have

\[
2^k\le(\log y)^{1-\delta}.
\tag{21}
\]

The first term in `(12)` is therefore, by `(14)`,

\[
k\exp\!\left(-\frac{c_u\log y}{2^k}\right)
\le
k\exp\!\left(-c_u(\log y)^\delta\right)
=o(1).
\tag{22}
\]

Since `Q>y`, `(19)` similarly gives

\[
\mathbf E_Q^{\,2^{-k}}
\le
\exp\!\left(-\tfrac12(\log y)^\delta+o((\log y)^\delta)\right)
=o(1).
\tag{23}
\]

Thus `(12)` yields

\[
\frac1N\left|\sum_{n\le N}\chi(n)\right|=o(1),
\tag{24}
\]

contradicting the positive lower bound `(9)`. This proves `(3)`. Since `(3)` holds for every fixed `theta<1/log 2`, it implies `(2)` and `(4)`.

For the quadratic Legendre matrix `A` of `MC-238`, every nonzero blind vector therefore obeys the corresponding Hamming-weight bound

\[
\operatorname{wt}(v)
\ge
\left(\frac1{\log2}-o(1)\right)\log\log y.
\tag{25}
\]

This does not prove full column rank; it says only that any kernel vector must become increasingly global across shell columns at an explicit rate.

## 5. Prior art and novelty audit

The analytic machinery is literature. Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026), develops the required explicit `q`-van der Corput framework. Proposition 7 gives `(12)` with constants remaining bounded after the successive roots, Proposition 6 supplies the prime complete-sum estimate used in `(15)`, and Lemma 7 controls displacement collisions. Their Proposition 7 is explicitly described as very similar to Graham–Ringrose's earlier iterative lemma. See `MC-S46`.

Their Theorem 3 also displays the characteristic loss from iterated differencing, but it begins by fixing the integer `k`; the subsequent proof of Theorem 4 explicitly remarks that `k` is fixed there. Therefore `MC-242` does **not** substitute a growing `k(y)` into a fixed-parameter theorem. The support floor comes from re-auditing the displayed inequalities whose `k`-dependence is explicit.

The smooth-number lower bound is the same elementary `1<u<2` calculation already used in `MC-241`, based on Mertens' reciprocal-prime asymptotic (`MC-S6`). Least-character-nonresidue arguments that oppose a long initial block of `chi=1` to character-sum cancellation are classical, and smooth-modulus character sums go back through Graham–Ringrose and later refinements. The source-specific contribution recorded here is only the specialization of the 2026 explicit differencing bounds to the exact shell-radical annihilator from `MC-239`, with the resulting quantitative support threshold. **No novelty claim is made.**

A broad literature search found the standard least-nonresidue and smooth-modulus character-sum results but no source stating this shell-support corollary in the present notation. Absence from that search is not evidence of novelty.

## Decisive audit

The critical possible failure is hidden non-uniformity in the number of differencing steps. That is why the proof uses Proposition 7 and Proposition 6 directly rather than Theorem 1, Corollary 2, or Theorem 3 with a varying parameter. Proposition 7 makes the repeated-root constants explicit and bounded (`<4` after the `2^k`-th root), while Proposition 6 displays the complete-sum dependence as an explicit `2^k` factor before that root. The collision average in `(18)` is uniform because each coordinate costs at most `1/Q`.

The threshold `1/log 2` is a threshold of this particular iterative estimate, not an asserted arithmetic optimum. At the boundary `2^k` comparable with `log y`, the exponential decay in `(22)`–`(23)` is no longer forced to tend to zero, so the present proof cannot cross it without additional information.

## Boundaries and updated frontier

- `(2)` does not prove `H_y(Q_S)=G_S`; blind characters with support well above `log log y` remain possible.
- The result controls support size only. It does not bound the number, order, or distribution of surviving blind characters.
- No Fourier decay of the smooth-dilation measure on nonblind modes follows from the support floor.
- No bound is obtained for the Möbius progression amplitudes paired with these characters; a high-support mode could still matter unless a separate coupling estimate rules it out.
- No RH, GRH, zero-density, or zero-free-region input is used.
- No estimate for `B_S(X)`, `M(X)`, or the zeta zero set follows directly.

The live annihilator gate is now narrower than after `MC-241`: a surviving exact blind mode must involve at least

\[
\left(\frac1{\log2}-o(1)\right)\log\log y
\]

shell primes. The next useful question is whether the same explicit differencing architecture, or a different source-specific argument, can force still larger support, eventual annihilator triviality, or quantitative small coupling between such highly collective modes and the Möbius progression vector.