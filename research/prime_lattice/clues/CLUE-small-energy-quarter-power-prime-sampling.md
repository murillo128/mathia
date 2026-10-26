---
id: CLUE-prime-lattice-small-energy-quarter-power-prime-sampling
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.md
  - research/prime_lattice/findings/PL-481-stratified-random-starts-retain-the-prime-variance-criterion.md
  - research/prime_lattice/findings/PL-480-prime-supported-interval-recovery-has-sharp-inverse-query-rate.md
---

# Does small empirical energy permit quarter-power-many prime observations?

## Observation

PL-481 resolves the cube-root stratified transfer: deterministic
cell-integrated weights remove the empirical center, and concentration
recovers the complete prime pole tests with the jump price `log(3X)`.
The resulting paired sample-energy condition is almost surely equivalent
to joint GRH modulo 5. No energy ceiling is established independently.

MC-537 uses a different observation law and a different recovered object.
For a fixed real population `u_1,...,u_X` with jumps at most `A`, draw
`2q` independent uniform indices with replacement. Let `V` be their
ordinary empirical variance and
`D=X^(-2) sum_(j,k) |u_j-u_k|` the population mean absolute dispersion.
For `t>0` and `r=min(X,ceil(Xt/(2q)))`, its finite lemma gives, with
probability at least `1-3 exp(-t)`,

`D <= (4+16t/sqrt(q)) sqrt(V) + 16 A r t/q`.

Pairwise differences remove the center; hitting neighborhoods of fixed
population extrema bounds the unknown range on the same event. Every
bounded mean-zero pairing is then controlled simultaneously by `D`.
With bounded `A`, `q=ceil(X^(1/4))` and summable failure probabilities,
MC-537 obtains the Möbius RH-equivalent observation criterion. It does
not recover the complete second moment. Its generic tent obstruction
below exponent `1/4` concerns this uniform sampling law, not Möbius
optimality or a common arithmetic coefficient realization.

## Research question

For `a_n=Lambda(n) 1_(n=1 mod 5)`, set
`S_L(j)=sum_(j<n<=j+L) a_n`, `H=floor(X/20)`,
`L_1=H`, `L_2=floor(sqrt(2)H)`, and `q=ceil(X^(1/4))`.
In each channel sample `2q` independent uniform starts in
`{X,...,2X-1}`, with replacement, independently across channels and
integer scales under a law fixed before consulting prime values or zeros.
Retain repeated draws with their multiplicities and define

`V_i(X)=min_(c in R) (2q)^(-1) sum_a |S_(L_i)(R_(i,X,a))-c|^2`.

Is joint GRH for zeta and the three primitive nonprincipal mod-5
functions equivalent, on a probability-one set of outcomes, to existence
of one unbounded integer scale set on which both
`V_i(X) <<_(epsilon,omega) X^(1+epsilon)` hold for every `epsilon>0`?
The scale set may depend on the observations but must be common to both
channels and fixed before epsilon varies. The arithmetic source is fixed
before all draws.

## Why it may matter

The resolved stratified clue controls quadrature error without using a
small observed energy. This tests whether the energy premise itself
reduces the destination's observation requirement. It is a distinct
sampling law and proof obligation, not a reopening of that resolved clue.
Either outcome should leave explicit the independent task of proving
the actual prime energies. PL-480's controls chosen against deterministic
query transcripts do not settle a fixed-source probability guarantee.

## Decisive test

Reconstruct MC-537's finite range/dispersion argument with the growing
jump bound `A_X=log(3X)`. At `t=4 log X`, test the candidate all-large-
integer-scale bound

`D_i(X) << sqrt(V_i(X)) + sqrt(X) (log X)^3`

almost surely. Verify the failure probabilities, repeated draws,
endpoint extrema, constant signals and empirical centering. The range
bound must be inserted after the concentration event is proved with the
fixed true range; a random range cannot silently enter that theorem.
Check that the event controls all bounded mean-zero weights at once.

Compose only with the destination's complete mean-zero pole pairings in
PL-481 §3, including their `O(log X)` rounding error. The proposed floor
is `sum_i sqrt(V_i(X)) + sqrt(X)(log X)^3 >>_rho X^beta` for a
hypothetical strict-right zero. Retain the positive multiplicity weights
of the logarithmic derivatives, without importing the reciprocal-zeta
factor `(log X)^(m-1)`. Obtain the converse separately from the
joint-GRH pointwise prime-counting estimate with center `L_i/4`.
State the probability-one event and the source/sample/scale-set/epsilon
quantifiers explicitly. Compare the method with the classical
concentration and empirical-variance sources identified in MC-537;
classicalization is a valid outcome.

**Bounded source reading for Prime Lattice:** read only
`research/mobius_cancellation/findings/MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.md`,
inspected at revision `f91ecb829f0b0d247fdc767f48ad4ed09bcde0f7`,
for its self-contained finite lemma (§1), simultaneous pairing recovery
(§2), and generic lower-exponent boundary (§4). Include its exact adjacent
`research/mobius_cancellation/findings/MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.review.md`
if present. Check current source and review state and reconstruct these
arguments independently. No other source-line finding, recursive
dependency, Mind, graph or clue inbox is authorized. The Möbius analytic
dependencies are unnecessary: the destination supplies its own pole
tests and prime-counting converse.

## Evidence boundary

MC-537 proves the generic finite dispersion lemma and its Möbius
application; PL-481 proves the cube-root stratified prime criterion.
The quarter-power prime composition above is a target to validate, not
an established destination theorem. Neither result supplies the prime
energy premise, complete uncentered variance, a finite GRH decision
procedure, effective zero-uniform onset, adaptive sampling, randomized
minimax optimality for prime data, or a guarantee for sources selected
after the draws. No novelty or formal-verification claim is made.
