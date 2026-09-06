---
id: CLUE-analytic-frontier-montgomery-taylor-near-extremizer-rigidity
type: research-clue
status: resolved
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/clues/CLUE-even-moment-radial-coercivity.md
  - research/analytic_frontier/findings/ANF-059-exact-montgomery-taylor-curvature-transform-shrinks-the-five-point-separation-annulus.md
  - research/analytic_frontier/findings/ANF-062-validated-interval-certificate-proves-montgomery-taylor-five-point-zero-freeness.md
  - research/analytic_frontier/findings/ANF-063-endpoint-anti-concentration-closes-all-moment-orders-from-nine.md
  - research/analytic_frontier/findings/ANF-064-validated-finite-moments-complete-sharp-montgomery-taylor-radial-coercivity.md
  - research/analytic_frontier/findings/ANF-065-additive-annulus-incompatibility-forces-near-extremizer-pair-disappearance.md
  - research/analytic_frontier/findings/ANF-066-certified-curvature-convexity-completes-two-branch-montgomery-taylor-near-extremizer-stability.md
---

# Do all near-minimizers approach two rigid one-pair boundary families?

## Observation

Independent compute execution of [issue #122](https://github.com/murillo128/mathia/issues/122#issuecomment-5556155381) certified

`P_n(t)=M_n(t)+[2^(2n−1)/(1+2^(2n−1))]M_n(0)>0`

for every real `t` and all seven residual orders `n=2,3,4,5,6,7,8`, with the exact Montgomery–Taylor spectrum. This is computer-assisted evidence: Arb/FLINT enclosures of derivatives of `G²`, the analytic bound `|(M_n/M_n(0))'|≤2π`, and twice-integrated analytic Fourier tails cover the full frequency line. Tail cutoffs are respectively `4,5,6,7,8,9,10`; the rational compact covers inspected 601 cells, produced 304 positive leaves, and left none unresolved. Successful leaves used 128-bit arithmetic; undecided parents were reevaluated at 256 and 512 bits before splitting. The finite result is canonicalized in `ANF-064`; no order `n≥9` was recomputed because `ANF-063` covers that tail analytically.

The strict global bound `P_2(t)>ε`, with `ε=0.00082277`, contains information beyond the all-order sign condition. `ANF-064` combines it with the series bridge to obtain the quantitative remainder

`H_MT ≥ c_* S + 2π⁴ ε S²`,

where `S=y1²+y2²`, `K=M_1`, `k_*=inf_t K(t)`, and `c_*=2π²[2K(0)+3k_*]`. The value `ε` is certified enclosure slack, not a sharp moment minimum.

Restoring the horizontal linkage discarded by the independent moment bounds exposes a second structure. Label the larger-height pair by `h`, the other by `l`, and put `r=y_l²/S≤1/2`, `d=t_h−t_l`, and `g(t)=K(t)−k_*`. The quadratic part of the normalized excess `E=H_MT/S−c_*` is exactly

`2π²[(1−r)g(t_h)+r g(t_l)+2g(d)]`.

Thus approaching the sharp value requires simultaneous compatibility of curvature minima, not just separately small scalar bounds. `ANF-059` excludes `K≤−K(0)/3` outside `0.545<|t|<1.01`. That signed annulus contains no additive triple `u,v,u−v`: same-sign differences have magnitude below `0.465`, while opposite-sign differences exceed `1.09`. `ANF-065` converts this incompatibility into the global bound `E≥2π²Δr+2π⁴εS`, where `Δ=max(0,-K(0)/3-k_*)`.

The controlling computation [issue #124](https://github.com/murillo128/mathia/issues/124) has now certified the missing curvature facts. It proves `K''>1/5` on all `[0.545,1.01]`, isolates the unique positive critical point in `[0.7588064485352071602166,0.7588064485352071602167]`, certifies `K''>1.66` at that root, and places its value strictly below `-K(0)/3`. Combined with `ANF-059` and evenness, the only global minimizers are therefore `±τ`. `ANF-066` reconstructs the exact analytic consequences and proves the full two-sided stability law.

## Research question

Does `K` have exactly one positive global minimizer `τ`, with `K''(τ)>0`, and does this yield the complete stability law

`E ≍ S+r+min_{σ,η∈{−1,1}}[(t_h−στ)²+(d−ητ)²]`

for all genuine configurations with sufficiently small `E`, with fixed positive comparison constants depending only on the Montgomery–Taylor profile?

This predicts two boundary families for the disappearing pair: `t_l→0` when `σ=η`, and `t_l→±2τ` when `σ=−η`. It also predicts the rates `S=O(E)`, `r=O(E)`, and horizontal deviations `O(√E)`.

## Why it may matter

The question turns a sharp infimum into a complete description of how it can be approached. It isolates a one-dimensional curvature-landscape test governing the remaining five-point geometric degeneracy, including a second boundary family hidden by the separate moment bounds.

## Decisive test

Using the exact `ANF-059` transform, first certify a value below `−K(0)/3`, then determine every global minimizer in the resulting signed annulus and test nondegeneracy. More than one positive global minimizer or a degenerate minimum would kill the proposed two-family quadratic law as stated.

If the curvature test succeeds, combine the displayed exact quadratic excess with the certified quartic remainder of `ANF-064` to prove the lower comparison. Obtain the upper comparison from a uniform height-series bound and curvature Taylor control near the signed minimizers, and construct approaching sequences showing that both `t_l→0` and `t_l→±2τ` branches are genuine. This is exactly the route completed in `ANF-065`--`ANF-066`.

## Evidence boundary

The all-order moment inequalities and quartic remainder are canonical evidence in `ANF-063`--`ANF-064`. The pair-disappearance mechanism and additive linkage are canonical in `ANF-065`. The curvature minimizer location, uniqueness and convexity input are computer-assisted, backed by the outward-rounded Arb/FLINT certificate returned through issue `#124`; ordinary numerical optimization or dense sampling would not suffice. `ANF-066` keeps that scalar computer-assisted input separate from the exact derivation of the two-sided stability law.

The resolved result concerns only the fixed five-point Montgomery--Taylor profile. It makes no assertion about another spectrum, larger conjugation-invariant multisets, a stronger pair-correlation theorem, or RH.

## Research disposition

Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-065-additive-annulus-incompatibility-forces-near-extremizer-pair-disappearance.md]]
- [[research/analytic_frontier/findings/ANF-066-certified-curvature-convexity-completes-two-branch-montgomery-taylor-near-extremizer-stability.md]]

`ANF-065` supplies the exact additive-annulus lower bound forcing `S=O(E)` and `r=O(E)` once the threshold crossing is known. Issue `#124` then certifies that the exact curvature transform is strictly convex throughout the residual annulus, has one positive critical point `τ`, and has only the two global minimizers `±τ`. `ANF-066` combines those facts with the all-order height expansion to prove fixed constants `c_-,c_+>0` for

`c_-[S+r+D²] ≤ E ≤ c_+[S+r+D²]`,

where `D²=min_{σ,η}[(t_h−στ)²+(d−ητ)²]`, and explicitly realizes both boundary families. The accepted rigidity prediction is therefore supported as stated. Further work on the same scalar five-point profile would be refinement rather than a new frontier; the line should move to larger configurations or a genuinely richer information carrier.