# MC-542 — Balanced prime replicas force centered window energy

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`NO-NOVELTY-CLAIM`. The lower bound is over a prescribed-prime random
multiplicative ensemble. It is neither a pointwise lower bound for
every realization nor a statement about actual Möbius sums.

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

The limitations are consequential:

* The expectation is over the free prime signs. It does not rule out
  favorable realizations with smaller energy, and supplies no lower
  probability or almost-sure bound for that energy.
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

The remaining route must control the actual signed background in a
chosen realization, pay to remove the coherent replicas, or prove
additional interactions between non-isolated blocks. Simply replacing
arbitrary weights by intervals and fitting their means does not give
a uniformly small expected energy in this admissible class.

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
