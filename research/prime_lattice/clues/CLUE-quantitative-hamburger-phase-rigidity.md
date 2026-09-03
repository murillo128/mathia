---
id: CLUE-prime_lattice-quantitative-hamburger-phase-rigidity
type: research-clue
status: resolved
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-125-sierra-squarefree-rindler-dirac-grosswald-schnitzer-control.md
  - research/prime_lattice/findings/PL-126-hamburger-functional-equation-rigidity.md
  - research/visual_exploration/findings/VIS-006-modulus-functional-equation-defect-forced-critical-line.md
  - research/visual_exploration/visualizations/functional-equation-modulus-trench.md
---

# Is Hamburger rigidity quantitatively stable in a phase-sensitive norm for Grosswald–Schnitzer deformations?

## Observation

`PL-125` gives integer Grosswald–Schnitzer deformations `Z_q=phi_q zeta` that preserve the zeta zero divisor in `Re(s)>0`, while `PL-126` shows that exact Riemann self-duality inside Hamburger's finite-order ordinary Dirichlet-series class forces the deformation to collapse back to `zeta`.

`VIS-006` adds an information-loss control: the modulus-only defect

`log|F(s)| - log|chi(s)F(1-s)|`

vanishes identically on `Re(s)=1/2` for every Schwarz-symmetric `F`, including `F=1` and deformed finite Euler products. Thus a quantitative version of the `PL-126` discriminator cannot be based only on critical-line magnitudes; it must retain phase/complex reflection information or equivalent coefficient data.

## Research question

For an integer Grosswald–Schnitzer deformation with

`Z_q(s)=phi_q(s) zeta(s)`,

the exact functional-equation failure can be written, wherever the continuation is available, as the reflection cocycle

`R_q(s) = Z_q(s) / (chi(s) Z_q(1-s)) = phi_q(s) / phi_q(1-s)`.

Is there a **scale-aware stability theorem** saying that small complex deviation `R_q-1` on an appropriate strip/vertical window, together with Hamburger-type growth hypotheses, forces the low Dirichlet coefficients of `Z_q` — equivalently the low generators `q_n` — to agree with those of `zeta` up to a quantitatively related scale?

The scale dependence is essential: changing only a very large generator can make its contribution arbitrarily small on a fixed compact set, so no uniform local lower bound independent of the first altered prime should be expected.

## Why it may matter

An affirmative result would turn `PL-126` from an exact uniqueness boundary into a usable discriminator for approximate spectral/geometric constructions. It could say how much genuinely global phase-sensitive self-duality must be recovered before the rational-prime lattice becomes identifiable, and would provide a mathematically meaningful observable for visual or computational exploration.

A negative result would also be valuable: if nontrivial integer deformations can approximate the full reflection cocycle arbitrarily well on expanding windows while remaining arithmetically different at controlled low scales, then “approximate functional equation” mechanisms would inherit a new Grosswald–Schnitzer obstruction.

## Decisive test

First determine whether existing converse-theorem literature already supplies a quantitative/stability form of Hamburger uniqueness. A bounded search around “stability/quantitative Hamburger theorem” did not expose an obvious standard result, but this is not a novelty claim.

If no suitable theorem is standard, attack the simplest one-defect family: keep all generators equal to `p_n` except one admissible integer `q_j != p_j`. Then `phi_q` is an explicit one-factor ratio. Derive the size and phase of

`log R_q(s) = log phi_q(s) - log phi_q(1-s)`

as a function of the altered prime, the window height, and the distance from `Re(s)=1/2`. Determine whether a norm of this cocycle can recover the location of the first altered generator up to constants, or construct a sequence of one-defect controls that defeats every proposed local norm.

## Evidence boundary

At proposal time, exact Hamburger rigidity was established in `PL-126` but no quantitative stability statement was known here. The clue itself remains workflow metadata rather than mathematical evidence. `PL-127` now establishes a narrower Grosswald–Schnitzer-specific result: the critical-line reflection **phase slope at the self-dual point** is a positive additive defect, and integer discreteness turns it into a finite-scale certificate for agreement of low prime generators. It does not establish a general quantitative Hamburger theorem for arbitrary Dirichlet series.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/prime_lattice/findings/PL-127-grosswald-schnitzer-phase-slope-rigidity.md]]

The general stability problem for Hamburger's converse theorem remains open in this repository, but the decisive Grosswald–Schnitzer test motivating this clue is settled more directly: no strip norm is needed to detect integer deformations at finite scale; a single phase-sensitive derivative at `s=1/2` already provides a positive, noncancelling certificate.