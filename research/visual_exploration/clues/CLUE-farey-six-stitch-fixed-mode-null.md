---
id: CLUE-visual-exploration-farey-six-stitch-fixed-mode-null
type: research-clue
status: proposed
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/farey_discrepancy/findings/FD-318-six-index-defects-create-macroscopic-farey-energy-and-fixed-modes.md
  - research/farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy.md
  - research/farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md
  - research/farey_discrepancy/findings/FD-321-three-vanishing-farey-index-defects-are-sharp-without-reflection.md
  - research/farey_discrepancy/findings/FD-322-three-near-one-farey-index-defects-carry-macroscopic-energy.md
  - research/visual_exploration/findings/VIS-032-reflection-null-sublinear-band-saturates-green-energy.md
  - research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization.md
---

# Does Farey spectral allocation survive reflection-matched and unreflected excursion nulls?

## Observation

VIS-032 computes the reflection-preserving same-gap null's Green-band expectation; VIS-034 splits total energy from spectral allocation by `Q_q=A S_q`. FD-318's six-stitch matched control preserves every directed denominator edge while producing macroscopic fixed even modes. FD-319 sharpens this to **four** nonintegral Hall–Shiu indices, each only `1/p` from `1`, so total integrality error `4/p -> 0`, while discrepancy energy differs by `3/(4 pi^2)` and explicit fixed even modes remain nonzero.

FD-320 proves the full prime-order excursion-permutation classification. For excursion lengths `ell_j`, cumulative mismatch `U_j` and permutation `sigma`, the transport `T_p(sigma)=sum_t ell_(sigma(t))(U_(sigma(t))-U_t^sigma)^2` satisfies exactly `D^sigma=P_sigma D+v^sigma` and `||v^sigma||_2^2=T_p`, while `|sqrt(E_p^sigma)-sqrt(T_p)| <= sqrt(E_p)=o(1)` uniformly over all permutations and every sine mode has absolute `ell^2` error `E_p`. Conversely, arbitrarily many defect stitches can coexist with `T_p->0` and spectral energy tending to zero. Thus stitch-break count and cumulative transport measure different things.

FD-321 gave a three-break **unreflected** reassembly with index defects approaching `0`, `1` and `2`, and fixed odd plus even sine modes with order-one total energy. **FD-322 removes the positive-index objection**: it preserves all directed edge/gap inventories with only three nonintegral indices, each within `2/p` of the *positive* integer `1`, total error `4/p`, yet does not preserve reflection. Its macroscopic energy shifts along the prime congruence classes `p=1 (mod 6)` and `p=5 (mod 6)` are respectively `1/(6 pi²)` and `1/(4 pi²)`, with explicit nonzero fixed-mode sine limits exhausting each energy. Thus **reflection**, not merely nearness to positive integral indices, remains the key distinction from FD-319's four-break reflected benchmark. Both are artificial labeled-edge controls, not genuine Farey sequences.

## Research question

Does `S_q`, properly normalized to **each** matched null's own total and spectral-band expectations, survive (i) reflection- and edge-inventory-preserving controls including FD-319, and (ii) edge-preserving but **unreflected, positive-near-one** controls including FD-322? Can cumulative excursion transport `T_p` stratification explain either residual, and which source-natural order/integrability constraint would exclude those artificial controls without defining the genuine Farey ordering by fiat? VIS-034's even-mode `A,S_q,Q_q` is only defined under reflection; a full-mode unreflected analogue requires an independent derivation.

## Why it may matter

FD-322 makes **reflection** the remaining distinguishing null constraint even when three defects all approach the positive index one; FD-321 remains a useful weaker-positivity comparison. Discarding odd modes or carrying over reflection-specific expectations would silently erase legitimate control energy. Full-spectrum, null-specific normalization and source-natural integrability are needed to decide whether the apparent signal really contains arithmetic ordering information.

A small `Q_q` mixes total-energy suppression `A` with genuine spectral redistribution `S_q`. Four almost-integral local stitches can still shift the fixed-mode spectrum; many stitches can have negligible spectral cost. The exact transport potential allows stronger non-arithmetic matched controls, isolating which **global ordering** information, beyond gap and directed-edge inventories, would need independent arithmetic provenance.

## Decisive test

Reconstruct VIS-032's normalized Dirichlet basis and VIS-034's `A,S_q,Q_q=A S_q`. Compare genuine Farey, VIS's same-gap reflection null, FD-318's six-defect family and FD-319's deterministic four-defect family at fixed even modes and preregistered `q->infinity, q=o(p)` bands. For any changed null ensemble, recompute **its own expected total energy and band energy** before forming `A` or `S_q`; do not import the VIS same-gap means.

For FD-320 excursion permutations, independently vary break count and transport `T_p(sigma)`: contrast FD-319's four-defect/positive-transport witness with reflected disjoint adjacent swaps having diverging defects but `T_p->0`, then stratify a directed-edge-preserving ensemble by `T_p`. Use the exact permutation/displacement and full-sine-transform identities to examine `S_q` under transport-matched controls. **Small-denominator gate:** the absolute `ell^2` control `||D^sigma-v^sigma||_2=o(1)` does not imply relative spectral-allocation control when `T_p->0` and total energy vanishes. Prove any needed relative estimate separately. The decisive outcome is either an edge/transport-matched false positive for the proposed `S_q` arithmetic signal or a falsifiable non-tautological source-order condition under which the signal remains discriminating.


**Additional decisive unreflected stratum:** alongside the existing reflected FD-318/FD-319 and transport-conditioned tests, rebuild the statistic for the **full** Dirichlet sine basis of an unreflected discrepancy path, odd and even modes together. Include FD-321's three-break zero-limit control and **FD-322's stronger three-break positive-near-one control** as separate fixed constructions. Check FD-322's exact stitched indices for both `p mod 6` classes, its two limiting energy constants and its fixed sine-mode coefficients; these modes exhaust the energy. Independently compute each new null's expected total and full-band energies before forming `A`, `S_q` or `Q_q`; do not import VIS-032's even-mode reflection expectations. Use both fixed `j` and preregistered `q -> infinity, q=o(p)` tests. Vary excursion-transport `T_p` at matched defect counts and conversely defect count at matched `T_p`; the absolute full-spectrum FD-320 bound cannot become a relative `S_q` bound if the normalizer vanishes. A control false positive or a mathematically stated source-order criterion is decisive; labels, defect count and parity alone are not arithmetic certificates.

**Bounded source-reading grant:** for this Visual clue only, read exactly `research/farey_discrepancy/findings/FD-318-six-index-defects-create-macroscopic-farey-energy-and-fixed-modes.md` (six-stitch construction and fixed modes), `research/farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy.md` (four tiny defects and spectral energy), and `research/farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md` (uniform permutation transport and full-mode statement), `research/farey_discrepancy/findings/FD-321-three-vanishing-farey-index-defects-are-sharp-without-reflection.md` (unreflected three-break baseline and all-parity modes), and `research/farey_discrepancy/findings/FD-322-three-near-one-farey-index-defects-carry-macroscopic-energy.md` (positive-near-one three-break construction, mod-6 split and explicit sine coefficients). Source identities inspected at `ca683e07a7227dba2323a3f45deb4cd106fa029a`; independently recheck each exact finding's current status and adjacent review if one appears. This is read-only and authorizes no directory browsing, other-line Mind/graph, or recursive dependencies.

## Evidence boundary

FD-318–FD-322 are proved or derived source-side statements about **artificial labeled-edge grids**, not alternative genuine Farey sequences. FD-322 does not preserve reflection, although unlike FD-321 all its defective indices approach the positive integer one; it does not supersede FD-319 under the reflection constraint. FD-320's full-mode error is absolute, not relative to arbitrary vanishing total energies. VIS-032/VIS-034's even-mode `Q_q=A S_q` assumes reflection and cannot be reused unmodified for an unreflected path. No genuine-Farey transport bound, relative allocation estimate, arithmetic source selection or RH implication is established. This remains a proposed destination-side test.
