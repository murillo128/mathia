---
id: CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint
type: research-clue
status: resolved
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-127-grosswald-schnitzer-phase-slope-rigidity.md
  - research/prime_lattice/findings/PL-129-kakeya-phase-slope-tail-aliasing.md
  - research/prime_lattice/findings/PL-130-finite-phase-fingerprint-real-grosswald-schnitzer-nonidentifiability.md
  - research/prime_lattice/findings/PL-131-grosswald-schnitzer-phase-arc-injectivity.md
  - research/prime_lattice/findings/PL-132-integer-grosswald-schnitzer-finite-phase-fingerprint.md
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

`PL-131` supplies the complementary infinite-data boundary. For arbitrary admissible real generators, equality of the reflection cocycle on any set of critical-line heights with a finite accumulation point forces the two complete generator sequences to coincide. Thus the full analytic phase is injective even though every finite real fingerprint is not. The unresolved issue was specifically whether **integer discreteness reduces that analytic-germ requirement to finitely many observables**.

## Research question

Fix a finite prime cutoff `X` and restrict to admissible **integer** Grosswald–Schnitzer generators `p_n<=q_n<=p_(n+1)`. Is there a finite family of phase-sensitive observables — for example finitely many derivatives of `log R_q` at `s=1/2`, finitely many phase samples on `1/2+it`, or another explicitly bounded critical-line functional — that uniquely and quantitatively determines every `q_n` with `p_n<=X`?

Equivalently, can the scalar prefix certificate of `PL-127` be upgraded to a finite low-scale arithmetic fingerprint without invoking a general quantitative Hamburger theorem?

## Why it may matter

A positive result would turn the reflection phase from a one-number rigidity test into a reconstructive diagnostic for approximate spectral or geometric models. It would also show that discrete rational-prime arithmetic compresses the information requirement: `PL-131` proves that an accumulating exact phase set determines the full real deformation, while `PL-130` proves that no finite phase family can do so continuously in the real class.

A negative result would be equally useful. If two distinct admissible integer deformation patterns can agree on every natural finite phase fingerprint of a prescribed size/window, it would quantify a remaining information-loss barrier even after modulus has been discarded in favor of phase and would show that the real-class finite/infinite transition of `PL-130`/`PL-131` persists arithmetically.

## Decisive test

The one-observable case is closed negatively by `PL-129`, and the arbitrary finite-observable case is closed negatively for **real** generators by `PL-130`. At the other extreme, `PL-131` proves that exact phase data on any accumulating critical-line set are fully identifying even for real generators. The next test therefore had to be genuinely finite-dimensional, integer-valued, and keep the arbitrary tail active.

For a fixed cutoff `X`, the decisive goal was to prove a tail-uniform separation bound for admissible integer prefixes under some finite family of phase observables, or else construct two admissible integer sequences differing below `X` that collide exactly under such a family.

Finite-support or tail-frozen uniqueness was not enough: after cross-multiplication that setting reduces to a finite exponential-polynomial identity and sufficiently long Taylor data separate it by classical Vandermonde/Prony arguments. Likewise, an infinite Taylor jet, a phase arc, or an accumulating exact sample set was no longer progress because `PL-131` already proved those data injective. The target was specifically the **finite integer-tail inverse problem**.

## Evidence boundary

`PL-127` establishes the positive scalar phase slope and its low-prefix certificate. `VIS-007` proves the monotone one-step integer threshold. `PL-129` establishes exact arbitrary-tail collisions for that **single** scalar slope. `PL-130` establishes exact collisions for every finite natural jet/sample fingerprint when the admissible generators vary continuously over the real prime gaps. `PL-131` establishes the opposite infinite-data boundary: an accumulating exact set of reflection-phase values determines the entire real Grosswald–Schnitzer sequence.

`PL-132` now supplies the missing discrete bridge. For any fixed cutoff and any nondegenerate bounded critical-line interval, the integer control space is a compact product of finite alphabets and its low-prefix quotient has finitely many clopen classes. The `PL-131` phase-arc map is continuous and injective on that compact space, so distinct prefix classes have a positive uniform distance in `C(I)`. Compactness of the image gives uniform equicontinuity, allowing the separating arc to be replaced by finitely many phase samples while retaining a positive tail-uniform margin.

The result is non-effective: it proves existence of a finite sampling set and positive margin but does not provide useful explicit bounds for the number or location of samples or for the separation constant. Effective sample complexity is therefore a different residual question, not a reason to keep the yes/no finite-identifiability clue open.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/prime_lattice/findings/PL-132-integer-grosswald-schnitzer-finite-phase-fingerprint.md]]

The core finite-integer-tail identifiability question is answered positively: for every fixed low-prime cutoff, finitely many critical-line reflection-phase samples separate all admissible integer prefixes uniformly over arbitrary admissible integer tails. What remains unresolved is quantitative effectiveness — explicit sample locations/counts and usable lower bounds for the separation margin. Any future clue should target those rates or conditioning directly rather than reopen finite-fingerprint existence.