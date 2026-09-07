# MI-009 — Guarded energy fixes static feasibility and the low-mode periodic heat law

**Evidence level:** proved for the declared Xi visible-moment and periodic heat interfaces through XF-087

## Core intuition

The destination-weighted guarded resource now removes two apparent source-class problems at once. First, bounded guarded energy forces the visible moment vector into a cone admitting an exact equal-weight real-divisor realization. Second, once those first `K` moments are fixed, their periodic heat trajectory is unique and is exactly the trapezoidal frequency discretization of the canonical one-sided Volterra flow. Neither arbitrary root placement nor high periodic moments remain free dynamic variables in the guarded band.

The surviving difficulty is quantitative **continuum-to-grid transport of the actual Xi source**, especially the singular endpoint/background structure of the Volterra convolution.

## Strongest justified principle

XF-084 identifies a degree-`N` real-divisor carrier with an equal-weight `N`-atomic unit-circle measure and formulates the visible power sums as a positive trigonometric moment problem. XF-085 shows that a fixed normalized `ell^1` interior margin admits exactly `N` equal-weight nodes once the Xi node budget dominates the visible degree. XF-086 proves that the guarded selector norm supplies that margin automatically: `R(Q)=o(J^3)` forces the normalized visible moment mass to zero, so bounded guarded resource is more than enough.

XF-087 then derives the exact power-sum heat ODE from the periodic Vieta system. For grid frequency `xi_m=m Delta`, its quadratic term is precisely the composite trapezoidal rule for the continuum Volterra convolution, including half-weight endpoints that reproduce the exact flat-density damping. The system is triangular for `m<=N`, so any two degree-`N` realizations with the same first `K` moments have the same first-`K` heat trajectory. Root collisions, labels, and high modes do not change that state.

Thus the live bridge has become: obtain the actual Xi moment prefix with controlled guarded resource, and bound the difference between the source continuum Volterra field and this exact grid evolution after the endpoint/background normalization.

## Counterevidence / boundary

XF-087 does not prove the required consistency estimate for the actual Xi carrier. A naive smooth trapezoid bound is only a calibration because XF-051's positive-frequency source has a singular endpoint. Nor do XF-084--XF-087 prove that a hypothetical positive-`Lambda` transition produces nontrivial guarded mass.

The exact periodic result is restricted to the nonwrapped range `K=o(N)`, which contains the current source-visible band. Nothing is asserted about arbitrary higher modes.

## Epistemic status

**Proved static feasibility and exact low-mode discrete dynamics; source extraction, endpoint consistency, and transition coercivity open.**

## Falsification criterion

Produce a guarded moment vector in the XF-086 regime that fails exact equal-weight realization, or two degree-`N` periodic carriers with the same first `K` moments whose first-`K` heat trajectories differ despite XF-087. More relevantly, an Xi-compatible endpoint profile whose trapezoidal Volterra defect stays order one in the guarded band would identify the intended remaining obstruction rather than falsify the static/discrete statements.