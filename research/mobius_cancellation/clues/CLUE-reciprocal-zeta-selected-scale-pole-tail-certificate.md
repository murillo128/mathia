---
id: CLUE-mobius-cancellation-reciprocal-zeta-selected-scale-pole-tail-certificate
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-470-positive-source-strip-growth-and-the-infinite-pole-tail-gate.md
  - research/mobius_cancellation/findings/MC-526-selected-mobius-variance-excludes-finite-exceptional-zero-clusters.md
  - research/mobius_cancellation/findings/MC-525-polynomial-strip-growth-forces-pole-variance-on-every-block.md
  - research/mobius_cancellation/findings/MC-522-centered-dyadic-variance-recovers-all-reciprocal-zeta-poles.md
---

# Can a reciprocal-zeta pole-tail certificate go beyond finite exceptional clusters?

## Observation

MC-526 proves that, if zeta has finitely many but at least one zero in a fixed half-plane `Re s>sigma_*>1/2`, then its complete centered window variance satisfies

`V_mu(X,H)>=c H^2 X^(2beta-1)(log X)^(2m-2)`

on every sufficiently large block, for integer `1<=H<=h_0 X`. Here `beta` is the largest real part and `m` the largest multiplicity on that line. Finiteness supplies zero-free high disks and hence polynomial reciprocal growth; a finite mean-zero covariance bank retains all leading Laurent coefficients. A diagonal-order ceiling on any unbounded set of scales therefore excludes finite exceptional clusters, but does not exclude an infinite sparse family.

PL-470 supplies a related quantitative interface for the different source `Lambda(n) 1_(n=1 mod 5)`. Its smoothed logarithmic derivative has an absolutely convergent zero sum, including all multiplicities and the explicit correction for powers of 5. A finite packet's normalized Gram margin yields a variance floor only if the **complete remaining vector** is smaller on the same measured scales. The fixed-test absolute high-tail estimate is only `C_(N,f) X T^(1-N) log(2T)`. Growing the packet changes its Gram margin, derivative seminorms, test norms and admissible window width. The source proves this interface, not the required arithmetic residual bound.

For `1/zeta`, even a simple pole has coefficient `1/zeta'(rho)` rather than a signed multiplicity. Multiple poles require the full Laurent principal part. Neither PL-470's absolute zero-sum convergence nor its logarithmic-derivative contour estimates automatically transfers.

## Research question

Fix `0<theta<1`, `H=floor X^theta`, and an unbounded measured scale set `E`. Suppose hypothetically that zeta has a zero `rho_0` with real part `beta>1-theta/2`, without assuming a rightmost zero, a horizontal gap, simplicity, or finitely many exceptions. Can a justified truncated reciprocal-zeta contour formula and a quantitatively controlled pole packet force a centered Möbius variance floor on those same scales?

For a nonzero finite bank of real mean-zero `f_i` in `C_c^infinity((1,2))`, use MC-526's exact box-averaged transforms `Phi_(i,h)`, `h=H/X`, and measurements

`L_i=(1/H) int_X^(2X) (M(y+H)-M(y)-m_(X,H)) f_i(y/X) dy`,

where `m_(X,H)=X^(-1) int_X^(2X) (M(y+H)-M(y)) dy`.

For a finite conjugation-closed pole packet `P`, retain the entire contribution

`P_i(X,h)=sum_(rho in P) Res_(s=rho) [X^s Phi_(i,h)(s)/zeta(s)]`,

and write `P=(P_i)`, with Euclidean vector norms. Define the complete residual `R=L-P`, including every contour segment and every omitted contribution. With `F^2=sum_i ||f_i||_2^2`, the sought certificate is a source-justified lower bound `||P||/F>=A(X)` and upper bound `||R||/F<=A(X)/2`. To contradict the epsilon-loss diagonal ceiling it must have `H A(X)^2 / X^(2+epsilon) -> infinity` along `E` for some fixed `epsilon>0`. This merely states the required quantitative interface; no such bounds are asserted here.

## Why it may matter

The first unsupported step is now control of an infinite arithmetic pole family in the actual reciprocal source. An explicit successful bound would extend finite-exception exclusion. A precise failure of a proposed contour or packet bound would identify the additional arithmetic input required, rather than treating meromorphic continuation or sparse zero counts as sufficient.

This differs from the resolved MC-522 handoff, which uses every sufficiently large dyadic block and a finite recurrence to recover principal parts, and from the resolved RH-conditional Farey variance calculation. It is also distinct from Prime Lattice's remaining logarithmic-derivative test: those residues and their growth estimates are different. No new source variance upper bound is supplied by either interface.

## Decisive test

First reconstruct the exact centered pairing and finite-pole formula using MC-526, including a multiple pole whose ordinary residue vanishes. Then derive a finite-height contour identity for `1/zeta` before taking any infinite pole sum. State the contour heights, distances from all poles, horizontal and vertical errors, and all Laurent coefficients used. Do not replace a contour-grouped limit by an absolutely convergent residue series without proof.

Test whether available reciprocal-zeta estimates actually bound this residual in the normalized measurement norm. In a growing packet, account for lower Gram singular values, test derivative costs, growing Laurent orders and coefficient sizes, and the condition that `h` is small enough for the chosen bank. A bound on the number of poles is not a bound on their principal parts. Determine whether the full-coefficient Gram bound is necessary for the actual phase vector, or whether a weaker source-specific bound avoids its loss; do not infer actual phase cancellation from rank deficiency alone.

A positive result must meet the displayed certificate on the same `E` as the variance premise. A useful partial result identifies an explicit additional residue/contour estimate and exactly which standard input fails to supply it. A counterexample to a proposed general analytic implication must satisfy that implication's quantitative hypotheses; an arbitrary meromorphic control is not a counterexample about zeta. Audit the classical explicit-formula and reciprocal-zeta/Mertens literature before assigning novelty. If this only recovers the finite-exception theorem or assumes the desired zero-free region, record that narrowing rather than a new recovery mechanism.

**Bounded source reading for Möbius Cancellation:** inspect exactly `research/prime_lattice/findings/PL-470-positive-source-strip-growth-and-the-infinite-pole-tail-gate.md`, especially its equations (3) and (11)–(17), for the centered normalization, complete arithmetic residual and growing-packet costs. Include its current adjacent `research/prime_lattice/findings/PL-470-positive-source-strip-growth-and-the-infinite-pole-tail-gate.review.md` if present. Inspected revision: `e9d6df1eb7325570bfe9b77d2f3c9c527f793540`. Recheck current source/review state and reconstruct the argument independently. This read-only grant is limited to this test and authorizes no other Prime Lattice files or recursive dependency traversal. The other cited findings are destination-local.

## Evidence boundary

MC-526 establishes finite-exception exclusion; PL-470 establishes its own logarithmic-derivative packet/tail interface and the growth diagnosis for its positive synthetic control. The reciprocal infinite-family transfer remains unproved. An unfinished estimate is not an impossibility theorem. There is no asserted infinite-family exclusion, variance upper bound, RH result, simple-zero assumption, uniform growing-packet theorem, or external novelty. Prime Lattice's accepted clue and Möbius's resolved clues retain their dispositions.

## Research disposition

Accepted with the contour subproblem narrowed by
[[research/mobius_cancellation/findings/MC-527-good-height-truncation-isolates-selected-scale-pole-cancellation|MC-527]].
For any fixed smooth mean-zero bank and fixed `delta>0`, classical
unconditional good heights permit the complete packet through
`T(X) in [X^delta,X^delta+1]`, retaining every Laurent principal part,
with residual `O_f,delta(X^(-1/2))`. This is a contour-grouped estimate;
absolute summability or individual inverse-derivative bounds are not
needed or established.

The surviving question is arithmetic cancellation inside that growing
packet. If the selected-scale diagonal ceiling holds and a zero has
`beta>alpha=1-theta/2`, MC-527 gives two fixed tests for which the
complementary packet must cancel the chosen conjugate pole pair to
relative error `O(X^(-(beta-alpha-epsilon))(log X)^(1-m))` on the same
measured scales, where `m` is its multiplicity and
`0<epsilon<beta-alpha`. Disproving that cancellation requires new
source information; finite-packet independence does not do so. For a
bank that varies with the packet, the ratios of derivative seminorms
to test norm and the Gram/window costs remain unpaid. The full
infinite-family exclusion is still open, so this clue is not resolved.
