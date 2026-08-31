# MI-005 — Hardy nonlocality survives, but finite-shell essential coupling is a wedge of universal Hilbert bands

**Evidence level:** supported by exact operator classifications

## Core intuition

The canonical Hardy interior/exterior split genuinely escapes Prime Circle's earlier modewise scalarization: the logarithmic cyclotomic potential becomes a nonlocal Hankel operator that mixes Fourier modes. That escape is real, but its noncompact spectral core is still universal. Arithmetic survives below the essential level, in trace-class relative data, rather than in a new finite-shell essential spectrum.

## Strongest justified principle

PC-075 decomposes each primitive-shell Hardy operator into finitely many generalized Hilbert channels plus a trace-class remainder. For every `n>2` its essential spectrum is the universal band `[-π,π]`, with arithmetic entering only through channel multiplicities and the nuclear remainder.

PC-076 shows how aggressively the first relative invariant classicalizes: the trace of that remainder is exactly the parity-twisted von Mangoldt combination `1/2(Λ(n)-1_{2|n}Λ(n/2))`, equivalently the difference of the two cyclotomic endpoint potentials at `+1` and `-1`. PC-077--PC-080 further place higher or mixed finite relative data in radical/divisor/resultant and trace-class territory rather than producing a new essential carrier.

PC-081 closes the finite algebraic cross-shell escape at the Calkin level. For any finite family of distinct shells, every genuinely mixed word is trace class, and the generated essential algebra is a wedge of independent universal Hilbert bands glued only at zero. Finite noncommutative algebraic coupling therefore cannot create a joint arithmetic essential spectrum from the canonical shell operators.

## What remains possible

The surviving Hardy route is necessarily below or beyond that finite essential algebra: trace-class cyclic traces and relative determinants may contain arithmetic, and an **infinite all-shell coupling not generated algebraically by finitely many completed shell operators** could in principle have new behavior. Such an object still needs an RH-specific selector rather than merely another exact cyclotomic identity.

## Status / novelty

The Hankel decompositions, relative traces, trace-class mixed products, and Calkin wedge classification are persisted exact findings with classical operator-theoretic ingredients. The synthesis does not rule out infinite cross-level or genuinely new Hardy-type operators.

## Falsification criterion

Construct a finite algebraic combination of the canonical `Γ_n` whose essential class contains genuinely mixed shell information; this would contradict PC-081. A positive advance would instead derive an intrinsically infinite cross-level operator and show that its invariant cannot be reduced to Hilbert bands, endpoint values, divisor/radical data, or resultants.

## Lean-formalizable core

- Trace-class ideal argument for mixed shell words.
- Quotient algebra decomposition into one-shell branches.
- First relative-trace cyclotomic endpoint identity.
