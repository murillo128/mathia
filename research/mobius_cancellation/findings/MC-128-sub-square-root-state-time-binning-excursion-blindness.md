# MC-128 — Sub-square-root state and time binning remain blind to excursion amplitude

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix integers `q>=2`, `r>=1`, and `b>=1`, and put

\[
N=2qrb.
\tag{1}
\]

Partition a length-`N` increment word into `b` consecutive bins of equal length `2qr`. There are two `\{+1,-1\}` words with the same initial and final cumulative sum and with **identical complete directed modular transition histograms inside every time bin**, but with first-absolute excursion means differing by the factor `r=N/(2qb)`.

Define one grouped and one alternating bin by

\[
G=+^{qr}-^{qr},
\qquad
A=(+^q-^q)^r,
\tag{2}
\]

and let

\[
U=G^b,
\qquad
W=A^b.
\tag{3}
\]

For a word `X=(x_1,\ldots,x_N)`, write

\[
S_X(j)=\sum_{i=1}^j x_i,
\qquad
D_1(X)=\frac1N\sum_{j=1}^N|S_X(j)|.
\tag{4}
\]

For bin `k=1,...,b`, let `I_k={(k-1)2qr+1,...,k2qr}` and define the bin-local modular transition count

\[
T_{X,k}(a,\epsilon)
=
\#\{j\in I_k:S_X(j-1)\equiv a\pmod q,\ x_j=\epsilon\},
\tag{5}
\]

where `a in Z/qZ` and `epsilon in {+1,-1}`.

Then every bin starts and ends at lifted height `0`, and for every `k,a`,

\[
\boxed{
T_{U,k}(a,+1)=T_{W,k}(a,+1)=r,
\qquad
T_{U,k}(a,-1)=T_{W,k}(a,-1)=r.
}
\tag{6}
\]

Thus `U` and `W` remain indistinguishable even after the aggregate Markov type of `MC-127` is refined by an ordered time label taking `b` values. Equivalently, for every family of observables

\[
\Psi_k:(\mathbb Z/q\mathbb Z)\times\{+1,-1\}\to\mathbb C,
\tag{7}
\]

chosen arbitrarily and separately for every time bin,

\[
\sum_{k=1}^b\sum_{j\in I_k}
\Psi_k(S_U(j-1)\bmod q,U_j)
=
\sum_{k=1}^b\sum_{j\in I_k}
\Psi_k(S_W(j-1)\bmod q,W_j).
\tag{8}
\]

Nevertheless,

\[
\boxed{D_1(U)=\frac{qr}{2}=\frac{N}{4b},}
\qquad
\boxed{D_1(W)=\frac q2,}
\tag{9}
\]

and hence

\[
\boxed{
\frac{D_1(U)}{D_1(W)}=r=\frac{N}{2qb}.
}
\tag{10}
\]

In particular, along any integer family with

\[
q=N^{\alpha+o(1)},
\qquad
b=N^{\beta+o(1)},
\qquad
0\le\alpha<\frac12,
\qquad
0\le\beta<\frac12,
\tag{11}
\]

one has

\[
D_1(W)=N^{\alpha+o(1)}/2=o(N^{1/2+o(1)}),
\tag{12}
\]

while

\[
D_1(U)=N^{1-\beta+o(1)}/4=N^{1/2+\Omega(1)}.
\tag{13}
\]

Thus this explicit quotient can still place representatives on opposite sides of the square-root excursion scale while **both** its modular state resolution and its number of temporal bins are sub-square-root. This is a representation-level obstruction, not an arithmetic counterexample: the words are not claimed to satisfy Möbius multiplicativity, square-free placement, divisor relations, or prime-value constraints.

## 1. Exact equality of every bin-local transition type

A block `+^q` started at a multiple of `q` traverses each positive directed edge of the residue cycle exactly once and returns to the same residue. A block `-^q` does the same for the negative directed edges.

Inside `G`, the run `+^{qr}` is exactly `r` complete positive residue cycles and `-^{qr}` is exactly `r` complete negative residue cycles. Inside `A`, the same `r` positive and `r` negative cycles are merely interleaved. Both bins begin and end at integer height `0`.

Therefore the complete directed edge multiset inside one `G` bin and one `A` bin is identical, giving `(6)`. Since `U` and `W` repeat those bins in the same temporal positions, the equality holds separately for every labeled bin. Equation `(8)` follows because any statistic that uses the bin index and then scalarizes the transitions inside each bin factors through these counts.

This is strictly more information than the global transition histogram in `MC-127`: the observer knows **when, up to one of `b` coarse time cells**, every residue/direction transition occurred. What remains forgotten is the ordering of complete lifted residue cycles *inside* each cell.

## 2. Exact excursion areas

Within one grouped bin `G`, the lifted path visits

\[
1,2,\ldots,qr
\]

and then

\[
qr-1,qr-2,\ldots,0.
\]

Its absolute area is therefore

\[
\frac{qr(qr+1)}2+\frac{qr(qr-1)}2=q^2r^2.
\tag{14}
\]

There are `b` independent zero-endpoint bins, so

\[
D_1(U)
=
\frac{bq^2r^2}{2qrb}
=
\frac{qr}{2}
=
\frac{N}{4b}.
\tag{15}
\]

Each elementary block `+^q-^q` in `A` has absolute area `q^2`, and there are `rb` such blocks in `W`. Hence

\[
D_1(W)
=
\frac{rbq^2}{2qrb}
=
\frac q2.
\tag{16}
\]

This proves `(9)` and `(10)`. The loss mechanism is exactly the hidden order of lifted cycles inside each time cell: grouping `r` positive windings before `r` negative windings reaches height `qr`, whereas alternating them resets to zero after each pair.

## 3. A two-axis square-root boundary for this control family

The formulas expose two independent resolutions:

- state resolution is the modulus `q`, and controls the low-excursion representative through `D_1(W)=q/2`;
- temporal resolution is the number of bins `b`, and controls the high-excursion representative through `D_1(U)=N/(4b)`.

For this construction to stop straddling square-root scale, at least one of those two resolutions must itself reach square-root order: `q` must be `N^{1/2+o(1)}` or larger to prevent the alternating control from being sub-square-root, or `b` must be `N^{1/2+o(1)}` or larger to force the grouped control down to square-root order.

This is only a **kill threshold for the explicit matched-control family**, not a sufficiency theorem. Even `q` or `b` of square-root size need not determine excursion amplitude. The result says that simply taking a sub-square-root growing modular state and adding a sub-square-root number of coarse temporal labels still leaves enough hidden cycle order to cross the RH-relevant amplitude boundary.

The information budget can also be stated directly. The binned type contains `2qb` transition counts, but equality of that entire vector does not control `D_1`. Merely increasing the number of scalar occupation coordinates polynomially is therefore not the relevant issue; their temporal granularity and the lift-order information they retain are decisive.

## 4. Consequence for the mean-absolute transfer route

`MC-127` left temporally ordered occupation as a plausible escape from aggregate modular transition types. The present result narrows that escape. **Coarse** ordering obtained by dividing time into bins and remembering a full modular transition histogram in each bin is still insufficient whenever the bins are broad enough to contain reorderable lifted cycles.

A surviving ordered-occupation proposal must therefore do something stronger than attach a sub-square-root number of time labels to sub-square-root modular states. It may retain genuinely fine transition order, couple neighboring or nested time scales, use position-dependent arithmetic labels, record cross-bin noncommutative information, employ non-additive state, or prove a Möbius-specific theorem that forbids the matched cycle reorderings used here.

This does not rule out a source-natural Möbius statistic with coarse time localization. It says that any positive transfer theorem needs an **additional arithmetic hypothesis** whose role can be identified explicitly; the generic state-time type itself cannot carry the required excursion amplitude.

## Prior art and novelty assessment

`MC-S41` records the classical Markov-type language: empirical directed transition counts are balanced frequency matrices / directed multigraph data. The binned object here is simply an ordered tuple of such classical transition types on preassigned consecutive blocks. No novelty is claimed for Markov types, blockwise empirical transition frequencies, cycle decompositions, or reordering complete residue cycles.

A targeted literature audit around Markov types, empirical transition matrices, blockwise/piecewise transition frequencies, Eulerian cycle ordering, and partial-sum excursions found established method-of-types and path-enumeration frameworks rather than a basis for claiming a new general combinatorial theory. The exact construction and area calculation above are elementary. The durable Mathia content is the quantitative information boundary: adding coarse temporal localization to a growing modular transition type still cannot recover first-absolute excursion amplitude, with an explicit state/time square-root kill surface.

## Boundaries and falsification tests

- The controls are `\{+1,-1\}` words, not the actual Möbius sequence. They do not preserve square-free support by integer position, multiplicativity, divisor relations, prime values, or zeta-specific analytic structure.
- Equality holds for the complete directed modular transition histogram **inside each fixed bin**. The full ordered modular path, transition timestamps inside a bin, run lengths, finer adaptive subdivisions, and nonlocal cross-time pairings distinguish the controls and are outside the quotient.
- Every bin has matched lifted boundary height `0`. The separation is therefore not an artifact of different bin endpoints or cumulative drift between bins.
- The equal-bin construction requires `N=2qrb`. The asymptotic exponent statements are along corresponding integer families and are not a uniform statement for arbitrary real-valued schedules `q(N),b(N)`.
- The square-root state/time threshold is specific to this control. No positive reconstruction theorem is claimed at `q~sqrt(N)` or `b~sqrt(N)`.
- The result does not refute an arithmetic theorem that combines binned transition data with additional Möbius-specific constraints. It identifies exactly what that extra theorem must exclude.
- No RH assumption, zero-free region, probabilistic independence, Mellin continuation, or `1/zeta` identity enters the derivation.

The exact claim can be falsified by finding one bin/residue/direction count that differs between `U` and `W`, by finding a bin with a nonzero endpoint, or by contradicting the area formulas `(14)`--`(16)`. Each bin contains exactly the same `r` positive and `r` negative complete residue cycles, so none occurs.

## Consequence for the line

The accepted mean-absolute transfer frontier can now reject another superficially promising information upgrade before arithmetic effort is invested in it. `MC-125` showed that sub-square-root local-memory histograms forget cycle order; `MC-127` showed that growing modular transition histograms forget integer lift order; `MC-128` shows that combining a sub-square-root modular state with a sub-square-root number of **ordered time bins** still forgets enough within-bin lift order to straddle square-root excursion scale.

The residual opportunity is narrower and more arithmetic: either obtain near-square-root-or-finer temporal/state resolution from a source-natural estimate without smuggling in Mertens control, or find a genuinely Möbius-specific nonlocal relation that makes such brute-force resolution unnecessary.