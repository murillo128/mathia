# MI-001 — Screening is an information-bandwidth obstruction, not merely a loose matrix bound

**Evidence level:** proved within the audited Montgomery–Taylor/Alpöge–Furman compression

## Core intuition

The main obstruction in the current inertia route is not that one has failed to estimate the negative eigenvalue of an isolated off-line zero accurately enough. An isolated functional-equation pair does carry a depth-dependent negative direction, but a vertically organized family can **screen that direction exactly** in the compressed Weil geometry. Detecting horizontal displacement requires information that the support-one test family literally does not contain.

## Strongest justified principle

WI-005 computes the exact two nonzero eigenvalues of one off-line mirror pair and confirms that its negative mass grows with normalized horizontal depth. The same finding then places equally deep pairs on the critical vertical sampling lattice and proves that their full aggregate is positive semidefinite and independent of the depth; for the ideal flat window it is exactly `2I`.

WI-006 strengthens the interpretation by showing that the screened off-line lattice is matrix-equivalent, in the relevant compression, to an on-line lattice of double zeros. Thus a statistic built only from that compressed matrix cannot distinguish the two zero configurations.

WI-007 identifies the exact information threshold. For any auxiliary compactly supported window of support length `H<=L`, arbitrary real sample frequencies still give the same quadratic form for the screened off-line lattice and its on-line-double replacement. Horizontal depth appears only through nonzero Poisson aliases, and the first alias can occur only once the support crosses `H=L`. This is exactly the point at which the explicit formula begins to require arithmetic information beyond the support-one regime.

So the barrier has a clean meaning:

\[
\text{support }\le1
\quad\Longrightarrow\quad
\text{horizontal depth can be information-theoretically invisible after aggregation}.
\]

No refinement of a depth-only charge inequality inside the same information class can overcome an exact identification of the adversarial configurations.

## Evidence against overgeneralization

The screening lattice is an adversarial model, not a claim about the actual zeta zeros. Actual ordinates need not form that lattice. Therefore the result does not prove that support-one methods can never improve the numerical certified proportion; WI-009--WI-012 do improve the accounting of the simple critical-line contribution.

What it rules out is a stronger qualitative inference: support-one compressed data alone cannot force a positive lower charge for every off-line pair based only on horizontal depth. Breaking the screening requires vertical/arithmetic information not invariant under the replacement.

## Status / novelty

The Gabor/Poisson identities are classical and the Alpöge--Furman framework is prior art. The exact screening construction and its use as an obstruction are persisted evidence. The synthesis is a precise statement about where the missing information enters.

## Falsification criterion

Produce a support-`<=1` observable within the audited compression class that distinguishes the full critical screening lattice of off-line pairs from the corresponding on-line double lattice, contradicting the exact alias identity, or identify an additional arithmetic input already present at support one that invalidates the matched construction.

## Lean-formalizable core

- Two-rank spectrum of an isolated mirror pair.
- Poisson-summation identity that cancels the horizontal weight on the critical lattice.
- Support condition eliminating every nonzero alias for `H<=L`.
- Logical implication from equality of compressed operators to impossibility of a discriminator using only that operator.
