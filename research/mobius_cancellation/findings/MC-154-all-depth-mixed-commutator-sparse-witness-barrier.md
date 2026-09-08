# MC-154 — Complete all-depth mixed prime-commutator scalar regularity is cancellation-blind

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue in the canonical number-state representation used in `MC-149`–`MC-153`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_k=\varepsilon_{pk},
\qquad
D_a\varepsilon_k=a_k\varepsilon_k,
\]

and, for every nonempty finite set `F` of distinct primes, let

\[
C_F(a)
=
\operatorname{ad}_{S_{p_r}}\cdots
\operatorname{ad}_{S_{p_1}}(D_a),
\qquad
P_F=\prod_{p\in F}p.
\tag{1}
\]

`MC-153` showed that every **fixed finite depth** can be matched by a support-preserving parity truncation with linear summatory bias. The control there depended on the chosen depth. The apparent escape was therefore to retain the entire hierarchy over all finite prime sets at once.

That escape also fails for the scalar regularity data of the individual mixed commutators.

For every fixed integer `R_0\ge0`, there exists one bounded deterministic sequence `b=b_{R_0}` such that

\[
|b(n)|=\mu(n)^2
\qquad(n\ge1),
\tag{2}
\]

and

\[
b(n)=\mu(n)
\qquad
\text{for every squarefree }n\text{ with }\Omega(n)\le R_0,
\tag{3}
\]

but, for **every** nonempty finite set `F` of distinct primes,

\[
\boxed{
\|C_F(b)\|
=
\|C_F(\mu)\|
=2^{|F|},
}
\tag{4}
\]

and even

\[
\boxed{
\|C_F(b)\|_{\rm ess}
=
\|C_F(\mu)\|_{\rm ess}
=2^{|F|}.
}
\tag{5}
\]

Consequently both `C_F(b)` and `C_F(\mu)` are noncompact and lie outside every finite Schatten class for every such `F`. Thus the complete unbounded-depth profile consisting of

- operator norms;
- essential norms;
- compact/noncompact status; and
- membership in any finite Schatten class

is identical for `b` and Möbius in every distinct-prime mixed direction.

Nevertheless `b` has positive linear summatory bias:

\[
\boxed{
B(x):=\sum_{n\le x}b(n)
=
\frac6{\pi^2}x+o(x).
}
\tag{6}
\]

Therefore **unbounded commutator depth by itself is not the missing Möbius selector once each direction is reduced to its own scalar regularity data**. The finite-depth control from `MC-153` was not merely failing because the depth cutoff was fixed. One fixed support-matched sequence can fool the entire all-depth norm/essential-norm/compactness/Schatten profile while having the opposite of Mertens cancellation.

A surviving Bost--Connes/semigroup route must retain joint state/location coherence between directions, a genuinely non-scalar or twisted relation, or another source-forced coupling not factored into separate scalar regularity summaries. It must then prove that this extra information is cheaper than reconstructing the full Möbius parity field.

## 1. Mixed commutators are weighted injections

For a finite distinct-prime set `F`, `MC-153` gives the exact mixed finite difference

\[
C_F(a)\varepsilon_k
=
\Delta_Fa(k)\,\varepsilon_{P_Fk},
\tag{7}
\]

where

\[
\Delta_Fa(k)
=
\sum_{E\subseteq F}
(-1)^{|F|-|E|}
 a\!\left(k\prod_{p\in E}p\right).
\tag{8}
\]

Since `k\mapsto P_Fk` is injective, the output basis vectors are orthogonal as `k` varies. Hence

\[
\|C_F(a)\|
=
\sup_{k\ge1}|\Delta_Fa(k)|
\le
2^{|F|}\|a\|_\infty.
\tag{9}
\]

The same weighted-injection structure used in `MC-149` gives

\[
\boxed{
\|C_F(a)\|_{\rm ess}
=
\limsup_{k\to\infty}|\Delta_Fa(k)|,
}
\tag{10}
\]

and for every finite `q>0`,

\[
C_F(a)\in\mathcal S_q
\quad\Longleftrightarrow\quad
\sum_{k\ge1}|\Delta_Fa(k)|^q<\infty.
\tag{11}
\]

Thus it is enough to plant infinitely many exact maximal mixed-difference witnesses for every finite prime direction while changing only a density-zero subset of the squarefree integers.

## 2. Sparse cubes can realize every finite prime direction simultaneously

The collection of nonempty finite sets of primes is countable. Choose a sequence

\[
F_1,F_2,F_3,\ldots
\tag{12}
\]

in which **every** such finite set occurs infinitely many times. Put

\[
A_j:=\sum_{i\le j}2^{|F_i|}.
\tag{13}
\]

Choose marker primes `q_j` recursively so that

1. `q_j\notin F_j`;
2. `q_j` is larger than every integer appearing in every previously planted cube; and
3. `q_j>jA_j`.

Such a prime always exists. Define the `j`-th multiplicative cube

\[
\mathcal C_j
=
\left\{
q_j\prod_{p\in E}p:E\subseteq F_j
\right\}.
\tag{14}
\]

Every element of `\mathcal C_j` is squarefree. The cubes are pairwise disjoint: every point of a later cube is at least its new marker prime, which by construction exceeds every point of every earlier cube.

Let

\[
\mathcal L_{R_0}
=
\{n:n\text{ is squarefree and }\Omega(n)\le R_0\}.
\tag{15}
\]

Now define

\[
b(n)=
\begin{cases}
0,
& n\text{ not squarefree},\\
\mu(n),
& n\in\mathcal L_{R_0}\cup\bigcup_{j\ge1}\mathcal C_j,\\
1,
& \text{otherwise}.
\end{cases}
\tag{16}
\]

Equations `(2)` and `(3)` are immediate. In particular, when `R_0\ge1`, the control agrees with Möbius on **every prime**, not merely on a finite selected prime set. Taking larger fixed `R_0` preserves any prescribed finite initial segment of the squarefree parity ladder without changing the construction below.

## 3. Every finite direction attains the Möbius norm at infinitely many markers

Fix one occurrence `F_j=F`. For each `E\subseteq F`, all vertices

\[
q_jP_E,
\qquad
P_E:=\prod_{p\in E}p,
\]

belong to the planted cube `\mathcal C_j`, so by `(16)`

\[
b(q_jP_E)
=
\mu(q_jP_E)
=
(-1)^{1+|E|}.
\tag{17}
\]

Substituting into `(8)` at `k=q_j` gives

\[
\begin{aligned}
\Delta_Fb(q_j)
&=
\sum_{E\subseteq F}
(-1)^{|F|-|E|}(-1)^{1+|E|}\\
&=
(-1)^{|F|+1}2^{|F|}.
\end{aligned}
\tag{18}
\]

Since `\|b\|_\infty=1`, the universal upper bound `(9)` is attained and therefore

\[
\|C_F(b)\|=2^{|F|}.
\tag{19}
\]

Because every finite `F` occurs infinitely many times in `(12)`, equation `(18)` holds along infinitely many marker primes tending to infinity. Equation `(10)` therefore gives

\[
\|C_F(b)\|_{\rm ess}=2^{|F|}.
\tag{20}
\]

For Möbius itself, choose any prime `q\notin F`. Then the same calculation gives

\[
\Delta_F\mu(q)=(-1)^{|F|+1}2^{|F|}.
\tag{21}
\]

There are infinitely many such primes, so

\[
\|C_F(\mu)\|
=
\|C_F(\mu)\|_{\rm ess}
=2^{|F|}.
\tag{22}
\]

Equations `(19)`–`(22)` prove `(4)`–`(5)`. They also show directly that for both sequences the coefficient family contains infinitely many values of magnitude `2^{|F|}`. Hence neither commutator is compact and the series in `(11)` diverges for every finite `q`, proving the complete scalar regularity match claimed above.

## 4. The planted witnesses have density zero

The construction only needs a vanishing-density set of squarefree exceptions to the constant positive background.

First, for each fixed `R_0`,

\[
|\mathcal L_{R_0}\cap[1,x]|=o(x).
\tag{23}
\]

This is the elementary fixed-prime-factor-count estimate already proved in `MC-153`: for fixed `y`, the number of prime divisors from `p\le y` has mean tending to `\sum_{p\le y}1/p` and variance at most that size; reciprocal-prime divergence then forces the density of integers with at most `R_0` distinct prime factors to zero. Restricting to squarefree integers only makes the set smaller.

Second, the union of planted cubes also has density zero. If

\[
q_j\le x<q_{j+1},
\]

then only cubes `\mathcal C_i` with `i\le j` can meet `[1,x]`, and therefore

\[
\left|
\left(\bigcup_i\mathcal C_i\right)\cap[1,x]
\right|
\le
\sum_{i\le j}|\mathcal C_i|
=
A_j.
\tag{24}
\]

By the marker condition `q_j>jA_j`,

\[
\frac{A_j}{x}
\le
\frac{A_j}{q_j}
<
\frac1j
\longrightarrow0.
\tag{25}
\]

Thus

\[
\left|
\left(\mathcal L_{R_0}\cup\bigcup_i\mathcal C_i\right)
\cap[1,x]
\right|
=o(x).
\tag{26}
\]

Outside that density-zero set, `b(n)=\mu(n)^2`. Since the classical squarefree-counting asymptotic recorded in `MC-S12` is

\[
Q(x):=\sum_{n\le x}\mu(n)^2
=
\frac6{\pi^2}x+o(x),
\tag{27}
\]

and `|b(n)-\mu(n)^2|\le2`, equations `(26)`–`(27)` give `(6)`.

The control therefore has not merely a larger-than-square-root exceptional excursion. It has a nonzero positive mean while reproducing the complete all-depth scalar mixed-commutator regularity profile.

## 5. Why this is stronger than the fixed-depth obstruction

`MC-153` constructed, for every fixed `R`, a control `b_R` that matched all mixed commutator norms through depth `R` and then froze the parity sign. That result left a precise logical gap: no **single** control in that family matched the full hierarchy over unbounded depth.

The sparse-cube construction closes exactly that gap. It does not try to match Möbius everywhere. Instead, it exploits the fact that an operator norm or essential norm only asks whether sufficiently large witnesses attain the extremal coefficient. A density-zero sequence of disjoint multiplicative cubes can realize the exact Möbius parity pattern required by **each** finite mixed difference, infinitely often, while the density-one squarefree background keeps constant positive sign.

This identifies the deeper information loss:

\[
\text{all finite multiplicative directions}
+
\text{separate extremal scalarization}
\quad\not\Rightarrow\quad
\text{global parity coherence}.
\tag{28}
\]

The obstruction is therefore not finite depth alone. It is the loss of **where the witnesses live and whether the same arithmetic states carry coherent information across directions and scales**.

## 6. Prior-art and novelty audit

The Bost--Connes semigroup representation and the use of its canonical isometries are established prior art already audited in `MC-138`–`MC-153`. `MC-149` also locates the nearby twisted-spectral-triple literature and records that weighted-injection norm, compactness, essential-norm, and Schatten criteria are standard operator-theoretic mechanisms. `MC-153` records that iterated distinct-prime commutators are ordinary mixed multiplicative finite differences.

For the present step, targeted searches for Bost--Connes iterated commutators, mixed prime finite differences, Möbius arithmetic, and sparse matched witnesses did not locate an established result with the exact all-depth construction `(12)`–`(27)`. That search absence is **not** treated as evidence of novelty. The construction is elementary once one asks what information separate supremum/essential-norm scalarizations retain, so no novelty claim is made.

The only asymptotic arithmetic input used in the proof is classical: fixed finite prime-factor-count sets have density zero as in `MC-153`, and squarefree integers have density `6/\pi^2` as recorded in `MC-S12`. No zero-free region, analytic continuation of `1/\zeta`, Mertens estimate, random model, or RH-equivalent input enters the obstruction.

## Boundaries and falsification tests

- **Distinct-prime mixed directions only.** The theorem classifies the hierarchy indexed by finite sets of distinct primes. Repeated-prime commutators probe squareful directions and are not covered by `(18)`; Möbius does not automatically saturate the same trivial bound there.
- **Separate scalar regularity only.** The theorem matches each direction's operator norm, essential norm, compactness status, and finite-Schatten status. It does **not** claim that the operators `C_F(b)` and `C_F(\mu)` coincide, nor that their matrix coefficients or joint state distributions match.
- **No arbitrary finite-`q` row equality.** Unlike the anchored fixed-depth control in `MC-153`, different directions here may attain their maxima on different sparse marker states. An external direct-sum norm that keeps simultaneous state information can therefore distinguish the two sequences. That is precisely an admissible escape from this obstruction rather than a counterexample to it.
- **The control is not multiplicative.** Exact multiplicativity together with squarefree support and the prime values `-1` already fixes Möbius. The result rules out conclusions based only on the stated represented scalar data; it does not say that every source-natural arithmetic relation is cancellation-blind.
- **Arbitrarily large fixed initial parity can be preserved.** The parameter `R_0` may be chosen as large as desired before constructing `b`, but it remains fixed. Requiring agreement with Möbius on all squarefree prime-factor depths would simply require agreement with Möbius on every squarefree integer.
- **Sparse planting is deterministic.** No independence, random-walk, density-one heuristic, or probabilistic transfer is used.
- **No Mertens or RH consequence.** The theorem is a no-go for one all-depth scalarization strategy. It supplies neither a new estimate for `M(x)` nor evidence against RH.

## Consequence for the line

The current local frontier should no longer describe **unbounded depth alone** as a plausible repair of the finite-depth Bost--Connes obstruction. The entire family of distinct-prime mixed commutators can be retained to every finite depth and still be cancellation-blind if the family is collapsed direction-by-direction to extremal scalar regularity.

The remaining Bost--Connes question is narrower and more structural: can a canonical construction retain **joint state-relational coherence** across prime directions or use a genuinely twisted/non-scalar coupling in a way that excludes the sparse planted controls, still admits Möbius, and yields an independently controlled bridge to first-absolute Mertens excursion? Any such proposal must also show that its retained data are not simply a disguised reconstruction of the full Möbius parity field.