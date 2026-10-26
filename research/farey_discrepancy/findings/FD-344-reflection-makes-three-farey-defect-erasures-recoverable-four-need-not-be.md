# FD-344 — Reflection makes three Farey defect erasures recoverable; four need not be

**Status:** EXACT-DERIVED + EXACT-FINITE-COUNTEREXAMPLE + PNT/DIRICHLET-ASSISTED-ASYMPTOTIC + SHARP-REFLECTED-ERASURE-BOUNDARY.

In the reflection-preserving prime-Farey excursion class, the full list of
defective ranks and all but any three defect values determine the reassembly
exactly. Four erased values can already conceal different quadratic
discrepancy energies at order `p=7`. This settles the reflection-restricted
erasure question left open in FD-340. The mechanism is equality of mirrored
values plus the integer checksum, followed by FD-331's exact inverse.
The four-erasure failure also persists at the macroscopic energy scale:
FD-333's existing family, specialized below, gives an infinite-prime
sequence of identical erased records with energy gap tending to
`17/(288 pi^2)>0`.

The result concerns known-position value erasures in inherited denominator
labels. It does not provide stability under perturbed ranks or an estimate
for the genuine Farey discrepancy. The asymptotic pair has unequal energies;
it does not settle asymptotic spectral separation after exact energy is
also retained.

## 1. Reflected signatures and the recovery theorem

Fix an odd prime `p>=7`, put `n=p-2` and
\[
N=\sum_{q\le p}\varphi(q).
\]
Let `E_j`, `1<=j<=n`, be the whole directed denominator-`p` excursion in
the genuine Farey sequence from `j/p` to `(j+1)/p`, with positive gap count
`ell_j`. A permutation `sigma` of these excursions retains the two outer
edges. Every inherited edge `(a,b)` retains gap `1/(ab)`. Impose
\[
\sigma(n+1-t)=p-1-\sigma(t)\qquad(1\le t\le n).
\tag{1}
\]
The full denominator word is then palindromic, and its reconstructed grid
satisfies `x_(N-k)=1-x_k`. This is the precise reflection class used here;
reflection of the reconstructed positions alone is not substituted for (1).

Write `I(a)` for the inverse of `a mod p` represented in `{1,...,p-1}`.
With sentinels `sigma(0)=0`, `sigma(n+1)=p-1`, the seam after label `j`
and before label `k` has inherited Hall–Shiu index
\[
\nu_{j,k}=1+\frac{I(j+1)-I(k)}p.
\tag{2}
\]
It is noninteger exactly when `k!=j+1`. All indices inside each excursion
remain integral. Let the complete noninteger signature, ordered by rank, be
\[
((r_1,\nu_1),\ldots,(r_m,\nu_m)),\qquad
d_i=p(\nu_i-1)\in\mathbb Z\setminus\{0\}.
\tag{3}
\]

**Theorem.** For fixed `p` and the genuine excursion lengths, every valid
signature in class (1) satisfies
\[
\boxed{m=2h,\qquad r_{m+1-i}=N-r_i,\qquad
d_{m+1-i}=d_i,\qquad \sum_{i=1}^{h}d_i=0.}
\tag{4}
\]
The complete exact rank list, erasure locations, and remaining exact values
determine the entire reassembly whenever at most one mirror pair of values
is completely erased. In particular **any three erased values are
recoverable**, uniformly over this class and all primes `p>=7`.

The guarantee of three arbitrary erasures is sharp: Section 3 gives two
members of the class with the same rank list whose value vectors differ in
exactly four coordinates and whose discrepancy energies differ.

## 2. Proof and explicit completion

Reflection takes the seam `j -> k` to
`(p-1-k) -> (p-1-j)`. Since `I(p-a)=p-I(a)`, its numerator is
\[
I(p-k)-I(p-1-j)
=(p-I(k))-(p-I(j+1))=I(j+1)-I(k).
\tag{5}
\]
Thus the values agree, rather than changing sign. The palindromic
denominator word places the reflected seam at rank `N-r`.

There is no noninteger seam fixed by this reflection. Indeed `n` is odd,
and (1) puts the unique self-reflected excursion `E_((p-1)/2)` in the
central position. Its midpoint `1/2` is an interior vertex, not a seam:
its two endpoint fractions have denominator `p`, whereas `1/2` has
denominator `2`. The index at this central vertex remains a genuine
integral index. All seams, including the two outer interfaces, therefore
occur in distinct mirror pairs. This proves the first three assertions
of (4).

For completeness, the checksum of FD-340 follows by summing (2) over
every seam, including those with numerator zero. The two argument lists
`sigma(t)+1` and `sigma(t+1)`, `0<=t<=n`, each run through
`{1,...,p-1}` once, so
\[
\sum_{i=1}^m d_i=0.
\tag{6}
\]
Dividing the paired sum by two gives the last assertion of (4).

To complete a record, pair its ranks by `r <-> N-r`. If at least one
member of a pair is known, copy its numerator to the other member.
If one entire pair remains unknown, choose its left-half representative
`i_0` and set
\[
\boxed{d_{i_0}=d_{m+1-i_0}
=-\sum_{\substack{1\le i\le h\\i\ne i_0}}d_i.}
\tag{7}
\]
Three erasures cannot remove both members of two distinct pairs, so this
procedure completes every such promised-valid record. If `m=0`, there
are no defects and the permutation is the identity.

FD-331 now reconstructs the unique permutation: the first rank identifies
the initial consecutive-label prefix by strictly increasing cumulative
gap counts; at each defect, knowing the preceding run's last label `j`
and `d_i` fixes the next run's first label `k` by
`I(k)=I(j+1)-d_i`. Its known gap count, the difference to the next defect
rank, fixes its endpoint uniquely because all original `ell_j` are
positive. Continuing through the final suffix reconstructs the whole
word. For data not promised valid, cover and recomputed-signature checks
are still necessary; reflection and checksum alone do not prove
realizability.

Equivalently, at a fixed full rank list, two distinct realizable reflected
numerator vectors have Hamming distance at least four. Their left-half
vectors have sum zero and cannot differ in just one coordinate, and each
left-half difference is repeated at its mirror. This is an elementary
distance bound, not a claim that the realizable signatures form a linear
code or that every pattern with two completely missing pairs is ambiguous.

## 3. A complete four-erasure certificate at order seven

For `p=7`, `N=18` and
\[
(\ell_1,\ldots,\ell_5)=(4,3,2,3,4).
\]
Take
\[
\sigma=(2,1,3,5,4),\qquad \tau=(2,5,3,1,4).
\tag{8}
\]
Both satisfy (1). Their full defective-rank list is
\[
\mathbf r=(1,4,8,10,14,17),
\tag{9}
\]
and their numerator vectors are
\[
\mathbf d^\sigma=(-3,4,-1,-1,4,-3),\qquad
\mathbf d^\tau=(-3,2,1,1,2,-3).
\tag{10}
\]
Erasing the values at ranks `4,8,10,14` leaves exactly the same record:
both retain the value `4/7` at ranks `1` and `17`. The erased coordinates
are precisely two complete mirror pairs.

The complete inherited denominator words are small enough to retain:

```text
sigma: 1,7,3,5,7,6,5,4,7,2,7,4,5,6,7,5,3,7,1
tau:   1,7,3,5,7,4,5,6,7,2,7,6,5,4,7,5,3,7,1
```

For either word `q_0,...,q_18`, define
\[
x_0=0,\qquad x_k=\sum_{a=1}^k\frac1{q_{a-1}q_a},\qquad
D_k=x_k-k/18,\qquad E=\sum_{k=1}^{17}D_k^2.
\tag{11}
\]
All gaps are positive, `x_18=1`, and the directed-edge multiset is exactly
that of the genuine `F_7`. Both words and both grids preserve reflection.
The values `(q_(k-1)+q_(k+1))/q_k` directly verify (9)–(10), with no
additional noninteger indices. Exact rational summation gives
\[
E^\sigma=\frac{2911}{52920},\qquad
E^\tau=\frac{635}{10584},\qquad
\boxed{E^\sigma-E^\tau=-\frac{11}{2205}\ne0.}
\tag{12}
\]
Also `||D^sigma-D^tau||_2^2=97/44100`. Thus the ambiguity affects the
transported scalar target, not merely the excursion labels. It establishes
the sharp uniform erasure threshold even within reflection-preserving
controls with identical complete directed-edge and gap inventories.

## 4. Four erased values can hide an order-one limiting energy gap

This is a specialization of the already-proved construction in
[[research/farey_discrepancy/findings/FD-333-one-quantum-fixed-rank-farey-spectral-instability|FD-333]],
not a new reassembly mechanism. It strengthens the same erasure boundary
from finite nonuniqueness to failure of asymptotically vanishing additive
energy recovery.

Let `p>=19` run through primes `p=7 mod 12`, an infinite progression by
Dirichlet's theorem. Put `i=(p+1)/4`, `j=(p-1)/3`, and partition the original
excursion list into the nonempty consecutive blocks
\[
A=E_1\cdots E_{i-1},\quad B=E_i\cdots E_{j-1},\quad
C=E_j\cdots E_{p-j-1},\quad
H=E_{p-j}\cdots E_{p-i-1},\quad R=E_{p-i}\cdots E_{p-2}.
\tag{13}
\]
Their gap counts are `(a,b,h,b,a)` by reflection. Retain the two outer edges
and use the orders `sigma=BACRH` and `tau=HACRB`. Both satisfy (1) and
preserve the same directed-edge inventory. Their complete defective-rank
list and integer numerators are
\[
\begin{aligned}
\mathbf r&=(1,1+b,1+a+b,N-1-a-b,N-1-b,N-1),\\
\mathbf d^\sigma&=(-3,p-4,7-p,7-p,p-4,-3),\\
\mathbf d^\tau&=(-2,p-5,7-p,7-p,p-5,-2).
\end{aligned}
\tag{14}
\]
Indeed the seam formula (2) uses `I(i)=4`, `I(j)=p-3`,
`I(p-j)=3`, and `I(p-i)=p-4`. All six displayed numerators are nonzero;
within each block the indices remain integral. Both orders have the same
slot gap counts `(b,a,h,a,b)`, proving the rank equality without an
asymptotic approximation.

Erase the two mirror pairs
\[
\{1,N-1\},\qquad\{1+b,N-1-b\}.
\tag{15}
\]
The entire observed record agrees exactly. The two retained values, at
`1+a+b` and `N-1-a-b`, both equal `7/p`. Thus this is a four-value erasure
example even though there are six defective ranks; no rank is erased.

Write `E_p^omega=sum_(k=1)^(N-1)(x_k^omega-k/N)^2` for the full
reconstructed energy and `E_p` for the genuine Farey energy. For its limit,
set
\[
x=\frac aN-\frac{i-1}{p},\quad
y=\frac bN-\frac{j-i}{p},\quad
z=\frac hN-\frac{p-2j}{p}.
\]
FD-320's exact block transport, on slots of lengths `(b,a,h,a,b)`, is
`(x,-y,0,y,-x)` for `sigma` and
`(x+y+z,-y,0,y,-x-y-z)` for `tau`. Hence
\[
T_p(\sigma)=2b x^2+2a y^2,\qquad
T_p(\tau)=2b(x+y+z)^2+2a y^2.
\tag{16}
\]
Writing `rho_p(t)` for the number of positive genuine Farey fractions at
most `t`, adjacency to `1/4` and `1/3` gives the exact counts
`a=rho_p(1/4)` and `b=rho_p(1/3)-rho_p(1/4)-2`.
FD-330's PNT-based estimate `rho_p(1/q)=N/q+o_q(p)` and
`N/p^2 -> 3/pi^2`, together with `2x+2y+z=2/p-2/N`, yield
\[
\frac aN\to\frac14,\quad\frac bN\to\frac1{12},\qquad
px\to\frac34,\quad py\to\frac7{12},\quad
p(x+y+z)\to\frac23.
\tag{17}
\]
Both transports in (16) are bounded. FD-318's unconditional genuine
energy bound `E_p=o(1)` and FD-320's exact permutation-plus-transport
decomposition therefore give `E_p^omega-T_p(omega)=o(1)` for these two
orders. Substitution in (16) proves
\[
\boxed{
E_p^\sigma\longrightarrow\frac{19}{24\pi^2},\qquad
E_p^\tau\longrightarrow\frac{211}{288\pi^2},\qquad
E_p^\sigma-E_p^\tau\longrightarrow\frac{17}{288\pi^2}>0.}
\tag{18}
\]
These are full reconstructed energies, not merely transport energies.
The use of PNT is unconditional and supplies no RH-strength rate.

Any scalar estimator `F_p` using only the common erased record must return
the same value on both configurations. Consequently
\[
\liminf_{\substack{p\to\infty\\p\equiv7\ (12)}}
\max\{|F_p-E_p^\sigma|,|F_p-E_p^\tau|\}
\ \ge\ \frac{17}{576\pi^2}.
\tag{19}
\]
Thus even an `o(1)` additive energy guarantee fails uniformly for this
record. The erasure pattern (15) is sufficient for failure; no assertion
is made about every pattern with two missing mirror pairs. Exact energy
as an extra datum distinguishes this family for all sufficiently large
primes. FD-345 separately treats finite spectral ambiguity with energy
retained, and (18) must not be substituted for that stronger matching
condition.

## 5. Audit, prior art, and research boundary

A standard-library exact audit enumerated every permutation satisfying
(1) at `p=7` and `p=11`: respectively `8` and `384` permutations, grouped
into `6` and `66` distinct full defective-rank lists. Every signature
obeyed (4), and the minimum Hamming distance between distinct value vectors
in a common rank class was four at each prime. The all-prime lower bound
is proved above; the enumeration is only a finite check and a way of
locating the displayed certificate.

A separate word-only rational calculation verified both displayed words
against the genuine `F_7` directed-edge multiset. It checked endpoint,
reflection, every interior index, (9)–(12), and the discrepancy-vector
distance without using the modular-inverse seam formula. It also
recovered each numerator vector from all `42` erasure subsets of sizes
zero through three, for `84` exact completions. The displayed words and
(11) make the finite certificate reproducible without the enumeration.
No Lean proof or independent adversarial approval is claimed.

For (13)--(18), an independent exact audit sorted all reduced fractions
`a/b` with `0<=a<=b<=p` for `p=19,31,43,67,79,103,127`, cut the resulting
denominator words into the stated excursions, and reconstructed both
grids from their inherited gaps. It verified reflection, endpoint one,
the directed-edge inventories, every defective rank and value in (14),
the erased-record equality, the exact rational-rank counts, and the
coordinatewise permutation-plus-transport identities underlying (16).
At `p=19`, the common ranks are `(1,10,39,81,110,119)` and the exact full
energy difference is `49440269/132691759200`. These finite checks audit
the construction, not convergence to (18); the latter follows from the
stated PNT inputs and exact transport formulas.

The index itself is classical: R. R. Hall and P. Shiu, *The index of a
Farey sequence*, Michigan Mathematical Journal **51**(1) (2003), 209–223,
[DOI](https://doi.org/10.1307/mmj/1049832901), definition (1.2).
The specialization to excursion seams and the full-signature inverse are
already derived in FD-320 and FD-331. FD-340 supplies the checksum and the
unrestricted one-erasure boundary. None is claimed as new here.

Repetition constraints, checksums, and minimum-distance recovery are
classical coding mechanisms; see R. W. Hamming, *Error Detecting and
Error Correcting Codes*, Bell System Technical Journal **29**(2) (1950),
147–160, §§2 and 5,
[original-paper scan](https://zoo.cs.yale.edu/classes/cs323/doc/Hamming.pdf),
[DOI](https://doi.org/10.1002/j.1538-7305.1950.tb00463.x).
The present integer family is constrained by Farey realizability rather
than binary linearity. The recovery argument is an immediate classical
consequence once the paired seam structure is proved; the additional
local result is that actual reflected Farey reassemblies attain distance
four while changing discrepancy energy. Targeted comparison with
Farey-index reconstruction, reflection, and repetition/checksum erasure
recovery supplies no priority claim for this specialized certificate.

The asymptotic erasure conclusion is an immediate consequence of FD-333's
already-persisted one-quantum instability family. It is integrated here
to make the strength of the erasure obstruction explicit, with no claim
of an independent new construction. Neighboring gap-permutation work,
R. Tomás García, *A General Lower Bound for Average Local Discrepancy and
an Application to the Farey Sequence*, Mathematics **14** (2026), 2543,
§3, [DOI](https://doi.org/10.3390/math14142543), studies average local
discrepancy over a gap-permutation family; that statistic does not supply
the exactly matched defective ranks and retained values used here.

This closes the exact reflection-restricted erasure boundary, rather than
creating a new cancellation channel. The prime, genuine excursion lengths,
all defective ranks, and erasure locations must remain exact. Dropped or
shifted ranks, inaccurate lengths, unknown-location errors, and approximate
reflection are outside the theorem. Equation (18) supplies an order-one
asymptotic separation for a specified four-erasure pattern, but does not
match scalar energy or establish an energy-conditioned asymptotic spectral
gap. Inherited labels at defective stitches need not be actual reduced
vertex denominators, so the controls
are not alternative genuine Farey sequences. No RH-critical estimate or
improved bound on the genuine Franel energy follows.
