# VIS-094 — static temporal-edge delay graphs add exactly one local block order

## Claim

Let

`a=(a_1,...,a_N)`

be a finite real sequence and fix `1<=m<N`. Write

`w_i=(a_i,...,a_(i+m-1)) in R^m`, `1<=i<=N-m+1`.

Form the **static directed window-transition multigraph** `D_m(a)` by identifying equal window values as the same vertex and, for every `1<=i<=N-m`, adding one directed edge

`w_i -> w_(i+1)`

with multiplicity.

Then the directed edge multiset of `D_m(a)` is in exact bijection with the unordered multiset of length-`(m+1)` blocks of `a`. The correspondence is

`(x_1,...,x_(m+1))`

`-> ((x_1,...,x_m) -> (x_2,...,x_(m+1)))`.

Conversely, every consistent transition edge recovers the unique `(m+1)`-block obtained by adjoining the last coordinate of its head to its tail. Therefore a static temporal-edge graph constructed this way adds **exactly one local block order** relative to the unordered `m`-window cloud of `VIS-093`, but it still forgets the order in which those transition edges were traversed.

Equivalently, the original sequence determines an Eulerian trail through the edge-occurrence multigraph, while the static graph retains the edge inventory but not the distinguished Eulerian trail. Any deterministic graph, topological, spectral, or geometric invariant that consumes only this static value-quotiented transition multigraph cannot distinguish two sequences having the same length-`(m+1)` block multiset.

If direction and multiplicity are discarded further and only the polygonal geometric trace

`T_m(a)=union_i [w_i,w_(i+1)] subset R^m`

is retained, still more information is lost. In particular, sequence reversal becomes invisible up to the coordinate-reversal isometry of `R^m`: the reversed trace is `J(T_m(a))`, where `J(x_1,...,x_m)=(x_m,...,x_1)`. Ordinary homology, Euclidean offsets, and persistence built only from that undirected geometric trace are therefore reversal-invariant.

The block-order loss is strict. For `m=2`, the positive sequences

`a=(1,1,2,1,1,1,1)`

and

`b=(1,1,1,2,1,1,1)`

have the same three-block multiset,

`(1,1,1) x2`, `(1,1,2) x1`, `(1,2,1) x1`, `(2,1,1) x1`,

so their complete directed two-window transition multigraphs, including edge multiplicities, are identical. Yet their four-block multisets differ: `a` contains `(1,1,1,1)` while `b` contains `(1,1,1,2)`. Thus the static temporal-edge graph cannot recover even the next local ordering layer, let alone the full global sequence.

Applied to a zeta-zero gap sequence, connecting consecutive delay vectors is therefore not by itself a nonlocal-order escape from `VIS-093`. A static directed transition graph lifts the information carrier from empirical `m`-blocks to empirical `(m+1)`-blocks. To retain genuinely longer ordering, the construction must preserve additional trail information rather than immediately quotient the trajectory to a static graph or geometric edge set.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DE-BRUIJN/EULERIAN SPECIALIZATION + NEGATIVE INFORMATION-LOSS CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that temporal graphs, directed topology, path-aware invariants, or sliding-window methods are useless. The result classifies only the information content of the static transition multigraph obtained from consecutive fixed-window values and of further invariants that factor through that graph.

## 1. Consecutive window edges are exactly `(m+1)`-blocks

Let

`u_i=(a_i,...,a_(i+m))`

be the length-`(m+1)` block beginning at position `i`. Define prefix and suffix maps

`P(x_1,...,x_(m+1))=(x_1,...,x_m)`,

`S(x_1,...,x_(m+1))=(x_2,...,x_(m+1))`.

Then by construction

`P(u_i)=w_i`, `S(u_i)=w_(i+1)`.

Hence every occurrence of an `(m+1)`-block contributes exactly the directed edge `P(u_i)->S(u_i)`, with repeated blocks contributing repeated edges.

Conversely, for an edge arising from consecutive windows, the overlap condition

`head_j = tail_(j+1)` for `1<=j<m`

holds automatically. Its tail `(x_1,...,x_m)` and head `(x_2,...,x_(m+1))` therefore reconstruct the unique block `(x_1,...,x_(m+1))`.

Thus the directed transition-edge multiset and the empirical `(m+1)`-block multiset are equivalent data. Adding those edges to the value-quotiented `m`-window cloud does not inject an unbounded memory of the original visitation order; it advances the local block inventory by one coordinate.

## 2. The missing datum is the distinguished Eulerian trail

The edge occurrences of `D_m(a)` are traversed by the original sequence in their chronological order. Consecutive edges fit because the head window of one occurrence is the tail window of the next. Therefore the original sequence induces an Eulerian trail through the occurrence multigraph: every transition occurrence is used exactly once.

But the static graph does not record **which Eulerian trail was taken** when several are compatible with the same edge inventory. Distinct trails can spell distinct sequences while preserving every `(m+1)`-block count.

This is the classical de Bruijn/Eulerian reconstruction viewpoint. In sequence assembly, `k`-mers are represented as directed edges from their `(k-1)`-prefixes to `(k-1)`-suffixes, and reconstruction is an Eulerian-path problem. Pevzner, Tang, and Waterman, **An Eulerian path approach to DNA fragment assembly**, *PNAS* 98:17 (2001), 9748–9753, DOI `10.1073/pnas.171285098`, is an established canonical reference for this graph representation and its reconstruction role.

The present statement is not claimed as a new graph theorem. Its Mathia-specific content is the information audit: a tempting "time-respecting" visual repair of ordinary delay-cloud persistence can still collapse immediately to a classical finite-memory block graph if the temporal edges are frozen into a static object.

## 3. Explicit collision beyond the edge inventory

For

`a=(1,1,2,1,1,1,1)`

and

`b=(1,1,1,2,1,1,1)`,

the length-three block counts agree exactly:

- `(1,1,1)` occurs twice;
- `(1,1,2)` occurs once;
- `(1,2,1)` occurs once;
- `(2,1,1)` occurs once.

At `m=2`, those are exactly the directed transition edges between two-windows. Both sequences therefore induce the same edge multiset

`(1,1)->(1,1) x2`,

`(1,1)->(1,2) x1`,

`(1,2)->(2,1) x1`,

`(2,1)->(1,1) x1`.

Their next-order blocks differ. The four-block multiset of `a` is

`(1,1,2,1)`, `(1,2,1,1)`, `(2,1,1,1)`, `(1,1,1,1)`,

while that of `b` is

`(1,1,1,2)`, `(1,1,2,1)`, `(1,2,1,1)`, `(2,1,1,1)`.

So even retaining directed edge multiplicities does not recover how transition edges follow one another. A static graph invariant may exploit genuine three-block information absent from the bare two-window cloud, but it cannot certify a four-block or global ordering channel without additional data.

## 4. Undirected geometric traces lose direction as well

Suppose the visual construction forgets directed edge identity and retains only the union of Euclidean segments

`T_m(a)=union_i [w_i,w_(i+1)]`.

This object is determined by the set of undirected transition segments, so repeated traversal and chronology have disappeared.

For the reversed sequence `a^R`, each window is `J(w_j)` for the appropriate reversed index `j`, and each consecutive transition is traversed in the opposite direction. Because an undirected segment satisfies `[x,y]=[y,x]`,

`T_m(a^R)=J(T_m(a))`.

The coordinate reversal `J` is orthogonal. Consequently any Euclidean-isometry-invariant construction depending only on `T_m(a)` — ordinary homology, distance offsets, nerves of equal-radius balls, or persistence derived from those offsets — agrees for a sequence and its reversal.

A directed invariant need not have this reversal symmetry; direction can carry a local arrow. But if that directed invariant still factors only through `D_m(a)`, it remains bounded by the `(m+1)`-block multiset established above.

## 5. Prior art and novelty assessment

Sliding-window/time-delay embeddings and persistence are classical methodology; Perea and Harer, **Sliding Windows and Persistence: An Application of Topological Methods to Signal Analysis**, *Foundations of Computational Mathematics* 15:3 (2015), 799–838, DOI `10.1007/s10208-014-9206-z`, is the baseline already used in `VIS-093`.

The prefix/suffix transition graph is also classical de Bruijn/Eulerian sequence-reconstruction structure. The 2001 Pevzner–Tang–Waterman paper above gives an authoritative applied instance in which fixed-length words are edges between overlapping shorter words and compatible sequences are Eulerian traversals.

No novelty is claimed for either ingredient or for the elementary bijection between `(m+1)`-blocks and consecutive `m`-window transitions. The value of `VIS-094` is as a precise negative control for the live visual/TDA route: **static temporal adjacency is not the same thing as preserving the trajectory order**.

## Boundary and falsification

The theorem concerns the value-quotiented static transition multigraph and constructions that factor through it. It does not cover an indexed path in which every occurrence `w_i` remains a distinct vertex carrying its time index; such a representation can retain the full visitation sequence by definition.

It also does not classify:

- prefix-by-prefix or genuinely time-indexed filtrations;
- zigzag or dynamic persistence that consumes a sequence of changing spaces rather than one frozen graph;
- path signatures, iterated integrals, or other invariants of an ordered parametrized curve;
- directed constructions that retain occurrence identities or higher transition order;
- a time/index coordinate appended to each window;
- window length or memory order growing materially with the observation scale;
- independent analytic marks such as `Z(g_n)`, derivative values, zero multiplicity, or another field coordinate.

Those are legitimate possible escapes because they supply information not equivalent to the static `(m+1)`-block inventory. They still require an explicit information audit: if the extra structure itself trivially contains the desired order, a visually richer output is not evidence of new arithmetic organization.

Falsify the main claim by producing two consistent consecutive-window transition edges with the same tail and head but different underlying `(m+1)` blocks, or by producing two sequences with the same `(m+1)`-block multiset whose value-quotiented directed transition multigraphs differ. Either would contradict the prefix/suffix bijection directly.

## Visual consequence

No canonical PNG is retained. This is an exact pre-render control. A trajectory graph can look dramatically richer than an unordered delay cloud, but if the rendering is made from the frozen value-quotiented consecutive-edge graph, the new information is precisely one higher local block inventory plus whatever further quotient the renderer imposes.

## Research consequence

`CLUE-zeta-critical-strip-multiscale-geometry` should narrow the proposed "time-respecting edge" escape. Merely connecting consecutive fixed-window vectors and then analyzing the resulting static graph is only a finite-memory lift from `m`-blocks to `(m+1)`-blocks. A genuinely nonlocal topological route must preserve the distinguished trail, use a dynamically indexed filtration, let memory grow in a mathematically material way, or add an independent source coordinate whose contribution is not reconstructible from the same fixed local block inventory.