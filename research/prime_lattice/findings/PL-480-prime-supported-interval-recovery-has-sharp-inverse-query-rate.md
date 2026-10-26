# PL-480 — Prime-supported interval recovery has a sharp inverse-query rate

**Evidence/status:** EXACT-DERIVED / LITERATURE+DERIVED / SHARP RECOVERY
BOUND FOR A REWEIGHTED CONTROL CLASS. Classical optimal recovery and
Brun–Titchmarsh inputs; no external novelty or actual-prime variance
estimate is claimed.

## Claim and observation model

Fix a nonzero complex \(\phi\in C_c^1((4/3,5/3))\) and put
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
T_X(b)=\sum_n b_n\phi(n/X).
\tag{1}
\]
Here and below \(X\) is an integer. Let \(\mathcal B_X\) be the
class of real sequences satisfying
\[
b_n=a_n\quad(n\notin(X,2X]),\qquad
\tfrac12a_n\le b_n\le\tfrac32a_n,\qquad
\sum_n(b_n-a_n)=0.
\tag{2}
\]
The sum in (2) is finite. These controls have exactly the actual
prime-power support and total block mass. The baseline \(a\) and
the class are known, but the unknown member \(b\) is observed only
through at most \(q\) exact integer interval sums
\(\sum_{u<n\le v}b_n\), with \(0\le u<v\). Queries may be chosen
deterministically and adaptively. The returned estimate may be
nonlinear. Define
\[
e_q(X)=\inf_{\mathcal A}\sup_{b\in\mathcal B_X}
       |\mathcal A(b)-T_X(b)|,
\tag{3}
\]
where the infimum is over those query algorithms, with no restriction
on computations using the known baseline.

For every fixed \(0<\varepsilon<1\), there are
\(c_{\phi,\varepsilon}>0\), \(C_\phi<\infty\) and
\(X_{\phi,\varepsilon}\) such that
\[
\boxed{\quad
c_{\phi,\varepsilon}\frac{X}{q+1}
\le e_q(X)\le C_\phi\frac{X}{q+1},
\qquad 0\le q\le X^{1-\varepsilon},\quad
X\ge X_{\phi,\varepsilon}.
\quad}
\tag{4}
\]
The lower bound is realized by two controls \(a\pm d\) which give
the baseline response to every query. Moreover, \(d\) can be
supported only on **primes** congruent to 1 modulo 5: all higher
prime-power coefficients stay unchanged.

[[research/prime_lattice/findings/PL-479-prime-supported-relative-perturbations-retain-interval-query-ambiguity|PL-479]]
gave the lower bound \(X/((q+1)\log(3X))\) from a maximum-atom
estimate, for \(q\le\kappa_\phi X/\log(3X)\). The new claim is
the two-sided optimal rate (4) on each fixed polynomial query range.
The improvement uses short-interval **upper** bounds to prevent
concentration; it does not assume primes in every query cell. It does
not remove the logarithm throughout PL-479's larger, nearly linear
range.

## 1. Endpoint primitive area is weighted median dispersion

On an integer cell \((l,r]\), take capacities \(c_n\ge0\), and set
\[
W=\sum_{l<n\le r}c_n,\quad
C_j=\sum_{l<n\le j}c_n,\quad
F_j=\min(C_j,W-C_j)\quad(l\le j\le r).
\tag{5}
\]
The endpoints of \(F\) are zero, and
\(|F_j-F_{j-1}|\le c_j\). If \(W>0\), choose an integer
weighted median \(m\) with \(C_{m-1}\le W/2\le C_m\). Summing
the distances of atoms on each side of \(m\) gives the exact identity
\[
\begin{aligned}
\mathcal A:=\sum_{j=l}^{r-1}F_j
&=\sum_{j=l}^{m-1}C_j+\sum_{j=m}^{r-1}(W-C_j)\\
&=\sum_{l<n\le r}c_n|n-m|
 =\min_{z\in\mathbb R}\sum_{l<n\le r}c_n|n-z|.
\end{aligned}
\tag{6}
\]
The last equality is the usual weighted median characterization;
moving \(z\) rightwards changes the one-sided slope by the mass to
its left minus the mass to its right. Formula (6) also holds for
zero total mass. An atom straddling the half-mass level causes no
rounding error.

Suppose the atomic measure \(\mu=\sum c_n\delta_n\) has, for
some \(K>0,E\ge0\), the concentration bound
\[
\mu([z-u,z+u])\le 2Ku+E\qquad(z\in\mathbb R,\ u\ge0).
\tag{7}
\]
The layer-cake formula for distance, applied at a median, implies
\[
\mathcal A
=\int_0^\infty\mu(\{|n-m|>u\})\,du
\ge\int_0^\infty(W-E-2Ku)_+\,du
=\frac{(W-E)_+^2}{4K}.
\tag{8}
\]
Here \(x_+=\max(x,0)\). If a common measure obeying (7) is
restricted to \(k\) disjoint cells, each restriction obeys the
same bound. For total capacity \(W_*\), Cauchy–Schwarz then gives
\[
\boxed{\quad
\sum_{j=1}^k\mathcal A_j
\ge\frac{(W_*-kE)_+^2}{4Kk}.
\quad}
\tag{9}
\]
Indeed \(\sum_j(W_j-E)_+\ge(W_*-kE)_+\).
Empty cells and cells with only one atom are included. In particular,
(7) forces each atom to have mass at most \(E\); (8) cannot
mistakenly assign positive area to an isolated heavy atom.

## 2. A sieve bound supplies concentration control for prime weights

Choose a fixed \([s,t]\Subset(4/3,5/3)\), a unit complex
\(\omega\), and \(\eta>0\) with
\[
\operatorname{Re}(-\omega\phi'(v))\ge\eta
\qquad(s\le v\le t).
\tag{10}
\]
This is possible because a nonzero compactly supported \(C^1\)
function has a nonzero derivative somewhere. Write
\(p=\lceil sX\rceil\), \(r=\lfloor tX\rfloor\) and use only
the capacities
\[
c_n=\tfrac12\log n\,
 \mathbf1_{\{n\text{ prime},\ n\equiv1\ (5),\ p<n\le r\}}.
\tag{11}
\]
The fixed-modulus PNT gives
\[
W_*:=\sum_n c_n=(t-s)X/8+o(X).
\tag{12}
\]
For completeness, the prime-only version follows from
\(\psi(y;5,1)=y/4+o(y)\): the contribution of all powers
\(\ell^j\le y\), with \(\ell\) prime and \(j\ge2\), is
\(O(\sqrt y(\log y)^2)=o(y)\), by counting their possible bases
and exponents. No short-interval PNT is used.

The Montgomery–Vaughan Brun–Titchmarsh inequality states
\[
\pi(x+y;5,1)-\pi(x;5,1)
<\frac{2y}{4\log(y/5)}\qquad(x\ge1,\ y>5).
\tag{13}
\]
See source 148, or the explicit statement in
[Chirre–Pereira Júnior–de Laat, Section 2.2](https://arxiv.org/pdf/2005.02393).
This inequality is unconditional; their separate GRH-dependent
short-interval existence theorem is not being used.

Set \(L=\lceil X^{\varepsilon/2}\rceil\). For sufficiently large
\(X\), any half-open interval of length \(y\ge L\), with left
endpoint at least 1, contains capacity from (11) at most
\[
\frac{y\log(3X)}{4\log(y/5)}\le K_\varepsilon y,
\qquad K_\varepsilon=4/\varepsilon.
\tag{14}
\]
Only atoms in \((p,r]\) count, so their weights are bounded by
\(\tfrac12\log(3X)\) even if the containing interval is larger.
For a closed interval \(I\), intersect with \([p,r]\), cover the
intersection by a half-open interval, and enlarge it to length at
least \(L\) when needed. The covering length can be chosen at
most \(|I|+L+2\), with left endpoint at least 1. Thus
\[
\mu(I)\le K_\varepsilon(|I|+L+2),\qquad
E_X=K_\varepsilon(L+2)
\tag{15}
\]
supplies (7). This is an upper bound for every cell, not a lower
bound for its prime population. Sparsity and empty gaps do not
invalidate it.

## 3. Hide a signed response from all queried intervals

For any list of \(q\) integer interval queries, partition \([p,r]\)
at all distinct queried endpoints strictly inside it. There are
\(k\le2q+1\) cells. Use (5) in each cell, join the zero
endpoints, extend \(F\) by zero elsewhere, and put
\(d_n=F_n-F_{n-1}\). Then
\[
|d_n|\le c_n\le a_n/2,\quad
\sum_n d_n=0,\quad
\sum_{u<n\le v}d_n=F_v-F_u=0
\tag{16}
\]
for every query. Consequently \(a\pm d\in\mathcal B_X\), and
both have the actual baseline's query responses. The construction
leaves higher prime powers untouched.

Uniformly for \(q\le X^{1-\varepsilon}\), equations (12) and (15)
give
\[
kE_X=O_\varepsilon(X^{1-\varepsilon/2})=o(W_*).
\tag{17}
\]
After increasing \(X_{\phi,\varepsilon}\), ensure
\(kE_X\le W_*/2\). By (9),
\[
\sum_nF_n\ge\frac{W_*^2}{16K_\varepsilon k}
\gg_{\phi,\varepsilon}\frac{X^2}{q+1}.
\tag{18}
\]
Discrete summation by parts and (10) now yield
\[
\begin{aligned}
\operatorname{Re}\bigl(\omega T_X(d)\bigr)
&=-\sum_{n=p}^{r-1}F_n\operatorname{Re}\bigl(
\omega[\phi((n+1)/X)-\phi(n/X)]\bigr)\\
&\ge\frac{\eta}{X}\sum_nF_n
\gg_{\phi,\varepsilon}\frac{X}{q+1}.
\end{aligned}
\tag{19}
\]
All unit cells in this sum lie inside \([sX,tX]\). One fixed
rotated derivative controls the complex target without a
cancellation assumption.

For a deterministic adaptive algorithm, run it on \(a\), then
construct \(d\) using the resulting transcript's endpoints.
Induction over the queries gives the same transcript on \(a+d\)
and \(a-d\). The same output cannot be within less than
\(|T_X(d)|\) of both targets. This proves the lower bound in (4),
including algorithms that know the exact baseline and total mass.

## 4. A matching nonadaptive upper bound

For \(1\le q\le X\), partition \((X,2X]\) at
\(t_j=X+\lfloor jX/q\rfloor\), \(0\le j\le q\), query its
\(q\) cell masses \(B_j\), and return
\[
\widehat T_X=\sum_{j=1}^q\phi(t_{j-1}/X)B_j.
\tag{20}
\]
Since \(b_n\ge0\), the Lipschitz estimate gives
\[
|T_X(b)-\widehat T_X|
\le\|\phi'\|_\infty\frac{\lceil X/q\rceil}{X}
       \sum_{X<n\le2X}b_n
\ll_\phi X/q.
\tag{21}
\]
The mass is \(O(X)\) by (2) and the fixed-modulus PNT. For
\(q=0\), return \(T_X(a)\); the amplitude envelope bounds the
error by \(O_\phi(X)\). These bounds prove the upper half of
(4). No numerical evaluation cost or noisy-query model is claimed.

## Consequences, prior art and boundaries

The logarithmic loss in PL-479 is unnecessary on any fixed polynomial
query range. At \(q\asymp\sqrt X\), the worst-case error for
this control class is exactly of square-root order; for
\(q=o(\sqrt X)\), it is larger. Support, positive relative
weights, fixed mass and shared-source compatibility therefore do
not yield better uniform recovery in this observation model.

This is a classification of **unknown reweightings**, even with the
baseline known. It is not a query-complexity lower bound for the
single explicitly known sequence \(\Lambda(n)\mathbf1_{n\equiv1(5)}\).
The controls depend on scale and transcript; they need not be one
fixed pair across all scales. They do not impose canonical Euler
factors, a completed functional equation or actual prime variance
ceilings. Their common observed energies equal the baseline's,
whatever those energies are. The upper bound uses freely chosen
interval lengths; no matching rate for prescribed paired-window
queries is asserted. No conclusion about RH or joint GRH,
randomized algorithms, noisy observations, or a nearly linear query
regime follows.

The indistinguishable-input and adaptive-transcript arguments are
classical optimal recovery (source 146). The median identity and
layer-cake estimate are elementary classical facts, proved here;
(13) is classical sieve theory (source 148). The PNT input is
source 147. The local addition is their combination into a sharp
two-sided recovery rate for the actual-support relative-envelope
class, with a prime-only perturbation and the concentration defect
\(kE_X\) made explicit. No new sieve theorem or general recovery
principle is claimed. PL-479 remains useful in its larger query
range and under its weaker maximum-atom input.

An exact integer check verified (6), (8) and (9), capacity-bounded
increments, zero pinned endpoints and the affine-test
summation-by-parts identity for all 27,993 capacity/partition cases
of lengths 1 through 6 with capacities in \(\{0,1,4\}\).
For that check \(K=1\) and
\(E=\max(0,\max_{i\le j}[\sum_{n=i}^j c_n-(j-i)])\), which
enforces (7) on the atomic measure. Another 500 sparse rational
cases of lengths at most 64, seed 480, checked the same identities
with varying positive rational \(K\). These checks validate finite
bookkeeping only. The proof and the cited unconditional theorems
establish (4); no Lean verification or independent adversarial
approval is claimed.
