# Farey-discrepancy source anchors

This file records durable literature dependencies for `research/farey_discrepancy/`. It is an anchor list, not a search history.

## Core criterion

- [`research/prior_art/franel-landau-farey-discrepancy-criterion.md`](../prior_art/franel-landau-farey-discrepancy-criterion.md). Role: Mathia prior-art anchor for RH-equivalent Farey discrepancy bounds and the warning that a geometric redrawing is not new progress.
- [`research/prior_art/dedekind-sum-reciprocity-in-farey-correlations.md`](../prior_art/dedekind-sum-reciprocity-in-farey-correlations.md). Role: neighboring reciprocity/correlation structure relevant when a candidate uses arithmetic information beyond scalar discrepancy.

## Denominator shells and harmonic arithmetic

- Rogelio Tomás García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140, DOI `10.3390/math13010140`. Role: prior-art boundary for decomposing Farey local discrepancy into exact-denominator/totient-level contributions and for Mertens-based discrepancy formulas used in `FD-001`.
- Srinivasa Ramanujan, *On Certain Trigonometrical Sums and Their Applications in the Theory of Numbers*, Transactions of the Cambridge Philosophical Society **22** (1918), 259--276. Role: classical source for Ramanujan sums and their divisor arithmetic used to derive the exact shell Fourier and Gram identities in `FD-001`.
- Paolo Codecà and Alberto Perelli, *On the uniform distribution (mod 1) of the Farey fractions and l^p spaces*, Mathematische Annalen **279** (1988), 413--422, DOI `10.1007/BF01456278`. Role: neighboring harmonic-analysis prior-art boundary for Farey uniform distribution and RH-sensitive norm estimates; `FD-001` does not claim that harmonic analysis of Farey fractions is new.

## Empirical-distribution quadratic identity

- Harald Cramér, *On the Composition of Elementary Errors: Second Paper: Statistical Applications*, Scandinavian Actuarial Journal **1928** (1928), 141--180, DOI `10.1080/03461238.1928.10416872`. Role: classical source boundary for the Cramér--von Mises integrated empirical-distribution quadratic statistic whose ordered-sample formula is specialized to the Farey endpoint grid in `FD-002`.
- Richard von Mises, *Wahrscheinlichkeit, Statistik und Wahrheit*, Springer, Berlin, 1928, DOI `10.1007/978-3-662-36230-3`. Role: classical source boundary for the same integrated-distribution quadratic criterion; `FD-002` proves its required Farey specialization directly and does not import statistical asymptotics.

## Expansion rule

Add primary sources only when a canonical finding depends on an exact Farey discrepancy theorem, Möbius bridge, reciprocity identity, or genuinely stronger geometric/multiscale structure.