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

Partition the tail after the common prefix `v` into `b` consecutive bins, each of length `2kLr`. Then **inside every corresponding bin**, `U` and `W` have both of the following exact matches:

1. the count of every contiguous `+/-` factor of every length at most `k`;
2. the complete directed modular transition histogram

\[
T_t(a,\varepsilon)
=
\#\{j\text{ in bin }t:S(j-1)\equiv a\pmod q,\ x_j=\varepsilon\},
\tag{7}
\]

for every residue `a in Z/qZ` and `epsilon in {+1,-1}`.

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

Despite this simultaneous local-memory, state-occupation, and coarse-time agreement, their first-absolute excursion means are

\[
D_1(Z)=\frac1N\sum_{j=1}^{N}|S_Z(j)|,
\tag{9}
\]

with the exact values

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

Thus even **combining** complete local factor statistics, growing modular-state transition statistics, and coarse time localization does not generically recover square-root excursion amplitude throughout the regime `(14)`.

This is a representation-level matched-control obstruction, not an arithmetic counterexample. The words are not claimed to satisfy Möbius multiplicativity, the actual square-free support pattern, prime values, or divisor relations.

## 1. Exact bin-local factor-histogram equality

Use the binary de Bruijn graph of order `k-1`. Its vertices are words of length `k-1`, and appending one symbol traverses the edge labelled by the corresponding length-`k` factor.

At the base vertex

\[
v=+^{k-1},
\]

the word `A=+` is a closed one-edge walk. The word

\[
B=-^k+^{k-1}
\]

is also a closed walk: the first `k-1` minus signs move from `v` to `-^(k-1)`, the next minus traverses the `-^k` loop, and the final `k-1` plus signs return to `v`.

Therefore `P=A^L` and `Q=B^L` are closed walks based at the same de Bruijn vertex. In one grouped bin `X=P^rQ^r` and one alternating bin `Y=(PQ)^r`, the total closed-walk multiset is identical: both contain exactly `Lr` copies of `A` and `Lr` copies of `B`. Consequently, after prepending the common base word `v`, the two traversals have exactly the same length-`k` edge multiset.

The actual bin words `X` and `Y` also have a common prefix and suffix of length `k-1`. Indeed `L>=k`, so both begin with at least `k` plus signs, and both end in `Q`, whose last copy of `B` ends in `+^(k-1)`. The extra length-`k` factors created by prepending `v` are therefore identical and may be subtracted from the equal edge multisets. Thus `X` and `Y` have the same count of every length-`k` factor.

The standard characterization of `k`-abelian equivalence then gives equality of the counts of **every** factor of length at most `k`. Since the same pair of bin words is repeated in the same bin positions, this equality holds separately in every time bin, not merely after global aggregation.

## 2. Exact bin-local modular transition equality

Because `q|L`, one block `P=+^L` has net increment `L == 0 mod q`. It traverses the positive residue cycle exactly `c=L/q` times and therefore contributes exactly `c` positive transitions from every residue.

One copy of `B` has net increment `-1`. In `Q=B^L`, the starting residues of the `L` consecutive copies of `B` therefore run through each residue exactly `c` times. A single `B` contains `k` negative steps and `k-1` positive steps. Across one complete set of `q` consecutive starting residues, each fixed step position occurs once from every residue. Hence `Q` contributes, from every residue,

\[
ck\text{ negative transitions}
\quad\text{and}\quad
c(k-1)\text{ positive transitions}.
\tag{17}
\]

Combining `P` and `Q` therefore gives exactly `ck` transitions in **each** direction from every residue. A grouped bin `P^rQ^r` and an alternating bin `(PQ)^r` contain the same `r` copies of each modularly closed macro-cycle, so both produce `(8)`.

Moreover `P` has lifted net increment `+L` and `Q` has lifted net increment `-L`. Both `P^rQ^r` and `(PQ)^r` have lifted net increment zero. After the common prefix `v`, every bin in both `U` and `W` consequently starts and ends at height `k-1`; no difference is hidden in boundary drift.

## 3. Exact excursion areas

All partial sums of both words are nonnegative. The common prefix contributes

\[
C_k=1+2+\cdots+(k-1)=\frac{k(k-1)}2.
\tag{18}
\]

For a grouped bin,

\[
X=P^rQ^r=A^{Lr}B^{Lr}.
\]

This is the same closed-walk geometry as the cycle-ordering control with parameter `m=Lr`: starting at height `k-1`, the `A` copies first build a macroscopic height and the `B` copies then unwind it. Direct summation gives the tail area

\[
\boxed{
A_X=Lrk(Lr+k-1).
}
\tag{19}
\]

For the alternating bin it suffices to evaluate one pair

\[
PQ=A^LB^L.
\]

The `A^L` segment, started at height `k-1`, contributes

\[
L(k-1)+\frac{L(L+1)}2.
\tag{20}
\]

A `B` block started at height `H` contributes

\[
(2k-1)H-k^2.
\tag{21}
\]

The `j`-th copy of `B` in `B^L`, for `j=0,...,L-1`, starts at height

\[
H_j=k-1+L-j.
\tag{22}
\]

Summing `(21)` over `(22)` and adding `(20)` yields

\[
\boxed{
A_{PQ}=Lk(k+L-1).
}
\tag{23}
\]

Since a `PQ` pair has lifted net increment zero, an alternating bin has tail area

\[
\boxed{
A_Y=rLk(k+L-1).
}
\tag{24}
\]

Every bin resets to height `k-1`. Multiplying `(19)` or `(24)` by `b`, adding the single common-prefix area `(18)`, and dividing by `(6)` proves `(10)` and `(11)`.

The difference again lies only in **cycle order**. The grouped word accumulates `Lr` positive one-step cycles before unwinding the same number of negative-net de Bruijn cycles. The alternating word resets the lifted height after each `P,Q` pair. Both the local factor histogram and the modular transition histogram forget precisely that macro-cycle ordering.

## 4. What this adds beyond MC-125 and MC-128

`MC-125` showed that complete local factor histograms through sub-square-root memory can forget excursion order. `MC-127` and `MC-128` showed that growing modular transition types, even localized into coarse time bins, can also forget lifted excursion order.

Those results separately left a natural repair: retain **both** kinds of information. The present construction kills that repair over a substantial joint regime. Each time bin preserves the complete local empirical law through length `k` **and** the complete directed `mod q` state/increment occupation vector, while the first-absolute excursion can still lie on opposite sides of square-root scale.

The mechanism is a common-cycle refinement. The basic de Bruijn cycles are grouped into macro-cycles whose net displacement is divisible by `q`. They are therefore simultaneously closed in the local de Bruijn quotient and in the modular additive-state quotient. Reordering those common closed macro-cycles changes the integer lift dramatically while leaving both summaries invariant.

The resulting information budget is sharper than simply counting coordinates. The obstruction survives whenever the retained local/state scale `L~max(k,q)` is sub-square-root and the product of local-memory and time resolution remains below square-root in the exponent sense of `(14)`. Increasing several summary dimensions polynomially does not help if they still factor through quotients that share the same hidden cycle-order freedom.

## Prior art and novelty assessment

The component languages are classical.

Juhani Karhumäki, Aleksi Saarela and Luca Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, Journal of Combinatorial Theory, Series A 120 (2013), no. 8, 2189–2206, DOI `10.1016/j.jcta.2013.08.008`, introduces `k`-abelian equivalence by equality of factor counts through length `k`.

Juhani Karhumäki, Svetlana Puzynina, Michaël Rao and Markus A. Whiteland, *On cardinalities of k-abelian equivalence classes*, Theoretical Computer Science 658 (2017), 190–204, DOI `10.1016/j.tcs.2016.06.010`, explicitly connects `k`-abelian equivalence classes with cycle decompositions of de Bruijn graphs.

`MC-S41` records the separate Markov-type prior art of Jacquet, Knessl and Szpankowski, where transition-count types are balanced frequency matrices / directed multigraph data.

A targeted audit around `k`-abelian equivalence, de Bruijn cycle switching, Markov types, partial sums, discrepancy, and excursions found the established component theories rather than a reason to claim a new general combinatorial framework. **No novelty is claimed** for `k`-abelian equivalence, de Bruijn cycle reordering, Markov transition types, or the common-cycle construction itself. The durable content here is the exact Mathia/Möbius-line specialization: an explicit family matching both source summaries inside every coarse time bin while quantifying the excursion separation and its square-root kill surface.

## Boundaries and falsification tests

- The controls are binary `+/-1` words. They do not preserve Möbius zeros at nonsquarefree positions, multiplicativity, prime values, divisor relations, or zeta-specific analytic structure.
- The theorem matches **two complete bin-local summaries simultaneously**: factor counts through length `k`, and modular state/increment transition counts. It does **not** match the finer joint cross-tabulation coupling a particular local word to the contemporaneous modular state. A candidate retaining that cross-coupled tensor lies outside this obstruction.
- Full transition timestamps, within-bin order, run lengths, adaptive subdivisions, noncommutative cross-time observables, prime/divisor labels, and non-additive persistent state also lie outside the matched quotient.
- The common prefix `v` is identical in both words and lies outside the `b` equal tail bins. Every tail-bin lifted endpoint is matched exactly at height `k-1`.
- The choice `L=q ceil(k/q)` is only a synchronization device making each macro-cycle closed in both quotients. It changes neither the qualitative local-memory scale nor the modular-state scale because `max(k,q)<=L<k+q`.
- The exponent boundary `(14)` is a **kill region for this explicit control family**, not a positive reconstruction theorem outside it. No sufficiency is claimed when `max(k,q)` or the `k*b` information scale reaches square-root order.
- The construction is parameterized by integers; asymptotic power laws are along corresponding integer families.
- No probabilistic independence, RH hypothesis, zero-free region, Mellin continuation, Perron inversion, or `1/zeta` identity enters the derivation.

The exact claim can be falsified by finding one bin and one factor of length at most `k` whose count differs, one bin/residue/direction transition count that differs, a mismatched bin endpoint, or a failure of `(10)`–`(11)`. These assertions reduce to the common closed-cycle counts and the displayed finite sums.

## Consequence for the line

The accepted mean-absolute transfer problem can now reject another obvious representation upgrade before arithmetic effort is invested in it. Combining sub-square-root local empirical memory with sub-square-root modular-state occupation and coarse temporal localization is not automatically excursion-sensitive: the two summaries can share a common cycle-order kernel.

A surviving source mechanism must therefore identify information absent from this joint quotient. The cleanest remaining escapes are a **cross-coupling** between local arithmetic pattern and persistent state, genuinely finer ordered/multiscale information, non-additive state, prime/divisor-labelled long-range relations, or a Möbius-specific theorem proving that the matched common-cycle reorderings are arithmetically inadmissible. Without such an extra bridge, simply stacking the previously separate local and modular summaries does not recover RH-scale first-absolute amplitude.