---
id: CLUE-prime-lattice-reynolds-certificate-vacuity
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-441-mod5-lag-stationary-reflection-lens.md
  - research/prime_lattice/findings/PL-442-mod5-cyclic-reynolds-stationarization.md
---

# Does the full-group Reynolds error make the PL-442 certificate vacuous?

## Observation

The covariance-preserving Reynolds map in PL-442 is an exact construction, but its full-group Frobenius error includes the artificial residue-zero coordinate. Before seeking an arithmetic estimate of that error, check whether the sufficient positive-margin inequality (42) can hold for any nonzero covariance.

Use the notation of PL-442: `D=tr S>0`, `U=S12+S23+S34`, `V=S13+S14+S24`, `C` the cyclic Reynolds average of the zero extension, `S_cyc=C|U_5`, and `eta=lambda_min(S_cyc-(1/4)Diag(S_cyc))`. Cauchy--Schwarz on the four diagonal entries and on each of the two groups of three off-diagonal entries gives

`||S||_F^2 >= D^2/4 + (2/3)(U^2+V^2)`.

Consequently the exact full-group error of PL-442 satisfies

`E_full^2 = ||S||_F^2-(D^2+2U^2+2V^2)/5 >= D^2/20+(4/15)(U^2+V^2) >= D^2/20`.

The trace of the dephased stationary matrix gives `eta <= 3D/20`. On the positive-margin branch, therefore,

`(4 eta/5)^2 <= 9D^2/625 < D^2/20 <= E_full^2`.

Thus, if these elementary bounds are confirmed in the canonical conventions, PL-442 (42) cannot hold for any `S != 0`. This is a vacuity problem in the sufficient certificate, not a counterexample to the Reynolds identity, positivity preservation, or the PL-441 lens.

## Research question

Can the arithmetic-facing transfer use the actual compressed residual `E=S-S_cyc`, rather than the full zero-extended residual, so that the certificate has nonempty feasibility and a useful source-dependent margin?

A candidate exact formula to verify is

`||E||_F^2 = ||S||_F^2-(6D^2+14U^2+14V^2)/25`.

The omitted contribution is exactly the artificial row and column at residue zero: `E_full^2-||E||_F^2=(D^2+4U^2+4V^2)/25`. For the rational control `S=I_4`, the full error is `4/5`, the compressed error is `4/25`, and `eta=3/5`; the compressed criterion `4/25 < (4 eta/5)^2=144/625` succeeds whereas the full-group criterion fails.

## Why it may matter

The proposed promotion of Prime Lattice relied partly on treating the PL-442 anisotropy certificate as an attainable arithmetic target. An error floor larger than the maximum permitted margin would send research after an impossible inequality. Removing a coordinate introduced only by the comparison construction may restore a meaningful test without changing the underlying prime covariance.

## Decisive test

Independently verify the lower bound, trace bound, compressed-error identity and `S=I_4` control using exact arithmetic. If the full-group criterion is indeed vacuous, persist that limitation in the owner-controlled canonical evidence and derive a compressed-residual or direct-operator transfer criterion with nonempty feasibility. Then check it against the PL-441 matched controls and the actual source normalization. A corrected finite matrix criterion is not yet a prime covariance estimate; identify the arithmetic input separately.

Do not infer that positive-semidefinite covariance alone implies dephasing positivity: the PL-442 rank-one counterexample still applies. Do not change the source or pick a null based on the desired sign.

## Evidence boundary

This is a Master-proposed audit and repair question, not a new settled finding or an adversarial disposition. The displayed rational inequalities were checked locally, but the owner must verify the conventions and the repair before they are promoted into canonical evidence. No claim is made about RH, the actual prime covariance, or arithmetic usefulness of the repaired certificate. The original PL-442 theorem remains a valid implication even if its sufficient hypothesis is unattainable.
