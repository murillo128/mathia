# FD-336 — Growing Farey gap-block shuffles retain the Brownian spectral null

**Status:** LITERATURE+DERIVED + EXACT-FINITE-CALIBRATION + UNCONDITIONAL-WEAK-LIMIT + LOCAL-ORDER-BOUNDARY.

The reflection/same-gap null in FD-335 forgets all local order. A strictly more constrained null preserves the internal order of consecutive blocks of genuine Farey gaps. For every deterministic integer block length `b>=1` with `b=o(Q)`, this null still has the same normalized Brownian energy and growing-band allocation laws. Dress's absolute-discrepancy theorem controls centered internal block motion by `2/Q`, independently of block length, while a truncated large-gap second moment prevents the centered block variance from collapsing. In particular, for any prescribed window length `h=o(Q)`, an admissible block choice preserves a proportion tending to one of its original labeled occurrences without changing those limiting laws. Its finite mean energies must nevertheless be recalculated: the single-gap Green formula is generally false for this ensemble.

This resolves a specified stronger-control calibration question from the accepted gap-ordering clue. It does not preserve the complete adjacent-pair inventory, estimate the original Farey spectrum, or prove a new Franel–Landau bound.

## 1. A realizable block ensemble and its limit

Use the genuine order-`Q` Farey grid with both endpoints,
\[
0=x_0<\cdots<x_N=1,\qquad N=\sum_{d\le Q}\varphi(d)=2m,
\quad g_i=x_i-x_{i-1},\quad a_i=g_i-1/N.
\]
Assume `Q>=3`. Its first-half gaps sum to `1/2`, and `a_1+...+a_m=0`.

For an integer `b>=1`, write `m=Kb+r`, `0<=r<b`, and require `K>=2`. Partition the first `Kb` gaps into `K` labeled consecutive blocks of length `b`. Uniformly permute these blocks **without changing their internal order**, append the unchanged final `r` gaps of the first half, and reflect the resulting half-word to form the second half. The sample space is the `K!` block-label permutations; repeated identical blocks give equal multiplicities to distinct output block words. The reconstructed points are cumulative sums of these positive gaps.

The ensemble preserves reflection, endpoints, the full gap multiset, every chosen block word and the anchored remainder. It changes block seams. It need not preserve denominator edges, Hall–Shiu indices, or the entire overlapping local-block inventory.

Define centered block totals and their squared mass by
\[
s_j=\sum_{t=1}^b a_{(j-1)b+t},\quad
S=\sum_{j=1}^K s_j=-\sum_{i=Kb+1}^m a_i,
\quad c_j=s_j-S/K,\quad V_b=\sum_{j=1}^K c_j^2.
\tag{1}
\]
For a sampled grid put `D_k=x_k^pi-k/N` and
\[
E=\sum_{k=1}^{N-1}D_k^2,\qquad
 d_u=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(\pi uk/N),
\qquad E_q=\sum_{j=1}^q d_{2j}^2.
\tag{2}
\]
All expectations below use this block ensemble, with the original Farey population fixed. Let
\[
A=E/\mathbb E E,\qquad f_q=\mathbb E E_q/\mathbb E E,
\qquad S_q=(E_q/E)/f_q,\qquad Q_q=E_q/\mathbb E E_q=A S_q.
\tag{3}
\]
The subscripted `Q_q` is a statistic, not the Farey order.

**Theorem.** For every deterministic integer sequence
\[
1\le b=b(Q),\qquad b/Q\longrightarrow0,
\tag{4}
\]
`V_b>0` eventually. If `B` is a standard Brownian bridge, then the interpolated first-half discrepancy process satisfies
\[
\left(\frac{D_{\lfloor mt\rfloor}}{\sqrt{V_b}}\right)_{0\le t\le1}
\ \Rightarrow\ (B(t))_{0\le t\le1}
\tag{5}
\]
in the uniform topology, with linear interpolation understood at the grid points. Write
\[
W=\int_0^1B(t)^2dt
 =\sum_{j\ge1}\frac{Z_j^2}{\pi^2j^2},
\qquad Z_j\text{ independent }N(0,1).
\]
Then
\[
\boxed{\frac{E}{NV_b}\Rightarrow W,\qquad
\frac{\mathbb E E}{NV_b}\longrightarrow\frac16,\qquad A\Rightarrow6W.}
\tag{6}
\]
For every deterministic `q=q(Q)->infinity` with `q<=m-1`,
\[
\boxed{f_q\longrightarrow1,\qquad S_q\longrightarrow1\text{ in probability},
\qquad (A,Q_q)\Rightarrow(6W,6W).}
\tag{7}
\]
In particular, both predeclared bands `floor(sqrt(Q))` and `floor(Q^(2/3))` have this law. The amplitude limit remains nondegenerate, with variance `4/5`.

For fixed `b>1` the preserved fraction of within-block adjacencies is positive. For `b->infinity` satisfying (4), all but `O(1/b)` of the original **labeled adjacent occurrences** survive, yet (6)–(7) remain valid. More generally, for `h=o(b)`, all but `O(h/b)` of the original labeled length-`h` windows lie inside the retained blocks or remainder. For any prescribed deterministic integer `h=h(Q)>=1` with `h=o(Q)`, choose `b=ceil(sqrt(Q h))`. Then `h/b->0`, `b/Q->0`, and the same Brownian law holds while retaining a proportion tending to one of the length-`h` windows. The block choice depends on the prescribed sequence `h`; no single `b=o(Q)` is claimed to dominate every such sequence. This is density-one preservation of occurrences, not equality of the complete window-count matrix: seam-crossing windows can change.

## 2. Exact finite calibration, including the anchored remainder

Let `a_j` now denote the column vector of `b` centered gaps in block `j`, and set
\[
\bar a=K^{-1}\sum_j a_j,\qquad z_j=a_j-\bar a,
\qquad C=\sum_j z_jz_j^{\mathsf T}.
\tag{8}
\]
Thus `V_b=1^T C 1`. For deterministic half-grid weights `w=(w_1,...,w_m)`, let `w_j` be the vector of its weights in block slot `j`, and define
\[
L_w=\sum_{i=1}^m w_i a_i^\pi,\qquad
\mu_w=\sum_{i>Kb}w_i a_i+\sum_{j=1}^K w_j^{\mathsf T}\bar a.
\]
For any two weight vectors `w,v`, exactly,
\[
\boxed{\mathbb E L_w=\mu_w,\qquad
\operatorname{Cov}(L_w,L_v)=
\frac1{K-1}\sum_{j=1}^K w_j^{\mathsf T}C v_j
-\frac{(\sum_jw_j)^{\mathsf T}C(\sum_jv_j)}{K(K-1)}.}
\tag{9}
\]
Indeed a uniform block permutation has
`E[z_pi(j) z_pi(l)^T]=C/K` for `j=l`, and `-C/[K(K-1)]` otherwise. Expanding the two linear forms proves (9); the anchored tail contributes only to their means.

For `H_k=D_k`, `0<=k<=m`, take `w_i=1_(i<=k)`. Reflection gives `D_(N-k)=-H_k`, so
\[
\mathbb E E=2\sum_{k=1}^{m-1}\{\mu_{w^{(k)}}^2+
\operatorname{Var}(L_{w^{(k)}})\}.
\tag{10}
\]
For the even sine coefficient take
\[
w_i^{[u]}=\frac2{\sqrt m}\sum_{k=i}^{m-1}\sin(\pi uk/m),
\qquad d_{2u}=L_{w^{[u]}}.
\tag{11}
\]
Equations (9)–(11) give the exact total and band expectations, all spectral covariances, and any nonzero finite means. Odd coefficients vanish identically. Finite even modes need not be uncorrelated or centered; one must not import FD-335's diagonal covariance into the block ensemble. For `b=1`, these formulas reduce to that single-gap result.

## 3. Uniform internal motion and the large-gap variance reservoir

FD-335 derives directly from the coprime Farey denominator triangle that
\[
V_1:=\sum_{i=1}^m a_i^2
\sim\frac6{\pi^2}\frac{\log Q}{Q^2},\qquad
\max_i g_i=1/Q,\qquad N\sim3Q^2/\pi^2.
\tag{12}
\]
These are unconditional arithmetic inputs, not assumptions about random independent gaps. Using only `b max g_i` would control a block by `b/Q`. Rank separation gives a stronger elementary bound, and the absolute-discrepancy theorem removes its logarithmic block-length loss.

### 3.1 Uniform mass of a consecutive gap window

Any two distinct fractions of denominator at most an integer `R<=Q` are separated by at least `floor(Q/R)` gaps in `F_Q`. To prove this, first take neighbors `a/q<c/d` in `F_R`. Their determinant is one, so all the fractions
\[
\frac{a+kc}{q+kd},\qquad
1\le k\le\left\lfloor\frac{Q-q}{d}\right\rfloor,
\]
are distinct reduced fractions strictly between the two endpoints. The number of these fractions is at least `floor(Q/R)-1`. Nonneighboring `F_R` endpoints are separated by at least as many `F_Q` gaps.

For any `b` consecutive gaps, let `A_R` count their `b+1` vertices of denominator at most `R`. It follows that
\[
A_R\le1+\frac b{\lfloor Q/R\rfloor}
\le1+\frac{2bR}{Q}.
\tag{13a}
\]
The last bound also holds for real `1<=R<=Q`, by taking its integer part. Writing the vertex denominators as `q_i`, the exact integral identity for reciprocal integers gives
\[
\sum_{i=0}^b\frac1{q_i}
=\frac{b+1}{Q}+\int_1^Q\frac{A_t}{t^2}\,dt
\le1+\frac{b+1}{Q}+\frac{2b\log Q}{Q}.
\]
Neighboring denominators satisfy `q_i+q_(i+1)>Q`. Their gap is therefore at most `2/[Q min(q_i,q_(i+1))]`. Summing over the window yields
\[
\boxed{\sum_{\text{window}}g_i
\le\frac4Q\left(1+\frac{b+1}{Q}
                   +\frac{2b\log Q}{Q}\right)
\ll\frac1Q+\frac{b\log(2Q)}{Q^2}.}
\tag{13b}
\]
The estimate is uniform over the starting rank, including endpoint windows. It gives gap mass `O(1/Q)` when `b<=Q/log(2Q)`.

For the full range (4), use the **original** Farey discrepancies
`delta_k=x_k-k/N`, distinguished from the shuffled `D_k` in (2). Dress's theorem gives `max_k |delta_k|<=1/Q`, with `delta_0=delta_m=delta_N=0`. This uses exactly the positive-point convention `A_Q(x_k)=k`; the extra zero endpoint has discrepancy zero. Hence every original consecutive window, of any length `t` and starting rank `l`, satisfies
\[
\boxed{\left|\sum_{i=l+1}^{l+t}a_i\right|
=|\delta_{l+t}-\delta_l|\le2/Q,\qquad
\sum_{i=l+1}^{l+t}g_i\le t/N+2/Q.}
\tag{13b-D}
\]
In particular, under (4), every block and partial prefix has mass `O(1/Q)`. At the anchored remainder the sharper identities are
`S=delta_(Kb)` and `sum_(i>Kb)^m g_i=r/N-S`, so
\[
|S|\le1/Q,\qquad
\sum_{i=Kb+1}^m g_i\le r/N+1/Q=O(1/Q).
\]
Also `|s_j|<=2/Q`, `|c_j|<=3/Q`, and every centered within-block prefix is at most `2/Q` in absolute value. These centered bounds hold for any block length with `K>=2`; only the uncentered mass conclusion here uses `b=o(Q)`. They are properties of the genuine input blocks, not a Dress bound asserted for the shuffled grid.

### 3.2 Large gaps cannot be removed by centering the blocks

Put `G_j=sum_(t=1)^b g_((j-1)b+t)`, `T=sum_j G_j<=1/2`, and `lambda=T/K`. Then `c_j=G_j-lambda` and
\[
V_b=\sum_j(G_j-\lambda)^2.
\]
For any block containing a gap `g_i>=2 lambda`, positivity gives `G_j-lambda>=G_j/2`. Consequently the following is an exact finite inequality:
\[
V_b\ge\frac14\sum_{\substack{i\le Kb\\g_i\ge2\lambda}}g_i^2.
\tag{13c}
\]
Thus subtracting the block mean does not cost `b/Q^2` against the entire second moment: it suffices to retain the gaps above that mean.

For large `Q`, (12) gives `m>=Q^2/8` and `K>=m/(2b)`, hence `lambda<=8b/Q^2`. Choose
\[
R=\left\lfloor\frac{Q}{32b}\right\rfloor.
\]
Condition (4) implies `R->infinity`, `R<Q/2`, and `log R=log(Q/b)+O(1)`. Every gap having an endpoint denominator at most `R` is at least `1/(RQ)>=32b/Q^2>=2 lambda`.

The coprime denominator triangle counts the squared mass of precisely these gaps. With `q_i` now the denominators of the complete Farey grid, reflection and `R<Q/2` give
\[
\begin{aligned}
\sum_{\substack{1\le i\le m\\\min(q_{i-1},q_i)\le R}}g_i^2
&=\sum_{q\le R}\frac1{q^2}
  \sum_{\substack{Q-q<d\le Q\\(q,d)=1}}\frac1{d^2}\\
&\ge\frac1{Q^2}\sum_{q\le R}\frac{\varphi(q)}{q^2}
 =\frac{(6/\pi^2)\log R+O(1)}{Q^2}.
\end{aligned}
\tag{13d}
\]
The inner interval has exactly `phi(q)` coprime residues. The last estimate follows from `phi(q)/q=sum_(d|q)mu(d)/d` and the harmonic sum; it uses no cancellation hypothesis.

Removing the final `r<b` gaps loses at most their total mass squared, which is `O(Q^-2)` by (13b-D) and the remainder bound. Combining (13c)–(13d) proves, along every sequence in (4),
\[
\boxed{V_b\gg\frac{\log(Q/b)}{Q^2}>0.}
\tag{13e}
\]
In particular `Q^2 V_b->infinity` because `Q/b->infinity`; no fixed logarithmic separation between `b` and `Q` is required. The implicit lower-bound constant is absolute once `Q/b` is sufficiently large, although the onset may depend on the chosen sequence.

The centered bounds following (13b-D), together with (13e), now give
\[
\frac{\max_j|c_j|}{\sqrt{V_b}}
+\frac{|S|+\max_{j,t}|\sum_{i=1}^t a_{(j-1)b+i}|}{\sqrt{V_b}}
\ll\frac1{\sqrt{\log(Q/b)}}=o(1).
\tag{14}
\]
This verifies both the vanishing-jump condition for the block totals and the negligibility of internal block motion. It also excludes an ensemble of identical block totals asymptotically. The expression in (14) is a deterministic error bound, not a distributional convergence rate.

For comparison, positivity and Cauchy–Schwarz still give the general bounds
`V_1-O(b/Q^2)<=V_b<=bV_1`: removing the remainder costs at most `b/Q^2`, subtracting `T^2/K` costs `O(b/Q^2)`, and `sum_j s_j^2<=bV_1`. Combining the upper bound and (13e) with the mean limit proved below gives
\[
\log(Q/b)\ll\mathbb E E
\le(1+o(1))\frac3{\pi^4}b\log Q.
\tag{15}
\]
For `b=o(log Q)`, the sharper lower bound remains
`E[E]>=(1-o(1))(3/pi^4)log Q`. No exact leading amplitude or universal formula for `V_b/V_1` is asserted across the larger range.

## 4. Bridge limit and passage to growing bands

Let `R_k=sum_(j<=k)c_pi(j)`, `0<=k<=K`. The array `c_j/sqrt(V_b)` has zero sum, squared mass one and vanishing maximum by (14). The classical exchangeable-increment bridge criterion therefore yields convergence of its interpolated partial sums to `B`. One may assign independent uniform times to these deterministic increments, apply Kallenberg's criterion in the form of Bertoin's Lemma 2.1(i), and order the times. The order-statistic time change tends uniformly to the identity, giving the uniform block-permutation process.

Define the coarse half-grid path
\[
Y_{kb+t}=R_k\quad(0\le k<K,\ 0\le t<b),
\qquad Y_{Kb+t}=0\quad(0\le t\le r).
\]
At an interior block position,
\[
H_{kb+t}=R_k+kS/K+
\sum_{i=1}^t a_{(\pi(k+1)-1)b+i}.
\]
Consequently `max|H-Y|<=3/Q` deterministically by (13b-D): the drift `kS/K` costs at most `1/Q` and the centered partial block at most `2/Q`. On the anchored tail, `H_(Kb+t)=delta_(Kb+t)` and `Y=0`, so the error is at most `1/Q`. Moreover `Kb/m->1` and the largest coarse jump divided by `sqrt(V_b)` tends to zero. These facts prove (5) and convergence of the total-energy and each fixed sine-coefficient functional.

The expectation in (6) requires a moment argument, not just weak convergence. The exact finite-population formula is
\[
\mathbb E R_kR_l=\frac{V_b}{K-1}
\left(\min(k,l)-\frac{kl}{K}\right).
\tag{16}
\]
It gives
\[
\frac{2\sum_{i=0}^{m-1}\mathbb E Y_i^2}{NV_b}
=\frac{b(K+1)}{6m}\longrightarrow\frac16.
\tag{17}
\]
The normalized Euclidean distance between the full reflected `H` and `Y` paths is at most `C/(Q sqrt(V_b))=o(1)`. Cauchy–Schwarz and (17) then show that their normalized expected energies differ by `o(1)`. The same bound applies to every fixed orthogonal sine projection. Equation (16), by Riemann summation, gives its limiting covariance. Thus for fixed `J`, jointly,
\[
\frac{d_{2j}}{\sqrt{NV_b}}\Rightarrow\frac{Z_j}{\pi j}
\quad(1\le j\le J),\qquad
\frac{\mathbb E E_J}{NV_b}\longrightarrow
L_J:=\sum_{j\le J}\frac1{\pi^2j^2}.
\tag{18}
\]

For any diverging `q(Q)`, eventually `q>=J`. Orthogonal projection and nonnegativity give
\[
\limsup_{Q\to\infty}\frac{\mathbb E(E-E_q)}{NV_b}
\le\frac16-L_J.
\]
Letting `J->infinity` makes this zero. Markov's inequality and `E/(NV_b) => W>0` imply `(E-E_q)/E -> 0` in probability; the expectation statements imply `f_q->1`. This proves (7). No uniform high-mode diagonalization or unproved exchange of a growing cutoff with a process limit is used.

## 5. Verification, prior art and boundary

An independent exact-rational enumeration constructed genuine Farey fractions, partitioned their actual first-half gaps, exhausted each labeled block-permutation sample space, and compared every half-path mean and covariance with (9). The tested `(Q,b,K,r)` cases were `(4,1,3,0)`, `(5,2,2,1)`, `(6,2,3,0)`, `(8,2,5,1)`, `(9,3,4,2)`, `(11,4,5,1)` and `(12,4,5,3)`: 398 permutations in total. All rational identities passed. The respective exact mean full energies were
\[
1/54,\quad17/900,\quad2/135,\quad14461/554400,
\quad883/45360,\quad15473/762300,\quad17334281/883658160.
\]
An independently applied full-grid sine transform verified Parseval and the means and second moments from (9)–(11), with maximum absolute floating-point discrepancy below `1.3e-16`. These checks test constants, nonzero remainder handling and finite calibration; the limit is established by the preceding proof.

An additional exact-rational audit generated every genuine Farey grid at `3<=Q<=80`. It checked 1,117,828 consecutive pairs in all denominator-cutoff subsequences against the rank separation used in (13a); 407,949 windows at all available starting ranks for the selected lengths `1,2,3,5,8,13,floor(Q/log(2Q)),floor(m/3)` against the rational harmonic-sum relaxation of (13b); 561 block partitions against (13c) and the squared-tail-mass bound; and 218 truncated denominator triangles against the exact first equality and lower bound in (13d). All exact assertions passed. These are finite normalization and combinatorial checks; the logarithmic reservoir and weak limits follow from the proof, not finite extrapolation.

An independent exact-rational check of (13b-D) enumerated the Farey sets directly by reduced fractions for `3<=Q<=60` and `Q=80,120,200`. It checked all `1<=b<=min(Q,floor(m/2))` at the first 58 orders and the distinct choices `1,2,3,floor(Q/2),Q,floor(Q/sqrt(log(2Q))),floor(Q/log(2Q))` at the last three, subject to `K>=2`. All 41,633 point-discrepancy checks, 1,825 partition checks, and 633,910 within-block prefix identities/bounds passed. For 276 partitions with a nonempty denominator cutoff satisfying `1/(RQ)>=2 lambda`, the exact truncated-triangle equality, retained large-gap lower bound, and squared-tail-loss inequality also passed. Exhausting all block permutations with `K<=5` and `Q<=20` in this panel gave 2,932 checks of `max|H-Y|<=3/Q`, including the sharper anchored-tail bound. These finite checks cover centering and endpoint conventions, including block lengths beyond `Q/log(2Q)`; they do not prove a weak limit or infer its validity at `b=Theta(Q)`.

Block permutation principles and Brownian limits are classical. Claudia Kirch, *Block permutation principles for the change analysis of dependent data*, Journal of Statistical Planning and Inference **137** (2007), 2453–2474, [DOI 10.1016/j.jspi.2006.09.026](https://doi.org/10.1016/j.jspi.2006.09.026), studies block-resampling statistics and deterministic-score conditions in Theorem 2.1 before applying them to dependent data. No novelty is claimed for that method. The probability input actually used here is the vanishing-maximum/squared-mass criterion in [Bertoin, Lemma 2.1(i)](https://arxiv.org/abs/2005.11986), a specialization of Kallenberg (1973), Theorem 2.3, already cited in FD-335 and SOURCES.md. We verify the deterministic Farey conditions directly and assume no stationary time-series or mixing model.

The closest spacing-moment comparison is Anji Dong, Huy Xuan Nguyen, Vi Anh Nguyen and Alexandru Zaharescu, *Effective Estimates for a Class of Farey Fraction Sums and Bounds for Mundici-Type Constants*, [arXiv:2606.12907v1](https://arxiv.org/html/2606.12907v1), Theorems 1.1, 1.2 and 2.1. It treats sums of squares of all overlapping `h`-spacings, including a fixed-`h` leading term and explicit `h`-dependent thresholds. That is distinct from the centered variance of one disjoint block partition with an anchored remainder. No such fixed-`h` estimate is extrapolated to growing `b` here: (13a)–(13e) directly establish the needed uniform bounds. The mediant insertion, denominator triangle and totient harmonic sum are elementary classical ingredients; no novelty is claimed for them individually.

The input for (13b-D) is François Dress, *Discrépance des suites de Farey*, JTNB **11**(2) (1999), 345–367, [primary paper](https://jtnb.centre-mersenne.org/article/JTNB_1999__11_2_345_0.pdf). Its sample-point consequence is also used in FD-337. Subtracting two sample discrepancies is elementary; it removes the logarithmic loss in (13b), rather than providing a new discrepancy theorem.

Hall's Farey gap work and [García's same-gap average-local-discrepancy paper](https://doi.org/10.3390/math14142543) remain the arithmetic and permutation prior-art boundaries recorded in SOURCES.md. FD-313 already gives worst-case noncoercivity for **exact complete** local-window inventories on different rational controls; it does not supply a probability law for this genuine-Farey block population. The line-local addition is the verified range `b=o(Q)`, its exact finite calibration with a pinned remainder, and the conclusion that every prescribed sublinear window depth admits density-one retention with the Brownian normalized spectral null. The proof combines the classical absolute-discrepancy bound with the truncated large-gap reservoir; neither input alone gives the normalized limit. This is a literature-backed specialization, not a new general invariance principle or a priority claim.

Condition (4) is sufficient, not proved sharp. The controlling inputs are the vanishing normalized block maximum and internal motion in (14), not block length alone. For `b=Theta(Q)`, Dress still bounds centered internal motion by `2/Q`, but `R=floor(Q/(32b))` no longer diverges and the variance argument does not force `Q^2 V_b->infinity`. Thus this proof stops at the linear block scale; it does not establish Brownian failure there. Matching every overlapping adjacent pair, conditioning denominator seams, or using a different partition/sample distribution requires a fresh analysis. Neither density-one retention nor the Brownian law turns these reassembled grids into genuine Farey sequences. The theorem concerns the null's `S_q`; it makes no assertion about the original Farey `S_q` or its asymptotic suppression. Finite-order distributional error rates and the clue's larger-order comparison panel remain outside this result.
