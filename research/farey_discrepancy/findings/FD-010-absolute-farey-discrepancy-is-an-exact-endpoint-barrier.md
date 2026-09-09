# FD-010 — absolute Farey discrepancy is an exact endpoint barrier

**Status:** `LITERATURE+CLASSICAL-EXACT + ENDPOINT-LOCALIZATION + NORM-SEPARATION + NEGATIVE/OBSTRUCTION`. `FD-002` identifies the Franel quadratic discrepancy with a cumulative Mertens energy, and `FD-003`--`FD-009` show how difficult it is to obtain a stronger scalar extraction after denominator-shell compression. A natural apparent escape is to replace the quadratic discrepancy by a stronger pointwise norm before looking for finer ordered structure. For the ordinary absolute/star discrepancy of the complete Farey sequence, that route is already closed classically: François Dress proved that the normalized absolute discrepancy of order `n` is **exactly** `1/n` for every `n`.

The equality is not an RH-sensitive cancellation phenomenon. Its lower bound is forced by the first empty interval before the smallest positive Farey fraction `1/n`; Dress proves that no interior point produces a larger discrepancy. Thus the complete `L^infty` discrepancy is pinned by endpoint geometry at the unconditional `N_n^{-1/2}` scale. Replacing the Franel--Landau average/quadratic discrepancy by this supremum therefore destroys, rather than strengthens, the cumulative arithmetic sensitivity that the line is trying to exploit.

## 1. The first Farey gap already forces the exact scale

Let

\[
\mathcal F_n
=\left\{\frac pq:1\le p\le q\le n,\ (p,q)=1\right\}
\]

be the positive Farey fractions of order `n`, written increasingly, and put

\[
N_n:=|\mathcal F_n|=\sum_{q\le n}\varphi(q).
\tag{1}
\]

For `0<\alpha\le1`, write `A_n(\alpha)` for the number of terms of `mathcal F_n` not exceeding `alpha`, and define the normalized local discrepancy

\[
R_n(\alpha)
:=\left|\alpha-\frac{A_n(\alpha)}{N_n}\right|,
\qquad
R_n^\infty:=\sup_{0<\alpha\le1}R_n(\alpha),
\tag{2}
\]

with the usual harmless one-sided convention at jumps. Dress's 1999 theorem is

\[
\boxed{R_n^\infty=\frac1n\qquad(n\ge1).}
\tag{3}
\]

The lower-bound mechanism is elementary and geometric. The smallest positive fraction in `mathcal F_n` is `1/n`. Hence for every

\[
0<\alpha<\frac1n
\]

there is no Farey point in `(0,alpha]`, so

\[
A_n(\alpha)=0,
\qquad
R_n(\alpha)=\alpha.
\tag{4}
\]

Letting `alpha` increase to `1/n` from the left gives

\[
\boxed{R_n^\infty\ge\frac1n.}
\tag{5}
\]

If discrepancy is encoded using the left-continuous empirical count instead, the same value is attached directly to the abscissa `1/n`; this is the convention reflected in Dress's statement that the absolute discrepancy equals the local value at that abscissa. The distinction is only the finite jump convention, not the supremum or the endpoint mechanism.

## 2. Dress proves that the endpoint lower bound is globally sharp

The nontrivial half of (3) is the global upper bound

\[
\boxed{R_n(\alpha)\le\frac1n
\quad\text{for every }0<\alpha\le1.}
\tag{6}
\]

Dress proves this exactly, using in particular an integral estimate involving the summatory Möbius function. Combining (5) and (6) leaves no room for a smaller constant, an improved exponent, or a hidden interior maximizer: the complete normalized absolute discrepancy is already determined for every finite order.

Since

\[
N_n=\frac{3}{\pi^2}n^2+O(n\log n),
\tag{7}
\]

one has

\[
\boxed{
R_n^\infty
=\frac{\sqrt3}{\pi\sqrt{N_n}}\,(1+o(1)).
}
\tag{8}
\]

This `N_n^{-1/2}` scale is therefore unconditional and endpoint-forced. It cannot by itself encode the RH-critical improvement carried by the Franel--Landau discrepancy criteria.

## 3. The `L^infty` norm and the Franel quadratic statistic retain different information

The exact result must not be confused with `FD-002`. If

\[
0<x_1<\cdots<x_{N_n}=1
\]

are the ordered positive Farey fractions, the Franel quadratic statistic studied there is

\[
\mathfrak F_n
=\sum_{j=1}^{N_n}
\left(x_j-\frac{j}{N_n}\right)^2.
\tag{9}
\]

At every sample point, Dress's theorem gives the elementary bound

\[
\left|x_j-\frac{j}{N_n}\right|\le\frac1n
\tag{10}
\]

up to the same endpoint-count convention. Summing its square yields only

\[
\mathfrak F_n\le\frac{N_n}{n^2}=O(1),
\tag{11}
\]

which does not supply the decaying cumulative control sought by the Franel--Landau criterion. The reason is structural: a supremum asks for the single largest deviation, while `mathfrak F_n` accumulates the complete ordered discrepancy path. An endpoint gap can determine the first quantity while contributing only one small part of the second.

This gives an exact norm-separation warning for the line. A pointwise norm can look formally stronger than an averaged norm but be arithmetically weaker when its extremum is dominated by a universal boundary feature. Any proposed norm change therefore has to preserve the cumulative or interior information needed by the RH-facing implication; monotonicity of norms alone is irrelevant.

## 4. Consequence for the ordered Farey frontier

Equation (3) closes one broad class of apparent geometric upgrades. Any candidate whose final invariant is only the complete absolute discrepancy

\[
\sup_\alpha
\left|\alpha-\frac{A_n(\alpha)}{N_n}\right|
\]

cannot reveal a new Farey cancellation mechanism: its value is already fixed exactly by the endpoint barrier. Likewise, showing that some ordered representation reconstructs this `L^infty` quantity is not additional arithmetic information.

This does **not** close the live ordered routes in the local Mind. Interior-restricted observables, adjacency or mediant/refinement data, spectral allocation, multiscale signed fields, and the full Franel discrepancy may retain information that the supremum forgets. In particular `CLUE-farey-gap-order-bridge-suppression.md` deliberately tests spectral allocation after separating global amplitude and fixed endpoint layers; Dress's theorem neither proves nor refutes that residual. It does impose a clean falsification control: if a proposed ordered carrier eventually scalarizes only to the complete absolute discrepancy, the route has collapsed to a known endpoint quantity.

The same distinction applies to endpoint excision. Removing the first and last Farey gaps can make an interior supremum nontrivial, but that is a **different observable** whose relation to the RH-equivalent Franel criterion must be proved rather than inherited from (3).

## 5. Prior art and audit boundary

The exact theorem is classical. François Dress, *Discrépance des suites de Farey*, Journal de théorie des nombres de Bordeaux **11**(2) (1999), 345--367, MR 1745884, proves that the absolute discrepancy of the Farey sequence of order `n` is exactly `1/n`; the stable primary archive is `https://www.numdam.org/item/JTNB_1999__11_2_345_0/`. Dress explicitly presents the result as sharpening the earlier discrepancy estimates of Niederreiter. No novelty is claimed for the theorem, its endpoint value, or the standard asymptotic (7).

The Mathia-specific result is the research-boundary splice with `FD-002`--`FD-009`: **the complete `L^infty` Farey discrepancy is not a stronger RH-facing replacement for the cumulative Franel discrepancy, because its exact finite value is already saturated by endpoint geometry.** That closes a natural but misleading norm-upgrade route and narrows any genuinely new ordered mechanism to information that survives before this endpoint scalarization.

Several conventions must remain explicit. Dress's Farey sequence is the positive sequence ending at `1`; including `0`, changing whether empirical counts are left- or right-continuous, or using another star-discrepancy convention can move individual jump values by `O(1/N_n)`, but does not change the endpoint `1/n` supremum after the definitions are reconciled. The theorem says nothing by itself about the asymptotics of `mathfrak F_n`, the spectral-allocation clue, sparse divisor-horizon constraints, or RH. Its durable consequence is an exact negative boundary on what the absolute discrepancy can carry.