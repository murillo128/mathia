# MC-430 — Exact factor identity has near-linear capacity but a tiny symmetric Möbius-sign quotient

**Evidence:** `EXACT-DERIVED · LITERATURE+DERIVED · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-429` leaves **exact factor identity** outside its subpolynomial state-count obstruction for fixed-dimensional coarse factor summaries. That escape is real at the level of raw combinatorial capacity.

Let `n` be squarefree with

\[
n=p_1\cdots p_r,
\qquad r=\omega(n),
\]

and let `\mathcal U(n)` be the set of unordered active factorizations

\[
n=u_1\cdots u_d,
\qquad u_j>1,
\]

where permuting the factors does not create a new state. Then

\[
\boxed{|\mathcal U(n)|=B_r,}
\tag{1}
\]

where `B_r` is the `r`th Bell number. The bijection is exact: an unordered factorization is the same thing as a set partition of the `r` distinct prime divisors, with each block replaced by the product of the primes in that block.

This capacity is almost polynomially maximal along the squarefree primorial sequence. If

\[
N_r:=\prod_{j\le r}p_j,
\]

then

\[
\boxed{B_r=N_r^{1-o(1)}.}
\tag{2}
\]

Thus the exact factor-identity escape left by `MC-429` genuinely carries a near-linear number of permutation-invariant states at suitable arithmetic inputs. The fixed-depth and coarse-summary obstructions in `MC-423`--`MC-429` must not be extrapolated to full exact factor identity.

However, almost all of this capacity disappears immediately if each exact factor is read only through its Möbius sign. For a partition into `d` blocks, let `k` be the number of odd-cardinality blocks. Then the unordered sign multiset

\[
\{\mu(u_1),\ldots,\mu(u_d)\}
\]

is determined completely by `(d,k)`, and

\[
k\equiv r\pmod 2.
\tag{3}
\]

Across all active depths `1\le d\le r`, the number of possible permutation-invariant Möbius-sign states is therefore at most

\[
\boxed{
\sum_{d=1}^r(d+1)=O(r^2).
}
\tag{4}
\]

For squarefree `n\le X`, `r=O(\log X/\log\log X)`, so `(4)` is only `X^{o(1)}`. Along the same primorial sequence for which the exact factor identity has `N_r^{1-o(1)}` states, its symmetric Möbius-sign quotient has only polylogarithmically many states.

The consequence is a sharp capacity/semantics split:

> **Full exact factor identity escapes the state-volume barrier, but it does so by retaining the actual prime-block incidence information. Möbius sign alone still collapses that near-linear state family to a subpolynomial quotient.**

This does not yield cancellation for `M(x)`. It instead identifies the price of the surviving escape from `MC-429`: any useful factor-lift mechanism must exploit actual factor identities or comparably rich relational arithmetic before the sign projection. Merely retaining more exact factorizations while eventually using only the factorwise values `mu(u_j)` cannot convert the raw Bell-number capacity into polynomial Möbius-source complexity.

## 1. Exact unordered factorizations are set partitions

Because `n` is squarefree, every divisor of `n` is the product of a unique subset of the prime set

\[
P=\{p_1,\ldots,p_r\}.
\]

Given an unordered active factorization

\[
n=u_1\cdots u_d,
\]

the sets of prime divisors of the `u_j` are nonempty, pairwise disjoint, and have union `P`. Hence they form a set partition of `P`.

Conversely, if

\[
P=A_1\sqcup\cdots\sqcup A_d
\]

is a set partition, define

\[
u_j:=\prod_{p\in A_j}p.
\]

Unique factorization makes these two operations inverse to each other. Since factor order is ignored on one side and block order is ignored on the other, the correspondence is exact after the same permutation quotient. This proves `(1)`.

This is different from `MC-079`. There the word *prime partition* classifies how the **global prime set is assigned among Dirichlet-convolution factors of the arithmetic function `mu`**. Here the object is the multiplicative partition of **one squarefree integer** into integer factors. The common set-partition language does not identify the two constructions.

## 2. Bell capacity is near-linear along primorials

Only a coarse Bell estimate is needed. The trivial encoding of a set partition by a map from an `r`-element set to at most `r` labels gives

\[
B_r\le r^r,
\qquad
\log B_r\le r\log r.
\tag{5}
\]

For a matching exponent-scale lower bound, let

\[
m=\lfloor\log r\rfloor,
\qquad
q=\lfloor r/m\rfloor,
\qquad
b=r-qm<m.
\]

Count only those set partitions having `q` blocks of size `m` and, when `b>0`, one residual block of size `b`. Their number is

\[
\frac{r!}{(m!)^q q!\,b!}
\tag{6}
\]

(with the factor `b!` omitted when `b=0`). Stirling's formula and the elementary bounds `m!\le m^m`, `q!\le q^q` give

\[
\log B_r
\ge
r\log r-r\log\log r-O(r).
\tag{7}
\]

Combining `(5)` and `(7)`,

\[
\boxed{\log B_r=(1+o(1))r\log r.}
\tag{8}
\]

For the primorial `N_r`, the prime number theorem and `p_r\sim r\log r` give

\[
\log N_r=\vartheta(p_r)=(1+o(1))r\log r.
\tag{9}
\]

Equations `(8)` and `(9)` prove `(2)`.

The point is not a new asymptotic for Bell numbers. Much sharper classical Bell asymptotics are known. The self-contained estimate above is retained only because it isolates exactly the exponent-scale fact needed by the Mathia frontier: quotienting factor-slot order does **not** make full exact factor identity subpolynomial.

## 3. The symmetric Möbius-sign projection destroys the Bell capacity

Let one exact factor state correspond to a partition with block sizes

\[
s_1,\ldots,s_d,
\qquad
s_1+\cdots+s_d=r.
\]

Because each factor is squarefree,

\[
\mu(u_j)=(-1)^{s_j}.
\tag{10}
\]

After factor-slot permutations have been quotiented, the sign state remembers only how many block sizes are odd. If that number is `k`, the sign multiset consists of `k` copies of `-1` and `d-k` copies of `+1`.

Moreover,

\[
r=\sum_j s_j\equiv k\pmod2,
\]

which gives `(3)`. For a fixed `d`, there are at most `d+1` choices of `k`, and summing this crude upper bound over every possible depth gives `(4)`.

The bound is deliberately generous: not every pair `(d,k)` satisfying the parity condition is realizable, because nonempty even blocks have size at least two. That only reduces the quotient further.

`MC-425` gave the corresponding obstruction before quotienting factor order: ordered factorwise sign vectors across all depths form only `X^{o(1)}` states. The present result sharpens the exact setting left by `MC-429`: under its permutation-invariant factor-slot convention, the sign quotient has only `O(r^2)` states even though the full factor identity has `B_r` states.

The total product sign is even less informative:

\[
\prod_{j=1}^d\mu(u_j)=\mu(n)=(-1)^r
\tag{11}
\]

for every exact factorization of the same squarefree `n`. Thus none of the Bell multiplicity is visible in the aggregate Möbius phase.

## 4. Relation to the MC-423--MC-429 capacity frontier

The recent factor-lift sequence now has a clean separation.

`MC-423` proves that one exact-product fiber at **fixed depth** is subpolynomial. `MC-424` shows that fixed-depth factorization cannot amplify the exponent of a short product shell and quantifies how growing depth may restore raw state volume. `MC-425` proves that growing depth still does not create polynomially many ordered Möbius-sign channels. `MC-426`--`MC-429` then show that bounded-dimensional additive or coarse factor summaries remain subpolynomial unless their resolution becomes correspondingly expensive.

The present result resolves the explicit full-identity escape left by `MC-429` in the opposite direction:

\[
\text{coarse symmetric factor summary}
\quad\Longrightarrow\quad X^{o(1)}\text{ states},
\]

whereas along primorials

\[
\text{full exact unordered factor identity}
\quad\Longrightarrow\quad X^{1-o(1)}\text{ states}.
\]

So state capacity itself is no longer the obstruction once full factor identity is retained. The obstruction moves to **what analytic observable uses that identity without simply carrying a near-lossless copy of the original prime incidence data**.

That distinction is essential. Exact factor identity can distinguish Bell-many partitions because it remembers which specific primes occur together in each factor. If a proposed mechanism subsequently forgets those identities and keeps only sign, bounded additive summaries, or another coarse permutation-invariant statistic, the previous barriers reappear at the corresponding quotient.

## Representation-match map

The same statement can be seen through the repository representation lenses without changing the mathematics.

- **Affine/system view:** for a fixed depth, use Boolean variables `x_{ij}` recording whether prime `p_i` belongs to factor block `j`, with `x_{ij}^2=x_{ij}` and `sum_j x_{ij}=1`; active blocks are nonempty.
- **Ideal view:** the Boolean one-hot relations generate the natural incidence ideal. They describe labeled factor slots before quotienting their artificial order.
- **Quotient/symmetry view:** the symmetric group on factor slots permutes columns of the incidence matrix. Its orbits are exactly set partitions, hence Bell-number states when depth is allowed to vary.
- **Elimination view:** eliminating prime-incidence data down to factorwise Möbius signs retains only the parities of column sums; after the same symmetry quotient this collapses to the pair `(d,k)` and therefore `O(r^2)` states.
- **Matrix/rank view:** ordinary matrix rank is not the controlling invariant here. The decisive change is orbit information lost under the parity projection, not linear dependence of the raw incidence columns.

This map is diagnostic rather than a second proof: it makes explicit that the large capacity comes from retaining prime-block incidence, while the Möbius projection is an aggressive quotient of that information.

## Prior art and novelty boundary

Unordered integer factorizations are the classical *factorisatio numerorum* or multiplicative-partition problem. Canfield, Erdős and Pomerance, *On a Problem of Oppenheim concerning “Factorisatio Numerorum”*, Journal of Number Theory **17** (1983), 1--28, define `f(n)` as the number of unordered factorizations into factors larger than one and prove a near-linear maximal-order scale for highly factorable integers. Their result independently confirms that multiplicative-partition state counts can reach `n^{1-o(1)}`; no novelty is claimed for that phenomenon.

Hughes and Shallit, *On the Number of Multiplicative Partitions*, American Mathematical Monthly **90** (1983), 468--471, is another classical entry point for the same counting problem. Bell-number asymptotics themselves are much older; Moser and Wyman, *An asymptotic formula for the Bell numbers*, Transactions of the Royal Society of Canada, Series III **49** (1955), Section III, 49--54, gives a classical sharp treatment. None of those classical counting results is claimed as new here.

The Mathia contribution is the **frontier consequence** relative to `MC-423`--`MC-429`: full exact factor identity is a genuine high-capacity escape from the recent coarse-factor state-count no-go results, while the natural permutation-invariant Möbius-sign projection of the same state family remains only `X^{o(1)}`. This identifies precisely where the missing information lives.

## Boundaries and falsification tests

- **Squarefreeness is load-bearing for the Bell bijection.** Repeated prime powers lead to multiplicative partitions of a multiset of exponents rather than ordinary set partitions. The broader factorisatio-numerorum literature covers that setting, but `(1)` is intentionally squarefree.
- **Exact factor identity is load-bearing for the large capacity.** Replacing each factor by a bounded-dimensional coarse summary returns to `MC-426`--`MC-429`.
- **Permutation invariance is built in.** Ordered factor tuples have still more nominal states; the Bell count shows that polynomial-scale capacity survives after removing that artificial slot order.
- **Capacity is not cancellation.** `B_r=N_r^{1-o(1)}` says only that many arithmetic states exist. It supplies no orthogonality, no usable coefficients, no mean-value theorem, and no bound for `M(x)`.
- **The sign quotient is specific.** Richer exact functions of the factors -- residues, gcd/lcm relations, cross-factor characters, or transformed phases -- need separate counting and analytic audits. They are not ruled out by `(4)`.
- **Near-lossless representations are not automatically explanatory.** A mechanism that succeeds only because exact factor identities preserve essentially all prime-incidence information must still show an analytic operation that creates cancellation rather than merely re-encoding the input.
- **No zero information or analytic continuation is used.** The derivation is finite unique-factorization combinatorics plus the prime number theorem for the primorial scale.

## Consequence for the research line

The exact-identity branch should no longer be rejected on state-count grounds: it has ample capacity. But the source of that capacity is now explicit and adversarially expensive -- it is the full set-partition incidence of the prime divisors.

The next useful test is therefore not to count still more exact factorizations. It is to identify the **weakest genuinely relational quotient of exact factor identity** that (i) retains polynomially many states after factor-slot symmetry, (ii) is substantially smaller than a near-lossless encoding of the prime partition, and (iii) supports a signed analytic operation not already reduced by `MC-425`--`MC-429`. If no such intermediate quotient survives, the Bell-capacity escape is combinatorial rather than a cancellation mechanism.