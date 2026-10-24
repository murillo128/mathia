# RE-262 — Balanced integer Mertens repairs force a prime-chain edge or quadratic support

**Status:** EXACT-DERIVED + FINITE-INTEGER-SOURCE-OBSTRUCTION + CLASSICAL-VALUATION-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-172 (finite prime-supported Mertens rigidity), RE-257 (subdyadic integer-label rigidity), RE-261 (sharp counting norm and its distinct finite/infinite realizations).

RE-261 attains its sharp counting norm with finite integer modifications by replacing each selected prime with two composite labels. Its finite real-label construction preserves the number of labels, while its other integer construction uses an infinite correction. These are materially different hypotheses. The following exact obstruction constrains the missing **finite, count-preserving integer** realization: a nontrivial repair must either use a divisibility relation between deleted primes and their predecessors, or insert an integer divisible by two deleted primes. For deletions in one subdyadic packet, the second mechanism is necessary and forces a quadratic insertion scale.

## 1. Finite Euler-factor rigidity with a counting constraint

For a finite multiset \(B\) of integers at least two, write
\[
\mathscr E(B)=\prod_{n\in B}\frac n{n-1},
\]
with occurrences counted separately. Let \(D\) be a finite set of distinct ordinary primes. Suppose
\[
|B|\le |D|,\qquad \mathscr E(B)=\mathscr E(D),
\tag{1}
\]
and assume both
\[
r\nmid s-1\quad(r,s\in D,\ r\ne s),
\tag{2}
\]
\[
\#\{r\in D:r\mid n\}\le1\quad(n\in B).
\tag{3}
\]
Then
\[
\boxed{B=D\quad\text{as multisets}.}
\tag{4}
\]
No insertion-height bound is assumed, and repeated labels in \(B\) are allowed subject to (1)--(3).

**Proof.** The empty case follows because every factor exceeds one. For each \(r\in D\), distinct prime numerators and (2) give
\[
v_r(\mathscr E(D))=1.
\]
Taking the \(r\)-adic valuation in (1),
\[
\sum_{n\in B}v_r(n)=1+\sum_{n\in B}v_r(n-1)\ge1.
\tag{5}
\]
Thus every prime in \(D\) divides at least one numerator occurrence in \(B\). By (3), each occurrence can serve at most one such prime. The counting constraint forces \(|B|=|D|\), with a bijection \(r\mapsto n_r\) between \(D\) and the occurrences of \(B\), such that \(r\mid n_r\). In particular \(n_r\ge r\). Since \(t/(t-1)\) is strictly decreasing for \(t>1\),
\[
\mathscr E(B)=\prod_{r\in D}\frac{n_r}{n_r-1}
\le\prod_{r\in D}\frac r{r-1}=\mathscr E(D).
\tag{6}
\]
Equality forces \(n_r=r\) for every \(r\), proving (4). Denominator cancellation on the insertion side does not evade (5); it only increases the required numerator valuation. \(\square\)

Equivalently, every nontrivial equality (1) has at least one of the following two features:

- distinct \(r,s\in D\) with \(r\mid s-1\);
- an occurrence \(n\in B\) divisible by distinct \(r,s\in D\), hence \(n\ge rs\).

These are necessary alternatives, not sufficient conditions for an Euler-product identity.

## 2. A subdyadic deletion packet forces quadratic insertion support

Let \(D=\{r_1<\cdots<r_m\}\) consist of odd primes with
\[
r_m<2r_1.
\tag{7}
\]
Then (2) holds automatically. Indeed, if \(r\mid s-1\) for \(r,s\in D\), then \(0<s-1<2r_1\le2r\), forcing \(s-1=r\). But \(r+1>2\) is even and cannot equal the prime \(s\).

Consequently, for \(m\ge2\), (1) implies
\[
\boxed{B\ne D\quad\Longrightarrow\quad\max B\ge r_1r_2.}
\tag{8}
\]
For \(m=1\), (1) is always trivial, regardless of insertion height. In particular, if all inserted labels are below \(r_1r_2\), any nontrivial exact replacement must have **strictly more** insertions than deletions. This is stronger in insertion range than RE-257, at the cost of the new counting and deletion-packet hypotheses: the insertions may range far beyond twice the deletion height before (8) permits a balanced repair.

To translate this to the source class, let \(P\) be the ordinary primes and \(Q\subset\{2,3,\ldots\}\) a distinct-label source with finite symmetric difference from \(P\). Put
\[
D=P\setminus Q,\qquad B=Q\setminus P.
\]
Every member of \(B\) is composite. Finite modification gives the exact identity
\[
\Gamma(Q)-\gamma
=\log\mathscr E(B)-\log\mathscr E(D),\qquad
\Gamma(Q)=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}\log\frac q{q-1}-\log\log x\right).
\tag{9}
\]
Also the eventual counting discrepancy is \(|B|-|D|\). Hence a nontrivial source with \(\Gamma(Q)=\gamma\), nonpositive eventual counting discrepancy, and (7) must contain an inserted label at least \(r_1r_2\).

For a family agreeing with \(P\) through a frontier \(p\), suppose all deletions lie at \(cp+o(p)\) uniformly, where \(c\ge1\) is fixed. If the finite repair satisfies \(\Gamma(Q)=\gamma\), preserves the total count, and is nontrivial, it must have at least two deletions and
\[
\boxed{\max B\ge(c^2+o(1))p^2.}
\tag{10}
\]
Thus it cannot be completed with all insertions on any fixed \(Mp\)-scale. In particular, a finite integer replacement of the three real packets in RE-261, keeping its single deletion packet and equal counts, cannot keep the same fixed-relative support. The finite splitting witnesses of RE-261 instead pay a positive terminal count; their validity is unchanged.

## 3. Exact boundary controls

Both alternatives are real algebraic possibilities, including for distinct composite insertions into the ordinary-prime source.

First,
\[
\frac54\frac{11}{10}=\frac43\frac{33}{32}=\frac{11}{8}.
\tag{11}
\]
Deleting \(5,11\) and inserting \(4,33\) preserves the exact Mertens constant and total count, agrees with the primes through \(3\), and has maximum absolute counting discrepancy one. The insertion numerators share no pair of deleted prime divisors. The escape is \(5\mid11-1\), and the deletion packet is not subdyadic. This rules out a global count-preserving rigidity claim without (2).

Second,
\[
\frac{31}{30}\frac{61}{60}
=\frac{21}{20}\frac{1891}{1890}
=\frac{1891}{1800},\qquad1891=31\cdot61.
\tag{12}
\]
Here \(61<2\cdot31\), and neither deleted prime divides the other's predecessor. The inserted composite \(1891\) attains the precise product threshold in (8). This source agrees with the primes through \(19\), has equal counts, and again has maximum absolute counting discrepancy one. Thus the strict insertion bound cannot be replaced universally by an inclusive bound. This is a finite equality example, not an infinite family of asymptotically sharp counting-norm witnesses.

Finally, dropping the count hypothesis permits the already classical telescoping replacement
\[
\frac54=\frac98\frac{10}{9}.
\tag{13}
\]
It increases the count by one, with no denominator edge or shared numerator. This is the mechanism of RE-261's finite splitting construction. Exact rational arithmetic checks (11)--(13); the proof of (4)--(10) does not depend on a finite search.

## 4. Prior art and research boundary

The proof uses unique factorization, counting incidences, and monotonicity of \(n/(n-1)\); none is a new general method. The relation \(r\mid s-1\) is the classical prime-chain relation studied by K. Ford, S. V. Konyagin and F. Luca, [*Prime chains and Pratt trees*, Geometric and Functional Analysis **20** (2010), 1231--1258](https://arxiv.org/abs/0904.0473), especially Section 1.1. No distribution theorem about those chains is needed here, and no novelty is claimed for that relation. The elementary two-factor identities likewise are not proposed as new Diophantine phenomena.

RE-172 gives rigidity when all labels remain prime. RE-257 allows arbitrary integer labels but confines both sides to a subdyadic interval without a counting hypothesis. RE-261 realizes the sharp norm using finite real labels, infinite integer repair, or finite integer splitting with a positive count offset. None gives (8): a **single subdyadic deletion packet with count nonincrease remains rigid against integer insertions strictly below the product of its two smallest primes**. That source-class restriction, and the exact escape dichotomy behind it, are the mathematical delta. The literature comparison bounds the claim to this derived application; it does not establish a globally new factorization theorem.

The obstruction is exact and finite. It gives no quantitative lower bound for an approximately matched Euler product, does not apply its valuations to an infinite real-convergent product, and imposes no new restriction on actual CA exponent vectors. Multiple deletion packets may contain prime-chain edges and evade (8); quadratic-height insertions may also evade it. Neither escape is shown to attain RE-261's asymptotic sharp norm under finite count preservation. Composite labels remain synthetic Euler atoms, not the ordinary divisor-sum factors of those integers. The CA-selected signed Robin tail and the universal Robin inequality remain unproved.
