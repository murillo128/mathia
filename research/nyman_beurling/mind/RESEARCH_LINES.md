# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Build target-aware multiscale control rather than Gram-only compression

**Linked intuition:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`.

NB-001 proves that the complete finite generator Gram matrix does not determine distance to the fixed Nyman target; the missing datum is the target-pairing vector, and the exact finite residual is the augmented-Gram Schur complement `1-b^*G^+b`. NB-002 makes the loss internal to the canonical family: multiplicative semigroup copies preserve the entire local Gram block while attenuating every global target pairing by `m^{-1/2}` and projection energy by `1/m`.

The live finite-to-infinite route must therefore track **where target mass sits across absolute multiplicative scale**, not merely whether local blocks are well conditioned or self-similar. Seek a multiscale decomposition or dual certificate that controls the augmented Gram data and the accumulation of target projection energy as the canonical span grows.

## Separate local approximation quality from global target capture

A high-scale canonical block approximates its normalized local target with exactly the same error as the base block while becoming nearly orthogonal to the fixed global target. Local self-similarity is therefore not evidence of global Nyman convergence.

A useful asymptotic theorem must quantify target-weighted near-null modes, cross-scale interactions, or a normed dual witness. Gram spectra, determinants, and condition numbers without transported target pairings are controls.