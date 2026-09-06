# MC-096 — Prime-block radialization has an unavoidable collision–reconstruction norm tradeoff

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-095` leaves one natural intermediate possibility between two incompatible extremes. Full product-fiber Walsh coordinates retain exact orthogonality but make generic point evaluation polynomially expensive; total-degree Hamming radialization has subpolynomial endpoint reconstruction but collapses all square-free kernels with the same `omega(a)`. A tempting compromise is to partition the prime coordinates into several blocks and retain the vector of prime counts in those blocks.

For this entire **prime-block count** class there is an exact no-free-lunch theorem. Any such quotient factors the Möbius endpoint through two Hilbert-space maps: a collision map that sums Walsh coefficients sharing a block-count profile, and an endpoint map that recombines the profiles with Möbius parity. Their operator norms cannot both be subpolynomial. In fact their product is already forced to have size at least

\[
\boxed{
\bigl(\pi(N)-\pi(N/2)\bigr)^{1/2}
=N^{1/2-o(1)}.
}
\tag{1}
\]

This lower bound is forced by the source itself, not by unused ambient Walsh coordinates: for every prime `N/2<p<=N`, the product-fiber coefficient `W_N(p)` of `MC-092` is nonzero.

Thus simply replacing the single degree `omega(a)` by finitely or subpolynomially many prime-size/residue/label blocks does **not** reconcile the already available full-Walsh `L^2` bound with cheap endpoint reconstruction. If the quotient has only `N^{o(1)}` profiles, the collision step has norm `N^{1/2-o(1)}`; if the collision step is reduced to `N^{o(1)}`, the endpoint recombination has norm `N^{1/2-o(1)}`. More generally the product lower bound `(1)` is independent of how the prime blocks are chosen.

This does not rule out block decompositions as arithmetic tools. It rules out obtaining the missing Mertens gain from the **existing generic Walsh norm plus block-count radialization alone**. A surviving block route must prove source-specific signed cancellation inside the collision classes, or use additional structure not determined only by block-count profiles.

No improved Mertens estimate is claimed.

## 1. Block-count refinement of the Hamming deformation

Use the exact product-fiber coefficients from `MC-092`:

\[
W_N(a)
:=
\sum_{\substack{b\ \mathrm{squarefree}\\(a,b)=1\\ab^2\le N^2}}
R_N(a,b)
 z\!\left(\frac{N^2}{ab^2}\right),
\tag{2}
\]

for square-free `a`, where

\[
R_N(a,b)
=
\#\left\{d\mid a:\frac{ab}{N}\le d\le\frac{N}{b}\right\}.
\tag{3}
\]

Let

\[
\mathcal A_N
:=\{a\le N^2:a\text{ square-free and }W_N(a)\ne0\}.
\tag{4}
\]

Fix any finite partition of the prime coordinates relevant to `a<=N^2`,

\[
\Pi_N=\{\mathcal P_{1,N},\ldots,\mathcal P_{B_N,N}\}.
\tag{5}
\]

For `a in mathcal A_N`, define its block-count profile

\[
\kappa_N(a)
=(\kappa_1(a),\ldots,\kappa_{B_N}(a)),
\qquad
\kappa_j(a):=\#\{p\mid a:p\in\mathcal P_{j,N}\}.
\tag{6}
\]

For every occurring profile `k`, put

\[
S_k:=\{a\in\mathcal A_N:\kappa_N(a)=k\},
\qquad
m_k:=|S_k|,
\qquad
C_k:=\sum_{a\in S_k}W_N(a).
\tag{7}
\]

The associated multivariate block radialization is

\[
\boxed{
\mathcal Q_{N,\Pi}(t_1,\ldots,t_{B_N})
=
\sum_{a\in\mathcal A_N}
W_N(a)\prod_{j=1}^{B_N}(-t_j)^{\kappa_j(a)}
=
\sum_k(-1)^{|k|}C_k t^k.
}
\tag{8}
\]

At the all-one point,

\[
\boxed{
\mathcal Q_{N,\Pi}(1,\ldots,1)
=
\sum_a\mu(a)W_N(a)
=
\mathcal Q_N(1),
}
\tag{9}
\]

because `|kappa_N(a)|=omega(a)`. On the diagonal `t_1=...=t_B=t`, `(8)` reduces exactly to the one-parameter Hamming deformation of `MC-092`--`MC-095`. Hence `(8)` is not an externally fitted family; it is the canonical refinement obtained by remembering several prime-count coordinates instead of only total degree.

## 2. Exact collision and endpoint operator norms

Fix `0<r<=1`. On the finite coefficient space `ell_2(mathcal A_N)`, define the weighted block-collision operator

\[
(A_r c)_k
:=r^{|k|}\sum_{a\in S_k}c_a.
\tag{10}
\]

Because the sets `S_k` are pairwise disjoint, the rows of `A_r` are orthogonal. Therefore

\[
\boxed{
\|A_r\|_{2\to2}
=
\max_k r^{|k|}\sqrt{m_k}.
}
\tag{11}
\]

On the profile space define endpoint recovery by

\[
E_r(d)
:=
\sum_k(-1)^{|k|}r^{-|k|}d_k.
\tag{12}
\]

Its exact Hilbert norm is

\[
\boxed{
\|E_r\|_{2\to\mathbb C}
=
\left(\sum_{k:m_k>0}r^{-2|k|}\right)^{1/2}.
}
\tag{13}
\]

The factorization is exact:

\[
\boxed{
E_r A_r c
=
\sum_{a\in\mathcal A_N}\mu(a)c_a.
}
\tag{14}
\]

Taking `c_a=W_N(a)` gives the hard Möbius endpoint. Thus every attempt to combine the existing full-fiber Walsh `L^2` information with a block-count shell norm and then recover the endpoint passes, at the generic Hilbert-space level, through the two exact norms `(11)` and `(13)`.

The parameter `r` does not remove the tradeoff below: its factor appears with opposite powers in the singleton collision and reconstruction sectors and cancels from their product.

## 3. The source has a macroscopic nonzero singleton sector

The lower bound is not caused by Walsh coordinates whose source coefficient happens to vanish. Let `p` be prime with

\[
\frac N2<p\le N.
\tag{15}
\]

For `a=p`, the divisor set in `(3)` is `{1,p}`. If `b>=2`, then `b>N/p`, so neither divisor can satisfy both inequalities in `(3)`. For `b=1`, both divisors are admissible. Consequently

\[
\boxed{
W_N(p)=2z\!\left(\frac{N^2}{p}\right).
}
\tag{16}
\]

This never vanishes for all sufficiently large integer `N`. Indeed `z(x)=0` would require the fractional part of `x` to equal `1/2`, hence

\[
\frac{2N^2}{p}\in2\mathbb Z+1.
\tag{17}
\]

For odd `p`, `(17)` implies `p|N`; but `p>N/2` then forces `N=p`, in which case `2N^2/p=2N` is even, a contradiction. The finitely many small cases are immaterial.

Therefore every prime in `(N/2,N]` belongs to `mathcal A_N`. By the prime number theorem,

\[
q_N
:=\#\{p:N/2<p\le N\}
=\pi(N)-\pi(N/2)
=\frac{N}{2\log N}(1+o(1)).
\tag{18}
\]

So the exact source vector has `N^{1-o(1)}` nonzero degree-one Walsh coordinates available to collide under any prime-block quotient.

## 4. Collision–reconstruction product lower bound

Let `b_N` be the number of blocks of `Pi_N` that meet the prime interval `(N/2,N]`. For each such block `j`, the singleton profile `e_j` occurs, and

\[
m_{e_j}
\ge
\#\{p\in\mathcal P_{j,N}:N/2<p\le N\}.
\tag{19}
\]

Pigeonhole gives

\[
\max_j m_{e_j}\ge\frac{q_N}{b_N}.
\tag{20}
\]

Using only these degree-one profiles in `(11)` and `(13)`,

\[
\|A_r\|_{2\to2}
\ge
r\sqrt{\frac{q_N}{b_N}},
\tag{21}
\]

while

\[
\|E_r\|_{2\to\mathbb C}
\ge
r^{-1}\sqrt{b_N}.
\tag{22}
\]

Multiplying cancels both the arbitrary block count and the noise radius:

\[
\boxed{
\|A_r\|_{2\to2}\,
\|E_r\|_{2\to\mathbb C}
\ge
\sqrt{q_N}
=
N^{1/2-o(1)}.
}
\tag{23}
\]

This is the promised tradeoff. It holds for every prime partition, including partitions depending on `N`, and uses only source coefficients that are provably nonzero.

Two immediate regimes clarify the obstruction.

First, let `D_N` be the number of nonempty block-count profiles. If the quotient is small enough that generic endpoint aggregation costs only `N^{o(1)}`, then necessarily `b_N<=D_N=N^{o(1)}` and `(21)` gives, for fixed `r`,

\[
\boxed{
\|A_r\|_{2\to2}
\ge N^{1/2-o(1)}.
}
\tag{24}
\]

Thus a subpolynomial-dimensional profile space cannot inherit the full Walsh `L^2` scale through a generic contraction.

Conversely, if one refines the blocks until the collision norm in `(21)` is only `N^{o(1)}`, then `(20)` forces

\[
b_N=N^{1-o(1)},
\tag{25}
\]

and hence `(22)` gives

\[
\boxed{
\|E_r\|_{2\to\mathbb C}
\ge N^{1/2-o(1)}.
}
\tag{26}
\]

The power cost has simply moved from compression to reconstruction.

## 5. Sublogarithmic block families are reconstructible but maximally collisional

The source itself limits total support degree to

\[
K_N=O\!\left(\frac{\log N}{\log\log N}\right)
\tag{27}
\]

as in `MC-093`--`MC-095`. Therefore a partition into `B_N` prime blocks has at most

\[
D_N
\le
\binom{K_N+B_N}{B_N}
\tag{28}
\]

possible block-count profiles.

In particular, if

\[
B_N=O(\log\log N),
\tag{29}
\]

then

\[
\log D_N=O((\log\log N)^2)=o(\log N),
\qquad
D_N=N^{o(1)}.
\tag{30}
\]

So dyadic prime-size bands, logarithmically many residue/scale classes, or any comparable block-count refinement remain cheap enough for endpoint reconstruction at the level of profile dimension. But `(24)` then forces an `N^{1/2-o(1)}` generic collision norm before that reconstruction. This is exactly the compromise that looked available after `MC-095`, and it does not preserve the already available full-Walsh orthogonality at subpolynomial cost.

At the opposite extreme, singleton or near-singleton prime blocks preserve the degree-one Walsh coordinates, but then there are `N^{1-o(1)}` distinct degree-one profiles and generic endpoint recombination itself costs their square-root scale.

## 6. Prior art and novelty boundary

Walsh--Fourier expansion, Parseval, noise operators, Fourier levels, and symmetric-function radialization are standard analysis of Boolean functions; a canonical reference is Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014, DOI `10.1017/CBO9781139814782` (also arXiv `2105.10386`).

Partial and block symmetry are established Boolean-function languages rather than Mathia inventions. Eric Blais, Amit Weinstein and Yuichi Yoshida, *Partially Symmetric Functions Are Efficiently Isomorphism Testable*, SIAM Journal on Computing 44 (2015), 411--432, DOI `10.1137/140971877`, treats invariance under large variable-permutation classes. Frederic Green, Daniel Kreymer and Emanuele Viola, *Block-symmetric polynomials correlate with parity better than symmetric*, Computational Complexity 26 (2017), 323--364, DOI `10.1007/s00037-017-0153-3`, explicitly studies block-symmetric polynomial structure and parity correlation.

The operator norms `(11)`--`(13)` are elementary finite-dimensional linear algebra for disjoint orbit-sum rows, and `(18)` is the classical prime number theorem. A targeted literature check around block/partial symmetry, Boolean noise, parity correlation, and orbit-sum Fourier compression supplied no basis for claiming a new general theorem for these ingredients.

**No novelty claim is made.** The durable line-specific content is the exact composition of those classical mechanisms with the Huxley--Watt product-fiber coefficients, especially the source nonvanishing identity `(16)` and the resulting uniform tradeoff `(23)` for every prime-block count quotient.

## 7. Boundaries and decisive continuation

Equation `(23)` is a **sufficiency obstruction**, not a lower bound on the actual value of the Möbius endpoint. Operator norm measures what follows from the current generic `L^2` input for an arbitrary coefficient vector on the same source support. The particular vector `W_N(a)` may have additional arithmetic cancellation inside block classes, and a theorem exploiting that structure can beat the collision norm.

The result also does not rule out weighted or nonlinear encodings that retain information other than block counts; non-partition transforms; pairwise or higher prime-log geometry; source-coupled bilinear estimates; or a block scheme accompanied by an independent theorem for the signed class sums. It says only that the missing gain cannot be obtained by taking the full Walsh Parseval estimate, applying a block-count orbit sum, and paying only the generic Hilbert norms.

Nor is the number of blocks itself the invariant. A huge number of blocks can still collide badly, and a small number can be useful if arithmetic structure controls the resulting shell sums directly. The invariant exposed by `(23)` is the tradeoff between **actual singleton collisions** and **endpoint profile multiplicity**.

The decisive continuation is therefore narrower than the second option left by `MC-095`. An intermediate source-forced quotient must do at least one of the following:

1. prove arithmetic cancellation inside its fibers strong enough that the generic collision norm `(11)` is irrelevant for the actual `W_N` vector;
2. retain signed/phase/relational information beyond prime-count profiles so that the singleton sector is not collapsed by an orbit-sum map of this form; or
3. provide a coupled estimate and reconstruction theorem whose gain is established directly, rather than assembled from the existing full-Walsh norm and a separate generic endpoint bound.

A candidate that merely groups primes into dyadic, logarithmic, residue, or other finitely/subpolynomially many bins and then appeals to the existing Walsh variance is killed by `(23)`.

## Consequence for the research line

`MC-095` showed that total-degree radialization loses the within-shell coordinates on which Walsh Parseval is diagonal and suggested an intermediate quotient as one possible escape. `MC-096` tests the most natural family of such intermediates: remember several blockwise prime counts instead of only total degree.

The result is negative but sharp enough to redirect the live route. **Prime-block refinement cannot make generic Walsh orthogonality and cheap Möbius endpoint reconstruction coexist; their norm costs have an invariant product of at least `N^{1/2-o(1)}` already on the nonzero singleton-prime sector.** Any useful intermediate representation now needs genuinely arithmetic within-fiber cancellation or a carrier richer than block counts, not merely a better choice of prime bins.