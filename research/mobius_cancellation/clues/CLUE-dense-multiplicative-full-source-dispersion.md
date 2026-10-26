---
id: CLUE-mobius-cancellation-dense-multiplicative-full-source-dispersion
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
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

MC-544 now resolves broad-band deterministic replica cancellation in a
different way. One fixed square-free multiplicative character source has
prefix `O(sqrt(x))`, complete centered energy `O(X)`, and balanced selected
prime targets of order `Y/log Y`. Its background cancels those targets:
the full smooth source sum on the band is only `O_phi(sqrt(Y))`. Thus
deterministic compatibility alone is no longer the missing test. A large
signal belonging to the **full source** must survive the cancellation.

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
them as absent. Use MC-544's character source as a control: its small
prefix must not be mistaken for a solution with the stated dispersion
floor. Independent random block orientations do not settle the
deterministic question already separated by MC-543.

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
