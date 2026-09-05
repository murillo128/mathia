# MI-004 — Complete scalar control is a diffraction-realizability problem; the last five-point obstruction is compact-height coherence

**Evidence level:** supported through ANF-043 by exact finite-configuration reductions, positive-definite curvature constraints, a sharp pointwise self-energy floor, and uniform height coercivity

## Core intuition

For universal support-one scalar pair certificates, finite-real stability is not the final control. Complex conjugation introduces genuinely new horizontal--vertical geometry, but cardinality five is now sharply localized: both irreducible local complex patterns are controlled by the curvature gate, and the remaining two-pair pattern cannot escape to arbitrarily small or large conjugate heights once that gate is nonnegative.

The unresolved scalar problem is therefore a **bounded interior-height cross-frequency coherence problem**. Individual frequencies can still favor a reversal, but neither local splitting nor vertical escape supplies one.

## Strongest justified principle

ANF-018--ANF-034 reduce complete finite-real stability to a pair-potential/diffraction-realizability problem and construct an explicit central-notch support-one ray beating the Montgomery--Taylor finite-real ratio. ANF-035--ANF-039 then classify one conjugate pair plus three real anchors: its defect is nonnegative at every height exactly when

`m_5(J)=2K_J(0)+3 inf_t K_J(t)>=0`.

ANF-040--ANF-041 identify the last irreducible cardinality-five pattern, two conjugate pairs plus one real point, and prove that the same `m_5>=0` condition is the exact small-height criterion, including the equality case. Positive-definite Gram rigidity prevents a hidden zero-margin local escape.

ANF-042 gives the exact pointwise normal form for this two-pair geometry. A single frequency can still be harmful, but the defect has a sharp self-energy floor; local negativity therefore does not by itself assemble into an integrated counterexample.

ANF-043 closes the opposite vertical boundary. For every nonzero continuous compactly supported spectrum `J>=0`, the integrated two-pair defect tends to `+infinity` uniformly in horizontal placement when either conjugate height tends to infinity. Under `m_5(J)>=0`, any negative defect must satisfy

`epsilon_J <= y_1,y_2 <= Y_J`

for source-independent positive constants depending only on `J`. The Montgomery--Taylor profile and the current central-notch separator both lie in this compact-height regime.

## What remains possible

A decisive scalar continuation must resolve the full two-pair minimum inside that bounded height region while retaining the common horizontal phase/separation across frequencies and the admissible affine/multiplicity slack. A positive theorem would show that interval-frequency coherence plus `m_5>=0` prevents every interior reversal; a counterexample would be an explicit finite-height two-pair configuration for a spectrum already passing the local gate.

More finite-real configurations, another Taylor expansion at height zero, or an asymptotic large-height search no longer change the frontier. A non-scalar carrier can still evade it by retaining matrix, inertia, source-specific, or higher-correlation information before scalar diffraction compression.

## Status / novelty

Positive-definite Fourier representation, Gram constraints, pair-potential stability, and elementary hyperbolic/trigonometric coercivity are classical ingredients. The persisted synthesis is the boundary shift: **for `m_5>=0`, every remaining cardinality-five scalar obstruction is a genuinely finite-height, two-pair cross-frequency coherence phenomenon**.

## Falsification criterion

Produce a nonnegative compact-band spectrum with `m_5(J)>=0` and a negative two-pair defect arbitrarily near height zero or along a sequence with one height tending to infinity, contradicting ANF-041/ANF-043; or prove the full compact-height two-pair defect nonnegative under the same curvature gate.

## Lean-formalizable core

- One-pair all-height curvature criterion.
- Two-pair local `m_5>=0` criterion including equality.
- Pointwise two-pair self-energy floor.
- Uniform large-height coercivity.
- Compact-height localization of every remaining negative defect.
