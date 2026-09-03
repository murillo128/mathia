---
id: CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint
type: research-clue
status: accepted
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-127-grosswald-schnitzer-phase-slope-rigidity.md
  - research/visual_exploration/findings/VIS-007-grosswald-schnitzer-rigidity-profile-monotone.md
  - research/visual_exploration/visualizations/grosswald-schnitzer-rigidity-profile.md
---

# Can a finite critical-line phase fingerprint recover the low Grosswald–Schnitzer deformation pattern?

## Observation

`PL-127` proves that the central reflection-phase slope

`D(q)=sum_n [g(p_n)-g(q_n)]`

is a positive additive discriminator for one-sided Grosswald–Schnitzer deformations and, with integer generators, certifies that all primes below a controlled cutoff are untouched. `VIS-007` sharpens the cutoff: the minimum detectable one-step defect is a strictly decreasing function of prime scale, so the scalar certificate has a canonical resolution profile.

That scalarization still discards structure. Once the untouched prefix has been certified, `D(q)` records only the sum of the later positive contributions. It need not say which admissible generators changed or how several changes are distributed. The full reflection cocycle `R_q(1/2+it)` carries a critical-line phase function whose local derivatives and samples potentially retain more of that arithmetic fingerprint.

## Research question

Fix a finite prime cutoff `X` and restrict to admissible **integer** Grosswald–Schnitzer generators `p_n<=q_n<=p_(n+1)`. Is there a finite family of phase-sensitive observables — for example finitely many derivatives of `log R_q` at `s=1/2`, finitely many phase samples on `1/2+it`, or another explicitly bounded critical-line functional — that uniquely and quantitatively determines every `q_n` with `p_n<=X`?

Equivalently, can the scalar prefix certificate of `PL-127` be upgraded to a finite low-scale arithmetic fingerprint without invoking a general quantitative Hamburger theorem?

## Why it may matter

A positive result would turn the reflection phase from a one-number rigidity test into a reconstructive diagnostic for approximate spectral or geometric models. Such a model could then be tested not only for whether it preserves a prime prefix, but for whether its phase data actually encode the correct low arithmetic deformation pattern.

A negative result would be equally useful. If two distinct admissible integer deformation patterns can agree on every natural finite phase fingerprint of a prescribed size/window, it would quantify a remaining information-loss barrier even after modulus has been discarded in favor of phase.

## Decisive test

Start with a fixed finite cutoff and one- and two-defect families. Write the exact contribution of each altered generator to `log R_q(1/2+it)` and to its derivatives at `t=0`.

Then either:

- prove that a finite collection of such observables gives an injective map on the finite admissible integer deformation set up to `X`, with an explicit separation bound; or
- construct two distinct admissible deformation patterns below `X` that collide under the proposed observables, and determine whether increasing derivative/sample order resolves the collision or whether a structural non-identifiability remains.

The test should keep `X` finite first; compactness of a finite deformation set must not be mistaken for a useful quantitative theorem unless the observable family and separation scale are explicit.

## Evidence boundary

`PL-127` establishes only the positive scalar phase slope and its low-prefix certificate. `VIS-007` proves only that the one-step integer threshold decreases monotonically with prime scale. Neither result proves reconstruction of the complete deformation pattern from finitely many phase observables, and no such injectivity or collision theorem is asserted here.

## Research disposition

Accepted. The direction survives initial scope and prior-art checks only as a tail-uniform inverse problem. If the tail is frozen and only finitely many Euler factors vary, equality of reflection cocycles reduces after cross-multiplication to a finite exponential-polynomial identity, so a sufficiently long Taylor jet is separating by classical Vandermonde/Prony uniqueness. That finite-dimensional argument is not the target and gives no useful uniform separation in the presence of an arbitrary admissible tail.

The remaining question is whether finitely many critical-line observables recover every generator below `X` uniformly over the full integer Grosswald–Schnitzer tail. The continuation to `Re(s)>0` uses paired factor differences, so simply returning to a finitely supported or absolutely convergent coefficient-inversion setting removes the hard part. A resolution must control tail contamination using the one-sided integer constraints or exhibit an exact admissible integer-tail collision.