# MC-096 — Prime-block radialization has an unavoidable collision–reconstruction norm tradeoff

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-095` leaves one natural intermediate possibility between two incompatible extremes. Full product-fiber Walsh coordinates retain exact orthogonality but make generic point evaluation polynomially expensive; total-degree Hamming radialization has subpolynomial endpoint reconstruction but collapses all square-free kernels with the same `omega(a)`. A tempting compromise is to partition the prime coordinates into several blocks and retain the vector of prime counts in those blocks.

For this entire **prime-block count** class there is an exact no-free-lunch theorem. Any such quotient factors the Möbius endpoint through two Hilbert-space maps: a collision map that sums Walsh coefficients sharing a block-count profile, and an endpoint map that recombines the profiles with Möbius parity. Their operator norms cannot both be subpolynomial.

The source-forced lower bound is stronger than the original singleton estimate. Fix any

\[
\sqrt{\frac23}<\alpha<1,
\]

and put

\[
q_{N,\alpha}:=\pi(N)-\pi(\alpha N).
\]

Then every product `a=pq` of two distinct primes `alpha N<p,q<=N` is an actual nonzero product-fiber coordinate, and in fact its coefficient is uniformly positive. Consequently every prime-block partition satisfies, for every `0<r<=1`,

\[
\boxed{
\|A_r\|_{2\to2}\,\|E_r\|_{2\to\mathbb C}
\ge
\sqrt{\binom{q_{N,\alpha}}2}
=
\frac{1-\alpha}{\sqrt2}\frac{N}{\log N}(1+o(1))
=N^{1-o(1)}.
}
\tag{1}
\]

Thus simply replacing the single degree `omega(a)` by finitely or subpolynomially many prime-size/residue/label blocks does **not** reconcile the already available full-Walsh `L^2` bound with cheap endpoint reconstruction. If the quotient has only `N^{o(1)}` relevant profiles and `r=N^{-o(1)}` (in particular, for fixed `r`), the collision step is already `N^{1-o(1)}` on a concrete degree-two source sector; without any lower-scale assumption on `r`, only the radius-independent product tradeoff is asserted. If the collision step is reduced to `N^{o(1)}`, endpoint recombination costs `N^{1-o(1)}`. The product lower bound `(1)` is independent of the choice of prime blocks and of the noise radius.

The degree-two witness is also more informative than the degree-one witness used in the first version of this finding. The **entire degree-one source contribution is absolutely bounded by `O(N log log N)`**, already at the square-scale critical power up to subpolynomial factors. By contrast, the degree-two shell contains a source-forced same-sign prime rectangle of size `asymp N^2/log^2 N`. Hence the first low-degree obstruction is not Möbius parity itself: inside degree two, `mu(a)=+1` throughout, and any critical-scale shell estimate must obtain cancellation from the arithmetic weight outside that coherent rectangle.

This does not rule out block decompositions as arithmetic tools. It rules out obtaining the missing Mertens gain from the **existing generic Walsh norm plus block-count radialization alone**. A surviving block route must prove source-specific cancellation inside collision classes, retain phase/relational data beyond counts, or estimate a coupled recurrence directly.

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

because `|kappa_N(a)|=omega(a)`. On the diagonal `t_1=...=t_B=t`, `(8)` reduces exactly to the one-parameter Hamming deformation of `MC-092`--`MC-095`.

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

Taking `c_a=W_N(a)` gives the Möbius endpoint. Thus every attempt to combine the existing full-fiber Walsh `L^2` information with a block-count shell norm and then recover the endpoint passes, at the generic Hilbert-space level, through `(11)` and `(13)`.

## 3. Degree one is source-nonzero but endpoint-cheap

The original proof used primes `N/2<p<=N` only to certify many nonzero source coordinates. There is a stronger source-level observation: the complete degree-one endpoint contribution is already small enough in absolute value to be harmless at the critical square-scale power.

For `a=p` prime, the only divisors in `(3)` are `1` and `p`. Both are admissible exactly when `pb<=N`; otherwise neither is. Therefore

\[
\boxed{
W_N(p)
=
2\!\sum_{\substack{b\le N/p\\b\ \mathrm{squarefree}\\(b,p)=1}}
 z\!\left(\frac{N^2}{pb^2}\right),
}
\tag{15}
\]

and `W_N(p)=0` for `p>N`. Since `|z(x)|<=1/2`,

\[
|W_N(p)|\le \frac Np.
\tag{16}
\]

Hence the whole degree-one shell obeys

\[
\boxed{
\sum_{\substack{a\in\mathcal A_N\\\omega(a)=1}}|W_N(a)|
\le
N\sum_{p\le N}\frac1p
=
N\log\log N+O(N).
}
\tag{17}
\]

The last estimate is the classical reciprocal-prime theorem recorded in `MC-S6`. Thus the singleton sector can be separated from the endpoint at `N^{1+o(1)}` cost without using any cancellation. The earlier singleton norm lower bound was a valid generic sufficiency obstruction, but it was not by itself evidence that the actual degree-one source was hard.

## 4. Degree two contains a macroscopic same-sign prime rectangle

Fix

\[
\sqrt{\frac23}<\alpha<1
\tag{18}
\]

and take distinct primes

\[
\alpha N<p,q\le N.
\tag{19}
\]

Set `a=pq`. Because `pq>alpha^2 N^2` and `alpha>1/2`, the condition `ab^2<=N^2` forces `b=1`. For `b=1`, the admissible divisors in `(3)` are exactly `p` and `q`: the divisors `1` and `pq` lie outside the interval, while

\[
\frac{pq}{N}\le p,q\le N.
\]

Therefore

\[
R_N(pq,1)=2,
\qquad
W_N(pq)=2z\!\left(\frac{N^2}{pq}\right).
\tag{20}
\]

Moreover

\[
1<\frac{N^2}{pq}<\alpha^{-2}<\frac32,
\]

so on this entire rectangle the centered sawtooth has one fixed sign:

\[
z\!\left(\frac{N^2}{pq}\right)
=
\frac32-\frac{N^2}{pq}.
\]

Consequently

\[
\boxed{
W_N(pq)
\ge
c_\alpha
:=3-2\alpha^{-2}>0.
}
\tag{21}
\]

Every such kernel lies in `mathcal A_N`, has `omega(pq)=2`, and has Möbius sign `mu(pq)=+1`. If

\[
\mathcal T_{N,\alpha}
:=\{pq:\alpha N<p<q\le N,\ p,q\text{ prime}\},
\tag{22}
\]

then by the prime number theorem

\[
|\mathcal T_{N,\alpha}|
=
\binom{q_{N,\alpha}}2
=
\frac{(1-\alpha)^2}{2}\frac{N^2}{\log^2N}(1+o(1)).
\tag{23}
\]

The positive mass carried by this subrectangle is therefore

\[
\boxed{
\sum_{a\in\mathcal T_{N,\alpha}}W_N(a)
\ge
c_\alpha\binom{q_{N,\alpha}}2
\asymp_\alpha \frac{N^2}{\log^2N}.
}
\tag{24}
\]

This is a **submass statement**, not a lower bound on the complete degree-two shell sum. Other degree-two kernels can have the opposite sawtooth sign and cancel `(24)`. But that distinction is precisely informative: any theorem that aims to bound the entire degree-two shell by `O_epsilon(N^{1+epsilon})` must make the complementary degree-two region cancel the explicit positive mass `(24)` to relative discrepancy

\[
O_{\alpha,\varepsilon}\!\left(N^{-1+\varepsilon}\log^2N\right).
\tag{25}
\]

Möbius parity cannot provide that cancellation inside the shell, because `mu(a)=+1` for every square-free `a` of degree two. The required mechanism must act through the arithmetic weights, the reciprocal phase outside the coherent rectangle, or another retained relation.

## 5. Strengthened collision–reconstruction product lower bound

Partition the coordinates in `mathcal T_{N,alpha}` by their block-count profiles. Let `n_k` denote the number of rectangle kernels with profile `k`, and let

\[
D_{N,\alpha}:=\#\{k:n_k>0\}.
\]

All these profiles have total degree `|k|=2`, and `m_k>=n_k`. Therefore `(11)` gives

\[
\|A_r\|_{2\to2}
\ge
r^2\sqrt{\max_k n_k}
\ge
r^2\sqrt{\frac{|\mathcal T_{N,\alpha}|}{D_{N,\alpha}}}.
\tag{26}
\]

Using only the same occurring degree-two profiles in `(13)`,

\[
\|E_r\|_{2\to\mathbb C}
\ge
r^{-2}\sqrt{D_{N,\alpha}}.
\tag{27}
\]

Multiplication cancels both the radius and the number of profiles:

\[
\boxed{
\|A_r\|_{2\to2}\,\|E_r\|_{2\to\mathbb C}
\ge
\sqrt{|\mathcal T_{N,\alpha}|}
=
\sqrt{\binom{q_{N,\alpha}}2}
=N^{1-o(1)}.
}
\tag{28}
\]

This is the strengthened no-free-lunch bound `(1)`. It is forced by a concrete nonzero source sector and is one square-root power stronger than the original singleton proof.

Two regimes make the tradeoff explicit. If the relevant profile family has only `N^{o(1)}` elements, then `(26)` gives

\[
\|A_r\|_{2\to2}\ge r^2 N^{1-o(1)}.
\tag{29}
\]

Hence the standalone collision norm is `N^{1-o(1)}` whenever `r=N^{-o(1)}` (in particular for fixed `r`). Conversely, if the collision map is `N^{o(1)}` on this sector, `(28)` forces

\[
\|E_r\|_{2\to\mathbb C}\ge N^{1-o(1)}.
\tag{30}
\]

The cost cannot be removed by choosing better prime bins; for arbitrary shrinking `r`, the unconditional statement is the product lower bound `(28)` rather than a unilateral collision estimate.

## 6. Sublogarithmic block families remain reconstructible but now maximally collisional at full power

The source limits total support degree to

\[
K_N=O\!\left(\frac{\log N}{\log\log N}\right)
\tag{31}
\]

as in `MC-093`--`MC-095`. A partition into `B_N` prime blocks has at most

\[
D_N\le\binom{K_N+B_N}{B_N}
\tag{32}
\]

block-count profiles. In particular, for

\[
B_N=O(\log\log N),
\]

one has

\[
D_N=N^{o(1)}.
\tag{33}
\]

Thus dyadic prime-size bands, logarithmically many residue/scale classes, or comparable block-count refinements remain cheap enough for endpoint reconstruction at the level of profile dimension. For `r=N^{-o(1)}` (in particular fixed `r`), the degree-two rectangle then forces a generic collision norm `N^{1-o(1)}`, not merely the earlier `N^{1/2-o(1)}`. For unrestricted `0<r<=1`, the radius-independent conclusion remains the product tradeoff `(28)`.

At the opposite extreme, singleton or near-singleton blocks avoid degree-two collisions but create `asymp N^2/log^2N` distinct rectangle profiles, whose generic endpoint recombination costs their square root, `asymp N/logN`.

## 7. Prior art and novelty boundary

Walsh--Fourier expansion, Parseval, noise operators, Fourier levels, and symmetric-function radialization are standard analysis of Boolean functions; a canonical reference is Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014, DOI `10.1017/CBO9781139814782` (also arXiv `2105.10386`).

Partial and block symmetry are established Boolean-function languages rather than Mathia inventions. Eric Blais, Amit Weinstein and Yuichi Yoshida, *Partially Symmetric Functions Are Efficiently Isomorphism Testable*, SIAM Journal on Computing 44 (2015), 411--432, DOI `10.1137/140971877`, treats invariance under large variable-permutation classes. Frederic Green, Daniel Kreymer and Emanuele Viola, *Block-symmetric polynomials correlate with parity better than symmetric*, Computational Complexity 26 (2017), 323--364, DOI `10.1007/s00037-017-0153-3`, explicitly studies block-symmetric polynomial structure and parity correlation.

The underlying Mertens/Huxley--Watt finite identities are already primary prior art in `MC-S24`; reciprocal-prime asymptotics used in `(17)` are recorded in `MC-S6`. A targeted search around Huxley--Watt identities, reciprocal exponential sums, bilinear prime sums, block/partial symmetry, Boolean noise, parity correlation, and orbit-sum Fourier compression supplied no basis for a novelty claim. The operator norms, the prime-rectangle specialization, and the PNT counting step are elementary once the product-fiber representation is fixed.

**No novelty claim is made.** The durable line-specific content is the sharpened consequence for the exact source: degree one is absolutely endpoint-cheap, degree two contains a macroscopic coherent rectangle, and every prime-block count quotient pays the invariant product cost `(28)` on that rectangle.

## 8. Boundaries and decisive continuation

Equation `(28)` is a **sufficiency obstruction**, not a lower bound on the actual value of the Möbius endpoint. Operator norm measures what follows from the current generic `L^2` input for an arbitrary coefficient vector on the same source support. The particular vector `W_N(a)` may have arithmetic cancellation inside block classes, and a theorem exploiting that structure can beat the generic collision norm.

Likewise `(24)` is not a lower bound on the complete degree-two coefficient. It identifies an explicit positive region that must be balanced elsewhere if the whole shell is small. A method that estimates only the complete endpoint can also use cancellation between different degree shells; the shellwise requirement `(25)` applies only to strategies that seek critical-scale control of degree two itself.

The result does not rule out weighted or nonlinear encodings; non-partition transforms; pairwise or higher prime-log geometry; reciprocal-phase decompositions that retain where a degree-two kernel lies inside the shell; source-coupled bilinear estimates; or a block scheme accompanied by an independent theorem for the actual class sums. It says only that the missing gain cannot be obtained by taking the full Walsh Parseval estimate, applying a block-count orbit sum, and paying only generic Hilbert norms.

The decisive continuation is narrower than before. A surviving intermediate representation must do at least one of the following:

1. prove arithmetic cancellation inside the degree-two and higher collision fibers strong enough that the generic norm `(11)` is irrelevant for the actual `W_N` vector;
2. retain phase, prime-log, product-location, or relational information that separates the coherent degree-two rectangle from compensating regions without expanding endpoint reconstruction back to polynomial cost; or
3. provide a coupled estimate and reconstruction theorem whose strict gain is established directly, rather than assembled from the existing full-Walsh variance and a separate generic endpoint bound.

A candidate that merely groups primes into dyadic, logarithmic, residue, or other finitely/subpolynomially many bins and then appeals to the existing Walsh variance is killed by `(28)`.

## Consequence for the research line

`MC-095` showed that total-degree radialization loses the within-shell coordinates on which Walsh Parseval is diagonal and suggested an intermediate quotient as one possible escape. The first version of `MC-096` showed that blockwise prime counts already suffer a `N^{1/2-o(1)}` collision–reconstruction product cost on a nonzero singleton sector.

The sharpened source analysis changes the frontier in two ways. First, the singleton shell itself is not the arithmetic difficulty: it is absolutely `N^{1+o(1)}`. Second, the degree-two shell already contains `N^{2-o(1)}` uniformly positive source coordinates, which upgrades the generic block-count norm tradeoff to **`N^{1-o(1)}`** and shows that plain Möbius parity provides no internal cancellation there.

The useful next object is therefore not a finer prime-count partition by itself. It is a source-forced statistic that retains enough **within-degree reciprocal-phase or prime-log structure** to prove cancellation between the coherent degree-two region and its compensating region, while still admitting subpolynomial-cost transfer to the endpoint.