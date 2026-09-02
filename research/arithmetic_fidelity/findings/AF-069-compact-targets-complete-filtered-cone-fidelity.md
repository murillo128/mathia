# AF-069 — Compact targets complete filtered cone fidelity by intersections

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a finite-dimensional real normed space. For a nonempty family `\mathcal K` of cones in `V`, each containing `0`, and an arbitrary subset `S\subseteq V`, define

\[
H_{\mathcal K}(S)
=
\bigcap_{K\in\mathcal K}(S-K).
\tag{1}
\]

Equivalently,

\[
m\in H_{\mathcal K}(S)
\iff
S\cap(m+K)\ne\varnothing
\quad\forall K\in\mathcal K.
\tag{2}
\]

For a class `\mathscr C` of admissible targets, define the cone consequences of `\mathcal K` by

\[
\operatorname{Imp}_{\mathscr C}(\mathcal K)
=
\left\{
L:
H_{\mathcal K}(S)\subseteq S-L
\text{ for every }S\in\mathscr C
\right\}.
\tag{3}
\]

Thus `L` is a consequence when every point passing all `\mathcal K`-tests automatically has an actual target witness in the translated cone `m+L`.

Then:

1. **For arbitrary targets, the complete consequence relation is still plain containment cofinality, even for infinite presentations.** If `\mathscr C` is the class of all subsets of `V`, then
   \[
   \boxed{
   \operatorname{Imp}_{\mathrm{all}}(\mathcal K)
   =
   \{L:\exists K\in\mathcal K\text{ with }K\subseteq L\}.
   }
   \tag{4}
   \]
   More generally,
   \[
   H_{\mathcal K}(S)\subseteq H_{\mathcal L}(S)
   \quad\forall S\subseteq V
   \]
   iff every `L\in\mathcal L` contains some `K\in\mathcal K`. Finiteness was therefore not needed for AF-068's universal-comparison theorem; it was needed for the existence of a canonical inclusion-minimal antichain presentation.

2. **Compact targets add genuine limit consequences.** Let `\mathscr K_c` be the class of nonempty compact subsets of `V`, and restrict consequence cones to closed cones. If
   \[
   \{L_\alpha\}_{\alpha\in A}
   \subseteq
   \operatorname{Imp}_{\mathscr K_c}(\mathcal K)
   \tag{5}
   \]
   is downward directed under inclusion, meaning that for every finite set of indices there exists `\gamma` with
   \[
   L_\gamma\subseteq\bigcap_j L_{\alpha_j},
   \tag{6}
   \]
   then
   \[
   \boxed{
   \bigcap_{\alpha\in A}L_\alpha
   \in
   \operatorname{Imp}_{\mathscr K_c}(\mathcal K).
   }
   \tag{7}
   \]
   Thus compact-target consequence is closed under filtered meets of closed cone constraints.

3. **A downward-directed family collapses to its intersection on compact targets.** If `\mathcal K` itself is a nonempty downward-directed family of closed cones and
   \[
   K_\infty=\bigcap_{K\in\mathcal K}K,
   \tag{8}
   \]
   then for every nonempty compact `S`,
   \[
   \boxed{
   H_{\mathcal K}(S)=S-K_\infty.
   }
   \tag{9}
   \]
   Infinitely many moving-witness constraints become exactly one limit-cone constraint once the target category is compact.

4. **The same collapse fails for arbitrary, closed noncompact, and bounded nonclosed targets.** In `V=\mathbb R^2`, put
   \[
   K_n
   =
   \{(x,y):x\ge0,\ |y|\le x/n\},
   \qquad n\ge1.
   \tag{10}
   \]
   Then
   \[
   K_{n+1}\subsetneq K_n,
   \qquad
   K_\infty
   =
   \bigcap_{n\ge1}K_n
   =
   \{(x,0):x\ge0\}.
   \tag{11}
   \]
   For the closed noncompact set
   \[
   S_{\mathrm{esc}}=\{(n,1):n\ge1\},
   \tag{12}
   \]
   one has `(n,1)\in K_n`, so
   \[
   0\in H_{\{K_n\}}(S_{\mathrm{esc}}),
   \]
   but `S_{\mathrm{esc}}\cap K_\infty=\varnothing`. Likewise the bounded nonclosed set
   \[
   S_{\mathrm{miss}}=\{(1,1/n):n\ge1\}
   \tag{13}
   \]
   meets every `K_n` but misses `K_\infty`. Adding the missing limit point `(1,0)` makes the latter target compact and restores the limit witness exactly as (9) predicts.

5. **Compact consequence is not closed under arbitrary intersections.** The filtered hypothesis cannot simply be replaced by an unrestricted meet rule. In `V=\mathbb R`, let
   \[
   L_+=\mathbb R_{\ge0},
   \qquad
   L_-=\mathbb R_{\le0},
   \qquad
   \mathcal K=\{L_+,L_-\}.
   \tag{14}
   \]
   Both `L_+` and `L_-` are trivially consequences of `\mathcal K`, but for the compact target
   \[
   S=\{-1,1\}
   \tag{15}
   \]
   one has `0\in H_{\mathcal K}(S)` while
   \[
   S\cap(L_+\cap L_-)
   =S\cap\{0\}
   =\varnothing.
   \tag{16}
   \]
   Compactness can merge a coherent descending family of witnesses into a limit witness; it does not fuse incompatible witness branches merely because all individual constraints are satisfied.

6. **Infinite presentations need not possess inclusion-minimal generators.** The family `(K_n)` in (10) has no inclusion-minimal member. Hence AF-068's finite antichain canonicalization does not extend by simply taking `\min(\mathcal K)`. On arbitrary targets the canonical information state is the generated containment upper set from (4), whereas on compact targets the same presentation acquires additional filtered-limit consequences such as `K_\infty`.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{the logical content of an infinite compression presentation depends on the admissible target category;}\\
\text{arbitrary targets retain only algebraic containment consequences,}\\
\text{while compact targets also turn coherent filtered limits into real witness constraints.}
\end{array}
}
\tag{17}
\]

This is a precise form of category-dependent structural fidelity. A relation that is genuinely lost when arbitrary sources may chase ever-narrower tests can become recoverable when compactness forces the moving witnesses to have a common limit. Conversely, compactness does not erase provenance across unrelated branches: without a directed refinement, distinct witnesses need not coalesce.

## Derivation

### Arbitrary-target consequences are exactly the containment upper closure

If some `K\in\mathcal K` satisfies `K\subseteq L`, then

\[
S-K\subseteq S-L
\tag{18}
\]

for every `S`, hence

\[
H_{\mathcal K}(S)
\subseteq S-K
\subseteq S-L.
\tag{19}
\]

Thus every cone containing a declared generator is a universal consequence.

Conversely, suppose no `K\in\mathcal K` is contained in `L`. Then every difference set

\[
K\setminus L
\tag{20}
\]

is nonempty. Define, without making any choice of representatives,

\[
S_L
=
\bigcup_{K\in\mathcal K}(K\setminus L).
\tag{21}
\]

For every `K\in\mathcal K`, the set `S_L` meets `K`, so

\[
0\in H_{\mathcal K}(S_L).
\tag{22}
\]

But by construction `S_L\cap L=\varnothing`, hence

\[
0\notin S_L-L.
\tag{23}
\]

Therefore `L` is not a consequence on arbitrary targets. This proves (4). Applying the same statement separately to every member of `\mathcal L` gives the infinite-family extension of AF-068's cofinality comparison.

The important distinction from AF-068 is now visible: mutual cofinality still classifies arbitrary-target hull operators, but an infinite cofinality class need not contain any minimal member. A canonical finite clutter/antichain presentation is therefore a finiteness phenomenon, not part of the universal order theorem itself.

### Compactness turns a filtered consequence family into its meet

Let `S` be nonempty compact and let

\[
m\in H_{\mathcal K}(S).
\tag{24}
\]

For every `\alpha`, assumption (5) implies

\[
m\in S-L_\alpha,
\]

so the subset

\[
F_\alpha
=
S\cap(m+L_\alpha)
\tag{25}
\]

is nonempty. Since each `L_\alpha` is closed, every `F_\alpha` is closed in the compact space `S`.

The downward-directed property gives the finite-intersection property. Given `\alpha_1,\ldots,\alpha_r`, choose `\gamma` satisfying (6). Then

\[
F_\gamma
\subseteq
\bigcap_{j=1}^r F_{\alpha_j},
\tag{26}
\]

and the left-hand side is nonempty. Compactness therefore gives

\[
\bigcap_{\alpha\in A}F_\alpha\ne\varnothing.
\tag{27}
\]

But

\[
\bigcap_{\alpha\in A}F_\alpha
=
S\cap\left(m+\bigcap_{\alpha\in A}L_\alpha\right).
\tag{28}
\]

Hence `m` has an actual target witness in the meet cone, proving (7).

If the original family `\mathcal K` is itself downward directed, apply (7) to its members, which are trivially consequences of themselves. This gives

\[
H_{\mathcal K}(S)
\subseteq S-K_\infty.
\tag{29}
\]

The reverse inclusion is purely algebraic because `K_\infty\subseteq K` for every `K\in\mathcal K`:

\[
S-K_\infty
\subseteq
\bigcap_{K\in\mathcal K}(S-K)
=H_{\mathcal K}(S).
\tag{30}
\]

Together (29) and (30) prove (9).

### The moving-witness obstruction without compactness

For (10), each `K_n` is a closed convex cone and the family is strictly decreasing. The intersection statement in (11) is immediate: if `(x,y)` lies in every `K_n`, then

\[
|y|\le x/n
\quad\forall n,
\]

so `y=0` and `x\ge0`.

The target `S_{\mathrm{esc}}` is closed because it has no finite accumulation point, and it is noncompact because it is unbounded. For every `n`, its point `(n,1)` satisfies

\[
1\le n/n,
\]

hence belongs to `K_n`. The witness required by the `n`-th constraint therefore escapes to infinity as the cone narrows. No point of the target lies on the limit ray.

For `S_{\mathrm{miss}}`, the witnesses stay bounded but converge to a point deliberately omitted from the target. Thus closedness failure can replace escape-to-infinity failure. The compact completion

\[
\overline{S_{\mathrm{miss}}}
=S_{\mathrm{miss}}\cup\{(1,0)\}
\tag{31}
\]

contains exactly the limiting witness forced by the finite-intersection argument.

These two controls separate the roles of boundedness and closedness in finite dimension: compactness needs both. The theorem is not a statement that setwise convergence of `K_n` alone preserves hitting; it is the compact target that prevents witnesses from escaping or disappearing at a missing boundary point.

### Why unrelated meets remain non-faithful

In the one-dimensional control (14)--(16), the two cone constraints use different points of `S`. The sets

\[
F_+=S\cap L_+=\{1\},
\qquad
F_-=S\cap L_-=\{-1\}
\tag{32}
\]

are both nonempty and closed in compact `S`, but they do not have the finite-intersection property. Compactness therefore has nothing to apply to. This is exactly the provenance distinction: the two surviving observations are individually witnessed, but no coherent refinement says that they arose from one common upstream point.

## Prior art and novelty assessment

The mathematical mechanisms used here are classical.

- James R. Munkres, ***Topology***, 2nd ed., Prentice Hall (2000), §26. Compactness is equivalent to the statement that every family of closed sets with the finite-intersection property has nonempty total intersection; nested closed-set intersection is a standard corollary. Equation (27) is a direct application of that theorem.
- Gerald Beer, ***Topologies on Closed and Closed Convex Sets***, Mathematics and Its Applications 268, Kluwer Academic Publishers (1993), DOI `10.1007/978-94-015-8149-3`. The monograph develops hit-and-miss hyperspace topologies together with Fell and Kuratowski--Painlevé set convergence. It is the closest established language for treating constraints through which closed sets are hit or missed while the constraint sets themselves vary.
- R. Tyrrell Rockafellar and Roger J.-B. Wets, ***Variational Analysis***, Grundlehren der mathematischen Wissenschaften 317, Springer (1998), DOI `10.1007/978-3-642-02431-3`, especially the chapter on set convergence. This supplies standard variational-analysis context for limits of closed/convex sets and prevents interpreting the limit-cone language itself as new structure.

No novelty is claimed for the finite-intersection property, filter-base compactness, nested closed-set limits, cone intersections, or hit-and-miss/set-convergence language. The arbitrary-family cofinality argument is an elementary extension of AF-068.

The Arithmetic Fidelity contribution is the exact category comparison encoded by (4) and (7): the same declared compression family has a strictly larger consequence theory when sources are restricted to compact targets, but that enlargement is controlled by coherent filtered witness families rather than by arbitrary intersections. This turns `minimal lift` and `canonical retained structure` into category-indexed notions rather than presentation-only notions.

## Boundary conditions and falsification tests

1. **Closedness of the consequence cones matters.** The compactness proof uses `S\cap(m+L_\alpha)` as closed subsets of `S`. Without closed constraints, a nested family can converge to a boundary that every open constraint hits while the target misses the limiting intersection.
2. **Compactness of the target matters.** Equations (12) and (13) provide separate closed-noncompact and bounded-nonclosed failures.
3. **Downward directedness is not cosmetic.** Equation (16) shows that individual compact-target consequences need not survive an arbitrary intersection.
4. **No claim of a complete characterization of `\operatorname{Imp}_{\mathscr K_c}` is made.** Filtered-meet closure is a rigorous additional rule, not a proof that every compact-target consequence arises by iterating containment and filtered intersections.
5. **No topology may be silently imported into the arbitrary-target theorem.** Equation (4) deliberately quantifies over all subsets, so an unrepresented limit cone is not a consequence merely because it is a Hausdorff, Fell, Wijsman, or Kuratowski--Painlevé limit of declared generators.
6. **Target-category changes are mathematical assumptions, not free repairs.** A downstream RH construction may use compactness only if its actual retained object genuinely lives in a compact admissible class; one cannot recover a lost discriminator by imposing compactness after the compression without independent justification.

A decisive falsification of the compact filtered-meet claim would require a nonempty compact `S`, a downward-directed family of closed consequence cones, and a point `m` whose translated target intersections are all nonempty but whose total intersection is empty. That would contradict the classical finite-intersection characterization of compactness, so within the stated hypotheses the result is exact.

## Consequences for Arithmetic Fidelity

AF-068 identified the finite cone presentation with a canonical inclusion antichain. AF-069 shows exactly where that finite picture stops being intrinsic.

For an infinite family there may be no minimal declared generator at all. On unrestricted targets, nothing repairs this: the hull operator remembers only the generated containment upper set. On compact targets, however, coherent descending tests can force a new limit constraint that was absent from the presentation, and an entire filtered family can collapse to one meet cone.

This yields a practical audit rule for future compression mechanisms:

\[
\boxed{
\text{before calling a lift or retained discriminator minimal, specify the admissible source/target category.}
}
\tag{33}
\]

In particular, when an RH-relevant construction uses infinitely many increasingly sharp local, spectral, boundary, or asymptotic tests, one must distinguish two cases. If admissible witnesses can escape or omit their limit, satisfying every finite-stage test does not preserve the limiting discriminator. If the actual mathematical category supplies compactness and closed coherent constraints, the limiting discriminator may already be forced and should not be counted as an additional independent lift.

The next unresolved structural question is to characterize the full compact-target consequence class beyond filtered meets: which additional cone constraints are forced by hit-and-miss topology or convexity, and when can that larger consequence theory itself be given a canonical presentation without smuggling in the original target.