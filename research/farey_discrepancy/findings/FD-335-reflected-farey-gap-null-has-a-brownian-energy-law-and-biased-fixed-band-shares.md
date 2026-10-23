# FD-335 — Reflected Farey gap permutations have a Brownian energy law and biased fixed-band shares

**Status:** LITERATURE+DERIVED + EXACT-FINITE-COVARIANCE + UNCONDITIONAL-WEAK-LIMIT + NULL-CALIBRATION-BOUNDARY.

The accepted gap-ordering clue separates total amplitude from spectral allocation and asks for distributional calibration of the reflection-preserving same-gap null. Its exact mean energies do not establish concentration or give the allocation ratio mean one. Here that null has an unconditional joint limiting law: normalized total energy remains nondegenerate, every fixed low-band allocation ratio has limiting mean **strictly below one**, and every diverging band captures essentially all of a typical null path's energy. This calibrates the existing weak null; it does not estimate the genuine Farey discrepancy or any stronger denominator/adjacency-conditioned null.

## 1. Ensemble, observables, and theorem

Let the order-\(Q\) Farey grid include both endpoints,
\[
0=x_0<x_1<\cdots<x_N=1,\qquad N=\sum_{d\le Q}\varphi(d)=2m,
\]
with \(Q\ge3\). Write \(g_i=x_i-x_{i-1}\). Reflection gives \(g_i=g_{N+1-i}\) and \(\sum_{i\le m}g_i=1/2\). Choose a uniform permutation \(\pi\) of the **labeled first-half gaps**, and concatenate
\[
(g_{\pi(1)},\ldots,g_{\pi(m)},g_{\pi(m)},\ldots,g_{\pi(1)}).
\tag{1}
\]
Equal gap values cause no weighting ambiguity: each distinct half-word has the same number of labeled preimages. This samples the reflection-symmetric full gap multiset, preserving endpoints and positivity. It does not preserve adjacent-pair counts, denominator edges, or Farey stitch integrality.

Set
\[
a_i=g_i-1/N\quad(1\le i\le m),\qquad
V_Q=\sum_{i=1}^m a_i^2>0.
\]
For the reconstructed grid let \(D_k=x_k^\pi-k/N\), and define
\[
E=\sum_{k=1}^{N-1}D_k^2,\qquad
d_s=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(\pi sk/N),
\qquad E_q=\sum_{r=1}^q d_{2r}^2.
\]
Here \(1\le q\le m-1\). All expectations below are over (1), with \(Q\) fixed. Put
\[
A_Q=\frac{E}{\mathbb E E},\qquad
f_{q,Q}=\frac{\mathbb E E_q}{\mathbb E E},\qquad
S_{q,Q}=\frac{E_q/E}{f_{q,Q}},\qquad
Q_{q,Q}=\frac{E_q}{\mathbb E E_q}=A_QS_{q,Q}.
\tag{2}
\]
The symbol \(Q_{q,Q}\) is the combined statistic, not the Farey order.

Let \(Z_1,Z_2,\ldots\) be independent standard normal variables and define
\[
\lambda_r=\frac1{\pi^2r^2},\qquad
W_q=\sum_{r\le q}\lambda_r Z_r^2,\quad
W=\sum_{r\ge1}\lambda_r Z_r^2,\quad
L_q=\sum_{r\le q}\lambda_r,\quad L=\frac16.
\tag{3}
\]
As \(Q\to\infty\), unconditionally:

* \(E/(NV_Q)\Rightarrow W\), so \(A_Q\Rightarrow6W\). The limiting law has mean one and variance \(4/5\); **\(A_Q\) does not concentrate at one**.
* For every fixed \(q\), jointly,
\[
\boxed{(A_Q,S_{q,Q},Q_{q,Q})
\Rightarrow
\left(6W,\frac{W_q/W}{6L_q},\frac{W_q}{L_q}\right).}
\tag{4}
\]
The three coordinates use the same Gaussian sequence. In particular,
\[
\boxed{\lim_{Q\to\infty}\mathbb E S_{q,Q}<1
\quad\text{for every fixed finite }q.}
\tag{5}
\]

* For any deterministic \(q=q(Q)\to\infty\) with \(q\le m-1\),
\[
\boxed{S_{q,Q}\longrightarrow1\text{ in probability},\qquad
(A_Q,Q_{q,Q})\Rightarrow(6W,6W).}
\tag{6}
\]
Thus both predeclared clue bands \(q=\lfloor\sqrt Q\rfloor\) and \(q=\lfloor Q^{2/3}\rfloor\) satisfy (6). This does not say how quickly their finite-order distributions settle.

The arithmetic normalization is
\[
V_Q\sim\frac6{\pi^2}\frac{\log Q}{Q^2},\qquad
\mathbb E E=\frac{m+1}{3}V_Q\sim\frac3{\pi^4}\log Q.
\tag{7}
\]
The logarithmic mean is accompanied by order-one relative fluctuations, rather than a law of large numbers.

## 2. Exact finite covariance and sine normalization

Write \(H_k=\sum_{i\le k}a_{\pi(i)}\), \(0\le k\le m\). Then
\[
D_k=H_k\ (k\le m),\qquad D_{N-k}=-H_k,
\qquad H_0=H_m=0.
\tag{8}
\]
Sampling without replacement gives, for \(1\le i,j<m\),
\[
\mathbb E H_iH_j=
\frac{V_Q}{m-1}\left(\min(i,j)-\frac{ij}{m}\right).
\tag{9}
\]
Indeed each sampled increment has variance \(V_Q/m\), while two distinct sampled increments have covariance \(-V_Q/[m(m-1)]\). Summing those terms proves (9).

The matrix in parentheses is the inverse of the Dirichlet tridiagonal Laplacian with diagonal 2 and off-diagonal \(-1\). Its normalized sine eigenvectors have eigenvalues \([4\sin^2(\pi r/(2m))]^{-1}\). Reflection in (8) annihilates every odd full-grid sine coefficient and gives
\[
d_{2r}=\frac2{\sqrt m}\sum_{k=1}^{m-1}H_k\sin(\pi rk/m).
\]
Consequently
\[
\boxed{\mathbb E d_{2r}d_{2s}
=\mathbf1_{r=s}\frac{V_Q}{2(m-1)\sin^2(\pi r/(2m))},}
\tag{10}
\]
and
\[
\mathbb E E=\frac{m+1}{3}V_Q,\qquad
f_{q,Q}=\frac{3}{2(m^2-1)}
\sum_{r=1}^q\csc^2(\pi r/(2m)).
\tag{11}
\]
These finite mean identities are already conveyed by the local clue; they are rederived here to fix the normalization, not claimed as a new result. Finite uncorrelated modes are not asserted independent.

## 3. Why the actual Farey gap population satisfies the bridge limit

The classical Farey-neighbor characterization enumerates every gap once by
\(1\le a,b\le Q\), \(a+b>Q\), \((a,b)=1\), with gap \(1/(ab)\). It gives the largest gap \(1/Q\) and
\[
\sum_{i=1}^N g_i^2
=\sum_{\substack{a,b\le Q\\a+b>Q\\(a,b)=1}}\frac1{a^2b^2}
=\frac{12}{\pi^2}\frac{\log Q}{Q^2}+O(Q^{-2}).
\tag{12}
\]
For completeness, split the triangle into \(a\le Q/2\), its transpose, and the region where both variables exceed \(Q/2\). The last region contributes \(O(Q^{-2})\). For fixed \(a\le Q/2\), the integers \(Q-a<b\le Q\) contain exactly \(\varphi(a)\) coprime residues, and replacing \(b^{-2}\) by \(Q^{-2}\) costs \(O(a\varphi(a)/Q^3)\). After multiplication by \(a^{-2}\) and summation the cost is \(O(Q^{-2})\). Finally,
\(\sum_{a\le Q/2}\varphi(a)/a^2=(6/\pi^2)\log Q+O(1)\), by \(\varphi(a)/a=\sum_{d\mid a}\mu(d)/d\). This proves (12) with its leading constant.

Since \(2V_Q=\sum_i g_i^2-1/N\), (12) and \(N\sim3Q^2/\pi^2\) prove (7), and
\[
\max_{i\le m}\frac{|a_i|}{\sqrt{V_Q}}
=O((\log Q)^{-1/2})\longrightarrow0.
\tag{13}
\]

The classical exchangeable-increment convergence criterion applies to deterministic arrays \(b_i=a_i/\sqrt{V_Q}\): \(\sum b_i=0\), \(\sum b_i^2=1\), and \(\max|b_i|\to0\). Hence the linearly interpolated partial-sum process
\[
X_Q(k/m)=\frac{H_k}{\sqrt{V_Q}}\quad(0\le k\le m),
\quad\text{interpolated between grid points},
\qquad X_Q\Rightarrow B
\tag{14}
\]
in the uniform topology, where \(B\) is a standard Brownian bridge. This is a literature theorem, not a new invariance principle: see Kallenberg (1973), Theorem 2.3, in the specialization stated as Bertoin (2020), Lemma 2.1(i).

To make the passage from that specialization to random permutations explicit, assign independent uniform times \(U_i\) to the deterministic \(b_i\). The bridge \(\sum_i b_i(\mathbf1_{U_i\le t}-t)\) satisfies the cited criterion. The linear term vanishes. Ordering the \(U_i\) gives a uniform permutation of the \(b_i\); the order-statistic time change converges uniformly to the identity. The continuous limit and vanishing maximum jump (13) permit this time change and interpolation, yielding (14).

Uniform convergence to a continuous limit makes squared-integral and fixed sine-coefficient functionals continuous. Their grid sums have the same limits because the interpolated step size tends to zero. Equations (8) and (14) therefore give, jointly for any fixed collection of modes,
\[
\frac{E}{NV_Q}\Rightarrow\int_0^1B(t)^2\,dt,
\qquad
\frac{d_{2r}}{\sqrt{NV_Q}}
\Rightarrow\sqrt2\int_0^1B(t)\sin(\pi rt)\,dt.
\tag{15}
\]
The bridge covariance kernel \(\min(s,t)-st\) is the Green kernel of \(-d^2/dt^2\) with zero endpoint values. Its orthonormal sine eigenvalues are \(\lambda_r\). Gaussianity makes the coefficients in (15) independent centered normals of variances \(\lambda_r\); Parseval gives (3). In particular \(\mathbb EW=1/6\), \(\operatorname{Var}(W)=2\sum_r\lambda_r^2=1/45\), and \(W>0\) almost surely. Equations (11) and (15) prove (4) and nonconcentration.

## 4. Fixed-band bias and growing-band saturation

Put \(P(t)=\mathbb E e^{-tW}=\prod_{r\ge1}(1+2t\lambda_r)^{-1/2}\). By Tonelli's theorem and \(W^{-1}=\int_0^\infty e^{-tW}\,dt\),
\[
h_r:=\frac{\mathbb E(\lambda_r Z_r^2/W)}{\lambda_r}
=\int_0^\infty\frac{P(t)}{1+2t\lambda_r}\,dt.
\tag{16}
\]
Every integral is finite (any sufficiently long finite subproduct bounds its tail). Since \(\lambda_r\) strictly decreases, \(h_r\) strictly increases with \(r\). Also \(\sum_r\lambda_rh_r=1\). The weighted average of \(h_r\) over any finite initial segment is strictly smaller than the weighted average over all indices, namely \(1/L=6\). Thus
\[
\mathbb E\frac{W_q/W}{6L_q}
=\frac{\sum_{r\le q}\lambda_rh_r}{6L_q}<1.
\tag{17}
\]
Because \(0\le S_{q,Q}\le1/f_{q,Q}\) and \(f_{q,Q}\to6L_q>0\), convergence in (4) also gives convergence of expectations, proving (5). This strict bias is a consequence of normalizing each realization by its own total energy; it is compatible with \(\mathbb E A_Q=\mathbb E Q_{q,Q}=1\) exactly.

For growing bands, \(\sin(\pi r/(2m))\ge r/m\) in (10) gives the uniform bound
\[
\frac{\mathbb E(E-E_q)}{NV_Q}
\le\frac{m}{4(m-1)}\sum_{r>q}^{m-1}\frac1{r^2}
=O(q^{-1}).
\tag{18}
\]
Markov's inequality and \(E/(NV_Q)\Rightarrow W>0\) imply \((E-E_q)/E\to0\) in probability whenever \(q\to\infty\). Equation (18) also implies \(f_{q,Q}\to1\), so (6) follows. No interchange of a fixed-mode limit with an uncontrolled growing sum is used.

## 5. Audit checks, prior art, and evidence boundary

An exact rational enumerator formed the genuine Farey grids at \(Q=4,5,6\), then exhausted all \(3!,5!,6!\) labeled half-gap permutations. It checked reflection, every covariance entry (9), and the mean energies \(1/54,1/36,7/270\), respectively, against (11). Independent full-grid sine transforms checked odd-mode annihilation, Parseval, and all mode variances (10), with maximum floating-point error below \(2\cdot10^{-17}\). These checks validate finite constants and endpoint conventions, not the limit theorem.

For an illustrative evaluation of (17), the product formula is
\[
P(t)=\left(\frac{\sqrt{2t}}{\sinh\sqrt{2t}}\right)^{1/2}.
\]
Ordinary numerical quadrature after \(y=\sqrt{2t}\) gives limiting means of \(S_{q,Q}\) approximately \(0.72251,0.81222,0.86022\) for \(q=1,2,3\). Halving the integration mesh on \([0,100]\) changed the answers by less than \(7\cdot10^{-13}\); these are numerical illustrations, not certified enclosures. The strict inequalities come from (16)--(17).

The load-bearing probability theorem is classical: Olav Kallenberg, *Canonical representations and convergence criteria for processes with interchangeable increments*, Z. Wahrscheinlichkeitstheorie verw. Gebiete **27** (1973), 23–36, [DOI 10.1007/BF00736005](https://doi.org/10.1007/BF00736005); the precise vanishing-maximum/squared-mass specialization is available in Jean Bertoin, *How linear reinforcement affects Donsker's theorem for empirical processes*, Probability Theory and Related Fields **178** (2020), 1173–1192, [Lemma 2.1(i)](https://link.springer.com/article/10.1007/s00440-020-01001-9). No reinforcement model is used here. Brownian bridge Green eigenfunctions and Gaussian quadratic-energy laws are classical as well.

R. R. Hall's [*A Note on Farey Series*, J. London Math. Soc. **s2-2** (1970), 139–148](https://doi.org/10.1112/jlms/s2-2.1.139) and García's [2026 same-gap permutation paper](https://doi.org/10.3390/math14142543) are the arithmetic/prior-art boundary. The latter concerns average absolute discrepancy; this finding concerns reflected quadratic energy and joint spectral ratios. The classical covariance/mean laws already stated in the local clue are not additional contributions. The line-local delta is the verified applicability of the classical process limit to the actual Farey gap population, its joint amplitude/allocation calibration, strict fixed-band mean bias, and typical-path saturation for the clue's diverging bands. No general novelty claim is made for permutation bridges or Gaussian energy ratios.

This closes a calibration subquestion only. It does not resolve the accepted gap-ordering clue, justify transferring this law to an adjacent-pair or denominator-conditioned ensemble, supply a finite-order error rate, or show that the genuine Farey \(S_{q,Q}\) tends to any limit. In particular (6) is a theorem about the randomly reordered control, not the original arithmetic order. It gives neither a new Franel–Landau estimate nor a bound on off-critical zeta zeros.
