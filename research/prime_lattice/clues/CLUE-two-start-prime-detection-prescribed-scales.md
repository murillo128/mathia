---
id: CLUE-prime-lattice-two-start-prime-detection-prescribed-scales
type: research-clue
status: resolved
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales.md
  - research/prime_lattice/findings/PL-482-small-empirical-energy-permits-quarter-power-prime-observations.md
  - research/prime_lattice/findings/PL-483-fixed-prime-supported-sources-evade-subquarter-uniform-observations.md
---

# Can two prime-window starts detect every strict-right pole on prescribed fourth-power scales?

## Observation

MC-539 trades observations per scale for mandatory scale coverage. For a
fixed real population of size `X`, jumps at most `A`, independent uniform
indices `J,K`, dispersion `D=E|u_J-u_K|`, and
`p_T=Pr(|u_J-u_K|>T)`, its self-contained finite lemma proves

`D <= 2T + A X p_T^2 + A p_T`.

Its Möbius pole certificate forces dispersion of order at least `X^beta`
in one of the two macroscopic window channels at every sufficiently large
block, for any hypothetical zero with `beta>1/2`. With bounded jumps,
independent pairs detect that dispersion infinitely often on `X_k=k^4`.
The resulting two-start energy criterion requires every sufficiently late
prescribed scale. It does not permit a favorable post-selected subsequence.

PL-482 already supplies the prime-side complete mean-zero pairings, jump
bound `A_X=log(3X)`, and separate joint-GRH converse. PL-483 supplies a
different boundary: positive fixed prime-supported reweightings agree
with the baseline's sampled windows eventually on `4^k`, while their
signed targets differ. Their common energy is not proved small, and
their source need not retain the canonical logarithmic-derivative pole
formula. Geometric-scale invisibility therefore does not settle the
proposed prescribed polynomial-scale criterion.

## Research question

Fix `a_n=Lambda(n) 1_(n=1 mod 5)`,
`S_L(j)=sum_(j<n<=j+L) a_n`, and `X_k=k^4`, `k>=3`.
Set `L_1=floor(X_k/20)` and `L_2=floor(sqrt(2)L_1)`.
In each channel take two uniform starts `R_(i,k,1),R_(i,k,2)` in
`{X_k,...,2X_k-1}`, with replacement, with all draws independent
including across scales. Fix this law before examining source values
or zeros, and retain coincident draws. Define

`V_i(k)=|S_(L_i)(R_(i,k,1))-S_(L_i)(R_(i,k,2))|^2/4`.

On a probability-one set of outcomes, is joint GRH for zeta and the three
primitive nonprincipal mod-5 functions equivalent to

`for every epsilon>0, V_i(k) <<_(epsilon,omega) X_k^(1+epsilon)`

for both channels and all sufficiently large `k`? The constants and
onset may depend on the outcome; the whole sequence is prescribed before
sampling. There is no post-selected unbounded set in this question.

## Why it may matter

This distinguishes a genuine observation trade from the claim that the
quarter-power per-scale count is intrinsically necessary. It would leave
the actual prime energy premise unproved. The resolved quarter-power
clue has a different sampling law and scale quantifier; this question
does not reopen its established result. Classicalization of this
composition is a valid outcome, without a new probability or novelty claim.

## Decisive test

Reconstruct MC-539's finite pair-tail lemma with the growing prime jump
bound. Compose it with PL-482 §3's deterministic complete pairings to
derive or refute the candidate detection rate

`Pr(max_i V_i(k)>X_k^(2 gamma)) >>_rho
 X_k^(-(1-beta)/2)/sqrt(log(3X_k))`,

for each fixed `1/2<gamma<beta`. Check explicitly whether its sum
diverges on `X_k=k^4`, then justify the independent-repetition step and
the countable probability-one intersection. The channel carrying the
dispersion may change with the scale. Arithmetic window values themselves
are not independent; only the observation draws are.

Keep the positive prime pole weights and `O(log X)` rounding error from
PL-482. Do not import a reciprocal-zeta multiplicity logarithm. Obtain
the converse separately from the joint-GRH pointwise prime-counting
estimate with center `L_i/4`. Constants, repeated draws, endpoint
extrema, and the sample-mean factor `1/4` must survive the dictionary.
Test why replacing the full prescribed sequence by selected favorable
scales invalidates this proof, and compare PL-483's geometric-scale
control without assuming its unknown baseline energy is small.

**Bounded source reading for Prime Lattice:** read only
`research/mobius_cancellation/findings/MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales.md`,
inspected at revision `003b948d3ccdccce8e5d87a8f82ba3ee45cfea87`,
for §1's finite lemma, §3's independent-repetition quantifiers, §4's
generic scale boundary, and its classical probability/optimal-recovery
comparison. Also inspect the exact adjacent
`research/mobius_cancellation/findings/MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales.review.md`
if present. Check current source and review state and reconstruct these
arguments independently. No recursive source-line dependencies, other
findings, Mind, graph, or clue inbox are authorized. The destination's
PL-482 supplies its own analytic pairings and converse, so MC-539's
Möbius analytic dependencies are unnecessary.

## Evidence boundary

MC-539 establishes the Möbius theorem and finite lemma; PL-482 establishes
the quarter-power prime criterion; PL-483 establishes its stated
fixed-source signed-recovery control. The prime two-start theorem and
displayed detection rate are proposed tests, not a Master result.
Classical Borel–Cantelli and Lipschitz hidden-area arguments are already
identified in those sources; the owner must audit the composition and
closest prior art before promoting an outcome.

No prime energy ceiling, finite GRH decision procedure, computational
speedup, optimal actual-source scale sequence, dependent-sampling
guarantee, full uncentered second moment, or covariance-cone positivity
is established here. MC-539's faster-polynomial-scale tents are generic
populations, not one prime source. Neither those tents nor PL-483 settle
optimality of this proposed criterion. No formal verification or
independent adversarial approval is asserted.

## Research disposition

Outcome: supported

Resolved by:
- [[research/prime_lattice/findings/PL-484-two-random-starts-detect-prime-poles-on-fourth-power-scales]]

The prime jump envelope contributes `1/sqrt(log(3X))` to the pair-tail
lower bound, whose sum still diverges on `X_k=k^4` for every strict-right
zero. Independent repetitions and the separate mod-5 GRH pointwise
converse prove the stated almost-sure equivalence on the full prescribed
sequence. The finite lemma and probability mechanism are classical/reused;
no prime-energy ceiling or optimal actual-prime sampling claim follows.
Generic tents explain both the faster-polynomial coverage boundary of
this inference and why favorable unbounded subsequences are insufficient.
