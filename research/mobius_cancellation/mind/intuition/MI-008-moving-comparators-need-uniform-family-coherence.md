# MI-008 — Quadratic comparator freedom collapses under positive feedback; the surviving route is genuinely coupled signed cancellation

**Evidence level:** supported by MC-053--MC-072; exact for the convolution/inverse/block identities and literature-backed for Burgess/Munsch, Siegel--Walfisz, large-sieve, Landau--Page, and Siegel inputs

## Core intuition

Allowing a quadratic comparator to move with scale does not leave a broad positive-feedback search corridor. The feedback condition forces an extreme arithmetic bias, and the current analysis now pushes the positive triangle architecture beyond the square-root conductor range at power scale. Even the possible Landau--Page exceptional character does not rescue it below `q=X^(2-o(1))`.

The obvious signed escape is also sharply constrained. Inverting the feedback kernel is exact, but standalone cancellation of that inverse, or even of its first dyadic annulus, already carries the zeta and Dirichlet-`L` zero-free burden. The live mechanism is therefore **joint signed cancellation in the complete recovery sum**, not a better positive budget or an independently controlled inverse kernel.

## Strongest justified principle

MC-053--MC-065 establish the family/transfer gate: useful quadratic fits require conductor growth and pay explicit squarefree-character transfer costs. MC-066 identifies the exact positive feedback kernel `h_chi=1+mu^2 chi`; because `h_chi>=0`, triangle closure is controlled by the weighted mass `R_theta(X;chi)`.

MC-067--MC-069 show that this mass cannot be small for ordinary low conductors: polylogarithmic and stretched-exponential motion is excluded, the large sieve leaves only `O(log X)` prime-conductor candidates below square-root scale, and Landau--Page reduces the quasi-subpower range to at most one exceptional primitive character.

MC-070 closes that exceptional positive corridor much further. The mean of `h_chi` is proportional to `L(1,chi)`, and Siegel's lower bound implies `R_theta>1` uniformly for every fixed `theta<=1-eta` and `q<=X^A`, `A<2`, once `X` is sufficiently large. Thus positive contraction requires `q>=X^(2-o(1))`. Combined with the Munsch/Burgess comparator estimate, the exact package cannot certify a fixed exponent below `theta=7/8`.

MC-071 then computes the signed Dirichlet inverse `k_chi` exactly. Its Dirichlet series is

`K_chi(s)=L(2s,chi^2)/(zeta(s)L(s,chi))`.

A square-root-scale bound for its partial sums therefore implies RH for `zeta` and GRH for the comparator `L`-function; coefficientwise absolute inversion converges only for `Re(s)>1`. MC-072 shows that localization does not make this burden cheaper: the first reciprocal block is `K_chi(X)-K_chi(floor(X/2))`, and a power bound on those dyadic increments telescopes back to the same zero-free conclusion.

## What remains possible

A continuation of this quadratic architecture must preserve cancellation **between** `k_chi(d)` and `F_chi(X/d)`, between reciprocal blocks, or in an equivalent coupled recurrence. It cannot first prove RH-scale control of `k_chi` or its leading annulus as an independent input. Positive triangle feedback is already methodically exhausted below near-square conductor, while the signed inverse is only useful if its cancellation is inseparable from the comparator values it weights.

Alternative comparator classes remain logically possible, but each must expose its own transfer, feedback, complexity, turnover, and signed-coupling resources rather than inherit the quadratic conclusions by analogy.

## Status / novelty

The character-sum, large-sieve, exceptional-zero, Siegel, Dirichlet-series, and dyadic-telescoping ingredients are classical. The synthesis is the frontier reduction: **moving quadratic comparators no longer offer an ordinary positive-feedback escape; the remaining information must live in a coupled signed recovery that cannot be factored into separately bounded pieces**.

## Falsification criterion

Exhibit a fixed `A<2`, `eta>0`, and arbitrarily large `X` with a prime quadratic comparator in `q<=X^A` satisfying the positive contraction `R_theta<1`, contradicting MC-070; or give a standalone subcritical power bound for the inverse kernel/first dyadic annulus without the corresponding zeta and Dirichlet-`L` zero-free consequence, contradicting MC-071/072.

## Lean-formalizable core

- Exact signed convolution feedback and inverse identities.
- Positive feedback mass lower bound from the kernel mean.
- Method-specific `7/8` certification floor.
- Inverse-kernel Dirichlet-series factorization.
- Dyadic-annulus telescoping to full inverse partial sums.
- Logical distinction between standalone inverse control and coupled signed recovery.
