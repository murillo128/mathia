# MI-009 — Stable analytic novelty must beat the held-out-prime collision baseline

**Evidence level:** proved representation criterion plus quantitative matched null; zeta separation remains open

## Core intuition

Exact finite prime phases contain set-theoretic height information that no stable decoder can necessarily use. The exact Lipschitz decoder cost is the phase-collision quotient, but the newest evidence shows that large or even polynomially growing collision complexity is not automatically zeta-specific: an ordinary omitted prime frequency already produces it.

The meaningful source question is therefore **relative**. A zeta-facing coordinate must separate quantitatively from held-out-prime recurrence under the same representation budget.

## Strongest justified claim

VIS-161 proves that two exact prime phases identify real height while the inverse on the dense torus orbit is nowhere continuous. VIS-162 shows that, for fixed support `P`, the optimal exact Lipschitz decoder constant for an observable `A` is exactly

`Lambda_P(A;S)=sup_(t!=u) |A(t)-A(u)|/||Phi_P(t)-Phi_P(u)||`.

VIS-163 supplies a decisive null model. If `r` is a prime omitted from `P`, the phase `r^(-it)` has no continuous decoder from the retained torus, its orbit decoder is nowhere continuous, and its global Lipschitz collision quotient is infinite. Thus qualitative decoder failure can mean nothing more than frequency omission.

VIS-164 anchors one retained phase exactly and computes the limiting collision law for the omitted prime. If `d=|P|-1`, fixed-threshold exceedances converge to a Haar law with tail `c_d L^(-d)`. The heavy-tail exponent is the retained support dimension, not a zero-side invariant.

VIS-165 crosses the fixed-threshold limitation in a rigorous range. Linear-form lower bounds make the prime-log rotation finite Diophantine type; discrepancy theory then gives polynomial equidistribution error. Consequently the held-out-prime exceedance law remains valid for sufficiently slowly growing polynomial thresholds and forces positive-power growth of finite-window Lipschitz complexity.

## Synthesis of evidence

The correct experimental/theoretical object is now a normalized comparison. Freeze retained support, anchor convention, torus metric, height window, observable normalization, and threshold law. Compare the zeta-facing collision profile with one or more held-out-prime controls matched in frequency/scale. Only an excess beyond the dimension-coded Haar/discrepancy baseline is evidence of additional analytic structure.

Alternatively let the retained support grow and prove a uniform separation that survives changing torus dimension and recurrence scale. Simply increasing support without controlling that geometry does not remove the null.

## Counterevidence / boundary cases

VIS-165 supplies only an existence exponent depending on the fixed prime set and a conservative threshold-growth regime, not an extreme-value law. A zeta observable could match the held-out-prime tail at fixed support yet separate in another regularity class, joint statistic, or growing-support regime.

The criterion remains metric- and decoder-class-specific. Other stable representation classes require their own matched null and extension theorem.

## Epistemic status

**Exact criterion plus quantitative omitted-source null:** stable decoder complexity is measurable directly from collisions, but fixed-support divergence and even some polynomial growth are already classical consequences of omitting one prime frequency. Source sensitivity requires quantitative separation from that baseline.

## Novelty/prior-art status

Kronecker--Weyl theory, linear forms in logarithms, discrepancy bounds, and Lipschitz extension remain classical as recorded in the findings. This intuition synthesizes the resulting control standard for visual research.

## Falsification criterion

Construct a continuous finite-support decoder for an omitted prime, invalidate the Haar tail or polynomial discrepancy regime of VIS-164--VIS-165, or show that a proposed zeta separation disappears when compared under the same held-out-prime normalization. A robust excess over that matched baseline would cross the current gate.