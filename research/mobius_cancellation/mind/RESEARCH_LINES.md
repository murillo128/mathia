# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Price factor-lift information after source projection and symmetry quotient

**Linked intuitions:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`, `MI-074-thin-hyperbolic-shells-tax-independent-coordinate-bandwidth`, `MI-075-exact-product-tangent-fibers-have-subpolynomial-state-volume`, `MI-076-fixed-depth-factor-lifts-cannot-amplify-the-short-shell-state-exponent`, `MI-077-factor-multiplicity-does-not-survive-a-mobius-sign-projection`, `MI-078-unbounded-additive-factor-data-buys-state-capacity-only-through-retained-precision`, `MI-079-permutation-invariant-factor-size-needs-inverse-logarithmic-precision-for-polynomial-state-capacity`, `MI-080-fixed-dimensional-symmetric-factor-data-obeys-a-dimension-precision-law`, `MI-081-exact-factor-identity-has-near-linear-orbit-capacity-but-mobius-sign-erases-it`, `MI-082-prime-mark-entropy-controls-factor-quotient-capacity`, `MI-083-sparse-relational-asymmetry-can-preserve-the-full-factor-state-exponent`.

MC-423--MC-430 show that tangent dimension, factor multiplicity and fixed-dimensional additive summaries cannot manufacture polynomial state capacity without paying retained precision, while full labelled prime-block incidence has Bell-number capacity `N_r^(1-o(1))` along primorials.

MC-431--MC-432 price finite-type color quotients by the multinomial distinguishability budget `D=log(r!/prod_a r_a!)`. MC-433 shows that this color law cannot be extrapolated to arbitrary sparse relations: if a retained relation `R` has automorphism group `G`, then `Q_R>=B_r/|G|`, and `log|G|=o(r log r)` already guarantees near-full primorial-scale Bell capacity. A bounded-degree tree with only `r-1` edges can be rigid and preserve every factor state.

The live capacity audit is therefore **symmetry of the actual surviving datum**, not relation count or local degree. For a proposed relational lift, compute or bound `Aut(R_surv)` after the coefficient/source map. If the symmetry-breaking budget `log(r!/|Aut(R_surv)|)` is a positive fraction of `r log r`, the construction has escaped the state-count obstruction even when its relation is sparse.

That escape is not yet analytic progress. The remaining question is whether the symmetry breaking is canonically forced by arithmetic rather than an externally chosen encoding of prime identity, and whether it survives Möbius-facing projection as a signed cancellation mechanism rather than merely a decoder.

## Separate description sparsity, quotient entropy and analytic usefulness

A small alphabet is meaningful for color quotients because the quotient action is explicit. A sparse general relation can still individualize every prime coordinate; edge count, bounded degree and finite relation type therefore do not price information without an invariance/generation constraint.

The correct ledger now separates: retained coordinate precision, factor-state orbit count, automorphism/symmetry-breaking budget, canonical arithmetic provenance, and the datum actually consumed after projection. Passing the automorphism test certifies only representation capacity. A viable route must then show that the same relational asymmetry is source-native and contributes to the destination sign/cancellation estimate.