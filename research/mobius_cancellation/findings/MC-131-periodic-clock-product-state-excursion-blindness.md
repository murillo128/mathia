# MC-131 — Periodic clock augmentation remains excursion-blind below the joint square-root scale

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISMS`, `NO-NOVELTY-CLAIM`.

## Claim

The product-state obstruction of `MC-129` survives a fine periodic time coordinate. Recording the position modulo a growing period does not by itself recover the macroscopic order of lifted cycles.

Fix integers

\[
k,q,m\ge 2,
\qquad r,b\ge 1,
\]

put

\[
d=\operatorname{lcm}(q,m),
\qquad
L=d\left\lceil\frac{k}{d}\right\rceil,
\tag{1}
\]

so that

\[
q\mid L,
\qquad
m\mid L,
\qquad
\max(k,d)\le L<k+d.
\tag{2}
\]

As in `MC-129`, write

\[
v=+^{k-1},
\qquad
A=+,
\qquad
B=-^k+^{k-1},
\tag{3}
\]

and define the two based macro-cycles

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

Both words have length

\[
N=2kLrb+k-1.
\tag{6}
\]

Partition the tail after the common prefix `v` into `b` consecutive bins of length `2kLr`. For a tail step `j`, let `C_Z(j-1)` be the preceding `k-1` increments, let

\[
S_Z(j-1)=\sum_{i<j}z_i,
\]

and retain also the deterministic clock phase

\[
\tau(j-1)=j-1\pmod m.
\tag{7}
\]

Define the bin-local clocked product-state tensor

\[
K_{Z,t}(u,a,c,\varepsilon)
=
\#\{j\text{ in bin }t:
C_Z(j-1)=u,\
S_Z(j-1)\equiv a\pmod q,\
\tau(j-1)=c,\
z_j=\varepsilon\}.
\tag{8}
\]

Then for every bin and every state/clock transition,

\[
\boxed{
K_{U,t}(u,a,c,\varepsilon)
=
K_{W,t}(u,a,c,\varepsilon).
}
\tag{9}
\]

Thus the controls remain indistinguishable after simultaneously retaining local memory, lifted height modulo `q`, a periodic time label modulo `m`, the next increment, and a coarse bin label. In particular every scalar observable

\[
\sum_{j\text{ in bin }t}
\Psi_t\!\left(
C_Z(j-1),
S_Z(j-1)\bmod q,
(j-1)\bmod m,
z_j
\right)
\tag{10}
\]

has the same value for `U` and `W`.

Nevertheless the exact first-absolute excursion means are still

\[
\boxed{
D_1(U)
=
\frac{\frac12k(k-1)+bLrk(Lr+k-1)}{2kLrb+k-1},
}
\tag{11}
\]

and

\[
\boxed{
D_1(W)
=
\frac{\frac12k(k-1)+bLrk(k+L-1)}{2kLrb+k-1}.
}
\tag{12}
\]

Hence, when `Lr/k -> infinity`,

\[
D_1(U)\sim \frac{Lr}{2},
\qquad
D_1(W)\sim \frac{k+L}{2}.
\tag{13}
\]

The construction therefore gives a periodic-time matched-control obstruction across square-root excursion scale. Let `R -> infinity`, choose

\[
k=R^{\alpha+o(1)},
\qquad
d=\operatorname{lcm}(q,m)=R^{\delta+o(1)},
\qquad
b=R^{\gamma+o(1)},
\]

write

\[
\ell=\max(\alpha,\delta),
\]

and take

\[
r=R^{1-\alpha-\ell-\gamma+o(1)}.
\tag{14}
\]

Whenever

\[
\ell<\frac12,
\qquad
\alpha+\gamma<\frac12,
\tag{15}
\]

one has `N=R^(1+o(1))` and

\[
D_1(U)=N^{1-\alpha-\gamma+o(1)}
      =N^{1/2+\Omega(1)},
\tag{16}
\]

while

\[
D_1(W)=N^{\ell+o(1)}
      =N^{1/2-\Omega(1)}.
\tag{17}
\]

The relevant periodic resolution is the **joint period** `lcm(q,m)`. Separate sub-square-root moduli can consume a larger joint budget when they are arithmetically incommensurate; conversely, when their least common multiple remains sub-square-root, adding the periodic clock does not close the excursion gap.

This is a representation-level matched-control obstruction. The words are not claimed to satisfy Möbius multiplicativity, the actual square-free support pattern, prime values, divisor relations, or any zeta-specific analytic constraint.

## 1. Exact closure in the clock-augmented product graph

Consider the directed graph with vertices

\[
(\eta,a,c)
\in
\{+,-\}^{k-1}
\times\mathbb Z/q\mathbb Z
\times\mathbb Z/m\mathbb Z
\]

and an edge labelled by `epsilon in {+1,-1}`

\[
(\eta_1\cdots\eta_{k-1},a,c)
\longrightarrow
(\eta_2\cdots\eta_{k-1}\varepsilon,
 a+\varepsilon,
 c+1).
\tag{18}
\]

Traversing an edge records exactly the quadruple counted by `(8)`. The first two coordinates are the product-state graph of `MC-129`; the third is a directed time cycle.

At the common state reached after the prefix `v`, `P=+^L` is a closed walk in all three coordinates. It preserves the local context, its lifted displacement is `+L`, which is `0 mod q`, and its length is `L`, which is `0 mod m`.

The word `B=-^k+^{k-1}` returns the local coordinate to `v` and has lifted displacement `-1`. Therefore `Q=B^L` returns the local coordinate, has lifted displacement `-L=0 mod q`, and has length `L(2k-1)=0 mod m`. Thus `P` and `Q` are closed walks based at the **same vertex of the full local-state/height/clock graph**.

Consequently `P^rQ^r` and `(PQ)^r` traverse exactly the same multiset of directed edges: both contain `r` copies of the closed walk `P` and `r` copies of the closed walk `Q`, differing only in their macro-order. Repeating the construction in every bin proves `(9)`. Each bin also returns to the same lifted height, local suffix, and clock phase, so there is no boundary mismatch carrying the excursion separation.

The failure mechanism is unchanged from `MC-129`: the empirical edge multiset remembers which transition occurred at which periodic phase, but forgets the **order in which whole based cycles with the same boundary state were concatenated**.

## 2. Periodic weights and finite families of clocks are already included

Any deterministic weight of period `m` is a function of the clock coordinate. Hence `(9)` covers not just a label but every periodically weighted local/state statistic of the form `(10)`. Oscillatory factors such as

\[
e^{2\pi i a(j-1)/m}
\]

or arbitrary functions on `Z/mZ` do not escape the obstruction when the remaining observable factors through the clocked empirical transition tensor.

Likewise a finite family of periodic clocks with periods

\[
m_1,\ldots,m_s
\]

is equivalent to one clock of period

\[
M=\operatorname{lcm}(m_1,\ldots,m_s).
\tag{19}
\]

The same proof applies after replacing `m` by `M`. Thus adding finitely many periodic phases is not a genuinely ordered carrier; only their joint period matters for this control family.

This does **not** cover arbitrary deterministic weights or absolute timestamps. A nonperiodic/adaptive weight can distinguish two reorderings even when all fixed periodic phases agree, and the theorem makes no claim that such information is sufficient for Möbius cancellation.

## 3. Finite-horizon path types do not reopen the periodic-clock route

Combine the present state augmentation with `MC-130`. An `h`-step path type starting with local memory `k_0-1` folds into a one-step type with effective context

\[
K=k_0+h-1.
\tag{20}
\]

If the path type also records its starting position modulo `m`, the enlarged terminal state records the terminal clock phase, from which the starting phase is recovered by subtracting `h-1 mod m`. The intermediate clock phases are then deterministic. The modular-height coordinate is recovered exactly as in `MC-130`.

Therefore a finite or growing finite-horizon empirical path histogram augmented by periodic position modulo `m` is still a projection of a one-step tensor of the form `(8)` after replacing `k` by `K`. The same square-root obstruction applies whenever the effective context, joint height/clock period, and bin resolution satisfy `(15)`.

So the immediate escape left after `MC-130` can be narrowed further: **finite-horizon path information plus periodic timing is still not occurrence order**.

## 4. Prior art and novelty assessment

Both component languages are classical. `MC-S41` records that Markov types are empirical transition-count matrices / balanced directed multigraphs. Adding a periodic position coordinate is also established combinatorics on words rather than a new graph construction.

Nicolás Álvarez, Verónica Becher, Pablo A. Ferrari and Sergio A. Yuhjtman, *Perfect necklaces*, Advances in Applied Mathematics 80 (2016), 48–61, DOI `10.1016/j.aam.2016.05.002`, define `(k,n)`-perfect necklaces by requiring each length-`k` word to occur at positions that are distinct modulo `n`. This is exactly the classical idea of coupling a local word state to a periodic position class.

Nicolás Álvarez, Verónica Becher, Martín Mereb, Ivo Pajor and Carlos Miguel Soto, *On extremal factors of de Bruijn-like graphs*, Discrete Applied Mathematics 357 (2024), 352–364, DOI `10.1016/j.dam.2024.06.010`, studies the tensor product of a de Bruijn graph with a simple cycle. That product is the graph-theoretic clock factor used in `(18)` before crossing it with the additional modular-height coordinate.

Accordingly, **no novelty is claimed** for Markov types, periodic-position types, perfect necklaces, astute/de-Bruijn-cycle product graphs, state augmentation, or reordering common based cycles. The durable Mathia result is the exact consequence for the existing `MC-129` controls: a periodic time coordinate, even growing and cross-coupled with local and modular state, still admits representatives on opposite sides of square-root excursion scale whenever the joint period remains below the explicit threshold.

## Boundaries and falsification tests

- The clock is periodic, not an absolute timestamp. Exact positions, nonperiodic/adaptive schedules, and full occurrence order are outside the quotient.
- The relevant closure scale is `d=lcm(q,m)`, not `max(q,m)`. A proposal using several apparently small periodic moduli must account for their joint least-common-multiple resolution before invoking this obstruction.
- Equality is for the complete clocked product-state transition tensor separately inside each coarse bin. Any statistic that factors through that tensor is matched; a statistic retaining the ordered list of its edge occurrences need not be.
- The finite-horizon extension covers empirical path **types**, not the ordered trajectory of those path types.
- The controls do not preserve Möbius multiplicativity, square-free placement, prime/divisor labels, or arithmetic constraints. An arithmetic theorem forbidding the common-cycle reorderings remains a genuine escape.
- The square-root boundary is a kill threshold for this explicit family, not a reconstruction theorem at or above the threshold.
- No `1/zeta` identity, contour shift, RH-equivalent estimate, probabilistic independence assumption, or numerical coincidence enters the proof.

## Consequence for the line

`MC-128` showed that coarse temporal bins do not recover excursion amplitude, `MC-129` matched the full contemporaneous local/modular product state inside each bin, and `MC-130` folded finite-horizon empirical paths back into longer one-step types. The present result closes another natural repair: **adding periodic phase information inside the bins still leaves macro-cycle order invisible**.

A surviving timing-based source mechanism must therefore retain genuinely nonperiodic/absolute/adaptive occurrence information, a nested multiscale order relation that cannot be flattened into a periodic finite-state type at the available joint resolution, or Möbius-specific arithmetic structure that forbids the matched reorderings. Merely attaching one or finitely many periodic clocks to the existing local/state/path summaries is not such a carrier.