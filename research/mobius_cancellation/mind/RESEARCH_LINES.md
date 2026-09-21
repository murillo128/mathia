# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Price factor-lift information after source projection and Möbius interaction extraction

**Linked intuitions:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`, `MI-074-thin-hyperbolic-shells-tax-independent-coordinate-bandwidth`, `MI-075-exact-product-tangent-fibers-have-subpolynomial-state-volume`, `MI-076-fixed-depth-factor-lifts-cannot-amplify-the-short-shell-state-exponent`, `MI-077-factor-multiplicity-does-not-survive-a-mobius-sign-projection`, `MI-078-unbounded-additive-factor-data-buys-state-capacity-only-through-retained-precision`, `MI-079-permutation-invariant-factor-size-needs-inverse-logarithmic-precision-for-polynomial-state-capacity`, `MI-080-fixed-dimensional-symmetric-factor-data-obeys-a-dimension-precision-law`, `MI-081-exact-factor-identity-has-near-linear-orbit-capacity-but-mobius-sign-erases-it`, `MI-082-prime-mark-entropy-controls-factor-quotient-capacity`, `MI-083-sparse-relational-asymmetry-can-preserve-the-full-factor-state-exponent`, `MI-084-global-ordinal-prime-relations-can-saturate-source-capacity-only-by-paying-identity-scale-information`, `MI-085-mobius-divisor-convolution-sees-only-the-full-prime-interaction`, `MI-086-additive-consecutive-chain-statistics-lose-every-interior-motif-under-mobius-projection`.

MC-423--MC-435 show that tangent dimension, factor multiplicity and bounded/local factor decorations do not provide polynomial conditional source diversity unless their retained information budget reaches the `Theta(r log r)` scale of prime identity. MC-436 shows that this threshold is attainable as a representation budget: the global ordinal pattern of adjacent selected-prime gaps realizes all `(r-1)! = N_r^(1-o(1))` types.

MC-437 adds the downstream survival gate. For a squarefree source `n=p_1...p_r`, a divisor statistic `F_n(T)` passes through arithmetic Möbius convolution only through its top Boolean coefficient

`I_F(n)=sum_(T subset [r]) (-1)^(r-|T|) F_n(T)`.

Every bounded-order interaction expansion is annihilated once `r` exceeds its interaction degree, even if the representation is injective on all `2^r` divisor states. Raw source diversity, representation fidelity and Möbius interaction depth are therefore independent resources.

MC-438 closes the most immediate adjacency-dependent loophole. If a divisor statistic is a sum of a fixed kernel over consecutive `k`-blocks of the selected prime chain, then its full interaction keeps only blocks spanning both global endpoint primes. For `k=2` the entire statistic collapses to the single endpoint term `(-1)^(r-2)W(p_1,p_r)`. Selection-dependent adjacency can generate high Boolean degree, but additive local chain structure still loses every interior motif under the Möbius projection.

The live gap-order branch should therefore no longer spend effort on fixed-size additive consecutive-block scores. The next exact object must be a genuinely global nonadditive functional of the induced gap-order permutation, a rank/context-dependent statistic whose full interaction is explicitly derived, or a growing-depth construction. Compute or sharply constrain its `I_G(n)` on every divisor subset first; only if that survives should source-height realization and signed analytic control be investigated. A factorial full-set alphabet still gives no lower bound on the top interaction.

## Separate description sparsity, quotient entropy, source diversity, interaction depth and analytic usefulness

A small alphabet is meaningful only after the actual quotient is specified. Sparse incidence can rigidify every coordinate; a universal rigid scaffold can still carry zero source diversity; bounded local decorations can carry too little conditional variation; a global ordinal relation can recover factorial variation only by paying `Theta(r log r)` information; and Möbius divisor convolution can erase all of that information if it lives below full prime interaction order or, by MC-438, if its apparent high interaction is only the inclusion-exclusion shadow of additive local adjacency.

The surviving relational escape is therefore not “use gaps” or “use a canonical order” in the abstract. It is a source-forced relation with an explicitly priced type budget and realization scale whose induced divisor statistic has a nontrivial full-order coefficient not reducible to boundary-only motifs, followed by an analytic estimate that turns that coefficient into cancellation. A different downstream operation remains possible, but then its own information-loss map must be identified explicitly.