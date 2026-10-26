# PL-478 — Geometric coverage retains the paired prime criterion on sparse samples

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL TRANSFER;
CLASSICAL LIPSCHITZ RECOVERY; NON-EFFECTIVE ZERO-DEPENDENT CONSTANTS;
NO EXTERNAL NOVELTY CLAIM. No arithmetic sample-energy ceiling is proved.

## Claim and observation boundary

For a positive integer \(X\), write
\[
I_X=\{X,\ldots,2X-1\},\qquad
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
S_L(j)=\sum_{j<n\le j+L}a_n.
\]
Let \(1\le H\le X/20\) be an integer and put
\(L_1=H\), \(L_2=K=\lfloor\sqrt2H\rfloor\).
For each channel independently choose a nonempty retained set
\(R_i\subset I_X\) and a constant \(c_i\in\mathbb C\).
Assign each start \(j\) to a nearest retained point \(\pi_i(j)\),
breaking ties toward the smaller point, and define
\[
w_{i,r}=|\pi_i^{-1}(r)|,\qquad
D_i=\sum_{j\in I_X}|j-\pi_i(j)|,\qquad
W_i(c_i)=\sum_{r\in R_i}w_{i,r}|S_{L_i}(r)-c_i|^2.
\tag{1}
\]
If zeta or any of the three primitive nonprincipal Dirichlet functions
modulo 5 has a nontrivial zero \(\rho_0=\beta+i\gamma\),
\(\beta>1/2\), there are \(C>0,X_0\), depending on that zero and
the full zero set, such that
\[
\boxed{\sum_{i=1}^2
\frac{\sqrt{XW_i(c_i)}+\log(3X)D_i}{L_i}\ge C X^\beta.}
\tag{2}
\]
This holds for every integer \(X\ge X_0\), uniformly in the stated
lengths, nonempty retained sets and constant centers. No positive
retained fraction is required.

In particular set
\[
H_X=\lfloor X/20\rfloor,\quad K_X=\lfloor\sqrt2H_X\rfloor,
\quad g_X=\lfloor\sqrt X\rfloor,
\]
\[
R_X=\{X+kg_X:0\le k\le\lfloor(X-1)/g_X\rfloor\},
\quad q_X=|R_X|,\quad
Q_i(X)=\min_{c\in\mathbb C}\sum_{r\in R_X}|S_{L_i}(r)-c|^2.
\tag{3}
\]
Here \((L_1,L_2)=(H_X,K_X)\) and \(q_X\asymp\sqrt X\).
The following is **equivalent to joint GRH for these four functions**:
there exists one unbounded set \(\mathcal X\) of integer scales,
fixed before epsilon varies, such that for every \(\varepsilon>0\),
both channels satisfy
\[
\boxed{Q_i(X)/q_X\ll_\varepsilon X^{1+\varepsilon}
\quad(X\in\mathcal X\text{ sufficiently large}),\quad i=1,2.}
\tag{4}
\]
The grid is fixed independently of the source and epsilon. Each channel
uses its own ordinary sample mean. The two ceilings must hold on the
same unbounded scale set.

The change from
[[research/prime_lattice/findings/PL-476-trimmed-paired-prime-variance-retains-the-grh-obstruction|PL-476]]
is geometric coverage instead of a small deletion count. The finite
lemma and grid bookkeeping were suggested by
[[research/mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance|MC-533]],
Sections 1, 3 and 4, read under the local Master clue's bounded grant.
They are reconstructed below. The prime jump bound, noncancelling
logarithmic-derivative formula and GRH converse are destination inputs;
no reciprocal-zeta theorem or Möbius pointwise estimate is imported.

## 1. Recover complete absolute mass with the actual sampling weights

Let \(u_j\in\mathbb C\) be indexed by \(N\) consecutive integers,
with \(|u_{j+1}-u_j|\le J\), and retain any nonempty set \(R\).
For its nearest assignment, weights \(w_r\), and distance sum \(D\),
telescoping and weighted Cauchy–Schwarz give
\[
\begin{aligned}
\sum_j|u_j|
&\le\sum_j\bigl(|u_{\pi(j)}|+J|j-\pi(j)|\bigr)\\
&=\sum_{r\in R}w_r|u_r|+JD
\le\sqrt{N\sum_{r\in R}w_r|u_r|^2}+JD.
\end{aligned}
\tag{5}
\]
The proof needs only \(\sum_r w_r=N\), not majority retention.
Any assignment works; nearest assignment minimizes the distance term,
not necessarily the whole right side, since its weights also enter
the energy. An unweighted energy on an irregular set must pay its
largest cell size:
\[
\sum_r w_r|u_r|^2\le w_{\max}\sum_r|u_r|^2.
\tag{6}
\]

For the prime source,
\[
S_L(j+1)-S_L(j)=a_{j+L+1}-a_{j+1},\qquad
|S_L(j+1)-S_L(j)|\le\log(3X).
\tag{7}
\]
All relevant indices are below \(3X\), and both coefficients are in
\([0,\log(3X)]\); positivity avoids a factor two. Subtraction of a
constant preserves this jump bound. Consequently
\[
\sum_{j\in I_X}|S_{L_i}(j)-c_i|
\le\sqrt{XW_i(c_i)}+\log(3X)D_i.
\tag{8}
\]

## 2. Preserve the complete arithmetic tests

The analytic inputs are
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]],
Sections 1–3, and
[[research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance|PL-475]],
Sections 1–4, as assembled for integer starts in PL-476, Section 2.
For any fixed \(1/2<\sigma_0<\beta\), they give a fixed
\(\varphi\in C_c^\infty((4/3,5/3);\mathbb C)\), \(\int\varphi=0\),
with
\[
T_\varphi(X):=\sum_n a_n\varphi(n/X)
=-w_{\rho_0}X^{\rho_0}+O_\varphi(X^{\sigma_0}),\qquad
w_{\rho_0}=\tfrac14\sum_\chi m_\chi(\rho_0)>0.
\tag{9}
\]
The sum runs over the four functions. Sparse-zero interpolation removes
every other zero to the right of \(\sigma_0\); the actual explicit
formula controls the remaining full zero sum. Coincident zeros add
positive multiplicities, and a multiple zero still gives a simple
logarithmic-derivative pole. There is no reciprocal-pole logarithmic
factor in (9).

For \(h=H/X\), the compact two-box deconvolvers give mean-zero smooth
tests \(f_{1,h},f_{2,h}\), supported in a fixed compact subset of
\((1,2)\), with uniformly bounded sup and first derivative norms for
\(0<h\le1/20\). With
\(A_af(u)=\int_0^1f(u-at)\,dt\), they satisfy
\[
A_hf_{1,h}+A_{\sqrt2h}f_{2,h}=\varphi,\qquad
\|A_hf_{1,h}+A_{K/X}f_{2,h}-\varphi\|_\infty
\ll_\varphi X^{-1}.
\tag{10}
\]
The second assertion retains the rounding error; it is not an exact
inverse of the rounded rational pair. Its pairing with \(O(X)\)
coefficients bounded by \(\log(3X)\) costs \(O_\varphi(\log(3X))\).

Define the **complete**, unmasked pairings
\[
\mathcal L_i=\frac1{L_i}\int_X^{2X}
 (S_{L_i}(y)-c_i)f_{i,h}(y/X)\,dy.
\]
Each constant center cancels exactly. Interchanging a finite sum with
the integral of the zero-extended test gives
\[
\mathcal L_i=\sum_n a_n(A_{L_i/X}f_{i,h})(n/X),\qquad
|\mathcal L_1+\mathcal L_2|\ge\tfrac12w_{\rho_0}X^\beta
\tag{11}
\]
for every sufficiently large \(X\), uniformly in \(H\).
The integration at coefficient \(n\) is over \([n-L_i,n]\);
windows crossing a block endpoint are included.
For integer \(L_i\), \(S_{L_i}(y)=S_{L_i}(j)\) on
\([j,j+1)\). Equations (8) and the uniform test bounds therefore give
\[
|\mathcal L_i|\ll_\varphi
\frac{\sqrt{XW_i(c_i)}+\log(3X)D_i}{L_i}.
\tag{12}
\]
Combining (11) and (12) proves (2). At no point is a retained-set
indicator inserted into the smooth Mellin test.

## 3. A vanishing retained fraction and the independent converse

For the grid (3), every start is within \(g_X\) of a sample. Each
nearest-sample cell has at most \(2g_X\) starts, including the endpoint
cells; the uncovered final segment has length less than \(g_X\).
Also \(g_Xq_X\le X+g_X\le2X\). Hence
\[
D_i\le Xg_X\le X^{3/2},\qquad
W_i(c_i)\le2g_XQ_i(X)\ll_\varepsilon X^{2+\varepsilon}
\tag{13}
\]
under (4), using the ordinary sample mean as the same \(c_i\) in
both the weighted and unweighted expressions. It need not minimize
the weighted energy.

Both window lengths are comparable to \(X\). The left side of (2)
is therefore
\[
O_\varepsilon\bigl(X^{1/2+\varepsilon/2}
                      +X^{1/2}\log(3X)\bigr).
\tag{14}
\]
For a zero with \(\beta>1/2\), choose
\(0<\varepsilon<2\beta-1\). This is \(o(X^\beta)\), contradicting
(2) along the single unbounded set \(\mathcal X\). No density or
spacing condition on that scale set is needed. Functional-equation
symmetry within the full four-function family gives joint GRH.

Conversely, joint GRH for these functions implies the classical
fixed-modulus estimate
\[
\psi(x;5,1)=x/4+O(\sqrt{x}\log^2(3x)).
\tag{15}
\]
Apply the character-wise GRH explicit-formula bound and character
orthogonality; the principal character's omitted powers of 5 contribute
only \(O(\log x)\). See [Lee (2023), Corollary 1.1 and the
character-wise proof](https://arxiv.org/pdf/2301.13457), source 144.
For every retained \(r\) and either length, both endpoints are
comparable to \(X\). Taking \(c=L_i/4\) gives
\[
Q_i(X)/q_X
\le\max_{r\in R_X}|S_{L_i}(r)-L_i/4|^2
\ll X\log^4(3X)\ll_\varepsilon X^{1+\varepsilon}.
\tag{16}
\]
Thus (4) holds on all sufficiently large integer scales, for the same
fixed grid and scale family for every epsilon. This pointwise argument
does not assume that a small complete mean square controls a sparse
deterministic sample. That implication is false for general data.

## 4. Geometry, controls and limits of the conclusion

For ordered samples \(r_1<\cdots<r_q\) in \(\{1,\ldots,N\}\),
put \(a=r_1-1\), \(b=N-r_q\). The exact distance bill is
\[
D=\frac{a(a+1)}2+\frac{b(b+1)}2+
  \sum_{k=1}^{q-1}\left\lfloor\frac{(r_{k+1}-r_k)^2}{4}\right\rfloor.
\tag{17}
\]
The interior formula sums \(\min(j,d-j)\) over a gap of length \(d\).
Each cell of size \(w\) has distance sum at least
\(\lfloor w^2/4\rfloor\), attained by a middle sample. Thus
\[
D\ge\tfrac14\bigl(\sum_r w_r^2-q\bigr)
 \ge\tfrac14(N^2/q-q).
\tag{18}
\]
The sequence \(u_j=J\operatorname{dist}(j,R)\) has jumps at most
\(J\), zero sample values and absolute mass exactly \(JD\).
This explains the worst-case geometric price for the elementary
absolute-mass method. It is not a prime-source example or necessarily
a compatible pair of sliding-window sequences. Neither (18) nor this
envelope proves optimality for signed tests, prime arithmetic, the
logarithmic factor, or an exact minimal sample count.

The common-mask construction in
[[research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity|PL-477]]
is consistent with (2): its three separated omitted blocks have
\(D\asymp B^2\) by (17), and its hidden signed response is
\(\asymp B^2/X\). The grid here instead has \(D=O(X^{3/2})\)
even though \(X-q_X\sim X\) starts are omitted. Retained fraction
alone does not measure either configuration's recovery cost.

Other boundaries remain essential. Empty retained sets are excluded;
a singleton is allowed but generally pays a large distance bill.
At \(H=K=1\) the measurements can coincide and the rounding estimate
(10) still applies; no division by \(K-H\) occurs. Different masks
and centers are allowed, but start-dependent fitted centers would
change both (7) and the mean-zero argument. One favorable channel or
disjoint scale families cannot replace (4).

The finite recovery is universal. Rational primes enter through (9)
and (15), which phase twists, generalized primes and arbitrary positive
residue-supported sources do not inherit. The target and onset remain
non-effective and depend on the full hypothetical zero set. There is
no uniformity as \(\beta\downarrow1/2\), no critical-line lower bound,
no simplicity assertion, no relative covariance positivity, and no
unconditional route to the ceiling (4).

## Prior art and validation

[[research/prior_art/incremental/PA-lipschitz-integration-recovery|Nearest-sample integration for Lipschitz data]] is classical optimal
recovery; [Foucart (2022), Chapter 11](https://doi.org/10.1017/9781009003933.017),
source 146, is the relevant comparison. Equations (5), (17) and (18)
are elementary discrete versions, not new sampling principles.
The analytic two-box inverse is the classical multichannel mechanism
already localized in PL-475 (sources 142–143). Strong prime variance
bounds forcing zero-free conclusions are also classical;
[Zaccagnini (2016), Section 3.3](https://arxiv.org/pdf/1603.02952),
source 123, discusses the Selberg-integral converse. Its full-integral
statement is not being cited as the sparse, sample-centered,
paired fixed-modulus criterion (4).

The local addition is the proved transfer of geometric recovery to
the actual prime source and an independently proved GRH converse on
a prescribed grid with a vanishing retained fraction. It changes the
measurement requirement, not the arithmetic strength still missing.
No external priority or new prime-distribution estimate is claimed.

An auxiliary exact integer/rational check covered all 2,036 nonempty
sample sets on intervals of lengths 1 through 10, all square-root
grids of sizes 1 through 4,096, and 360 paired-channel cases from 180
nonnegative residue-supported coefficient arrays (seed 478). It
verified the distance formula and lower bound, endpoint-cell bounds,
the distance-envelope equality, the endpoint jump identity, weighted
recovery and conversion using the same sample mean or an arbitrary
constant. Singleton, full, clustered and irregular retained sets were
included. These are bookkeeping checks for generic rational data;
the displayed derivation proves the transfer. No analytic inverse,
prime logarithm or zero location is validated by those finite checks,
and no Lean or independent adversarial approval is claimed.
