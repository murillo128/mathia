# MI-001 — Nyman geometry is target-aware and remembers absolute multiplicative scale

**Evidence level:** exact finite augmented-Gram and canonical semigroup-copy results through NB-002

## Core intuition

The Nyman approximation problem is not determined by the geometry of the generators among themselves. The fixed target supplies a separate coordinate, and canonical multiplicative self-similarity can preserve every generator inner product while continuously losing relevance to that target.

## Strongest justified principle

NB-001 gives the exact finite formula `d_N^2=1-b_N^*G_N^+b_N` and constructs Gram-preserving controls with different target distances. NB-002 shows the same phenomenon inside the canonical Nyman semigroup: a scale-`m` copy has the identical Gram block but target projection energy exactly divided by `m`.

## Program consequence

Any multiscale compression must transport the target-pairing vector or an equivalent augmented-Gram/dual datum together with the local block. Absolute scale is load-bearing. A promising theorem would control how target projection energy accumulates across canonical scales despite local self-similarity and conditioning.

## Counterevidence / boundary

These results do not bound the actual canonical distance `d_N` asymptotically and do not show that cross-scale interactions cannot recover the missing global target mass.

## Epistemic status

**Exact finite and semigroup information boundary; no new Nyman approximation rate or RH consequence is established.**

## Falsification criterion

Find two finite Nyman configurations with the same augmented Gram data but different target distance, or a canonical semigroup copy violating the `m^{-1/2}` target-pairing law. A positive continuation should prove a target-aware cross-scale estimate rather than a Gram-only one.