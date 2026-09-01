# MI-005 — Hardy nonlocality survives, but finite cycle periods remain cyclotomic and incidence-controlled

**Evidence level:** supported by exact operator classifications, finite-trace formulas, and the cubic period reduction

## Core intuition

The canonical Hardy interior/exterior split genuinely escapes Prime Circle's cotangent endpoint closure: the logarithmic cyclotomic potential becomes a nonlocal Hankel operator. Its noncompact spectral core is nevertheless universal. Arithmetic survives below the essential level in trace-class mixed words, but the new evidence pushes their finite cycle structure toward classical cyclotomic multiple-period data rather than toward an independent RH spectral parameter.

## Strongest justified principle

PC-075 and PC-081 classify the essential layer. Each primitive-shell Hardy operator is a finite combination of generalized Hilbert channels plus trace-class remainder, and any finite family has a joint Calkin algebra that is a wedge of independent universal Hilbert bands. Finite algebraic coupling therefore cannot create a new joint arithmetic essential spectrum.

The relative layer is richer but controlled. PC-082 gives exact cone/cube period formulas beyond pairwise resultants; PC-084 and the corrected PC-086 give the corresponding trace-class and finite-section convergence boundary for genuinely mixed separated words. Common repeated-prime depth factors as a universal finite tensor component rather than a new interaction variable.

PC-100 identifies the first nontrivial cycle period explicitly: cubic Hardy cycle traces are weight-three cyclotomic multiple polylogarithms. This is a real nonlocal finite interaction, but it belongs to an established cyclotomic-period category rather than defining a new spectral arithmetic algebra by itself.

PC-101 then isolates the combinatorics for all separated cycles. The denominator-index map is the unsigned incidence matrix of a cycle. Odd cycles have determinant `2` and parity-coset uniqueness; even cycles have a one-dimensional alternating kernel and explicit fiber multiplicity. In particular, the quartic trace acquires a genuine relation such as `r+t=s+u` with a multiplicity factor rather than reducing immediately to the cubic pattern. The remaining finite-period question is therefore precise: determine whether the `k>=4` incidence-constrained sums reduce to known cyclotomic multiple-polylogarithmic/conical period spaces or create a genuinely larger canonical period algebra.

## What remains possible

Higher finite traces may contain arithmetic beyond endpoints and pairwise resultants, but a positive result must first survive the cyclotomic-period audit. Even a larger finite period algebra would still need an independently derived RH selector, sign theorem, or analytic parameter. A truly infinite all-shell coupling could organize the finite periods in a way not visible at any finite Calkin level, but fixed-state rational wrappers and canonical complete-tube limits are already controlled by PC-098--PC-099.

## Status / novelty

The Hilbert-channel classification, trace-class mixed products, cubic multiple-polylogarithm reduction, and cycle-incidence formulas are persisted exact findings. Cyclotomic multiple polylogarithms and conical periods are established prior art; no theorem-level novelty is inferred merely from their appearance here.

## Falsification criterion

Construct a finite mixed word whose essential class contains shell interaction, contradicting PC-081, or show that the cubic trace escapes the weight-three cyclotomic multiple-polylogarithm space, contradicting PC-100. A positive finite advance should characterize the `k>=4` period space and prove a component not already forced by classical cyclotomic-period theory.

## Lean-formalizable core

- Trace-class ideal argument for mixed shell words.
- Cycle incidence determinant/rank classification.
- Parity-coset solution count for odd cycles.
- Alternating-kernel fiber description for even cycles.
