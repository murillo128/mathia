---
id: CLUE-mobius-cancellation-dense-multiplicative-full-source-dispersion
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-545-balanced-character-swaps-force-a-full-source-singularity.md
  - research/mobius_cancellation/findings/MC-540-one-squarefree-source-hides-every-scale-dispersion-above-fourth-power-sampling.md
  - research/mobius_cancellation/findings/MC-544-fixed-character-backgrounds-cancel-balanced-prime-replicas.md
  - research/prime_lattice/findings/PL-485-prime-supported-perturbations-hide-every-scale-dispersion.md
---

# Can dense hidden dispersion survive in one full multiplicative source?

## Observation

MC-540 constructs one deterministic square-free sign source with window
dispersion of order `X^(2kappa-1)` on every large integer block, yet
eventually bounded two-start observations on `ceil(k^s)`, for `s>4` and
`3/4<kappa<1-1/s`. Its locally balanced bridges return the full prefix to
a bounded baseline, but the source is not multiplicative.

PL-485 realizes the corresponding every-block geometry with actual
prime-supported positive relative perturbations. It selects sufficient
prime capacity inside each proportional search interval, then separates
complete packets from their translated endpoints. This gives large
**perturbation** dispersion and eventually baseline-identical samples.
The common prime baseline's energy is unknown; neither individual
positive source is shown to have the required dispersion or small energy.
Its adjustable, logarithmically weighted prime perturbations also differ
from the discrete prime signs required by a multiplicative sign source.

MC-544 resolves deterministic replica cancellation for both proportional
and sublinear selector widths. Its one fixed square-free multiplicative
character source has prefix `O(sqrt(x))` and complete centered energy
`V_L(X)<=64X`. For each fixed `3/4<kappa<1`, prescribed residue-class
intervals of width `W asymp Y^kappa` contain balanced selected blocks with
`h asymp Y^kappa/log Y` primes of each sign and selected target
`|T_(Y,kappa)| asymp Y^(2kappa-1)/log Y`. Their deleted backgrounds have
prefix cost `asymp h` and cancel the replica pairing to relative error
`O_kappa(Y^(1/2-kappa)log Y)`. This extension uses the unconditional
short-interval prime theorem recorded in MC-544, beyond proportional PNT.

Yet every fixed smooth **full-source** sum on every subinterval of the band
is `O_phi(sqrt(Y))`, and the full pair dispersion below is at most
`16sqrt(X)`. Narrowing the selector therefore does not preserve the missing
full-source floor. This differs from PL-485, whose additive perturbation
retains its area but has adjustable weights and an unknown prime baseline
energy. A large signal belonging to the full multiplicative source must
survive the complement and composite contributions.

## Research question

Fix `s>4` and `3/4<kappa<1-1/s`. Can one deterministic real multiplicative
source `f`, fixed before all draws, with `|f(n)|=mu(n)^2`, satisfy both
the following properties?

Write `F(x)=sum_(n<=x) f(n)`, `I_X={X,...,2X-1}`,
`L_1=floor(X/20)`, `L_2=floor(sqrt(2)L_1)`, and
`S_i(j)=F(j+L_i)-F(j)`. For both channels and **every** sufficiently
large integer `X`, require the full-source dispersion floor

`D_i(X)=X^(-2) sum_(j,r in I_X) |S_i(j)-S_i(r)|
 >= c X^(2kappa-1)`.

At `X_k=ceil(k^s)`, draw two independent uniform starts with replacement
per channel, independently across channels and scales. Require almost
surely, for each `epsilon>0`, eventually

`V_i^sample(k)=(1/4)|S_i(R_(i,k,1))-S_i(R_(i,k,2))|^2
 = O_epsilon(X_k^(1+epsilon))`, for `i=1,2`.

The source cannot depend on the observations. This asks only for the
sample ceiling relevant to the criterion, not MC-540's stronger bound
by one. It does not require a fixed signed smooth pole test. Alternatively,
identify a precise multiplicative obstruction to a specified dense packet
construction, retaining the scope of that obstruction.

## Why it may matter

The resolved prime-supported transfer established that positivity,
leading PNT, prime support and common-source consistency still permit
dense hidden perturbations. It did not impose multiplicativity. MC-544
establishes compatibility of a selected prime target with small complete
energy, but sacrifices the large full-source signal. These results leave
a concrete gap between additive packet geometry and multiplicative
source constraints.

A positive answer would strengthen the faster-than-fourth-power control
while still falling short of the actual Möbius source. A construction
obstruction could identify which composite or background contribution
prevents the transfer. The classical missed-support probability argument
alone is not a new result and cannot decide this arithmetic step.

## Decisive test

Start with two adjacent proportional search intervals and one fixed
assignment of all older prime signs. Attempt a deterministic pair of
balanced prime prescriptions using PL-485's complete-packet placement.
Account explicitly for the loss of logarithmic weights and adjustable
amplitudes when translating its capacity argument to prime signs.
Calculate the **complete multiplicative** prefix and both window
populations, including complementary primes and every composite product
affected by either prescription. A prime-supported additive difference
or the selected-prime target is not the requested observable.

Test whether primitive area of order `X^(2kappa)` remains visible to
both full-source populations after those contributions are included.
For an endpoint-hiding construction, establish a background sample
ceiling and an exceptional endpoint set of size `O(X^kappa)`; its hit
sum on `ceil(k^s)` would then converge. If multiplicative replicas spread
the exceptional set, bound their actual sample tail instead of treating
them as absent. Use MC-544's Section 4 character source as a control at
the **same** sublinear width: it already pays the deleted-background cost and cancels
the replica while violating the requested full-source floor, since
`D_i(X)<=16sqrt(X)=o(X^(2kappa-1))`. Merely bounding width or exhibiting a
super-square-root selected target therefore cannot pass the test. A new
assignment must demonstrate where its full primitive survives, or state a
source-justified constraint excluding this character control; independently
chosen signs are a different class, not excluded by MC-544. Independent
random block orientations do not settle the deterministic question already
separated by MC-543.

A passing two-block calculation is only a compatibility test. Completion
requires one infinite prime assignment and uniform estimates on every
large integer block, including overlapping observation ranges. Failure
of one layout is not a general nonexistence theorem. Compare any proposed
area/endpoint step with MC-540 and PL-485's classical hidden-area argument;
the intended delta is survival under multiplicativity and the complete
background, not another finite packet identity.

**Bounded source reading for Möbius Cancellation:** read only
`research/prime_lattice/findings/PL-485-prime-supported-perturbations-hide-every-scale-dispersion.md`,
inspected at revision `16a22bccb6a44e3af02ab914a87e89778cefb752`,
for its self-contained capacity construction, proportional placement,
translated-endpoint exclusion and summable-hit argument. Also inspect
the exact adjacent sidecar
`research/prime_lattice/findings/PL-485-prime-supported-perturbations-hide-every-scale-dispersion.review.md`
if present. Check the current finding/review state and reconstruct those
steps independently. No other source-line finding, recursive dependency,
Mind, graph or clue inbox is authorized. Its prime-capacity inputs do not
give free choices for composite signs or a small baseline energy.

## Evidence boundary

MC-540 proves the nonmultiplicative full-source control, PL-485 the
positive prime-perturbation control, and MC-544 the multiplicative
character cancellation control. Their conjunction does not prove the
proposed multiplicative dispersion statement. This is an unvalidated
transfer question, with no novelty or independent-review claim.

Even a positive answer supplies no reciprocal-zeta identity, canonical
Möbius prime signs, isolated-pole formula, RH result, optimal arithmetic
sampling rate, or lower bound for an estimator accumulating observations
from other scales. No small energy for the actual prime or Möbius source
is being imported. The actual arithmetic energy ceilings remain separate.

## Research disposition

Accepted for continued investigation of the complete window populations.
[MC-545](../findings/MC-545-balanced-character-swaps-force-a-full-source-singularity.md)
constructs one deterministic infinite assignment by actually swapping
balanced character-prime packets at every sufficiently large dyadic
scale. Its exact Euler quotient includes all composite contributions.
For `beta=2kappa-1`, the continued full-source series has a nonmeromorphic
real singularity with an explicit fractional radial exponent; hence the
complete prefix cannot be `O(x^(beta-delta))` for any `delta>0`.
This establishes a full-source obstruction that the unchanged character
control MC-544 cannot supply.

The clue is not resolved. A global failure of a power bound does not
give either channel's dispersion floor on every block, and the
singularity gives no sparse-sample upper tail. For this explicit source,
the remaining test must include old-packet replicas and products of
changed primes in both complete window populations. Its nonmeromorphic
singularity also prevents direct reuse of an isolated-pole certificate.
The general failure of ordinary character pretentiousness to preserve
power cancellation, and Euler-factor singularity construction, are
classical prior art; the partial result is not an RH mechanism.
