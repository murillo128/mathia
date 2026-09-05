# MI-004 — Complete scalar five-point control is a curvature-correlation realizability problem

**Evidence level:** supported through ANF-059 by the exact five-point normal form, support-free mismatch bounds, phase-aware curvature-correlation gate, and profile-specific transform certificate

## Core intuition

Once conjugation symmetry reduces a cardinality-five Weil obstruction to one off-axis pair plus a critical-line point, the remaining scalar problem is not governed only by vertical mismatch. Horizontal separation survives through the curvature correlation of the chosen profile. Discarding that phase information creates the small-frequency barrier seen in the support-free estimates; retaining it converts part of the two-variable defect into an explicit one-dimensional signed correlation gate.

For the fixed Montgomery--Taylor profile that gate is no longer a qualitative oscillation constraint. Its curvature transform has an exact rational--trigonometric form, so the surviving scalar problem has been compactified to a narrow, auditable separation/mismatch region.

## Strongest justified principle

ANF-054--ANF-057 show that, for a nonnegative even profile satisfying the explicit curvature gate `m_5(J)>=0`, equal heights are positive and a universal support-free tube excludes sufficiently small relative mismatch. For the Montgomery--Taylor profile this forces any remaining zero to have relative mismatch `q>0.1409`.

ANF-058 retains the positive horizontal phase term that the support-free comparison discarded. After integration, its contribution is exactly the canonical curvature correlation `K_J(d)`. If `K_J(d)>=-K_0/3`, the resulting quadratic lower bound is positive for every positive pair of heights. Hence any five-point zero must lie in a negative curvature-correlation lobe.

ANF-059 evaluates that lobe for the fixed Montgomery--Taylor profile without numerical quadrature. The exact factorization `J_MT=g*g` gives `K_MT(t)=-F_MT''(t)/(4 pi^2)` as an explicit rational--trigonometric function. An outward-rounded mesh certificate plus a twice-integrated analytic tail proves the sharper necessary condition

`0.545 < |t_1-t_2| < 1.01`.

Combined with the previous height gate, every remaining Montgomery--Taylor five-point scalar zero must therefore satisfy both `q>0.1409` and this narrow horizontal-separation window. The surviving scalar frontier is an explicit compact two-parameter realizability problem, not an unconstrained support/notch optimization.

## What remains possible

ANF-059 does not prove zero-freeness inside the residual compact set and does not extend the five-point result to larger conjugation-invariant multisets. The live scalar question is whether the exact Montgomery--Taylor five-point form, together with the remaining height/common-translation coherence terms, excludes that compact remainder.

A broader escape may retain additional horizontal or ordered information before scalarization, but it must survive the exact ANF-058--ANF-059 curvature controls rather than reintroduce a support-free coefficient already known to be sharp at small frequency.

## Status / novelty

The Fourier/cosine identities, hyperbolic inequalities, Cauchy estimates, moment bounds, bounded-variation control, and interval certification are classical tools. Persisted evidence makes the Mathia-specific synthesis exact at cardinality five. ANF-058--ANF-059 do not claim publication-level novelty for the resulting transfer or compactification.

## Falsification criterion

Exhibit a valid Montgomery--Taylor five-point zero with `q<=0.1409`, with `|t_1-t_2|<=0.545`, or with `|t_1-t_2|>=1.01`; alternatively find an error in the retained phase term, its curvature-correlation reduction, or the outward-rounded transform certificate.

## Lean-formalizable core

- The phase-retaining five-point lower bound and discriminant gate.
- The implication `K_J(d)>=-K_0/3 => H_J>0` under the stated curvature hypothesis.
- The exact Montgomery--Taylor transform formula and finite interval inequalities yielding the sharpened separation window.
