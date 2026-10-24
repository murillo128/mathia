---
id: CLUE-mobius-cancellation-multiplicity-aware-sparse-zero-annihilator
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block.md
  - research/mobius_cancellation/findings/MC-527-good-height-truncation-isolates-selected-scale-pole-cancellation.md
  - research/mobius_cancellation/findings/MC-526-selected-mobius-variance-excludes-finite-exceptional-zero-clusters.md
  - research/prior_art/incremental/PA-montgomery-dirichlet-zero-density-bound.md
  - research/mobius_cancellation/clues/CLUE-reciprocal-zeta-selected-scale-pole-tail-certificate.md
---

# Can a fixed multiplicity-aware Mellin annihilator isolate one reciprocal-zeta pole?

## Observation

PL-471 closes the actual mod-5 prime source's infinite-pole variance transfer by changing the test, rather than bounding a growing packet's smallest singular value. For a chosen zero `rho_0` with real part `beta>1/2` and fixed `1/2<sigma_0<beta`, arithmetic zero density bounds the unwanted zeros to the right of `sigma_0` by `O(T^a)` for some `a<1`. A genus-zero product of order at most `a`, applied through a convergent derivative series to a sufficiently regular compactly supported Gevrey bump, produces a fixed complex test `phi` in `C_c^infinity((1,2))`. Its Mellin transform satisfies `Phi(1)=0`, `Phi(rho_0)=1`, and vanishes at every other zero in that half-plane. The logarithmic-derivative explicit formula then leaves one mode plus `O(X^sigma_0)`. A fixed finite-order box inverse transfers it to empirical variance on every large block. Constants depend on the whole hypothetical zero set; this is an existence proof, not finite-data acquisition.

MC-527 supplies a different arithmetic contour interface for `1/zeta`: any fixed smooth bank has a complete good-height packet through `T(X) in [X^delta,X^delta+1]`, with grouped remainder `O(X^(-1/2))`. It leaves cancellation inside the growing packet unresolved. A reciprocal pole of order `m_rho` involves every derivative `Phi^(j)(rho)` for `0<=j<m_rho`; one zero of the test at each unwanted location is insufficient. Moreover, MC-527 does not provide an absolutely summable series of reciprocal residues.

## Research question

For a hypothetical zeta zero `rho_0=beta+i gamma` of order `m`, with `beta>1/2`, can a **single fixed test** kill the entire principal part at every other zero with `Re rho>sigma_0`, while retaining `Phi(rho_0)!=0` and a justified smaller contour remainder?

The precise prospective criterion is a compact smooth mean-zero complex test with

`Phi^(j)(rho)=0` for every `rho!=rho_0`, `Re rho>sigma_0`, and `0<=j<m_rho`,

and, for some fixed `sigma_0<sigma_1<beta`, the actual-source asymptotic

`sum_n mu(n) phi(n/X) = X^rho_0 P_(m-1)(log X) + O_phi(X^sigma_1)`.

Here `P_(m-1)` must retain the full selected Laurent contribution, with leading coefficient `c_(rho_0,m) Phi(rho_0)/(m-1)! != 0`; `c_(rho_0,m)` is the highest principal-part coefficient of `1/zeta`. If `rho_0` is nonreal, its conjugate is among the unwanted poles. Real and imaginary test components are admissible real measurements. No rightmost zero, simplicity, uniform multiplicity bound, or finite exceptional family is supplied.

## Why it may matter

This isolates a specific alternative within the accepted pole-tail question: replace an expanding finite packet by one all-zero-dependent test and price its reciprocal contour. Success would test whether the finite-exception restriction in MC-526 is an artifact of the available test, while leaving the independent variance ceiling entirely unproved. It would not construct an arithmetic cancellation estimate from zero data.

The proposed test is distinct from MC-522's resolved all-dyadic recurrence and MC-527's fixed-bank truncation. The accepted parent clue keeps its disposition; this handoff supplies a new exact source-reading packet and a narrower analytic lemma, not another disposition of that question.

## Decisive test

First audit PL-471's product/Gevrey construction with each unwanted zero repeated according to its actual multiplicity. The persisted Montgomery estimate counts multiplicities and covers `q=1`, but the derivative-series convergence, compact support, nonzero selected value, and mean-zero condition still need reconstruction. Do not assume that a formal product times a Mellin transform is itself an admissible compact smooth test.

The next gate is **quantitative division by zeta after those cancellations**. Prove a bound strong enough that the removable continuation of `Phi(s)/zeta(s)` is integrable on a fixed line `Re s=sigma_1`, and that horizontal contour contributions vanish along justified good heights. Alternatively give another rigorous grouped-contour argument yielding the displayed smaller remainder. Analytic removability alone gives no vertical growth estimate; absolute summation of inverse-derivative residues is not licensed. Identify explicitly whether the Gevrey decay can dominate the growth after division, including near arbitrarily clustered zeros. A failed estimate is not a counterexample about zeta; if only an additional growth hypothesis yields the result, state it separately and test whether classical arithmetic bounds supply it.

Only after this gate passes, use a fixed finite-order inverse of the additive box average on the test. Track the coefficient-domain error, derivative norms, and empirical-mean cancellation. For each fixed `0<theta<1`, `H=floor X^theta`, the desired consequence to prove is

`V_mu(X,H) >= c H^2 X^(2beta-1) (log X)^(2m-2)`

at every sufficiently large real `X`, with all constants fixed before `X` varies. This would contradict the diagonal epsilon-loss ceiling on any unbounded measured set when `beta>1-theta/2`. It must not replace that measured set by a convenient sequence of large values elsewhere. Include a multiple-pole control with zero ordinary residue and retain the finite-exception theorem as a check. Audit classical reciprocal-zeta oscillation/converse results before assigning novelty.

**Bounded source reading for Möbius Cancellation:** read exactly `research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block.md`, especially Sections 1 and 4, for the convergent sparse-zero test and finite box inverse. Read exactly `research/prior_art/incremental/PA-montgomery-dirichlet-zero-density-bound.md` for the multiplicity-counted `q=1` input and its scope. Include the current adjacent `research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block.review.md` if present. These sources were inspected at `400495d9bc8f0970fa06ed9f110a0e1e2ac4c21d`; recheck current source/review state and reconstruct the hypotheses independently. This read-only grant is destination-specific and limited to this test. It grants no other Prime Lattice files, directory traversal, or recursive dependency reading. MC-526 and MC-527 are destination-local and supply the reciprocal and centered-window interfaces.

## Evidence boundary

PL-471 proves its logarithmic-derivative result. MC-527 proves good-height truncation, not the displayed one-pole asymptotic. The multiplicity-aware interpolation and, especially, the reciprocal growth bound remain unvalidated here. No infinite-family Möbius exclusion, variance upper bound, effective zero-based test bank, new theorem of oscillation, or RH result is asserted. Dependence on all hypothetical zeros is acceptable for a necessity proof but cannot be relabelled as independently acquired source control. A result conditional on an unpaid growth estimate would remain conditional.
