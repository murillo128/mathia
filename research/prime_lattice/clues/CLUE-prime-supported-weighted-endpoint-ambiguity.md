---
id: CLUE-prime-lattice-prime-supported-weighted-endpoint-ambiguity
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.md
  - research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity.md
  - research/prime_lattice/findings/PL-478-geometric-coverage-retains-sparsely-sampled-prime-variance.md
  - research/prime_lattice/findings/PL-270-finite-weil-source-positive-compression.md
  - research/prime_lattice/findings/PL-271-full-weil-source-tower-projective-identifiability.md
  - research/prior_art/incremental/PA-lipschitz-integration-recovery.md
---

# Does prime-power support prevent hidden weighted primitives between observed endpoints?

## Observation

MC-534 realizes the classical indistinguishable-input obstruction with one common square-free coefficient sequence per control, exact magnitudes `mu(n)^2`, and any prescribed `q<=kappa_phi X` interval observations at sufficiently large `X`. The difference primitive vanishes at every queried endpoint. Nonnegative bridges on a fixed interval where a rotated derivative of the target has one sign retain target separation at least `c_phi X/(q+1)`. Its proof uses the total square-free population in that interval, without assuming density in each observation gap. These signs are not multiplicative.

PL-477 already constructs compatible positive controls with a common mask and signed target separation, but its support fills a residue class rather than the prime powers. PL-478's sparse-grid criterion leaves the actual arithmetic energy ceilings unproved. Thus a concrete remaining distinction is whether the support restriction itself prevents endpoint bridges, before invoking the exact von Mangoldt amplitudes and explicit formula.

PL-270's positive finite-Weil compression and PL-271's full-tower identifiability address another observation operator. They do not supply a target-separation rate for interval queries under a uniform relative amplitude cap.

## Research question

Fix a nonzero complex `phi in C_c^1((4/3,5/3))`, with zero integral if desired, before the integer scale `X`. Choose `[s,t]` compactly inside `(4/3,5/3)`, a unit complex `omega`, and `eta>0` with `Re(-omega phi'(u))>=eta` on that interval; all are fixed with the test. Put `a_n=Lambda(n) 1_(n=1 mod 5)` and `A(t)=sum_(n<=t) a_n`. Given any `q` integer interval queries `(u_l,v_l]`, can one construct real perturbations `d_n`, supported in `(sX,tX]`, satisfying

`|d_n| <= a_n/2`, `sum_n d_n=0`,

`sum_(u_l<n<=v_l) d_n=0` for every query,

yet

`|sum_n d_n phi(n/X)| >= c_phi X / ((q+1) log(3X))`

for all sufficiently large `X` and `q <= kappa_phi X/log(3X)`?

The candidate controls are `b_n^+=a_n+d_n` and `b_n^-=a_n-d_n`. They retain exactly the prime-power support in this residue and positive weights between one half and three halves of the actual weights. Every observed interval value agrees with the actual baseline. The amplitude freedom is real and continuous; exact von Mangoldt coefficients are **not** retained. The logarithmic loss is a proposed first target, not a sharpness assertion.

## Why it may matter

A positive answer would show that support, positivity, bounded relative amplitudes and common-source consistency alone do not give a power improvement in sparse signed recovery. At `q<=X^(1/2-delta)` for fixed `0<delta<1/2`, the proposed separation still exceeds square-root size by a power up to a logarithm. An actual-source improvement would need a restriction beyond this control class. A negative answer would have to identify the support/weight constraint that blocks the bridge, potentially sharpening the arithmetic question left by PL-478.

## Decisive test

1. Reconstruct MC-534's endpoint partition and derivative-phase argument. Replace its unit sign steps by a nonnegative primitive `F(n)=sum_(k<=n)d_k` whose increments obey `|F(n)-F(n-1)|<=a_n/2` and which returns to zero at every queried endpoint. Price the loss at a weighted midpoint explicitly; a unit-sign parity argument does not transfer to unequal logarithmic weights.
2. Test whether total prime weight in the fixed derivative interval, together with `max a_n<=log(3X)` in the modified block, suffices for the displayed lower bound uniformly over all endpoint partitions. Use only a justified unconditional fixed-modulus PNT input for that total weight. Do not assume prime density in every possibly empty or short cell, GRH, or either sample-energy ceiling. Empty cells, a single heavy atom, repeated endpoints and intervals crossing the modified block are decisive controls.
3. Verify positivity, unchanged support, zero total perturbation and exact query equality before summation by parts. Agreement with the actual baseline does not prove that its sampled energies are small. If deterministic adaptive queries are included, first run the policy on that baseline and construct controls against the resulting transcript; no random-seed-dependent input or randomized lower bound is licensed.
4. Compare with PL-477 and the registered classical recovery mechanism. PL-270 allows a different positive reweighting under a finite Galerkin quotient; PL-271 concerns all bands. The additional result sought here is the quantitative signed-target ambiguity under bounded relative perturbations and interval observations. Stop if this precise conclusion is already available; do not create a new finding merely for repeating a general nullspace argument.

**Bounded source reading for Prime Lattice:** read only `research/mobius_cancellation/findings/MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.md`, Sections 1–3 and the deterministic-adaptivity paragraph, for the endpoint-pinned primitive, total-population bound and signed-target conversion. Include its adjacent `research/mobius_cancellation/findings/MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.review.md` if present. Inspected revision: `93eb193b674edc61d061bf2be1973b0deec878a9`. Recheck current source/review state and reconstruct these arguments independently. This read-only grant covers no other Möbius dependency, directory, Mind, graph or clue. The weighted destination assertion must be proved separately.

## Evidence boundary

MC-534 proves the square-free sign construction; PL-477 proves the positive residue-supported common-mask construction; PL-478 proves a conditional actual-prime floor and a GRH-equivalent sampling criterion. None proves the proposed prime-supported weighted bridge. No optimal logarithmic factor, actual-prime sampling lower bound, small baseline energy, Euler product, pole formula for the controls, randomized result, cross-scale fixed-source construction, external novelty, formal verification or RH/GRH progress is asserted. Reweighting actual prime-power locations is a matched control, not another arithmetic prime system.
