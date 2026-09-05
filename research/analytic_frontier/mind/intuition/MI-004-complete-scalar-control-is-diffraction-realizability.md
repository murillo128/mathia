# MI-004 — Complete scalar five-point control is now an unequal-height Montgomery--Taylor zero-freeness problem

**Evidence level:** supported through ANF-055 by exact defect reductions, compactness, perturbative notch asymptotics, a global equal-height curvature gate, and an explicit unequal-height stability tube

## Core intuition

The complete scalar cardinality-five problem has narrowed from a generic anti-phase coherence danger to one precise base-kernel question. A narrow central notch does not create the decisive positivity margin: its leading perturbation universally **lowers** the five-point defect. Consequently the notch family survives exactly when the underlying Montgomery--Taylor two-pair defect is already zero-free on the compact obstruction set.

The geometry is also no longer symmetric between equal and unequal heights. Equal-height two-pair configurations are globally positive under the natural `m_5(J)>=0` gate, uniformly over all horizontal frequencies. An explicit neighborhood of that diagonal remains positive for unequal heights. Any surviving scalar obstruction must therefore live in the remaining compact unequal-height region.

## Strongest justified principle

ANF-043--ANF-051 reduce scalar five-point negativity to a compact balanced-height, finite-separation, near-anti-phase regime. ANF-052 shows that central-notch modifications are perturbatively small there.

ANF-053 identifies the decisive sign of that perturbation. For `J_{eta,s}=J_MT-s phi_eta`, the leading notch contribution is a negative quadratic-height term of order `eta^3`; horizontal/anti-phase structure first enters later. Thus any genuine zero of the Montgomery--Taylor base defect is destabilized by a sufficiently narrow notch, whereas strict base positivity on the compactified obstruction set transfers to all sufficiently narrow notches.

ANF-054 proves a global curvature gate on the equal-height diagonal: for every nonzero continuous even nonnegative compactly supported kernel with `m_5(J)>=0`, the two-pair five-point defect is strictly positive for every positive height and all horizontal frequencies. ANF-055 decomposes unequal heights into mean height and mismatch and gives an explicit positive tube around that diagonal. The unresolved scalar set is therefore compact, unequal-height, and separated from the certified tube.

## What remains possible

The direct scalar route now asks for a theorem about the fixed Montgomery--Taylor base defect, not for another notch parameter search. Prove zero-freeness on the residual compact unequal-height set, or find a genuine zero there. Either outcome transfers immediately to the fate of all sufficiently narrow central-notch variants.

A different kernel family can remain relevant only if it changes the base defect mechanism rather than relying on the same narrow-notch perturbation. Matrix/inertia, higher-correlation, or non-scalar carriers remain outside this scalar reduction.

## Status / novelty

The Montgomery--Taylor kernel, Fourier positivity, compactness arguments, and curvature estimates use classical analytic ingredients. The persisted synthesis is the exact boundary: **equal-height coherence is closed, near-diagonal unequal heights are quantitatively safe, and narrow central notches live or die with genuine zero-freeness of the fixed base defect on the residual compact set**.

## Falsification criterion

Exhibit a genuine zero of the Montgomery--Taylor two-pair defect in the residual compact unequal-height region, or prove it has none. A counterexample to the equal-height lower bound or to the explicit ANF-055 stability tube under their stated hypotheses would falsify the corresponding reductions.

## Lean-formalizable core

- Equal-height curvature lower bound.
- Mean-height/half-mismatch decomposition.
- Explicit unequal-height stability inequality.
- Leading central-notch perturbation and zero-instability implication.
