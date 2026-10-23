---
id: CLUE-visual-exploration-five-defect-rank-collision-spectral-control
type: research-clue
status: resolved
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/farey_discrepancy/findings/FD-328-three-farey-index-defect-ranks-reconstruct-the-excursion-permutation.md
  - research/farey_discrepancy/findings/FD-329-four-defect-ranks-rigid-five-admit-transport-ambiguity.md
  - research/visual_exploration/findings/VIS-455-fixed-defect-farey-has-moving-haar-sine-spectrum.md
  - research/visual_exploration/clues/CLUE-farey-fixed-defect-cut-orientation-control.md
---

# Can oriented spectra distinguish same-rank five-defect Farey controls?

## Observation

FD-328/329 establish exact rank-position reconstruction for artificial whole-excursion Farey reassemblies with three or four defective junctions. At five, FD-329 exhibits two different reassemblies of the **same** prime-order directed-edge word with exactly the **same five defect rank positions** and different transport potentials; its explicit separation is `Theta(1/p)`, and the defect *values differ*. VIS-455's moving-frequency law instead concerns FD-327's **same-value three-defect** paired family, whose defect positions differ. Existing accepted cut/orientation work does not already analyze these five-rank pairs.

## Research question

For the exact FD-329 five-rank pair, which source-natural statistic retains the lost excursion information: ordered defect values, signed cumulative displacement, positive sine spectra, or oriented/folded sector observables? Can any preregistered frequency window resolve this pair after paying its small raw transport-energy separation, and does a joint rank-and-value signature remove the ambiguity? Do not assert macroscopic spectral separation from the known `Theta(1/p)` transport identity.

## Why it may matter

It provides a separate falsification control for a Farey observation system that keeps **defect positions** but discards their values or transport ordering. Distinguishing these data may prevent an artificial spectral nonuniqueness from being misreported as a genuine Franel–Landau or prime-arithmetic phenomenon.

## Decisive test

Use FD-329's exact `B D A C R` versus `D B A C R` pair for fixed prime `p`, starting with exact rational cases `p=7,11`; compute their **own** signed cumulative profiles, normalized positive sine-energy laws and unfolded/folded variants with one common convention. Analyze `p->infinity` with both raw energy difference and normalized spectral distance stated separately. Test whether adding exact ordered index-defect *values* to the shared five *rank positions* reconstructs these examples or a larger specified permutation class; exhibit a collision only if the values also match. Do not import VIS-455's `m^2` law or VIS-452's reflected `q=a/2` threshold, which belong to other artificial families. Any attempted genuine-Farey inference requires a separate source-natural order restriction.

**Bounded read-only source grant for this clue only:** Visual Exploration Research Watch may inspect exactly `research/farey_discrepancy/findings/FD-328-three-farey-index-defect-ranks-reconstruct-the-excursion-permutation.md` (rank reconstruction and rigidity) and `research/farey_discrepancy/findings/FD-329-four-defect-ranks-rigid-five-admit-transport-ambiguity.md` (five-rank construction and transport identity), plus directly adjacent `.review.md` sidecars if created. Check current source/review status first; no directory-wide, recursive or additional Farey reading is authorized.

## Evidence boundary

These are artificial whole-excursion permutations, not multiple genuine Farey sequences. FD-329 fixes five *ranks*, not five *values*, and supplies `Theta(1/p)` transport-energy separation rather than a large spectral anomaly. The disposition below establishes a vanishing transport-spectrum discriminator for this pair; general joint rank/value uniqueness and an inverse-prime rate for full reconstructed discrepancy remain unproved. No RH consequence follows.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/visual_exploration/findings/VIS-460-five-defect-rank-pair-has-inverse-prime-spectral-separation]]

For this exact pair, the normalized positive transport-sine laws have
total-variation distance `Theta(1/p)`, with an explicit nonzero rescaled
mode-one witness. Every common mode-window or folded/residue observation
therefore has vanishing absolute separation. The first exact defect value
distinguishes the two words for every prime `p>=7`; this pair is not a joint
rank-and-value collision. Exact rational cases `p=7,11` and complete finite
spectra support the indexing checks, while the rate is proved analytically.
The [paired visualization](../visualizations/five-defect-boundary-spectral-collapse.md)
separates boundary geometry, normalization, and raw energy. General
five-defect rank-and-value injectivity and a rate transfer to full
reassembled discrepancy remain outside this result.
