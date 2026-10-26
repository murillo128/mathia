# PC-461 — Admissible triplets force cotangent populations above the pair spectrum

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-SIEVE-BOUNDARY. The full conductor-scaled cotangent matrix on a primorial complete tube has a growing population of both positive and negative eigenvalues above the largest atom of PC-460's leading pair law. The two shortest admissible triplets force an explicit lower bound of order `N/(log y)^3`, uniformly in refinement. This is a lower bound, not a second-order counting asymptotic or a classification of all outliers. Its arithmetic coefficient is the classical prime-triplet singular series; no prime-tuple conjecture or zeta-zero implication is used.

## 1. Statement and the missing population

Let
\[
d_y=\prod_{p\le y}p,\qquad N=d_y m,\qquad m\ge1,
\qquad Y=\{a\bmod N:(a,d_y)=1\},\qquad M=|Y|.
\]
On the coordinate space of `Y`, retain the full matrices
\[
T_{ab}=\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T^+=T+J_M/N,
\tag{1}
\]
including the diagonal of the all-ones augmentation. Write
`n_+(A,t)=#{lambda(A)>t}` and `n_-(A,t)=#{lambda(A)<-t}`,
with multiplicity.

Put
\[
\lambda_2=\frac1{2\pi},\qquad \lambda_3=\frac7{12\pi},\qquad
\mathfrak S_3=\frac92\prod_{p\ge5}\frac{p^2(p-3)}{(p-1)^3}>0.
\tag{2}
\]
For every fixed `lambda_2<t<lambda_3`, either sign and either matrix convention satisfy
\[
\boxed{\quad
\liminf_{y\to\infty}\ \inf_{m\ge1}
\frac{(\log y)^3}{d_y m}\,n_\pm(T^{(+)},t)
\ \ge\ 2e^{-3\gamma}\mathfrak S_3.
\quad}
\tag{3}
\]
The factor two counts the different shapes `{0,2,6}` and `{0,4,6}`. It does not count the two signs: the bound holds separately for each sign.

By [[research/prime_circle/findings/PC-460-primorial-cotangent-rare-spectrum-has-a-prime-pair-counting-law]], all fixed thresholds above `lambda_2` have
\[
n_\pm(T^{(+)},t)=o\!\left(\frac{N}{(\log y)^2}\right)
\tag{4}
\]
uniformly in `m`. Equation (3) proves that this smaller population nevertheless contains at least a positive constant times `N/(log y)^3` eigenvalues. In particular, the largest pair-law atom is not a spectral edge, and the exceptions above it are not merely finitely many local spectral points.

## 2. The two extremal admissible three-point blocks

For a fixed finite integer set `F`, let `H_F` be the Hermitian matrix with off-diagonal entries
\[
(H_F)_{fg}=\frac{i}{\pi(f-g)}\quad(f\ne g),
\qquad (H_F)_{ff}=0.
\tag{5}
\]
For `F={0,a,a+b}`, `a,b>0`, its eigenvalues are
\[
0,\quad \pm\frac1\pi
\sqrt{\frac1{a^2}+\frac1{b^2}+\frac1{(a+b)^2}}.
\tag{6}
\]
Indeed a three-dimensional real skew-symmetric matrix has eigenvalues zero and an opposite imaginary pair; the squared magnitude of that pair is the sum of the squares of its three upper-triangular entries. Multiplication by `i/pi` gives (6).

A pattern is *admissible* if it omits a residue class modulo every prime. An admissible triple has all its points of the same parity, so `a,b` are positive even integers. The pair `a=b=2` is excluded modulo `3`. The expression under the square root in (6) strictly decreases in either gap. Thus its largest possible value among admissible triples is attained exactly at `(a,b)=(2,4)` or `(4,2)`, up to translation and ordering. Both patterns are admissible: they occupy one class modulo `2`, two modulo `3`, and at most three modulo every larger prime. Their positive eigenvalue is
\[
\frac1\pi\sqrt{\frac14+\frac1{16}+\frac1{36}}
=\frac7{12\pi}=\lambda_3>\lambda_2.
\tag{7}
\]
This maximizes the three-point block eigenvalue only; it is not an upper bound for the full matrix or for larger constellations.

The corresponding principal block of (1), on any translate of either pattern, has eigenvalues `0,+lambda_N,-lambda_N`, where
\[
\lambda_N=\left[\sum_{h\in\{2,4,6\}}
\left(\frac1N\cot\frac{\pi h}N\right)^2\right]^{1/2}
\longrightarrow\lambda_3.
\tag{8}
\]
The convergence is uniform over `m>=1`, since `N>=d_y->infinity`. Translation across the circle's coordinate cut changes differences by multiples of `N` and leaves the cotangent entries unchanged.

## 3. Almost all triplet copies can be separated by any fixed distance

Let `F_1={0,2,6}` and `F_2={0,4,6}`. For any fixed integer pattern `F`, CRT gives the exact count
\[
A_y(F):=\#\{a\bmod N:a+F\subset Y\}
=N\prod_{p\le y}\left(1-\frac{\nu_p(F)}p\right),
\qquad \nu_p(F)=|F\bmod p|.
\tag{9}
\]
Every allowed residue modulo `d_y` has exactly `m` lifts, even when `m` shares prime factors with `d_y`. This is the classical constellation count already present in [[research/prime_circle/findings/PC-149-finite-chord-word-traces-are-lucas-totient-singular-series]].

For an admissible fixed pattern of size `r`, the product
\[
\mathfrak S(F)=\prod_p
\frac{1-\nu_p(F)/p}{(1-1/p)^r}
\]
converges absolutely to a positive number: outside finitely many primes, `nu_p(F)=r`, and the factor is `1+O_F(p^-2)`. Mertens's product theorem therefore gives
\[
A_y(F)\sim \frac{N e^{-r\gamma}\mathfrak S(F)}{(\log y)^r}.
\tag{10}
\]
For either `F_j`, the factors at `2` and `3` are `4` and `9/8`, respectively, giving exactly `mathfrak S(F_j)=mathfrak S_3` in (2).

Fix an integer `L>12`. Regard a copy as a *typed start* `(a,j)` with `a+F_j subset Y`. Discard every typed start having another typed start `(b,k)` at circular center distance at most `L`, including a different type at the same center.

For a signed displacement `s` with `|s|<=L`, two distinct typed starts impose the union pattern
\[
F_j\cup(s+F_k).
\tag{11}
\]
Its size is at least four. Two translates of these three-point sets can coincide only for the same type and `s=0`, the excluded identical-copy case. Each remaining union is either inadmissible and eventually absent, or has count `O_L(N/(log y)^4)` by (9)--(10). There are finitely many types and displacements. The number discarded is at most twice the number of close unordered copy pairs, hence is also `O_L(N/(log y)^4)`.

The surviving copies are disjoint, their centers have circular separation greater than `L`, and their total number satisfies
\[
K_{y,L}\sim\frac{2N e^{-3\gamma}\mathfrak S_3}{(\log y)^3}.
\tag{12}
\]
All these asymptotics and error bounds are uniform over `m>=1`. The separation cutoff is fixed before taking `y->infinity`; no growing-window sieve estimate is asserted.

## 4. Full long-range interactions preserve the population lower bound

Compress `T` to the union of the `K=K_(y,L)` selected copies, obtaining a `3K`-dimensional principal matrix `B`. Let `D` keep its diagonal three-point blocks and set the entries between different copies to zero. The full matrix has not been replaced by `D`; the error must be controlled.

For circular integer distance `delta_N(u)>0`,
\[
\left|\frac1N\cot\frac{\pi u}N\right|
\le\frac1{\pi\delta_N(u)}.
\tag{13}
\]
If two centers have distance `delta>L>12`, any two vertices from their copies have circular distance at least `delta-6>=delta/2`. Each of the nine entries between those copies is therefore at most `2/(pi delta)` in magnitude.

For a fixed center, order the other centers separately in the two semicircles. Separation by more than `L` puts the `j`th center in either direction at distance at least `jL`. Consequently
\[
\sum_{b\ne a}\frac1{\delta_N(a-b)^2}
\le\frac{2}{L^2}\sum_{j\ge1}\frac1{j^2}
=\frac{\pi^2}{3L^2}.
\]
Summing squared entries over the ordered block pairs gives
\[
\boxed{\qquad \|B-D\|_{\rm HS}^2\le\frac{12K}{L^2}.\qquad}
\tag{14}
\]
This is a bound per selected copy. It does not claim operator-norm smallness of the full cotangent tail.

For Hermitian matrices, spectral truncation of `E=B-D` at size `epsilon>0` splits it into an operator of norm at most `epsilon` and an operator of rank at most `epsilon^-2 ||E||_HS^2`. Min--max and finite-rank interlacing then give
\[
n_+(B,t)\ge n_+(D,t+\epsilon)
-\epsilon^{-2}\|B-D\|_{\rm HS}^2.
\tag{15}
\]
Choose `epsilon>0` with `t+epsilon<lambda_3`. By (8), for all sufficiently large `y`, every diagonal block contributes one eigenvalue above `t+epsilon`, uniformly in `m`. Principal-submatrix interlacing and (14)--(15) imply
\[
n_+(T,t)\ge n_+(B,t)
\ge K\left(1-\frac{12}{\epsilon^2L^2}\right).
\tag{16}
\]
First let `y->infinity` at fixed `L`, using (12), and then let `L->infinity`. This proves (3) for the raw positive count. Complex conjugation sends `T` to `-T`, giving the same negative count exactly.

Finally, `T^+-T` has rank one, so either signed count changes by at most one. Since `(log y)^3/N->0` uniformly over refinements, the augmented assertion follows. Its exact finite spectral symmetry is not assumed.

## 5. Consequences, controls, and evidence boundary

PC-460 determines the full leading population of order `N/(log y)^2` from isolated pairs. The proof above identifies a strictly higher spectral range populated by three-point interactions at a smaller but still divergent scale. A single principal-block interlacing argument would supply only one eigenvalue; (11)--(16) are needed to retain the asymptotic number of copies despite overlaps and long-range coupling.

The same comparison works for any other support having these two asymptotic triplet counts, negligible close-copy collisions, and the same cotangent kernel. Thus this surviving population has an explicit classical sieve explanation. The comparison blocks retain the triplet geometry and its arithmetic frequencies deliberately; they are not a matched full support with all arithmetic information removed.

Neither (3) nor the comparison proves:

- an asymptotic equality at scale `N/(log y)^3`, or a matching upper bound;
- concentration of these finite eigenvalues near `lambda_3`, rather than merely above a fixed smaller threshold;
- a complete classification at `t=lambda_2`, `t=lambda_3`, or moving thresholds;
- localization of individual full-matrix eigenvectors, completeness of the anchor/antipodal limits in PC-459, or a norm limit;
- any implication about actual prime triplets, zeta zeros, or RH.

The upper bound (4) and lower bound (3) leave a real interval of possible population sizes. Larger patterns and long-range collective effects are not excluded. The theorem closes only the question whether the sector above the leading pair atoms can consist of boundedly many exceptions.

## 6. Prior art and validation

The arithmetic is classical. G. H. Hardy and J. E. Littlewood, *Some problems of “Partitio numerorum”; III: On the expression of a number as a sum of primes*, **Acta Mathematica 44** (1923), 1--70, [§5.68, p. 63](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5327-11511_2006_Article_BF02403921.pdf), explicitly discuss the two triplet shapes and their equal predicted prime frequency. K. S. Kedlaya's [*Notes on analytic number theory*, Definition 19.1](https://kskedlaya.org/ant/chap-k-tuples.html) records the singular-series normalization used here. We use exact reduced-residue counts, not the conjectural passage from local densities to prime counts.

J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, **Bull. Amer. Math. Soc. 50** (2013), 527--628, [Theorem 3.3.2](https://arxiv.org/pdf/1303.1856), supplies the Mertens product theorem in (10). W. Ejsmont and F. Lehner, *The Trace Method for Cotangent Sums*, **J. Combin. Theory Ser. A 177** (2021), 105324, [author manuscript](https://arxiv.org/abs/2002.06052), is neighboring finite cotangent-matrix and trace theory. CRT, finite-block eigenvalues, separation packing, Hilbert--Schmidt perturbation and interlacing are standard mechanisms.

Directed searches covered cotangent/reduced-residue spectra, sieved discrete Hilbert matrices, triplet spectra and sparse-cluster eigenvalue bounds. The local duplication check included PC-149's finite-word constellation counts, PC-150's leading matching law and PC-460's full cotangent pair law. Those counts and tools are not new. The additional conclusion here is the explicit, uniform-refinement multiplicity lower bound **above the largest leading atom**, with a full-matrix interaction estimate. No historical priority claim is made.

The proof is analytic, not Lean-verified. Standard-library Python checked **26** exact triplet counts and **234** exact union-pattern counts at primorial cutoffs through `13`, with refinements `1,2,3`; inadmissible unions and overlaps were included. Rational arithmetic checked the three-point extremal formula on **1,922** admissible even-gap pairs with gaps at most `100`. System LAPACK `zheev`, called through `ctypes`, checked **26** finite block spectra, **21** nonempty separated-copy Hilbert--Schmidt bounds, **756** perturbation inequalities, **96** principal-compression count inequalities, and **96** rank-one count comparisons. Full matrices had dimension at most `480`; selected compressions had at most `60` copies. The maximum block-eigenvalue error was below `1.2e-16`, the raw spectral-symmetry error below `3.9e-16`, and the largest observed ratio of the squared Hilbert--Schmidt error to (14)'s bound was below `0.032`. These are finite consistency checks, not proofs of the limits. Scratch code and outputs remain outside Git.

The decisive audit points are the two distinct shape counts, the four-point minimum in every nonidentical close-copy union, uniformity in arbitrary refinement, circular rather than linear separation, counting all nine entries per ordered block pair, the squared Hilbert--Schmidt normalization by `K`, the order `y->infinity` before `L->infinity`, and retaining only a lower bound after principal compression.
