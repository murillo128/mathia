---
id: CLUE-analytic-frontier-montgomery-taylor-near-extremizer-rigidity
type: research-clue
status: proposed
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/clues/CLUE-even-moment-radial-coercivity.md
  - research/analytic_frontier/findings/ANF-059-exact-montgomery-taylor-curvature-transform-shrinks-the-five-point-separation-annulus.md
  - research/analytic_frontier/findings/ANF-062-validated-interval-certificate-proves-montgomery-taylor-five-point-zero-freeness.md
  - research/analytic_frontier/findings/ANF-063-endpoint-anti-concentration-closes-all-moment-orders-from-nine.md
---

# Do all near-minimizers approach two rigid one-pair boundary families?

## Observation

Independent compute execution of [issue #122](https://github.com/murillo128/mathia/issues/122#issuecomment-5556155381) certified

`P_n(t)=M_n(t)+[2^(2n−1)/(1+2^(2n−1))]M_n(0)>0`

for every real `t` and all seven residual orders `n=2,3,4,5,6,7,8`, with the exact Montgomery–Taylor spectrum. This is computer-assisted evidence: Arb/FLINT enclosures of derivatives of `G²`, the analytic bound `|(M_n/M_n(0))'|≤2π`, and twice-integrated analytic Fourier tails cover the full frequency line. Tail cutoffs are respectively `4,5,6,7,8,9,10`; the rational compact covers inspected 601 cells, produced 304 positive leaves, and left none unresolved. Successful leaves used 128-bit arithmetic; undecided parents were reevaluated at 256 and 512 bits before splitting. The linked issue comment preserves the full reproduction specification, bounds, controls, and cover hashes. No order `n≥9` was recomputed.

The strict global bound `P_2(t)>ε`, with `ε=0.00082277`, contains information beyond closing the accepted parent's moment condition. Combining it with that parent's series bridge and the separately persisted `ANF-063` gives the quantitative remainder

`H_MT ≥ c_* S + 2π⁴ ε S²`,

where `S=y1²+y2²`, `K=M_1`, `k_*=inf_t K(t)`, and `c_*=2π²[2K(0)+3k_*]`. Indeed, put `A_2=y1⁴+y2⁴` and `B_2=(y1+y2)⁴+(y1−y2)⁴`. The fourth-moment bracket in the series is at least `ε(A_2+B_2)`, its prefactor is `(2π)⁴/4!`, and `A_2+B_2=3S²+6y1²y2²≥3S²`. The value `ε` is certified enclosure slack, not a sharp moment minimum.

Restoring the horizontal linkage discarded by the independent moment bounds exposes a second structure. Label the larger-height pair by `h`, the other by `l`, and put `r=y_l²/S≤1/2`, `d=t_h−t_l`, and `g(t)=K(t)−k_*`. The quadratic part of the normalized excess `E=H_MT/S−c_*` is exactly

`2π²[(1−r)g(t_h)+r g(t_l)+2g(d)]`.

Thus approaching the sharp value requires simultaneous compatibility of curvature minima, not just separately small scalar bounds. `ANF-059` excludes `K≤−K(0)/3` outside `0.545<|t|<1.01`. That signed annulus contains no additive triple `u,v,u−v`: same-sign differences have magnitude below `0.465`, while opposite-sign differences exceed `1.09`.

## Research question

Does `K` have exactly one positive global minimizer `τ`, with `K''(τ)>0`, and does this yield the complete stability law

`E ≍ S+r+min_{σ,η∈{−1,1}}[(t_h−στ)²+(d−ητ)²]`

for all genuine configurations with sufficiently small `E`, with fixed positive comparison constants depending only on the Montgomery–Taylor profile?

This predicts two boundary families for the disappearing pair: `t_l→0` when `σ=η`, and `t_l→±2τ` when `σ=−η`. It also predicts the rates `S=O(E)`, `r=O(E)`, and horizontal deviations `O(√E)`. The accepted parent asks for the sharp bound and radial monotonicity and exhibits one approaching family; it does not classify all near-minimizers or establish this stability law.

## Why it may matter

The new question would turn a sharp infimum into a complete description of how it can be approached. It isolates a one-dimensional curvature-landscape test governing the remaining geometric degeneracy, including a second boundary family hidden by the separate moment bounds.

## Decisive test

Using the exact `ANF-059` transform, first certify a value below `−K(0)/3`, then determine every global minimizer in the resulting signed annulus and test nondegeneracy. More than one positive global minimizer or a degenerate minimum kills the proposed two-family quadratic law as stated.

If the curvature test succeeds, combine the displayed exact quadratic excess with the certified quartic remainder to prove the lower comparison. Obtain the upper comparison from a uniform local height expansion near each branch, and construct approaching sequences showing the stated rates are sharp. Check the `t_l→±2τ` branches explicitly. No new five-point sign certificate is needed.

## Evidence boundary

The seven all-frequency moment inequalities are validated computer-assisted evidence, distinct from ordinary numerical searches. The all-order conclusion additionally uses `ANF-063`; the all-height remainder uses the accepted parent's series identity. Neither the finite certificate margins nor their minimizing cells identify curvature minimizers, establish their uniqueness or nondegeneracy, or prove the proposed complete stability law. The annulus becomes a constraint on global minimizers only after verifying that the minimum lies below its stated threshold. The clue concerns the fixed five-point Montgomery–Taylor profile and makes no assertion about another spectrum, larger multisets, or RH.
