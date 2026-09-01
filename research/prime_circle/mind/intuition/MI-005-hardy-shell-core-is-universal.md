# MI-005 — Hardy nonlocality survives, but every fixed finite trace layer classicalizes or is spectrally too sparse

**Evidence level:** supported by exact operator classifications, finite-trace reductions, and the trace-class zero-density obstruction

## Core intuition

The canonical Hardy interior/exterior split genuinely escapes cotangent endpoint closure: it produces a nonlocal Hankel operator. The finite and fixed-shell parts of that escape are now much more tightly bounded, however. All ordinary finite mixed traces and all fixed-shell relative moments lie in cyclotomic hyperlogarithmic period algebras, while the fixed-shell trace-class Fredholm determinant has a zero divisor far too sparse to realize Riemann-zero density under a natural linear spectral scale.

## Strongest justified principle

PC-075 and PC-081 classify the essential layer. Primitive-shell Hardy operators are finite combinations of universal Hilbert channels plus trace-class remainders, and finite families have a joint Calkin algebra that is a wedge of universal Hilbert bands. Finite algebraic coupling cannot create a new arithmetic essential spectrum.

PC-100--PC-103 close the separated finite-cycle period question. The cubic and quartic cases reduce explicitly to cyclotomic multiple polylogarithms, and PC-103 proves that every finite cyclically separated Hardy cycle is linearly reducible with only cyclotomic letters. The odd/even incidence distinction changes the reduction geometry but does not create an elliptic or otherwise new finite period class.

PC-104 removes the repeated-shell loophole for ordinary nonconstant mixed words: once one adjacent pair supplies a trace-class core, reciprocal closing edges and repeated shell labels still yield an absolutely convergent cyclotomic Euler integral and hence a cyclotomic-hyperlogarithmic trace. PC-106 closes the complementary constant-shell relative-moment side: for every fixed conductor `n`, every `Tr(T_n^k)` and every Taylor coefficient of `det(I-zT_n)` lies in the same finite-conductor cyclotomic period algebra.

PC-107 then attacks the infinite determinant rather than its coefficients. Because `T_n` is self-adjoint trace class, the nonzero Fredholm zeros satisfy

\[
\sum_{D_n(z)=0}|z|^{-1}<\infty,
\qquad
N_{D_n}(R)=o(R).
\]

Riemann zeros instead have `T log T` counting and divergent reciprocal sum. Thus no fixed-shell trace-class determinant can directly realize the Riemann ordinate divisor under an asymptotically linear geometric normalization. The obstruction is operator-ideal sparsity, not failure to compute more moments.

## What remains possible

The surviving Hardy route must therefore change scale **globally**, not merely increase finite word length. A genuinely all-shell coupling could alter the operator ideal, create a relative/noncompact object with Riemann-compatible spectral density, or organize shell interactions through a completion not determined by any fixed conductor. A Hilbert--Schmidt/regularized determinant scale is not excluded by the PC-107 counting argument, but its canonicity and arithmetic content would have to be derived rather than chosen because its zero density is compatible.

Any positive mechanism still needs an independent RH-relevant selector or sign theorem. Cyclotomic period complexity, a real Fredholm zero set, or an infinite product assembled by hand is not sufficient.

## Status / novelty

Cyclotomic hyperlogarithms, trace ideals, Fredholm determinants, and Riemann--von Mangoldt are classical. The persisted Prime-Circle content is the exact reduction of the canonical Hardy data to those classes and the resulting boundary: finite/fixed-shell Hardy information is either classical period data or trace-class spectral data with the wrong zero-density scale.

## Falsification criterion

Produce a finite ordinary Hardy trace covered by PC-103/PC-104 or a fixed-shell relative moment covered by PC-106 that escapes the stated cyclotomic hyperlogarithmic algebra, or a trace-class fixed-shell determinant whose zero divisor violates reciprocal summability. A positive advance should instead construct a genuinely global all-shell operator whose ideal/spectral scale is forced intrinsically and survives matched non-arithmetic controls.

## Lean-formalizable core

- Cycle-incidence linear reducibility reductions.
- Trace-class mixed-word ideal argument.
- Fixed-shell relative-moment cube reduction.
- Trace-class Fredholm reciprocal-zero summability and sublinear counting.
