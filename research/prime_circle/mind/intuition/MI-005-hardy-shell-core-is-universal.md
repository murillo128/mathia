# MI-005 — Hardy nonlocality survives, but its finite essential core is universal and its finite relative sector is cyclotomic-period data

**Evidence level:** supported by exact operator classifications and finite-trace formulas

## Core intuition

The canonical Hardy interior/exterior split genuinely escapes Prime Circle's earlier modewise scalarization: the logarithmic cyclotomic potential becomes a nonlocal Hankel operator. Its noncompact spectral core is nevertheless universal. Arithmetic survives below the essential level, in trace-class interactions whose finite-word traces are canonical and richer than pairwise resultants, but still sit inside explicit cyclotomic-period geometry rather than a demonstrated RH selector.

## Strongest justified principle

PC-075 decomposes each primitive-shell Hardy operator into finitely many generalized Hilbert channels plus a trace-class remainder; for `n>2` the essential spectrum is the universal band `[-pi,pi]`. PC-081 shows that for any finite family of distinct shells every genuinely mixed algebraic word is trace class and the joint Calkin algebra is a wedge of independent universal Hilbert bands. Finite algebraic coupling cannot create a new joint arithmetic essential spectrum.

The relative sector is stronger than the earlier pairwise picture. PC-082 proves that higher cyclic traces are exact cyclotomic cone/cube periods and supplies a control showing information beyond pairwise resultants. The corrected PC-086 establishes the ordinary operator-trace statement at the precise root-channel boundary: cyclically separated root words of length at least two are trace class and their natural finite Hardy sections converge in trace norm to the ordinary trace. A one-letter separated scalar finite-section sum can converge without making the underlying Hilbert channel trace class, so scalar convergence must not be confused with an operator trace. PC-084 supplies the corresponding trace-norm convergence mechanism for the completed-shell finite-word sector.

PC-085 identifies a large universal direction inside that richer algebra. Repeated prime-power depth common to every conductor in a finite word factors simultaneously as a finite involutive tensor component. It changes multiplicity/sign in a universal way but not the residual mixed Hardy interaction. The potentially informative variables are therefore in the primitive/radical interaction pattern, not common repeated depth.

## What remains possible

Higher finite trace periods may encode arithmetic beyond endpoints and pairwise resultants, and an infinite all-shell coupling could organize them in a way not visible at any finite Calkin level. Neither fact supplies an RH spectral parameter, functional equation, or sign theorem. A surviving mechanism must show that the relevant period package is not just known cyclotomic/conical-period data and then derive an independently meaningful zero selector.

## Status / novelty

The Hilbert-channel classification, trace-class mixed products, corrected finite-section convergence, higher cone-period formulas, and common-depth tensor factorization are persisted exact findings. Neighboring conical/cyclotomic period theories are established prior art; no theorem-level historical novelty is inferred from the synthesis.

## Falsification criterion

Construct a finite algebraic combination whose essential class contains genuinely mixed shell information, contradicting PC-081, or produce a cyclically separated one-letter Hilbert channel that is trace class, contradicting the corrected boundary in PC-086. A positive advance would instead derive an all-level invariant whose arithmetic content cannot be reduced to the documented finite period/classical packages.

## Lean-formalizable core

- Trace-class ideal argument for mixed shell words and finite-section convergence at length at least two.
- Quotient algebra decomposition into one-shell branches.
- Simultaneous common-depth tensor factorization.