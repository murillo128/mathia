---
id: PA-landau-nonnegative-dirichlet-series-singularity
type: prior-art
canonical_name: Landau's theorem for nonnegative Dirichlet series
aliases:
  - Landau's abscissa theorem
  - Landau's nonnegative-transform singularity principle
kind: analytic-continuation-obstruction
topics:
  - Dirichlet-series
  - positivity
  - abscissa-of-convergence
---

# Landau's theorem for nonnegative Dirichlet series

## What it is

A Dirichlet series with nonnegative real coefficients and a finite real abscissa of convergence has a singularity at that real boundary point. Holomorphic continuation to a neighborhood of the boundary would contradict the abscissa: positivity allows the Taylor expansion to recover convergence farther left.

## Relation to RH / Mathia research

[[research/prime_lattice/findings/PL-460-raw-window-moment-landau-zero-free-gate|PL-460]] and [[research/prime_lattice/findings/PL-461-single-identity-residue-moment-zero-free-gate|PL-461]] explicitly use the nonnegative Mellin-transform version, with the positive-Taylor argument transferred by logarithmic change of variable. Their auxiliary nonnegative function is a one-sided error majorant minus a progression-counting error. Real-axis nonvanishing and cancellation of the main pole are separate inputs. The resulting zero-free implications remain conditional on unproved raw prime-window moment ceilings.

## Known scope and limits

Nonnegativity and a finite abscissa are essential to the stated theorem. It is not a zero-free theorem for arbitrary Dirichlet series, does not supply a prime-moment bound, and does not itself verify real-axis nonvanishing. Kedlaya's cited theorem is stated for Dirichlet series; the Mellin application and the special modulus-5 checks are supplied in the persisted Mathia arguments. No new analytic theorem is claimed here.

## Related prior art

The zero-free application also needs classical Dirichlet logarithmic derivatives and character identities. Those ingredients are distinct from Landau's convergence-boundary principle; sharing them does not establish a further finding-to-finding relation.

## Evidence and provenance

- Kiran S. Kedlaya, *Notes on Analytic Number Theory*, Chapter 3, Section 3.1, [Theorem 3.4 and proof](https://kskedlaya.org/ant/chapter-3.html): authoritative theorem statement and positive-Taylor proof for nonnegative Dirichlet series.
- Persisted lookup triggers: `research/prime_lattice/findings/PL-460-raw-window-moment-landau-zero-free-gate.md` (Section 3 and prior-art discussion) and `research/prime_lattice/findings/PL-461-single-identity-residue-moment-zero-free-gate.md` (Section 2 and prior-art discussion), at source revision `f5f2f29e0d2b76651fc8ef264cbf020baeb55ffa`.
- Recursive identity lookup across frozen and incremental canonical prior art found no existing node for this theorem. The similarly named Franel–Landau criterion concerns Farey discrepancy and is a different object.
