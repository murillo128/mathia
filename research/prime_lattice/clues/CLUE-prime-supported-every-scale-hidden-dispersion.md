---
id: CLUE-prime-lattice-prime-supported-every-scale-hidden-dispersion
type: research-clue
status: resolved
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-540-one-squarefree-source-hides-every-scale-dispersion-above-fourth-power-sampling.md
  - research/prime_lattice/findings/PL-483-fixed-prime-supported-sources-evade-subquarter-uniform-observations.md
  - research/prime_lattice/findings/PL-484-two-random-starts-detect-prime-poles-on-fourth-power-scales.md
---

# Can positive prime reweightings hide compatible every-scale perturbation dispersion?

## Observation

MC-540 removes the separate-populations loophole in the faster-scale
pair-detection obstruction. For every `s>4`, choose
`3/4<kappa<1-1/s`. One deterministic square-free sign source has both
macroscopic window dispersions of order `X^(2kappa-1)` at **every** large
integer scale, while two uniform starts per channel give energies at most
one eventually almost surely on `X_k=ceil(k^s)`. Balanced bridges at
geometrically spaced centers return one common prefix to a bounded
baseline. Their endpoint-hit probabilities are summable on this
polynomial sequence. This source is not multiplicative or prime-supported.

PL-483 already realizes balanced primitive area using positive relative
reweightings of the actual mod-5 prime source. Its deterministic packets
use coarse PNT mass and a Brun–Titchmarsh concentration bound, without a
lower bound in a prescribed short interval. But its signed target
separation and baseline-identical samples are established on `4^k`;
it does not give a dispersion floor on every integer block. PL-484's
faster-scale controls still use independently specified populations.

## Research question

Fix `s>4`, `3/4<kappa<1-1/s`, and
`a_n=Lambda(n) 1_(n=1 mod 5)`. Are there two deterministic infinite
sources `b_n^+=a_n+d_n` and `b_n^-=a_n-d_n`, fixed before sampling, with

- `|d_n|<=a_n/2`, and `d_n=0` unless `n` is an actual prime;
- `F(x)=sum_(n<=x)d_n=O(x^kappa)`, so both sources retain the leading PNT;
- for `I_X={X,...,2X-1}`, `L_1=floor(X/20)`, and
  `L_2=floor(sqrt(2)L_1)`, the **perturbation** windows
  `U_i(j)=F(j+L_i)-F(j)` satisfy

  `D_i^d(X)=X^(-2) sum_(j,r in I_X)|U_i(j)-U_i(r)|
   asymp X^(2kappa-1)`

  for both channels at every sufficiently large integer `X`;
- when the three sources share two independent uniform starts with
  replacement per channel on `X_k=ceil(k^s)`, all sampled windows of
  `b^+` and `b^-` eventually equal the corresponding windows of `a`,
  almost surely?

The last property concerns the whole prescribed sequence, not selected
favorable scales. Fix the product observation law across channels and
scales in advance, retaining coincident draws.

## Why it may matter

This would test whether positive relative weights, exact prime support,
PNT and common-source consistency prevent the every-scale hidden-area
mechanism. It differs from PL-483's geometric-scale signed-target test
and from PL-484's actual-source criterion. The first unresolved step is
realizing a dense family of balanced prime-capacity packets whose area
remains visible to both perturbation populations on every block.

Crucially, `D_i^d` is the dispersion of the difference from the baseline.
A theorem about it would not establish a dispersion floor or small
energies for either positive source individually. Keeping that boundary
avoids converting baseline-identical observations into an unproved
prime-energy counterexample.

## Decisive test

Test whether PL-483's deterministic capacity selection can be placed in
sufficiently closely spaced, disjoint macroscopic search intervals while
retaining an isolated complete packet in every large `I_X`. Its location
must be selected from actual prime mass, not assumed to contain enough
primes at a preassigned short interval.

The construction must then prove, rather than infer from a picture:
packet area of order `X^(2kappa)`, endpoint support of size `O(X^kappa)`
in each observation range, a two-channel dispersion lower bound without
cancellation from translated neighboring packets, and a matching upper
bound. Verify zero total perturbation per packet, the relative weight
constraint, cumulative PNT error and one source's consistency across
all overlapping scales. Check that the resulting endpoint-hit sum on
`ceil(k^s)` converges; this is the classical missed-support probability
step, not a new number-theoretic estimate.

An obstruction to the proposed placement or lower bound should identify
which prime-capacity or overlap constraint fails. Failure of one layout
is not a refutation of the existence question. Conversely, a proof must
not replace perturbation dispersion by absolute prime-source dispersion
or claim that the unknown common sample energy is small. Compare the
result with the existing Lipschitz hidden-area prior art and PL-483's
packet lemma; repeating their finite identities alone is not the delta.

**Bounded source reading for Prime Lattice:** read only
`research/mobius_cancellation/findings/MC-540-one-squarefree-source-hides-every-scale-dispersion-above-fourth-power-sampling.md`,
inspected at revision `532115861405d6e93f165266f268cdff1e3f2afd`,
for its common-prefix construction, every-block placement, translated
endpoint exclusion and summable-hit argument. Also inspect the exact
adjacent sidecar
`research/mobius_cancellation/findings/MC-540-one-squarefree-source-hides-every-scale-dispersion-above-fourth-power-sampling.review.md`
if present. Check the current finding and review state and reconstruct
those arguments independently. No other source-line finding, recursive
dependency, Mind, graph or clue inbox is authorized. PL-483 supplies the
destination's prime-capacity construction and its classical sources;
MC-540's square-free counting estimate is not a prime counting input.

## Evidence boundary

MC-540 proves its square-free-source statement. PL-483 proves the
positive prime-reweighting statement on its geometric scales. PL-484
proves the two-start criterion for the exact Mangoldt source on prescribed
fourth-power scales. Their conjunction does **not** establish the proposed
prime-supported every-scale perturbation construction.

This is an unvalidated transfer question, with no novelty or independent
review claim. The proposed sources need not preserve canonical Euler
factors, the completed functional equation or the positive isolated-pole
formula. Even a positive answer would prove no RH/GRH statement, optimal
actual-prime sampling rate, small prime energy, fixed signed pole test
on every scale, or lower bound for an estimator accumulating observations
from other scales. The actual energy estimate remains a separate problem.

## Research disposition

Outcome: supported

Resolved by:
- [[research/prime_lattice/findings/PL-485-prime-supported-perturbations-hide-every-scale-dispersion]]

Deterministic maximal-capacity prime packets in disjoint proportional
search intervals realize the requested positive reweightings. Geometric
placement supplies an isolated complete packet in every large integer
block for both lengths, giving perturbation dispersion
`asymp X^(2kappa-1)`; summable endpoint-hit probabilities give eventual
baseline-identical observations on the entire `ceil(k^s)` schedule.
The result concerns perturbation dispersion and transfers no unproved
small-energy ceiling from the baseline to either positive control.
