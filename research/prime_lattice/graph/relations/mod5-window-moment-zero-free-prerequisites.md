---
id: RG-mod5-window-moment-zero-free-prerequisites
type: research-graph-relation
scope: prime_lattice
derived: true
---

# Mod-5 window moments retain zero-free prerequisites

[[research/prime_lattice/graph/prime-lattice|Prime Lattice]] · [[research/graph/atlas/territories/RA-A1-zero-free-regions-pnt-error|Classical zero-free territory]]

This mechanism records conditional implications already proved in the canonical sources. The prime estimates are unproved premises. It neither proves RH nor refutes the conditional covariance calculation.

## The conditional source and its distinct gates

Throughout, `H = floor(X^theta)` and the estimates concern the actual von Mangoldt windows in reduced residues modulo 5.

- [[research/prime_lattice/findings/PL-458-mod5-singular-series-matrix-second-order-transfer|PL-458]] computes the mod-5 triangular singular-series model unconditionally, but transfers it to the deterministically centered prime covariance only under separate first-moment (A) and signed second-order pair (B) assumptions, for fixed `1/6 < theta < 1/2` and at `t=0`.
- [[research/prime_lattice/findings/PL-459-integrated-first-moment-zero-free-gate|PL-459]] diagnoses (A): the four integrated first moments at `o(X log X)` precision imply zero-freeness of every mod-5 Dirichlet L-function in `Re s > 1-theta`, for fixed `0 < theta < 1/2`. The family with fixed exponents tending to `1/2` is equivalent to joint GRH modulo 5. The endpoint is excluded from this equivalence.
- [[research/prime_lattice/findings/PL-460-raw-window-moment-landau-zero-free-gate|PL-460]] diagnoses (B) independently of (A): four raw diagonal ceilings `Q_aa <= X H^2/16 + O(X H log X)` imply the same zero-free half-plane for fixed `0 < theta <= 1/2`. Its pair-to-moment endpoint accounting does not establish the transfer from (B) at `theta=1/2`.
- [[research/prime_lattice/findings/PL-461-single-identity-residue-moment-zero-free-gate|PL-461]] reduces that raw premise to the identity residue `a=1`. Coincident zero residues add with one sign there; Landau positivity also needs the separately verified absence of real mod-5 zeros. Only the `a=b=1` instance of (B) is needed in PL-458's strict range. This refines PL-460's four-channel proof, without changing its conclusion.
- [[research/prime_lattice/findings/PL-462-narrow-window-phase-coherence-zero-free-gate|PL-462]] transfers one selected twisted raw ceiling per scale to PL-461, for fixed `0 < theta <= 1/2`, when `|t_X| = O(X sqrt(log X)/H^(3/2))`. Its positive-arc comparison uses nonnegative coefficients and does not transfer to centered or signed windows.
- [[research/prime_lattice/findings/PL-463-empirically-centered-window-variance-zero-free-gate|PL-463]] treats the different empirical-centering premise `V_1 = O(X H (log X)^A)`, with fixed finite `A >= 0` and `0 < theta < 1`. Mean-zero probes and finite-order inversion of the box average retain zero poles and imply only `Re s > 1-theta/2`. At `theta=1/2` this gives `Re s > 3/4`; a family with fixed exponents tending to `1` implies joint GRH. No converse or prime-specific optimality is asserted.

All these moment premises hold for **every sufficiently large real scale**, with fixed exponents in each application. None is supplied by Gram positivity or by a relative lower-frame bound. Sparse scales, vertical-frequency averages and centers varying inside the window are outside these deductions. The broader signed/oriented covariance route remains a separate obligation.

## Classical mechanism and evidence boundary

[[research/prior_art/incremental/PA-landau-nonnegative-dirichlet-series-singularity|Landau's theorem]] is the named prior-art dependency of PL-460 and PL-461, not a new arithmetic result. PL-463 uses a different Mellin probe argument, explicitly calibrated against Zaccagnini's [Selberg-integral converse, Section 3.3](https://arxiv.org/abs/1603.02952); that multiplicative, deterministically centered result is not identified with the empirical additive-window theorem. [[research/prime_lattice/mind/intuition/MI-064-the-mod5-first-moment-premise-is-a-zero-free-input|MI-064]] synthesizes the distinction; the findings above supply the evidence.

Existing prose references in PL-459–PL-463 carry direct internal links where their exact endpoints and relation passages were verified. This note supplements those adjacencies. References outside this bounded mechanism are not certified as fully reconciled. The five obstruction refinements form one frontier question about the zero-free content of proposed moment inputs, not five fertility events; topology maintenance and prior-art registration add no events.


## Dyadic continuation of the empirical-variance question

[[research/prime_lattice/graph/relations/dyadic-seam-filtered-zero-recovery|Dyadic seam filtering and arithmetic pole recovery]] records PL-464's weaker dyadic scale premise and PL-466's removal of its sharp-block endpoint loss using classical zero density. It retains the full base-point integral at every large dyadic scale. The preceding all-real-scale restriction describes PL-459–PL-463, not an impossibility theorem for dyadic data. PL-466 does not establish a relative covariance frame or prove the prime variance input.
