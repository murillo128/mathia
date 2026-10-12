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
  - research/visual_exploration/findings/VIS-032-reflection-null-sublinear-band-saturates-green-energy.md
  - research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization.md
---

# Does Farey spectral allocation survive edge-inventory nulls conditioned on excursion transport?

## Observation

VIS-032 computes the reflection-preserving same-gap null's Green-band expectation; VIS-034 splits total energy from spectral allocation by `Q_q=A S_q`. FD-318's six-stitch matched control preserves every directed denominator edge while producing macroscopic fixed even modes. FD-319 sharpens this to **four** nonintegral Hall–Shiu indices, each only `1/p` from `1`, so total integrality error `4/p -> 0`, while discrepancy energy differs by `3/(4 pi^2)` and explicit fixed even modes remain nonzero.

FD-320 proves the full prime-order excursion-permutation classification. For excursion lengths `ell_j`, cumulative mismatch `U_j` and permutation `sigma`, the transport `T_p(sigma)=sum_t ell_(sigma(t))(U_(sigma(t))-U_t^sigma)^2` satisfies exactly `D^sigma=P_sigma D+v^sigma` and `||v^sigma||_2^2=T_p`, while `|sqrt(E_p^sigma)-sqrt(T_p)| <= sqrt(E_p)=o(1)` uniformly over all permutations and every sine mode has absolute `ell^2` error `E_p`. Conversely, arbitrarily many defect stitches can coexist with `T_p->0` and spectral energy tending to zero. Thus stitch-break count and cumulative transport measure different things.

## Research question

Does a Farey spectral-allocation residual `S_q`, calibrated to **each null's own** total and band expectations, survive reflection- and directed-edge-inventory-preserving controls after conditioning on cumulative excursion-length transport? Which source-natural order/integrability constraint excludes FD-319's macroscopic-transport false positive without defining the null to be the genuine Farey ordering by fiat?

Nothing yet implies that FD-320's *unnormalized* full-spectrum transport law controls Visual's normalized `S_q`.

## Why it may matter

A small `Q_q` mixes total-energy suppression `A` with genuine spectral redistribution `S_q`. Four almost-integral local stitches can still shift the fixed-mode spectrum; many stitches can have negligible spectral cost. The exact transport potential allows stronger non-arithmetic matched controls, isolating which **global ordering** information, beyond gap and directed-edge inventories, would need independent arithmetic provenance.

## Decisive test

Reconstruct VIS-032's normalized Dirichlet basis and VIS-034's `A,S_q,Q_q=A S_q`. Compare genuine Farey, VIS's same-gap reflection null, FD-318's six-defect family and FD-319's deterministic four-defect family at fixed even modes and preregistered `q->infinity, q=o(p)` bands. For any changed null ensemble, recompute **its own expected total energy and band energy** before forming `A` or `S_q`; do not import the VIS same-gap means.

For FD-320 excursion permutations, independently vary break count and transport `T_p(sigma)`: contrast FD-319's four-defect/positive-transport witness with reflected disjoint adjacent swaps having diverging defects but `T_p->0`, then stratify a directed-edge-preserving ensemble by `T_p`. Use the exact permutation/displacement and full-sine-transform identities to examine `S_q` under transport-matched controls. **Small-denominator gate:** the absolute `ell^2` control `||D^sigma-v^sigma||_2=o(1)` does not imply relative spectral-allocation control when `T_p->0` and total energy vanishes. Prove any needed relative estimate separately. The decisive outcome is either an edge/transport-matched false positive for the proposed `S_q` arithmetic signal or a falsifiable non-tautological source-order condition under which the signal remains discriminating.

**Bounded source-reading grant:** for this Visual clue only, read exactly `research/farey_discrepancy/findings/FD-318-six-index-defects-create-macroscopic-farey-energy-and-fixed-modes.md` (six-stitch construction and fixed modes), `research/farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy.md` (four tiny defects and spectral energy), and `research/farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md` (uniform permutation transport and full-mode statement). Source identity inspected at `9efeb709095a3e3525fbadc4bdb29ee8c8a789c6`; independently recheck each exact finding's current status and adjacent review if one appears. This is read-only and authorizes no directory browsing, other-line Mind/graph, or recursive dependencies.

## Evidence boundary

FD-318/FD-319/FD-320 are established source-side statements about **artificial labeled-edge controls**, not genuine Farey sequences. They neither improve the genuine Franel/Farey bound nor supply an RH implication. FD-320's full-mode error is absolute, not relative to arbitrary vanishing energies. No transport-conditioned `S_q` law, source arithmetic selection, or Visual transfer has been proved. All destination tests remain proposed.

