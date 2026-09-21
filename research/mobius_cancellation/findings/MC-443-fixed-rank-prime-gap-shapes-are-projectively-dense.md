# MC-443 — Fixed-rank prime-divisor gap shapes are projectively dense

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-436` proved that, at every fixed rank, every strict ordering of the adjacent gaps between selected prime divisors is realizable. The same prime-number-theorem construction gives a substantially stronger fixed-rank statement: after forgetting common scale, selected-prime gap vectors are dense in the entire positive gap-shape space.

Fix `r>=2`. For primes

\[
p_1<p_2<\cdots<p_r
\]

define

\[
g_i=p_{i+1}-p_i\quad(1\le i\le r-1),
\qquad
S(g)=\sum_{i=1}^{r-1}g_i=p_r-p_1,
\]

and the normalized gap shape

\[
\sigma(p_1,\ldots,p_r)
=
\left(\frac{g_1}{S(g)},\ldots,\frac{g_{r-1}}{S(g)}\right).
\tag{1}
\]

Let

\[
\Delta_{r-2}^{\circ}
=
\left\{u\in\mathbb R_{>0}^{r-1}:\sum_i u_i=1\right\}
\tag{2}
\]

be the open simplex of positive gap shapes. Then

\[
\boxed{
\left\{\sigma(p_1,\ldots,p_r):p_1<\cdots<p_r\text{ primes}\right\}
\text{ is dense in }\Delta_{r-2}^{\circ}.
}
\tag{3}
\]

Equivalently, the projective rays of positive prime-divisor gap vectors are dense in the full positive projective gap cone. Taking

\[
n=p_1\cdots p_r
\]

shows that these are genuine gap shapes of the ordered prime divisors of squarefree integers with `omega(n)=r`.

Consequently, let `Phi` be any continuous scale-invariant statistic of a fixed-rank positive gap vector,

\[
\Phi(\lambda g)=\Phi(g)\qquad(\lambda>0),
\tag{4}
\]

with values in a metric space. Then

\[
\boxed{
\overline{\Phi(\mathcal G_r^{\rm prime})}
=
\overline{\Phi(\mathbb R_{>0}^{r-1})},
}
\tag{5}
\]

where `G_r^prime` is the set of gap vectors arising from `r` selected primes. The same holds for any finite vector of such observables.

Thus no continuous fixed-rank **gap-shape** observable can separate rational-prime divisor geometry from generic positive-gap controls by a forbidden range, an open-set exclusion, or any positive topological margin. Prime-derived shapes come arbitrarily close to every generic positive shape.

This does not compare distributions, frequencies, source heights, or growing-rank behavior. It gives no estimate for `M(x)`.

## 1. Density from macroscopic prime intervals

Fix an arbitrary target

\[
u=(u_1,\ldots,u_{r-1})\in\Delta_{r-2}^{\circ}
\]

and an accuracy `eta>0`. Choose a fixed offset `a>0` and cumulative target locations

\[
c_1=a,
\qquad
c_j=a+\sum_{i=1}^{j-1}u_i\quad(2\le j\le r).
\tag{6}
\]

Then

\[
c_{j+1}-c_j=u_j,
\qquad
c_r-c_1=1.
\tag{7}
\]

Choose `delta>0` so small that

\[
4\delta<\min_i u_i
\tag{8}
\]

and small enough that the normalization error below is less than `eta`. For a scale `X`, consider the fixed-proportion intervals

\[
I_j(X)=[(c_j-\delta)X,(c_j+\delta)X].
\tag{9}
\]

They are pairwise disjoint and ordered by `(8)`. By the prime number theorem, each `I_j(X)` contains a prime for every sufficiently large `X`. Choose one prime `p_j\in I_j(X)`. The ordering of the intervals gives

\[
p_1<\cdots<p_r.
\]

Write

\[
p_j=(c_j+\varepsilon_j)X,
\qquad |\varepsilon_j|\le\delta.
\]

Then

\[
\frac{g_i}{X}
=
u_i+\varepsilon_{i+1}-\varepsilon_i,
\qquad
\left|\frac{g_i}{X}-u_i\right|\le2\delta,
\tag{10}
\]

and

\[
\frac{S(g)}X
=1+\varepsilon_r-\varepsilon_1,
\qquad
\left|\frac{S(g)}X-1\right|\le2\delta.
\tag{11}
\]

For `delta<1/4`, equations `(10)` and `(11)` imply uniformly in `i`

\[
\frac{g_i}{S(g)}=u_i+O_u(\delta).
\tag{12}
\]

Since `delta` can be chosen arbitrarily small, `(12)` places a prime-derived normalized gap shape inside every neighborhood of `u`. This proves `(3)`.

The proof is deliberately weaker than any prime-tuple theorem: the selected primes need not be consecutive in the ambient prime sequence, and each interval has length proportional to `X`. No small-gap, Hardy-Littlewood, or simultaneous fixed-offset prime conjecture is being used.

## 2. Continuous fixed-rank shape statistics inherit the density

A positive gap vector modulo common scaling is represented uniquely by its normalized point in `(2)`. Hence every continuous scale-invariant statistic `Phi` in `(4)` descends to a continuous map

\[
\phi:\Delta_{r-2}^{\circ}\to Y.
\]

Given any `u` in the simplex, choose prime-derived shapes `u_m` converging to `u` by `(3)`. Continuity gives

\[
\phi(u_m)\to\phi(u).
\]

Therefore every value attained on a generic positive gap shape lies in the closure of the values attained on prime-derived shapes. The reverse inclusion is automatic because prime-derived gap vectors are a subset of the positive cone. This proves `(5)`.

The conclusion is a range/robust-separation obstruction. It is stronger than saying that all rank permutations occur: every open neighborhood *inside each permutation chamber*, and across the whole simplex, is approximated by actual prime-divisor gap shapes.

## 3. Application to the path-distance determinant branch

For the path-distance matrix of `MC-440`--`MC-442`, scaling all gaps by `lambda` scales the matrix by the same factor:

\[
D(\lambda g)=\lambda D(g).
\]

Writing

\[
\det(XD(g)-I_r)=\sum_{k=0}^r c_k(g)X^k,
\]

one therefore has

\[
c_k(\lambda g)=\lambda^k c_k(g).
\tag{13}
\]

Hence each normalized coefficient

\[
\widehat c_k(g)=\frac{c_k(g)}{S(g)^k}
\tag{14}
\]

is a continuous scale-invariant function of the gap shape. Equation `(5)` implies

\[
\overline{\{\widehat c_k(g):g\in\mathcal G_r^{\rm prime}\}}
=
\overline{\{\widehat c_k(g):g\in\mathbb R_{>0}^{r-1}\}}.
\tag{15}
\]

More strongly, the whole finite normalized coefficient vector

\[
(\widehat c_2,\ldots,\widehat c_r)
\tag{16}
\]

has the same image closure on prime-derived and generic positive gap shapes.

Likewise the first order-sensitive scalar from `MC-441`,

\[
J(g)=\frac1{g_1}+\frac1{g_{r-1}}
-S(g)\sum_{i=1}^{r-2}\frac1{g_i g_{i+1}},
\tag{17}
\]

satisfies

\[
J(\lambda g)=\lambda^{-1}J(g).
\]

Thus

\[
\widehat J(g)=S(g)J(g)
\tag{18}
\]

is continuous and scale-invariant, and its prime-derived value set is dense in its generic positive-gap value set.

`MC-442` already proved that raw coefficient signs and the raw sign of `J` are source-generic. Equations `(15)`--`(18)` now give a different obstruction for magnitudes: **at fixed rank, normalized path-distance magnitudes cannot isolate the rational-prime source by range or by a robust margin either**. A generic positive-gap control can be approximated arbitrarily closely by a prime-divisor chain in every such continuous normalized observable.

This does not say the prime and control *distributions* of those observables agree. A distributional bias, source-height law, or growing-rank effect remains logically possible.

## 4. Representation and invariance audit

The intrinsic object here is the ordered finite prime-divisor chain only through its adjacent positive gaps. Translation of all vertex locations is already quotiented out when passing to gaps. The additional equivalence relation used in the theorem is common positive scaling,

\[
g\sim\lambda g,
\]

because the claim concerns **shape** rather than absolute arithmetic size.

The normalized simplex `(2)` is merely a convenient cross-section of that projective quotient. The density statement is therefore invariant under replacing `(1)` by any other continuous coordinates on the positive projective cone. It is not an artifact of choosing the normalization `S(g)=1`.

Absolute scale is intentionally not discarded when a proposed mechanism genuinely uses it. Such a mechanism lies outside the no-go `(5)` and must pay whatever source-height or analytic cost its scale dependence entails.

## 5. Prior art and novelty boundary

The mathematical input is classical. `MC-S15` records a prime-number-theorem source strong enough for the ordinary PNT used above, and `MC-436` already used exactly the same fixed-proportion-interval construction to realize every gap-rank permutation. The present theorem extracts the full continuous consequence of that construction instead of retaining only its ordinal consequence.

Adjacent literature on gaps between prime divisors includes Efthymios Sofos, *Gaps between prime divisors and analogues in Diophantine geometry*, Glasgow Mathematical Journal 65 (2023), S129--S147, DOI `10.1017/S0017089522000398`, which studies statistical/moment behavior of prime-divisor gaps. That is a different question from the elementary fixed-rank macroscopic realization argument here.

No novelty is claimed for the prime number theorem, primes in fixed proportional intervals, or the resulting elementary density argument as a standalone number-theoretic theorem. The durable Mathia contribution is the frontier consequence: the gap-order escape opened by `MC-436` has no fixed-rank robust geometric range discriminator once common scale is removed, and this applies immediately to the normalized path-distance observables surviving `MC-440`--`MC-442`.

## Boundaries and falsification tests

- **Fixed rank is essential.** The threshold scale needed to realize an `eta`-approximation may depend arbitrarily badly on `r`, the target shape, and `eta`. No uniform growing-rank density theorem is proved.
- **No source-height efficiency is proved.** The squarefree integer `n=prod p_i` realizing a shape may be enormously larger than the corresponding primorial-scale source. This is the same load-bearing limitation already present in `MC-436`.
- **Selected primes are not required to be consecutive primes globally.** The gaps are between adjacent selected prime divisors of `n`; unused ambient primes may lie between them.
- **Density is not equidistribution.** Nothing here compares how often different shapes occur, gives a limiting measure, or matches rational-prime statistics to a random/Beurling control.
- **Approximation is not exact coincidence.** A discontinuous invariant, exact integrality condition, algebraic identity, or arithmetic source label can separate a dense subset from its ambient space. Equation `(5)` rules out only continuous robust shape separation.
- **Scale-sensitive observables are outside the corollary.** Absolute prime size, source height, or a coupled scale-shape statistic may carry arithmetic information; it must be analyzed with its scale dependence intact.
- **Growing-rank observables remain open.** A family whose rank increases with source size can evade the fixed-`r` topological argument even if every individual rank obeys `(3)`.
- **No Möbius estimate follows.** The result constrains one representation route; it does not establish cancellation, a zero-free region, or RH.

## Consequence for the research line

The gap-order branch now has a sharper boundary. `MC-436` showed that global ordinal gap relations have enough raw source capacity to escape bounded local summaries. `MC-440`--`MC-442` then showed that the canonical path-distance determinant retains order only in subleading magnitudes and has completely source-generic signs. The present result rules out the next tempting interpretation: at any fixed rank, those normalized magnitudes cannot become a robust prime-specific range invariant, because prime-divisor gap shapes are already dense in the entire generic positive shape space.

A useful continuation must therefore exploit something not captured by fixed-rank continuous projective gap geometry: quantitative **distribution** of shapes, effective source-height costs, a growing-rank phenomenon, or a genuinely arithmetic/discontinuous observable. Merely changing the continuous normalized functional of a fixed number of prime-divisor gaps cannot produce a topologically isolated Möbius cancellation mechanism.