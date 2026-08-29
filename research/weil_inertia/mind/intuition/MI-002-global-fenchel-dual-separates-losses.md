# MI-002 — Within support one, the exact global Fenchel dual separates optimization loss from information loss

**Evidence level:** proved for the variational identity; supported for the research redirect

## Core intuition

The support-one inertia program contains two different bottlenecks that should not be conflated. Screening is an **information loss**: some off-line configurations are exactly invisible. Fixed-block assembly is only an **optimization loss**: it throws away cross-boundary coordinates of a global variational witness even though those coordinates are available in the same data.

## Strongest justified principle

WI-012 gives the exact spectral Fenchel representation of the Gram defect

\[
\mathcal D(M)
=
\sup_{H=H^*,\,H\preceq2I}
\left[
\operatorname{tr}H(M-I)-\frac14\operatorname{tr}H^2
\right].
\]

Restricting `H` to be block diagonal gives exactly the pinching lower bound used in the fixed-block analysis. The boundary loss is therefore not an intrinsic limitation of the Montgomery--Taylor matrix; it is the consequence of forbidding cross-block coordinates of the witness.

A concrete globally coupled feasible class is supplied by connection-Laplacian edge weights with vertex capacities. Its optimization is a concave capacitated fractional-matching problem with an exact convex dual. Translation-covariant finite-range choices lead to a one-dimensional potential for which a Bellman/subaction inequality can certify the average with only endpoint loss.

This identifies the right support-one target:

\[
\text{local Gram information}
\to
\text{globally feasible Fenchel witness}
\to
\text{Bellman certificate}.
\]

It can improve how efficiently the known information certifies simple critical-line zeros. It cannot, by itself, recover horizontal depth erased by MI-001's screening symmetry.

## Evidence against overgeneralization

The exact Fenchel dual is classical convex spectral analysis, and the specific connection-Laplacian/Bellman route is already present in the public prior-art archive audited by WI-012. The remaining value is not novelty of the formulation but a precise separation of losses.

Nor does the existence of the global dual prove a better numerical proportion. A finite-range witness still needs a rigorous ground-state/Bellman certificate and the finite-`T` analytic splice. Failure of one witness family would not refute the unrestricted Fenchel identity.

## Status / novelty

The variational identity and the interpretation of block pinching are exact. The programmatic conclusion is supported: optimize globally **within** support one for quantitative gain, but do not expect that optimization to solve the qualitatively different screening obstruction.

## Falsification criterion

Refute the first part by showing that the fixed-block pinching bound cannot be realized as a restriction of the displayed Fenchel feasible set. Refute the programmatic separation by exhibiting a support-one Fenchel witness that distinguishes two configurations whose complete compressed Montgomery--Taylor matrices are exactly equal.

## Lean-formalizable core

- Scalar Fenchel conjugate producing the piecewise spectral defect function.
- Matrix lift for Hermitian spectral functions.
- Block-diagonal restriction equals the pinching sum.
- Feasibility and objective of the connection-Laplacian witness under vertex capacities.
