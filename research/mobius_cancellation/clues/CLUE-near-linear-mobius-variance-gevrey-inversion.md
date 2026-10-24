---
id: CLUE-mobius-cancellation-near-linear-variance-gevrey-inversion
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows.md
  - research/mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md
  - research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md
  - research/mobius_cancellation/clues/CLUE-multiplicity-aware-sparse-zero-annihilator.md
---

# Does a bounded Gevrey box inverse give a single near-linear Möbius variance criterion?

## Observation

MC-528 resolves the fixed-power reciprocal annihilation question. Given a hypothetical zero `rho_0=beta+i gamma`, `beta>1/2`, of multiplicity `m`, its compact mean-zero test has

`sum_n mu(n) phi(n/X) = X^rho_0 Q_(m-1)(log X) + O_phi(X^sigma_1)`,

with `1/2<sigma_1<beta` and nonzero leading coefficient of `Q_(m-1)`. Unwanted principal parts are killed with their full multiplicities, and a quantitative local product estimate controls division by zeta. A fixed finite box inverse then yields the centered variance floor at each fixed `H=floor X^theta`, `0<theta<1`. That finding explicitly supplies no uniform limit as `theta` approaches one.

PL-472 treats this remaining window issue for the different logarithmic-derivative prime source. The sparse-product test retains Gevrey order `q>1`. For `A_h f(u)=h^(-1) int_0^h f(u-v)dv`, its growing finite Bernoulli inverse `f_h` has common compact support, zero integral, uniformly bounded `L^2` norm, and

`||A_h f_h-phi||_infinity <= C exp(-c h^(-1/q))`.

Choosing `1<q<B` gives its prime variance floor uniformly for `1<=H<=X/(log X)^B`, for every fixed `B>1`. Its explicit formula is applied only to the fixed test `phi`; the moving inverse is controlled in the coefficient domain. The combined test is bounded, but its derivative-bank size grows.

## Research question

For the actual Möbius source, define

`S_(X,H)(y)=M(y+H)-M(y)`, `m_(X,H)=X^(-1) int_X^(2X) S_(X,H)(y)dy`,

`V_mu(X,H)=int_X^(2X)|S_(X,H)(y)-m_(X,H)|^2dy`.

Can MC-528's multiplicity-aware test be proved to retain a Gevrey order permitting PL-472's bounded growing inverse, and thereby establish, for every fixed `B>1`,

`V_mu(X,H) >= c H^2 X^(2beta-1) (log X)^(2m-2)`

for every sufficiently large real `X` and every integer `1<=H<=X/(log X)^B`, with constants uniform in that range?

If so, determine whether the single law `H_B(X)=floor(X/(log X)^B)` and the premise

`V_mu(X,H_B(X)) <<_epsilon X^(1+epsilon) H_B(X)`

on one arbitrary unbounded real scale set `E`, for every fixed `epsilon>0` with constants uniform on `E`, imply RH. Check the converse against MC-520 with the same centering and real-scale conventions; do not silently strengthen an epsilon-loss ceiling to a fixed logarithmic-loss ceiling.

## Why it may matter

This would replace a family of fixed-power selected-scale premises approaching exponent one by one near-linear window law. It would identify the exact strength of that source estimate without pretending to prove it. The resolved annihilator clue already owns the reciprocal growth gate at fixed power; the new discriminator is uniform growing-order inversion and its window quantifiers. It is not another request to solve the same pole-tail problem.

## Decisive test

1. Start from MC-528's coefficient estimate `|p_j|<=C A^j/(j!)^(1/a)`, `a<1`, and reconstruct a derivative bound `||phi^(ell)||_infinity<=C L^ell (ell!)^q` for a choice `1<q<min(B,1/a)`. Track multiplicities, normalization, analytic composition with `log u`, and support. Smoothness alone does not provide the needed uniform bound in `ell`.
2. Reconstruct PL-472's finite inverse with coefficients from `z/(1-exp(-z))` and truncation order of size `h^(-1/q)`. Prove a remainder uniform in both order and `h`, a bounded combined test norm, and exact mean cancellation. A fixed-order big-O with an unspecified order-dependent constant is insufficient.
3. Use `|mu(n)|<=1` to price the coefficient-side error on the same block. Retain MC-528's full nonzero logarithmic polynomial, including a multiple pole with zero ordinary residue; retain endpoint-crossing windows in the exact centered pairing. Apply the reciprocal contour only to the fixed `phi`, avoiding a new unproved uniform contour theorem for moving tests.
4. Compare the resulting floor with the stated ceiling along exactly `E`, and audit the converse from MC-520. State dependence on the entire hypothetical zero set and the lack of effective onset or fixed finite acquisition bank. At `B=1` and `H` comparable to `X`, distinguish failure of this Gevrey error estimate from a mathematical counterexample. Audit classical variance converses and optimal truncation before assigning novelty; a direct specialization of the two persisted arguments should be identified as such.

**Bounded source reading for Möbius Cancellation:** inspect exactly `research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows.md`, Sections 1–3, for preservation of Gevrey order, the uniform finite Bernoulli remainder and the centered coefficient-side transfer. Include the current adjacent `research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows.review.md` if present. Inspected source revision: `f9c4957c71c4198c7b7bef9d9f2a9690e1b8a377`. Recheck current source/review state and reconstruct the estimates independently. This read-only, destination-specific grant is limited to this test; it grants no other Prime Lattice files, directory traversal or recursive dependency reading. MC-528 supplies the destination-local test and reciprocal contour, so PL-471's source proof need not be imported.

## Evidence boundary

PL-472 proves the near-linear statement for its prime logarithmic derivative. MC-528 proves the multiplicity-aware Möbius result at fixed power windows. Their near-linear reciprocal combination and the displayed single-law criterion remain questions here. No variance upper bound, new cancellation estimate, effective test acquisition, sharp boundary at `B=1`, zero-simplicity conclusion, external novelty or RH proof is asserted. A successful transfer would be a conditional criterion with an unpaid arithmetic premise.
