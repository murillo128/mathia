# MI-009 — Support-one bounded-depth scalar and pointwise-PSD matrix universality collapse to the Montgomery--Taylor extremal

**Evidence level:** proved for the support-one scalar and pointwise-PSD matrix classes covered by WI-145--WI-154; extremal input is literature-backed

## Core intuition

The bounded-depth signed-scalar central spike is not a genuine support-one escape. Real two-point universality already forces the real-gap Fourier transform into the classical nonnegative one-delta admissible cone, and the sharp Montgomery--Taylor/CCLM extremal theorem fixes the final support-one cost without requiring the spectral profile itself to be nonnegative.

A natural matrix enlargement does not help if positivity is retained pointwise on real gaps and the destination consumes the matrix in Loewner order or through positive states. Every quadratic compression is the same scalar extremal problem, and equality forces a fixed PSD channel factor times the scalar extremizer.

## Strongest justified principle

WI-145--WI-152 locate the finite-test versus broad-universality boundary and show quantitatively that signed spectral mass at bounded strip depth is squeezed toward a central layer. Those results left open a central spike whose height grows with depth.

WI-153 closes that escape at the actual support-one arithmetic interface. The real two-point census gives `H(x)>=0` for every real gap. Fejer inversion places `H` in the CCLM one-delta class: integrable, nonnegative, normalized at zero, with Fourier support in `[-1,1]`. The sharp CCLM theorem then forces the support-one cost to be at least the Montgomery--Taylor constant. No bound on the central spike and no proof `phi>=0` are needed.

WI-154 extends the same obstruction to continuous matrix kernels `R(x)` that are pointwise PSD on real gaps with entrywise Fourier support in `[-1,1]`. Applying the scalar extremal theorem to every quadratic compression gives the Loewner bound

`M(R) >= m_MT R(0)`.

Equality is rigid: `R(x)=R_MT(x)R(0)`. Thus noncommuting or varying channel structure cannot improve the constant inside this pointwise-PSD real-gap category, even when the Fourier-side matrix is indefinite.

## What remains possible

The Weil-inertia program is not closed. A serious support-one escape must leave at least one load-bearing hypothesis: use sign-indefinite matrix/joint information not positive under every real-gap compression, a nonlinear configuration functional, source-restricted zeta classes, higher correlations, or a justified support-greater-than-one interface. Existing Gram/inertia constructions already retain information outside the collapsed scalar cost.

The next question is therefore categorical, not a larger central spike: identify a source-forced joint or indefinite carrier whose final order theorem cannot be reduced to positive scalar compressions.

## Status / novelty

The Montgomery--Taylor/CCLM extremal, Fourier inversion, and Loewner compression arguments are classical. The persisted synthesis is the closure: **support-one source-free universality cannot beat Montgomery--Taylor through either a signed scalar profile or a pointwise-PSD matrix lift consumed positively**.

## Falsification criterion

Construct a scalar profile satisfying the WI-153 universal census with support-one cost below `C_MT`, or a pointwise-PSD matrix kernel satisfying WI-154 whose positive-state/Loewner cost beats the scalar extremal. A sign-indefinite or source-restricted matrix carrier lies outside the theorem.

## Lean-formalizable core

- Real two-point positivity of the real-gap kernel.
- Reduction to the one-delta admissible cone.
- Scalar Montgomery--Taylor lower bound.
- Quadratic-compression proof of the matrix Loewner bound.
- Equality rigidity to a fixed PSD channel factor.
