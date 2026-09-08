# VIS-096 — fixed-delay signatures through level three, and planar level four, remain edge-current determined

## Claim

Let

`a=(a_1,...,a_N)`

be a finite real sequence and fix `1<=m<N`. Write

`w_i=(a_i,...,a_(i+m-1)) in R^m`, `1<=i<=M=N-m+1`,

and let `X_a` be the ordinary unaugmented piecewise-linear path that visits

`w_1,w_2,...,w_M`

in chronological order.

Then the complete signature of `X_a` through tensor level three is determined by only:

1. the first and last delay windows `w_1,w_M`; and
2. the unordered multiset of length-`(m+1)` blocks

`u_i=(a_i,...,a_(i+m))`, `1<=i<=N-m`.

Equivalently, for any piecewise-linear path in `R^m`, signature levels one through three are determined by its starting point together with the unordered multiset of its **oriented geometric edges**. For a fixed-delay path, each `(m+1)` block determines exactly one such oriented edge.

There is one further exact planar restriction. When `m=2`, the same data determine the complete signature through **level four**. Thus an unaugmented two-coordinate delay path cannot recover genuinely nonlocal visitation order at signature depths `1,2,3,4` once the unordered three-block multiset and endpoint windows are fixed.

The planar level-four statement follows by closing the path with the fixed endpoint chord. The resulting closed polygonal curve has a winding-number function determined additively by its oriented edge multiset plus that chord. Boedihardjo–Ni–Qian prove that the first four homogeneous terms of the log signature of any closed planar finite-`p`-variation curve, `1<=p<2`, are determined by its winding-number function. Chen concatenation with the fixed closing chord then recovers the original open signature through level four.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BACKED PLANAR DEGREE-FOUR BOUNDARY + NEGATIVE INFORMATION-LOSS CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that level four is local-block determined for general `m>=3`, or that planar level five necessarily distinguishes delay sequences sharing the same local block inventory. The result only identifies the first signature depths not already excluded by this particular information-current argument.

## 1. Levels one and two are edge-current data

Translate the path conceptually by its starting point `x_0`; signatures of increments are translation invariant. Write

`Y(t)=X(t)-x_0`.

For tensor coordinates, let

`S_i = integral dX_i`,

`S_(i,j) = integral_(t_1<t_2) dX_i(t_1)dX_j(t_2)`.

Then

`S_i=Y_i(1)`

and, by integrating the prefix increment,

`S_(i,j)=integral Y_i dX_j`.

For a straight oriented edge `p -> q`, with

`y=p-x_0`, `v=q-p`,

the edge contribution is

`integral_edge Y_i dX_j = v_j (y_i + v_i/2)`.

Hence every second-level coordinate is the sum of a fixed polynomial function of the oriented edges. This is the same edge-current content that underlies the Levy-area specialization in `VIS-095`.

## 2. Every third-level coordinate is also edge additive

For a third-level coordinate `S_(i,j,k)`, the shuffle identity gives

`S_(i,j) S_k = S_(i,j,k) + S_(i,k,j) + S_(k,i,j)`.

At each prefix of the path,

`Y_i Y_k = S_(i,k)(prefix) + S_(k,i)(prefix)`.

Therefore

`integral Y_i Y_k dX_j = S_(i,k,j) + S_(k,i,j)`,

and subtraction yields the exact identity

`S_(i,j,k) = S_(i,j) S_k - integral Y_i Y_k dX_j`.

The remaining integral is again edge additive. On one straight edge `p -> q`, with `y=p-x_0` and `v=q-p`,

`integral_edge Y_i Y_k dX_j`
` = v_j [ y_i y_k`
`           + (1/2)(y_i v_k + y_k v_i)`
`           + (1/3) v_i v_k ].`

Thus `S_(i,j,k)` is determined by the starting point and the unordered multiset of oriented edges. Traversal order of those same edge occurrences cannot change any coordinate through level three.

This argument is dimension-independent and does not use any property special to zeta, gaps, or delay embeddings.

## 3. Delay blocks fix the complete oriented-edge multiset

For the fixed-`m` delay path, the edge from `w_i` to `w_(i+1)` is

`(a_i,...,a_(i+m-1)) -> (a_(i+1),...,a_(i+m))`.

It is therefore a deterministic function of the single `(m+1)` block

`u_i=(a_i,...,a_(i+m))`.

Consequently the unordered `(m+1)`-block multiset determines the unordered multiset of directed geometric edges, with multiplicity. The first and last `m`-windows fix the boundary data.

Combining this observation with the edge-additive formulas above proves the delay-path claim through level three.

The explicit collision already used in `VIS-094` and `VIS-095` therefore remains a collision at level three. For `m=2`,

`a=(1,1,2,1,1,1,1)`,

`b=(1,1,1,2,1,1,1)`

have the same length-three block multiset and the same first/last two-windows, while their length-four block multisets differ. Their delay paths consequently have identical signatures through level three despite different assembly of the same local transition inventory.

## 4. In the plane, the fourth level is still fixed by the same edge current

Now specialize to `m=2`. Let `C` be the straight chord from `w_M` back to `w_1`, and let

`Gamma = X_a * C`

be the closed planar polygonal curve obtained by concatenation.

For any point `z` off the curve, its winding number can be written as the line integral

`eta_Gamma(z) = (1/(2 pi i)) integral_Gamma dζ/(ζ-z)`.

This integral is additive over oriented edges. Therefore the winding-number function of `Gamma` is determined by the unordered oriented-edge multiset of `X_a` together with the fixed closing chord. Any two delay paths with the same three-block multiset and the same endpoint windows give chord-closed curves with the same winding number around every point away from the common oriented polygonal current.

Boedihardjo, Ni, and Qian prove for continuous closed planar curves of finite `p`-variation, `1<=p<2`, that the first four homogeneous terms of the **log signature** are functions of the winding-number function alone. Polygonal curves are within this class. Hence the truncated log signatures of the two closed curves agree through degree four, and so do their signatures through degree four because the exponential relation between log signature and signature is triangular by degree.

Finally Chen multiplicativity gives

`S(Gamma)=S(X_a) tensor S(C)`.

The closing chord is fixed by `w_1,w_M`, and its signature has a fixed tensor inverse. Thus the open-path signature `S(X_a)` through degree four is determined by the closed signature through degree four and the endpoint chord. This proves the planar claim.

The same literature result also shows that the number four is sharp for **general closed planar curves**: equal winding functions need not force equal fifth signature terms. That sharpness does not by itself construct two delay paths with equal three-block multisets and different fifth signatures; it only shows that winding/current data cease to be a universal degree-five determination principle.

## 5. Prior art and novelty assessment

Path signatures and their full uniqueness up to tree-like equivalence for bounded-variation paths are classical. Ben Hambly and Terry Lyons, **Uniqueness for the signature of a path of bounded variation and the reduced path group**, *Annals of Mathematics* 171:1 (2010), 109–167, DOI `10.4007/annals.2010.171.109`, is the standard uniqueness boundary.

Horatio Boedihardjo, Hao Ni, and Zhongmin Qian, **Uniqueness of signature for simple curves**, *Journal of Functional Analysis* 267:6 (2014), 1778–1806, DOI `10.1016/j.jfa.2014.06.006`, arXiv `1304.0755`, prove that moments of the winding number appear in the planar log signature and state in Corollary 2 that the first four terms of the log signature of a closed planar finite-`p`-variation curve are determined by the winding-number function. They also show that degree four is sharp in the general planar closed-curve class.

No novelty is claimed for shuffle identities, Chen multiplicativity, path signatures, winding-number moments, or the planar degree-four theorem. The Mathia-specific contribution is the exact information audit for a **sliding-window delay path**: its unordered `(m+1)`-block inventory already fixes the full oriented edge current, which in turn fixes signature degrees through three in every dimension and, after chord closure, degree four in the planar `m=2` case.

## Boundary and falsification

The theorem concerns the ordinary unaugmented polygonal path through fixed-dimensional delay windows.

It does not classify:

- signature level four for general delay dimension `m>=3`;
- signature level five or higher for the planar `m=2` path;
- the full signature, whose complete information is much richer up to the usual tree-like equivalence;
- a time/index coordinate appended to the delay path;
- lead-lag, visibility, or other lifts that add coordinates before taking signatures;
- occurrence-labelled edges or another carrier that directly retains chronology;
- delay dimension, memory order, or signature depth growing materially with observation scale;
- independent analytic marks such as `Z(g_n)`, derivatives, zero multiplicity, or another field coordinate.

For arbitrary `m`, level four is therefore the first signature depth not ruled out by this edge-additivity result. For planar `m=2`, level five is the first depth not ruled out after adding the winding-number theorem. These are **open gates, not positive signals**.

Falsify the general level-three claim by producing two piecewise-linear paths with the same start and the same oriented-edge multiset but different signatures through degree three, or by finding a third-level coordinate that violates the displayed shuffle/edge-integral identity.

Falsify the planar level-four specialization by producing two planar fixed-delay paths with the same three-block multiset and endpoint windows but different fourth-level signatures, or by showing that their chord closures can have different winding functions despite identical oriented-edge currents.

## Visual consequence

No canonical PNG is retained. This is an exact pre-render information audit. Rendering level-three signature tensors or planar level-four features could create visually rich separation between datasets, but at fixed delay dimension those features cannot be interpreted as nonlocal chronology unless the comparison first escapes the local-block/current quotient established here.

## Research consequence

`CLUE-zeta-critical-strip-multiscale-geometry` should narrow again. A fixed-`m` unaugmented delay-path proposal cannot claim genuinely nonlocal order from signature levels `1`–`3`; in the commonly visualized planar `m=2` delay portrait, levels `1`–`4` are already fixed by the local three-block edge current plus endpoints.

A live signature-based escape must therefore begin, at minimum, with level four in dimension `m>=3`, level five in the planar `m=2` case, or with a mathematically justified augmentation/growing-memory construction. Any such candidate still has to demonstrate that its added degree of freedom survives the relevant lower-order spectral-statistics and representation controls rather than merely producing a richer picture.