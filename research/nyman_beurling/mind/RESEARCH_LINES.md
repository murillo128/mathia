# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Separate logarithmic aggregate coercivity from the actual Hardy quadratic bridge

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`, `MI-067-critical-hardy-zero-sampling-is-logarithmically-displaced-from-the-real-ford-axis`, `MI-068-a-critical-ford-notch-exports-the-scalar-carrier-into-a-depth-ladder`, `MI-069-near-full-positive-carriers-export-the-ford-obstruction-to-a-shrinking-boundary-layer`, `MI-070-a-cheap-signed-boundary-notch-exports-its-conditioning-into-a-ford-scale-side-lobe`, `MI-071-positive-depth-strip-suppression-is-noncoercive-with-unpriced-conditioning`, `MI-072-polynomial-rank-coupled-ford-coverage-recovers-the-euler-anchor`, `MI-073-nonquasianalytic-cutoffs-push-euler-anchor-recovery-through-any-fixed-iterated-log-loss`, `MI-074-rank-adaptive-compact-cutoffs-reach-the-logarithmic-ford-coverage-endpoint-in-aggregate`, `MI-075-logarithmic-ford-mesh-mass-does-not-force-diagonal-quadratic-energy`, `MI-076-resolved-center-spikes-force-rank-growing-destination-strength`, `MI-077-target-pairings-change-mismatch-not-source-gram-strength`.

NB-264--NB-267 force `Omega(m)` aggregate mesh response down to `O(log K)` rank-coupled coverage under bounded resolved cost. NB-268 then shows that this linear aggregate obstruction does not force diagonal quadratic energy: the legal uniform carrier keeps the aggregate mass while its damped diagonal diagnostic vanishes.

NB-269 resolves the actual Hardy-projected multi-shell diagnostic for the explicit matched packet. The resolved shell bands are disjoint after projection, so full-line Plancherel diagonalizes the shell index exactly. For the uniform positive carrier `c_j=1/K`, the projected energy is `Theta(1/K)` even though the center value remains order one on a spike of width `Theta(1/K)`. Thus the hard-window quadratic form itself can vanish; generic off-diagonal shell terms do not rescue this carrier.

NB-270 classifies every positive band-diagonal repair. If shell `j` is charged by `q_j`, the Euler anchor `sum c_j=1` has a rank-uniform quadratic floor exactly when `sum_j q_j^(-1)` remains bounded. Sobolev weights have the sharp threshold `s>1/2`; the critical `s=1/2` endpoint still leaks as `1/log K`, with the exact logarithmic refinement determined by reciprocal summability. The ordinary Hardy norm is the leaking `s=0` case.

NB-271 removes the generic off-diagonal loophole at the same abstraction level. For a positive Gram matrix `A_K`, the optimal anchored energy is `1/(1^* A_K^dagger 1)` when the anchor lies in the range, and zero if an anchor-visible null direction exists. Testing the uniform anchored vector shows that any rank-uniform positive floor requires operator strength at least `Theta(K)` relative to the canonical resolved Hardy norm. Uniformly bounded, finite-band or summably decaying positive corrections therefore cannot repair the leak.

NB-272 sharpens the remaining target-sensitive loophole by an exact finite-section identity. For source Gram `R_K=S_K^*S_K`, target pairing `b_K=S_K^*g`, and Euler anchor `e_K^*c=1`, the constrained residual splits into

`delta_K^2 + |mu_K|^2/(e_K^*R_K^(-1)e_K)`,

where `delta_K=dist(g,ran S_K)` and `mu_K=1-e_K^*R_K^(-1)b_K`. The target cross term changes the unconstrained projection and anchor mismatch but does not modify the source-source Hessian `R_K`; it cannot itself be the `Theta(K)` positive Gram repair sought after NB-271. In the resolved regime `R_K asymp I`, the mismatch penalty is `Theta(|mu_K|^2/K)`, so only a nonvanishing section defect, a `sqrt(K)`-scale anchor mismatch, or genuinely new source-source quadratic geometry can provide an order-one target-side obstruction.

The live destination question is therefore a concrete fork. Estimate the actual canonical-target quantities `delta_K` and `mu_K` in the same rank-coupled resolved regime, or identify the smallest exact source component outside the NB-269 channel whose relative Gram has `Omega(K)` strength and passes the inverse-Gram anchor test. Merely invoking target cross terms, generic off-diagonal coherence, diagonal reweighting or local/summable corrections is closed at this abstraction level.

The separate source-side question of whether `O(log K)` aggregate coverage is minimal remains open, but improving that radius cannot by itself overcome the destination leak. Aggregate response, projected Hardy energy, target projection defect, anchor mismatch, inverse-Gram conditioning and the full Nyman norm are distinct currencies.

## Keep preassigned strips, rank-coupled coverage, certificate complexity and target norm distinct

A future theorem must state the order of quantifiers and every bounded resource. NB-269--NB-272 show that an order-one point residue can be hidden in a shrinking width while every positive quadratic observable continuously dominated by the resolved `H^2` channel pays the rank leak, and that the ordinary target pairing does not secretly alter the source Gram. A successful target mechanism must therefore locate either a genuine target mismatch that survives at order one or a new source-source component with the necessary rank-growing strength, rather than infer coercivity from aggregate source response or unspecified target-sensitive structure.
