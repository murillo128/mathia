# MC-535 — Multiplicative prime bridges retain sparse-window ambiguity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim and quantifiers

Fix a nonzero complex test \(\phi\in C_c^1((4/3,5/3))\). There are
constants \(c_\phi,\kappa_\phi>0\) and \(X_\phi\) such that the following
holds for every integer \(X\ge X_\phi\). Choose any integer
\(1\le H\le X/20\), put \(L_1=H\), \(L_2=K=\lfloor\sqrt2H\rfloor\),
and prescribe nonempty sets of starts
\[
 R_i\subset\{X,\ldots,2X-1\},\qquad q_i=|R_i|,\qquad
 q=q_1+q_2\le\kappa_\phi X/\log X.
\tag{1}
\]
The sets are fixed before the coefficient construction. Then there are
**multiplicative** functions \(f^+,f^-:\mathbb N\to\{-1,0,1\}\), with
\[
 |f^+(n)|=|f^-(n)|=\mu(n)^2,
\tag{2}
\]
satisfying all three conclusions below. Write
\(F^\pm(y)=\sum_{n\le y}f^\pm(n)\),
\(S^\pm_L(j)=F^\pm(j+L)-F^\pm(j)\), and
\(T_{\phi,X}(f)=\sum_n f(n)\phi(n/X)\).

First, the exact observed values agree in both channels:
\[
 S^+_{L_i}(j)=S^-_{L_i}(j)\quad(j\in R_i,\ i=1,2).
\tag{3}
\]
Second, even their uncentered sample mean squares are small:
\[
 \boxed{\frac1{q_i}\sum_{j\in R_i}|S^\pm_{L_i}(j)|^2
       \le 2(H+K+2),\qquad i=1,2.}
\tag{4}
\]
Third, the fixed signed smooth target remains separated:
\[
 \boxed{|T_{\phi,X}(f^+)-T_{\phi,X}(f^-)|
       \ge c_\phi\frac{X}{(q+1)(\log X)^2}.}
\tag{5}
\]
In particular the centered sample energies also satisfy (4).
All window sums within each control come from its one multiplicative
coefficient sequence.

This strengthens [MC-534](MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.md)
in a different admissible class: multiplicativity is restored while
matching the sampled observations and retaining their small energy.
The price here is a squared logarithm in the separation, a restricted
observation horizon, and fixed nonadaptive start sets. The controls
**depend on the scale and the prescribed sets**. No single pair with
these properties on an unbounded sequence of scales is constructed.
They do not obey the Möbius prime law \(\mu(p)=-1\), nor its
reciprocal-zeta identity.

## 1. Prime signs without composite copies in the observation range

Choose a closed interval \([s,t]\Subset(4/3,5/3)\), a unit complex
number \(\omega\), and \(\eta>0\), all depending only on \(\phi\), with
\[
 \operatorname{Re}(-\omega\phi'(u))\ge\eta\quad(s\le u\le t).
\tag{6}
\]
Such an interval exists because a nonzero compactly supported test
cannot have identically zero derivative. Set
\[
 a=\lceil sX\rceil,\quad b=\lfloor tX\rfloor,\quad
 P=\{p\text{ prime}:a<p\le b\},\quad S=|P|.
\tag{7}
\]
All queried coefficients lie below
\[
 N=2X-1+K<\tfrac52X<2\min P
\tag{8}
\]
for sufficiently large \(X\). Thus, up to \(N\), a number divisible
by a selected prime is that prime itself. Altering signs at \(P\)
does not alter any composite coefficient in the observed range. This
is the precise reason multiplicativity allows the construction.

Set every prime-power value of exponent at least two to zero and
extend values at distinct primes multiplicatively. At primes outside
\(P\), initially choose independent Rademacher signs. Let \(g\) denote
the auxiliary multiplicative function with the same signs outside
\(P\), but with value zero at the selected primes, and put
\(G(y)=\sum_{n\le y}g(n)\).

As a baseline, assign alternating signs \(+1,-1,+1,-1,\ldots\) to
\(P\) in increasing order. Their cumulative sum is
\[
 B(y)=\#\{p\in P:p\le y\}\pmod2\in\{0,1\}.
\tag{9}
\]
The full baseline multiplicative function \(f^0\) has, throughout the
observation range, the exact prefix identity
\[
 F^0(y)=G(y)+B(y)\qquad(0\le y\le N).
\tag{10}
\]
The auxiliary \(g\) need not have exact square-free support; the final
functions \(f^0,f^+,f^-\) do.

## 2. One background serves both small-energy channels

Distinct square-free integers not divisible by any selected prime have
distinct products of the independent signs. Hence
\[
 \mathbb E[g(n)g(m)]=0\quad(n\ne m),\qquad
 \mathbb E\left|G(j+L)-G(j)\right|^2
   =\#\{j<n\le j+L:\mu(n)^2=1,\ (n,\prod_{p\in P}p)=1\}
   \le L.
\tag{11}
\]
For the intervals here \(j\ge X>1\), every summand also has zero
expectation. Since \(|B(j+L)-B(j)|\le1\), (10) gives
\[
 \mathbb E|S^0_L(j)|^2\le L+1.
\]
Therefore, for the two prescribed sets, the nonnegative variable
\[
 Z=\sum_{i=1}^2\frac1{q_i}\sum_{j\in R_i}|S^0_{L_i}(j)|^2
\]
satisfies \(\mathbb E Z\le H+K+2\). Markov's inequality gives a
choice of the common background with
\[
 Z\le2(H+K+2).
\tag{12}
\]
Fix that choice. Only finitely many prime signs are involved; all
remaining signs can subsequently be assigned arbitrarily. Each
individual channel obeys (4) for this baseline. No independence
between windows or channels is used.

## 3. Balanced prime bridges preserve every queried endpoint

Partition \([a,b]\) at every queried endpoint \(j,j+L_i\) strictly
inside it:
\[
 a=z_0<z_1<\cdots<z_k=b,\qquad k\le2q+1.
\tag{13}
\]
In a gap \((z_{r-1},z_r]\), let \(m_r\) be its number of selected
primes, \(h_r=\lfloor m_r/2\rfloor\), and \(e=B(z_{r-1})\).
At the first \(h_r\) selected primes assign \(+1\) to \(f^+\) and
\(-1\) to \(f^-\); at the next \(h_r\), reverse those signs.
If \(m_r\) is odd, assign the remaining last prime the common sign
\(1-2e\). Keep all other prime values equal to the chosen background.

Each gap's two selected-prime sums equal the alternating baseline's
sum: zero for even \(m_r\), and \(1-2e\) for odd \(m_r\).
Consequently both full prefixes equal \(F^0\) at every queried
endpoint, including endpoints outside \([a,b]\). Equation (8) excludes
composite copies of the changed signs. This proves (3), transfers (12)
to both controls, and proves (4). The multiplicative extension gives
(2) for every positive integer, including integers beyond \(N\).

Within \([0,N]\), the difference primitive
\(D(n)=F^+(n)-F^-(n)\) is nonnegative and vanishes outside \((a,b)\).
At the \(\ell\)-th selected prime in the even part of a gap it is
\(2\min(\ell,2h_r-\ell)\). Thus
\[
 \sum_{n=a}^{b-1}D(n)\ge2\sum_{r=1}^k h_r^2
 \ge\frac{(S-k)_+^2}{2k}.
\tag{14}
\]
The first inequality retains only the distinct selected-prime
positions; intervening integers contribute nonnegatively. The second
uses \(\sum h_r\ge(S-k)/2\) and Cauchy--Schwarz. Neither a local
prime-density estimate in every gap nor a lower bound on every gap's
length is required.

Discrete summation by parts and (6) now give
\[
 \begin{aligned}
 \operatorname{Re}\bigl(\omega[T_{\phi,X}(f^+)-T_{\phi,X}(f^-)]\bigr)
 &=-\sum_{n=a}^{b-1}D(n)\operatorname{Re}
       \bigl(\omega[\phi((n+1)/X)-\phi(n/X)]\bigr)\\
 &\ge\frac{\eta(S-k)_+^2}{2Xk}.
 \end{aligned}
\tag{15}
\]
Every unit cell used here lies in \([sX,tX]\). Although \(D\) need
not vanish past \(N\), \(\phi(n/X)\) is supported below \(2X\le N\),
so no later composite copies enter this identity.

The classical prime number theorem, used only on the fixed interval
in (7), gives
\[
 S=(t-s+o(1))X/\log X.
\tag{16}
\]
Take \(d_\phi>0\) so that \(S\ge d_\phi X/\log X\) eventually,
and choose \(\kappa_\phi=d_\phi/8\). Increasing \(X_\phi\) makes
\(k\le S/2\). Substitution into (15), with \(k\le2q+1\), proves
(5). The squared logarithm comes from squaring the available prime
population in (14); optimal logarithmic dependence is not asserted.

## 4. What this rules out, and what remains arithmetic

At macroscopic \(H=\lfloor X/20\rfloor\), both sample averages in
(4) are \(O(X)\), yet for fixed \(0<\delta<1/2\) and
\(q\le X^{1/2-\delta}\), (5) is
\[
 \gg_\phi X^{1/2+\delta}/(\log X)^2.
\tag{17}
\]
Any estimator given only these interval values, the exact support,
and the fact of multiplicativity produces the same output for the
pair. Its worst-case target error is at least half (5), even if it is
nonlinear. Thus those assumptions alone cannot give a uniform
square-root-exponent recovery from this number of fixed observations,
**even on the subclass obeying the observed energy ceiling**.

The pole-isolating test in
[MC-532](MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md)
has the required support and is an admissible fixed test. Its
source-independent two-box identity also applies to these bounded
coefficients. Its reciprocal-zeta pole asymptotic does not.
This is not a counterexample to the Möbius criterion of
[MC-533](MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md).
That criterion concerns the actual Möbius sequence, a larger sample
exponent, and one unbounded scale set for a fixed arithmetic source.

The omitted hypotheses matter. The controls do not keep every prime
sign negative; imposing that law with (2) and multiplicativity fixes
Möbius exactly. No qualitative Chowla limits or prescribed Euler product
continuation are imposed. One fixed pair on infinitely many scales is
not supplied. The selected-prime changes propagate to multiples above
the observed range, so the disjoint-block pasting argument of MC-534
cannot be transferred without controlling those copies. The start sets
are fixed before choosing the random background; data-dependent or
adaptive sampling is not covered by the mean-square selection step.
No claim of a probabilistic model for deterministic Möbius is made.

## Prior art, validation, and mathematical delta

The prime count (16) is the classical PNT
([NIST DLMF, §27.12](https://dlmf.nist.gov/27.12), MC-S89), not a
short-interval improvement. The Rademacher square-free multiplicative
model is classical; [Harper, Section 1](https://msp.org/ant/2019/13-10/ant-v13-n10-p02-s.pdf)
(MC-S88) defines it. Only the elementary orthogonality calculation
(11) is needed here, not Harper's higher-moment theorems.
[Klurman--Mangerel--Pohoata--Teräväinen](https://arxiv.org/abs/1911.06265)
(MC-S16) study discrepancy in this exact-support multiplicative class;
their unbounded-partial-sum result is distinct from same-block matched
observations and a fixed signed target.

The information lower-bound method is the classical indistinguishable
input construction behind [Baran--Demaine--Katz](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85) and MC-534. Within this line,
[MC-118](MC-118-balanced-prime-block-multiplicative-fractional-moment-barrier.md)
already combines balanced terminal prime signs, a Rademacher background,
and multiplicative propagation to obtain a fractional-moment obstruction.
It does not match arbitrary prescribed window observations or impose
their small sample mean squares. MC-534 does both observation matching
and signed target separation but its coefficient signs are not
multiplicative. The result here combines these existing ingredients to
close that specific one-scale multiplicativity escape. No external
novelty, new probability principle, or new PNT estimate is claimed.

Exact finite validation enumerated all 2,048 background-prime sign
assignments up to 41 with selected primes \(\{29,31\}\), checking the
second-moment identity for five intervals. A separate 336-case check
used scales \(X\in\{40,80,120,200,500,1000,2000\}\), the degenerate
pair \(H=K=1\) and the macroscopic pair, per-channel counts
\(1,2,3,5,10,20\), and four start patterns
(spaced, pseudorandom, left-clustered, right-clustered; seed 535).
It checked exact magnitudes, common endpoint and interval values,
(12)--(15), and 28,433 coprime-product identities; 253 cases had
strictly positive target separation. The rational test was
\(\phi(u)=-(u-3/2)((5/32)^2-(u-3/2)^2)^2\) on
\([43/32,53/32]\), zero outside. On \([23/16,25/16]\),
\(-\phi'\ge1/16384\). Small cases need not meet the asymptotic
population condition in (1); the exact bound (15) was checked instead.
These finite tests audit the construction; the proofs establish the
unbounded-scale quantified theorem. No Lean verification or independent
adversarial approval is asserted.

The remaining question is which additional **Möbius-specific** input,
or which fixed-function constraint across scales, can exclude these
prime-sign bridges. Generic multiplicativity by itself does not do so
at a single observed scale. No stronger bound for \(M(x)\), no
arithmetic sample-energy ceiling, and no obstruction to an improved
Möbius-specific recovery theorem is established. The present elementary
assembly does not supply a separate high-value formalization handoff.
