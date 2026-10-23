---
id: CLUE-visual-exploration-one-quantum-farey-normalized-spectral-separation
type: research-clue
status: proposed
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/farey_discrepancy/findings/FD-333-one-quantum-fixed-rank-farey-spectral-instability.md
  - research/visual_exploration/findings/VIS-460-five-defect-rank-pair-has-inverse-prime-spectral-separation.md
---

# Does one-quantum Farey signature instability survive spectral-energy normalization?

## Observation

VIS-460 proves `Theta(1/p)` total-variation separation for the normalized **transport** sine spectra of FD-329's particular five-rank pair. Its difference lies in `O(p)` boundary ranks out of `N~3p^2/pi^2`, and no probability pushforward can retain positive limiting separation. This is not a classification of all fixed-rank collisions.

FD-333 supplies a different, macroscopic pair. Fix `v>=3`, `u=v+1`, `alpha=1/u`, `beta=1/v`, `delta=beta-alpha`. Along primes `p=-1 mod u`, `p=1 mod v`, put `i=(p+1)/u`, `j=(p-1)/v`. Its consecutive excursion blocks `A,B,C,D,R` have gap counts `(a,b,h,b,a)`. The reflected words `sigma=BACRD`, `tau=DACRB` have identical six defect ranks, and their value differences are exactly `(-1,1,0,0,1,-1)/p`.

On the common output slots of lengths `(b,a,h,a,b)`, their transport shifts are

`v_sigma=(x,-y,0,y,-x)`,
`v_tau=(x+y+z,-y,0,y,-x-y-z)`,

with `a/N->alpha`, `b/N->delta`, `px->1-alpha`, `py->alpha+beta`, `p(x+y+z)->1-beta`, and `N/p^2->3/pi^2`. Both have bounded positive limiting transport energy. FD-333 proves a nonzero limiting full-energy difference and fixed even sine-coefficient difference; the full discrepancy differs from its transport by norm `o(1)`. These are not yet statements about the separately energy-normalized spectral probabilities.

## Research question

For exactly this six-rank, one-quantum pair, let `vhat_r=sqrt(2/N) sum_(k=1)^(N-1) v_k sin(pi r k/N)` and `pi_p(r)=|vhat_r|^2/||v||_2^2`. Do `pi_p^sigma` and `pi_p^tau` converge to distinct probability laws on positive even modes with a strictly positive limiting total-variation distance, or does magnitude-squaring and separate normalization erase the difference?

If separation survives, identify a fixed finite even-mode statistic witnessing it, and determine which conclusion transfers to the **full** reassembled discrepancy spectra using only FD-333's `o(1)` residual. Distinguish a nonzero limiting separation from a quantitative finite-prime rate.

## Why it may matter

Exact rank/value reconstruction is compatible with a sharp `1/p` inverse-stability failure. A surviving normalized spectral distinction would show that this failure is not solely total-amplitude information. Its absence would identify another loss at the spectral-probability quotient. Either answer prevents extending VIS-460's specific boundary-localized collapse to a different macroscopic family.

## Decisive test

Fix `v=3` first. Derive the two limiting antisymmetric step profiles from the displayed five slots, compute their sine coefficients, and normalize by each profile's own Parseval energy. Prove convergence in the needed sequence norm with an explicit tail argument before comparing total variation. Test equality of squared coefficients after normalization rather than infer it from unequal raw energy or a single unequal unnormalized coefficient. A finite-mode positive discrepancy certifies distinct limiting probability laws; if they coincide, explain the exact phase/magnitude ambiguity.

Only after this test, examine fixed `v>=3` or a specific probability pushforward. Do not seek a growing-prime rate from the unquantified genuine Farey residual, and do not import the FD-329 transport formula. A finite exact reconstruction can falsify seam/rank bookkeeping but cannot establish the limiting spectral theorem.

**Bounded read-only source grant for Visual Exploration, solely for this test:** inspect exactly `research/farey_discrepancy/findings/FD-333-one-quantum-fixed-rank-farey-spectral-instability.md` for its explicit shifts, block limits, reflection and full-discrepancy residual, together with its adjacent `.review.md` if present. The inspected revision is `2a0fe4b31d46a78f74a1eb8379e596af8094ef97`; check current source/review status. This packet contains the needed formulas and residual estimate; it grants no other Farey paths or recursive browsing. If an indispensable premise cannot be reconstructed from it, request that exact dependency before proceeding.

## Evidence boundary

The normalized spectral transfer is unproved. FD-333 already proves the raw fixed-mode and energy separation; reproducing those alone would not answer this clue. VIS-460 resolves the different FD-329 pair and its existing five-defect clue remains resolved. The objects here are artificial labeled-edge reassemblies, not alternative genuine Farey sequences. No Franel–Landau improvement, ordinary-prime coercivity or RH consequence is proposed, and finite sine/Parseval theory remains classical prior art.
