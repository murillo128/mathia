# VIS-093 — fixed-window sliding-window persistence forgets delay-vector order

## Claim

Let

`a=(a_1,...,a_N)`

be a finite real sequence and fix `1<=m<=N`. Define the indexed sliding-window cloud

`W_m(a)={w_i=(a_i,...,a_(i+m-1)) in R^m : 1<=i<=N-m+1}`

with the ordinary Euclidean metric on window vectors. Build an ordinary unweighted Vietoris-Rips or Cech filtration from this cloud.

Then the complete persistence module is invariant under every relabelling of the window indices. Consequently it depends on at most the **unordered multiset of length-`m` window vectors** (and on only the set of distinct vectors when an implementation deduplicates coincident windows). The temporal/index order in which those windows were visited is not an additional input to ordinary point-cloud persistence.

More strongly, if two sequences have window clouds related by one global Euclidean isometry, their ordinary Rips/Cech persistence modules are isomorphic at every filtration scale. In particular, sequence reversal is always invisible. If

`a^R_j=a_(N+1-j)`,

then the windows of `a^R` are the windows of `a` in reverse index order followed by the coordinate-reversal map

`J(x_1,...,x_m)=(x_m,...,x_1)`,

and `J` is orthogonal. Thus

`PH(W_m(a^R)) = PH(W_m(a))`

for ordinary Euclidean Rips/Cech persistence.

This is a strict information-loss boundary, not merely a symmetry curiosity. For `m=2`, the distinct positive sequences

`a=(1,1,1,1,2,1,2)`

and

`b=(1,1,1,2,1,1,2)`

have exactly the same two-window multiset,

`{(1,1) x3, (1,2) x2, (2,1) x1}`,

and hence identical ordinary sliding-window persistence in every degree at every scale, while their three-window multisets differ. They therefore have different higher-order ordering information that fixed two-window point-cloud persistence cannot recover.

Applied to a zeta-zero gap sequence, a fixed-`m` delay embedding can genuinely escape the one-dimensional collapse of `VIS-092` by creating positive-dimensional geometry in `R^m`, but its ordinary persistence still cannot be interpreted as a nonlocal ordering invariant without an information audit. It sees the geometry of the empirical local `m`-block cloud and forgets how those blocks are sequenced.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-SLIDING-WINDOW/PERSISTENCE SPECIALIZATION + NEGATIVE INFORMATION-LOSS CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that sliding-window persistence is useless: it can detect real local `m`-block geometry, periodic/quasiperiodic structure represented in the delay cloud, or other information absent from the scalar one-dimensional point cloud. The claim is only that ordinary point-cloud persistence discards the external ordering of the delay vectors once the cloud has been formed.

## 1. Ordinary persistence is a function of the metric cloud, not its visitation order

For each scale `r`, the Vietoris-Rips complex is determined by the pairwise distances

`||w_i-w_j||_2`.

Permuting the vertex labels by any permutation `pi` replaces `w_i` by `w_(pi(i))` but leaves the finite metric space unchanged up to isometry. The corresponding Rips complexes are simplicially isomorphic for every `r`, and these isomorphisms commute with the inclusion maps of the filtration. Hence all persistent homology groups and barcodes are unchanged.

The same argument applies to the ordinary Euclidean Cech filtration: a global relabelling changes neither the balls nor their intersections, only their names. A global Euclidean isometry moves every ball isometrically and therefore preserves every nerve in the filtration.

Thus ordinary Rips/Cech persistence consumes the geometric point cloud after the time-series-to-window map. It does **not** separately consume the sequence

`w_1,w_2,...,w_(N-m+1)`

as an ordered trajectory.

If coincident windows occur, treating them as indexed zero-distance vertices or deduplicating them does not rescue the lost order. Indexed duplicates are still invariant under relabelling; deduplication throws away still more information.

## 2. Reversal is an exact Euclidean isometry of every fixed-window cloud

Let `a^R` denote the reversed sequence. Its `i`-th window is

`(a_(N+1-i), a_(N-i), ..., a_(N-m+2-i))`.

If `j=N-m+2-i`, this is exactly

`J(w_j)`

where `J` reverses the `m` coordinates. Since `J` is represented by a permutation matrix,

`||Jx-Jy||_2=||x-y||_2`.

The reversed delay cloud is therefore an isometric copy of the original delay cloud, with the window indices traversed in reverse order. Ordinary Rips/Cech persistence cannot distinguish the two.

This remains true for any coordinate-permutation-invariant norm. Euclidean distance is enough for the standard TDA setting used here.

## 3. Fixed local windows do not determine longer-range order

The two explicit sequences in the claim give an elementary finite witness. Their consecutive pair multisets are both

- three copies of `(1,1)`;
- two copies of `(1,2)`;
- one copy of `(2,1)`.

Therefore their complete `m=2` indexed metric clouds are isometric after relabelling, so every ordinary persistence barcode is identical.

But their three-window multisets differ. For `a`, the three-block counts are

`(1,1,1) x2`, `(1,1,2) x1`, `(1,2,1) x1`, `(2,1,2) x1`,

whereas for `b` they are

`(1,1,1) x1`, `(1,1,2) x2`, `(1,2,1) x1`, `(2,1,1) x1`.

The sequences even have the same symbol counts and the same endpoints, so the difference is not merely an endpoint-count artifact. Fixed two-window persistence has forgotten information that appears immediately at the next local order.

The general information statement does not require constructing all such collisions: whenever two sequences have the same unordered length-`m` window multiset, ordinary persistence of that delay cloud must agree. Distinguishing them requires either increasing the supplied window information or retaining additional structure beyond the point cloud.

## 4. Prior art and novelty assessment

Sliding-window/time-delay embeddings followed by persistent homology are established methodology. Jose A. Perea and John Harer, **Sliding Windows and Persistence: An Application of Topological Methods to Signal Analysis**, *Foundations of Computational Mathematics* 15:3 (2015), 799–838, DOI `10.1007/s10208-014-9206-z`, develops the point-cloud/persistent-homology framework and proves structural results connecting delay-cloud geometry to signal periodicity.

The present order-loss statement is not claimed as a new TDA theorem. It is the elementary information-accounting consequence of that standard pipeline: once delay vectors are handed to an ordinary point-cloud filtration, permutation of their visitation indices is invisible, and coordinate reversal gives an exact isometry for a reversed scalar sequence.

The Mathia-specific value is as a control on the topological escape explicitly left open by `VIS-092`. A visually nontrivial loop or torus in a delay embedding may be genuine geometry of local gap blocks, but ordinary persistence alone does not certify a new **nonlocal ordering** channel in the zeta-zero sequence.

## Boundary and falsification

The claim concerns ordinary unweighted Rips/Cech persistence of a fixed-dimensional sliding-window cloud with the usual point-cloud metric. It does not cover constructions that deliberately retain or add information such as:

- temporal edges or a trajectory graph connecting `w_i` to `w_(i+1)`;
- directed, zigzag, path-aware, or otherwise order-sensitive filtrations;
- a time/index coordinate appended to each window;
- marks such as `Z(g_n)`, derivative data, zero multiplicity, or another analytic field value;
- multiparameter filtrations carrying an independent parameter;
- window length or embedding dimension growing with the observation scale in a theorem that uses that growth materially.

Those are legitimate possible escapes, but the extra carrier must be named and audited rather than credited to ordinary delay-cloud persistence.

The finding also does not say that a fixed `m` delay cloud contains only one-gap information. For `m>=2` it can encode genuine local `m`-block correlations and therefore can be richer than `VIS-092`. The obstruction is specifically to **ordering beyond the unordered empirical window cloud** and, in particular, to orientation/time-arrow information.

Falsify the main claim by producing an ordinary Euclidean Rips or Cech persistence construction on a sliding-window point cloud whose persistence changes solely when the window indices are permuted while the metric cloud is kept fixed, or by showing that sequence reversal is not related to the original cloud by coordinate reversal. Either would contradict the defining metric-cloud construction directly.

## Visual consequence

No canonical PNG is retained. A delay-cloud rendering could be visually informative, but the result here is an exact pre-render information audit: any apparent loop, cluster, or torus in a fixed-window cloud must be interpreted as geometry of the unordered local window vectors unless the visualization/filtration explicitly preserves additional ordering information.

## Research consequence

`CLUE-zeta-critical-strip-multiscale-geometry` should treat ordinary fixed-window delay persistence as a **partially classified escape**. It escapes the scalar-line theorem `VIS-092` by supplying local multi-gap coordinates, but it does not by itself supply nonlocal sequence order or an orientation-sensitive channel.

A live topological route should therefore state which information it intends to add beyond the empirical fixed-`m` block cloud. Especially discriminating next possibilities are time-respecting/nonlocal edges, an independent analytic mark or field coordinate, a genuinely informative growing-window regime, or a filtration whose extra parameter cannot be reconstructed from the same local block multiset.