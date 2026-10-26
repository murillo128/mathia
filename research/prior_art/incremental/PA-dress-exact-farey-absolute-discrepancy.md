---
id: PA-dress-exact-farey-absolute-discrepancy
type: prior-art
canonical_name: Dress's exact absolute discrepancy of the Farey sequence
aliases:
  - Dress's Farey discrepancy theorem
kind: exact discrepancy theorem
topics:
  - Farey fractions
  - absolute discrepancy
---

# Dress's exact absolute discrepancy of the Farey sequence

## What it is

For the positive Farey fractions of order Q, let `N=sum_(q<=Q) phi(q)` and let `A_Q(x)` count points in `(0,x]`. Dress proves `sup_(0<x<=1) |x-A_Q(x)/N|=1/Q` for every positive integer Q. The lower bound is approached just before the first point `1/Q`; the upper bound is global. In particular, the ordered points satisfy `|x_k-k/N|<=1/Q`.

## Relation to RH / Mathia research

[[research/farey_discrepancy/findings/FD-010-absolute-farey-discrepancy-is-an-exact-endpoint-barrier|FD-010]] uses the theorem to separate endpoint-determined supremum discrepancy from cumulative Franel energy. [[research/farey_discrepancy/findings/FD-348-small-denominator-half-period-pairs-are-exact-rational-translates|FD-348]], Section 2, uses its pointwise bound as the analytic input to an exact rational half-translation restriction. These are separate applications of the same classical theorem, not a direct dependency between the findings.

## Known scope and limits

The convention excludes zero and includes one. Jump values depend on the counting convention; the displayed supremum uses the stated right-continuous count. This theorem alone supplies neither a joint denominator-count estimate, rank anti-concentration, half-period decorrelation nor an RH-strength averaged discrepancy bound. FD-348's incidence formula is its own finite reduction, not Dress's theorem.

## Related prior art

The [[research/prior_art/franel-landau-farey-discrepancy-criterion|Franel–Landau criterion]] concerns discrepancy aggregates. The [[research/prior_art/incremental/PA-farey-fixed-lag-gap-correlations|fixed-lag Farey gap-correlation theorem]] concerns products of gaps. Neither is this exact supremum theorem.

## Evidence and provenance

- François Dress, *Discrépance des suites de Farey*, Journal de théorie des nombres de Bordeaux **11**(2) (1999), 345–367. [Primary paper](https://www.numdam.org/article/JTNB_1999__11_2_345_0.pdf): definitions on printed page 345 and theorem on page 348, checked against the page images.
- Persisted trigger: `research/farey_discrepancy/findings/FD-348-small-denominator-half-period-pairs-are-exact-rational-translates.md`, Sections 2 and 5, at `f38757c6b031e9f0a9a77f99e7a05723bad81152`. The same dependency is explicit in `research/farey_discrepancy/findings/FD-010-absolute-farey-discrepancy-is-an-exact-endpoint-barrier.md`, Sections 1–3. Recursive canonical-prior-art comparison found no existing node for Dress's theorem; the Franel–Landau and fixed-lag nodes retain their distinct identities.
