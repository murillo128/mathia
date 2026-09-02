# AF-070 — Compact-target cone consequence is zero normalized-excess closure

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a finite-dimensional real normed space. Let `\mathcal K` be a nonempty family of cones in `V`, each containing `0`, and let `L\subseteq V` be a closed cone containing `0`. For a cone `K`, define its **directed normalized excess toward `L`** by

\[
\varepsilon(K\mid L)
=
\sup_{x\in K\setminus\{0\}}
\frac{d(x,L)}{\|x\|},
\tag{1}
\]

with `\varepsilon(\{0\}\mid L)=0`. Because `L` is a cone,

\[
d(tx,L)=t\,d(x,L)
\qquad(t\ge0),
\tag{2}
\]

so whenever `K\ne\{0\}`,

\[
\varepsilon(K\mid L)
=
\sup_{\substack{x\in K\\ \|x\|=1}} d(x,L).
\tag{3}
\]

Write

\[
\delta_{\mathcal K}(L)
=
\inf_{K\in\mathcal K}\varepsilon(K\mid L).
\tag{4}
\]

Let `\mathscr K_c` denote the class of nonempty compact targets and let `\operatorname{Imp}_{\mathscr K_c}(\mathcal K)` be AF-069's compact-target consequence class:

\[
L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
\iff
H_{\mathcal K}(S)\subseteq S-L
\quad\text{for every nonempty compact }S\subset V.
\tag{5}
\]

Then:

1. **Normalized excess gives the complete compact-target consequence criterion.** One has
   \[
   \boxed{
   L\in\operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \iff
   \delta_{\mathcal K}(L)=0.
   }
   \tag{6}
   \]
   Thus the unresolved compact consequence class left open in AF-069 is exactly the zero one-sided excess closure of the declared cone family. Literal containment is no longer necessary: it is enough that declared cones approach `L` arbitrarily closely after radial normalization.

2. **Positive excess margin gives an explicit compact falsifier.** If
   \[
   \delta_{\mathcal K}(L)=c>0,
   \tag{7}
   \]
   then for every `0<\eta<c` the set
   \[
   S_\eta
   =
   \{u\in V:\|u\|=1,\ d(u,L)\ge\eta\}
   \tag{8}
   \]
   is compact, disjoint from `L`, and meets every `K\in\mathcal K`. Consequently
   \[
   0\in H_{\mathcal K}(S_\eta)
   \qquad\text{but}\qquad
   0\notin S_\eta-L.
   \tag{9}
   \]
   The number `\delta_{\mathcal K}(L)` is therefore a sharp zero-versus-positive robustness margin for compact consequence: any positive margin can be converted directly into a compact matched-control witness.

3. **Zero excess forces every compact moving-witness family to hit the limit cone.** Suppose `\delta_{\mathcal K}(L)=0` and let `S` be nonempty compact with
   \[
   0\in H_{\mathcal K}(S),
   \tag{10}
   \]
   so `S\cap K\ne\varnothing` for every `K\in\mathcal K`. Then necessarily
   \[
   \boxed{S\cap L\ne\varnothing.}
   \tag{11}
   \]
   More generally, after translating by any `m`, every compact target that supplies witnesses for all translated `m+K` must supply a witness in `m+L`.

4. **Compact-target comparison of arbitrary cone presentations is exact one-sided excess cofinality.** If `\mathcal L` is any family of closed cones containing `0`, then
   \[
   \boxed{
   H_{\mathcal K}(S)\subseteq H_{\mathcal L}(S)
   \quad\forall S\in\mathscr K_c
   \iff
   \forall L\in\mathcal L:\
   \inf_{K\in\mathcal K}\varepsilon(K\mid L)=0.
   }
   \tag{12}
   \]
   Hence two closed-cone presentations induce the same hull operator on every compact target exactly when they are mutually cofinal at zero directed normalized excess.

5. **Finite presentations collapse back to AF-068's literal containment order.** If `\mathcal K` is finite, then because `L` is closed,
   \[
   \varepsilon(K\mid L)=0
   \iff
   K\subseteq L.
   \tag{13}
   \]
   Therefore
   \[
   \delta_{\mathcal K}(L)=0
   \iff
   \exists K\in\mathcal K\text{ with }K\subseteq L.
   \tag{14}
   \]
   On finite presentations compact targets add no new cone consequences beyond AF-068. The enlargement discovered in AF-069 is intrinsically an **infinite-presentation limit phenomenon**.

6. **Filtered intersections are sufficient but not complete: non-directed angular approximation already forces consequence.** In Euclidean `\mathbb R^2`, let
   \[
   L=\mathbb R_{\ge0}(1,0),
   \qquad
   K_n=\mathbb R_{\ge0}(\cos\theta_n,\sin\theta_n),
   \qquad
   \theta_n=1/n.
   \tag{15}
   \]
   Distinct rays are inclusion-incomparable, so `(K_n)` is not downward directed and no `K_n` is contained in `L`. Nevertheless
   \[
   \varepsilon(K_n\mid L)=\sin(1/n)\longrightarrow0,
   \tag{16}
   \]
   and therefore
   \[
   \boxed{L\in\operatorname{Imp}_{\mathscr K_c}(\{K_n:n\ge1\}).}
   \tag{17}
   \]
   This lies strictly beyond AF-069's filtered-meet theorem: compact-target consequence can arise from metric/set-convergence of incomparable constraints, not only from a nested or directed refinement whose literal intersection is retained.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{arbitrary targets remember literal cone containment;}\\
\text{compact targets remember the zero normalized-excess closure of the cone family;}\\
\text{finite presentations identify the two, while infinite presentations can separate them.}
\end{array}
}
\tag{18}
\]

This gives a precise category-indexed completion of AF-068--AF-069. Compactness does not make arbitrary witness branches coherent, but it does prevent a family of witnesses from staying uniformly separated from a cone that the declared tests approach with vanishing normalized excess.

## Derivation

### Homogeneous excess is the right cone-scale quantity

Because `L` is a cone, for every `t>0`,

\[
\begin{aligned}
d(tx,L)
&=\inf_{y\in L}\|tx-y\|\\
&=t\inf_{z\in L}\|x-z\|\\
&=t\,d(x,L),
\end{aligned}
\tag{19}
\]

where the second line uses `y=tz` and conicity of `L`. Thus the ratio in (1) is invariant under positive radial rescaling. It measures only the directional discrepancy between the two cone constraints, not an arbitrary choice of witness magnitude.

Since `0\in L`,

\[
0\le d(x,L)\le\|x\|,
\]

so

\[
0\le\varepsilon(K\mid L)\le1.
\tag{20}
\]

This bounded normalization is essential for the compact-sphere argument below.

### Positive margin produces a compact counterexample

Assume `c=\delta_{\mathcal K}(L)>0` and choose `0<\eta<c`. For every `K\in\mathcal K`,

\[
\varepsilon(K\mid L)\ge c>\eta.
\tag{21}
\]

Hence, by the definition of supremum, there exists some unit vector `u_K\in K` satisfying

\[
d(u_K,L)>\eta.
\tag{22}
\]

The set `S_\eta` in (8) is a closed subset of the unit sphere. Finite dimensionality makes that sphere compact, so `S_\eta` is compact. Equation (22) shows that

\[
S_\eta\cap K\ne\varnothing
\qquad\forall K\in\mathcal K,
\tag{23}
\]

and therefore `0\in H_{\mathcal K}(S_\eta)`.

But every point of `S_\eta` has strictly positive distance from `L`, so

\[
S_\eta\cap L=\varnothing.
\tag{24}
\]

Since `0\in S_\eta-L` would mean `s=l` for some `s\in S_\eta` and `l\in L`, equation (24) implies `0\notin S_\eta-L`. Thus `L` is not a compact-target consequence. This proves the `\Rightarrow` direction of (6) by contraposition and also proves item 2.

### Zero margin forces a compact target to meet the consequence cone

Assume now

\[
\delta_{\mathcal K}(L)=0.
\tag{25}
\]

Let `S` be nonempty compact and suppose `S\cap K\ne\varnothing` for every `K\in\mathcal K`. If, contrary to (11),

\[
S\cap L=\varnothing,
\tag{26}
\]

then `0\notin S` because `0\in L`. The function

\[
r(s)=\frac{d(s,L)}{\|s\|}
\tag{27}
\]

is therefore continuous and strictly positive on compact `S`. Hence

\[
\eta
:=
\min_{s\in S}r(s)
>0.
\tag{28}
\]

By (25), choose `K\in\mathcal K` with

\[
\varepsilon(K\mid L)<\eta.
\tag{29}
\]

Every nonzero `x\in K` then satisfies

\[
\frac{d(x,L)}{\|x\|}
\le
\varepsilon(K\mid L)
<\eta.
\tag{30}
\]

But every point of `S` satisfies the reverse lower bound `r(s)\ge\eta`. Therefore

\[
S\cap K=\varnothing,
\tag{31}
\]

contradicting the assumption that `S` hits every declared cone. Thus `S\cap L\ne\varnothing`, proving item 3 and the converse implication in (6).

Translation gives the full hull statement. If `m\in H_{\mathcal K}(S)`, put `Q=S-m`. Then `Q` is compact and meets every `K`; equation (11) gives `q\in Q\cap L`, hence `m=s-q\in S-L`.

### Presentation comparison is pointwise consequence comparison

For a family `\mathcal L` of closed cones,

\[
H_{\mathcal K}(S)\subseteq H_{\mathcal L}(S)
\quad\forall S\in\mathscr K_c
\]

holds exactly when

\[
H_{\mathcal K}(S)\subseteq S-L
\quad\forall S\in\mathscr K_c
\]

holds separately for every `L\in\mathcal L`. Applying (6) to each `L` proves (12). Applying the same criterion in both directions gives the equality statement.

For finite `\mathcal K`, the infimum in (4) is a minimum. If `\varepsilon(K\mid L)=0`, then every nonzero `x\in K` has `d(x,L)=0`, and closedness of `L` gives `x\in L`; also `0\in L`, so `K\subseteq L`. The converse is immediate. Equations (13)--(14) follow.

## Exact controls

### Incomparable rays produce a genuine compact-only consequence

For the rays in (15), each nonzero point of `K_n` is a positive multiple of

\[
u_n=(\cos(1/n),\sin(1/n)).
\]

The Euclidean nearest point on the positive `x`-axis is `(\cos(1/n),0)`, so

\[
d(u_n,L)=\sin(1/n),
\tag{32}
\]

which proves (16). No two distinct rays contain one another. Thus neither AF-068's finite containment criterion nor AF-069's downward-directed meet mechanism explains (17); it is exactly the zero-excess criterion.

The category dependence is visible through two matched failures.

A bounded but nonclosed target can hit every ray while missing `L`:

\[
S_{\mathrm{miss}}
=
\{u_n:n\ge1\}.
\tag{33}
\]

Its missing limit is `(1,0)\in L`. Adding that one limit point makes the target compact and forces the consequence.

A closed noncompact target can instead let the witnesses escape:

\[
S_{\mathrm{esc}}
=
\{n u_n:n\ge1\}.
\tag{34}
\]

It intersects every `K_n`, is closed and unbounded, and misses `L`. Since

\[
n u_n=(n\cos(1/n),n\sin(1/n))
\sim(n,1),
\]

its witnesses never acquire a finite limit point on `L`. These controls reproduce AF-069's two compactness failure modes without a nested cone family.

### Positive margin is robust under arbitrary cardinality

The falsifier `S_\eta` in (8) does not select one witness and then take its closure. It is defined intrinsically from the sphere and `L`, and it meets **every** declared cone whenever `\eta<\delta_{\mathcal K}(L)`, regardless of the cardinality of `\mathcal K`. Thus the negative direction of (6) needs no countability, sequence extraction indexed by the cone family, or axiomatically chosen witness set.

### A single cone cannot gain a compact-only consequence

If `\mathcal K=\{K\}`, equation (6) reduces to

\[
L\in\operatorname{Imp}_{\mathscr K_c}(\{K\})
\iff
\varepsilon(K\mid L)=0
\iff
K\subseteq L.
\tag{35}
\]

Compactness does not repair a fixed information loss. The extra consequence arises only because an infinite presentation contains constraints at arbitrarily small normalized excess from the candidate limit constraint.

## Prior art and novelty assessment

The distance/excess and compactness mechanisms are classical.

- Ľubica Holá and Roberto Lucchetti, **“Polishness of Weak Topologies Generated by Gap and Excess Functionals,”** *Journal of Convex Analysis* 3(2) (1996), 283–294. Role: direct established hyperspace language for one-sided **excess functionals**, Hausdorff-type comparisons, and weak topologies generated by gap/excess observables. Equation (1) is a homogeneous cone specialization of this general distance/excess viewpoint, not a new notion of set distance.
- Gerald Beer, **“Mosco convergence and weak topologies for convex sets and functions,”** *Mathematika* 38(1) (1991), 89–104, DOI `10.1112/S0025579300006471`. Role: established use of distance functionals to characterize convergence/topology of convex sets. It supplies the appropriate prior-art boundary for interpreting vanishing distance to a moving family as set-convergence information rather than a new geometric primitive.
- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer Academic Publishers (1993), DOI `10.1007/978-94-015-8149-3`. Role: the broader hit-and-miss, Fell, Wijsman, and hyperspace framework already cited in AF-069.
- Somashekhar Naimpally, **“All hypertopologies are hit-and-miss,”** *Applied General Topology* 3(1) (2002), 45–53, DOI `10.4995/agt.2002.2111`. Role: mature hit-and-miss language for comparing hyperspace topologies, reinforcing that the compact-target witness semantics belong to established hyperspace theory.
- James R. Munkres, ***Topology***, 2nd ed., Prentice Hall (2000), §26. Role: standard compactness principle underlying the fact that a compact target cannot remain a positive normalized distance away from an approximating family without yielding a compact separating witness.

No novelty is claimed for directed Hausdorff/Pompeiu excess, distance-to-set functionals, compactness, hit-and-miss topology, Mosco/Wijsman/Fell-type convergence, or homogeneous cone rescaling. The theorem (6) is an elementary exact specialization to AF-069's cone-hit consequence problem.

The durable Arithmetic Fidelity contribution is narrower and internal to the program: AF-069 proved one sufficient compact completion rule and explicitly left the full compact consequence class open. AF-070 closes that boundary. It identifies exactly what additional information the compact source category retains from an arbitrary cone presentation and gives a constructive compact falsifier whenever the proposed retained constraint remains at positive normalized excess. The resulting criterion is representation-auditable and reduces to AF-068's containment cofinality on finite presentations.

## Boundary conditions and falsification tests

1. **Finite dimensionality is used materially.** The positive-margin falsifier is a closed subset of the unit sphere, which is compact only in finite-dimensional normed spaces. In an infinite-dimensional Banach space, positive normalized excess need not yield a compact target by this construction, so (6) must not be exported without an additional compactness/properness hypothesis.
2. **Closedness of `L` is essential.** It is used both in `\varepsilon(K\mid L)=0\Rightarrow K\subseteq L` and in the positive lower bound (28) for a compact target disjoint from `L`. Replacing `L` by a nonclosed cone changes the natural consequence to its closure at the distance-functional layer.
3. **The criterion is one-sided.** `\varepsilon(K\mid L)` measures whether `K` lies close to `L`; it does not require `L` to lie close to `K`. Symmetrizing it would impose information not required by the consequence relation.
4. **Radial normalization is structural, not cosmetic.** Unnormalized Hausdorff distance between unbounded cones is usually infinite or scale-dependent. Equation (1) removes magnitude exactly because the cone-hit constraint is homogeneous.
5. **Zero excess is a consequence criterion, not a provenance reconstruction theorem.** It proves that some compact target witness survives in `L`; it does not identify which upstream witness produced it, provide a canonical selector, or recover labels/phase/sign beyond the declared cone relation.
6. **No arithmetic specificity follows.** The theorem is abstract compression mathematics. A prime/RH application must still identify a concrete destination category, prove that its retained constraints instantiate this cone-hit model, and compare rational-prime data with matched non-prime controls at that same layer.
7. **AF-069's filtered-meet result remains useful.** Directed intersections provide an order-theoretic sufficient certificate for zero excess in many closed-cone families. AF-070 says that such certificates are not complete: metric approach in normalized direction space is the exact compact-target criterion even when no directed refinement is present.

The next natural frontier is no longer the full compact consequence class itself. It is to determine which non-conic compression families admit an analogous **category-indexed zero-excess completion theorem**, and which destination geometries require stronger retained data than distance/excess because labels, coupling, orientation, or other provenance remain invisible to the underlying hyperspace topology.