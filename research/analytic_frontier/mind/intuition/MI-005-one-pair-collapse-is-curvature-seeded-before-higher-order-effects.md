# MI-005 — The scalar pair frontier is nonseparable center-height geometry, not multiplicity or height alone

**Evidence level:** proved for the declared central-notch model by exact derived certificates through ANF-085

## Core intuition

The fixed central-notch strategy now controls much more than the real boundary. ANF-081 closes every finite real multiset, ANF-083 gives one fixed complex height strip independent of pair count, and ANF-085 proves all-height safety whenever the center-height occupation is separable. The first surviving scalar obstruction is therefore not large multiplicity, many conjugate pairs, or large height by itself. It is **nonseparable correlation between horizontal center and vertical profile** outside the protected strip.

This materially changes the complexity question. The `p^{-1/4}` tube from ANF-082 was a phase-blind proof loss, not a genuine pair-count barrier, and even arbitrarily high vertical profiles remain harmless when their occupation matrix has rank one after zero rows/columns are removed.

## Strongest justified principle

ANF-081 uses two-level clipping plus the exact affine surplus to obtain one certificate uniform over all finite real supports and integer multiplicities. ANF-083 replaces the coherent pairwise triangle loss of ANF-082 by an entrywise-positive kernel domination argument, producing constants `h_*>0` and a strict normalization margin independent of the number and arrangement of nonreal pairs.

ANF-085 exploits factorization of a separable center-height occupation. The vertical profile contributes one common positive factor while the horizontal amplitudes inherit the already controlled affine certificate. Consequently proportional vertical fibers are safe at every height, including configurations far outside the fixed strip.

The durable boundary is therefore: **a counterexample to this pair-energy certificate must simultaneously leave the fixed positive tube and carry genuinely non-product center-height structure.** Any proposed scalar complexity measure that counts pairs, multiplicity, or maximum height without detecting this coupling is already falsified by the exact controls.

## Counterevidence / boundary

ANF-083 relies on the special entrywise-nonnegative Montgomery--Taylor kernel; positive semidefiniteness alone does not imply the same domination. ANF-085 covers separable occupation, not arbitrary low-rank perturbations or mixtures of several vertical profiles. Neither theorem proves that a nonseparable high configuration actually defeats the certificate.

The next useful theorem may therefore be positive: control a neighborhood of the separable cone, perhaps in an explicitly normalized rank-defect or projective metric, rather than search immediately for a higher-order obstruction.

## Epistemic status

**Proved for the stated model.** The frontier relocation is a direct synthesis of exact findings; no RH consequence or external novelty claim is asserted.

## Falsification criterion

Produce a finite configuration violating ANF-081, a conjugation-invariant configuration inside the uniform ANF-083 strip that violates its certificate, or a separable all-height center-profile configuration violating ANF-085. Any such example reopens the corresponding earlier boundary.