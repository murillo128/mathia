# MI-001 — Visual residuals must survive reconstruction and matched maximum-entropy/statistical controls

**Evidence level:** supported through VIS-020 by exact reconstruction identities, literature-backed finite-size spacing baselines, and an exact information-theoretic closure

## Core intuition

Visual complexity is not an independent arithmetic resource when it can be reconstructed from coordinates, divisor data, regular holomorphic continuation, phase gauge, or lower-order probability laws. The meaningful object is the residual after the strongest baseline that preserves the information already known to generate the picture.

VIS-020 makes this precise for three consecutive gaps. Once the two overlapping adjacent-pair marginals are fixed, there is a unique maximum-entropy completion. Generic non-Markov dependence is therefore not an arithmetic signal; the zeta question begins only after comparing its departure from that closure with the corresponding departure of a matched finite-size random-matrix/arithmetic control.

## Strongest justified principle

VIS-013--VIS-017 classify complete circular modulus/phase data and connected overlap gluing as zero sources plus harmonic boundary data with one global `U(1)` gauge. VIS-018 closes the topological phase escape: argument-principle winding and local vortex charge are exactly enclosed zero/pole multiplicity.

VIS-019 adds the finite-size statistical control. Adjacent unfolded-gap return maps, two-gap densities, nearest-neighbor anti-correlation, and ratio histograms already have finite-size CUE baselines with known arithmetic corrections in the relevant channels.

VIS-020 fixes the next information layer exactly. For finite-valued consecutive gaps `X,Y,Z`, the joint

`Q(x,y,z)=P_XY(x,y) P_YZ(y,z)/P_Y(y)`

is the unique maximum-entropy distribution with the prescribed adjacent-pair marginals, and

`D(P||Q)=I(X;Z|Y)=H(Q)-H(P)`.

Thus `P-Q` localizes conditional dependence beyond the two pair marginals, while conditional mutual information is its canonical nonnegative scalar distance. But a determinantal CUE process is itself not first-order Markov, so positive conditional mutual information on zeta alone proves nothing. The live statistic is the **zeta-minus-matched-control residual after each side is projected against its own maximum-entropy closure**.

## What remains possible

Higher-order or long-range residuals, deliberately incomplete measurements with quantified recovery defect, separated-region bridge observables, and non-holomorphic/multi-object representations remain live. They earn promotion only after the relevant reconstruction and lower-order statistical quotient is removed and the residual is stable across partition, height, finite-size, and rendering controls.

## Status / novelty

Complex-analysis reconstruction, finite-size random-matrix spacing theory, maximum entropy, relative entropy, and conditional mutual information are prior art. The synthesis is the strengthened visual gate: **match the complete generating baseline, including the maximum-entropy closure of retained marginals, before interpreting residual geometry as arithmetic**.

## Falsification criterion

Exhibit a visual/statistical invariant beyond the covered reconstruction and adjacent-pair maximum-entropy baseline that separates zeta from matched controls preserving the same lower-order data, with a statement independent of rendering choices.

## Lean-formalizable core

- Argument-principle winding as divisor count.
- Maximum-entropy Markov completion from two overlapping pair marginals.
- `D(P||Q)=I(X;Z|Y)` for the fixed-marginal family.
- Logical quotienting of reconstruction baselines before residual tests.
