---
id: CLUE-prime-lattice-stratified-random-starts-prime-variance
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-536-stratified-random-starts-reduce-the-mobius-variance-sample-exponent.md
  - research/prime_lattice/findings/PL-478-geometric-coverage-retains-sparsely-sampled-prime-variance.md
  - research/prime_lattice/findings/PL-480-prime-supported-interval-recovery-has-sharp-inverse-query-rate.md
---

# Does stratification retain the prime variance criterion with cube-root-many starts?

## Observation

MC-536 proves an almost-sure Möbius criterion using one uniform integer
start from each of `q_X=ceil(X^(1/3))` balanced cells in
`I_X={X,...,2X-1}`, independently in two macroscopic window channels.
The source is fixed before sampling. For a fixed real sequence with
jump bound `A` and a uniformly bounded mean-zero `C^1` test, its
cell-integrated deterministic weights remove every fitted constant
exactly. The complete pairing has bias `O(A X/q_X^2)` and fluctuation
proxy `O(A^2 X^2/q_X^3)` when the window length is comparable to `X`.
Summable concentration gives all-integer-scale control almost surely.
The rate is classical stratified quadrature, not random Möbius signs.

PL-478 already supplies the destination ingredients: for
`a_n=Lambda(n) 1_(n=1 mod 5)`, the window sums have jump bound
`log(3X)`, two complete mean-zero tests have uniform first-derivative
bounds, and their sum detects any strict-right zero of the four mod-5
functions by a term of size `X^beta`. Its independent converse uses
the joint-GRH pointwise prime-counting estimate. The published sparse
criterion uses a deterministic square-root grid.

PL-480 proves deterministic minimax recovery rate `Theta(X/(q+1))`
for unknown prime-supported positive relative reweightings with fixed
block mass, on each range `q<=X^(1-epsilon)`. Its indistinguishable
controls are constructed against a deterministic query transcript.
It does not give a randomized lower bound for a source fixed before
the draws. Thus that result does not itself rule out this transfer.

## Research question

Fix `H_X=floor(X/20)`, `L_1=H_X`, `L_2=floor(sqrt(2)H_X)` and
`q_X=ceil(X^(1/3))`. Partition `I_X` into the balanced consecutive
cells with endpoints `X+floor(bX/q_X)`. In each channel choose one
uniform integer `R_(i,X,b)` per cell, independently across cells,
channels and scales, under a law independent of the prime values and
zeros. Put

`S_L(j)=sum_(j<n<=j+L) a_n`,

`Q_i(X)=min_(c in R) sum_b |S_(L_i)(R_(i,X,b))-c|^2`.

Is joint GRH for zeta and the three primitive nonprincipal mod-5
functions equivalent, on a probability-one set of sampling outcomes,
to existence of one unbounded integer scale set `mathcal X` on which
both `Q_i(X)/q_X <<_epsilon X^(1+epsilon)` hold for every positive
epsilon? The scale set may depend on the realized observations but
must be common to both channels and fixed before epsilon varies.
Constants may depend on the outcome and epsilon, uniformly along
that set. No uniform assertion over sources chosen after sampling
is intended.

## Why it may matter

This tests whether the shared smooth-pairing interface admits the
same smaller observation count after paying the prime jump logarithm.
A successful transfer would refine the measurement requirement while
preserving the independent arithmetic energy obligation. It would
also separate the deterministic reweighting obstruction from a
fixed-source probability guarantee, without treating random sampling
as an arithmetic cancellation law.

## Decisive test

Reconstruct MC-536's finite covariance and concentration argument with
`A=log(3X)`. For each destination test `f_(i,X)`, use
`W_(i,b)=integral_(cell b) f_(i,X)(y/X) dy` and
`P_hat_i=L_i^(-1) sum_b W_(i,b) S_(L_i)(R_(i,X,b))`.
Check `sum_b W_(i,b)=0` before subtracting the random sample mean.
Point-evaluated weights need not have that property; uniform sampling
does not remove the within-cell covariance bias.

The proposed first target is an all-large-integer-scale error bounded
almost surely by

`O_phi(log(3X) [X^(1/3)+sqrt(X log X)])`.

Verify the bias, both real-coordinate tail bounds and summability
with the growing jump bound. Then pair with PL-478's complete
arithmetic tests, including its `O(log X)` rounding error. The desired
off-critical lower floor is

`sum_i sqrt(Q_i/q_X) + log(3X)[X^(1/3)+sqrt(X log X)] >>_rho X^beta`.

This is a target to prove or refute, not an imported prime theorem.
Keep the prime logarithmic-derivative multiplicity weights; do not
copy the reciprocal-zeta logarithmic pole factor. Obtain the reverse
implication from the prime-counting estimate with center `L_i/4`,
not from a complete mean square. State the probability-one event
and the order of source, zero/test, sample, scale-set and epsilon
quantifiers explicitly. Controls should include unequal/singleton
cells, a constant signal, empirical centering and a source chosen
after the draws, the last of which lies outside the asserted guarantee.

Compare the resulting statement with the classical stratified
quadrature and Hoeffding inputs already identified in MC-536 and the
destination's deterministic recovery results. Classicalization of the
transfer is a valid outcome; neither optimality nor new Monte Carlo
theory is required.

**Bounded source reading for Prime Lattice:** read only
`research/mobius_cancellation/findings/MC-536-stratified-random-starts-reduce-the-mobius-variance-sample-exponent.md`,
inspected at revision `a6f2eb6120810f6869822cef7afa9cc40a2b2daf`,
for its finite mean-removing quadrature, covariance bias, concentration
and probability quantifiers. Include its adjacent
`research/mobius_cancellation/findings/MC-536-stratified-random-starts-reduce-the-mobius-variance-sample-exponent.review.md`
if present. Check current source/review status and reconstruct those
steps independently. Its Möbius analytic dependencies are not needed
or authorized by this grant: the destination's own PL-475/476/478
supply the prime tests and converse. This read-only grant permits no
other source-line findings, recursive dependencies, Mind, graph or
clue-inbox traversal.

## Evidence boundary

MC-536 establishes the Möbius statement; PL-478 establishes the
deterministic prime criterion; PL-480 establishes deterministic
minimax recovery over a reweighting class. None is being cited as an
already proved stratified prime criterion. No prime energy ceiling,
randomized minimax optimality, adaptive-sampling guarantee, effective
zero-uniform onset, finite GRH decision procedure, novelty, formal
verification or zero-exclusion result is asserted by this clue.
The retained energy premise remains an arithmetic hypothesis even
if the observation transfer succeeds.
