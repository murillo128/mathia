---
id: PA-lipschitz-integration-recovery
type: prior-art
canonical_name: Lipschitz integration and sampling recovery
aliases:
  - Lipschitz recovery
  - Lipschitz envelope integration
  - Tent-function integration lower bounds
kind: optimal-recovery mechanism
topics:
  - optimal-recovery
  - lipschitz-functions
  - sampling
---

# Lipschitz integration and sampling recovery

## What it is

For functions with a supplied Lipschitz constant, observed values constrain the function between upper and lower slope envelopes. Integrating these envelopes bounds the possible integral. In the unit-Lipschitz case, two samples separated by d with value difference Δ leave integral uncertainty of width (d²−Δ²)/2; equal values give the familiar quadratic gap cost. Indistinguishable admissible functions with different integrals provide recovery lower bounds. These are classical mechanisms, not arithmetic cancellation estimates.

## Relation to RH / Mathia research

[[research/mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance|MC-533]], Sections 1 and 4, explicitly specializes Lipschitz recovery to integer starts: nearest-sample cell weights and total distance control complete absolute mass. Its separate reciprocal-pole input yields a conditional sparse-grid RH criterion.

[[research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity|PL-477]], Sections 1–4, uses the classical indistinguishability/tent mechanism but constructs its own compatible pair of window observations from two fixed positive residue-supported sources. That construction is not asserted by the external integration theorem.

## Known scope and limits

The model class and observation functionals matter. Classical Lipschitz envelopes alone do not imply multiplicativity, prime-power support, arithmetic explicit formulas, or optimal sampling thresholds for Möbius or von Mangoldt data. MC-533's weighted discrete bound and PL-477's fixed-source packet construction remain canonical local derivations. No external priority or novelty upgrade is inferred.

## Related prior art

[[research/prior_art/incremental/PA-multichannel-compact-distribution-deconvolution|Multichannel compact-distribution deconvolution]] supplies a different operation in the cited applications: reconstruction of complete smooth tests. It does not itself recover deleted observations.

## Evidence and provenance

- Ilya Baran, Erik D. Demaine and Dmitriy A. Katz, *Optimally Adaptive Integration of Univariate Lipschitz Functions*, Algorithmica 50(2), 255–278 (2008), [DOI](https://doi.org/10.1007/s00453-007-9093-7). [Author-hosted paper](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf), Section 2, Definition 2 and Proposition 1, gives the envelope uncertainty; the [author bibliography](https://erikdemaine.org/papers/Integration_Algorithmica/) verifies publication identity.
- Simon Foucart, *Mathematical Pictures at a Data Science Exhibition* (Cambridge, 2022), [Chapter 9](https://doi.org/10.1017/9781009003933.015) and [Chapter 11](https://doi.org/10.1017/9781009003933.017). Publisher summaries identify the optimal-recovery framework and integration of Lipschitz functions; the full chapter proofs were not inspected here.
- Persisted lookup triggers: `research/mobius_cancellation/findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md`, prior-art paragraph and equations (7), (16)–(17); `research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity.md`, prior-art paragraph and Section 4. Both were read at `704e7681c084d662fa47114d33b79b6512815a8b`.
