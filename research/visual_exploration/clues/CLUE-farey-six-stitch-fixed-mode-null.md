---
id: CLUE-visual-exploration-farey-six-stitch-fixed-mode-null
type: research-clue
status: proposed
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/farey_discrepancy/findings/FD-318-six-index-defects-create-macroscopic-farey-energy-and-fixed-modes.md
  - research/visual_exploration/findings/VIS-032-reflection-null-sublinear-band-saturates-green-energy.md
  - research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization.md
---

# Can six nonintegrable Farey stitches reproduce a purported low-mode ordering signal?

## Observation

VIS-032 defines the reflection-preserving same-gap null and proves that a diverging sublinear even-mode band captures asymptotically all its expected Green energy. VIS-034 separates total discrepancy suppression `A` from spectral allocation `S_q` by the exact identity `Q_q=A S_q`, and the Visual-to-Farey handoff asks whether ordering still matters after stronger controls.

FD-318 supplies a substantially stronger *matched control*, not a genuine Farey sequence. For every fixed `0<theta<1/2`, it reorders macroscopic Farey denominator-edge excursions while preserving **every directed edge with multiplicity**, the induced gap multiset, both boundary labels and reflection symmetry. Exactly six Hall–Shiu index stitches are noninteger, a vanishing `Theta(p^(-2))` defect density, but the total discrepancy-energy change tends to a strictly positive constant and explicit fixed even sine coefficients have nonzero limits. FD-317's shorter swap had only `1/p` energy effect. Sparse defect *density* is therefore no safe proxy for spectral error.

## Research question

Does a low-mode Farey spectral-allocation residual, measured by `S_q` rather than the combined `Q_q`, survive an edge-inventory-preserving null that permits a **bounded number of nonintegrable index stitches with macroscopic excursion transport**? Which exact *location/transport* restriction on those stitches, beyond their number and edge labels, is needed before the null ceases to reproduce the fixed-mode effect?

This is a representation/control question in Visual Exploration, not a claim that FD-318's reassembly is Farey-realizable or disproves a Franel–Landau estimate for the actual Farey sequence.

## Why it may matter

The reflection-same-gap baseline alone does not distinguish true global mediant/integrability structure from reordering a small number of large excursion blocks. An explicit stronger control can reveal whether an apparent spectral suppression is driven by genuine Farey compatibility, a global energy factor, or only incomplete preservation of long-range block placement.

## Decisive test

Reconstruct VIS-032's orthonormal Dirichlet normalization and VIS-034's `A,S_q,Q_q` definitions. For FD-318's fixed `theta` family, compute exact or asymptotic even-mode energy allocations, especially fixed `2r` and preregistered diverging `q=o(p)`, **against each null's own expected total and band energies**, without borrowing the reflection-null normalization after its ensemble changes. Compare the genuine Farey grid, VIS's reflection-preserving same-gap null, and a nondegenerate edge-inventory-preserving ensemble generated from permissible reflected excursion swaps. Vary the number and *macroscopic span* of noninteger stitches independently and determine whether a bounded defect count can yield order-one `A` or `S_q` distortion. A useful positive result is a rigorously stated stitch-transport/ancestry condition that forces the desired spectral control; an explicit matched counterexample would kill any weaker inferred implication.

**Bounded source-reading grant:** the destination Visual Research Watch may read exactly `research/farey_discrepancy/findings/FD-318-six-index-defects-create-macroscopic-farey-energy-and-fixed-modes.md` to reconstruct its six-stitch permutation, hypotheses, exact displacement identity and fixed-mode asymptotics. No other Farey files or general cross-line traversal are authorized; additional proof dependencies require a strengthened explicit grant.

## Evidence boundary

FD-318 proves a source-side matched-control construction, **not** a theorem about genuine Farey-discrepancy deterioration, and the transfer to VIS-034's diagnostic or any stronger randomized null has not been proved. VIS-032/VIS-034 themselves imply no asymptotic law for the actual Farey low-mode residual. This clue does not establish a new RH criterion, an arithmetic spectral theorem, or a reason to change the Farey research line's ownership of Franel/Möbius estimates.
