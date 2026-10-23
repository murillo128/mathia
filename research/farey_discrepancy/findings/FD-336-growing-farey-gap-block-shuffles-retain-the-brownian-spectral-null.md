# FD-336 — Growing Farey gap-block shuffles retain the Brownian spectral null

**Status:** LITERATURE+DERIVED + EXACT-FINITE-CALIBRATION + UNCONDITIONAL-WEAK-LIMIT + LOCAL-ORDER-BOUNDARY.

The reflection/same-gap null in FD-335 forgets all local order. A strictly more constrained null preserves the internal order of consecutive blocks of genuine Farey gaps. For block length `b=o(sqrt(log Q))`, this null still has the same normalized Brownian energy and growing-band allocation laws. In particular, choosing `b -> infinity` preserves a proportion tending to one of the original adjacent gap pairs without changing those limiting laws. Its finite mean energies must nevertheless be recalculated: the single-gap Green formula is generally false for this ensemble.

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
1\le b=b(Q)=o(\sqrt{\log Q}),
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

For fixed `b>1` the preserved fraction of within-block adjacencies is positive. For `b->infinity` satisfying (4), all but `O(1/b)` of the original **labeled adjacent occurrences** survive, yet (6)–(7) remain valid. More generally, for `h=o(b)`, all but `O(h/b)` of the original labeled length-`h` windows lie inside the retained blocks or remainder. This is density-one preservation of occurrences, not equality of the complete window-count matrix: seam-crossing windows can change.

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

## 3. Farey positivity prevents collapse of the block variance

FD-335 derives directly from the coprime Farey denominator triangle that
\[
V_1:=\sum_{i=1}^m a_i^2
\sim\frac6{\pi^2}\frac{\log Q}{Q^2},\qquad
\max_i g_i=1/Q,\qquad N\sim3Q^2/\pi^2.
\tag{12}
\]
These are unconditional arithmetic inputs, not assumptions about random independent gaps.

Write `G_j=sum_(t=1)^b g_((j-1)b+t)` and `T=sum_j G_j<=1/2`. Centering by the block average gives
\[
V_b=\sum_j G_j^2-T^2/K.
\]
Since every gap is positive, `G_j^2>=sum_(i in block j)g_i^2`. Removing fewer than `b` gaps costs at most `b/Q^2`; also `T^2/K<=1/(4K)=O(b/Q^2)`. Therefore
\[
\boxed{V_1-O(b/Q^2)\le V_b\le bV_1.}
\tag{13}
\]
For the upper bound, subtracting the mean reduces squared mass and Cauchy–Schwarz gives `sum_j s_j^2<=b sum_(i<=Kb)a_i^2<=bV_1`.

Under (4), (12)–(13) imply `V_b >> log(Q)/Q^2` and
\[
\frac{\max_j|c_j|}{\sqrt{V_b}}
+\frac{|S|+\max_{j,t}|\sum_{i=1}^t a_{(j-1)b+i}|}{\sqrt{V_b}}
=O\!\left(\frac b{\sqrt{\log Q}}\right)=o(1).
\tag{14}
\]
Here `|a_i|<=1/Q+1/N`, and the same bound controls partial sums within the remainder. This verifies both the vanishing-jump condition for block totals and the negligibility of internal block motion. It also excludes a degenerate ensemble of identical block totals asymptotically.

Combining (6), (12) and (13) gives the useful mean boundary
\[
(1-o(1))\frac3{\pi^4}\log Q
\le\mathbb E E
\le(1+o(1))\frac3{\pi^4}b\log Q.
\tag{15}
\]
Preserving these blocks cannot suppress the null's total mean below the single-gap logarithmic scale. Its exact leading amplitude is encoded by `V_b`; no universal formula for `V_b/V_1` is asserted.

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
Consequently `max|H-Y|<=C b/Q` deterministically, including the tail. Moreover `Kb/m->1` and the largest coarse jump divided by `sqrt(V_b)` tends to zero. These facts prove (5) and convergence of the total-energy and each fixed sine-coefficient functional.

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
The normalized Euclidean distance between the full reflected `H` and `Y` paths is at most `C b/(Q sqrt(V_b))=o(1)`. Cauchy–Schwarz and (17) then show that their normalized expected energies differ by `o(1)`. The same bound applies to every fixed orthogonal sine projection. Equation (16), by Riemann summation, gives its limiting covariance. Thus for fixed `J`, jointly,
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

Block permutation principles and Brownian limits are classical. Claudia Kirch, *Block permutation principles for the change analysis of dependent data*, Journal of Statistical Planning and Inference **137** (2007), 2453–2474, [DOI 10.1016/j.jspi.2006.09.026](https://doi.org/10.1016/j.jspi.2006.09.026), studies block-resampling statistics and deterministic-score conditions in Theorem 2.1 before applying them to dependent data. No novelty is claimed for that method. The probability input actually used here is the vanishing-maximum/squared-mass criterion in [Bertoin, Lemma 2.1(i)](https://arxiv.org/abs/2005.11986), a specialization of Kallenberg (1973), Theorem 2.3, already cited in FD-335 and SOURCES.md. We verify the deterministic Farey conditions directly and assume no stationary time-series or mixing model.

Hall's Farey gap work and [García's same-gap average-local-discrepancy paper](https://doi.org/10.3390/math14142543) remain the arithmetic and permutation prior-art boundaries recorded in SOURCES.md. FD-313 already gives worst-case noncoercivity for **exact complete** local-window inventories on different rational controls; it does not supply a probability law for this genuine-Farey block population. The line-local addition is the verified growing-block regime, its exact finite calibration with a pinned remainder, and the conclusion that density-one retained gap order still gives the Brownian normalized spectral null. This is a literature-backed specialization, not a new general invariance principle or a priority claim.

Condition (4) is sufficient, not proved sharp. Larger blocks may require better block-sum or internal-oscillation bounds. Matching every overlapping adjacent pair, conditioning denominator seams, or using a different partition/sample distribution requires a fresh analysis. Neither density-one retention nor the Brownian law turns these reassembled grids into genuine Farey sequences. The theorem concerns the null's `S_q`; it makes no assertion about the original Farey `S_q` or its asymptotic suppression. Finite-order distributional error rates and the clue's larger-order comparison panel remain outside this result.
