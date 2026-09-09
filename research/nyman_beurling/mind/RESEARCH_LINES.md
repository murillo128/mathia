# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Build target-aware multiscale control with a growing anti-aliasing budget

**Linked intuition:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`.

NB-001 proves that the complete finite generator Gram matrix does not determine distance to the fixed Nyman target; the missing datum is the target-pairing vector, and the exact finite residual is the augmented-Gram Schur complement. NB-002 makes the loss internal to the canonical family: multiplicative semigroup copies preserve the entire local Gram block while attenuating every global target pairing by `m^{-1/2}` and projection energy by `1/m`.

NB-004--NB-006 now close the obvious finite-probe replacement for those pairings. Every fixed finite family of Bagchi adjoint-semigroup target-character tests admits target-orthogonal approximate Mellin aliases. The full integer semigroup identifies the target exactly, but remains noncoercive in every natural summable `ell^p`, `p>2`, defect norm. Even at the nonsummable harmonic boundary, the first `M` scales admit explicit aliases whose recurrence dimension is only `pi(M)`, forcing a quantitative scale-versus-Mellin-bandwidth problem and a superlogarithmic probe pressure against this witness family.

The live route must therefore track **where target mass sits across absolute multiplicative scale** with a scale family or norm strong enough to defeat Mellin aliasing on the source class actually produced by Nyman approximation. Exact character identification, finitely many covariance defects, or summable aggregation are not quantitative target certificates.

## Separate local approximation quality, exact target character, and global target capture

A high-scale canonical block can approximate its normalized local target exactly as well as the base block while becoming nearly orthogonal to the fixed global target. Likewise, a family of vectors may satisfy many target-character covariance tests almost perfectly while remaining exactly target-orthogonal.

A useful asymptotic theorem must control augmented target data, growing-scale anti-aliasing, or a normed dual witness tied to the actual residual. Gram spectra, fixed semigroup probes, and exact-but-noncoercive character identities are controls.