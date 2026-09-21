# MC-437 — Möbius divisor convolution extracts only the full prime interaction

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-MECHANISM · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-436` shows that a global relation among the ordered prime divisors of a squarefree integer can carry essentially identity-scale source information: the adjacent-gap rank pattern realizes `(r-1)! = N_r^{1-o(1)}` types. Raw source capacity is therefore no longer enough to kill that branch.

There is, however, an exact and much stricter survival test for any attempt to pass such information through a Möbius divisor convolution.

Let

\[
n=p_1\cdots p_r
\]

be squarefree, with distinct prime set `P={p_1,...,p_r}`. For any arithmetic observable `A` define the induced set function on the Boolean divisor lattice

\[
F_n(T):=A\!\left(\prod_{i\in T}p_i\right),
\qquad T\subseteq[r],
\tag{1}
\]

with the empty product equal to `1`. Then

\[
\boxed{
(\mu*A)(n)
=
\sum_{T\subseteq[r]}(-1)^{r-|T|}F_n(T)
=
\Delta_1\Delta_2\cdots\Delta_r F_n(\varnothing),
}
\tag{2}
\]

where

\[
\Delta_iF(T):=F(T\cup\{i\})-F(T)
\]

for `i\notin T`.

Equivalently, write the unique Boolean-lattice Möbius expansion

\[
F_n(T)=\sum_{S\subseteq T} c_n(S).
\tag{3}
\]

Then

\[
\boxed{(\mu*A)(n)=c_n([r]).}
\tag{4}
\]

Thus arithmetic Möbius convolution at a squarefree source does not measure the number of states retained by `F_n`, nor its injectivity on divisors, nor the size of its lower-order relational family. It extracts exactly the **full `r`-prime interaction coefficient**.

In particular, if `F_n` has Boolean interaction degree at most `k`, meaning

\[
F_n(T)=\sum_{\substack{S\subseteq T\\ |S|\le k}}c_n(S),
\tag{5}
\]

then

\[
\boxed{r>k\quad\Longrightarrow\quad(\mu*A)(n)=0.}
\tag{6}
\]

The same statement holds coordinatewise for vector-valued observables. Increasing the dimension, alphabet size, or raw state count does not help if every retained coordinate is built from interactions involving fewer than all `r` prime factors.

This creates a new frontier gate after `MC-435`--`MC-436`:

> **source diversity and Möbius survival are independent resources. A candidate that has `N_r^{1-o(1)}` source types still contributes nothing through a Möbius divisor convolution unless the downstream observable retains a nonzero full-order interaction.**

No cancellation estimate for `M(x)` follows.

## 1. Exact Boolean-lattice derivation

Every divisor `d|n` is squarefree and corresponds uniquely to a subset `D\subseteq[r]` via

\[
d=\prod_{i\in D}p_i.
\]

In the Dirichlet convolution

\[
(\mu*A)(n)=\sum_{d|n}\mu(d)A(n/d),
\]

put `T=[r]\setminus D`. Since `mu(d)=(-1)^{|D|}=(-1)^{r-|T|}` and

\[
\frac nd=\prod_{i\in T}p_i,
\]

we obtain the first equality in `(2)`.

For a set function on a finite Boolean lattice, the Möbius coefficient attached to `S` is

\[
c_n(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}F_n(T).
\tag{7}
\]

Boolean Möbius inversion gives `(3)`, and setting `S=[r]` in `(7)` gives `(4)` immediately. The alternating sum is also the standard iterated finite difference, proving the second equality in `(2)`.

Now assume `(5)`. The coefficient `c_n([r])` is absent whenever `r>k`, so `(4)` gives `(6)`. No asymptotics, analytic continuation, probability, or zero information is involved.

A direct cancellation proof of `(6)` is also useful. For a single interaction supported on `S\subsetneq[r]`,

\[
G_S(T):=\mathbf 1_{S\subseteq T},
\]

its contribution to `(2)` is

\[
\sum_{T\supseteq S}(-1)^{r-|T|}
=(1-1)^{r-|S|}=0.
\tag{8}
\]

Hence every proper-subset interaction is annihilated, regardless of its coefficient. Only the interaction supported on all prime coordinates can survive.

## 2. Classical generalized von Mangoldt functions are the exact model case

Take

\[
A_k(m):=(\log m)^k.
\]

For a divisor corresponding to `T`,

\[
F_{n,k}(T)
=
\left(\sum_{i\in T}\log p_i\right)^k.
\tag{9}
\]

As a function of the indicator variables `x_i=1_{i\in T}`, `(9)` is a multilinear Boolean polynomial of degree at most `k`: after expanding the `k`th power, no monomial can involve more than `k` distinct prime coordinates. Therefore `(6)` gives

\[
(\mu*\log^k)(n)=0
\qquad\text{whenever}\qquad \omega(n)>k.
\tag{10}
\]

This is exactly the classical support property of the generalized von Mangoldt functions

\[
\Lambda_k:=\mu*\log^k.
\]

For `k=1`, `(10)` is the familiar identity

\[
\mu*\log=\Lambda,
\]

already used in `MC-405`: a squarefree integer with at least two prime factors is annihilated because `log d` contains only first-order prime interactions.

Bombieri's *On twin almost primes*, Acta Arithmetica **28** (1975), 177--193, DOI `10.4064/aa-28-2-177-193`, defines the generalized von Mangoldt weight `A_k=mu*L^k` and records that it vanishes on integers having more than `k` distinct prime factors. The present Boolean-lattice derivation is therefore not a new support theorem; it exposes the structural reason relevant to the current Mathia frontier.

## 3. Large representation capacity does not imply Möbius survival

The gap exposed by `(4)` is stronger than a state-count obstruction. A divisor observable may preserve every divisor state distinctly and still have zero Möbius output.

The simplest example is

\[
A(m)=\log m.
\]

On the divisors of a fixed squarefree `n`, the map

\[
d\longmapsto\log d
\]

is injective, so it distinguishes all `2^r` divisor states exactly. Nevertheless

\[
(\mu*\log)(n)=\Lambda(n)=0
\qquad(r\ge2).
\tag{11}
\]

Thus even **lossless scalar encoding of the divisor identity** can be annihilated by the next arithmetic operation. The reason is not insufficient alphabet size or entropy: `log d` is additive in the prime indicators, so its entire information content lies at interaction order one, while Möbius convolution asks only for the order-`r` coefficient.

More generally, a vector

\[
V_n(T)=\bigl(V_{n,1}(T),\ldots,V_{n,m}(T)\bigr)
\]

may have an arbitrarily large number of coordinates and distinguish an enormous family of states. If every coordinate has Boolean degree at most `k<r`, then

\[
\sum_{T\subseteq[r]}(-1)^{r-|T|}V_n(T)=0
\tag{12}
\]

coordinatewise. Dimension cannot substitute for interaction depth.

This separates three quantities that the recent capacity branch must now keep distinct:

1. **source-type diversity** — how many different arithmetic source structures occur;
2. **representation fidelity** — how much of one source's factor/divisor state is retained;
3. **Möbius interaction depth** — whether the retained observable has a nonzero coefficient on the full prime set.

`MC-430`--`MC-436` primarily constrain the first two. Equation `(4)` shows that a Möbius-facing divisor convolution can ignore both unless the third is present.

## 4. Consequence for the gap-rank escape of MC-436

`MC-436` proved that the global ordering of adjacent selected-prime gaps can realize all `(r-1)!` permutations. That passes the source-capacity gate but says nothing about the coefficient in `(4)`.

To feed the gap relation into a divisor/Möbius mechanism, one must specify a set function on **every sub-divisor** of the source. For example, if `G_n(T)` is a scalar or vector statistic computed from the ordered primes selected by `T`, then its Möbius-facing contribution is

\[
\boxed{
\mathcal I_G(n)
:=
\sum_{T\subseteq[r]}(-1)^{r-|T|}G_n(T).
}
\tag{13}
\]

This is the exact full-interaction coefficient of the induced statistic. A factorial number of possible full-set gap permutations gives no lower bound on `|\mathcal I_G(n)|`, no guarantee that it is nonzero, and no analytic control of its average.

The first survival test for any proposed use of gap order is therefore no longer another permutation count. It is to define the **actual downstream statistic** `G_n(T)` and determine its full Boolean interaction `(13)` before estimating anything.

Several tempting simplifications fail immediately. If the chosen gap observable is replaced by a sum of prime-local terms, a sum of pair terms, or any fixed-order interaction expansion, then `(6)` kills it for sufficiently large `r`. The same is true for any fixed collection of such coordinates. A successful construction must either retain interaction order growing with `omega(n)` or use a different arithmetic operation for which the Boolean top-difference projection is not the relevant survival map.

This does **not** prove that the true gap-rank statistic has zero full interaction. Removing a prime changes adjacency among the remaining primes, so the induced ordinal statistic can genuinely couple many coordinates. Equation `(13)` identifies the quantity that must now be computed or bounded; its nontriviality remains open.

## 5. Relation to earlier obstructions

This result is distinct from the lcm-semiltattice collapse in `MC-404`. There the issue is that arbitrary finite Boolean functions of divisibility predicates can be rewritten through lcm indicators before analytic estimation. Here the divisor lattice of **one squarefree source** is retained deliberately, and the question is what survives convolution by the arithmetic Möbius function. The answer is the top Boolean Möbius coefficient.

It is also distinct from the state-count results `MC-423`--`MC-435`. Those can rule out representations before a Möbius projection because too few source states survive. The present obstruction can kill a representation even when its raw state count is maximal.

Finally, it sharpens the warning in `MC-436` that post-projection survival is mandatory. The warning now has an exact algebraic form for divisor convolution: surviving information must appear in the order-`r` interaction coefficient `(13)`. A large upstream relational alphabet is analytically irrelevant to this operation if it lives entirely in lower interaction degrees.

## 6. Prior art and novelty boundary

The underlying mathematics is classical.

G.-C. Rota's 1964 theory of Möbius functions on locally finite posets established Möbius inversion as the inverse of zeta summation in incidence algebras. On the Boolean subset lattice the Möbius function is `(-1)^{|S|-|T|}`, giving exactly `(7)`.

Michel Grabisch, Jean-Luc Marichal and Marc Roubens, *Equivalent Representations of Set Functions*, Mathematics of Operations Research **25** (2000), 157--178, DOI `10.1287/moor.25.2.157.12225`, treats the Möbius transform as one of the standard equivalent representations of a set function and relates it to interaction indices. The unique multilinear representation of a pseudo-Boolean function is another standard formulation of the same finite algebra.

In analytic number theory, Bombieri's generalized von Mangoldt functions provide the direct arithmetic specialization described in Section 2. Their support on integers with at most `k` distinct prime factors is precisely the finite-interaction consequence `(10)`.

No novelty is claimed for Boolean Möbius inversion, pseudo-Boolean degree, finite differences, generalized von Mangoldt functions, or their support property. The durable contribution is the **frontier-level survival criterion** obtained by applying those classical mechanisms to the live source-capacity branch: after `MC-436`, factorial source diversity is insufficient by itself; a Möbius divisor operation sees only the full prime interaction.

## Boundaries and falsification tests

- **Squarefreeness is load-bearing for the literal Boolean-cube identification.** For prime powers, the divisor poset is a product of longer chains and the incidence Möbius function gives the corresponding mixed finite-difference statement. The present finding needs only the squarefree source regime.
- **The theorem is about Möbius divisor convolution.** A different analytic operation may retain lower-order interactions, so `(6)` is not a universal no-go for every use of the same representation.
- **Interaction degree is representation-relative.** The set function must be the one actually passed to the divisor convolution. Re-encoding a high-order relation as a named scalar does not make its Boolean degree one; the value on all sub-divisors determines the true coefficient `(13)`.
- **Large top coefficient is not cancellation.** Even if `\mathcal I_G(n)` is nonzero or large on individual sources, one still needs signed control when summing over `n`.
- **Small top coefficient is not automatically useful either.** A bound obtained only by cancellation internal to `(13)` may be as hard as the original Möbius problem; the source of the bound must be independent and auditable.
- **No RH-scale input is used.** The argument is finite combinatorics plus elementary divisor arithmetic.
- **No claim is made for the gap-rank coefficient.** Its full interaction is the next object to test, not an established survivor.

## Consequence for the research line

The `MC-430`--`MC-436` capacity audit has reached a sharper endpoint. Once a representation clears the source-information budget, the next question is not whether it retains still more states. For any route entering through a Möbius divisor sum, compute the Boolean Möbius coefficient of the exact induced divisor statistic.

A bounded-order statistic dies identically once the source has more prime factors than its interaction degree. A high-capacity statistic survives only to the extent that it contains a genuine full-order prime interaction. The live gap-rank branch should therefore move directly to `(13)`: construct a canonical scalar or vector observable from the induced gap-order data on every divisor subset, compute or constrain its top interaction, and only then ask whether that surviving quantity admits an analytic estimate at source scale.