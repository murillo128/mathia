# MI-004 — Complete scalar control is a finite-configuration and diffraction-realizability problem

**Evidence level:** supported by ANF-018--ANF-021; the stability and convex-duality reductions are exact, while the random-matrix exclusions are literature-backed specializations

## Core intuition

For the universal affine support-one scalar carrier, the decisive adversary is not one periodic lattice, one thermodynamic density, or the local slope of a structure factor. The complete control is the whole family of finite real configurations, equivalently its weak-* convex diffraction body on the supported frequency band.

A candidate scalar gain is meaningful only if it survives both **finite binding** and **full-band realizability**. Local hyperuniformity, a favorable small-frequency cusp, or success on a fixed-density bulk can all coexist with a finite or intermediate-frequency obstruction that restores the Montgomery--Taylor ceiling.

## Strongest justified principle

ANF-018 identifies the exact finite-real floor `q_real(J)` with the classical stability constant of the pair potential `F=widehat J`. ANF-019 shows that this is genuinely a large-particle free-density problem: any finite bound cluster can be copied far apart, so its per-particle gain survives at arbitrarily large particle number. Fixed-density thermodynamic optimality therefore cannot replace the complete finite-configuration test.

ANF-020 dualizes the remaining scalar ceiling. The statement `q_real(J)<=C(J)/C_MT` for every admissible nonnegative band profile is equivalent to existence of one measure in the weak-* closed convex hull of finite diffraction measures dominated by the Montgomery--Taylor budget. This converts the profile-by-profile problem into one exact realizability/separation question. Stationary translation-invariant determinantal processes cannot realize the required strict contraction; the sine process saturates the endpoint.

ANF-021 closes a more subtle local escape. The symplectic/Pfaffian bulk has a small-frequency cusp compatible with the required local slope, but neither it nor convex scale mixtures satisfy the complete support-one domination. The obstruction appears at finite nonzero frequency. Thus the whole band, not only the origin, is load-bearing.

## What remains possible

A scalar survivor must either construct a genuinely admissible diffraction measure inside the Montgomery--Taylor budget or produce an admissible spectrum separating the complete finite-configuration body from that budget. A different non-scalar carrier may evade this scalar convex body, but then it must retain information that does not dualize back to the same signed profile.

## Status / novelty

Stability, Fekete subadditivity, diffraction, convex separation, determinantal/Pfaffian point processes, and hyperuniformity are classical. The Mathia synthesis is the completed control boundary: **finite clusters and full-band realizability are the exact scalar tests; local or thermodynamic success is insufficient**.

## Falsification criterion

Produce an admissible scalar profile whose complete finite-real floor beats the Montgomery--Taylor threshold, or construct a measure in the finite-configuration diffraction body dominated by the target budget. Conversely, any proposed bulk/RMT witness is insufficient unless its complete band domination is proved.

## Lean-formalizable core

- Subadditivity and free-density amplification of finite binding.
- Convex separation equivalence for the diffraction body.
- Logical distinction between local cusp control and full-band domination.
