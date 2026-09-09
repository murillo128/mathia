# AF-229 — perfect prime-tail proximity graphs split stochastic information exactly

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-THEOREM-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `ZERO-ERROR`, `GRAPH-ENTROPY`, `PERFECT-GRAPH`, `PRIME-TAIL`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-227 and AF-228 price two deterministic marking duties on the rational-prime log-log source: separating nearby source points and localizing a source point. AF-228 obtains the finite inequality

\[
E_Q(r)+R_Q(r/2,0)\ge \log \pi(Q)
\tag{1}
\]

and an asymptotically exact split on polynomial resolution scales, but explicitly leaves the stochastic/Körner graph-entropy relaxation outside its claim.

That boundary can be closed exactly.

For `Q>=3`, let

\[
S_Q:=\{-\log\log p:p\le Q,\ p\text{ prime}\},
\tag{2}
\]

and let `P` be **any** probability distribution on `S_Q`. Let `X\sim P`. For `r>0`, write `G_{Q,r}` for the proximity graph with vertex set `S_Q` and an edge between distinct `x,y` exactly when

\[
|x-y|\le r.
\tag{3}
\]

Define the stochastic zero-error **separation information**

\[
\mathsf S_{Q,P}(r)
:=
\inf I(X;M),
\tag{4}
\]

where the infimum is over arbitrary finite-valued stochastic marks `P_{M|X}` such that, for every mark value `m` with positive probability, its posterior support

\[
A_m:=\{x\in S_Q:\Pr(M=m\mid X=x)>0\}
\tag{5}
\]

is an independent set of `G_{Q,r}`. Thus a single realized mark never leaves two source points at distance at most `r` mutually possible.

Define also the stochastic zero-error **localization information**

\[
\mathsf L_{Q,P}(r/2)
:=
\inf I(X;M),
\tag{6}
\]

where the infimum is over arbitrary stochastic marks together with a decoder `d` satisfying

\[
|X-d(M)|\le r/2
\qquad\text{almost surely.}
\tag{7}
\]

Then

\[
\boxed{
\mathsf S_{Q,P}(r)=H(G_{Q,r},P),
\qquad
\mathsf L_{Q,P}(r/2)=H(\overline{G_{Q,r}},P),
}
\tag{8}
\]

where `H(G,P)` is Körner graph entropy.

The graph `G_{Q,r}` is a unit interval graph: represent `x\in S_Q` by the interval `[x-r/2,x+r/2]`. Hence it is an interval graph and therefore perfect. The Csiszár--Körner--Lovász--Marton--Simonyi entropy-splitting theorem for perfect graphs therefore gives, for every finite `Q`, every `r>0`, and every source law `P`,

\[
\boxed{
\mathsf S_{Q,P}(r)+\mathsf L_{Q,P}(r/2)=H(P).
}
\tag{9}
\]

Thus the stochastic relaxation turns AF-228's deterministic lower bound into an **exact finite-source information conservation law**. Randomization can lower either one-shot deterministic marking entropy at finite `Q`, but it cannot lower the sum of the two complementary zero-error information duties.

For the uniform prime cutoff law `P=P_Q`, so `H(P_Q)=\log\pi(Q)`, suppose

\[
\beta_Q:=\frac{\log^+(1/r_Q)}{\log Q}\longrightarrow\beta\in[0,\infty].
\tag{10}
\]

Then the deterministic phase laws of AF-227 and AF-228 squeeze the stochastic quantities to the same first-order rates:

\[
\boxed{
\frac{\mathsf S_{Q,P_Q}(r_Q)}{\log\pi(Q)}
\longrightarrow
(1-\beta)_+,
}
\tag{11}
\]

and

\[
\boxed{
\frac{\mathsf L_{Q,P_Q}(r_Q/2)}{\log\pi(Q)}
\longrightarrow
\min\{\beta,1\}.
}
\tag{12}
\]

Consequently, **stochastic marking does not beat the prime-tail first-order information phase law**. On a polynomial source resolution `r_Q=Q^{-\beta+o(1)}` with `0<\beta<1`, the total prime-source identity entropy splits exactly at finite `Q` in the stochastic graph-entropy model and asymptotically into fractions `1-\beta` for proximity separation and `\beta` for localization.

## Derivation

### 1. Stochastic separation information is Körner graph entropy

One standard operational definition of graph entropy is

\[
H(G,P)
=
\inf I(X;Y),
\tag{13}
\]

where `X\sim P`, `Y` ranges over random independent sets of `G`, and

\[
X\in Y
\qquad\text{almost surely.}
\tag{14}
\]

Take any stochastic separation mark `M` admissible in `(4)`. The posterior support `A_M` is an independent set and contains the realized `X` almost surely. Since `A_M` is a deterministic function of `M`, data processing gives

\[
I(X;A_M)\le I(X;M).
\tag{15}
\]

Therefore

\[
H(G_{Q,r},P)\le \mathsf S_{Q,P}(r).
\tag{16}
\]

Conversely, given any admissible random independent set `Y` in `(13)`, use `M=Y`. Its posterior support is contained in the realized independent set and hence is independent, so it is admissible in `(4)` and has the same mutual information. Thus

\[
\mathsf S_{Q,P}(r)\le H(G_{Q,r},P),
\tag{17}
\]

which proves the first identity in `(8)`.

This is the stochastic counterpart of AF-227's minimum-entropy proper coloring. A deterministic proper coloring is only one special admissible channel and has `I(X;M)=H(M)`.

### 2. Zero-error localization is complement graph entropy

Fix an admissible localization mark and decoder in `(6)`--`(7)`. For every realized `m`, all source points in `A_m` lie in

\[
[d(m)-r/2,d(m)+r/2].
\tag{18}
\]

Hence every pair in `A_m` has distance at most `r`; `A_m` is a clique of `G_{Q,r}`, equivalently an independent set of `\overline{G_{Q,r}}`.

Applying the same posterior-support reduction as above gives

\[
H(\overline{G_{Q,r}},P)
\le
\mathsf L_{Q,P}(r/2).
\tag{19}
\]

For the reverse inequality, let `Y` be any random independent set of `\overline{G_{Q,r}}` containing `X`. Then `Y` is a clique of `G_{Q,r}`. Because `S_Q\subset\mathbb R`, pairwise distance at most `r` is equivalent to

\[
\max Y-\min Y\le r.
\tag{20}
\]

Decoding `Y` to the midpoint of its extreme points reconstructs every member of `Y` within `r/2`. Thus `M=Y` is an admissible localization channel and

\[
\mathsf L_{Q,P}(r/2)
\le
H(\overline{G_{Q,r}},P).
\tag{21}
\]

This proves the second identity in `(8)`.

The one-dimensional source geometry is important here: a clique has diameter at most `r`, and one midpoint simultaneously localizes all its vertices within `r/2`.

### 3. Perfectness gives exact information splitting

The intervals

\[
I_x=[x-r/2,x+r/2],
\qquad x\in S_Q,
\tag{22}
\]

all have the same length, and

\[
I_x\cap I_y\ne\varnothing
\iff
|x-y|\le r.
\tag{23}
\]

Therefore `G_{Q,r}` is a unit interval graph. AF-225 already uses this structure to identify its chromatic number with its maximum local occupancy. Classically, interval graphs are chordal and hence perfect.

The 1990 theorem of Csiszár, Körner, Lovász, Marton, and Simonyi characterizes perfect graphs information-theoretically: for a perfect graph `G` and every probability distribution `P` on its vertices,

\[
H(G,P)+H(\bar G,P)=H(P).
\tag{24}
\]

Applying `(24)` to `G_{Q,r}` and using `(8)` gives `(9)`.

Unlike AF-227 and AF-228's explicit prime-tail phase laws, `(9)` does **not** require the uniform cutoff law, the prime number theorem, a short-interval estimate, or any asymptotic limit. It is an exact finite statement for every source distribution. The arithmetic source enters only through the chosen vertex set; the exact conservation itself is forced by the perfect-graph structure of one-dimensional proximity.

### 4. Deterministic phase laws squeeze the stochastic relaxation

Let `E_Q(r)` be AF-227's minimum entropy of a deterministic `r`-proper coloring under the uniform cutoff law, and let `R_Q(r/2,0)` be AF-228's minimum entropy of a deterministic zero-error radius-`r/2` localization mark.

Every deterministic admissible mark is an admissible stochastic channel and satisfies `I(X;M)=H(M)`. Hence

\[
\mathsf S_{Q,P_Q}(r)\le E_Q(r),
\qquad
\mathsf L_{Q,P_Q}(r/2)\le R_Q(r/2,0).
\tag{25}
\]

Equation `(9)` gives the reverse cross-bounds

\[
\mathsf S_{Q,P_Q}(r)
=
\log\pi(Q)-\mathsf L_{Q,P_Q}(r/2)
\ge
\log\pi(Q)-R_Q(r/2,0),
\tag{26}
\]

and

\[
\mathsf L_{Q,P_Q}(r/2)
\ge
\log\pi(Q)-E_Q(r).
\tag{27}
\]

AF-227 proves

\[
\frac{E_Q(r_Q)}{\log\pi(Q)}
\longrightarrow
(1-\beta)_+,
\tag{28}
\]

while AF-228, with the harmless constant factor `1/2` in the radius, proves

\[
\frac{R_Q(r_Q/2,0)}{\log\pi(Q)}
\longrightarrow
\min\{\beta,1\}.
\tag{29}
\]

The upper and lower bounds `(25)`--`(29)` have matching limits because

\[
(1-\beta)_+ + \min\{\beta,1\}=1.
\tag{30}
\]

This proves `(11)` and `(12)`.

The squeeze is useful conceptually: stochastic graph coding may improve finite additive terms relative to minimum chromatic entropy, but it cannot change the first-order prime-tail information-rate exponent already found by the deterministic analysis.

## Exact controls and boundaries

### The exact split is classical perfect-graph entropy mathematics

No novelty is claimed for graph entropy, entropy splitting, perfect graphs, or the identity `(24)`. Körner introduced graph entropy in the 1970s. Körner and Marton explicitly studied when graph and complement entropies split the source entropy, and Csiszár--Körner--Lovász--Marton--Simonyi gave the perfect-graph characterization.

The Arithmetic Fidelity contribution here is the specialization and interpretation: AF-225's prime-tail proximity graph happens to lie in a class where the stochastic relaxation of AF-227/AF-228 has an exact conservation law, and the previous deterministic phase estimates then prove that randomization does not alter the first-order prime-tail information budget.

### Zero error is load bearing for the complement identification

Equation `(9)` concerns exact posterior-support separation and exact radius-`r/2` localization. If a positive failure probability or average distortion is allowed, posterior supports may contain forbidden pairs and the problem becomes a rate-distortion/graph-coding problem without this direct complement identity. AF-228's nonzero-error localization phase is not replaced by `(9)`.

### One-dimensional proximity is load bearing for exact localization duality

The separation side `(8)` is graph-theoretic for any confusability graph. The localization side uses the fact that every clique in this one-dimensional threshold graph fits inside a single interval of diameter `r` and therefore has a common radius-`r/2` decoder. A general geometric proximity graph, especially in higher dimension, need not have this exact clique-to-one-center equivalence at the same radius.

### Perfectness is load bearing for exact conservation

For a nonperfect confusability graph, graph entropy and complement graph entropy need not sum to source entropy for every distribution. Therefore stochasticization does not generically create an exact conservation law; it does so here because the retained one-dimensional proximity structure is perfect.

### Exact conservation is not arithmetic discrimination

Equation `(9)` holds for any finite set of points on the real line with the same proximity construction. It does not distinguish rational primes from matched non-prime controls and has no RH consequence by itself. Its role is a no-escape theorem for a **generic repair mechanism**: replacing deterministic prime-tail marks by arbitrary stochastic marks cannot evade the combined zero-error separation/localization information budget while staying in this proximity model.

### Uniformity is needed only for the explicit phase law

The exact finite identity `(9)` holds for every source law `P`. Uniformity of the prime cutoff law is load bearing only for the explicit normalized phase `(11)`--`(12)`, where AF-227 and AF-228 use prime-tail occupancy and covering estimates together with `\log\pi(Q)\sim\log Q`.

## Prior art and novelty assessment

János Körner, **“Coding of an information source having ambiguous alphabet and the entropy of graphs,”** *Transactions of the Sixth Prague Conference on Information Theory, Statistical Decision Functions and Random Processes*, 411--425 (1973), introduced the information-theoretic graph entropy used in `(13)`.

János Körner and Katalin Marton, **“Graphs that Split Entropies,”** *SIAM Journal on Discrete Mathematics* **1**(1), 71--79 (1988), DOI `10.1137/0401008`, directly studies when the entropy of a graph and its complement add to the entropy of the underlying source distribution.

Imre Csiszár, János Körner, László Lovász, Katalin Marton, and Gábor Simonyi, **“Entropy splitting for antiblocking corners and perfect graphs,”** *Combinatorica* **10**(1), 27--40 (1990), DOI `10.1007/BF02122693`, gives the decisive classical perfect-graph characterization used in `(24)`.

The unit-interval/perfect-graph fact is standard interval-graph theory. AF-225 already establishes the exact unit-interval structure of the prime-tail proximity graph, so no new graph-class claim is made here.

A targeted literature check found the classical ingredients above and therefore rules out treating the entropy-splitting mechanism itself as new. The line-specific result is the derived bridge from those ingredients to AF-227/AF-228: arbitrary stochastic zero-error separation and localization on the prime-tail source obey exact finite information conservation, and the deterministic prime-tail phase laws force the stochastic optimum to have the same first-order exponents.

## Consequence for the research line

AF-228 left open whether its deterministic entropy accounting was an artifact of using colorings and deterministic quantizers rather than general randomized descriptions. AF-229 closes that escape in the strongest zero-error form available inside the same one-dimensional proximity model.

The obstruction is now more structural: if a marked translation repair needs both (i) enough information to rule out nearby conflicting prime-tail sources and (ii) enough information to localize the surviving source within the complementary radius, then **the two stochastic duties together cost exactly the entire source entropy**, not merely asymptotically and not merely for uniform primes. Under the uniform cutoff law, randomization can redistribute this cost but cannot improve the polynomial-resolution phase curve.

A genuinely cheaper arithmetic repair must therefore break at least one premise of this generic model: it must exploit arithmetic structure so that exact source localization is unnecessary, replace one-dimensional proximity by a different task geometry, tolerate controlled error/distortion with a quantitatively favorable consequence, or use a downstream invariant whose required discriminator is strictly smaller than full prime-source identity.