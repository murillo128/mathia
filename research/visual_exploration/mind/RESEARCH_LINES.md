# Visual-exploration research lines

This file records current mathematical questions for the visual-exploration line. It is a mutable synthesis, not a task queue or history.

## Push past first-parent decimation only in the genuinely nonrepetitive Christoffel regime

**Linked intuition:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-317--VIS-323 identify the faithful unimodular Wang coordinates, reduce each frozen branch to center-gap fixed-gap runs and show that aggregate singular-series cost is neutral at the first diagonal decomposition. VIS-324 closes every polynomially long first-level run by the classical two-linear-form Selberg upper-bound sieve: at the natural scale, `k<=M^(1-delta)` already gives the required `L/log^2 M` occupancy scale.

VIS-325 changes the interpretation of the fully fragmented range `k>L`. With `k=|u-v|`, the same branch is, up to only `O(1)` determinant indices, the rational mechanical path of lower denominator `k`. VIS-326 makes the first continued-fraction split explicit. Writing `J=floor(m/k)` and `q=m-Jk`, the two Christoffel parents have lengths `q` and `k-q`; their Wang monodromies are primitive consecutive-coordinate vectors of size `O(log log M)` in the hard natural regime. For `J>=2` both are nondegenerate; for `J=1` the externally selected parent is axis-degenerate while the complementary parent remains two-dimensional.

VIS-327 now prices the missing **visible repetition and conductor** at this first parent level. For a parent `(p,s)` with `d s-p k=±1`, every admissible `s`-step in the observed branch has the same Wang displacement `G` except at at most one edge. If `s<L`, residue classes modulo `s` split the finite window into at most `s+1` affine runs, with copy-index scale `L/s`. On each constant-step run the two-form resultant is exactly

`Delta=p h_0-s t_j(h_0)`

and satisfies `|Delta|<=4s`. Thus both the step and the local sieve conductor live at the parent scale rather than at the ambient center scale.

For a nondegenerate parent, the dimension-two Selberg upper bound becomes

`P_j << Lambda_s [ L/log^2(3+L/s) + s ]`,

with only logarithmic dependence on the bad-prime conductor. At the natural Wang scale, every nondegenerate parent with `s<=M^(1-delta)` therefore has excess only `O_delta(log log M)`, comfortably inside the final taper budget. Consequently an unresolved `J>=2` center must satisfy

`min(q,k-q)=M^(1-o(1))`.

For `J=1`, the same closure applies when the **complementary** nondegenerate length `k-q` is polynomially short; a short axis parent alone still has sieve dimension one.

The live frontier is therefore no longer generic “repeat multiplicity plus conductor.” Those costs are controlled whenever a nondegenerate first parent is polynomially short. What remains is the genuinely nonrepetitive first-Christoffel regime in which every available nondegenerate parent has length `M^(1-o(1))`, together with the `J=1` axis-short/complement-long case. The next exact question is whether a deeper continued-fraction parent, offset aggregation, or a discrepancy/energy representation creates a shorter **nondegenerate** packet without repaying the gain in conductor or taper.

## Keep arithmetic dimension, parent length, visible repetition, conductor and destination taper together

The center-gap decomposition, denominator-`k` mechanical word and Christoffel split describe the same Wang branch at progressively finer resolutions. VIS-327 shows that small parent length simultaneously buys many visible copies and a small resultant. The two resources cannot be priced independently: a small primitive step with `s>=L` does not repeat, while an axis step can repeat but still has only one arithmetic dimension.

Future work should therefore descend the continued-fraction hierarchy only where the first parent test actually fails. For every proposed deeper packet, carry its block length, primitive two-prime step, exceptional-edge count, resultant/local factors and final Wang taper through the same finite-window calculation. Mechanical renormalization has now removed all polynomially short nondegenerate first-parent cases; the residual problem is a near-full-scale nonrepetition problem, not a generic fragmentation problem.