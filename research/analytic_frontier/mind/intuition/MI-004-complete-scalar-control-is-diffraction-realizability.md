# MI-004 — Complete scalar control is a diffraction-realizability problem; the first one-pair complex layer is exactly a curvature gate

**Evidence level:** supported through ANF-039 by exact finite-configuration reductions, an explicit finite-real separator, and a rigorous Montgomery--Taylor curvature certificate

## Core intuition

For universal support-one scalar pair certificates, complete finite-real stability is not the final control. Complex conjugation can introduce genuinely new horizontal--vertical geometry, but the first such layer is now sharply classified rather than merely identified by cardinality.

One conjugate pair plus three real anchors does not create an independent finite-height obstruction. Its full all-height defect is controlled by one second-spectral-moment curvature margin. The exact Montgomery--Taylor spectrum has a strict positive margin, and a sufficiently small central-notch separator can keep its finite-real improvement while passing this entire complex layer. The remaining five-point obstruction is therefore the genuinely coupled geometry of two conjugate pairs plus one real point.

## Strongest justified principle

ANF-018--ANF-034 identify the finite-real boundary as a pair-potential stability/diffraction-realizability problem and construct an explicit central-notch support-one ray whose complete finite-real ratio beats Montgomery--Taylor. ANF-035--ANF-036 show that common vertical fibers and every conjugation-invariant configuration through four points collapse to real controls; five points are sharp for positivity-alone separation.

ANF-037 reduces the first five-point pattern, one conjugate pair plus three real anchors, to

`G_J(y)=A_y+3 inf_t L_y(t)`

and identifies the curvature margin

`m_5(J)=2K_J(0)+3 inf_t K_J(t)`.

ANF-038 proves rigorously that `m_5(J_MT)>0.0078` and that a sufficiently small central-notch perturbation can retain both finite-real gain and positive curvature margin. ANF-039 then closes the finite-height escape exactly:

`G_J(y) >= 2 pi^2 y^2 m_5(J)` for every `y>0`,

and `G_J(y)>=0` for all heights if and only if `m_5(J)>=0`. Every higher even-height correction in this geometry has favorable sign once the quadratic gate passes.

## What remains possible

The scalar branch is not closed. Cardinality five still contains the coupled pattern of two conjugate pairs plus one real point, whose structure factor has a mixed vertical term and does not decompose into independent anchor minima. Larger conjugation-invariant multisets, multiplicity slack, and source-admissible zeta restrictions remain separate gates.

A decisive continuation should derive the exact coupled two-pair criterion and test the central-notch ray against it before enlarging the finite-real control family again. Survival would move the burden toward genuinely source-specific complex constraints; failure would identify the missing complex obstruction explicitly.

## Status / novelty

Positive-definite Fourier--Laplace representation, pair-potential stability, and extremal-function theory are classical. The persisted synthesis is the boundary shift: **the first one-pair five-point complex layer is completely governed by a curvature margin, so complexity now begins with coupled complex fibers rather than finite height itself**.

## Falsification criterion

Produce a nonnegative compact-band spectrum with `m_5(J)>=0` but `G_J(y)<0` at some height, contradicting ANF-039, or show that the ANF-034 separator necessarily fails in the remaining two-pair-plus-one-real geometry. A richer non-scalar carrier would evade rather than falsify this intuition.

## Lean-formalizable core

- One-pair five-point structure-factor defect.
- Curvature margin `m_5` and all-height lower bound.
- Necessity/sufficiency of the curvature gate.
- Separation between independent-anchor and coupled-pair geometries.
