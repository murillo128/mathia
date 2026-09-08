# VIS-092 — one-dimensional Rips persistence of zero ordinates is exactly the adjacent-gap multiset

## Claim

Let

`X={x_1<...<x_n} subset R`

be any finite set of distinct real points, and let `VR_r(X)` be the Vietoris-Rips complex with the convention that a finite subset is a simplex exactly when its diameter is at most `r`. Put

`d_i=x_(i+1)-x_i`, `1<=i<=n-1`.

Then for every `r>=0`:

1. every connected component of `VR_r(X)` is contractible, so

   `H_q(VR_r(X))=0` for every `q>=1`;

2. the number of connected components is

   `beta_0(r)=1+#{i : d_i>r}`;

3. the degree-zero persistence barcode has one infinite bar and `n-1` finite bars whose death parameters, with multiplicity, are exactly

   `{d_1,...,d_(n-1)}`.

Consequently, standard one-parameter Vietoris-Rips persistent homology of a one-dimensional point cloud is completely determined by the **unordered multiset of adjacent gaps**. Conversely, its finite `H_0` death multiset recovers exactly that gap multiset. It contains no positive-dimensional persistent homology and forgets the order in which those gaps occur.

Applied to a finite set of Riemann-zero ordinates, raw or unfolded, a standard Rips barcode/persistence diagram is therefore not a new mesoscopic or fractal invariant of the zero process. In the unfolded coordinate it is exactly a repackaging of the nearest-neighbor gap multiset; any barcode texture or persistence-length distribution is already fixed by the one-gap data.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PERSISTENT-TOPOLOGY SPECIALIZATION + DECISIVE-NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No claim is made about intrinsically higher-dimensional embeddings, marked zero clouds, multiparameter filtrations, sublevel-set persistence of analytic fields, nonlocal graph filtrations, delay embeddings, or other constructions that deliberately add information beyond the scalar ordinate metric.

## 1. On the line the Rips complex is an interval nerve

Fix `r>=0`. Associate to each point `x_i` the closed interval

`I_i=[x_i-r/2, x_i+r/2]`.

For two vertices,

`I_i cap I_j != emptyset`

if and only if

`|x_i-x_j|<=r`.

A finite vertex set `sigma` is a simplex of `VR_r(X)` exactly when all of its pairwise distances are at most `r`. Equivalently, the corresponding intervals are pairwise intersecting.

Finite intervals on the real line have the one-dimensional Helly property: pairwise intersection already implies a common intersection. Hence

`VR_r(X)`

is exactly the nerve of the interval family `{I_i}`.

Every nonempty finite intersection of these intervals is itself an interval and therefore contractible. The nerve theorem identifies each connected component of the Rips complex with the corresponding connected component of the union

`U_r=union_i I_i`.

But every connected component of a union of intervals in `R` is an interval. Therefore every connected component of `VR_r(X)` is contractible. In particular no positive-dimensional homology class can be born at any scale:

`H_q(VR_r(X))=0`, `q>=1`.

The same conclusion can be phrased graph-theoretically. The Rips one-skeleton of points on the line is a unit-interval graph, hence chordal; connected chordal clique complexes are collapsible. The interval-nerve proof above makes the specialization immediate and does not require any zeta-specific input.

## 2. Degree-zero persistence is exactly single-linkage on adjacent gaps

The intervals `I_i` and `I_(i+1)` meet exactly when

`d_i<=r`.

A non-adjacent edge cannot merge components before the intervening adjacent gaps do: if `x_j-x_i<=r` for `i<j`, then every intervening adjacent gap is at most `x_j-x_i` and hence at most `r`.

Thus the connected components at threshold `r` are precisely the consecutive blocks obtained by cutting the ordered points at those indices for which `d_i>r`. This gives the exact count

`beta_0(r)=1+#{i:d_i>r}`.

At `r=0` all distinct points are separate. As `r` increases, one component merge occurs for each adjacent gap when its threshold is reached, with tied gaps producing simultaneous merges. Therefore the finite death parameters in the `H_0` barcode are exactly the multiset of adjacent gap lengths.

With the common alternative Cech convention in which the filtration parameter is the ball radius `epsilon`, the same event occurs at `epsilon=d_i/2`. This is only a parameter normalization; the information content is unchanged.

## 3. The barcode forgets gap order

Let two ordered point clouds have the same multiset of adjacent gaps but arrange those gaps in different orders. Their standard one-dimensional Rips persistence modules have the same barcode: all positive-dimensional groups vanish, and the finite `H_0` death parameters are the same multiset.

Hence the barcode cannot distinguish:

- adjacent-gap order;
- two-gap or three-gap conditional structure;
- long-range ordering of the gap sequence;
- where a large or small gap occurs in the sample;
- any arithmetic label or analytic feature not encoded in the scalar metric itself.

For unfolded zeta-zero ordinates this places the usual Rips persistence diagram at an even lower information level than the already-controlled consecutive-gap geometries in `VIS-019` and the later three-gap program: it retains the one-gap multiset but not the ordering needed for those higher-order statistics.

If zero multiplicity is represented by repeated coincident ordinates, an ordinary metric **set** removes that multiplicity before the filtration even begins. Preserving multiplicity requires an explicit mark or another data structure, which is then an additional information channel and must be audited separately.

## 4. Prior art and novelty assessment

Vietoris-Rips filtrations and persistent homology are standard computational-topology constructions; Herbert Edelsbrunner and John Harer, *Computational Topology: An Introduction*, AMS (2010), DOI `10.1090/mbk/069`, is a canonical reference.

The graph-theoretic specialization is also classical. Masamichi Kuroda and Shuhei Tsujie, **Unit Ball Graphs on Geodesic Spaces**, *Graphs and Combinatorics* 37 (2021), 111–125, DOI `10.1007/s00373-020-02231-3`, identifies unit-ball graphs on the real line with the unit-interval setting and places them in the strongly chordal class. Anton Dochtermann, **Exposed circuits, linear quotients, and chordal clutters**, *Journal of Combinatorial Theory, Series A* 177 (2021), 105327, DOI `10.1016/j.jcta.2020.105327`, records the standard fact that clique complexes of chordal graphs have collapsible components.

The exact `H_0` gap formula above is the elementary one-dimensional specialization of the standard minimum-spanning-tree/single-linkage interpretation of zero-dimensional persistence: the Euclidean minimum spanning tree on ordered points of `R` consists exactly of the adjacent edges.

No part of the topological statement is claimed as new. The Mathia-specific durable result is the **information-accounting consequence**: applying ordinary one-dimensional Rips/Cech persistence to zeta-zero ordinates cannot create a new fractal/topological channel; it strictly collapses to nearest-neighbor gap data and discards gap order.

## Boundary and falsification

The claim assumes the input to the filtration is a finite scalar point cloud with the ordinary absolute-distance metric. It does not say that persistent homology is useless for zeta research in general.

A genuinely different TDA construction can escape this obstruction by changing the information supplied to the filtration, for example through an intrinsically higher-dimensional or marked embedding, an analytic-field sublevel filtration, a nonlocal arithmetic graph, a delay-coordinate construction, or a multiparameter filtration. But such an escape must state exactly which new coordinate, relation, field value, or ordering information has been added; the resulting topology cannot be credited to the zero ordinates alone.

The result also does not assume RH. It concerns the one-dimensional point cloud of ordinates. If the full complex zero coordinates `(beta,gamma)` are used instead, the input is genuinely two-dimensional unless one separately assumes or restricts to zeros on the critical line, and the theorem no longer applies automatically.

Falsify the claim by producing a finite subset of `R` and a scale at which its standard Rips complex has nontrivial positive-dimensional homology, or by showing that its `H_0` death multiset differs from the adjacent-gap multiset under the stated threshold convention. Either would contradict the interval-nerve argument directly.

## Visual consequence

No canonical PNG is retained. A barcode rendering would be completely determined by the adjacent-gap list and would add no evidence. The exact collapse theorem is the more faithful artifact: it explains in advance why an apparently multiscale persistence plot of zero ordinates can look structured without containing any topology beyond nearest-neighbor spacing.

## Research consequence

Standard Vietoris-Rips/Cech persistent homology of scalar zero ordinates should be treated as a **closed baseline visualization**, not as a live route to mesoscopic fractal structure. Any future topological-data-analysis proposal in the critical-strip branch must expose and audit an additional information carrier rather than presenting a barcode of the one-dimensional zero sequence as a new invariant.

This narrows `CLUE-zeta-critical-strip-multiscale-geometry`: a surviving topological route must be intrinsically higher-dimensional, marked, field-based, nonlocal, ordered, incomplete, or multiparameter in a way that is not reconstructible from the ordinary adjacent-gap multiset.