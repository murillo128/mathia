# MC-129 — Joint local-factor and binned modular summaries remain excursion-blind

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISMS`, `NO-NOVELTY-CLAIM`.

## Claim

Fix integers

\[
k,q\ge 2,\qquad r,b\ge 1,
\]

and let

\[
L=q\left\lceil\frac{k}{q}\right\rceil,
\qquad
c=\frac{L}{q}.
\tag{1}
\]

Thus `q|L` and

\[
\max(k,q)\le L<k+q.
\tag{2}
\]

Write `+` for `+1` and `-` for `-1`, and define

\[
v=+^{k-1},\qquad A=+,\qquad B=-^k+^{k-1},
\tag{3}
\]

followed by the two macro-cycles

\[
P=A^L=+^L,
\qquad
Q=B^L.
\tag{4}
\]

Set

\[
X=P^rQ^r,
\qquad
Y=(PQ)^r,
\qquad
U=vX^b,
\qquad
W=vY^b.
\tag{5}
\]

The two full words have common length

\[
N=2kLrb+k-1.
\tag{6}
\]

Partition the tail after the common prefix `v` into `b` consecutive bins, each of length `2kLr`. For a tail step `j`, let `C_Z(j-1)` be the preceding `k-1` symbols of a word `Z`, and define the bin-local **cross-coupled product-state transition tensor**

\[
J_{Z,t}(u,a,\varepsilon)
=
\#\{j\text{ in bin }t:
C_Z(j-1)=u,\ 
S_Z(j-1)\equiv a\pmod q,\ 
z_j=\varepsilon\},
\]

for `u in {+,-}^{k-1}`, `a in Z/qZ`, and `epsilon in {+1,-1}`. Then, for every bin and every product-state transition,

\[
\boxed{
J_{U,t}(u,a,\varepsilon)=J_{W,t}(u,a,\varepsilon).
}
\]

Thus the construction matches not only the two marginals recorded previously, but their full contemporaneous cross-tabulation. In particular, inside every corresponding bin:

1. the count of every contiguous `+/-` factor of every length at most `k` is identical;
2. the complete directed modular transition histogram

\[
T_t(a,\varepsilon)
=
\#\{j\text{ in bin }t:S(j-1)\equiv a\pmod q,\ x_j=\varepsilon\}
\tag{7}
\]

is identical; and
3. every scalar one-step observable of the joint local context, modular state, increment, and coarse time label has the same total:

\[
\sum_{j\text{ in bin }t}
\Psi_t(C_U(j-1),S_U(j-1)\bmod q,U_j)
=
\sum_{j\text{ in bin }t}
\Psi_t(C_W(j-1),S_W(j-1)\bmod q,W_j).
\]

More precisely, for every bin `t` and residue `a`,

\[
\boxed{
T_{U,t}(a,+1)=T_{W,t}(a,+1)=rck,
\qquad
T_{U,t}(a,-1)=T_{W,t}(a,-1)=rck.
}
\tag{8}
\]

All bin boundaries also have the same lifted partial sum `k-1` in both words.

Despite this simultaneous local-memory, state-occupation, cross-coupling, and coarse-time agreement, their first-absolute excursion means

\[
D_1(Z)=\frac1N\sum_{j=1}^{N}|S_Z(j)|
\tag{9}
\]

have the exact values

\[
\boxed{
D_1(U)
=
\frac{\frac12k(k-1)+bLrk(Lr+k-1)}{2kLrb+k-1},
}
\tag{10}
\]

and

\[
\boxed{
D_1(W)
=
\frac{\frac12k(k-1)+bLrk(k+L-1)}{2kLrb+k-1}.
}
\tag{11}
\]

Hence, whenever `Lr/k -> infinity`,

\[
D_1(U)\sim \frac{Lr}{2},
\qquad
D_1(W)\sim \frac{k+L}{2}.
\tag{12}
\]

This gives a joint square-root obstruction. Let `R -> infinity`, put

\[
k=R^{\alpha+o(1)},\qquad
q=R^{\beta+o(1)},\qquad
b=R^{\gamma+o(1)},
\]

write `ell=max(alpha,beta)`, and choose

\[
r=R^{1-\alpha-\ell-\gamma+o(1)}.
\tag{13}
\]

If

\[
\ell<\frac12,
\qquad
\alpha+\gamma<\frac12,
\tag{14}
\]

then `N=R^(1+o(1))` and

\[
D_1(U)=N^{1-\alpha-\gamma+o(1)}
      =N^{1/2+\Omega(1)},
\tag{15}
\]

while

\[
D_1(W)=N^{\ell+o(1)}
      =N^{1/2-\Omega(1)}.
\tag{16}
\]

Thus even the **complete bin-local product-state transition type** coupling local memory to growing modular state can place matched representatives on opposite sides of square-root excursion scale throughout the regime `(14)`.

This is a representation-level matched-control obstruction, not an arithmetic counterexample. The words are not claimed to satisfy Möbius multiplicativity, the actual square-free support pattern, prime values, or divisor relations.

## 1. Exact bin-local product-state equality

Use the directed product graph with vertices

\[
(\eta,a)\in\{+,-\}^{k-1}\times\mathbb Z/q\mathbb Z
\]

and an edge labelled `epsilon in {+1,-1}`

\[
(\eta_1\cdots\eta_{k-1},a)
\longrightarrow
(\eta_2\cdots\eta_{k-1}\varepsilon,\ a+\varepsilon).
\tag{17}
\]

The first coordinate is the ordinary binary de Bruijn state and the second is the additive residue of the lifted partial sum. Traversing an edge records exactly the triple `(local context, residue, increment)` counted by `J`.

At the common base state

\[
(v,k-1\bmod q),
\]

the word `P=+^L` is a closed product-state walk: every `+` is the de Bruijn self-loop at `v`, and its lifted net displacement `L` is divisible by `q`.

The word `Q=B^L` is also closed in the same product graph. Each copy of

\[
B=-^k+^{k-1}
\]

returns the de Bruijn coordinate to `v` and has lifted net displacement `-1`. Therefore `Q` has net displacement `-L`, which is `0 mod q`, and returns both coordinates to the common base state.

Consequently `X=P^rQ^r` and `Y=(PQ)^r` traverse exactly the same multiset of directed **product-graph edges**: both are concatenations of `r` copies of the closed walk `P` and `r` copies of the closed walk `Q`, differing only in the order of those based loops. This proves the exact equality of `J` in every bin.

The same argument repeats independently in all `b` bins because both `X` and `Y` have lifted net displacement zero and end with the local suffix `v`. Hence every new bin starts from the same product state in `U` and `W`.

Equality for shorter local factors follows by projecting a product edge to the desired suffix of its `k-1` context. If factor counts are defined using only windows wholly contained inside a bin, the finitely many cross-boundary windows may be removed: they are identical pointwise because the preceding suffix, bin boundary height, and initial `P` segment agree.

This product-state statement strictly strengthens separate equality of the local-factor and modular-transition marginals. In particular, a statistic cannot escape the obstruction merely by asking **which local pattern occurred at which modular state** if it finally scalarizes to the empirical one-step type of `(C_{j-1},M_{j-1} mod q,mu_j)` inside the coarse bins.

## 2. Explicit marginal counts and bin boundaries

Projecting the product-state tensor to the de Bruijn coordinate gives the local factor histogram. The standard `k`-abelian description is also immediate from the construction: `A` and `B` are closed de Bruijn walks based at `v`, so `P^rQ^r` and `(PQ)^r` contain the same closed-walk multiset, with the same prefix and suffix of length `k-1`.

Projecting instead to the modular coordinate gives `(7)`. Because `q|L`, one block `P=+^L` traverses the positive residue cycle exactly `c=L/q` times and contributes `c` positive transitions from every residue.

One copy of `B` has net increment `-1`. In `Q=B^L`, the starting residues of the `L` consecutive copies of `B` therefore run through each residue exactly `c` times. A single `B` contains `k` negative steps and `k-1` positive steps. Across one complete set of `q` consecutive starting residues, each fixed step position occurs once from every residue. Hence `Q` contributes, from every residue,

\[
ck\text{ negative transitions}
\quad\text{and}\quad
c(k-1)\text{ positive transitions}.
\tag{18}
\]

Combining `P` and `Q` gives exactly `ck` transitions in each direction from every residue. Multiplying by `r` proves `(8)`.

Moreover `P` has lifted net increment `+L` and `Q` has lifted net increment `-L`. Both `P^rQ^r` and `(PQ)^r` therefore have lifted net increment zero. After the common prefix `v`, every bin in both `U` and `W` starts and ends at height `k-1`; no excursion separation is hidden in a boundary mismatch.

## 3. Exact excursion areas

All partial sums of both words are nonnegative. The common prefix contributes

\[
C_k=1+2+\cdots+(k-1)=\frac{k(k-1)}2.
\tag{19}
\]

For a grouped bin,

\[
X=P^rQ^r=A^{Lr}B^{Lr}.
\]

Starting at height `k-1`, the `A` copies first build a macroscopic height and the `B` copies then unwind it. Direct summation gives the tail area

\[
\boxed{
A_X=Lrk(Lr+k-1).
}
\tag{20}
\]

For the alternating bin it suffices to evaluate one pair

\[
PQ=A^LB^L.
\]

The `A^L` segment, started at height `k-1`, contributes

\[
L(k-1)+\frac{L(L+1)}2.
\tag{21}
\]

A `B` block started at height `H` contributes

\[
(2k-1)H-k^2.
\tag{22}
\]

The `j`-th copy of `B` in `B^L`, for `j=0,...,L-1`, starts at height

\[
H_j=k-1+L-j.
\tag{23}
\]

Summing `(22)` over `(23)` and adding `(21)` yields

\[
\boxed{
A_{PQ}=Lk(k+L-1).
}
\tag{24}
\]

Since a `PQ` pair has lifted net increment zero, an alternating bin has tail area

\[
\boxed{
A_Y=rLk(k+L-1).
}
\tag{25}
\]

Every bin resets to height `k-1`. Multiplying `(20)` or `(25)` by `b`, adding the single common-prefix area `(19)`, and dividing by `(6)` proves `(10)` and `(11)`.

The difference lies only in **macro-cycle order**. The grouped word accumulates `Lr` positive one-step cycles before unwinding the same number of negative-net de Bruijn cycles. The alternating word resets the lifted height after each `P,Q` pair. The product-state transition type forgets precisely the order in which those common based cycles were concatenated.

## 4. What this adds beyond MC-125 and MC-128

`MC-125` showed that complete local factor histograms through sub-square-root memory can forget excursion order. `MC-127` and `MC-128` showed that growing modular transition types, even localized into coarse time bins, can also forget lifted excursion order.

The original form of this finding combined those summaries as separate marginals. The same construction in fact gives the stronger statement above: because `P` and `Q` are closed at the **same vertex of the coupled de Bruijn/residue graph**, reordering them preserves the complete local-context/modular-state transition tensor, not just its two projections.

This closes the simplest contemporaneous cross-coupling repair as well. Increasing several summary dimensions polynomially does not help if the final information still factors through the empirical edge multiset of a finite/growing quotient that shares the hidden cycle-order freedom. The obstruction survives whenever the retained local/state scale `L~max(k,q)` is sub-square-root and the product of local-memory and time resolution remains below square-root in the exponent sense of `(14)`.

The remaining escapes are therefore more strongly ordered or arithmetic: exact transition timestamps or higher-order ordering of product states, nested/noncommutative cross-scale data, non-additive memory, prime/divisor labels, multiplicative constraints, or another Möbius-specific theorem that excludes the common-cycle reorderings for a proved reason.

## Prior art and novelty assessment

The component languages and the product-graph viewpoint are classical.

Juhani Karhumäki, Aleksi Saarela and Luca Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, Journal of Combinatorial Theory, Series A 120 (2013), no. 8, 2189–2206, DOI `10.1016/j.jcta.2013.08.008`, introduces `k`-abelian equivalence by equality of factor counts through length `k`.

Juhani Karhumäki, Svetlana Puzynina, Michaël Rao and Markus A. Whiteland, *On cardinalities of k-abelian equivalence classes*, Theoretical Computer Science 658 (2017), 190–204, DOI `10.1016/j.tcs.2016.06.010`, connects `k`-abelian equivalence classes with cycle decompositions of de Bruijn graphs.

`MC-S41` records the separate Markov-type prior art of Jacquet, Knessl and Szpankowski, where transition-count types are balanced frequency matrices / directed multigraph data.

A particularly close graph-theoretic boundary is Nicolás Álvarez, Verónica Becher, Martín Mereb, Ivo Pajor and Carlos Miguel Soto, *On extremal factors of de Bruijn-like graphs*, Discrete Applied Mathematics 357 (2024), 352–364, DOI `10.1016/j.dam.2024.06.010`, arXiv `2308.16257`. That paper explicitly studies tensor products of de Bruijn graphs with simple cycles in a cycle-decomposition setting. The labelled product graph `(17)` is not imported from their theorem, but the literature makes clear that coupling de Bruijn state with a cyclic coordinate is established combinatorial territory.

A targeted audit around `k`-abelian equivalence, de Bruijn cycle switching, de Bruijn/cycle product graphs, Markov types, and partial-sum excursions found the established component theories rather than a basis for claiming a new general combinatorial framework. **No novelty is claimed** for `k`-abelian equivalence, de Bruijn products, Markov transition types, or reordering common based cycles. The durable Mathia content is the exact Möbius-line information boundary: the same explicit controls preserve the full bin-local local-context/residue/increment tensor while their first-absolute excursions straddle the RH-relevant square-root scale.

## Boundaries and falsification tests

- The controls are binary `+/-1` words. They do not preserve Möbius zeros at nonsquarefree positions, multiplicativity, prime values, divisor relations, or zeta-specific analytic structure.
- The theorem matches the complete bin-local empirical one-step type of the product state `(last k-1 increments, cumulative sum mod q)` together with the current increment. Hence it also matches every contemporaneous cross-tabulation of a local factor through length `k` with modular state that factors through this product transition type.
- It does **not** match the full ordered product-state path, exact transition timestamps inside a bin, run lengths, adaptive subdivisions, higher-order/noncommutative cross-time observables, prime/divisor labels, or non-additive persistent state.
- The common prefix `v` is identical in both words and lies outside the `b` equal tail bins. Every tail-bin lifted endpoint is matched exactly at height `k-1`.
- The choice `L=q ceil(k/q)` synchronizes the macro-cycles so that they close in both coordinates. It changes neither qualitative local-memory nor modular-state scale because `max(k,q)<=L<k+q`.
- The exponent boundary `(14)` is a **kill region for this explicit control family**, not a positive reconstruction theorem outside it. No sufficiency is claimed when `max(k,q)` or the `k*b` information scale reaches square-root order.
- The construction is parameterized by integers; asymptotic power laws are along corresponding integer families.
- No probabilistic independence, RH hypothesis, zero-free region, Mellin continuation, Perron inversion, or `1/zeta` identity enters the derivation.

The strengthened claim can be falsified by finding one bin and one product-state transition `(u,a,epsilon)` whose count differs, a mismatched bin endpoint, or a failure of `(10)`–`(11)`. Because `P` and `Q` are closed walks based at the same product vertex and occur with the same multiplicities in both bin words, the product-edge multisets are identical.

## Consequence for the line

The accepted mean-absolute transfer problem can now reject the simplest **cross-coupled** representation upgrade as well as the separate local and modular summaries. A source statistic that only records, inside coarse bins, the empirical distribution of `(local context, M mod q, current increment)` remains vulnerable to common-cycle reordering and cannot generically recover first-absolute excursion amplitude.

A surviving source mechanism must retain information absent from that product-edge quotient. The clean residual surfaces are finer temporal or higher-order ordering of the coupled state path, genuinely non-additive memory, prime/divisor-labelled long-range relations, exact multiplicative constraints, or a Möbius-specific theorem proving that the matched common-cycle reorderings are arithmetically inadmissible. Without such an extra bridge, contemporaneously coupling local patterns to additive modular state still does not recover RH-scale first-absolute amplitude.
