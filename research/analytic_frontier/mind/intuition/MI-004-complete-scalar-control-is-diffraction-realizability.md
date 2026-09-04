# MI-004 — Complete scalar control is a diffraction-realizability problem; five-point local geometry is curvature-gated and finite-height coupling remains

**Evidence level:** supported through ANF-041 by exact finite-configuration reductions and positive-definite curvature constraints

## Core intuition

For universal support-one scalar pair certificates, finite-real stability is not the final control. Complex conjugation introduces genuinely new horizontal--vertical geometry, but cardinality five is now locally classified: both irreducible five-point complex patterns have the same sharp small-height curvature gate.

The remaining scalar question is therefore not another local Taylor coefficient. It is whether the genuinely coupled two-conjugate-pair geometry can reverse sign at finite joint height even when the local curvature margin is nonnegative.

## Strongest justified principle

ANF-018--ANF-034 reduce complete finite-real stability to a pair-potential/diffraction-realizability problem and construct an explicit central-notch support-one ray beating the Montgomery--Taylor finite-real ratio. ANF-035--ANF-036 show that every conjugation-invariant configuration through four points collapses to real controls.

ANF-037--ANF-039 classify one conjugate pair plus three real anchors. Its defect is nonnegative at every height exactly when the curvature margin

`m_5(J)=2K_J(0)+3 inf_t K_J(t)`

is nonnegative. Montgomery--Taylor and a sufficiently small central-notch perturbation have strict positive margin and pass this entire one-pair layer.

ANF-040 identifies the last irreducible cardinality-five pattern: two conjugate pairs plus one real point. It proves that the sign of `m_5` is sharp when strict: positive margin gives a uniform small-height collapse neighborhood, while negative margin creates genuine two-pair reversals arbitrarily close to the real axis.

ANF-041 closes the equality boundary. Because the curvature kernel is positive definite, its three-point Gram constraint prevents both quadratic brackets from flattening simultaneously; when one height becomes too small to use that margin, the pure quartic self-energy of the larger pair is uniformly positive. Hence

`m_5(J)>=0`

is the exact local cardinality-five complex criterion for both irreducible geometries.

## What remains possible

A decisive scalar continuation should analyze the full finite-height two-pair minimum, including the central-notch separator and the admissible affine/multiplicity slack, rather than enlarge the finite-real family or repeat small-height expansions. A positive theorem would extend local curvature control to all joint heights; a counterexample would identify the first genuinely finite-height complex obstruction.

A non-scalar carrier can still evade this boundary by retaining matrix, inertia, source-specific, or higher-correlation information before scalar diffraction compression.

## Status / novelty

Positive-definite Fourier representation, Gram constraints, and pair-potential stability are classical. The persisted synthesis is the boundary shift: **cardinality-five local complex geometry is completely controlled by `m_5`; any remaining five-point scalar obstruction must be genuinely finite-height and two-pair coupled**.

## Falsification criterion

Produce a nonnegative compact-band spectrum with `m_5(J)>=0` and a negative two-pair defect arbitrarily close to the real axis, contradicting ANF-041, or prove the full finite-height two-pair defect nonnegative under the same curvature gate.

## Lean-formalizable core

- One-pair all-height curvature criterion.
- Two-pair local `m_5>=0` criterion including equality.
- Three-point curvature Gram inequality.
- Quartic fallback in the asymmetric-height regime.
- Separation between local curvature control and global finite-height coupling.
