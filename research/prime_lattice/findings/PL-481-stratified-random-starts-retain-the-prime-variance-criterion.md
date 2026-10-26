# PL-481 — Stratified random starts retain the prime criterion with cube-root-many observations

**Evidence/status:** LITERATURE+DERIVED / EXACT CONDITIONAL TRANSFER;
CLASSICAL STRATIFIED QUADRATURE; NO EXTERNAL NOVELTY CLAIM.
Randomness concerns observation locations, not prime coefficients.
No arithmetic sample-energy ceiling or unconditional zero exclusion is proved.

## Claim and probability quantifiers

For each integer \(X\ge40\), set
\[
 a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
 S_L(j)=\sum_{j<n\le j+L}a_n,\qquad I_X=\{X,\ldots,2X-1\},
\]
\[
 H_X=\lfloor X/20\rfloor,\quad L_1=H_X,\quad
 L_2=\lfloor\sqrt2 H_X\rfloor,\quad q_X=\lceil X^{1/3}\rceil.
\tag{1}
\]
Partition \(I_X\) into the balanced consecutive cells
\[
 B_{X,b}=\{X+\lfloor(b-1)X/q_X\rfloor,\ldots,
               X+\lfloor bX/q_X\rfloor-1\},\qquad 1\le b\le q_X.
\tag{2}
\]
Choose one uniform integer \(R_{i,X,b}\) in each cell, independently
across cells, channels and scales. The product sampling law is fixed
independently of all prime values and zeros. Define the ordinary
sample-centered energies
\[
 Q_i(X)=\min_{c\in\mathbb R}\sum_{b=1}^{q_X}
                |S_{L_i}(R_{i,X,b})-c|^2,\qquad i=1,2.
\tag{3}
\]

There is an event \(\Omega_*\) of probability one such that, on
each outcome in \(\Omega_*\), **joint GRH for zeta and the three
primitive nonprincipal Dirichlet functions modulo 5 is equivalent to**:
there exists one unbounded set \(\mathcal X\) of integer scales on
which, for every \(\varepsilon>0\),
\[
 \boxed{Q_i(X)/q_X\ll_{\varepsilon,\omega}X^{1+\varepsilon},
       \qquad i=1,2.}
\tag{4}
\]
The set may depend on the observed outcome \(\omega\), but is common
to both channels and fixed before epsilon varies. Constants and
thresholds may depend on epsilon and the outcome, uniformly along
that set. The source itself is fixed before all draws.

More precisely, for each hypothetical nontrivial zero
\(\rho=\beta+i\gamma\), \(\beta>1/2\), of any of these four
functions, almost surely at every sufficiently large integer scale,
\[
 \boxed{\sum_{i=1}^2\sqrt{Q_i(X)/q_X}
       +\log(3X)\bigl[X^{1/3}+\sqrt{X\log X}\bigr]
       \gg_\rho X^\beta.}
\tag{5}
\]
The implied constant depends on the full hypothetical zero set through
the analytic test; the onset can additionally depend on the outcome.
There is no logarithmic factor from zero multiplicity on the right.

This changes the deterministic square-root grid of
[[research/prime_lattice/findings/PL-478-geometric-coverage-retains-sparsely-sampled-prime-variance|PL-478]]
to cube-root-many random starts per channel with an almost-sure,
fixed-source guarantee. The finite quadrature mechanism was suggested
by the local Master clue's explicitly authorized source
[[research/mobius_cancellation/findings/MC-536-stratified-random-starts-reduce-the-mobius-variance-sample-exponent|MC-536]],
Sections 1–2. It is reconstructed below. Its Möbius pole formula and
Mertens converse are not inputs to this prime statement.

## 1. Exact removal of a fitted mean and the covariance bias

Let \(u_j\in\mathbb R\), \(j\in I_X\), be deterministic, with
\(|u_{j+1}-u_j|\le A\). For a deterministic
\(f\in C^1([1,2];\mathbb C)\), with \(\int_1^2 f=0\), put
\[
 w_j=\int_j^{j+1}f(y/X)\,dy,\quad
 F=\|f\|_\infty,\quad D=\|f'\|_\infty.
\]
Then \(\sum_jw_j=0\), \(|w_j|\le F\) and
\(|w_j-w_k|\le D|j-k|/X\). For any partition into consecutive
nonempty cells \(B_b\), of sizes \(d_b\), let
\[
 W_b=\sum_{j\in B_b}w_j,\quad
 P=L^{-1}\sum_jw_ju_j,\quad
 \widehat P=L^{-1}\sum_b W_bu_{R_b},
\tag{6}
\]
where \(L>0\) and each \(R_b\) is an independent uniform draw
from \(B_b\). Since \(\sum_bW_b=0\), every common constant
disappears exactly from both pairings. For the estimator this includes
the empirical mean chosen after sampling. With
\(Q=\min_c\sum_b|u_{R_b}-c|^2\), Cauchy–Schwarz gives
\[
 |\widehat P|\le L^{-1}\sqrt{\sum_b|W_b|^2}\sqrt Q
              \le F L^{-1}\sqrt{\sum_b d_b^2}\sqrt Q.
\tag{7}
\]
The test weights are deterministic cell integrals; they require no
further observations of \(u\).

Uniform draws do not make (6) unbiased. Writing out the expectation
and symmetrizing within each cell gives the exact complex identity
\[
 P-\mathbb E\widehat P
 =\frac1L\sum_b\frac1{2d_b}
        \sum_{j,k\in B_b}(u_j-u_k)(w_j-w_k).
\tag{8}
\]
The arithmetic identity
\(\sum_{j,k\in B_b}(j-k)^2=d_b^2(d_b^2-1)/6\) therefore yields
\[
 |P-\mathbb E\widehat P|
 \le\frac{AD}{12LX}\sum_b d_b(d_b^2-1).
\tag{9}
\]
This uses the product of the two within-cell differences, rather than
an uncontrolled absolute level of \(u\).

## 2. Independent observation errors and all-integer-scale control

The deterministic values of \(u\) need not be independent. Only
the draws from different cells are independent. In particular,
\[
 \mathbb E|\widehat P-\mathbb E\widehat P|^2
 =\frac1{L^2}\sum_b|W_b|^2\operatorname{Var}(u_{R_b})
 \le\frac{A^2}{12L^2}\sum_b|W_b|^2(d_b^2-1).
\tag{10}
\]
The inequality follows by writing each variance as the mean squared
pairwise difference divided by two and using the jump bound.
For the required tail estimate set
\[
 \mathcal R^2=\frac{A^2}{L^2}\sum_b|W_b|^2(d_b-1)^2.
\]
Each real coordinate of the \(b\)-th summand in (6) has range length
at most \(A|W_b|(d_b-1)/L\). Applying
[Hoeffding's Theorem 2](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf)
to both tails of each coordinate, at threshold \(t/\sqrt2\), gives
\[
 \Pr\{|\widehat P-\mathbb E\widehat P|\ge t\}
       \le4\exp(-t^2/\mathcal R^2),\qquad t>0.
\tag{11}
\]
If \(\mathcal R=0\), the fluctuation is identically zero.

For a balanced partition with any \(1\le q\le X\),
\(d_{\max}\le2X/q\), \(\sum_bd_b=X\) and
\(\sum_bd_b^2\le2X^2/q\). At \(L\asymp X\), (7), (9) and
(11) give, with constants depending only on a lower bound for \(L/X\),
\[
 |\widehat P|\ll F\sqrt{Q/q},\quad
 |P-\mathbb E\widehat P|\ll AD X/q^2,\quad
 \mathcal R^2\ll A^2F^2X^2/q^3.
\tag{12}
\]

For the prime windows in (1), the exact endpoint identity is
\[
 S_L(j+1)-S_L(j)=a_{j+L+1}-a_{j+1},\qquad
 |S_L(j+1)-S_L(j)|\le\log(3X)=:A_X.
\tag{13}
\]
Both coefficients lie between zero and \(\log(3X)\), so a factor
two is unnecessary. All relevant indices are below \(3X\).

Take \(q=q_X\) and any deterministic sequence of tests with uniformly
bounded \(F,D\). The bias is \(O(A_X X^{1/3})\), and
\(\mathcal R^2=O(A_X^2X)\). With
\(t=C_f A_X\sqrt{X\log X}\) and a sufficiently large fixed
\(C_f\), (11) has failure probability at most \(4X^{-4}\).
Summing over all integer scales and both channels, the first
Borel–Cantelli lemma gives
\[
 |P_i(X)-\widehat P_i(X)|
 \ll_f \log(3X)\bigl[X^{1/3}+\sqrt{X\log X}\bigr]
\tag{14}
\]
almost surely for every sufficiently large integer \(X\).
Independence across scales or between channels is not needed for
this summability argument, although our stated sampling law has both.

## 3. The actual prime pole test and its independent converse

Fix \(\rho=\beta+i\gamma\) and \(1/2<\sigma_0<\beta\).
The destination analytic input is
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]],
Sections 1–3, combined with
[[research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance|PL-475]],
Sections 1–4. They construct a fixed mean-zero
\(\varphi\in C_c^\infty((4/3,5/3);\mathbb C)\) for which
\[
 T_\varphi(X):=\sum_n a_n\varphi(n/X)
 =-w_\rho X^\rho+O_\varphi(X^{\sigma_0}),\qquad
 w_\rho=\tfrac14\sum_\chi m_\chi(\rho)>0.
\tag{15}
\]
The sum includes zeta and the three primitive nonprincipal functions.
The full sparse zero set, not a finite pole packet, is used to
annihilate every other zero to the right of \(\sigma_0\).
Coincident zeros add their positive multiplicities. Logarithmic
derivatives have simple poles even at multiple zeros, explaining the
absence of a reciprocal-zeta multiplicity logarithm in (5).

Put \(h=H_X/X\). The compact two-box inverse supplies deterministic
mean-zero \(f_{1,h},f_{2,h}\), supported in one fixed compact subset
of \((1,2)\), with uniform sup and first derivative bounds, and
\[
 \|A_hf_{1,h}+A_{L_2/X}f_{2,h}-\varphi\|_\infty
 \ll_\varphi X^{-1},\qquad
 A_af(u)=\int_0^1f(u-at)\,dt.
\tag{16}
\]
The error retains the integer rounding of \(\sqrt2 H_X\); no
exact inverse for the rounded rational pair is asserted. Pairing
that error with the prime coefficients costs \(O_\varphi(\log(3X))\).
For integer \(L_i\), \(S_{L_i}(y)\) is constant on
\([j,j+1)\), so the complete pairing in (6) is exactly
\[
 P_i(X)=L_i^{-1}\int_X^{2X}S_{L_i}(y)f_{i,h}(y/X)\,dy.
\]
Finite-sum interchange integrates the test over \([n-L_i,n]\),
including endpoint-crossing windows. Consequently (15)–(16) imply
\[
 |P_1(X)+P_2(X)|\ge\tfrac12w_\rho X^\beta
\tag{17}
\]
for all sufficiently large integer \(X\). The rounding error is
absorbed here. Combining (7), (14) and (17) proves (5).

The quantifiers are important. Fix the actual arithmetic source,
then one analytic test construction per hypothetical strict-right zero,
before any sampling. There are countably many such zeros; intersecting
their probability-one events from (14) defines \(\Omega_*\).
If there are no such zeros, take the full outcome space. No
intersection over all possible sources or all smooth tests is used.
After the outcome is fixed in \(\Omega_*\), any unbounded set
\(\mathcal X\) satisfying (4) is subject to (5) eventually. For
a selected zero choose \(0<\varepsilon<2\beta-1\). Both the
energy contribution \(O(X^{1/2+\varepsilon/2})\) and the recovery
error in (5) are \(o(X^\beta)\), a contradiction on that set.
Functional-equation symmetry within the four-function family gives
joint GRH. This is an implication from the unproved premise (4).

Conversely, joint GRH gives the classical fixed-modulus estimate
\[
 \psi(x;5,1)=x/4+O(\sqrt{x}\log^2(3x)).
\tag{18}
\]
It follows from the character-wise explicit formula and orthogonality;
see [Lee (2023), Corollary 1.1 and its proof](https://arxiv.org/pdf/2301.13457),
source 144. Only this four-function family's GRH is needed.
At any sampled start, both endpoints are comparable to \(X\), and
\[
 |S_{L_i}(R_{i,X,b})-L_i/4|\ll\sqrt X\log^2(3X).
\]
Choosing \(c=L_i/4\) in (3) yields
\(Q_i/q_X\ll X\log^4(3X)\ll_\varepsilon X^{1+\varepsilon}\)
for every sampling outcome and all sufficiently large integer scales.
This proves the converse without transferring a complete mean square
to a sparse sample.

## Prior art, controls and mathematical boundary

The \(q^{-3/2}\) one-dimensional fluctuation rate is classical
stratified quadrature, recalled through Haber's rule in
[Chopin–Gerber, Section 2.1](https://arxiv.org/html/2210.01554v2#S2.SS1),
source 149. Hoeffding's classical inequality, source 150, supplies
the tail bound. The mean-removing discrete estimator here is biased;
(8)–(9) are the exact specialization needed to use these ideas with
an arbitrary fitted constant. None of these probability inputs is a
prime-distribution estimate or new Monte Carlo theory.

Strong prime variance bounds forcing zero-free regions are also
classical: [Zaccagnini (2016), Section 3.3](https://arxiv.org/pdf/1603.02952),
source 123, discusses the Selberg-integral converse. That complete
integral theorem is not being cited as the paired sample-centered
criterion (4). The local mathematical addition is the proved prime
transfer, with the logarithmic jump cost, positive multiplicity
weights, and a separate GRH converse retained. No external priority
claim follows from the literature comparison.

- **Unequal and singleton cells.** Equations (7)–(11) use their exact
  sizes. Singleton cells contribute neither bias nor fluctuation;
  sampling every start gives exact recovery. Balanced cells are needed
  only for the rate in (12). One cell has \(W_1=0\), so a lone
  centered observation is uninformative; its potentially large bias
  is not discarded.
- **Constants and empirical centering.** A constant signal gives zero
  in both pairings exactly. Replacing \(W_b\) by
  \(d_b f(R_b/X)\) generally destroys \(\sum_bW_b=0\).
  Subtracting a fitted mean after that replacement is not justified
  by this proof. Here cancellation precedes concentration.
- **Fixed-source guarantee.** PL-480's deterministic minimax controls
  are chosen against a query transcript. Choosing such a reweighting
  after the draws is outside the probability quantifiers above.
  Thus its inverse-query lower bound and (4) concern different
  guarantees. No randomized minimax lower bound, sample optimality,
  or assertion for every deterministic seed is proved here.
- **Arithmetic selectivity.** The finite quadrature works for any real
  bounded-jump sequence. Rational primes enter through (15) and (18).
  Phase twists, generic multiplicative frequencies and positive
  prime-supported reweightings do not inherit those inputs merely
  by obeying the same jump bound. The overlapping prime windows are
  not treated as independent random variables.
- **Remaining obligation.** Both energy ceilings must hold on the
  same unbounded scale set. Randomly choosing observation locations
  proves neither ceiling. The test constants remain non-effective
  and dependent on the full zero set; there is no zero-uniform onset,
  finite GRH decision procedure, critical-line lower bound, simplicity
  conclusion, relative covariance positivity, or unconditional RH gain.

An exact rational self-check covered 2,005 configurations and all
9,109 joint draws: interval sizes 1 through 6, every balanced cell
count, all increment strings in \(\{-2,0,2\}^{X-1}\), and initial
value 7. The complex test was
\(f(1+t)=(t-1/2)+i(t^2-t+1/6)\). It checked (8), (10), the
bias and range bounds, (7), and exact cancellation of the random
empirical mean. Unequal cells, constant signals and full retention
were included. These finite checks audit quadrature bookkeeping;
the displayed proofs establish the transfer. They do not verify an
arithmetic energy estimate, an asymptotic probability claim, or any
zero location. No Lean verification or independent adversarial
approval is asserted. The elementary covariance/concentration
assembly offers no separate high-value formalization fertility target.
