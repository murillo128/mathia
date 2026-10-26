---
id: PA-farey-fixed-lag-gap-correlations
type: prior-art
canonical_name: Fixed-lag correlations of consecutive Farey gaps
aliases:
  - Hall–Boca–Cobeli–Zaharescu gap correlations
kind: arithmetic correlation asymptotic
topics:
  - Farey fractions
  - gap correlations
---

# Fixed-lag correlations of consecutive Farey gaps

## What it is

For the order-Q Farey points `0=x_0<...<x_N=1`, extend `x_(k+N)=x_k+1`, put `g_k=x_(k+1)-x_k`, and set `S_r(Q)=sum_(k=0)^(N-1) g_k g_(k+r)`. The classical full-interval asymptotics are

`S_0=(12/pi^2)log(Q)/Q^2+O(Q^-2)`,
`S_1=(6/pi^2)log(Q)/Q^2+O(Q^-2)`,
`S_r=O_r(Q^-2)` for each fixed integer `r>=2`.

The fixed-lag condition is essential. The cited modern formulation supplies explicit errors and lag-dependent thresholds; only the displayed leading terms are registered here.

## Relation to RH / Mathia research

[[research/farey_discrepancy/findings/FD-346-classical-gap-correlations-separate-high-band-farey-transport|FD-346]], Sections 1–4, explicitly uses these correlations to determine the weak high-band rank-discrepancy profile and reject its four-defect projected-transport comparator. The Fourier conversion and that application belong to FD-346, not to the external theorem.

## Known scope and limits

These estimates alone do not give a growing-lag bound, half-period decorrelation, a split between alternating Fourier indices, or the low-frequency control needed for an RH-strength Franel estimate. The Mathia application keeps its frequency band fixed away from zero.

## Related prior art

The [[research/prior_art/franel-landau-farey-discrepancy-criterion|Franel–Landau criterion]] concerns global discrepancy. This node records a different gap-correlation theorem, not an improvement of that criterion. The frozen Dedekind-sum reciprocity node concerns Bernoulli correlations and is not the same object.

## Evidence and provenance

- Florin P. Boca, Cristian Cobeli and Alexandru Zaharescu, *A conjecture of R. R. Hall on Farey points*, J. reine angew. Math. **535** (2001), 207–236, [DOI](https://doi.org/10.1515/crll.2001.049). The [author-institution record](https://experts.illinois.edu/en/publications/a-conjecture-of-r-r-hall-on-farey-points/) states the fixed-r full-interval correlation asymptotic.
- Anji Dong, Huy Xuan Nguyen, Vi Anh Nguyen and Alexandru Zaharescu, *Effective Estimates for a Class of Farey Fraction Sums and Bounds for Mundici-Type Constants*, [arXiv:2606.12907v1](https://arxiv.org/html/2606.12907v1), Section 1 periodic convention, equation (2.2), definition (2.5) and Theorem 2.3. The displayed statements verify the three leading terms and fixed-lag scope.
- Persisted trigger: `research/farey_discrepancy/findings/FD-346-classical-gap-correlations-separate-high-band-farey-transport.md`, Sections 2 and 6, at `e9ffbffc09cd7cecdf451dada2dcc58c60ebc0c9`. Recursive canonical-prior-art comparison distinguishes this theorem from Franel–Landau, Dedekind reciprocity and bounded-variation Fourier decay.
