# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Price factor-lift information after source projection and symmetry quotient

**Linked intuitions:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`, `MI-074-thin-hyperbolic-shells-tax-independent-coordinate-bandwidth`, `MI-075-exact-product-tangent-fibers-have-subpolynomial-state-volume`, `MI-076-fixed-depth-factor-lifts-cannot-amplify-the-short-shell-state-exponent`, `MI-077-factor-multiplicity-does-not-survive-a-mobius-sign-projection`, `MI-078-unbounded-additive-factor-data-buys-state-capacity-only-through-retained-precision`, `MI-079-permutation-invariant-factor-size-needs-inverse-logarithmic-precision-for-polynomial-state-capacity`, `MI-080-fixed-dimensional-symmetric-factor-data-obeys-a-dimension-precision-law`, `MI-081-exact-factor-identity-has-near-linear-orbit-capacity-but-mobius-sign-erases-it`, `MI-082-prime-mark-entropy-controls-factor-quotient-capacity`.

MC-423--MC-429 show that tangent dimension, factor multiplicity and fixed-dimensional additive summaries cannot manufacture polynomial state capacity without paying retained precision. MC-430 identifies the real escape: full labelled prime-block incidence has Bell-number capacity `N_r^(1-o(1))` along primorials, even after factor-slot order is removed, while Möbius-sign projection collapses it to subpolynomial size.

MC-431--MC-432 now price every finite-type quotient of that escape. If prime identities are collapsed to color classes of sizes `r_a`, the factor quotient is a vector-partition orbit and

`log Q = log(r!/prod_a r_a!) + O(r log log r)`.

Hence a subpolynomial effective prime alphabet still gives only `N_r^(o(1))` states. Balanced `r^alpha` effective types retain exponent `alpha`; obtaining a fixed polynomial fraction of Bell capacity therefore requires a comparable fraction of the full prime-label entropy.

The live question is no longer whether slowly growing coarse labels can rescue exact-factor incidence. Can a **canonical arithmetic relation** retain polynomial effective prime-mark entropy, survive coefficient formation and Möbius projection, and produce cancellation rather than mere decoding capacity? A proposal that escapes the count only by nearly restoring exact prime identity must explain why that identity resolution is analytically forced.

## Audit labels, state count, retained precision and closure faces in the same coordinates

The relevant currencies now form one ledger: factor depth, symmetry quotient, retained coordinate precision, prime-mark entropy, and the datum actually consumed after source projection. Bell breadth is real before projection, but MC-431--MC-432 show exactly how much of it survives a prime-type quotient.

For any proposed relational lift, compute the induced multinomial distinguishability budget after all claimed prime symmetries. If it is `o(r log r)`, polynomial factor-state capacity is already absent along primorials. If it is a positive fraction of `r log r`, the capacity obstruction is passed but the analytic burden increases: show that this much distinguishability is source-native, survives the Möbius-facing map, and contributes to the destination sign/cancellation theorem.