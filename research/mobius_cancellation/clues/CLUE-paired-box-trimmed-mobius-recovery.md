---
id: CLUE-mobius-cancellation-paired-box-trimmed-mobius-recovery
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md
  - research/mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md
  - research/mobius_cancellation/findings/MC-531-bounded-jumps-recover-trimmed-mobius-variance.md
  - research/mind/intuition/MI-040-paired-box-inversion-transports-trimmed-mobius-pole-tests.md
  - research/prior_art/incremental/PA-multichannel-compact-distribution-deconvolution.md
---

# Does paired-box recovery extend the trimmed Möbius certificate to macroscopic lengths?

## Observation

PL-475 changes the measurement operator that caused the single-box obstruction. For `A_h f(u)=h^(-1) int_0^h f(u-v)dv`, compact finite-order distributions give a classical Bezout identity for the box lengths `1` and `sqrt(2)`. Applied to any fixed smooth mean-zero target supported in `(4/3,5/3)`, the dilated identity produces two mean-zero tests in a common compact subset of `(1,2)`, with uniformly bounded sup, first-derivative and L2 norms for `0<h<=1/20`. At integer lengths `H` and `K=floor(sqrt(2)H)`, rounding leaves target error `O(1/X)`. The inverse itself uses no prime-source property.

MC-528 constructs a compatible mean-zero reciprocal-zeta test by choosing its Gevrey bump in the smaller logarithmic support interval. A hypothetical zero `rho_0=beta+i gamma`, `beta>1/2`, of multiplicity `m` contributes `X^rho_0 Q_(m-1)(log X)`, with nonzero leading coefficient. MC-531 separately bounds any complete bounded linear window test from retained energy and a quadratic deletion bill, using the exact jump bound `|S_L(j+1)-S_L(j)|<=2`. Its current canonical theorem uses the single-box near-linear range. Global MI-040 records the proposed composition as conditional synthesis; it has no destination-local finding or independently checked arithmetic upper estimate.

## Research question

Can the destination independently establish the combined certificate for all sufficiently large integer `X` and all integer `1<=H<=X/20`, with `L_1=H`, `L_2=K=floor(sqrt(2)H)`? For separate masks `E_i` in `I_X={X,...,2X-1}`, counts `B_i=|E_i|<X/2`, arbitrary single constants `c_i`, and

`V_i=sum_(j in I_X minus E_i) |M(j+L_i)-M(j)-c_i|^2`,

the candidate is

`(sqrt(X V_1)+B_1^2)/H + (sqrt(X V_2)+B_2^2)/K >= c X^beta (log X)^(m-1)`.

At `H=floor(X/20)`, determine the exact strength of simultaneous bounds `V_i <<_epsilon X^(1+epsilon)L_i` and `B_i <<_epsilon X^(3/4+epsilon)` on one unbounded integer scale set, with the scale set, masks and centers fixed before the epsilon quantifier. In particular, audit the expected RH equivalence against MC-520's complete-moment converse. The question concerns a changed observation requirement, not a proposed proof of either arithmetic bound.

## Why it may matter

This would remove the single-box logarithmic range restriction at the explicit price of a second length, while retaining quantitative missing-start control. It would tell the source-estimate program exactly how strong an almost-all macroscopic variance premise already is. A bound for just one favorable member of the pair, or an unquantified exceptional density, would remain insufficient. The single-box regularity clue is resolved and is not reopened.

## Decisive test

1. Reconstruct PL-475's compact distributional inverse and its uniform smooth-test estimates. Apply them to the actual MC-528 target, retaining full unwanted-pole multiplicities and the selected Laurent polynomial. Check support, zero integrals and integer rounding; the coefficient envelope `|mu(n)|<=1` should charge `O(1)` rather than the prime source's `O(log X)`.
2. Write both exact complete pairings over the same block, including endpoint-crossing windows and separate constant centers. Apply MC-531's discrete lemma to each pairing, without cutting the analytic test by the retained-set indicator. Verify uniformity over masks, centers and lengths, including `H=K` at the smallest length. No independence between the channels is available or needed.
3. Derive the scale and epsilon quantifiers from the resulting inequality. Check the RH converse with empty masks using MC-520, and distinguish the resulting criterion from an independent source estimate. If the composition fails, identify the precise support, norm or analytic compatibility failure; failure of one construction is not a variance counterexample.
4. Retain the rational-common-zero and Liouville-small-divisor controls. Compare the inverse with the registered classical multichannel deconvolution prior art; do not claim a new inversion principle or external novelty. MC-531's bounded-coefficient tent only proves sharpness of generic absolute-mass recovery, not the optimal deletion threshold for this signed Möbius test.

**Bounded source reading for Möbius Cancellation:** inspect exactly `research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md`, Sections 1–3 and its controls, for the source-independent inverse, support, norm and rounding facts. Include its current adjacent `research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.review.md` if present. The exact prior-art packet `research/prior_art/incremental/PA-multichannel-compact-distribution-deconvolution.md` identifies the classical compact-distribution theorem and its scope. Inspected revision: `888edf1a133baad2f4419eee38db4c329903573a`. Recheck current source/review state and reconstruct the transfer independently. This read-only grant permits no other Prime Lattice files, recursive dependencies, or cross-line Mind/inbox browsing. The destination's own MC-528, MC-531 and MC-520 provide the reciprocal contour, deletion lemma and conditional converse.

## Evidence boundary

PL-475 establishes the source-independent inverse and its prime application; MC-528 and MC-531 establish the local reciprocal and missing-start ingredients. The displayed composition is supported by Mind synthesis but is not yet a canonical Möbius finding or an independently approved result. No retained-energy ceiling, exceptional-count estimate, optimal deletion exponent, effective all-zero-dependent test, uniform onset near the critical line, or RH proof is supplied. Changing from one length to two changes the premise and does not contradict the single-box Fourier obstruction. A new criterion alone is not independent progress toward cancellation.
