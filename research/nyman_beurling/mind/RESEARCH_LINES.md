# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Locate the logarithmic rank-coupled shallow-coverage threshold

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`, `MI-067-critical-hardy-zero-sampling-is-logarithmically-displaced-from-the-real-ford-axis`, `MI-068-a-critical-ford-notch-exports-the-scalar-carrier-into-a-depth-ladder`, `MI-069-near-full-positive-carriers-export-the-ford-obstruction-to-a-shrinking-boundary-layer`, `MI-070-a-cheap-signed-boundary-notch-exports-its-conditioning-into-a-ford-scale-side-lobe`, `MI-071-positive-depth-strip-suppression-is-noncoercive-with-unpriced-conditioning`, `MI-072-polynomial-rank-coupled-ford-coverage-recovers-the-euler-anchor`, `MI-073-nonquasianalytic-cutoffs-push-euler-anchor-recovery-through-any-fixed-iterated-log-loss`.

NB-261--NB-263 move the scalar problem to the shallow depth `u~log(J/K)` and expose a quantifier split: a strip chosen before the eventual rank can be flattened at vanishing resolved Hilbert cost when conditioning and later rank are free.

NB-264 couples coverage to rank and shows the opposite behavior under bounded resolved `ell^2` cost: exact reconstruction of the Euler anchor forces aggregate response `Omega(m)` throughout every fixed-power carrier radius `K^delta`. NB-265 sharpens this with a compact Gevrey plateau to every `O_epsilon((log K)^(1+epsilon))` radius.

NB-266 pushes the same exact reconstruction through any fixed finite hierarchy of iterated-log losses. For fixed `r` and `epsilon>0`, an explicit compact `C^infinity` plateau gives coercivity by

`B_K = C_(r,epsilon) log K L_(r,epsilon)(log K)`,

where `L_(r,epsilon)` is the corresponding product of iterated logarithms ending in exponent `1+epsilon`. In particular `B_K=o((log K)^(1+delta))` for every fixed `delta>0`, while the required aggregate `Omega(m)` response and the local Ford-shell placement are preserved.

The live scalar question is now the endpoint itself: can bounded-cost suppression persist on `B_K=O(log K)`, or does another exact reconstruction/duality argument force coercivity there? The current infinite-convolution construction does not prove the endpoint and does not establish that an iterated-log loss is necessary. Any sharper theorem must preserve the Euler normalization and then survive the true Hardy/Nyman projection rather than only matched compatibility controls.

## Keep preassigned strips, rank-coupled coverage, conditioning and actual-zero claims distinct

NB-263 and NB-264--NB-266 are complementary. The former fixes the strip before rank and can export conditioning; the latter tie coverage to eventual rank and assume bounded resolved Hilbert cost. The known coercive radius has now been pushed below every fixed superlogarithmic power, but not to a pure logarithm.

A future theorem must therefore state the order of quantifiers and the bounded resource. Matched carrier-locked packets remain adversarial controls, not assertions about actual zero locations. Growing coefficient norm, total variation, reconstruction conditioning and final Hardy/Nyman distance remain separate from the resolved `ell^2` obstruction.