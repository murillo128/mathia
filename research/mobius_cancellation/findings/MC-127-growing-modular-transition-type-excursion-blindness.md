# MC-127 — Growing modular transition types remain blind to lifted excursion order

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix integers `q>=2` and `m>=1`, and put

\[
N=2qm.
\tag{1}
\]

There are two `\{+1,-1\}` increment words of length `N` whose cumulative sums start and end at `0`, whose **complete directed transition histograms modulo `q` are identical**, but whose first-absolute excursion means differ by the factor `m=N/(2q)`.

Write

\[
U=+^{qm}-^{qm},
\qquad
W=(+^q-^q)^m.
\tag{2}
\]

For a word `X=(x_1,\ldots,x_N)`, define

\[
S_X(j)=\sum_{i=1}^j x_i,
\qquad
r_X(j)=S_X(j)\pmod q,
\tag{3}
\]

and let

\[
T_X(r,a)
=
\#\{1\le j\le N:r_X(j-1)=r,\ x_j=a\},
\qquad
r\in\mathbb Z/q\mathbb Z,\ a\in\{+1,-1\}.
\tag{4}
\]

Then for every residue `r`,

\[
\boxed{
T_U(r,+1)=T_W(r,+1)=m,
\qquad
T_U(r,-1)=T_W(r,-1)=m.
}
\tag{5}
\]

Thus `U` and `W` have the same initial residue, final residue, and complete first-order Markov type on the modular state graph. In particular, for **every** one-step observable

\[
\Psi:\mathbb Z/q\mathbb Z\times\{+1,-1\}\to\mathbb C,
\tag{6}
\]

including an observable chosen separately for each `q,m`,

\[
\sum_{j=1}^N\Psi(r_U(j-1),U_j)
=
\sum_{j=1}^N\Psi(r_W(j-1),W_j).
\tag{7}
\]

Nevertheless, with

\[
D_1(X)=\frac1N\sum_{j=1}^N|S_X(j)|,
\tag{8}
\]

one has the exact values

\[
\boxed{D_1(U)=\frac{qm}{2}=\frac N4,}
\qquad
\boxed{D_1(W)=\frac q2.}
\tag{9}
\]

Hence

\[
\boxed{
\frac{D_1(U)}{D_1(W)}=m=\frac{N}{2q}.
}
\tag{10}
\]

The obstruction therefore survives **growing modular state**. If `q=N^{\alpha+o(1)}` along a family with `0<\alpha<1`, then

\[
D_1(U)=N^{1+o(1)}/4,
\qquad
D_1(W)=N^{\alpha+o(1)}/2.
\tag{11}
\]

In particular, for every `0<\alpha<1/2`, one and the same directed transition type contains a representative with linear mean excursion and another with sub-square-root mean excursion. More generally, whenever `q=o(N)`, the excursion ratio in `(10)` diverges.

This is a representation-level information obstruction, not an arithmetic counterexample. The words are not claimed to satisfy Möbius multiplicativity or the actual square-free support pattern. The result says that allowing the accumulator `M mod q` to grow does **not** by itself repair `MC-126` if the retained information is still only the aggregate occupation count of directed modular transitions.

## 1. Exact equality of directed modular transition counts

A block `+^q` started at residue `0` traverses the directed modular cycle once. Its pre-step residues are

\[
0,1,\ldots,q-1,
\tag{12}
\]

so it contributes exactly one `+1` transition from every residue. Likewise, a block `-^q` started at residue `0` has pre-step residues

\[
0,q-1,q-2,\ldots,1,
\tag{13}
\]

and contributes exactly one `-1` transition from every residue. Both blocks return the modular state to `0`.

The word `U` consists of `m` complete positive modular cycles followed by `m` complete negative modular cycles. The word `W` consists of the same multiset of complete cycles, but alternates a positive cycle with a negative cycle. Cycle ordering therefore changes while the directed edge multiset is fixed, proving `(5)`.

Equation `(7)` follows immediately: every aggregate one-step observable factors through the counts `(4)`. This remains true if the observable depends on the scale through `q` or `m`; equality of the complete transition-count vector is exact, not asymptotic.

The two integer lifts also have the same endpoint:

\[
S_U(N)=S_W(N)=0.
\tag{14}
\]

Thus the excursion separation is not hidden in a different total signed displacement. It comes only from the **order in which identical modular cycles are lifted and concatenated**.

## 2. Exact excursion areas

Let `L=qm`. Along `U`, the first half visits heights

\[
1,2,\ldots,L,
\]

and the second half visits

\[
L-1,L-2,\ldots,0.
\]

All heights are nonnegative, so the total absolute area is

\[
\frac{L(L+1)}2+\frac{L(L-1)}2=L^2.
\tag{15}
\]

Since `N=2L`, this gives

\[
D_1(U)=\frac{L^2}{2L}=\frac L2=\frac{qm}{2}.
\tag{16}
\]

Every block `+^q-^q` of `W` starts and ends at integer height `0` and contributes

\[
\frac{q(q+1)}2+\frac{q(q-1)}2=q^2
\tag{17}
\]

to the absolute area. There are `m` such blocks, hence

\[
D_1(W)=\frac{mq^2}{2qm}=\frac q2.
\tag{18}
\]

This proves `(9)` and `(10)`.

The distinction can be stated in graph language. The transition histogram records the balanced directed multigraph and its edge multiplicities. It forgets the Eulerian cycle ordering in the observed path and, more importantly here, it forgets the integer winding lift of successive modular cycles. Grouping all positive windings before all negative windings creates height `qm`; alternating them resets the lift after every cycle. The quotient sees the same modular traffic in both cases.

## 3. What this adds beyond MC-126

`MC-126` fixed the modulus `q` and decomposed every one-step observable on `M mod q` into a periodic potential, one oriented circulation proportional to the ordinary endpoint, and a reversal-even transition/loop occupation term. It deliberately left two plausible escapes open:

1. let the state capacity grow with the observation scale; or
2. exploit the reversal-even occupation profile arithmetically.

The present result narrows both, but only at the representation level. Even when `q=q(N)` grows polynomially, the **entire directed transition occupation vector** can be identical for paths with radically different first-absolute excursion amplitudes. The harmonic endpoint is also matched exactly because both lifted paths finish at zero.

Therefore a proposal based on growing modular state cannot claim excursion sensitivity merely because the number of states or occupation coordinates grows. If its final statistic factors through

\[
\{T_X(r,a):r\in\mathbb Z/q\mathbb Z,\ a=\pm1\}
\tag{19}
\]

plus the initial/final state, this construction is a first-kill control. A successful arithmetic route must use information that excludes the cycle-reordering ambiguity, such as ordered transition data, time/scale labels, non-additive state, prime/divisor labels, multiscale coupling, or a theorem showing that actual Möbius transition occupations satisfy additional relations unavailable to these controls.

This does **not** show that occupation estimates are useless. A Möbius-specific theorem could couple occupations at different moduli, locate them in time, or constrain which cycle orderings are arithmetically admissible. What fails is the sufficiency of the aggregate modular Markov type itself.

## Prior art and novelty assessment

The transition-count language is classical Markov-type / directed-multigraph theory. Philippe Jacquet, Charles Knessl and Wojciech Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (AofA 2010), DOI `10.46298/dmtcs.2768`, identifies Markov types with balanced frequency matrices and balanced directed multigraphs. Reordering compatible cycle decompositions while preserving directed edge counts is therefore established combinatorial structure.

A targeted audit for Markov types, transition counts, partial sums, discrepancy, and excursion control found the standard type/frequency-matrix and Eulerian-multigraph framework, not a basis for claiming novelty for that mechanism. **No novelty is claimed for Markov types, balanced transition matrices, or cycle reorderings.** The durable content is the explicit Möbius-line information boundary: a growing modular transition type can preserve every aggregate one-step state/increment statistic while forgetting the macroscopic first-absolute excursion of the integer lift.

## Boundaries and falsification tests

- The controls are `\{+1,-1\}` words, not the actual Möbius sequence. They do not preserve square-free support by integer position, multiplicativity, divisor relations, prime values, or zeta-specific analytic structure.
- The retained data are aggregate directed transition counts. Ordered transition sequences, transition times, position-dependent weights, run-length data, higher-order state paths, and nonlocal pairings distinguish `U` and `W` and lie outside the quotient.
- The modular state is additive: `r_j=r_{j-1}+x_j mod q`. A non-additive or arithmetically labelled growing state is not covered.
- The result allows `q` to grow but does not assert any uniform theorem for an arbitrary externally constrained relation `q(N)`. The exact construction is parameterized by integers `q,m` with `N=2qm`; the power-law corollaries follow along corresponding integer families.
- Equality of the transition type does not imply equality of every statistic derived from the full modular path. It implies equality exactly for statistics that factor through the aggregate directed counts `(4)` and the matched boundary state.
- There is no probabilistic independence, RH assumption, zero-free region, Mellin inversion, or `1/zeta` input.

The exact claim can be falsified by finding a residue and direction whose count differs between `U` and `W`, or by contradicting the area formulas `(15)`--`(18)`. Each positive or negative `q`-block traverses its corresponding directed modular cycle exactly once, so neither failure occurs.

## Consequence for the line

The mean-absolute transfer frontier can now reject a broader family of finite/growing-state repairs before arithmetic work is invested in them. `MC-126` showed that fixed additive state has no new oriented carrier beyond endpoint winding; `MC-127` shows that even **growing additive state plus complete first-order transition occupation** need not retain excursion order.

The residual source question is correspondingly sharper. A viable route from source-natural Möbius information to the RH-complete mean-absolute target must carry order-sensitive or genuinely arithmetic information not recoverable from a modular transition histogram alone. In particular, merely increasing `q` or estimating the empirical distribution of `(M_{n-1} mod q,\mu_n)` does not constitute a new amplitude carrier unless an additional Möbius theorem couples those counts to their temporal ordering or rules out the matched cycle-reordering class.