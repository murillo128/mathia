---
id: CLUE-farey-discrepancy-reflected-farey-erasure-energy-conditioned-spectrum
type: research-clue
status: proposed
origin: master-researcher
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-344-reflection-makes-three-farey-defect-erasures-recoverable-four-need-not-be.md
  - research/visual_exploration/findings/VIS-461-one-quantum-farey-pair-retains-normalized-spectral-separation.md
  - research/visual_exploration/clues/CLUE-farey-reflection-parity-equal-energy-control.md
---

# Does exact total energy determine the spectrum after four reflected Farey value erasures?

## Observation

FD-344 fixes an odd prime `p>=7`, the genuine positive excursion lengths, the full defective-rank list and the erasure locations. In its reflected class, mirrored defect numerators are equal and their half-list sums to zero. Any three erased values are recoverable; four erasures comprising two whole mirror pairs can hide different reassemblies and different discrepancy energies. Its explicit `p=7` pair has unequal energies, so retaining total energy distinguishes that certificate.

VIS-461 supplies an asymptotic warning beyond the finite certificate: its reflected pair has the same six ranks and numerator difference `(-1,1,0,0,1,-1)`, yet distinct limiting normalized sine laws. Its limiting energies are also different. It therefore does not answer what happens when the exact scalar energy is retained. The existing equal-energy clue compares reflected and unreflected families with different parity constraints and does not impose a common partially erased signature.

## Research question

For the FD-344 class, does the following exact record determine the normalized positive sine spectrum of the **full reconstructed discrepancy**?

- the prime `p`, original excursion lengths, full ordered defective ranks, and locations of exactly two erased mirror pairs;
- every remaining defect numerator;
- the exact total energy `E=sum_(k=1)^(N-1) D_k^2>0`, with `N=sum_(q<=p) phi(q)`, reconstructed grid `x`, and `D_k=x_k-k/N`.

The spectrum is `pi_m=|Dhat_m|^2/E`, using the orthonormal Dirichlet sine transform and absolute mode indices `1<=m<N`. Either prove determination for this specified record or find two realizable reflected reassemblies sharing the record but differing in at least one normalized sine coefficient. This is a question about the remaining spectral shape, not about reconstructing every excursion label.

## Why it may matter

A total-energy measurement could eliminate an apparent spectral ambiguity caused only by discarded amplitude. A collision surviving that measurement would supply a stricter reflection- and energy-matched null with identical retained local data. Either outcome clarifies which observation actually retains order information; neither establishes that genuine Farey order satisfies an improved estimate.

## Decisive test

Start with exact reflected enumeration at `p=7,11`, grouped by the full rank list, chosen two erased mirror pairs and all retained integer numerators. Within each group compare exact rational **full** energies before examining spectra. If a nontrivial equal-energy pair exists, reconstruct both denominator words independently, verify their directed-edge inventory, reflection and complete signatures, then certify a differing squared sine coefficient by exact algebra or rigorous bounds. Floating equality of energies or a plot is insufficient. Global sign, rank reversal and scalar-amplitude changes are controls; different vectors alone do not establish different squared spectra.

If the finite search finds no collision, report only that bounded result. For a universal conclusion, reconstruct the allowed missing-numerator family from the half-checksum and Farey realizability, and determine whether exact energy identifies its spectrum. Do not assume every checksum-compatible numerator vector is realizable. Do not rescale artificial grids to force equal energies: that changes their gaps and the class. A transport-only calculation must separately justify transfer to full discrepancy; an asymptotic small-residual argument does not grant exact equality or uniqueness. An asymptotic family is a possible later extension, not a premise of this first test.

**Bounded source reading for Farey Discrepancy:** read only `research/visual_exploration/findings/VIS-461-one-quantum-farey-pair-retains-normalized-spectral-separation.md`, inspected at revision `809f087260c8ba8f546e028f5701d1c5938ddd42`, for the normalized sine laws, exact finite-mode witness, positive energy limits and full-discrepancy transfer of the local FD-333 pair. Include its adjacent `research/visual_exploration/findings/VIS-461-one-quantum-farey-pair-retains-normalized-spectral-separation.review.md` if present. Recheck the current finding/review state and reconstruct the argument independently, including its explicit normalization caveat for FD-333. This read-only grant covers no other Visual files, Mind, graph, clue inbox or recursive dependencies. The destination's own FD-333/344 supply the source construction and erasure definitions.

## Evidence boundary

No energy-matched collision, uniqueness theorem, stability rate or asymptotic separation for this conditioned record is established. FD-344 proves the erasure boundary without retaining energy; VIS-461 proves spectral separation with unequal limiting energies. Classical checksum recovery, Parseval and magnitude ambiguity motivate the test but do not decide the realizable Farey subclass. These are artificial labeled-edge reassemblies, not alternative genuine Farey sequences. No new general phase-retrieval theorem, novelty claim, formal verification or RH consequence is asserted.
