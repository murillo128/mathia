# PL-483 — Fixed prime-supported sources evade subquarter uniform observations

**Evidence/status:** EXACT-DERIVED / LITERATURE+DERIVED / NEGATIVE CONTROL.
Classical hidden-area and sieve arguments; no external novelty claim.
The controls retain actual prime-power support, positive relative weights
and the prime number theorem. They do not retain the exact von Mangoldt
coefficients or establish small sampled energies.

## Claim and quantifiers

Put
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
T_X(b)=\sum_n b_n\phi(n/X),
\]
where \(0\ne\phi\in C_c^1((4/3,5/3);\mathbb C)\) is fixed.
One may additionally require \(\int\phi=0\). Fix
\[
0\le\alpha<1/4,\qquad 3/4<\kappa<1-\alpha.
\tag{1}
\]
There are two **fixed deterministic infinite sequences** \(b^+,b^-\),
chosen before any observations, with
\[
\tfrac12a_n\le b_n^\pm\le\tfrac32a_n,
\qquad b_n^\pm=a_n\quad\text{unless }n\text{ is prime and }n\equiv1\ (5),
\tag{2}
\]
\[
\sum_{n\le x}b_n^\pm=\psi(x;5,1)+O_{\phi,\kappa}(x^\kappa)
=x/4+o(x).
\tag{3}
\]
For the deterministic scales \(X_k=4^k\), starting at a sufficiently
large fixed \(k_0\), let
\[
I_X=\{X,\ldots,2X-1\},\quad H=\lfloor X/20\rfloor,
\quad K=\lfloor\sqrt2H\rfloor,
\quad q_X=\lceil X^\alpha\rceil.
\tag{4}
\]
In each length channel take \(2q_X\) independent uniform starts from
\(I_X\), with replacement, under a law fixed in advance. Couple the
observations of all three sources using the same starts. With probability
one, at every sufficiently large scale \(X_k\), **every sampled value**
in both channels satisfies
\[
S_L^+(R)=S_L^-(R)=S_L^a(R),\qquad
S_L^b(j):=\sum_{j<n\le j+L}b_n,\quad L=H,K.
\tag{5}
\]
Nevertheless, deterministically at every sufficiently large \(X_k\),
\[
\boxed{|T_{X_k}(b^+)-T_{X_k}(b^-)|
\asymp_{\phi,\kappa} X_k^{2\kappa-1}.}
\tag{6}
\]
The exponent in (6) is strictly greater than \(1/2\).

This replaces the transcript-dependent controls of
[[research/prime_lattice/findings/PL-480-prime-supported-interval-recovery-has-sharp-inverse-query-rate|PL-480]]
by one pair fixed across all scales and before random draws. It also
places the missed-area mechanism of
[[research/prime_lattice/findings/PL-482-small-empirical-energy-permits-quarter-power-prime-observations|PL-482]]
on the actual prime support with positive relative weights. Unlike that
finding's abstract tents, the present controls do **not** have proved
small common sampled energies: their energies equal the baseline's,
whatever those are. Thus (6) is a signed-recovery obstruction, not
optimality of the actual-prime energy criterion.

## 1. Find one narrow prime packet without a short-interval lower bound

Choose \([s,t]\Subset(4/3,5/3)\), a complex unit \(\omega\), and
\(\eta>0\) with
\[
\operatorname{Re}(-\omega\phi'(u))\ge\eta\qquad(s\le u\le t).
\tag{7}
\]
Such an interval exists since a nonzero compactly supported \(C^1\)
function cannot have identically zero derivative.

For a large integer \(X\), partition
\([\lceil sX\rceil,\lfloor tX\rfloor]\) into consecutive integer
cells of length at most \(B=\lfloor X^\kappa\rfloor\), using length
\(B\) except possibly in the last cell. Give each prime \(p\equiv1\ (5)\)
in the partition capacity \(c_p=\tfrac12\log p\), and every other
integer capacity zero. The fixed-modulus PNT gives total capacity
\[
W_*=(t-s)X/8+o(X).
\tag{8}
\]
The prime-only statement follows by subtracting the higher-power
contribution \(O(\sqrt X\log^2 X)=o(X)\) from \(\psi\).
There are \(O_{s,t}(X/B)\) cells. Select the **leftmost cell of
maximal capacity**, denoted \((l_X,r_X]\), with capacity \(W_X\).
Then
\[
W_X\gg_{s,t} B.
\tag{9}
\]
This selection is deterministic and uses no samples. It requires no
lower bound on the prime count in a prescribed short interval.

An upper bound prevents the capacity in this selected cell from being
concentrated in a tiny subinterval. The unconditional Brun–Titchmarsh
inequality gives
\[
\pi(x+y;5,1)-\pi(x;5,1)<\frac{2y}{4\log(y/5)}
\quad(x\ge1,\ y>5).
\tag{10}
\]
Set \(D_X=\lceil X^{\kappa/2}\rceil\). For all sufficiently large
\(X\), the measure \(\mu_X=\sum_{l_X<n\le r_X}c_n\delta_n\)
obeys, for every real closed interval \(I\),
\[
\mu_X(I)\le C_\kappa(|I|+D_X+2),\qquad C_\kappa=4/\kappa.
\tag{11}
\]
Indeed intersect \(I\) with \([l_X,r_X]\), cover the result by a
half-open interval with left endpoint at least 1, and enlarge it to
length at least \(D_X\). Its length can be at most
\(|I|+D_X+2\). All contributing weights are at most
\(\tfrac12\log(3X)\); (10) then proves (11), since
\(\log(D_X/5)\ge(\kappa/4)\log X\) eventually. In particular
\(W_X\ll_\kappa B\). Write \(E_X=C_\kappa(D_X+2)=o(B)\).

The inputs are the fixed-modulus PNT in [Granville, Section 11.9,
equation (11.9.1)](https://dms.umontreal.ca/~andrew/Courses/Chapter11.pdf),
source 147, and Montgomery–Vaughan's sieve bound, source 148, as stated
in [Chirre–Pereira Júnior–de Laat, Section 2.2](https://arxiv.org/pdf/2005.02393).
The latter paper's GRH-dependent existence results are not used.

## 2. Balance the packet and retain its signed area

For \(l_X\le j\le r_X\) define
\[
C_j=\sum_{l_X<n\le j}c_n,\qquad
F_j=\min(C_j,W_X-C_j),
\tag{12}
\]
and extend \(F\) by zero elsewhere. Its endpoint values vanish,
\(F_j\ge0\), and \(|F_j-F_{j-1}|\le c_j\). The weighted-median
identity from PL-480, also immediate by summing the masses to either
side of a median, is
\[
\mathcal A_X:=\sum_{j=l_X}^{r_X-1}F_j
=\min_{z\in\mathbb R}\sum_{l_X<n\le r_X}c_n|n-z|.
\tag{13}
\]
If \(m\) is a median, (11) and the layer-cake formula give
\[
\begin{aligned}
\mathcal A_X
&=\int_0^\infty\mu_X(\{|n-m|>u\})\,du\\
&\ge\int_0^\infty(W_X-E_X-2C_\kappa u)_+\,du
=\frac{(W_X-E_X)_+^2}{4C_\kappa}.
\end{aligned}
\tag{14}
\]
Equations (9), (11) and \(E_X=o(B)\), together with
\(F_j\le W_X/2\) on at most \(B\) indices, prove
\[
\mathcal A_X\asymp_{\phi,\kappa} B^2.
\tag{15}
\]
With \(d_n=F_n-F_{n-1}\), the packet has zero total mass, prime-only
support, and \(|d_n|\le a_n/2\). Summation by parts and (7) imply
\[
\operatorname{Re}\left(\omega\sum_n d_n\phi(n/X)\right)
=-\sum_jF_j\operatorname{Re}\bigl(
\omega[\phi((j+1)/X)-\phi(j/X)]\bigr)
\ge\frac\eta X\mathcal A_X.
\tag{16}
\]
The corresponding upper bound is
\(\|\phi'\|_\infty\mathcal A_X/X\). Empty prime gaps, unequal
prime weights and an atom crossing the half-capacity level cause no
problem in (12)–(14).

Perform this deterministic construction at every \(X_k=4^k\), for
\(k\ge k_0\). Join the packet primitives into one sequence \(F_n\)
which is zero outside their disjoint cells, and define globally
\[
d_n=F_n-F_{n-1},\qquad b_n^\pm=a_n\pm d_n.
\tag{17}
\]
The cells lie in \((sX_k,tX_k]\). They are disjoint, and no other
packet meets \([X_k,2X_k+K_k]\) or the support of \(\phi(n/X_k)\).
Every completed packet has zero mass. Hence
\(\sum_{n\le x}d_n=F_{\lfloor x\rfloor}=O(x^\kappa)\), proving
(2)–(3), while (15)–(16) prove (6). In particular these are one pair
of infinite sources, not a sequence of controls chosen after queries.

## 3. Uniform observations miss the same fixed packets

At scale \(X=X_k\), let \(A_k=\{j:F_j\ne0\}\) inside its packet.
Then \(|A_k|\le B\). The common exceptional set of starts
\[
E_k=I_X\cap\bigl(A_k\cup(A_k-H)\cup(A_k-K)\bigr)
\tag{18}
\]
has size at most \(3B\). For either length, telescoping gives
\[
S_L^\pm(j)-S_L^a(j)=\pm(F_{j+L}-F_j),
\tag{19}
\]
so both channels equal the baseline outside this same set. This also
handles windows containing an entire balanced packet: their difference
is zero, even though they contain modified primes.

There are \(4q_X\) observations across the two channels. The union
bound gives
\[
\Pr\{\text{any sampled start belongs to }E_k\}
\le 12q_XB/X\ll X_k^{\alpha+\kappa-1}.
\tag{20}
\]
The exponent is negative by (1), and \(X_k=4^k\). Thus (20) is
summable. The first Borel–Cantelli lemma proves (5). Independence
across scales is unnecessary; sampling at other integer scales may
also be defined, but the assertion concerns this geometric subsequence.
Repeated draws retain their multiplicities and do not alter the bound.

Consequently the ordinary sample-centered variances of \(b^+,b^-\)
and \(a\) coincide exactly in each channel at all sufficiently large
\(X_k\), almost surely. No upper bound on their common value was used.
Their nonnegative coefficients also retain the window jump envelope
\(|S_L^\pm(j+1)-S_L^\pm(j)|\le\tfrac32\log(3X)\).

## Consequence, prior art and remaining boundary

For the stated uniform law, positivity, exact prime-power support,
bounded relative reweighting, the leading PNT, and compatibility of
both channels with one fixed source do not make the scale's sampled
values determine its signed smooth target to square-root accuracy.
Any estimator using only those values and the shared structural
constraints returns the same answer on the two controls when (5)
holds; at least one of its two errors is at least half (6). This is a
statement about the observations at that scale, not a lower bound for
adaptive queries or an algorithm accumulating observations from all
other scales and given additional information about the unknown source.

The hidden-area mechanism is classical optimal recovery, with
[Baran–Demaine–Katz](https://erikdemaine.org/papers/Integration_Algorithmica/)
(source 152) supplying the relevant deterministic/randomized Lipschitz
integration comparison. No general randomized minimax rate from that
different model is being asserted here. The local delta is the
simultaneous satisfaction of the prime-support/relative-weight
constraints, deterministic source choice across scales, and
almost-sure invisibility for both prescribed lengths. The sparse
packet selection uses coarse prime mass and an upper sieve bound;
it does not invoke a new short-interval prime theorem. PL-480's median
lemma is reused, not claimed again as a discovery.

The common energy remains the crucial distinction from the abstract
tent counterexample in PL-482 and the bounded residue-source controls
in [[research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity|PL-477]].
If a small baseline energy ceiling holds on these scales, (5) transfers
it to both controls. This conditional observation supplies no proof of
that ceiling. In particular the result does not refute any criterion
for the single exact sequence \(a_n\), prove that exponent \(1/4\)
is necessary for its energy criterion, or establish a logarithmic
lower loss. Canonical Euler factors, a completed functional equation
and the noncancelling zero-isolating formula are not preserved merely
by (2)–(3). No zero exclusion or RH/GRH conclusion follows.

An exact rational bookkeeping check covered 1,092 capacity populations
of lengths 1 through 6 with capacities in \(\{0,1,4\}\), verifying
median area, its concentration lower bound, capacity-bounded increments,
zero mass, summation by parts and 28,965 window identities. Three
geometrically separated blocks with rational capacities on actual
mod-5 prime support checked 10,752 window identities and common-mask
equalities, plus 600 sample-variance equalities with repeated draws.
These validate finite support/gluing bookkeeping, not asymptotic prime
counts, small prime energies, formal verification or independent
adversarial approval. The reused finite lemma and elementary gluing
offer no separate high-value formalization target.
