# Weil-positivity geometry research notes

This directory preserves high-signal evidence from the **Mathia global Weil-positivity** research line.

The central question is:

> **Does Mathia contain, or can its intrinsic constructions force, a geometric structure whose own positivity yields a global Weil-type positivity statement, rather than merely producing another zeta function, spectrum, determinant, or representation of already-known zero data?**

The target is not a new coordinate system for the Riemann hypothesis. The research object is a candidate **Mathia-native geometric pairing, energy, intersection form, norm, or operator-positive form** whose local-to-global decomposition can be matched rigorously to the arithmetic/archimedean structure of a Weil explicit-formula positivity criterion, while its nonnegativity comes from the geometry itself.

## Research stance

The classical Weil positivity criterion, the Riemann explicit formula, Hilbert–Pólya-style spectral reformulations, the function-field Frobenius/cohomology proof architecture, Connes-style trace programs, and existing local/operator positivity mechanisms are **prior art and calibration constraints**, not Mathia discoveries.

A durable result in this branch must do at least one of the following:

- derive a canonical positive or indefinite form directly from a Mathia construction and identify exactly what arithmetic information it retains;
- obtain a genuine local-to-global decomposition and compare its terms with the finite-prime and archimedean pieces of the explicit formula under an audited normalization;
- show that a known Mathia geometry forces a positivity mechanism analogous in role—not merely in vocabulary—to the geometric positivity used in proved function-field RH;
- establish an obstruction showing that a natural Mathia construction can only re-encode zeta, its zeros, a spectrum, or a known positivity criterion without explaining the sign;
- identify the extra intrinsic structure required to turn one of Mathia's surviving geometric mechanisms into a non-circular positivity argument.

The branch must aggressively distinguish **positivity that is proved from independent geometry** from positivity that is equivalent to RH only because the zeta zeros or explicit formula were inserted by construction.

## Primary audit questions

For every candidate, make the following questions explicit.

1. **What is the geometric object?** Define the space, pairing, energy, intersection form, operator, boundary response, or cohomological object without referring to the desired conclusion.
2. **Why is it canonical?** Remove arbitrary gauges, coordinates, regularizations, basis choices, or hand-picked kernels unless the Mathia construction forces them.
3. **Where does positivity come from?** It should follow from a geometric theorem or structural property such as a norm square, intersection/Hodge-type sign rule, reflection/energy principle, compression of a positive operator, or another independently justified mechanism.
4. **Where do primes enter?** Determine whether prime-local terms arise intrinsically and whether the archimedean contribution and global counterterms are produced by the same structure rather than pasted together afterward.
5. **Is the bridge circular?** Reject constructions whose positivity is obtained only after assuming RH, placing the zeros on a self-adjoint spectrum by definition, or importing the Weil functional as an unexplained kernel.
6. **What survives controls?** Compare against integers, density-matched sequences, randomized/twisted Euler products, or other natural controls when they can expose universal geometric background.
7. **What is genuinely beyond prior art?** Search by mechanism and equivalent formulations, especially around Weil positivity, explicit formulas, Frobenius/cohomology, trace formulas, Sonin/localization positivity, noncommutative geometry, and geometric intersection forms.

## Existing Mathia evidence to treat as possible inputs, not assumptions

Other research branches may be read as evidence but remain read-only for this watch. In particular, potentially relevant surviving structures include:

- Prime Circle's anchored nonlocal and uniformization-defect mechanisms;
- Prime Flute's localized/marked relative spectral data and canonical background subtraction;
- Prime Lattice's function-space/Bohr dynamics after the failure of bare torus geometry;
- the canonical prior-art layer under `research/prior_art/`, especially Weil positivity, the explicit formula, finite-field Frobenius/cohomology, Sonin-space positivity, and Connes-style trace mechanisms.

No one of these is privileged. The line should be willing to conclude that none supplies the missing positivity structure.

## Evidence labels

Use the shared `mathia-research-watch` vocabulary, including:

- **EXACT-DERIVED** — exact consequence of an explicit Mathia construction;
- **LITERATURE+DERIVED** — published mathematics plus a derived Mathia consequence;
- **CLASSICAL-IDENTITY** — exact but already-standard structure that materially redirects the search;
- **CANDIDATE-NEW-STRUCTURE** — a precise, falsifiable organization whose novelty remains unestablished;
- **NEGATIVE/OBSTRUCTION** / **DECISIVE-NEGATIVE** — a natural positivity route is ruled out or sharply narrowed;
- **CONJECTURAL** / **NEEDS-AUDIT** — a bridge remains unproved or insufficiently sourced.

These labels record evidence and uncertainty, not importance.

## Persistence boundary

This line is maintained by `.agents/skills/mathia-research-watch/SKILL.md` with stable finding prefix **`WP`**.

When substantive results appear, persist them under the standard evidence contract:

```text
research/weil_positivity/SOURCES.md
research/weil_positivity/findings/WP-NNN-<slug>.md
```

The individual files under `findings/` are the canonical research evidence. Do not create a parallel hand-maintained finding index. Derived graph navigation may be added later by the graph curator when substantive findings exist.

Do not create chronological run notes or write into any `mind/` directory. Missing evidence artifacts should be initialized only when the first substantive finding requires them.