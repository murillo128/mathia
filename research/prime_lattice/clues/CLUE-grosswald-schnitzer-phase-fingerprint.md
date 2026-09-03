---
id: CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint
type: research-clue
status: accepted
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-127-grosswald-schnitzer-phase-slope-rigidity.md
  - research/prime_lattice/findings/PL-129-kakeya-phase-slope-tail-aliasing.md
  - research/visual_exploration/findings/VIS-007-grosswald-schnitzer-rigidity-profile-monotone.md
  - research/visual_exploration/visualizations/grosswald-schnitzer-rigidity-profile.md
---

# Can a finite critical-line phase fingerprint recover the low Grosswald–Schnitzer deformation pattern?

## Observation

`PL-127` proves that the central reflection-phase slope

`D(q)=sum_n [g(p_n)-g(q_n)]`

is a positive additive discriminator for one-sided Grosswald–Schnitzer deformations and, with integer generators, certifies that all primes below a controlled cutoff are untouched. `VIS-007` sharpens the cutoff: the minimum detectable one-step defect is a strictly decreasing function of prime scale, so the scalar certificate has a canonical resolution profile.

`PL-129` now proves that this scalarization has exact aliases, not merely poor conditioning. Even in the binary endpoint subclass `q_n in {p_n,p_(n+1)}`, the possible central slopes fill the whole interval `[0,g(2)]`; for every prime index `j`, a deformation at `j` can be matched exactly by a suitable admissible tail with `q_j` left unchanged. Thus `D` cannot recover any designated low generator uniformly over an arbitrary tail, despite retaining the sharp one-sided prefix certificate of `PL-127`.

The full reflection cocycle `R_q(1/2+it)` still carries a critical-line phase function whose additional local derivatives and samples may retain more of that arithmetic fingerprint.

## Research question

Fix a finite prime cutoff `X` and restrict to admissible **integer** Grosswald–Schnitzer generators `p_n<=q_n<=p_(n+1)`. Is there a finite family of phase-sensitive observables — for example finitely many derivatives of `log R_q` at `s=1/2`, finitely many phase samples on `1/2+it`, or another explicitly bounded critical-line functional — that uniquely and quantitatively determines every `q_n` with `p_n<=X`?

Equivalently, can the scalar prefix certificate of `PL-127` be upgraded to a finite low-scale arithmetic fingerprint without invoking a general quantitative Hamburger theorem?

## Why it may matter

A positive result would turn the reflection phase from a one-number rigidity test into a reconstructive diagnostic for approximate spectral or geometric models. Such a model could then be tested not only for whether it preserves a prime prefix, but for whether its phase data actually encode the correct low arithmetic deformation pattern.

A negative result would be equally useful. If two distinct admissible integer deformation patterns can agree on every natural finite phase fingerprint of a prescribed size/window, it would quantify a remaining information-loss barrier even after modulus has been discarded in favor of phase.

## Decisive test

The one-observable case is closed negatively by `PL-129`. The next test must be genuinely vector-valued and keep the arbitrary tail active.

For a fixed cutoff `X`, choose an explicit finite family of independent critical-line observables beyond `D` and write the exact contribution of each endpoint or integer generator change. Then either prove a tail-uniform separation bound for all admissible tails, or construct two admissible sequences that differ below `X` but collide exactly under the whole finite observable vector.

Finite-support or tail-frozen uniqueness is not enough: after cross-multiplication that setting reduces to a finite exponential-polynomial identity and sufficiently long Taylor data separate it by classical Vandermonde/Prony arguments. The target is specifically the infinite-tail inverse problem.

## Evidence boundary

`PL-127` establishes the positive scalar phase slope and its low-prefix certificate. `VIS-007` proves the monotone one-step integer threshold. `PL-129` establishes exact arbitrary-tail collisions for that **single** scalar slope. None of these results proves or disproves reconstruction from a finite vector of two or more independent phase observables.

The Grosswald–Schnitzer continuation to `Re(s)>0` relies on paired factor differences, so returning to a finitely supported or absolutely convergent coefficient-inversion problem removes the hard part rather than solving it.

## Research disposition

Accepted, but narrowed again. The scalar branch is now decisively resolved negatively: `D` alone cannot identify even one prescribed low generator against an arbitrary admissible integer tail, because `PL-129` supplies exact tail aliases at every prime index.

The surviving direction is the finite-dimensional tail-uniform inverse problem. A substantive resolution must either exhibit a finite phase fingerprint with an explicit separation theorem uniform over the full admissible integer tail, or prove structural non-identifiability by constructing an exact collision for a genuinely multi-observable finite fingerprint. Merely increasing precision in `D`, freezing the tail, or invoking finite-dimensional Prony uniqueness no longer counts as progress on this clue.