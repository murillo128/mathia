# MI-004 — Pointed positivity recovers the finite Weil coefficient, but support selection and archimedean coupling still break the sign

**Evidence level:** supported by exact positive constructions, Möbius extraction, and exact semigroup/globalization obstructions

## Core intuition

The finite arithmetic package is now stronger than merely having a bounded Mangoldt anchor. In the pointed local Dirichlet geometry, intrinsic covers force the critical half-weight, a positive trace-class cocycle supplies `log n`, and Möbius extraction gives the exact scalar coefficient `Lambda(n)/sqrt(n)`. The obstruction has moved to the operation that selects prime-power support and couples it to the archimedean Weil term: that operation leaves the positive cone or collapses to a separable/coboundary structure.

## Strongest justified principle

WP-067--WP-071 identify the original topology obstruction: the exact shell anchor is unbounded in the natural rotation-invariant Hardy energy, and positive rotation-invariant repairs do not fix it. WP-072--WP-074 give the canonical positive escape. The base-point local Dirichlet form contains every shell, makes evaluation at `1` bounded, forces the unique isometric normalization `n^{-1/2}` under degree-`n` covers, and produces positive trace-class inverse-scale defects `Q_n` with `Tr Q_n=log n`.

WP-075--WP-076 close the direct archimedean shift escape. Positive shifted-resolvent defects contain a digamma correction, but under multiplicative composition they form an exact positive semigroup cocycle and the entire digamma term is the scalar coboundary `F(c/n)-F(c)`. It telescopes to endpoint data and creates no irreducible cross-prime coupling. Exact finite `log n` weights remain the zero-shift endpoint of this separated family.

WP-077 classifies the most canonical positive globalization by averaging the same pointed fibers over boundary basepoints while preserving every root cover. The only invariant probability measures are `a delta_1+(1-a) Haar`. The pointed branch is the existing construction; the Haar branch is the classical Dirichlet form and kills the cover resolvent defects and bounded anchor. Positive semigroup-compatible averaging therefore supplies no third mechanism.

WP-078 nevertheless sharpens the finite arithmetic result. The divisor-Möbius primitive

`M_n = sum_{d|n} mu(d) Q_{n/d}`

has `Tr M_n=Lambda(n)`. On every prime power `p^k`, `M_{p^k}` is itself positive and is just a transported copy of the one-step prime defect. On integers with at least two distinct prime factors, `M_n` is nonzero trace-zero and indefinite. Multiplying the trace by the cover overlap gives the exact finite scalar `Lambda(n)/sqrt(n)`, but the support-selecting Möbius operation is precisely where positivity fails off the prime-power rays.

Thus positivity does not fail to carry arithmetic. It fails to turn the exact finite selector into one completed positive Weil sign without an independently justified operation that handles mixed-prime cancellation and the archimedean term simultaneously.

## What remains possible

A genuinely nonseparable finite--archimedean form, higher cohomological construction, twisted family/boundary geometry, or singular pairing could couple the prime-power selector before it is reduced to scalar Möbius cancellation or a separated shifted resolvent. Any such mechanism must retain the pointed continuity and exact half-weight/log-degree package while proving its sign independently.

## Status / novelty

Local Dirichlet positivity, composition scaling, Jensen/resolvent positivity, semigroup cocycles, Möbius inversion, and invariant-measure arguments use classical ingredients. Their exact specialization to the Mathia cover data and the positive-on-prime-powers/indefinite-off-prime-powers split are persisted evidence. This is not a Weil-positivity proof.

## Falsification criterion

Construct within the audited pointed-cover family a positive Möbius primitive on every integer while retaining `Tr M_n=Lambda(n)`, contradicting WP-078, or a semigroup-compatible positive basepoint average outside the pointed-plus-Haar classification of WP-077. A positive advance should instead derive a new nonseparable completion outside those closed families.

## Lean-formalizable core

- Cover-cocycle identity and digamma coboundary telescoping.
- Invariant-measure classification under all power maps.
- Möbius primitive trace identity.
- Positivity on prime powers and trace-zero indefiniteness off them.
