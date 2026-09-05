# MI-004 — Complete scalar five-point control is now a residual unequal-height Montgomery--Taylor zero-freeness problem

**Evidence level:** supported through ANF-057 by exact defect reductions, compactness, perturbative notch asymptotics, a global equal-height curvature gate, and support-free unequal-height stability cones

## Core intuition

The complete scalar cardinality-five problem has narrowed from generic anti-phase coherence danger to one fixed base-kernel question on an intermediate mismatch region. A narrow central notch does not create the decisive positivity margin: its leading perturbation universally lowers the five-point defect. The notch family therefore survives exactly when the underlying Montgomery--Taylor two-pair defect is already zero-free on the residual obstruction set.

The diagonal neighborhood is now substantially closed without support-dependent deterioration. Equal-height configurations are globally positive, and retaining the positive quadratic mismatch block gives a fixed relative-height tube at every mean height. A sharper reciprocal-sinh comparison pushes the universal support-free radius to `q_*=0.129209...`; the strict Montgomery--Taylor curvature margin pushes the profile-specific exclusion beyond `q=0.1409`, where `q=|y_1-y_2|/(y_1+y_2)`.

## Strongest justified principle

ANF-043--ANF-051 reduce scalar five-point negativity to a compact balanced-height, finite-separation, near-anti-phase regime. ANF-052--ANF-053 show that central-notch modifications are perturbatively small there and that their leading contribution has the wrong sign to repair a genuine base zero.

ANF-054 proves a global equal-height curvature gate. ANF-055 obtains the first explicit unequal-height tube. ANF-056 improves the mechanism by retaining the positive quadratic mismatch block rather than paying a support-edge hyperbolic envelope, yielding a support-free fixed relative-height cone and an exact horizontal-free mismatch-loss functional.

ANF-057 sharpens that loss globally. For a nonnegative profile with `m_5(J)>=0`, every configuration with `q<q_J` is positive, with a universal minimum `q_*=0.1292091881...`. For the fixed Montgomery--Taylor profile, the already-certified strict diagonal margin gives `q_MT>0.1409`, so a genuine base zero must satisfy `y_max/y_min>1.3280`. The coefficient controlling this horizontal-free comparison is small-frequency sharp, so further widening requires genuinely new information rather than another scalar envelope optimization.

## What remains possible

The direct scalar route is now a theorem about the fixed Montgomery--Taylor defect on the residual intermediate-mismatch set. Prove zero-freeness there or exhibit a genuine zero. The earlier scale-free height/separation restriction should be kept simultaneously rather than reopening regions already excluded.

A sharper continuation may retain horizontal phase/separation information discarded by the present all-horizontal bound, use a stronger profile-specific diagonal estimate, or analyze the exact two-variable mismatch-loss integral for the Montgomery--Taylor profile. Matrix/inertia, higher-correlation, or non-scalar carriers remain outside this scalar reduction.

## Status / novelty

The Montgomery--Taylor kernel, Fourier positivity, hyperbolic inequalities, compactness, and curvature estimates use classical analytic ingredients. The persisted synthesis is the exact boundary: **equal heights and a fixed support-free relative-mismatch cone are closed globally; the remaining scalar question is genuine zero-freeness of the fixed Montgomery--Taylor defect on an intermediate unequal-height region, and the present horizontal-free coefficient is already sharp at small frequency**.

## Falsification criterion

Exhibit a Montgomery--Taylor two-pair zero with `q<=0.1409`, refute the ANF-054 diagonal margin or ANF-056/057 mismatch inequalities under their stated hypotheses, or prove that the residual region is zero-free. A stronger phase-aware theorem would extend rather than falsify the synthesis.

## Lean-formalizable core

- Equal-height curvature lower bound.
- Mean-height/half-mismatch decomposition and retained positive mismatch block.
- Support-free reciprocal-sinh mismatch envelope.
- Profile-dependent radius `q_J` and Montgomery--Taylor specialization.
- Leading central-notch perturbation and zero-instability implication.
