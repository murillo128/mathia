# FD-345 — Exact energy does not repair four reflected Farey defect erasures

**Status:** EXACT-DERIVED + EXACT-FINITE-COUNTEREXAMPLE + ENERGY-CONDITIONED-SPECTRAL-NONIDENTIFIABILITY.

In [[research/farey_discrepancy/findings/FD-344-reflection-makes-three-farey-defect-erasures-recoverable-four-need-not-be|FD-344]]'s reflected whole-excursion reassembly class, retaining the exact
full discrepancy energy does **not** make four known-position defect-value
erasures spectrally identifying. At prime order `p=617`, two reassemblies
have the same complete defective-rank list, agree in every defect value
outside two mirror pairs, and have exactly equal positive Franel energies,
but different normalized Dirichlet sine spectra.

The mechanism is an excursion reversal at a slot whose endpoint
discrepancies sum to zero. It preserves energy by a local signed reversal,
while unequal adjacent gaps change the second moment of the Dirichlet
spectral measure. Everything below concerns the **full reconstructed
discrepancy**, with no transport approximation, rescaling, or limiting
passage. This is a finite control obstruction, not an RH estimate.

For a single mirrored excursion-pair exchange, endpoint balance is also
**necessary** for exact energy equality: a noncentral prime-Farey
excursion cannot have zero intrinsic reversal skew. Moreover, the two
normalized spectra have total-variation distance at most
`sqrt(2/(p E))`. Thus this particular mechanism cannot produce a
nonvanishing asymptotic spectral separation when `p E -> infinity`,
including when the common energy has a positive limit. These restrictions
do not classify general four-erasure collisions.

## 1. Object and energy-preserving reversal

Fix an odd prime `p`, put `n=p-2` and
\[
N=\sum_{q\le p}\varphi(q).
\]
Let `E_j`, `1<=j<=n`, be the genuine Farey denominator-word excursion from
`j/p` to `(j+1)/p`, with `ell_j` gaps. Keep the two outer edges and
reassemble whole excursions in a permutation `sigma`. Each inherited
directed edge `(a,b)` still has gap `1/(ab)`. Define
\[
x_0=0,\quad x_k=\sum_{i=1}^k\frac1{q_{i-1}q_i},\quad
D_k=x_k-\frac{k}{N},\quad E=\sum_{k=1}^{N-1}D_k^2.
\tag{1}
\]
Impose FD-344's reflection law
\[
\sigma(n+1-t)=p-1-\sigma(t).
\tag{2}
\]
Farey reflection reverses the denominator word of `E_j` into that of
`E_(p-1-j)`; their gap counts agree. Thus exchanging these two labels at
mirrored slots preserves (2), every directed-edge multiplicity, and every
excursion slot's rank length. The grids satisfy `D_(N-k)=-D_k`.

Suppose the left slot is the `t`-th excursion slot, starts at rank `r`,
and has length `ell`. Since every excursion has geometric width `1/p`,
its geometric endpoints are `t/p` and `(t+1)/p`. If `y_a`, `0<=a<=ell`,
are its local cumulative gaps, reversal replaces them by
`1/p-y_(ell-a)`. Consequently
\[
D'_{r+a}=C-D_{r+\ell-a},\qquad
C=\frac{2t+1}{p}-\frac{2r+\ell}{N}
  =D_r+D_{r+\ell}.
\tag{3}
\]
The endpoints remain unchanged. In particular the exact balance condition
\[
\boxed{N(2t+1)=p(2r+\ell)}
\tag{4}
\]
makes the interior discrepancy a signed reversal and preserves its squared
norm. The same holds at the mirrored slot; all other coordinates are
unchanged. Hence the two **full** energies agree exactly.

### Necessity of balance for one mirrored pair

The sufficient condition (4) is exact for this operation. Suppose the
left slot contains `E_j`, and put
\[
A_j=\frac{\ell-1}{p}-2\sum_{a=1}^{\ell-1}y_a.
\tag{4a}
\]
Only interior coordinates change. Expanding (3), the energy change at the
left slot is
\[
\sum_{a=1}^{\ell-1}\bigl((D'_{r+a})^2-D_{r+a}^2\bigr)
=C\left((\ell-1)C-2\sum_{a=1}^{\ell-1}D_{r+a}\right)
=C A_j.
\tag{4b}
\]
The last equality uses
`D_(r+a)=t/p-r/N+y_a-a/N`; the rank and placement terms cancel.
At the reflected slot, both `C` and `A_j` change sign, so the complete
energy change is
\[
\boxed{E^{\mathrm{after}}-E^{\mathrm{before}}=2C A_j.}
\tag{4c}
\]

To rule out an unbalanced cancellation, let `f_a=j/p+y_a` be the genuine
fractions strictly inside `E_j`. Their reduced denominators are all
strictly less than `p`. Each denominator contributes at most one such
fraction to an interval of length `1/p`, so `ell<=p`. Also `ell>=2`:
otherwise the two endpoints, whose determinant is `p`, would be adjacent
Farey fractions, contrary to the determinant-one neighbor relation.
Consequently `1<=ell-1<p`. In the ring of rationals with denominator
coprime to `p`,
\[
p A_j=(\ell-1)(2j+1)-2p\sum_{a=1}^{\ell-1}f_a
\equiv(\ell-1)(2j+1)\pmod p.
\tag{4d}
\]
For `1<=j<=p-2`, this residue vanishes only when
`j=(p-1)/2`. That central excursion has `A_j=0` by reflection and is
fixed in the central slot under (2); exchanging it with its mirror does
nothing. Every nontrivial mirrored pair therefore has `A_j!=0`, and
(4c) proves
\[
\boxed{E^{\mathrm{after}}=E^{\mathrm{before}}
\quad\Longleftrightarrow\quad N(2t+1)=p(2r+\ell).}
\tag{4e}
\]

For a left slot `1<=t<=(p-3)/2`, `2t+1` is not divisible by `p`.
Thus a nontrivial single-pair energy collision requires `p|N`.
Since `N` is even and `p` is odd, `N/p` is then even, and (4) also
requires `ell` even. Neither divisibility nor evenness alone supplies a
realizable balanced rank. This necessity applies only to one mirrored
excursion-pair exchange: several changes can have compensating energy
increments, and a multi-excursion block exchange is a different operation.
No condition on every possible equal-energy collision is asserted.
Balance alone also does not guarantee an identical defective-rank list:
the changed seam values must remain noninteger, as checked in Section 2.

## 2. A realizable certificate at order 617

Take
\[
p=617,\qquad N=115996=188p,\qquad (p-1)/2=308.
\tag{5}
\]
Define the list `R` to be the increasing list of all integers from `5` to
`307` except `136` and `153`. The two left-half lists are
\[
A=(1,153,136,2,4,3,R),\qquad
B=(1,153,136,614,4,3,R).
\tag{6}
\]
For a list `L=(L_1,...,L_307)`, define the full permutation
\[
\mathcal P(L)=(L_1,\ldots,L_{307},308,
              616-L_{307},\ldots,616-L_1).
\tag{7}
\]
Set `sigma=P(A)` and `tau=P(B)`. Each is a permutation of `1,...,615`
and satisfies (2). They exchange only the excursions `E_2` and `E_614`
at mirrored positions. No labels, gaps, or excursions are added.

The genuine gap counts needed for the balance are
\[
\ell_1=309,\qquad\ell_{153}=227,\qquad
\ell_{136}=206,\qquad\ell_2=\ell_{614}=206.
\tag{8}
\]
The changed left slot has
\[
t=4,\qquad r=1+309+227+206=743,\qquad\ell=206.
\]
Thus `2r+ell=1692=9*188`, proving (4), and explicitly
\[
D_{743}=9/115996,\qquad D_{949}=-9/115996.
\tag{9}
\]
Equation (3) proves `E^sigma=E^tau`. This common energy is positive because
the unchanged coordinate `D_1=1/617-1/115996` is nonzero.

At each noninteger inherited index
`nu_k=(q_(k-1)+q_(k+1))/q_k`, write `d_k=p(nu_k-1)`.
The complete **left-half** signature is:

| Defective rank | `d^sigma` | `d^tau` |
|---:|---:|---:|
| 310 | 63 | 63 |
| 537 | 182 | 182 |
| 743 | 299 | 197 |
| 949 | -257 | -155 |
| 1134 | 41 | 41 |
| 1341 | 216 | 216 |
| 26002 | -177 | -177 |
| 28999 | -367 | -367 |

The right half is obtained by `r -> N-r` with **equal** numerators,
listed in increasing rank order. There are exactly sixteen defects and
no others. Both left-half numerator sums are zero. Erase precisely the
two mirror pairs
\[
\boxed{\{743,115253\},\qquad\{949,115047\}.}
\tag{10}
\]
All remaining values, the full rank list, the erasure locations, the
prime, the original excursion lengths, and the exact positive energy
coincide. The changed seams remain noninteger in both configurations,
so the record does not conceal a dropped or inserted defect.

## 3. Exact spectral separation without evaluating trigonometric numbers

Let `K` be the `(N-1)`-dimensional Dirichlet second-difference matrix,
with diagonal `2` and adjacent entries `-1`. Its orthonormal eigenvectors
and eigenvalues are
\[
s_m(k)=\sqrt{2/N}\sin(\pi mk/N),\qquad
\lambda_m=2-2\cos(\pi m/N),\quad 1\le m<N.
\tag{11}
\]
Put `Dhat_m=<D,s_m>` and `pi_m=|Dhat_m|^2/E`. Orthogonality and the
addition formula for sine give the exact spectral moment identity
\[
\sum_{m=1}^{N-1}\lambda_m^2\pi_m
=\frac{\|KD\|_2^2}{E},\qquad
\|KD\|_2^2=\sum_{k=1}^{N-1}(g_k-g_{k+1})^2,
\quad g_k=\frac1{q_{k-1}q_k}.
\tag{12}
\]
The uniform-grid contribution cancels from `KD`. Reversing the gaps
inside one excursion preserves all its internal squared adjacent-gap
differences. Only its two boundary terms can change. If `a,b` are its
first and last gaps and `L,H` the incoming and outgoing exterior gaps,
then the original-minus-reversed boundary contribution is
\[
(L-a)^2+(b-H)^2-(L-b)^2-(a-H)^2
=2(b-a)(L-H).
\tag{13}
\]
The mirrored block contributes the same amount. In (6), the four
changed seam triples are

| Rank | `sigma` denominator triple | `tau` denominator triple |
|---:|:---:|:---:|
| 743 | `(608,617,308)` | `(608,617,206)` |
| 949 | `(206,617,154)` | `(308,617,154)` |
| 115047 | `(154,617,206)` | `(154,617,308)` |
| 115253 | `(308,617,608)` | `(206,617,608)` |

Therefore
\[
\begin{aligned}
\|KD^\sigma\|_2^2-\|KD^\tau\|_2^2
&=4\left(\frac1{617\cdot206}-\frac1{617\cdot308}\right)
     \left(\frac1{617\cdot608}-\frac1{617\cdot154}\right)\\
&=\boxed{-\frac{11577}{141348948592544}\ne0.}
\end{aligned}
\tag{14}
\]
Since the denominators `E` in (12) are exactly equal and positive,
(14) proves that **at least one same-index normalized squared sine
coefficient differs**. This is an exact separating spectral moment,
not an inference from merely unequal discrepancy vectors or signed
coefficients. Both grids are reflected, so every odd mode vanishes and
the difference occurs among the even modes. No fixed low mode or
asymptotic spectral separation is claimed.

As an additional control, their first spectral moments coincide:
`<D,KD>=sum_(k=1)^N(g_k-1/N)^2` depends only on the common gap inventory.
Thus the difference in (14) is not total energy, gap energy, global sign,
or rank reversal in disguise.

### Asymptotic limit of the single-pair mechanism

There are only `2(ell-1)` possibly changed coordinates in one mirrored
pair. At each, the old and new positions lie in the same interval of
width `1/p` and have the same rank. Hence, without any approximation,
\[
\|D'-D\|_2^2\le\frac{2(\ell-1)}{p^2}<\frac2p.
\tag{15}
\]
Suppose the energies are equal to `E>0`, as in (4e), and define the two
normalized sine laws as in (11)--(12). Cauchy--Schwarz and orthogonality
give the full-spectrum estimate
\[
\begin{aligned}
\operatorname{TV}(\pi',\pi)
&:=\frac12\sum_{m=1}^{N-1}|\pi'_m-\pi_m|\\
&\le\frac{\|\widehat D'-\widehat D\|_2
               \|\widehat D'+\widehat D\|_2}{2E}
\le\frac{\|D'-D\|_2}{\sqrt E}
\le\sqrt{\frac{2(\ell-1)}{p^2E}}
<\sqrt{\frac2{pE}}.
\end{aligned}
\tag{16}
\]
This bounds every band-mass difference as well as each mode, on the
common absolute mode labels. In particular, an infinite family of these
collisions with `pE->infinity` has vanishing spectral total variation.
If instead `TV>=delta>0` along a family, (16) requires
`E<=2/(delta^2 p)`. The inequality does not prove the existence of such
a small-energy family, infinitely many eligible primes, or a lower bound
on its spectral separation. The positive finite separation in (14) is
fully consistent with (16). General four-erasure pairs can move whole
blocks and need not satisfy the support bound (15).

## 4. Exact audit and reproducibility

The Farey recurrence and a separate reduced-fraction enumeration both
generated the order-617 source. The latter sorted all reduced `a/b` with
`0<=a<=b<=617` using exact rational arithmetic. Reassembly from the actual
denominator words verified (8), every index in the table, the four seam
triples, both directed-edge multisets, endpoint `1`, and reflection.

With `Q=lcm(N,1,2,...,617)`, every `Q D_k` is an integer: consecutive
genuine Farey denominators are coprime, so each inherited denominator
product divides `Q`. Integer summation over both complete grids verified
exactly equal positive energies, (14), equality of the first spectral
moments, and exactly `410` changed discrepancy coordinates. The common
energy is approximately `0.012544345322965967`; the decimal is illustrative
only. The equality proof is (3)--(9), not rounded agreement.

The following compact certificate regenerates the relevant exact data;
it requires only Python's standard library and contains no stored search
output or dependence on an ephemeral script:

```python
from collections import Counter
from fractions import Fraction as F
from math import lcm

p = 617
fractions = [(0, 1)]
a, b, c, d = 0, 1, 1, p
while True:
    fractions.append((c, d))
    if c == d:
        break
    k = (p + b) // d
    a, b, c, d = c, d, k*c-a, k*d-b
N = len(fractions) - 1
assert N == 115996
q = [b for a, b in fractions]
cuts = {a: i for i, (a, b) in enumerate(fractions) if b == p}
ell = {j: cuts[j+1]-cuts[j] for j in range(1, p-1)}
assert [ell[j] for j in (1, 153, 136, 2)] == [309, 227, 206, 206]
rest = [j for j in range(5, 308) if j not in (136, 153)]
rank_half = [310, 537, 743, 949, 1134, 1341, 26002, 28999]
expected_ranks = rank_half + [N-r for r in rank_half[::-1]]
Q = lcm(N, *range(1, p+1))
vectors = []
for j, ds in ((2, [63,182,299,-257,41,216,-177,-367]),
              (614, [63,182,197,-155,41,216,-177,-367])):
    left = [1, 153, 136, j, 4, 3] + rest
    sigma = left + [308] + [616-j for j in left[::-1]]
    assert sorted(sigma) == list(range(1, 616))
    word = [1, p]
    for j in sigma:
        word += q[cuts[j]+1:cuts[j+1]+1]
    word += [1]
    assert word == word[::-1]
    assert Counter(zip(word, word[1:])) == Counter(zip(q, q[1:]))
    signature = [(k, word[k-1]+word[k+1]-p) for k in range(1, N)
                 if (word[k-1]+word[k+1]) % word[k]]
    assert all(word[k] == p for k, _ in signature)
    assert signature == list(zip(expected_ranks, ds+ds[::-1]))
    position, v = 0, [0]
    for k in range(1, N+1):
        product = word[k-1]*word[k]
        assert Q % product == 0
        position += Q // product
        v.append(position-k*(Q//N))
    assert position == Q and v == [-z for z in v[::-1]]
    vectors.append(v)
v, w = vectors
assert sum(z*z for z in v) == sum(z*z for z in w) > 0
assert all(w[743+k] == -v[949-k] for k in range(207))
moment = lambda v: sum((2*v[k]-v[k-1]-v[k+1])**2
                       for k in range(1, N))
assert F(moment(v)-moment(w), Q*Q) == F(-11577, 141348948592544)
```

Exact complete enumeration at `p=7,11,13,17` also tested respectively
`8,384,3840,645120` reflected permutations. At each of these four primes,
no two distinct members had both the same full rank list and the same
energy. This finite absence does not extend to all primes, as (5)--(14)
demonstrate. No minimality claim for `617` is made. No Lean verification
or independent adversarial approval is claimed.

For (4a)--(4e), an additional exact rational audit sorted all reduced
fractions at primes `7,11,13,17,19,23,29,31,43,61,101`. All `333`
excursions had zero `A_j` exactly at the central label and satisfied
(4d). Four reflected permutations per prime, generated by shuffling the
left-half labels and independently choosing each orientation with Python
`Random(345)`, were checked at the distinct slots in
`{1,max(1,h//2),h}`, `h=(p-3)//2`. These `128` mirrored reversals verified
(3), (4c), (4e), and the exact squared-distance bound (15), using full
gap reconstruction and rational energies. The order-617 certificate
above was also rerun successfully. The universal assertions follow
from the displayed proofs; these finite checks test signs, mirror
factors, central degeneracy, and endpoint conventions.

## 5. Prior art and consequence

The index `nu=(q_-+q_+)/q` is classical: R. R. Hall and P. Shiu,
*The index of a Farey sequence*, Michigan Mathematical Journal **51**(1)
(2003), 209--223, [DOI](https://doi.org/10.1307/mmj/1049832901).
[[research/farey_discrepancy/findings/FD-331-joint-farey-defect-ranks-and-values-invert-all-excursion-permutations|FD-331]] and FD-344 already supply the full-signature inverse and the
three-erasure guarantee. Their identities and the reversal isometry of
Euclidean norm are not claimed as new.

The sine eigenbasis of the Dirichlet second-difference matrix is standard;
see Gilbert Strang, *The Discrete Cosine Transform*, SIAM Review **41**(1)
(1999), 135--147, §§1--2,
[publisher text](https://epubs.siam.org/doi/10.1137/S0036144598336745).
Equations (11)--(14) specialize that classical spectral calculus and
derive the separating moment directly.

The conversion from vector error to total variation in (16) is classical
square-root-density/Cauchy--Schwarz stability; compare Alison L. Gibbs
and Francis Edward Su, *On choosing and bounding probability metrics*,
International Statistical Review **70**(3) (2002), 419--435, §3,
equation (8), [primary preprint](https://arxiv.org/abs/math/0209021).
The proof here is included to fix the normalization and its dependence
on `E`. It is not a new probability-metric inequality. The specific
additional boundary is the prime-denominator obstruction (4d), which
makes balance necessary for this realizable single-pair operation,
combined with its localized spectral cost (15).

General Fourier magnitude ambiguities are neighboring, but different,
prior art: Robert Beinert and Gerlind Plonka, *Enforcing uniqueness in
one-dimensional phase retrieval by additional signal information in time
domain*, Applied and Computational Harmonic Analysis **45**(3) (2018),
505--525, [DOI](https://doi.org/10.1016/j.acha.2016.12.002).
That literature studies recovery from Fourier intensities and additional
signal data. Here the input is a partially erased, realizable Farey
signature plus scalar energy, and the output shown nonidentifiable is
the intensity distribution itself. A generic phase-retrieval ambiguity
would not establish this certificate.

The local delta is a realizable **reflection-, rank-, retained-value-,
directed-edge-, and exact-energy-matched pair with different normalized
sine spectra**, together with its balanced-reversal mechanism. Targeted
comparison with Farey index/permutation literature, reversal symmetries,
and Fourier ambiguity does not supply a priority claim.

This refutes universal spectral determination for the precise record in
the local energy-conditioned-erasure clue. Retaining total energy does
not repair the four-erasure boundary, even though it distinguishes the
earlier order-seven example. The controls are artificial inherited-label
reassemblies, not alternative genuine Farey sequences. Equations
(4e) and (16) restrict extensions of the displayed mechanism: a single
mirrored reversal must be exactly balanced, and a uniformly separated
normalized spectrum requires common energy of order at most `1/p`.
This leaves asymptotic spectral separation for general energy-matched
four-erasure collisions open. No asymptotic spectral lower bound, new Möbius cancellation, or improvement
to the RH-equivalent Franel bound follows.
