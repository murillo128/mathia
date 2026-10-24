# FD-340 — One erased Farey defect value is recoverable; two need not be

**Status:** EXACT-DERIVED + EXACT-FINITE-COUNTEREXAMPLE + SHARP-UNIFORM-ERASURE-BOUNDARY.

FD-331 reconstructs a whole prime-Farey excursion permutation from the exact ranks and values of all its noninteger inherited Hall–Shiu indices. The complete value list contains one redundant coordinate: its signed defect numerators sum to zero. Consequently, **any one erased value can be recovered exactly**, provided its rank and all other defect ranks and values remain known.

This all-prime guarantee is sharp. At `p=11`, two reassemblies have the same five defect ranks and agree at three of the five values, but have different rational grids, transport energies, and quadratic discrepancy energies. Erasing the other two values makes the records identical. This is a finite identifiability boundary, not an asymptotic energy obstruction or an RH estimate.

## 1. Object, checksum, and recovery theorem

Fix an odd prime `p>=7`, put `n=p-2` and
\[
N=\sum_{q\le p}\varphi(q).
\]
As in FD-320, let `E_j` be the complete directed denominator-`p` excursion in the genuine Farey sequence from `j/p` to `(j+1)/p`, with positive gap count `ell_j`. Reassemble all `E_1,...,E_n` in any permutation `sigma`, keeping the original first and last edges. Inherited edge `(a,b)` retains its positive gap `1/(ab)`. These are labeled-edge controls; inherited labels after a defective join need not be the actual reduced denominators of reconstructed vertices.

Let `I(a)` be the representative of `a^(-1) mod p` in `{1,...,p-1}`. Set `sigma(0)=0` and `sigma(n+1)=p-1`. The exact seam formula is
\[
\nu_t=1+\frac{I(\sigma(t)+1)-I(\sigma(t+1))}{p},
\qquad 0\le t\le n.
\tag{1}
\]
It follows from the neighboring denominator triple
`(I(sigma(t)+1),p,p-I(sigma(t+1)))`. Since `0<nu_t<2`, a seam is integral precisely when its numerator in (1) is zero, equivalently when the labels are consecutive. Every within-excursion index remains integral.

Write the complete noninteger signature in increasing rank order as
\[
\mathcal J_p(\sigma)=((r_1,\nu_1),\ldots,(r_m,\nu_m)),
\qquad d_i=p(\nu_i-1)\ne0.
\]
Then
\[
\boxed{\sum_{i=1}^m d_i=0,\qquad \sum_{i=1}^m\nu_i=m.}
\tag{2}
\]
Indeed, including the zero numerators of consecutive seams does not change the sum. As `t` runs from `0` through `n`, each of the two argument lists `sigma(t)+1` and `sigma(t+1)` is a permutation of `{1,...,p-1}`. The two sums of `I` therefore cancel exactly. No totient estimate or asymptotic input is used. Equation (2) concerns only the noninteger seam indices, not the sum of every Hall–Shiu index along the word.

If the value at the known rank `r_h` is erased, recover it by
\[
\boxed{d_h=-\sum_{i\ne h}d_i,
\qquad \nu_h=m-\sum_{i\ne h}\nu_i.}
\tag{3}
\]
The completed joint signature determines the permutation by FD-331. Explicitly, its first rank fixes the original consecutive prefix by strict cumulative gap-count inversion. Knowing the preceding run's last label `j`, the next numerator fixes the next start `k` through `I(k)=I(j+1)-d_i`. The difference between consecutive defect ranks gives the length of that run, and positivity of the original `ell_j` fixes its endpoint uniquely. Induction reconstructs the word. The final cover and signature checks in FD-331 reject unrealizable records.

Thus, for data promised to come from this class, one erased value loses no information about the reassembly, its grid, or its spectrum. For arbitrary input, (3) gives only a candidate completion: the checksum alone is not a sufficient realizability test. The prime, original excursion lengths, exact full defect-rank list, and location of the erasure are required.

## 2. Exact two-erasure certificate

For `p=11`, `N=42` and the actual excursion lengths are
\[
(\ell_1,\ldots,\ell_9)=(6,4,4,5,2,5,4,4,6).
\tag{4}
\]
Take the two permutations
\[
\sigma=(1,8,3,2,4,5,6,7,9),\qquad
\tau=(1,7,2,8,3,4,5,6,9).
\tag{5}
\]
Both use the same complete directed-edge inventory, preserve both outer edges and endpoint `1`, and have exactly the same five noninteger-index ranks:
\[
\mathbf r=(7,11,15,19,35).
\tag{6}
\]
Their complete numerator vectors are
\[
\mathbf d^\sigma=(-1,1,-3,1,2),\qquad
\mathbf d^\tau=(-2,1,-3,1,3).
\tag{7}
\]
Equivalently, the index vectors are `(10,12,8,12,13)/11` and `(9,12,8,12,14)/11`. Only the values at ranks `7` and `35` differ, each by the least nonzero lattice distance `1/11`. Erasing those two values gives exactly the same observed record. In particular, a known erasure differs from the sub-lattice error guarantee of FD-331 and the six-defect asymptotic example of FD-333.

The following complete denominator words allow direct verification of (4)–(7) and the energy certificate without a permutation search:

```text
sigma:
1,11,10,9,8,7,6,11,4,9,5,11,7,10,3,11,5,9,4,11,8,5,
7,9,11,2,11,9,7,5,8,11,3,10,7,11,6,7,8,9,10,11,1

tau:
1,11,10,9,8,7,6,11,3,10,7,11,5,9,4,11,4,9,5,11,7,10,
3,11,8,5,7,9,11,2,11,9,7,5,8,11,6,7,8,9,10,11,1
```

For either word `q_0,...,q_42`, set
\[
x_0=0,\qquad x_k=\sum_{h=1}^k\frac1{q_{h-1}q_h},
\quad D_k=x_k-k/42,\quad E=\sum_{k=1}^{41}D_k^2.
\tag{8}
\]
All gaps are positive and `x_42=1` exactly. The noninteger values of `(q_(k-1)+q_(k+1))/q_k` give (6)–(7). Rational summation of (8) yields
\[
E^\sigma=\frac{5767}{232848},\qquad
E^\tau=\frac{345481}{12806640},\qquad
\boxed{E^\sigma-E^\tau=-\frac{131}{59290}\ne0.}
\tag{9}
\]
The squared discrepancy-vector distance is
\[
\|D^\sigma-D^\tau\|_2^2=\frac{208111}{64033200}>0.
\tag{10}
\]
As a separate check, FD-320's transport potential gives
\[
T_{11}(\sigma)=\frac{16}{4851},\qquad
T_{11}(\tau)=\frac{232}{53361},\qquad
T_{11}(\sigma)-T_{11}(\tau)=-\frac8{7623}.
\tag{11}
\]
These are finite quantities; no identification of `E` with `T` is made. The two reassemblies are not required to preserve reflection.

## 3. Sharpness and information retained

For fixed `p`, original excursion lengths, and complete defect-rank list, consider the set of realizable numerator vectors. Distinct vectors cannot differ in just one coordinate, by (2). FD-331 ensures that distinct permutations at those ranks have distinct vectors. Equations (6)–(7) attain distance two in this Hamming metric. Therefore **one is the largest number of arbitrary erased values that can be repaired uniformly over this class and all primes**. This does not say that every two-erasure record is ambiguous, or that every prime admits the certificate.

Likewise, an arbitrary single nonzero substitution of a value is detected by the checksum, but cannot always be corrected when its location is unknown. For example, `(-1,1,-3,1,3)` differs in one coordinate from each vector in (7). The distinct completions give the different energies in (9). This is the usual distinction between detection, correction, and known-position erasure recovery; no new general coding principle is asserted.

The result changes the exact sampling contract for the Farey control: all ranks plus all but one value remain fully identifying. All ranks plus all but two values need not even determine scalar energy. It does not turn the joint signature into a stable arithmetic estimate, and the finite witness gives no sequence of ambiguities with a nonzero limiting energy gap as `p` grows. Reflection-restricted two-erasure recovery, corrupted ranks, and unknown or inaccurate excursion lengths are outside this theorem.

## 4. Verification and prior-art boundary

A standard-library audit enumerated all `5!=120` excursion permutations at `p=7` and all `9!=362880` at `p=11`, using the exact genuine gap counts. Every numerator vector satisfied (2). There were respectively `102` and `57752` distinct defect-rank lists. Exhaustive comparison within each rank class gave minimum distinct-vector Hamming distances `3` and `2`. This search locates the certificate, but no all-prime conclusion relies on extrapolating it.

A separate exact-rational reconstruction copied the actual directed denominator words of the genuine `F_11` excursions in the two orders (5). It independently checked the directed-edge multisets, strict ordering, endpoint, all interior indices and their ranks, (9)–(10) by cumulative gap summation, and (11) from excursion counts. The displayed denominator words and formulas retain the complete finite certificate; the exhaustive search is unnecessary to reproduce it. The proof for every prime is (1)–(3) and the finite inversion argument, not computation. No Lean validation or independent adversarial approval is claimed.

The Farey-index formula is classical: R. R. Hall and P. Shiu, *The index of a Farey sequence*, Michigan Mathematical Journal **51**(1) (2003), 209–223, [DOI](https://doi.org/10.1307/mmj/1049832901). FD-320 supplies the exact prime-excursion specialization and FD-331 its complete-signature inverse. The cancellation in (2) is elementary permutation bookkeeping, distinct from the classical first-moment formula summing **all** genuine Farey indices.

Checksum constraints and the Hamming-distance distinction between error detection and correction are classical; see R. W. Hamming, *Error Detecting and Error Correcting Codes*, Bell System Technical Journal **29**(2) (1950), 147–160, [DOI](https://doi.org/10.1002/j.1538-7305.1950.tb00463.x), especially §§2 and 5 ([original-paper scan](https://zoo.cs.yale.edu/classes/cs323/doc/Hamming.pdf)). Here the checksum is an exact integer identity rather than a binary parity constraint, and the realizable signatures form a constrained family, not an asserted linear code.

Targeted comparison with Farey-index moments, permutation/breakpoint reconstruction, and elementary coding theory did not identify the specialized erasure certificate above; that does not establish priority. The line-local delta is the **sharp uniform one-value erasure guarantee with an explicit energy-changing two-value counterexample**. It is not a new Farey recurrence, general coding theorem, asymptotic discrepancy bound, or progress toward RH without additional source-natural arithmetic control.
