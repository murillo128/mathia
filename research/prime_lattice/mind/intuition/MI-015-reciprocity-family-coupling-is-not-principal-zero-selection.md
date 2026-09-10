# MI-015 — Canonical global arithmetic needs a nonfactorizing relation to constrain the principal zeta divisor

**Evidence level:** exact adelic/Artin block splitting, finite-dimensional representation-functor closure, and global Rankin--Selberg positive matched control through PL-252

## Core intuition

Prime Lattice does not lack canonical global arithmetic data, nonlinear representation operations, or positive global constructions. The recurring failure is more specific: the Riemann zeta contribution remains a factor or direct summand that the richer source structure does not constrain.

Thus “couple more arithmetic data” is still too weak. The required mechanism must be **nonfactorizing at the target theorem**: its sign, duality, spectral, or geometric relation must act across the richer source in a way that yields an unavoidable statement about the principal zeta divisor itself.

## Strongest justified principle

PL-249--PL-250 supply canonical class-field/Frobenius geometry and then keep the full finite abelian cover. The regular representation still decomposes into character blocks, and the trivial character remains exactly the `zeta_Q` factor.

PL-251 removes the abelian/linear loophole for a large canonical class. For any finite Galois group and finite-dimensional complex representation `W`, the averaging projector splits `W=W^G direct-sum W_0`; ordinary Artin formalism therefore factors `L(s,W)=zeta(s)^{dim W^G}L(s,W_0)`. Tensor products, duals, tensor powers, symmetric/exterior powers and Schur functors may create invariant tensors, but those invariants still split as copies of the trivial representation before the Artin determinant is read out.

PL-252 tests a different category: the canonical Rankin--Selberg self-correlation of a level-one Hecke form. Its completed self-convolution has nonnegative coefficients, a positive geometric integral for real `s>1`, analytic continuation and central functional-equation symmetry, yet factors as `zeta(s)L(s,sym^2 f)`. Since the companion is entire, every hypothetical off-line Riemann zero remains a zero of the positive global object. Positivity before continuation does not become critical-strip localization merely because zeta is a factor.

## Program consequence

Seek a source-forced global relation whose decisive theorem cannot be decomposed into an unconstrained principal zeta factor times companions. Relative trace/period formulas, cohomological correspondences, or genuinely global Hermitian positivity are relevant only if one can show where factorization is broken and how the resulting constraint survives analytic continuation into the principal divisor.

## Counterevidence / boundary

PL-251 concerns ordinary finite-dimensional representation-category functors and Artin `L`-readout; PL-252 concerns one canonical Rankin--Selberg self-correlation. Neither rules out infinite-dimensional dynamics, relative trace formulas, nonlinear geometric correspondences, or Weil-type global test-function positivity. Factorization also does not prove that no theorem about the whole object can constrain one factor; it proves that the standard positivity/functorial structure tested so far does not.

## Epistemic status

**Exact principal-factor isolation across finite representation functors plus a positive global automorphic matched control; a source-forced nonfactorizing critical-strip relation remains open.**

## Falsification criterion

Produce a construction inside the PL-251 or PL-252 classes whose established positivity/symmetry alone forces the inherited zeta divisor onto the critical line, or invalidate their exact factorization. A positive continuation should derive a canonical relation whose target consequence cannot leave `zeta(s)` as a freely inherited factor.
