# MC-542 — Balanced prime replicas force centered window energy

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`NO-NOVELTY-CLAIM`. The bounds concern a prescribed-prime random
multiplicative ensemble: an exact expectation floor and a simultaneous
high-probability floor on a comparable-scale band. They are neither
pointwise bounds for every realization nor statements about actual
Möbius sums.

## Claim and the interval-specific question

[MC-541](MC-541-optimal-prescribed-prime-moments-still-force-lacunarity.md)
rules out a small uniform weighted second-moment bound for the
prime-prescription method of
[MC-538](MC-538-one-fixed-multiplicative-source-defeats-subquarter-random-observations.md).
Its attaining weights are not interval indicators. Here one isolated
balanced prime block forces a large **expected centered window energy**
on a whole comparable-scale band. The surviving component is the
free-prime character at three, not an arbitrary sign-matched weight.

Let \(Y\ge100\) be an integer. Let \(A_0\) be a finite set of primes
not containing three, with
\[
                       Q_0:=\prod_{p\in A_0}p<Y.
\tag{1}
\]
The empty set is allowed, with product one. Prescribe arbitrary signs
on \(A_0\). Let
\[
 P=\{p_1<\cdots<p_{2h}\}\subset(4Y/3,5Y/3),\quad h\ge1,
 \qquad b_p\in\{-1,1\},\quad \sum_{p\in P}b_p=0.
\tag{2}
\]
Write \(w=p_{2h}-p_1\) and
\[
 B(n)=\sum_{p\in P,\ p\le n}b_p,\qquad
                    \mathcal B_2=\sum_{n\in\mathbb Z}|B(n)|^2.
\tag{3}
\]
Balance makes this a finite sum, supported on
\(p_1\le n<p_{2h}\). For integer \(X\), put
\[
 3Y\le X\le\lfloor13Y/4\rfloor,\quad
 I_X=\{X,\ldots,2X-1\},\quad
 H=\lfloor X/20\rfloor,\quad K=\lfloor\sqrt2H\rfloor.
\tag{4}
\]
Assume \(3w\le H\). In particular, \(3w\le\lfloor3Y/20\rfloor\)
makes the result simultaneous throughout this scale band.

Construct \(g\) by prescribing the signs above on \(A=A_0\cup P\),
setting prime values to zero on any finite set \(Z\) disjoint from
\(A\cup\{3\}\), and taking independent Rademacher signs at all other
primes. Extend multiplicatively on square-free integers, set all
nonsquare-free values to zero, and take \(g(1)=1\). If \(Z\) is empty,
every realization has exact magnitude \(\mu(n)^2\). Define
\[
 S_L(j)=\sum_{j<n\le j+L}g(n),\qquad
 \overline S_L=X^{-1}\sum_{j\in I_X}S_L(j),\qquad
 V_L=X^{-1}\sum_{j\in I_X}|S_L(j)-\overline S_L|^2.
\tag{5}
\]
For **each** \(L\in\{H,K\}\),
\[
                     \boxed{\mathbb E V_L\ge\frac6X\mathcal B_2.}
\tag{6}
\]
The same lower bound holds if one first replaces \(S_L(j)\) by
\(S_L(j)-\mathbb E S_L(j)\), then subtracts its empirical mean.
It also lower-bounds the expectation of the uncentered complete
energy, since centering only decreases that energy.

Two useful forms of the same obstruction are:

* If the first \(h\) prime signs are positive and the last \(h\)
  negative, then
  \[
    \mathcal B_2\ge\frac{2h^3+h}{3},\qquad
    \boxed{\mathbb E V_L\ge\frac{4h^3+2h}{X}.}
  \tag{7}
  \]
* For any \(\phi\in C^1([p_1/Y,p_{2h}/Y];\mathbb C)\) with
  \(\|\phi'\|_\infty>0\), and **any balanced sign order**, let
  \(T_B(Y)=\sum_{p\in P}b_p\phi(p/Y)\). Then
  \[
   \boxed{\mathbb E V_L\ge
    \frac{6Y^2|T_B(Y)|^2}{Xw\|\phi'\|_\infty^2}.}
  \tag{8}
  \]
  Thus retaining a large signed smooth target on a narrow prime
  block has a definite quadratic cost at its multiplicative replica.

Section 4 strengthens the same replica obstruction from expectation
to probability. For the ordered blocks of Section 3, with probability
\(1-o(1)\), both centered energies satisfy the lower bound in (19)
**simultaneously at every integer scale in (4)**. This uses a maximal
bound for the background with the selected prime block removed;
it does not infer typical behavior from (6) alone.

## 1. The free-prime projection isolates an actual interval profile

For every surviving square-free integer write \(n=dm\), where
\(d\mid Q_A:=\prod_{p\in A}p\), and \(m\) uses only free primes.
With \(b(d)=\prod_{p\mid d}b_p\), define
\[
 a_m(j)=\sum_{\substack{d\mid Q_A\\j<dm\le j+L}}b(d).
\tag{9}
\]
Only finitely many \(m\) contribute in the observation horizon.
The products \(\epsilon(m)\) of free prime signs are orthonormal,
including \(\epsilon(1)=1\), and
\[
 S_L(j)=\sum_m\epsilon(m)a_m(j).
\tag{10}
\]
Writing \(\overline a_m=X^{-1}\sum_j a_m(j)\) and subtracting
the empirical mean **before** squaring gives the exact identity
\[
 \mathbb E V_L=
 \frac1X\sum_m\sum_{j\in I_X}|a_m(j)-\overline a_m|^2.
\tag{11}
\]
Ensemble centering deletes only the \(m=1\) term. In particular the
\(m=3\) term survives either form of centering.

For \(j\in I_X\), every \(d\) in \(a_3(j)\) satisfies
\[
 Y\le j/3<d\le(j+L)/3
 <\frac{(2+\sqrt2/20)13}{12}Y
 <\frac83Y.
\tag{12}
\]
A divisor using only \(A_0\) is at most \(Q_0<Y\). A divisor using
a prime of \(P\) and any other prime is greater than \(8Y/3\),
since the other prime is at least two. Therefore the only possible
divisors in (12) are single primes of \(P\), regardless of the
old prescribed signs or the zero set. Consequently
\[
       a_3(j)=B(\lfloor(j+L)/3\rfloor)-B(\lfloor j/3\rfloor).
\tag{13}
\]
This is a Fourier coefficient in the random prime signs, obtained
from the original interval sum. No change of its arithmetic weights
has been made.

## 2. Two separated pulses have zero empirical mean

Set \(C(j)=B(\lfloor j/3\rfloor)\), for integer \(j\). Its support
is contained in
\[
                   J=\{3p_1,\ldots,3p_{2h}-1\}.
\tag{14}
\]
Each value of \(B\) is repeated exactly three times, so
\[
                       \sum_j|C(j)|^2=3\mathcal B_2.
\tag{15}
\]
The support of \(a_3=C(\cdot+L)-C\) lies in
\((J-L)\cup J\). These two sets are disjoint because
\(L\ge H\ge3w\). Both lie entirely inside \(I_X\): their lower
endpoint is greater than
\[
 4Y-\frac{\sqrt2}{20}\frac{13Y}{4}>\frac{13Y}{4}\ge X,
\]
and their upper endpoint is less than \(5Y\le2X-1\) for \(Y\ge100\).
Thus translations introduce no truncation at the ends of \(I_X\),
and exactly
\[
 \sum_{j\in I_X}a_3(j)=0,\qquad
 \sum_{j\in I_X}|a_3(j)|^2=6\mathcal B_2.
\tag{16}
\]
Retaining this one nonnegative term in (11) proves (6). It also
shows why an unknown fitted constant cannot absorb the replica.

For the ordered block in (7), \(B(p_r)=\min(r,2h-r)\). The
successive distinct integer prime positions have gaps at least one,
so
\[
 \mathcal B_2\ge h^2+2\sum_{r=1}^{h-1}r^2=(2h^3+h)/3.
\tag{17}
\]
This elementary bound need not be optimal for prime gaps.

For (8), discrete summation by parts and Cauchy–Schwarz give
\[
 T_B(Y)=-\sum_{n=p_1}^{p_{2h}-1}B(n)
             [\phi((n+1)/Y)-\phi(n/Y)],
\]
\[
            |T_B(Y)|^2\le
              \mathcal B_2\,w\|\phi'\|_\infty^2/Y^2.
\tag{18}
\]
This does not require a nonnegative primitive or a real test.

## 3. Consequence for the balanced-block background method

Fix \(2/3<\kappa<1\). The ordinary prime number theorem and the
pigeonhole construction of MC-538 give, for all sufficiently large
\(Y\), a cell of width at most \(Y^\kappa\) in
\((4Y/3,5Y/3)\) containing \(\gg Y^\kappa/\log Y\) primes.
Take an even subset and order its signs as in (7). For large \(Y\),
its width satisfies (4)'s separation condition throughout the band.
Hence the same prime prescription satisfies
\[
 \boxed{\mathbb E V_H,\ \mathbb E V_K
       \gg \frac{Y^{3\kappa-1}}{(\log Y)^3}
       \quad(3Y\le X\le\lfloor13Y/4\rfloor).}
\tag{19}
\]
In particular, even taking \(A_0=Z=\varnothing\), there is no
uniform \(X^{1+o(1)}\) upper bound for these actual centered ensemble
energies over such prescriptions. Their prime harmonic mass tends
to zero, since \(\sum_{p\in P}1/p\ll Y^{\kappa-1}\).
Neither balance nor small harmonic mass supplies that estimate.

MC-538 uses \(\kappa>3/4\) to retain a smooth target above the
square-root scale. Its blocks therefore lie strictly beyond the
\(2/3\) threshold of this interval-energy obstruction. More generally,
(8) shows that rearranging the balanced signs cannot retain the same
smooth target while freely eliminating the replica's energy cost.

This resolves one concrete part of MC-541's interval-specific gap:
the failure is not confined to its arbitrary coefficient extremizers.
An isolated balanced block already obstructs the desired expectation
bound for both intended window lengths on comparable scales.

## 4. The replica survives with high probability throughout the band

Retain (1)–(5), now with the band-wide separation
\(3w\le\lfloor3Y/20\rfloor\). Put
\[
 N=7Y,\qquad r=\lceil\log_2 N\rceil,\qquad
 C_0=2^{|A_0|}.
\tag{20}
\]
For every \(0<\tau<1\),
\[
\boxed{
 \Pr\!\left\{
  \text{for all }3Y\le X\le\lfloor13Y/4\rfloor
  \text{ and }L\in\{H,K\},\quad
  V_L\ge(1-\tau)^2\frac{6\mathcal B_2}{X}
 \right\}
 \ge 1-\frac{4C_0N(r+1)^2w}{\tau^2\mathcal B_2}.
}
\tag{21}
\]
All scales here are integers; \(H,K,V_L\) retain their dependence
on \(X\). A negative right side is simply uninformative. The event
also gives the same lower bound for energy about **any** fitted
constant, including a realization-dependent choice.

### Remove the entire prime block before bounding the background

Let \(g_0\) agree with \(g\) except that all primes in \(P\) are
set to zero, and define
\[
 G_0(t)=\sum_{n\le t}g_0(n),\qquad
 A=\max_{0\le t\le N}|G_0(t)|.
\tag{22}
\]
Grouping by the free prime part as in MC-541 gives, for every
deterministic complex weight vector supported on \([1,N]\),
\[
 \mathbb E\left|\sum_{n\le N}v_ng_0(n)\right|^2
             \le C_0\sum_{n\le N}|v_n|^2.
\tag{23}
\]
Only the old primes \(A_0\) are prescribed in this auxiliary
ensemble. The possibly large set \(P\) is zeroed and therefore
does not enter \(C_0\).

Here is the needed maximal version, with its constant explicit:
\[
                       \mathbb E A^2\le C_0N(r+1)^2.
\tag{24}
\]
Pad \(g_0(n)\) by zero from \(N+1\) through \(2^r\). Every
prefix is a disjoint union of at most \(r+1\) dyadic intervals,
so its squared sum is at most \(r+1\) times the sum of squared
block sums over the whole dyadic tree. At each of its \(r+1\)
levels, (23) bounds the expectation of that sum by \(C_0N\):
the intervals partition the padded range and the nonzero coefficient
norms total \(N\). This proves (24). It is the classical
Rademacher–Menshov dyadic argument, applied to the second-moment
bound (23); independence of the values \(g_0(n)\) is not assumed.

### Isolate the replica pathwise on the support of its test

For a given \(X,L\), write \(a_L(j)=C(j+L)-C(j)\), with
\(C\) from Section 2. On the support of \(a_L\), every integer
in the window \((j,j+L]\) lies between \(4Y-L\) and \(5Y+L\).
Also \(L\le13\sqrt2Y/80<Y/4\). A multiple of a selected
prime in this range can only have multiplier three or four:
multiplier at most two is below \(10Y/3\), and multiplier at
least five is above \(20Y/3\). Multiplier four is nonsquare-free
and contributes zero. All these windows lie below \(N\), and
\((\min P)^2>N\), so no product of two selected primes occurs.
Consequently, for every realization and every such start,
\[
 S_L(j)-[G_0(j+L)-G_0(j)]=g(3)a_L(j).
\tag{25}
\]
This identity uses the physical support of the test, not just its
Walsh coefficient. From (15)–(16),
\[
 \sum_j a_L(j)=0,\quad
 \sum_j|a_L(j)|^2=6\mathcal B_2,\quad
 \sum_j|a_L(j)|\le6\sqrt{w\mathcal B_2}.
\tag{26}
\]
The last bound is Cauchy–Schwarz on the \(3w\) positions of
\(C\), followed by the two disjoint translates. Thus
\[
 \sum_{j\in I_X}a_L(j)S_L(j)
      =6g(3)\mathcal B_2+E_L,\qquad
 |E_L|\le12A\sqrt{w\mathcal B_2}.
\tag{27}
\]
Because \(|g(3)|=1\), the single event
\[
                  A\le\frac{\tau\sqrt{\mathcal B_2}}{2\sqrt w}
\tag{28}
\]
forces the absolute pairing in (27) to be at least
\(6(1-\tau)\mathcal B_2\), for **every** scale and both
channels at once. No independence between \(g(3)\) and the error
is required. Since the test sums to zero, Cauchy–Schwarz gives,
for any complex constant \(c\),
\[
 \left|\sum_j a_L(j)S_L(j)\right|^2
       \le6\mathcal B_2\sum_j|S_L(j)-c|^2.
\tag{29}
\]
Take the empirical mean for \(c\), then apply Markov's inequality
to (24) and (28). This proves (21) without a union bound over the
scales. Under the original hypotheses, \(\mathbb E g(3)=0\)
and \(\mathbb E g_0(n)=0\) for \(n>Q_0\). Hence the pairing
with \(\mathbb E S_L\) is zero; the same event also proves (21)
after ensemble centering followed by empirical centering.

### Ordered blocks give a vanishing exceptional probability

The condition \(Q_0<Y\) implies \(C_0=Y^{o(1)}\), uniformly
over the old prescribed set. Indeed, for any \(\epsilon>0\),
\(2\le p^\epsilon\) for all sufficiently large primes; the
finitely many smaller primes contribute a fixed factor, giving
\(2^{|A_0|}\ll_\epsilon Q_0^\epsilon\).

For the ordered blocks in Section 3, \(w\le Y^\kappa\) and
\(\mathcal B_2\gg Y^{3\kappa}/(\log Y)^3\). For fixed
\(\tau\), the exceptional probability in (21) is therefore
\[
                 O_\tau\bigl(Y^{1-2\kappa+o(1)}\bigr)=o(1).
\tag{30}
\]
In particular, for the declared \(2/3<\kappa<1\), both
energies are \(\gg Y^{3\kappa-1}/(\log Y)^3\) on the entire
band with probability tending to one. The superlinear energy floor
is not supported only by rare large-energy realizations. This is a
finite-ensemble statement as the block scale grows, not an almost-sure
claim about one infinite family of interacting prescribed blocks.

## Prior art, controls, and evidence boundary

Multiplicative propagation of a balanced prime primitive is already
explicit in [MC-118](MC-118-balanced-prime-block-multiplicative-fractional-moment-barrier.md).
That finding bounds sub-\(L^1\) mass of the copies; it does not give
the centered window second-moment floor here. MC-538 uses a uniform
upper moment bound, and MC-541 computes its sharp norm. The added
conclusion is the isolated free-prime component (13), its exact
survival under empirical centering, and its cost for the actual
window and signed smooth weights.

[Harper, Section 1](https://msp.org/ant/2019/13-10/ant-v13-n10-p02-s.pdf)
(MC-S88) supplies the classical Rademacher model. Orthogonality of
products of independent signs is classical (MC-S94); (10)–(11)
derive the needed specialization. A closely related conditional
interval-variance decomposition appears in
[Harper–Soundararajan–Xu, Section 2, equation (2.1)](https://arxiv.org/html/2606.29040v1#S2)
(MC-S95), with smooth/rough factor grouping in a Steinhaus ensemble.
Their distributional and concentration conclusions are not imported
into this prescribed-sign Rademacher setting. The only prime-supply
input for (19) is the ordinary [PNT](https://dlmf.nist.gov/27.12)
(MC-S89). No new orthogonality, summation-by-parts, prime-counting,
or external novelty claim is made.

[Lewko–Lewko, Theorem 1](https://arxiv.org/html/1106.0871v2#S1)
(MC-S96) states the classical Rademacher–Menshov maximal inequality.
The proof of (24) supplies its needed finite variant directly, since
prescribing prime values destroys orthogonality of some integer
coefficients. The probability upgrade uses only that dyadic argument,
the second-moment estimate, Markov's inequality and the pathwise
isolation (25). MC-118 already selects a small random background at
a prime primitive; here the same strategy isolates its replica in
empirically centered windows and controls the whole scale band on
one event. No new concentration theorem is claimed.

The limitations are consequential:

* The expectation and probability are over the free prime signs.
  Equation (21) does not rule out exceptional realizations with
  smaller energy. It is useful only when its displayed error is
  small; arbitrary balanced sign orders need not meet that condition.
  No almost-sure statement across growing prescribed blocks follows.
* The observation band is comparable to one isolated source block.
  The condition \(Q_0<Y\) is sufficient to remove all older divisors
  from the isolated profile. No such isolation is proved for an
  arbitrary dense infinite family of prescriptions. The result does
  not establish a dense-scale multiplicative counterexample or its
  impossibility.
* Three must remain free. Prescribing or zeroing it destroys this
  particular random character argument; a different multiplier
  would require fresh isolation and support checks.
* Balance, full inclusion of both pulse supports, and \(L\ge3w\)
  are used in (16). Without them the exact zero mean and separated
  norm identity are not asserted.
* Complete energy can be large while sparse observations miss its
  localized contribution. The result does not contradict MC-538,
  improve Möbius estimates, or establish optimal sampling for RH.

The remaining route must select exceptional backgrounds that cancel
the replicas, pay to remove them, or prove additional interactions
between non-isolated blocks. Simply replacing arbitrary weights by
intervals and fitting their means gives neither uniformly small
expected energy nor typically small energy for the isolated ordered
blocks in this admissible class.

Exact finite checks used three actual prime blocks at source scales
100, 240 and 1,000, all 28 balanced sign patterns on those blocks,
and old sets empty, {2}, and {2,5,7} with every sign assignment.
Four free primes {3,13,17,19} were exhaustively averaged; other
nonprescribed primes within each horizon were zeroed. Across 308
configurations and 1,848 scale/channel cases, 29,568 direct
multiplicative realization/window cases verified (11), both forms of
centering, the lower bound, and 4,404,356 entries of (13). The
checks also verified (16) including the equality case of pulse
separation, (17) for ordered signs, and rational-weight versions of
(18). They check finite bookkeeping; the proof establishes the
ensemble bound with unrestricted remaining free primes and the
asymptotic consequence (19).
No Lean verification or independent adversarial approval is asserted.
The finite orthogonality/translation calculation alone does not
currently justify a separate formalization handoff.

Additional exact-integer checks for (24)–(29) used prime blocks
\(\{269,271\}\), \(\{1069,1087,1091,1093\}\), and
\(\{2671,2677,2683,2687,2689,2693\}\) at scales 200, 800,
and 2,000, all 28 balanced sign orders, and old sets empty, {2},
and {2,5,7} with every sign assignment. Four free primes
{3,11,13,17} were exhaustively averaged; other nonprescribed primes
inside the horizon were zeroed. The audit checked 22,656 full-band
scale/channel geometries, 9,371,120 dyadic blocks over 33 background
ensembles, and 3,015,936 pointwise entries of (25) in 29,568
realization/scale/channel cases. It also checked the exact pairing,
its error bound and the centered Cauchy–Schwarz inequality. These
small examples check identities and maximal-bound bookkeeping;
their maximal-event thresholds did not give a nonvacuous probability
test. The vanishing error in (30) is an analytic consequence of the
proved estimates, not a numerical extrapolation. The classical
maximal estimate does not add a separate formalization target.
