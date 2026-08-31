# MI-005 — Finite test families have independent scale, dimension, and admissibility gates

**Evidence level:** supported by exact reconstruction, local programming, constrained-cone jet freedom, and Beurling deformation fibers

## Core intuition

A test family can fail for three different reasons. Restricting where tests live creates a **scale horizon**; retaining only finitely many test values creates a **resolution horizon** inside the visible scale; and imposing admissibility conditions helps only when those conditions actually shrink the response quotient seen by the source. Singular isolation of one source point is not by itself evidence of arithmetic fidelity, because a flexible test class can manufacture such isolation around an arbitrary source.

## Strongest justified principle

AF-020 gives the positive endpoint: the complete Weil functional on `C_c^\infty(0,\infty)` determines the prime-power measure and hence the unordered generalized-prime norm multiset. Restricting support to `(0,A)` has an exact interpretation: generators beyond `e^A` are invisible.

AF-021--AF-023 separate finite-dimensional resolution from scale. Any fixed `d` scalar tests admit exact generalized-prime collisions; at a regular `N>d` source point the same-test fiber through the point has positive dimension. Thus ordinary rational primes cannot be locally identifiable there unless the source point is singular or the admissible category removes the ambient deformation directions.

AF-024 shows why singularity alone is not enough. In the unconstrained smooth class, local one-generator response germs can be programmed independently at any finite nonresonant block, and one nonnegative test can make an arbitrary chosen source an isolated exact point with vanishing Jacobian and positive Hessian. Pointwise rigidity can therefore be source-tuned rather than source-specific.

AF-025 sharpens the admissibility audit. The local experiment has a large exact measurement kernel. Finite linear constraints, moments, evenness, pointwise nonnegativity, and a finite normalization can be repaired inside that kernel and need not restrict the source experiment at all. The right invariant is the constraint induced on the quotient by the measurement kernel, not the formal strength of the condition on the test function.

AF-026--AF-027 then show that even compact support, normalization, Fourier positivity/positive definiteness, and simultaneous pointwise plus Fourier positivity leave full-dimensional finite raw-jet and Weil-response-jet freedom at every finite nonresonant block. These results do not prove arbitrary exact germ programming inside the double-positive cone, but they rule out the idea that those natural positivity constraints alone create finite-order prime rigidity.

## What remains possible

Finite-test fidelity can still arise from a genuinely global admissible class, a nonlocal transform relation, an exact infinite-dimensional coupling among test values, or a source restriction that removes the Beurling deformation fiber. Such a mechanism must be specified before the rational-prime point is selected and must constrain the **measurement quotient itself**, not merely impose conditions that can be corrected in invisible directions.

The surviving question is therefore no longer whether a singular finite-test point or a standard positivity cone can isolate the primes. It is whether a mathematically forced global test/source category destroys the programmable local freedom and gives exact source identifiability.

## Status / novelty

The measure-determination, constant-rank, local smooth-programming, quotient-kernel, and positive-definite modulation ingredients are exact persisted findings with classical analytic/convex inputs. Their synthesis is a supported fidelity gate, not a theorem about every explicit-formula test class.

## Falsification criterion

Produce exact local prime-specific isolation in an audited admissible class while the class still has the AF-024/AF-027 response freedom, or prove that one of the listed finite constraints reduces the local response image to a lower-dimensional locus contrary to AF-025--AF-027. A positive advance should instead prove isolation in a genuinely global constrained category or source class and identify the exact quotient mechanism responsible.

## Lean-formalizable core

- Finite-test Jacobian/fiber dimension.
- Measurement-kernel quotient criterion for linear constraints.
- Construction of exact local smooth response germs.
- Full-dimensional finite-jet images under positive-definite modulation families.
