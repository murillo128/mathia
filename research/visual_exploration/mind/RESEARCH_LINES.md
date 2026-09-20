# Visual-exploration research lines

This file records current mathematical questions for the visual-exploration line. It is a mutable synthesis, not a task queue or history.

## Quantify visible Christoffel-parent repetition after the first Wang renormalization

**Linked intuition:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-317--VIS-323 identify the faithful unimodular Wang coordinates, reduce each frozen branch to center-gap fixed-gap runs and show that aggregate singular-series cost is neutral at the first diagonal decomposition. VIS-324 closes every polynomially long first-level run by the classical two-linear-form Selberg upper-bound sieve: at the natural scale, `k<=M^(1-delta)` already gives the required `L/log^2 M` occupancy scale.

VIS-325 changes the interpretation of the fully fragmented range `k>L`. With `k=|u-v|`, the same branch is, up to only `O(1)` determinant indices, the rational mechanical path of lower denominator `k` and slope `d/k`, where `|dm-ck|=1`. Its exact period monodromy is `(sigma,sigma)`. Thus singleton fragmentation is a failure of the first diagonal period representation, not evidence that the path has no deeper repeated structure.

VIS-326 makes the first continued-fraction step explicit. Writing `J=floor(m/k)` and `q=m-Jk`, the Farey neighbour selected by the larger denominator gives a Christoffel parent of length `q`; the complementary parent has length `k-q`. Their lattice monodromies have consecutive integer coordinates and depend only on `J` and orientation: for `v>u` they are `(1-J,-J)` and `(J,J+1)`, with the sign-reversed analogue when `u>v`. In the hard natural regime `k>L asymp M/log log M`, these primitive step vectors are only `O(log log M)`.

There is one exact first-parent degeneracy. `J=1` iff `m>2n`; then the externally selected parent has axis monodromy `(0,-1)` or `(1,0)`, so copy-index sieving has only one varying prime coordinate. The complementary parent remains nondegenerate. For `J>=2`, both parent vectors have two nonzero coprime coordinates, removing the common-step obstruction to a two-affine-form sieve.

The live theorem is now quantitative rather than representational: determine how many useful copies of one parent block are actually visible inside the observed subperiod segment, with the relevant cyclic conjugacy, and control the resultants/local factors across internal offsets. If `J>=2` supplies enough repeats, the first parent split can feed the ordinary two-prime sieve with small primitive steps. If `J=1`, use the complementary parent, average over offsets to recover the second arithmetic dimension, or move to a later continued-fraction/energy representation. Cross-fragment aggregation should be invoked only after these exact renormalized alternatives are priced.

## Keep arithmetic dimension, center gap, representation denominator, parent repetition and destination taper together

The center-gap decomposition, denominator-`k` mechanical word and first Christoffel split describe the same Wang branch at progressively finer resolutions. VIS-326 shows that small primitive block monodromy is guaranteed, but repetition is not. A short step vector without enough visible copies gives no occupancy gain; a repeated axis block has only sieve dimension one; and a repeated nondegenerate block still carries offset-dependent resultants/local factors.

Future work must therefore preserve the two-prime local factor and final Wang taper while quantifying the continued-fraction packet actually seen by the finite window. Mechanical renormalization has removed the false “singleton means structureless” obstruction. The remaining price is visible repetition plus arithmetic conductor control, or a different discrepancy/energy mechanism in the regime where that repetition is absent.