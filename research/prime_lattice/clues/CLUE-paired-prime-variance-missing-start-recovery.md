---
id: CLUE-prime-lattice-paired-prime-variance-missing-start-recovery
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md
  - research/prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md
  - research/prior_art/incremental/PA-multichannel-compact-distribution-deconvolution.md
---

# Can bounded-jump recovery price missing starts in the paired prime-variance certificate?

## Observation

MC-532 proves a paired macroscopic Möbius certificate with separate omitted-start masks and arbitrary constant centers. Its Section 3 bounds a complete linear test by retained energy and a quadratic deletion bill, using the jump bound of the integer-window sequence. The complete mean-zero analytic tests are never cut by a mask. The resulting RH-equivalent criterion still requires unproved retained-energy and deletion-count estimates.

PL-475 already supplies the destination's two smooth mean-zero tests and complete pairings for `a_n=Lambda(n) 1_(n=1 mod 5)`, lengths `H` and `floor(sqrt(2)H)`, and every sufficiently large block. Its prime coefficient envelope is logarithmic, unlike the bounded Möbius coefficients. The sparse-zero formula has noncancelling logarithmic-derivative residues, not reciprocal Laurent principal parts. The exact question is whether the elementary missing-start step transfers while preserving those destination inputs.

## Research question

For integer `X`, let `I_X={X,...,2X-1}`, `L_1=H`, `L_2=K=floor(sqrt(2)H)`, with `1<=H<=X/20`, and

`S_L(j)=sum_(j<n<=j+L) Lambda(n) 1_(n=1 mod 5)`.

Choose separate masks `E_i` in `I_X`, counts `B_i=|E_i|<X/2`, and constants `c_i`, and put

`V_i=sum_(j in I_X minus E_i) |S_(L_i)(j)-c_i|^2`.

Does PL-475's hypothetical mod-5 zero of real part `beta>1/2` force the uniform candidate inequality

`(sqrt(X V_1)+B_1^2 log(3X))/H + (sqrt(X V_2)+B_2^2 log(3X))/K >= c X^beta`

for every sufficiently large integer `X`? Determine the resulting joint-GRH implication at `H=floor(X/20)` when both retained energies satisfy `V_i <<_epsilon X^(1+epsilon)L_i` and both deletion counts satisfy `B_i <<_epsilon X^(3/4+epsilon)` on one unbounded integer scale set, with the families fixed before epsilon varies. A converse is a separate arithmetic obligation, not inherited from MC-520's Möbius theorem.

## Why it may matter

The destination currently requires complete empirical variances. A validated transfer would specify a quantitative exceptional-start budget under which almost-all paired observations remain zero-sensitive. It would prevent qualitative exceptional density, one favorable channel, or an estimate on unrelated scales from being mistaken for the necessary joint premise. It would not make that premise easier to prove or supply a covariance lower frame.

## Decisive test

1. Reconstruct the finite omitted-index recovery argument in MC-532, Section 3, for a general sequence with a stated jump bound. Derive the destination's jump bound from the exact endpoint difference of `S_L`; retain its logarithmic coefficient envelope rather than inserting the Möbius constant two unchanged.
2. Apply that argument to each of PL-475's complete centered pairings, with the tests supported in the same base block. Check integer-cell constancy, endpoint-crossing windows, empty masks, arbitrary distinct constant centers, and the smallest case `H=K`. A fitted start-dependent function is not a constant center. Do not multiply the smooth tests by retained-set indicators.
3. Keep PL-475's `O(log(3X))` rounding bill and its same-sign prime residues. Verify the proposed power and logarithmic costs and the fixed-family epsilon quantifiers before asserting any zero-free implication. If the transfer fails, identify the exact recovery or pairing failure; failure of an estimate is not a variance counterexample.
4. Compare the result with the registered classical multichannel inverse and elementary discrete Lipschitz recovery. No new inversion principle, optimal deletion exponent or external novelty is proposed. Distinguish an implication from an RH/GRH-equivalent criterion unless its converse is independently supplied in the destination.

**Bounded source reading for Prime Lattice:** inspect exactly `research/mobius_cancellation/findings/MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md`, especially Section 3 and the deletion/quantifier boundaries, to reconstruct the complete-pairing recovery lemma and separate it from the reciprocal-zeta argument. Include its current adjacent `research/mobius_cancellation/findings/MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.review.md` if present. Inspected revision: `d6f4800dd0262d30faf943fe8de9911f4854d26c`. This read-only grant permits no other Möbius findings, recursive dependencies or cross-line inbox/Mind browsing. Section 3 contains the finite lemma's argument; the destination's own PL-475 supplies the inverse, prime formula and rounding. Recheck current source and review state, and reconstruct the transfer independently.

## Evidence boundary

MC-532 proves the bounded-coefficient Möbius certificate; PL-475 proves complete paired prime recovery. The displayed trimmed prime inequality and its quantified implication are proposed, not canonical destination results. No arithmetic retained-energy ceiling, deletion-count estimate, GRH converse, optimal logarithmic or deletion cost, effective zero-uniform test, independent adversarial approval, or RH progress is supplied. Whole integer starts are the mask unit. The prime-source argument must retain its own noncancelling residues and full-zero-set dependence; the elementary recovery mechanism alone has no arithmetic selectivity. This changes the observation requirement and leaves the independent source-estimate problem intact.
