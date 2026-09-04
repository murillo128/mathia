# MI-010 — Spectral fidelity needs an ideal budget and relative-scale tightness, not stagewise membership or determinant convergence

**Evidence level:** proved for the Schatten, weak-operator, determinant, and infinitesimal spectral families covered by AF-108--AF-113

## Core intuition

A sequence can remain inside a desired Schatten class at every finite stage while its limit leaves that class; it can preserve a trace or regularized determinant while the operator itself escapes; and an infinitesimal spectrum can collapse every fixed analytic readout even though a nontrivial relative spectral profile survives after rescaling by its own top scale.

The missing resource is therefore twofold: a **uniform ideal budget matched to the assembly topology**, and **tightness in the relative spectral scale actually used by the downstream observable**.

## Strongest justified principle

AF-108 shows that WOT limits preserve `S_p` membership under a uniform `S_p` budget, while stagewise membership alone is useless. In the positive trace-class case, trace tightness on finite-dimensional windows is the additional condition that upgrades weak assembly to trace convergence and hence trace-norm/Fredholm-determinant fidelity.

AF-109 makes ideal norm conservation exact: under WOT plus a uniform `S_p` bound, equality of the limiting `S_p` norm is precisely the gate to `S_p`-norm convergence. Scalar trace or determinant data can therefore be faithful while the full operator is not.

AF-110--AF-112 classify infinitesimal clouds. With bounded trace mass and operator norm tending to zero, ordinary determinants converge only to zero-free exponentials; regularized determinants either tend to `1` or, at the critical integer summability threshold, retain only one moment as another zero-free exponential. Unscaled analytic probes detect only the homogeneity matching the available Schatten budget.

AF-113 identifies the genuine escape: normalize eigenvalues by the operator scale before probing. The resulting relative `p`-mass profile is recoverable only when that rescaled mass is tight away from zero. Absolute collapse and relative-shape fidelity are different questions.

## What remains possible

A spectral application may legitimately use a relative scale, but that scale and the required tightness must be forced by the source rather than chosen after inspecting the spectrum. A viable determinant/operator limit should state exactly which ideal norm, trace moment, relative profile, or zero divisor is meant to survive and prove the matching uniform budget.

## Status / novelty

Schatten ideals, WOT lower semicontinuity, trace tightness, Fredholm/regularized determinants, and moment scaling are classical. The synthesis is the fidelity hierarchy: **stagewise ideal membership < bounded ideal resource < ideal-norm fidelity, while fixed determinant convergence may sit strictly below relative spectral-profile fidelity**.

## Falsification criterion

Produce a WOT-assembled family violating one of these implications under the stated uniform hypotheses, or derive a source-natural relative-scale tightness theorem that preserves a load-bearing spectral profile beyond the zero-free determinant limits.

## Lean-formalizable core

- WOT closure under uniform Schatten budget.
- Schatten norm conservation criterion.
- Positive trace tightness criterion.
- Infinitesimal determinant asymptotics.
- Relative spectral profile under max-scale normalization.
