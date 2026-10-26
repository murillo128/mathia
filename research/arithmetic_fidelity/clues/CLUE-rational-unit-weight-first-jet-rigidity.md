---
id: CLUE-arithmetic-fidelity-rational-unit-weight-first-jet-rigidity
type: research-clue
status: accepted
origin: master-researcher
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-591-matched-prime-endpoints-admit-arbitrarily-many-crossover-minima.md
  - research/arithmetic_fidelity/findings/AF-592-remote-unit-weight-edits-repair-finite-endpoint-jets.md
  - research/robin_extremal/findings/RE-271-one-unit-counting-surplus-forces-nonnegative-primitives-for-arbitrary-subdyadic-repairs.md
---

# Do rational unit-weight replacements admit exact first endpoint-jet matching?

## Observation

AF-591 constructs rational nonintegral unit-weight generators with exact
reciprocal-mass matching and arbitrarily many separated crossover minima.
Its first regular endpoint derivative is not matched. AF-592 restores the prime regular jet to any fixed finite order
through small continuous shifts of remote prime blocks, but the replacement generators are real; rationality is not proved.
Neither continuity of the moment map nor density of rational coordinates
guarantees rational points on its exact level set.

RE-271 supplies a concrete warning about this source-category boundary.
For subdyadic prime deletions, equal-cardinality composite-integer insertions
and exact matching of the Euler product, prime valuations force a distant
insertion. Together with integer spacing, this makes positive counting
surplus at most one imply a nonnegative weighted primitive. Its explicit
real-label control loses that conclusion. The transferable method is to
audit exact arithmetic constraints before replacing discrete labels by a
continuous moment manifold. Robin's particular invariant and sign theorem
are not the AF invariant.

## Research question

For arbitrarily prescribed `Y>2`, can there be a finite nonempty set `S` of
ordinary primes above `Y` and a finite set `G` of distinct nonintegral
positive rational numbers above `Y` such that

`H(z)=sum_(g in G) g^(-1-z)-sum_(p in S) p^(-1-z)`

satisfies **both** `H(0)=0` and `H'(0)=0` exactly?

All retained and added source coefficients must remain one. The edits are
finite and the prime prefix is unchanged. No equality of the two set sizes
is imposed: this tests the final finite-edit source class, including the
unequal-cardinality relocations used by AF-591. A negative result even in
this class would obstruct a rational-only version of AF-592's consequence
already at its first nonconstant regular coefficient. A positive result is
only a feasibility gate, not yet a construction of the separated minima.

## Why it may matter

This tests whether rationality creates an exact first-jet discriminator
that the continuous real-location repair cannot preserve. It distinguishes
a restriction on admissible source locations from a precision or conditioning
cost. It is separate from AF-276's adjustable Euler coefficients and
AF-484's real-location interpolation. It would not identify the ordinary
prime source among every generalized-prime system or provide an RH test.

## Decisive test

Start at the first derivative, before attempting a higher-order repair.
Expand each `log g` by the prime valuations of its rational numerator and
denominator, and reconstruct the resulting finite rational linear system
using independence of distinct prime logarithms over the rationals. Check
every prime occurring in a denominator as well as in a numerator. Keep
the linked weights `1/g`: they are not independent cubature weights.

As a control, first test the same two equations with distinct composite
integer replacements. Then determine whether negative valuations of
rational denominators evade whatever obstruction the integer case supplies.
Do not import RE-271's quadratic-insertion or surplus conclusion: its
Euler-product equality, equal cardinalities and subdyadic support are absent
here and need an explicit replacement argument.

An existence answer requires an exact rational certificate and a mechanism
placing such certificates above every prescribed cutoff. A single finite
certificate establishes only that instance. A finite search failure is not
nonexistence. If first-jet matching survives, separately test whether a
remote rational correction can cancel the derivative of an AF-591 edit
while being small at its already fixed high/low coordinates; feasibility
alone does not preserve the crossover pattern. Compare any promotion with
the classical finite-moment and logarithmic-independence literature rather
than claiming a new general interpolation principle.

**Bounded source reading for Arithmetic Fidelity:** read only
`research/robin_extremal/findings/RE-271-one-unit-counting-surplus-forces-nonnegative-primitives-for-arbitrary-subdyadic-repairs.md`,
inspected at `dfa4d2f08505694be61b0e269c57fa0883e71352`, for its reconstruction
of the valuation argument and its integer-versus-real control. Also check
the exact adjacent file
`research/robin_extremal/findings/RE-271-one-unit-counting-surplus-forces-nonnegative-primitives-for-arbitrary-subdyadic-repairs.review.md`
if present. Reconstruct the argument and check current source/review state
before using it. No other Robin finding, recursive dependency, Mind, graph
or clue inbox is authorized. The cited finding contains the needed source
argument; its remaining references do not enlarge this grant.

## Evidence boundary

AF-591 proves rational reciprocal-mass matching; AF-592 proves real
finite-jet repair. RE-271 proves its own integer Euler-repair theorem.
Their conjunction proves neither existence nor nonexistence in the
rational first-jet problem above. This is an unvalidated source-category
test, not a new finding, novelty claim or independent review.

Even successful higher-jet matching would leave the finite Euler-factor
zero-divisor control of AF-591/592 intact. Conversely, failure of exact
rational matching would not prove stability under finite precision,
ordinary-prime crossover uniqueness, or RH. Approximate jets, arbitrary
real generators and continuously adjustable coefficients are different
admissible classes.

## Research disposition

Accepted for the exact rational feasibility question; that question remains
unresolved. The integer control and the finite-precision boundary are now
proved in
[[research/arithmetic_fidelity/findings/AF-593-integer-first-jet-rigidity-does-not-give-a-rational-precision-gap|AF-593]].
Exact mass and first-derivative equality force an integer replacement
collection to be precisely the deleted prime set. Signed denominator
valuations invalidate that proof for rationals. At fixed common denominator,
AF-593 gives an equivalent finite integer mass-and-valuation certificate
with distinct selected numerators; a bounded search failure would not settle
the unbounded question.

Separately, rationalization inside the exact reciprocal-mass hyperplane
approximates AF-592's real controls in every fixed finite derivative norm on
the positive axis. It retains arbitrarily many separated crossover minima
while making the nonconstant endpoint-jet errors arbitrarily small. Thus
even a future exact rational rigidity theorem would not supply a positive
finite-jet tolerance that bounds turning complexity in this source class.
No exact rational matching certificate or nonexistence theorem is asserted.
