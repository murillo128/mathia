# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Test whether logarithmic rank-coupled coverage is minimal and survives the Hardy projection

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`, `MI-067-critical-hardy-zero-sampling-is-logarithmically-displaced-from-the-real-ford-axis`, `MI-068-a-critical-ford-notch-exports-the-scalar-carrier-into-a-depth-ladder`, `MI-069-near-full-positive-carriers-export-the-ford-obstruction-to-a-shrinking-boundary-layer`, `MI-070-a-cheap-signed-boundary-notch-exports-its-conditioning-into-a-ford-scale-side-lobe`, `MI-071-positive-depth-strip-suppression-is-noncoercive-with-unpriced-conditioning`, `MI-072-polynomial-rank-coupled-ford-coverage-recovers-the-euler-anchor`, `MI-073-nonquasianalytic-cutoffs-push-euler-anchor-recovery-through-any-fixed-iterated-log-loss`, `MI-074-rank-adaptive-compact-cutoffs-reach-the-logarithmic-ford-coverage-endpoint-in-aggregate`.

NB-261--NB-263 move the scalar problem to the shallow depth `u~log(J/K)` and expose a quantifier split: a strip chosen before the eventual rank can be flattened at vanishing resolved Hilbert cost when conditioning and later rank are free.

NB-264 couples coverage to rank and shows the opposite behavior under bounded resolved `ell^2` cost: exact reconstruction of the Euler anchor forces aggregate response `Omega(m)` throughout every fixed-power carrier radius `K^delta`. NB-265 sharpens this with a compact Gevrey plateau to every `O_epsilon((log K)^(1+epsilon))` radius, and NB-266 pushes through any fixed finite hierarchy of iterated-log losses using one fixed compact smooth cutoff.

NB-267 reaches the pure logarithmic endpoint for the aggregate quantity consumed by the matched Ford residue. The auxiliary cutoff is allowed to depend on rank: an `N_K asymp log K` finite box convolution has a sinc-power Fourier transform whose discrete tail beyond `O(log K)` is `o(K^(-1/2))`. Exact Euler reconstruction then forces

`sum_(|n Delta_m|<=C log K) |D_n| >= c m`.

This removes the iterated-log loss without contradicting compact-support Fourier barriers, because there is no single fixed cutoff with exponential decay; the finite smoothness order grows with `K`. The price is that the previous pointwise order-one lower bound is lost: the present argument yields only `sup |D_n| >= c/log K` from aggregate response.

The live scalar question is now whether **logarithmic coverage is minimal** under the declared bounded resolved-cost model, or whether a different exact certificate can force useful aggregate response on `o(log K)` radii. Any such refinement must price rank-dependent certificate complexity, dual variation/conditioning and the difference between aggregate and pointwise coercivity rather than hiding those resources in the cutoff choice.

The destination question remains independent and load-bearing: does the logarithmic aggregate obstruction survive the true Hardy/Nyman projection with the sign and norm needed for the actual criterion? Matched carrier-locked packets are still adversarial compatibility controls, not assertions about actual zero locations.

## Keep preassigned strips, rank-coupled coverage, certificate complexity and actual-zero claims distinct

NB-263 and NB-264--NB-267 are complementary. The former fixes the strip before rank and can export conditioning; the latter tie coverage to eventual rank and assume bounded resolved Hilbert cost. The known aggregate coercive radius now reaches `O(log K)`, but this does not establish a pointwise order-one obstruction or prove that logarithmic radius is sharp.

A future theorem must therefore state the order of quantifiers and every bounded resource. Growing coefficient norm, total variation, rank-adaptive cutoff order, dual reconstruction variation and final Hardy/Nyman distance remain separate from the resolved `ell^2` obstruction.