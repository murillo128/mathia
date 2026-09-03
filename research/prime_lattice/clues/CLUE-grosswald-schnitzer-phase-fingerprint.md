---
id: CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint
type: research-clue
status: accepted
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-127-grosswald-schnitzer-phase-slope-rigidity.md
  - research/prime_lattice/findings/PL-129-kakeya-phase-slope-tail-aliasing.md
  - research/prime_lattice/findings/PL-130-finite-phase-fingerprint-real-grosswald-schnitzer-nonidentifiability.md
  - research/prime_lattice/findings/PL-131-grosswald-schnitzer-phase-arc-injectivity.md
  - research/visual_exploration/findings/VIS-007-grosswald-schnitzer-rigidity-profile-monotone.md
  - research/visual_exploration/visualizations/grosswald-schnitzer-rigidity-profile.md
---

# Can a finite critical-line phase fingerprint recover the low Grosswald–Schnitzer deformation pattern?

## Observation

`PL-127` proves that the central reflection-phase slope

`D(q)=sum_n [g(p_n)-g(q_n)]`

is a positive additive discriminator for one-sided Grosswald–Schnitzer deformations and, with integer generators, certifies that all primes below a controlled cutoff are untouched. `VIS-007` sharpens the cutoff: the minimum detectable one-step defect is a strictly decreasing function of prime scale, so the scalar certificate has a canonical resolution profile.

`PL-129` proves that this scalarization has exact aliases, not merely poor conditioning. Even in the binary endpoint subclass `q_n in {p_n,p_(n+1)}`, the possible central slopes fill the whole interval `[0,g(2)]`; for every prime index `j`, a deformation at `j` can be matched exactly by a suitable admissible tail with `q_j` left unchanged. Thus `D` cannot recover any designated low generator uniformly over an arbitrary tail, despite retaining the sharp one-sided prefix certificate of `PL-127`.

`PL-130` closes the finite-observable branch for the original **real** Grosswald–Schnitzer class: any prescribed finite family of odd central phase derivatives and nonzero critical-line phase samples has exact local aliases, with finitely many tail coordinates compensating a change in a designated low real generator. This makes the integer restriction in the present clue load-bearing rather than cosmetic.

`PL-131` supplies the complementary infinite-data boundary. For arbitrary admissible real generators, equality of the reflection cocycle on any set of critical-line heights with a finite accumulation point forces the two complete generator sequences to coincide. Thus the full analytic phase is injective even though every finite real fingerprint is not. The unresolved issue is specifically whether **integer discreteness reduces that analytic-germ requirement to finitely many observables**.

## Research question

Fix a finite prime cutoff `X` and restrict to admissible **integer** Grosswald–Schnitzer generators `p_n<=q_n<=p_(n+1)`. Is there a finite family of phase-sensitive observables — for example finitely many derivatives of `log R_q` at `s=1/2`, finitely many phase samples on `1/2+it`, or another explicitly bounded critical-line functional — that uniquely and quantitatively determines every `q_n` with `p_n<=X`?

Equivalently, can the scalar prefix certificate of `PL-127` be upgraded to a finite low-scale arithmetic fingerprint without invoking a general quantitative Hamburger theorem?

## Why it may matter

A positive result would turn the reflection phase from a one-number rigidity test into a reconstructive diagnostic for approximate spectral or geometric models. It would also show that discrete rational-prime arithmetic compresses the information requirement: `PL-131` proves that an accumulating exact phase set determines the full real deformation, while `PL-130` proves that no finite phase family can do so continuously in the real class.

A negative result would be equally useful. If two distinct admissible integer deformation patterns can agree on every natural finite phase fingerprint of a prescribed size/window, it would quantify a remaining information-loss barrier even after modulus has been discarded in favor of phase and would show that the real-class finite/infinite transition of `PL-130`/`PL-131` persists arithmetically.

## Decisive test

The one-observable case is closed negatively by `PL-129`, and the arbitrary finite-observable case is closed negatively for **real** generators by `PL-130`. At the other extreme, `PL-131` proves that exact phase data on any accumulating critical-line set are fully identifying even for real generators. The next test must therefore be genuinely finite-dimensional, integer-valued, and keep the arbitrary tail active.

For a fixed cutoff `X`, choose an explicit finite family of independent critical-line observables beyond `D` and write the exact contribution of each admissible integer generator change. Then either prove a tail-uniform separation bound for all admissible integer tails, or construct two admissible integer sequences that differ below `X` but collide exactly under the whole finite observable vector.

Finite-support or tail-frozen uniqueness is not enough: after cross-multiplication that setting reduces to a finite exponential-polynomial identity and sufficiently long Taylor data separate it by classical Vandermonde/Prony arguments. Likewise, an infinite Taylor jet, a phase arc, or an accumulating exact sample set is no longer progress on this clue because `PL-131` already proves that such analytic-germ data are injective. The target is specifically the **finite integer-tail inverse problem**.

## Evidence boundary

`PL-127` establishes the positive scalar phase slope and its low-prefix certificate. `VIS-007` proves the monotone one-step integer threshold. `PL-129` establishes exact arbitrary-tail collisions for that **single** scalar slope. `PL-130` establishes exact collisions for every finite natural jet/sample fingerprint when the admissible generators vary continuously over the real prime gaps. `PL-131` establishes the opposite infinite-data boundary: an accumulating exact set of reflection-phase values determines the entire real Grosswald–Schnitzer sequence.

None of these results proves or disproves reconstruction from a finite vector of two or more independent phase observables for **integer** generators. The Grosswald–Schnitzer continuation to `Re(s)>0` relies on paired factor differences, so returning to a finitely supported or absolutely convergent coefficient-inversion problem removes the hard tail rather than solving it.

## Research disposition

Accepted, but now isolated to a sharp discrete information-compression question. The scalar branch is decisively negative by `PL-129`; every finite real-valued phase-fingerprint branch is negative by `PL-130`; and the analytic-germ/full-phase branch is positive by `PL-131`. What remains is neither ordinary phase retrieval nor smooth inverse-function theory.

A substantive resolution must show whether **integer Grosswald–Schnitzer discreteness** changes the finite/infinite boundary: either exhibit a finite phase fingerprint with an explicit separation theorem uniform over the full admissible integer tail, or prove structural non-identifiability by constructing an exact integer collision for a genuinely multi-observable finite fingerprint. Increasing precision in `D`, freezing the tail, using real-valued compensation, or taking infinitely many accumulating samples no longer counts as progress on this clue.