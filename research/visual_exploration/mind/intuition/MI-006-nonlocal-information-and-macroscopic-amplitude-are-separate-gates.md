# MI-006 — Source specificity begins after the one-window stochastic floor and cross-window dependence are both priced

**Evidence level:** exact finite-CUE mean/covariance reductions and point-process identifiability boundary through VIS-139

## Core intuition

A correct finite-CUE mean is not enough to expose a shrinking arithmetic residual. The bounded support-edge statistic has a genuine one-window stochastic floor, so detection at scale `1/L` requires averaging across source windows. That immediately makes the cross-window dependence law part of the null model.

## Strongest justified principle

VIS-130--VIS-132 correct the window convention and remove the samplewise diagonal mode. VIS-133 shows that bounded edge amplitudes retain order-one normalized covariance. VIS-134--VIS-135 identify the Wick contribution and prove a nondegenerate Gaussian terminal packet for fixed-window CUE, excluding self-averaging of any nontrivial fixed contrast.

VIS-136 translates the covariance tail into the required averaging exponent, while VIS-137 shows that one fixed-ratio circle contains only finitely many disjoint translated windows. VIS-138 proves that identical one-window marginals can coexist with arbitrary cross-window dependence. VIS-139 makes the missing information order explicit for disjoint quadratic statistics: after contractions vanish, covariance depends on a four-level relation not fixed even by all three-level inclusion data.

## Program consequence

Freeze the one-window CUE null, then move to the actual zeta source process and prove the multi-height covariance/mixing theorem needed by the declared averaging schedule. Pair correlation alone is not enough unless a rigorous closure principle reduces the required four-level term.

## Counterevidence / boundary

The four-level requirement is a general identifiability statement, not a claim that zeta has pathological dependence. Determinantal/Gaussian closure or sufficiently strong n-level results might supply the needed estimate in the relevant support regime, but that transfer has not been established.

## Epistemic status

**The fixed-window stochastic null is nondegenerate and the cross-window gate is genuinely higher-order; the zeta-side dependence law remains open.**

## Falsification criterion

Show that the declared disjoint quadratic statistic's covariance is determined by two- or three-level data under the exact source model without an additional closure theorem, or derive a direct zeta mixing bound strong enough to bypass the four-level expansion.