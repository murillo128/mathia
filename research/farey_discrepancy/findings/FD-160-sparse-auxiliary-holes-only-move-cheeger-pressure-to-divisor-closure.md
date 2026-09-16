# FD-160 — Sparse auxiliary holes only move Cheeger pressure to the divisor closure

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / arbitrary sparse auxiliary support / hole-flux and divisor-closure law
- **Depends on:** FD-157, FD-158, FD-159

## Claim

FD-159 leaves one explicit architecture escape: a deliberately sparse auxiliary core family need not be divisor-downward, so missing lower cores can act as extra incoming parents for the occupied packet. That escape is real at the level of the original sparse cut, but it is not free.

There are two exact statements.

First, for an arbitrary sparse core family, every additional incoming channel is charged by a **hole-core inflow** term. Retain the squarefree vertex set, uniform law, directed divisibility relation, edge probability measure, anchored Cheeger constant, parent distortion, and optional child distortion of FD-157--FD-159:

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
D_{S,T}:=\{n\in V_T:(n,P_S)=1\},
\qquad
R_{S,T}:=V_T\setminus D_{S,T},
\tag{1}
\]

\[
h_{S,T}
:=
\inf_{\varnothing\ne A\subseteq R_{S,T}}
\frac{\eta_T(\partial A)}{\nu_T(A)},
\qquad
P_{S,T}
:=
\max_{d\in D_{S,T}}
\frac{\eta_T^-(d)}{\nu_T(d)}.
\tag{2}
\]

Let `S` be a nonempty finite prime set, let `p_*:=min S`, and let `C` now be an **arbitrary** finite nonempty subset of `D_(S,T)` satisfying only the activity condition

\[
cp_*\le T
\qquad(c\in C).
\tag{3}
\]

Use the FD-159 fibers and packet

\[
F_{S,T}(c)
:=
\{q:q\mid P_S,\ q>1,\ qc\le T\},
\qquad
f_{S,T}(c):=|F_{S,T}(c)|,
\tag{4}
\]

\[
B_{S\mid C}(T)
:=
\{qc:c\in C,\ q\in F_{S,T}(c)\},
\qquad
M_{S,C}(T):=\sum_{c\in C}f_{S,T}(c).
\tag{5}
\]

Define the divisor closure and its holes by

\[
\downarrow C
:=
\{d\in D_{S,T}: d\mid c\text{ for some }c\in C\},
\qquad
H(C):=(\downarrow C)\setminus C.
\tag{6}
\]

For any squarefree vertex put

\[
\kappa_S(n):=\frac{n}{\gcd(n,P_S)}.
\tag{7}
\]

The hole-core incoming edges are

\[
E_{\rm hole}^{\rm in}(S,C,T)
:=
\{(d,m)\in E_T^*:d\notin B_{S\mid C}(T),\ m\in B_{S\mid C}(T),\ \kappa_S(d)\in H(C)\},
\tag{8}
\]

with coefficient-scale mass

\[
J_{S,C,T}
:=|V_T|\,\eta_T(E_{\rm hole}^{\rm in}(S,C,T)).
\tag{9}
\]

Retain the outgoing leakage

\[
E_{\rm out}(S,C,T)
:=
\{(n,m)\in E_T^*:n\in B_{S\mid C}(T),\ m\notin B_{S\mid C}(T)\},
\tag{10}
\]

\[
L_{S,C,T}
:=|V_T|\,\eta_T(E_{\rm out}(S,C,T)).
\tag{11}
\]

Then every arbitrary sparse family satisfies

\[
\boxed{
P_{S,T}|C|+J_{S,C,T}+L_{S,C,T}
\ge
h_{S,T}M_{S,C}(T).
}
\tag{12}
\]

Equivalently, with `bar f=M/|C|`,

\[
\boxed{
P_{S,T}
+
\frac{J_{S,C,T}+L_{S,C,T}}{|C|}
\ge
h_{S,T}\bar f_{S,C}(T).
}
\tag{13}
\]

Thus the heuristic resource balance proposed at the end of FD-159 is exact: **parent budget + hole inflow + outer leakage dominates occupied primary-fiber mass**.

Second, and more importantly, holes cannot be a terminal resource under the same global anchored-expansion hypothesis. Filling them into the test cut makes their incoming flux internal without reducing the primary depth of any core. For `1<=r<=|S|` define the deep part of any sparse family by

\[
C_{\ge r}
:=
\{c\in C:r_T(c)\ge r\},
\tag{14}
\]

where `r_T` is the FD-159 available-primary-depth function,

\[
r_T(c)
:=
\max\left\{
0\le j\le |S|:
 c\prod_{i=1}^{j}p_i\le T
\right\},
\tag{15}
\]

for `p_1<...<p_|S|` the primes of `S`. If `C_(>=r)` is nonempty, set

\[
D_r(C):=\downarrow C_{\ge r}.
\tag{16}
\]

Then `D_r(C)` is an active divisor down-set and every one of its cores still has primary depth at least `r`. Therefore FD-159 applies and gives

\[
\boxed{
P_{S,T}
+
\frac{L_{S,D_r(C),T}}{|D_r(C)|}
\ge
h_{S,T}(2^r-1).
}
\tag{17}
\]

No hole term occurs in (17): the holes have become part of the cut. In particular, a sparse proposal cannot use missing lower cores to neutralize a growing primary depth. It can only move the required boundary farther out in the divisor poset.

If child distortion is bounded,

\[
\eta_T^+(m)\le K_{S,T}\nu_T(m)
\qquad(m\in R_{S,T}),
\tag{18}
\]

then the distinct outgoing recipients of the closed packet satisfy

\[
\boxed{
|C_{\rm out}(S,D_r(C),T)|
\ge
\frac{|D_r(C)|\bigl(h_{S,T}(2^r-1)-P_{S,T}\bigr)_+}
{K_{S,T}}.
}
\tag{19}
\]

Since `C_(>=r) subset D_r(C)`, also

\[
\boxed{
|C_{\rm out}(S,D_r(C),T)|
\ge
\frac{|C_{\ge r}|\bigl(h_{S,T}(2^r-1)-P_{S,T}\bigr)_+}
{K_{S,T}}.
}
\tag{20}
\]

Hence non-downward sparsity does not weaken the exponential prime-depth pressure. Under fixed positive expansion and bounded endpoint distortion, every population of depth-`r` sparse cores forces exponentially many outer recipients per such core after divisor closure.

## 1. Every incoming sparse-packet parent is either an occupied core or a hole-core parent

Take an incoming boundary edge

\[
(d,m)\in E_T^*,
\qquad
d\notin B_{S\mid C}(T),
\qquad
m\in B_{S\mid C}(T).
\tag{21}
\]

Write

\[
m=qc,
\qquad
c\in C,
\qquad
q\mid P_S,
\qquad
q>1.
\tag{22}
\]

Since `d|m` and all vertices are squarefree, `d` has a unique decomposition

\[
d=q'c',
\qquad
q'\mid q,
\qquad
c'\mid c,
\tag{23}
\]

where `q'=gcd(d,P_S)` and `c'=kappa_S(d)`.

Suppose first that `c' in C`. If `q'>1`, then `d=q'c'<=m<=T`, so `q' in F_(S,T)(c')` and hence `d in B_(S|C)(T)`, contradicting (21). Therefore `q'=1`, and

\[
\boxed{d=c'\in C.}
\tag{24}
\]

If instead `c' notin C`, equation (23) and `c'|c` imply

\[
\boxed{c'=\kappa_S(d)\in H(C).}
\tag{25}
\]

There is no third case. Thus the entire incoming boundary decomposes into edges from the `|C|` occupied S-free cores themselves and edges whose parent has a missing lower core.

The first class has total mass at most

\[
\sum_{c\in C}\eta_T^-(c)
\le
\frac{|C|P_{S,T}}{|V_T|}.
\tag{26}
\]

The second class is exactly `J_(S,C,T)/|V_T|` by (8)-(9).

Together with the outgoing class (10), this gives the exact boundary decomposition

\[
\eta_T(\partial B_{S\mid C}(T))
\le
\frac{|C|P_{S,T}+J_{S,C,T}+L_{S,C,T}}{|V_T|}.
\tag{27}
\]

The packet has uniform mass `M_(S,C)(T)/|V_T|`, so Cheeger pressure gives the reverse lower bound

\[
\eta_T(\partial B_{S\mid C}(T))
\ge
\frac{h_{S,T}M_{S,C}(T)}{|V_T|}.
\tag{28}
\]

Combining (27)-(28) proves (12)-(13).

Notice what is and is not quantified. The current FD-157 framework controls outgoing marginal load only on anchor vertices through `P_(S,T)`. A nonanchor hole parent can in principle carry large outgoing mass, so **hole cardinality alone cannot replace `J`** without an additional nonanchor-parent distortion hypothesis. Classical shadow-size estimates therefore do not by themselves prove (12) with a cardinality penalty. The correct quantity at this level is actual weighted hole inflow.

## 2. Divisor closure absorbs the hole inflow without losing depth

The previous law still seems to leave `J` as a possible escape resource. Global Cheeger expansion supplies a stronger test.

Fix `r` and suppose `C_(>=r)` is nonempty. If

\[
d\in D_r(C),
\tag{29}
\]

then by definition `d|c` for some `c in C_(>=r)`. Hence

\[
c\prod_{i=1}^{r}p_i\le T.
\tag{30}
\]

Since `d<=c`,

\[
d\prod_{i=1}^{r}p_i\le T,
\tag{31}
\]

so

\[
\boxed{r_T(d)\ge r.}
\tag{32}
\]

Every divisor of an active core is active, so `D_r(C)` satisfies all hypotheses of FD-159. Its primary fiber obeys

\[
f_{S,T}(d)\ge2^r-1
\qquad(d\in D_r(C)),
\tag{33}
\]

because every nonempty subset of the first `r` primary primes fits. Therefore

\[
\bar f_{S,D_r(C)}(T)\ge2^r-1.
\tag{34}
\]

Apply FD-159 equation (11) to this down-set. Equation (34) gives (17) immediately.

Conceptually, this is the missing step in the sparse-support analysis. An edge entering the original packet from a hole-core parent was counted by `J`. Once the whole divisor closure is placed inside the test packet, that edge is internal and cannot pay Cheeger pressure. Positive expansion must then be supplied by the bounded anchor parents of the closed packet or by genuinely **outer** core leakage. Closing the holes therefore moves the bill; it does not erase it.

The argument needs no estimate for the cardinality of the shadow `D_r(C)`. Exact closure is enough. If the closure is large, that only increases the absolute amount of boundary mass and, under bounded child distortion, the number of required recipients.

## 3. One deep sparse core already reproduces the exponential prime-face law

The threshold form has a useful pointwise corollary. Take a single active core `c` and its principal divisor ideal

\[
D(c):=\{d:d\mid c\}.
\tag{35}
\]

Because `c` is squarefree,

\[
|D(c)|=2^{\omega(c)}.
\tag{36}
\]

Every `d|c` satisfies `r_T(d)>=r_T(c)`, so (17) with `r=r_T(c)` gives

\[
\boxed{
P_{S,T}
+
\frac{L_{S,D(c),T}}{2^{\omega(c)}}
\ge
h_{S,T}\bigl(2^{r_T(c)}-1\bigr).
}
\tag{37}
\]

If the whole primary face fits above `c`,

\[
cP_S\le T,
\tag{38}
\]

then every divisor `d|c` also supports every nonempty `S`-state, so the fiber size is exactly `2^|S|-1` throughout the principal ideal. Thus

\[
\boxed{
P_{S,T}
+
\frac{L_{S,D(c),T}}{2^{\omega(c)}}
\ge
h_{S,T}(2^{|S|}-1).
}
\tag{39}
\]

Under (18), the recipient count becomes

\[
\boxed{
|C_{\rm out}(S,D(c),T)|
\ge
\frac{2^{\omega(c)}\bigl(h_{S,T}(2^{|S|}-1)-P_{S,T}\bigr)_+}
{K_{S,T}}.
}
\tag{40}
\]

So even an **isolated single auxiliary core** with holes under every proper divisor cannot hide a full-depth primary Boolean face. The appropriate cut simply fills its principal divisor ideal and recovers the same exponential `S`-coordinate pressure, multiplied rather than diluted by the size of the auxiliary divisor shadow.

This is stronger than a statement that many occupied cores must collectively be downward-closed. No density of the sparse support is needed: one deep core is already enough to trigger the divisor-cone obstruction.

## 4. Bounded resources force genuinely terminal migrating support

Equations (17) and (37) identify what remains after the hole escape is removed. Suppose a family is required to have, on every relevant closed packet, a normalized outer leakage bound

\[
\frac{L_{S,D,T}}{|D|}\le\Lambda_{S,T}.
\tag{41}
\]

Then (37) implies for every represented core

\[
2^{r_T(c)}-1
\le
\frac{P_{S,T}+\Lambda_{S,T}}{h_{S,T}}.
\tag{42}
\]

Hence

\[
\boxed{
r_T(c)
\le
\log_2\!\left(
1+\frac{P_{S,T}+\Lambda_{S,T}}{h_{S,T}}
\right).
}
\tag{43}
\]

Under fixed positive expansion and bounded normalized parent/leakage resources, **every usable auxiliary core has bounded primary depth**. If the right side is at most an integer `R<|S|`, the definition of `r_T` yields

\[
c\prod_{i=1}^{R+1}p_i>T,
\qquad
\boxed{
c>\frac{T}{\prod_{i=1}^{R+1}p_i}.}
\tag{44}
\]

For the first-`s`-prime faces used in FD-155, any fixed `R` gives a fixed multiplicative terminal layer. Thus the surviving bounded-distortion architecture is no longer merely "sparse support with holes". It must **migrate toward the truncation ceiling strongly enough that only O(1) primary coordinates fit above each active core**, or else pay growing outer-core flux/recipient proliferation.

This does not yet forbid such terminal migration. It identifies it as the genuine remaining geometric escape.

## 5. Stress test: the smallest non-downward hole becomes internal after closure

Take

\[
S=\{2,3\},
\qquad T=30,
\qquad C=\{5\}.
\tag{45}
\]

The sparse packet is

\[
B_{S\mid C}(30)=\{10,15,30\}.
\tag{46}
\]

Its divisor closure and hole set are

\[
\downarrow C=\{1,5\},
\qquad H(C)=\{1\}.
\tag{47}
\]

The edge `(2,10)`, if present, is a genuine incoming boundary edge for the sparse packet. Its `S`-free core is `1`, so it is counted by `J_(S,C,30)` rather than by the anchor budget of the occupied core `5`. The same is true for `(3,15)` and `(6,30)`.

Now close the hole. The packet over `D={1,5}` is

\[
B_{S\mid D}(30)
=\{2,3,6,10,15,30\}.
\tag{48}
\]

All three former hole-inflow edges are internal. Both cores have full primary fiber size `3`, so FD-159/FD-160 gives

\[
\boxed{
P_{S,30}+\frac12L_{S,D,30}\ge3h_{S,30}.
}
\tag{49}
\]

This example shows exactly why counting holes in the original support is the wrong terminal invariant. A hole can create an incoming channel for one cut, but global expansion permits the cut to absorb that hole. The unresolved cost then reappears at the boundary of the lower closure.

## 6. Prior-art, representation audit, and remaining scope

Classical Kruskal--Katona theory and its modern extensions study the minimum **cardinality** of lower shadows of set families in the Boolean lattice. For example, Boris Bukh's multidimensional Kruskal--Katona theorem (SIAM Journal on Discrete Mathematics 26 (2012), 548--554, DOI `10.1137/100808630`) and the later extremal-family work of Oriol Serra and Lluís Vena (arXiv `2304.05145`) remain natural neighboring language for sparse supports and shadows. A targeted search also checked generic weighted/directed Cheeger literature.

None of that machinery is load-bearing here. The new statements use the exact squarefree divisor closure, the monotonicity `r_T(d)>=r_T(c)` under divisibility, and the already-internal anchored Cheeger framework. In particular, (17) does not minimize a shadow and does not require a compression theorem; it deliberately keeps the **entire** lower closure so that all hole inflow becomes internal. No matching published statement was located for the weighted hole-flux identity (12) or the divisor-closure pressure law (17) in this Möbius prime-face setting. Broad novelty is not claimed for lower shadows, principal ideals, or Cheeger cuts. No new external theorem is used, so `SOURCES.md` requires no additional anchor.

The representation audit is favorable but narrow. The comparator is exactly the same positive directed divisibility architecture and uniform squarefree vertex law as FD-157--FD-159; no arithmetic source information is inserted when the closure is taken. The cut may include vertices that a proposed sparse gadget hoped not to use, but that is legitimate precisely because `h_(S,T)` is a global infimum over **all** nonempty subsets of the nonanchor region. If those filled vertices were genuinely isolated, the claimed positive Cheeger constant would already fail.

Several escapes remain and should not be collapsed into this theorem. The architecture may let `h_(S,T)` decay, allow `P_(S,T)` or `K_(S,T)` to grow, tolerate large normalized outer leakage, move every relevant core into the terminal regime where `r_T=O(1)`, change the anchor geometry, or exploit a Farey-native source identity outside this positive-edge Cheeger model. Recipient cardinality still does not equal independent Möbius information. The result is therefore a **closure obstruction to sparse holes**, not an information lower bound and not a Farey/RH estimate.

The next pressure point is now more specific than the one stated in FD-159: quantify or obstruct **terminal migrating support with bounded primary depth**, rather than arbitrary non-downward sparsity. Any further cut argument must distinguish genuine scale migration from merely moving the same boundary charge through another finite layer.

### Retrieval notes

- Internal inputs: FD-157, FD-158, FD-159, the current `farey_discrepancy` line synthesis, and the current local clue dispositions.
- Unresolved adversarial-review sidecars were checked before starting new research; none had precedence in this pass.
- The candidate was derived before the external shadow/Cheeger search. The external literature is contextual only and no source was imported into the proof.
- `SOURCES.md`, clues, and `mind/**` are unchanged because there is no new load-bearing external dependency and no clue-state transition.
- Formalization handoff is not opened in this pass: the finite boundary decompositions are stable, but their present value is the architecture-level narrowing above rather than a reusable formal bottleneck whose verification would materially change the line.