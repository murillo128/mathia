---
id: RG-farey-transport-relative-energy-and-variation
type: research-graph-relation
derived: true
---

# Farey transport: relative energy and rank variation

[[research/farey_discrepancy/graph/farey-discrepancy|Farey Discrepancy]] · [[research/visual_exploration/graph/visual-exploration|Visual Exploration]]

This mechanism follows the explicit dependency passages in [[research/visual_exploration/findings/VIS-465-capped-variation-tariff-for-farey-transport-spectrum|VIS-465]] and the surviving synthesis [[research/visual_exploration/mind/intuition/MI-071-farey-spectral-transfer-pays-relative-energy-and-rank-variation|MI-071]]. Its two controls have different denominators.

- [[research/farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum|FD-320]], equations (1)–(4), gives `y=P_sigma D+v`, transport energy `T=||v||²`, and absolute all-mode error `E=||D||²=o(1)` for complete prime-Farey excursion permutations. The block displacement comes from cumulative excursion lengths. Absolute smallness does not by itself determine normalized energy allocation when `T` also vanishes.
- [[research/visual_exploration/findings/VIS-447-uniform-normalized-farey-transport-spectrum|VIS-447]], equations (1)–(3), bounds the total-variation distance between normalized sine-energy distributions by `min(1,sqrt(E/T))`, for `T>0` and `y!=0`. It controls every mode subset simultaneously. A null-normalized statistic additionally divides by that null's own expected band fraction.
- VIS-465, equations (1)–(4), applies [[research/prior_art/incremental/PA-bounded-variation-fourier-decay|classical bounded-variation Fourier decay]] through exact finite summation by parts. With zero endpoints, `V=sum |v_j-v_(j-1)|` and `R=N V²/T`, the high-band share is at most `min(1,B_q) <= min(1,R/(2q))`. The independent Parseval cap does not assert `B_q<=1`: the source's exact `N=3`, `v=(1,-1)`, `q=1` control has `B_q=16/9` and tail one. Combining the two source inequalities gives tail at most `min(1,R/(2q))+min(1,sqrt(E/T))` for the reassembled discrepancy.

## Explicit controls and scope

VIS-465 applies this sufficient condition to [[research/farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy|FD-319]] and [[research/farey_discrepancy/findings/FD-322-three-near-one-farey-index-defects-carry-macroscopic-energy|FD-322]]: their positive limiting transport energies and bounded roughness give low-band saturation for every divergent full-mode cutoff. The reflected control has `R->16`; the unreflected control has limits `32` or `64/3` in its two prime residue classes. This recovers an established consequence through variation, not a new arithmetic estimate.

[[research/visual_exploration/findings/VIS-032-reflection-null-sublinear-band-saturates-green-energy|VIS-032]] uses the first `q` even modes; in the reflected case this means full cutoff `2q` and roughness term `R/(4q)`. [[research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization|VIS-034]] separates total-energy suppression from allocation relative to the null. An unreflected control needs the full sine basis and its own comparator normalization.

Large roughness is necessary, not sufficient, for transport-dominated depletion. Genuine Farey order has `T=0` and lies outside this normalized transport comparison. These are labeled-edge reassemblies, not alternative genuine Farey sequences. The cap correction, source linking and classical-method registration create no frontier episode and change no Atlas state or mass.
