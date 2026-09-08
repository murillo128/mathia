# MC-155 — Simultaneous all-depth commutator row regularity is cancellation-blind

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue in the canonical number-state representation used in `MC-149`–`MC-154`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_k=\varepsilon_{pk},
\qquad
D_a\varepsilon_k=a_k\varepsilon_k.
\]

Enumerate without repetition all nonempty finite sets of distinct rational primes,

\[
F_1,F_2,F_3,\ldots,
\]

and write

\[
\Delta_i a(k)
=
\sum_{E\subseteq F_i}
(-1)^{|F_i|-|E|}
 a\!\left(k\prod_{p\in E}p\right).
\tag{1}
\]

Thus the mixed commutator from `MC-153`–`MC-154` satisfies

\[
C_{F_i}(a)\varepsilon_k
=
\Delta_i a(k)\,
\varepsilon_{P_i k},
\qquad
P_i=\prod_{p\in F_i}p.
\tag{2}
\]

`MC-154` proved that one support-matched linearly biased control can match Möbius in the norm, essential norm, compactness status, and finite-Schatten status of **every individual** mixed direction. It deliberately left open a natural escape: perhaps an external direct-sum norm that keeps many directions at the **same state** can distinguish Möbius because the sparse witnesses for different directions in `MC-154` need not coincide.

That magnitude-only escape also fails.

For every fixed integer `R_0\ge0`, there exists one bounded deterministic sequence `b=b_{R_0}` such that

\[
|b(n)|=\mu(n)^2
\qquad(n\ge1),
\tag{3}
\]

and

\[
b(n)=\mu(n)
\qquad
\text{for every squarefree }n\text{ with }\Omega(n)\le R_0,
\tag{4}
\]

while

\[
\boxed{
\sum_{n\le x}b(n)=\frac6{\pi^2}x+o(x).
}
\tag{5}
\]

Nevertheless there is an unbounded sequence of common marker states `q_j` such that, simultaneously for every `i\le j`,

\[
\boxed{
|\Delta_i b(q_j)|
=
|\Delta_i\mu(q_j)|
=2^{|F_i|}.
}
\tag{6}
\]

Consequently this **single control** fools every admissible weighted `\ell^r` simultaneous-state magnitude aggregation of the complete distinct-prime commutator hierarchy. More precisely, for `0<r<\infty` and weights `w=(w_i)` satisfying

\[
W_{w,r}^r
:=
\sum_{i\ge1}|w_i|^r2^{r|F_i|}
<\infty,
\tag{7}
\]

put

\[
R_{w,r}(a;k)
=
\left(
\sum_{i\ge1}|w_i|^r|\Delta_i a(k)|^r
\right)^{1/r}.
\tag{8}
\]

Then

\[
\boxed{
\sup_{k\ge1}R_{w,r}(b;k)
=
\limsup_{k\to\infty}R_{w,r}(b;k)
=W_{w,r}
=
\sup_{k\ge1}R_{w,r}(\mu;k)
=
\limsup_{k\to\infty}R_{w,r}(\mu;k).
}
\tag{9}
\]

For `r=\infty`, with

\[
W_{w,\infty}
:=
\sup_i |w_i|2^{|F_i|}<\infty,
\tag{10}
\]

and

\[
R_{w,\infty}(a;k)
=
\sup_i |w_i||\Delta_i a(k)|,
\]

the same equality holds with `W_{w,\infty}`.

The Hilbert direct-sum case is especially concrete. If

\[
\sum_i |w_i|^2 4^{|F_i|}<\infty,
\tag{11}
\]

define

\[
\mathcal R_w(a):\ell^2(\mathbb N)
\longrightarrow
\bigoplus_{i\ge1}\ell^2(\mathbb N)
\]

by

\[
\mathcal R_w(a)\varepsilon_k
=
\bigoplus_{i\ge1}
 w_i\Delta_i a(k)\,
 \varepsilon_{P_i k}.
\tag{12}
\]

For every nonzero admissible `w`,

\[
\boxed{
\|\mathcal R_w(b)\|
=
\|\mathcal R_w(b)\|_{\rm ess}
=
\|\mathcal R_w(\mu)\|
=
\|\mathcal R_w(\mu)\|_{\rm ess}
=
\left(\sum_i |w_i|^2 4^{|F_i|}\right)^{1/2}.
}
\tag{13}
\]

Both row operators are noncompact and belong to no finite Schatten class.

Thus **simultaneous state access does not rescue the all-depth commutator route once the joint directional vector is reduced to an unconditional magnitude norm**. The missing information, if this Bost–Connes/semigroup direction survives at all, must retain something that `(8)` and `(12)` discard: componentwise signs/phases, relational matrix coefficients, a source-forced coupling that is not an unconditional row magnitude, exact multiplicativity, or another structure capable of tying multiplicative parity to anchored additive order.

## 1. A nested sparse-cube construction synchronizes every finite prefix

For

\[
U_j:=\bigcup_{i\le j}F_i,
\qquad
A_j:=\sum_{h\le j}2^{|U_h|},
\tag{14}
\]
choose marker primes `q_j` recursively so that

1. `q_j\notin U_j`;
2. `q_j` is larger than every integer in every previously planted cube; and
3. `q_j>jA_j`.

There is always such a prime. Define the `j`-th nested multiplicative cube

\[
\mathcal C_j
=
\left\{
q_j\prod_{p\in E}p:E\subseteq U_j
\right\}.
\tag{15}
\]

Every point of `\mathcal C_j` is squarefree. The cubes are pairwise disjoint because every point of a later cube is at least its new marker prime, which was chosen above all points in all earlier cubes.

The planted union has density zero. Indeed, for

\[
q_j\le x<q_{j+1},
\]
no future cube contributes below `x`, while the total number of points available from the first `j` cubes is at most `A_j`. Hence

\[
\frac1x
\#\left(
[1,x]\cap\bigcup_{h\ge1}\mathcal C_h
\right)
\le
\frac{A_j}{q_j}
<\frac1j.
\tag{16}
\]

Let

\[
\mathcal L_{R_0}
=
\{n:n\text{ is squarefree and }\Omega(n)\le R_0\}.
\tag{17}
\]

As in `MC-154`, this fixed-depth squarefree set has density zero. Define

\[
b(n)=
\begin{cases}
0,
&n\text{ not squarefree},\\
\mu(n),
&n\in\mathcal L_{R_0}\cup\bigcup_j\mathcal C_j,\\
1,
&\text{otherwise}.
\end{cases}
\tag{18}
\]

Equations `(3)` and `(4)` are immediate. Since `b` differs from the squarefree indicator `\mu^2` only on a density-zero set, the classical squarefree asymptotic gives `(5)`.

This is the same adversarial principle as `MC-154`, but with a crucial change: the `j`-th planted cube contains **all primes occurring in the first `j` commutator directions**, not only the primes of one selected direction. That synchronizes the witnesses.

## 2. One marker simultaneously saturates the first `j` directions

Fix `j` and `i\le j`. Since `F_i\subseteq U_j`, every point

\[
q_j\prod_{p\in E}p,
\qquad E\subseteq F_i,
\]
belongs to `\mathcal C_j`. Therefore `(18)` gives

\[
b\!\left(q_j\prod_{p\in E}p\right)
=
\mu\!\left(q_j\prod_{p\in E}p\right).
\tag{19}
\]

Also `q_j\notin U_j`, so `q_j` is coprime to every prime in `F_i`. Hence

\[
\mu\!\left(q_j\prod_{p\in E}p\right)
=(-1)^{1+|E|}.
\tag{20}
\]

Substitution into `(1)` yields

\[
\begin{aligned}
\Delta_i b(q_j)
&=
\sum_{E\subseteq F_i}
(-1)^{|F_i|-|E|}(-1)^{1+|E|}\\
&=(-1)^{|F_i|+1}2^{|F_i|}.
\end{aligned}
\tag{21}
\]

The same computation holds for `\mu`, proving `(6)`. Since `q_j\to\infty`, every fixed finite prefix of directions attains its full coordinatewise oscillation at arbitrarily large **common** states.

This is exactly the feature absent from the sparse one-direction-at-a-time witness used in `MC-154`.

## 3. Every weighted `ell^r` magnitude row reaches the universal ceiling

For any bounded `a` with `\|a\|_\infty\le1`, equation `(1)` gives

\[
|\Delta_i a(k)|\le 2^{|F_i|}.
\tag{22}
\]

Therefore every admissible row satisfies

\[
R_{w,r}(a;k)\le W_{w,r}
\qquad(k\ge1).
\tag{23}
\]

For finite `r`, let

\[
W_{j,r}^r
=
\sum_{i\le j}|w_i|^r2^{r|F_i|}.
\tag{24}
\]

At the common marker `q_j`, equation `(6)` gives

\[
R_{w,r}(b;q_j)\ge W_{j,r},
\qquad
R_{w,r}(\mu;q_j)\ge W_{j,r}.
\tag{25}
\]

By monotone convergence, `W_{j,r}\uparrow W_{w,r}`. Combining `(23)` and `(25)` and using `q_j\to\infty` proves `(9)`.

For `r=\infty`, use instead

\[
W_{j,\infty}
=
\max_{i\le j}|w_i|2^{|F_i|}
\uparrow W_{w,\infty},
\]

and the same argument proves the endpoint case.

The construction of `b` does **not** depend on `r` or on the weights. Thus one and the same linearly biased sequence matches Möbius simultaneously for every finite or countably weighted `\ell^r` magnitude budget covered by `(7)` or `(10)`.

## 4. The Hilbert direct-sum operator has exactly the row magnitudes as singular data

For the operator `(12)`, distinct domain basis vectors have orthogonal images. Indeed, inside component `i`,

\[
k\ne \ell
\quad\Longrightarrow\quad
\varepsilon_{P_i k}\perp\varepsilon_{P_i\ell},
\]

and different components of the direct sum are orthogonal by construction. Consequently

\[
\mathcal R_w(a)^*\mathcal R_w(a)\,\varepsilon_k
=
R_{w,2}(a;k)^2\varepsilon_k.
\tag{26}
\]

Hence

\[
\|\mathcal R_w(a)\|
=
\sup_k R_{w,2}(a;k),
\tag{27}
\]

and the same finite-rank truncation argument used in `MC-149` gives

\[
\|\mathcal R_w(a)\|_{\rm ess}
=
\limsup_{k\to\infty}R_{w,2}(a;k).
\tag{28}
\]

Equations `(9)`, `(27)`, and `(28)` prove `(13)`.

Moreover,

\[
\mathcal R_w(a)\in\mathcal S_t
\quad\Longleftrightarrow\quad
\sum_{k\ge1}R_{w,2}(a;k)^t<\infty
\qquad(0<t<\infty).
\tag{29}
\]

For nonzero `w`, equation `(9)` gives positive limsup `W_{w,2}` for both `a=b` and `a=\mu`; therefore neither operator is compact and neither belongs to any finite Schatten class.

So even the most immediate external Hilbert-row completion of **all** mixed distinct-prime commutators has exactly the same scalar regularity signature for Möbius and for a sequence with positive linear mean.

## 5. What the theorem closes — and what it deliberately preserves

The result closes a precise loophole in `MC-154`. There, each mixed direction had a maximal witness somewhere, but different directions could peak at unrelated states. It was therefore legitimate to ask whether simultaneous state aggregation would create selectivity. The nested cubes show that this does not happen for unconditional magnitude aggregation: every finite directional prefix can peak together, and any summable infinite row norm is approximated from below by such prefixes.

The theorem does **not** identify the joint commutator vector itself. At `q_j`, equation `(21)` even records a definite sign pattern, and away from the planted cubes the componentwise coefficients for `b` and `\mu` can differ drastically. An operator or state that retains those signed matrix coefficients, their relative phases, or their exact location pattern is outside `(8)`–`(13)`.

This distinction is essential. If one retains enough componentwise coefficient data to reconstruct the complete squarefree parity field, the representation becomes target-complete rather than explanatory. A surviving relational proposal must therefore do two things at once: distinguish the biased controls through a source-forced joint relation, and prove that the retained relation is materially cheaper than reconstructing `\mu` itself.

The control is also intentionally nonmultiplicative. Exact multiplicativity together with squarefree support and the prime values `-1` determines Möbius. The point is not that arithmetic multiplicativity is irrelevant; it is that the entire all-depth **magnitude-regularity** hierarchy, even synchronized at common states, does not by itself exploit that arithmetic law.

## 6. Prior-art and novelty audit

The ambient Bost–Connes semigroup/crossed-product representation is classical. Laca and Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, realizes the Bost–Connes Hecke algebra as a semigroup crossed product and studies its representations. The canonical number-state semigroup action used here is already audited in `MC-138`–`MC-154`.

The operator facts in Section 4 are standard weighted-injection/direct-sum facts: orthogonal columns diagonalize `\mathcal R_w(a)^*\mathcal R_w(a)`, after which norm, essential norm, compactness, and Schatten membership reduce to the column lengths. `MC-149` contains the one-direction version and its prior-art boundary.

A targeted literature search for Bost–Connes mixed semigroup commutators, simultaneous direct-sum row norms, and Möbius cancellation did not locate this exact control construction or its information-boundary statement. No novelty inference is drawn from that absence. The synchronized sparse-cube argument is elementary and custom to the Mathia obstruction program, so the finding is recorded as `EXACT-DERIVED` and **makes no novelty claim**.

## Boundaries and falsification tests

- **Magnitude aggregation only.** The theorem covers unconditional `\ell^r` magnitudes and the Hilbert row regularity derived from them. It does not match signed component vectors, joint matrix coefficients, phases, or arbitrary nonlinear relational statistics.
- **Distinct-prime mixed directions only.** Repeated-prime commutators probe squareful directions and are not included. Möbius does not automatically saturate the same alternating-cube bound there.
- **External weights remain external.** The weights may be arbitrary subject to the displayed summability budget. If a source-derived operator couples directions non-diagonally rather than merely weighting their magnitudes, it requires a separate analysis.
- **The control is nonmultiplicative.** A theorem using exact multiplicativity in an essential way is not refuted by this construction.
- **Fixed initial parity can be preserved arbitrarily far.** `R_0` can be chosen as large as desired before constructing `b`, but it remains fixed. Agreement with Möbius at every squarefree factor depth would simply force agreement on all squarefree integers.
- **The bias is macroscopic.** The adversarial sequence has asymptotic mean `6/pi^2`, so this is not a small finite-range perturbation or numerical near-match.
- **No Mertens or RH consequence.** The theorem is a no-go for a representation-level scalarization. It neither bounds `M(x)` nor supplies evidence against RH.

A future proposal evades this finding only if its decisive statistic uses information not determined by the simultaneous row magnitudes above — for example signed/phase-sensitive joint coefficients, a non-unconditional coupling between directions, exact multiplicativity, or another source-forced relation — and then proves a non-tautological transfer to anchored Mertens excursion.

## Consequence for the line

The explicit direct-sum loophole left by `MC-154` is now closed at the natural scalar-regularity level. **It is not enough to move from separate all-depth commutator norms to simultaneous weighted row norms at a common state.** One support-matched sequence with positive linear bias saturates the same universal row ceilings as Möbius, for all finite prefixes and every summable weighted `\ell^r` completion.

The surviving Bost–Connes frontier is therefore narrower than “use joint state information.” It must use **relational signed information** that an unconditional magnitude row norm destroys, while remaining source-forced and cheaper than the complete Möbius parity lookup. That is the next meaningful proof obligation for this route.