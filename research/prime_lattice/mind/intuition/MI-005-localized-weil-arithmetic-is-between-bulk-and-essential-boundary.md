# MI-005 — Localized Weil arithmetic sits between universal bulk homogenization and essential boundary recurrence

**Evidence level:** supported by exact localized-operator limits and essential-norm obstructions

## Core intuition

The localized Weil operator now exhibits a topology-sensitive split. At finite scale, spectral reality can occur before any prime term is present. After boundary rescaling, fixed-depth strong limits lose the arithmetic and converge to zero or to a universal PNT-controlled rank-one model. Yet the prime-power thresholds do not disappear in norm or in the Calkin algebra: they survive as order-one partial reflections with infinite-multiplicity essential spectrum. The arithmetic is therefore neither captured by the universal bulk limit nor packaged as ordinary compact/Fredholm spectral flow.

## Strongest justified principle

PL-044 and PL-049--PL-054 isolate the three regimes.

- PL-044 shows that localized self-adjoint/real-zero spectral reality is not itself arithmetic: sufficiently short support sees no prime-power term at all while the canonical localized operator still has a real spectral characteristic object.
- PL-049 proves that the compressed prime-shift norm grows exponentially at the moving boundary, so a uniform bounded-operator limit cannot be obtained without rescaling.
- PL-050 shows that the natural rescaled boundary operator converges strongly to zero on every fixed window even though moving boundary states keep order-one spectral edges.
- PL-051 identifies the fixed-depth endpoint blow-up: after the natural normalization it converges strongly to a universal rank-one off-diagonal Hankel model governed by the prime number theorem. First-order bulk boundary spectrum therefore classicalizes before it sees zero fluctuations.
- PL-052 shows why norm convergence fails. Kronecker recurrence of the prime logarithms leaves an order-one norm gap, while smoothing against fixed probes suppresses that recurrence and returns to the classical explicit-formula zero modes.
- PL-053 upgrades the obstruction to the essential norm: the residual is not compact or Schatten, so it cannot be removed by an ordinary compact counterterm. PL-054 identifies each prime-power threshold with an essential partial-reflection channel having `+/-1` at infinite multiplicity; the threshold can vanish strongly while remaining order one in the Calkin algebra.

The live information is therefore in a **moving/mesoscopic boundary channel whose correct topology has not yet been identified**.

## What remains possible

A scale `R=R(L)` growing with the localization parameter, together with a smoothing or relative topology forced by the Weil geometry, could in principle subtract the universal PNT bulk while retaining zero-sensitive fluctuations without keeping the full essential threshold recurrence. A spectral-shift or determinant-type object would have to be defined in a category compatible with that topology; ordinary compact-perturbation Fredholm theory is already excluded for the unsmoothed threshold operator.

This does not assert that such an intermediate topology exists. Fixed strong limits, operator norm/Calkin limits, and fixed smooth probes currently land on three different known backgrounds: zero/universal, essential atomic recurrence, and the classical explicit formula.

## Status / novelty

The strong-limit, rank-one PNT, norm/essential-norm, and partial-reflection statements are persisted exact findings. The interpretation as a missing mesoscopic topology is a supported synthesis; existence of a useful zero-sensitive limit remains an open research direction.

## Falsification criterion

Show that every canonical scaling/smoothing compatible with the localized Weil construction either converges to the PNT universal model, retains the same essential partial-reflection obstruction, or is equivalent to inserting the classical explicit formula. Conversely, construct an intrinsic mesoscopic topology in which the PNT background can be removed and a nontrivial zero-sensitive relative object converges while surviving Beurling controls.

## Lean-formalizable core

- Strong-versus-norm convergence separation for moving boundary operators.
- Rank-one fixed-depth boundary limit.
- Essential-norm lower bound from Kronecker recurrence.
- Infinite-multiplicity `+/-1` spectrum of the prime-power threshold partial reflection.
