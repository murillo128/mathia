# MI-004 — Coordinate amplification is not operator amplification; relative transmission must cancel before Schatten norms

**Evidence level:** supported through PF-173 by exact collar Fourier models, boundary-ideal estimates, and trace-summable matched recoupling

## Core intuition

Large geometric multiplicity or a collapsing physical interface does not determine the operator burden by itself. Absolute single-surface recoupling can retain an order-one zero-mode cost even as a collar core shrinks, while the **relative** prime/clone transmission correction can be much smaller because the common zero mode cancels before any Schatten norm is taken.

The correct scale is therefore set by the matched operator difference, not by coordinate size, interface length, or separate absolute resolvent estimates.

## Strongest justified principle

PF-166--PF-171 show that the complete Margulis-short central sector is already benign at the sharp first-resolvent threshold: the matched Dirichlet-decoupled relative blocks lie in every `S_r`, `r>1`, with vanishing tail, although the endpoint `S_1` fails for that central direct sum.

PF-172 tests whether transmission across the artificial central cut reintroduces the missing obstruction. For any fixed finite interface family, elliptic boundary theory makes the absolute first-resolvent recoupling trace class. But on a collapsing model collar its angular zero mode is independent of the core length, giving an order-one lower bound on the **absolute** trace norm. Summing separate source and clone recouplings therefore cannot use pinching as a small parameter.

PF-173 performs the relative calculation instead. For matched core lengths `L` and `L'=e^t L`, the zero-mode block cancels exactly and the recoupling difference satisfies

`||G_{L'}-G_L||_1 <= C |t| L^2`.

Together with the prime/shift length asymptotics, these corrections are trace-summable over the complete short-core tail. The central transmission mode is therefore not the missing global Schatten obstruction.

## What remains possible

PF-173 is a fixed central-slab model, not the full uncut surface. Outer collar/body interfaces, global Dirichlet-to-Neumann response, localization commutators/overlap, and repeated head--tail interaction remain outside the theorem. The full relative resolvent also cannot become trace class in contradiction with the earlier non-isometry obstruction.

A positive continuation must place prime and clone in one common global interface calculus and expose the source/clone defect **before** ideal norms or absolute summation. A failure must be genuinely body-loaded or nonlocal rather than attributed to short-core multiplicity or the central zero mode.

## Status / novelty

Schatten ideals, Krein/boundary resolvent formulas, Fourier mode decomposition, and resolvent identities are classical. The line-specific synthesis is the operation-order principle: **absolute recoupling can stay order one under pinching, while matched recoupling is trace-summable because common transmission modes cancel before the norm**.

## Falsification criterion

Find a matched central collar family violating the `O(|t|L^2)` trace bound or retaining a nonzero relative zero-mode block, or show that a full-surface body/interface term is controlled by the same local cancellation and nevertheless produces a non-summable `S_r`, `r>1`, tail.

## Lean-formalizable core

- Zero-mode independence of collar length in the finite Fourier model.
- Rank-one half-collar recoupling representation per nonzero angular mode.
- Resolvent-difference factorization exposing `O(|t|q^{-2})` and the resulting trace sum.
