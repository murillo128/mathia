# MI-004 — Complete scalar five-point control is sharp radial coercivity

**Evidence level:** exact and validated through ANF-064

## Core intuition

For the Montgomery--Taylor profile, the cardinality-five scalar problem is completely closed. Horizontal phase, relative height, and common translation first compactify the geometry; validated computation then proves the exact defect positive; the completed moment hierarchy further identifies a sharp quadratic coercive floor and strict radial monotonicity.

## Strongest justified principle

ANF-062 proves strict positivity of the exact five-point defect on the entire genuine domain. ANF-063 proves the sufficient moment inequality for every `n>=9`; ANF-064 validates the remaining `n=2,...,8`, so every higher even-power coefficient in the height expansion is positive. Consequently

`H_MT >= 2 pi^2 m_5(J_MT) (y_1^2+y_2^2)`

with the constant sharp as an infimum, and the normalized defect is strictly increasing under simultaneous positive height dilation. ANF-064 also gives a certified positive quartic remainder from the order-two margin.

## What remains possible

The theorem does not settle larger conjugation-invariant multisets or a profile-independent positivity theory. The live use of this scalar result is as a sharp source-conditioned base case for richer ordered/multi-point carriers or for identifying which hypotheses make an all-order moment argument transfer.

## Status / novelty

The analytic and interval tools are classical. The durable synthesis is Mathia-specific: **Montgomery--Taylor five-point scalar positivity is not merely zero-free but sharply coercive, so reopening its scalar enclosure is no longer a live research mechanism**.

## Falsification criterion

Find a genuine five-point configuration violating ANF-064's sharp floor or radial monotonicity, or invalidate the validated finite-moment certificate or ANF-063 analytic tail.

## Lean-formalizable core

- The coefficient decomposition from the all-order moment inequalities.
- The sharp quadratic lower bound and radial monotonicity implication.
- The finite validated inequalities for `n=2,...,8` as certificate interfaces.