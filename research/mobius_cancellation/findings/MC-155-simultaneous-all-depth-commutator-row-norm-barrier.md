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

The same synchronized markers also close a narrower **phase-sensitive cluster** loophole. Define the normalized signed all-depth row

\[
U(a;k)
=
\left(2^{-|F_i|}\Delta_i a(k)\right)_{i\ge1}
\in[-1,1]^{\mathbb N}
\tag{14}
\]

and the signed corner

\[
s=
\left((-1)^{|F_i|+1}\right)_{i\ge1}.
\tag{15}
\]

Then the same marker sequence satisfies

\[
\boxed{
U(b;q_j)\longrightarrow s,
\qquad
U(\mu;q_j)\longrightarrow s
}
\tag{16}
\]

in the product topology. Hence every product-topology continuous signed/phase-sensitive scalarization has the same subsequential marker limit on `b` and Möbius. For any `1\le r<\infty` and weights satisfying `(7)`, the stronger weighted signed rows

\[
V_w(a;k)=\left(w_i\Delta_i a(k)\right)_{i\ge1}
\tag{17}
\]

converge in `\ell^r` along the same markers to

\[
v_w^*
=
\left(w_i(-1)^{|F_i|+1}2^{|F_i|}\right)_{i\ge1}.
\tag{18}
\]

If instead `|w_i|2^{|F_i|}\to0`, the analogous convergence holds in the weighted `\ell^\infty`/`c_0` endpoint. Thus merely retaining signs or phases does not help if the proposed statistic uses only the existence or continuous topology of one-state all-depth row clusters. A surviving phase-sensitive mechanism must use information not fixed by this common cluster — for example the **frequency/distribution** of signed rows, relations between different base states or scales, additive location/order, exact multiplicativity, or another source-forced nonlocal coupling.

Thus **simultaneous state access does not rescue the all-depth commutator route once the joint directional vector is reduced either to an unconditional magnitude norm or to continuous one-state cluster data**. The result does not identify the full signed field, but it narrows what a genuinely relational Bost–Connes/semigroup escape must retain.

## 1. A nested sparse-cube construction synchronizes every finite prefix

For

\[
U_j:=\bigcup_{i\le j}F_i,
\qquad
A_j:=\sum_{h\le j}2^{|U_h|},
\tag{19}
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
\tag{20}
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
\tag{21}
\]

Let

\[
\mathcal L_{R_0}
=
\{n:n\text{ is squarefree and }\Omega(n)\le R_0\}.
\tag{22}
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
\tag{23}
\]

Equations `(3)` and `(4)` are immediate. Since `b` differs from the squarefree indicator `\mu^2` only on a density-zero set, the classical squarefree asymptotic gives `(5)`.

This is the same adversarial principle as `MC-154`, but with a crucial change: the `j`-th planted cube contains **all primes occurring in the first `j` commutator directions**, not only the primes of one selected direction. That synchronizes the witnesses.

## 2. One marker simultaneously saturates the first `j` directions with the same signs

Fix `j` and `i\le j`. Since `F_i\subseteq U_j`, every point

\[
q_j\prod_{p\in E}p,
\qquad E\subseteq F_i,
\]
belongs to `\mathcal C_j`. Therefore `(23)` gives

\[
b\!\left(q_j\prod_{p\in E}p\right)
=
\mu\!\left(q_j\prod_{p\in E}p\right).
\tag{24}
\]

Also `q_j\notin U_j`, so `q_j` is coprime to every prime in `F_i`. Hence

\[
\mu\!\left(q_j\prod_{p\in E}p\right)
=(-1)^{1+|E|}.
\tag{25}
\]

Substitution into `(1)` yields

\[
\begin{aligned}
\Delta_i b(q_j)
&=
\Delta_i\mu(q_j)\\
&=
\sum_{E\subseteq F_i}
(-1)^{|F_i|-|E|}(-1)^{1+|E|}\\
&=(-1)^{|F_i|+1}2^{|F_i|}.
\end{aligned}
\tag{26}
\]

This proves `(6)` and strengthens its magnitude statement to exact signed equality on every synchronized finite prefix. Since `q_j\to\infty`, every fixed finite prefix attains the same fully oriented corner for `b` and Möbius at arbitrarily large common states.

This is exactly the feature absent from the sparse one-direction-at-a-time witness used in `MC-154`.

## 3. Every weighted `ell^r` magnitude row reaches the universal ceiling

For any bounded `a` with `\|a\|_\infty\le1`, equation `(1)` gives

\[
|\Delta_i a(k)|\le 2^{|F_i|}.
\tag{27}
\]

Therefore every admissible row satisfies

\[
R_{w,r}(a;k)\le W_{w,r}
\qquad(k\ge1).
\tag{28}
\]

For finite `r`, let

\[
W_{j,r}^r
=
\sum_{i\le j}|w_i|^r2^{r|F_i|}.
\tag{29}
\]

At the common marker `q_j`, equation `(6)` gives

\[
R_{w,r}(b;q_j)\ge W_{j,r},
\qquad
R_{w,r}(\mu;q_j)\ge W_{j,r}.
\tag{30}
\]

By monotone convergence, `W_{j,r}\uparrow W_{w,r}`. Combining `(28)` and `(30)` and using `q_j\to\infty` proves `(9)`.

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
\tag{31}
\]

Hence

\[
\|\mathcal R_w(a)\|
=
\sup_k R_{w,2}(a;k),
\tag{32}
\]

and the same finite-rank truncation argument used in `MC-149` gives

\[
\|\mathcal R_w(a)\|_{\rm ess}
=
\limsup_{k\to\infty}R_{w,2}(a;k).
\tag{33}
\]

Equations `(9)`, `(32)`, and `(33)` prove `(13)`.

Moreover,

\[
\mathcal R_w(a)\in\mathcal S_t
\quad\Longleftrightarrow\quad
\sum_{k\ge1}R_{w,2}(a;k)^t<\infty
\qquad(0<t<\infty).
\tag{34}
\]

For nonzero `w`, equation `(9)` gives positive limsup `W_{w,2}` for both `a=b` and `a=\mu`; therefore neither operator is compact and neither belongs to any finite Schatten class.

So even the most immediate external Hilbert-row completion of **all** mixed distinct-prime commutators has exactly the same scalar regularity signature for Möbius and for a sequence with positive linear mean.

## 5. Signed all-depth rows share a common phase-sensitive cluster point

The exact signed equality `(26)` is stronger than the magnitude statement used to prove `(9)`. Normalize the complete row by `(14)`. For each fixed coordinate `i`, once `j\ge i`, equation `(26)` gives

\[
2^{-|F_i|}\Delta_i b(q_j)
=
2^{-|F_i|}\Delta_i\mu(q_j)
=(-1)^{|F_i|+1}.
\tag{35}
\]

Every coordinate of `U(a;k)` lies in `[-1,1]`, so `(35)` is exactly coordinatewise convergence to the corner `s` in `(15)`. This proves `(16)` in the product topology.

Therefore, if

\[
\Phi:[-1,1]^{\mathbb N}\to Y
\]

is continuous for the product topology into any Hausdorff space `Y`, then

\[
\Phi(U(b;q_j))\to\Phi(s),
\qquad
\Phi(U(\mu;q_j))\to\Phi(s).
\tag{36}
\]

This includes every continuous finite-coordinate signed readout and every other continuous scalarization of the normalized one-state row. Merely avoiding absolute values therefore does **not** recover selectivity if the statistic ultimately asks only for a continuous cluster property of that row.

There is also a normed weighted version. For `1\le r<\infty` under `(7)`, define `V_w` by `(17)` and `v_w^*` by `(18)`. The first `j` coordinates agree exactly with `v_w^*` at `q_j`, while every remaining coordinate satisfies the trivial bound

\[
|w_i\Delta_i a(q_j)-w_i(-1)^{|F_i|+1}2^{|F_i|}|
\le 2|w_i|2^{|F_i|}
\qquad(a=b,\mu).
\]

Hence

\[
\boxed{
\|V_w(a;q_j)-v_w^*\|_{\ell^r}
\le
2\left(
\sum_{i>j}|w_i|^r2^{r|F_i|}
\right)^{1/r}
\longrightarrow0
}
\tag{37}
\]

for both `a=b` and `a=\mu`. In particular,

\[
\|V_w(b;q_j)-V_w(\mu;q_j)\|_{\ell^r}
\le
2\left(
\sum_{i>j}|w_i|^r2^{r|F_i|}
\right)^{1/r}
\longrightarrow0.
\tag{38}
\]

At the sup endpoint, the same proof gives convergence whenever

\[
|w_i|2^{|F_i|}\longrightarrow0,
\tag{39}
\]

because the right-hand tail becomes `2\sup_{i>j}|w_i|2^{|F_i|}`. This is the natural `c_0` endpoint. Mere boundedness of `|w_i|2^{|F_i|}` is **not** enough for signed sup-norm convergence, so the broader magnitude-only `r=\infty` theorem `(10)` remains strictly stronger in that different sense.

The conclusion is deliberately topological, not distributional. The construction forces one common signed all-depth cluster point at unbounded marker states; it does not match how often row states occur, their empirical/KMS distribution, relations between two different base states, or additive placement of the markers. Those are genuine escape routes rather than hidden assumptions of `(16)`–`(39)`.

## 6. What the theorem closes — and what it deliberately preserves

The result closes two nested loopholes in `MC-154`. First, different mixed directions need not peak at unrelated states: nested cubes make every finite directional prefix peak together, so unconditional magnitude aggregation remains blind. Second, simply retaining the componentwise signs at those common states is still insufficient at the level of continuous cluster data: the same markers converge to the same fully oriented all-depth corner for the linearly biased control and for Möbius.

The theorem does **not** identify the full joint commutator field. Away from the planted cubes the componentwise coefficients for `b` and `\mu` can differ drastically, and `(36)` says nothing about the frequency or measure of the common cluster. An operator or state that retains signed coefficient distributions, correlations between different base states, exact location/order, or a source-forced coupling across states is outside the obstruction.

This distinction is essential. If one retains enough componentwise coefficient data to reconstruct the complete squarefree parity field, the representation becomes target-complete rather than explanatory. A surviving relational proposal must therefore do two things at once: distinguish the biased controls through a source-forced joint relation not reduced to common one-state cluster topology, and prove that the retained relation is materially cheaper than reconstructing `\mu` itself.

The control is also intentionally nonmultiplicative. Exact multiplicativity together with squarefree support and the prime values `-1` determines Möbius. The point is not that arithmetic multiplicativity is irrelevant; it is that the entire all-depth magnitude hierarchy and even its maximally oriented common cluster can coexist with positive linear summatory bias when those source laws are not enforced.

## 7. Prior-art and novelty audit

The ambient Bost–Connes semigroup/crossed-product representation is classical. Laca and Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, realizes the Bost–Connes Hecke algebra as a semigroup crossed product and studies its representations. The canonical number-state semigroup action used here is already audited in `MC-138`–`MC-154`.

The operator facts in Section 4 are standard weighted-injection/direct-sum facts: orthogonal columns diagonalize `\mathcal R_w(a)^*\mathcal R_w(a)`, after which norm, essential norm, compactness, and Schatten membership reduce to the column lengths. `MC-149` contains the one-direction version and its prior-art boundary.

The signed-cluster strengthening in Section 5 uses only the exact synchronized equality `(26)`, product-topology convergence, and an elementary summable-tail estimate. A targeted literature search across Bost–Connes mixed semigroup commutators, twisted/spectral-triple commutator work, signed row observables, and Möbius cancellation located the established Bost–Connes/crossed-product and twisted-spectral-triple frameworks but no direct theorem matching this sparse-control cluster statement. No novelty inference is drawn from that absence. The synchronized sparse-cube and cluster arguments are recorded as `EXACT-DERIVED` and **make no novelty claim**.

## Boundaries and falsification tests

- **Magnitude regularity plus one common signed cluster.** The theorem matches unconditional `\ell^r` magnitude ceilings and proves a common signed all-depth cluster point. It does **not** match the complete signed row field, its distribution, joint matrix coefficients, or arbitrary nonlinear relational statistics across states.
- **Product-continuous readouts only for the phase-sensitive statement.** A discontinuous functional designed to detect rare coordinates or exact global row identity is outside `(36)`. Such a functional must still be shown source-natural and cheaper than reconstructing the target.
- **Weighted signed norm convergence has a tail condition.** For finite `r`, `(7)` suffices. At `r=\infty`, signed convergence is claimed only under the stronger `c_0` condition `(39)`; bounded weighted rows alone need not converge in sup norm.
- **Distinct-prime mixed directions only.** Repeated-prime commutators probe squareful directions and are not included. Möbius does not automatically saturate the same alternating-cube bound there.
- **External weights remain external.** The weights may be arbitrary subject to the displayed budgets. If a source-derived operator couples directions non-diagonally or aggregates across different base states, it requires a separate analysis.
- **The control is nonmultiplicative.** A theorem using exact multiplicativity in an essential way is not refuted by this construction.
- **Fixed initial parity can be preserved arbitrarily far.** `R_0` can be chosen as large as desired before constructing `b`, but it remains fixed. Agreement with Möbius at every squarefree factor depth would simply force agreement on all squarefree integers.
- **The bias is macroscopic.** The adversarial sequence has asymptotic mean `6/pi^2`, so this is not a small finite-range perturbation or numerical near-match.
- **No Mertens or RH consequence.** The theorem is a no-go for a representation-level scalarization/topology. It neither bounds `M(x)` nor supplies evidence against RH.

A future proposal evades this finding only if its decisive statistic uses information not determined by the simultaneous magnitude rows **or by the common signed cluster above** — for example signed-row frequency measures, correlations between distinct base states/scales, additive location/order, a non-unconditional source coupling, exact multiplicativity, or another source-forced relation — and then proves a non-tautological transfer to anchored Mertens excursion.

## Consequence for the line

The explicit direct-sum loophole left by `MC-154` is now closed at the natural scalar-regularity level, and the simplest phase-sensitive repair is narrower than previously stated. **It is not enough to move from separate all-depth commutator norms to simultaneous weighted row norms at a common state, nor merely to retain the signed row as a continuous cluster observable.** One support-matched sequence with positive linear bias shares Möbius's universal magnitude ceilings and the same maximally oriented all-depth cluster point.

The surviving Bost–Connes frontier must therefore use **relational signed information across states/scales or a source law such as exact multiplicativity**, rather than one-state row magnitude or cluster topology, while remaining source-forced and cheaper than the complete Möbius parity lookup. That is the next meaningful proof obligation for this route.