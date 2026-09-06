# MI-004 — Complete scalar five-point control includes sharp near-extremizer classification

**Evidence level:** exact and validated through ANF-066

## Core intuition

For the Montgomery--Taylor profile, the cardinality-five scalar problem is now closed not only at positivity/coercivity level but also at the boundary of sharpness. The exact height expansion, additive linkage among horizontal arguments, and validated curvature geometry together force every near-extremizer into two explicitly classified boundary families.

## Strongest justified principle

ANF-062 proves strict positivity of the exact five-point defect. ANF-063--ANF-064 prove the all-order moment inequalities, the sharp quadratic coercive floor, strict radial monotonicity under simultaneous height dilation, and a certified positive quartic remainder.

ANF-065 restores the relation `d=t_h-t_l` that independent moment bounds discard and proves a joint excess lower bound controlling both total height scale and the smaller-pair weight. ANF-066 validates the remaining one-dimensional curvature geometry: the transform has exactly two nondegenerate global minimizers `±tau`, and for sufficiently small normalized excess `E`,

`E asymp S + r + D^2`.

Consequently `S=O(E)`, the smaller pair satisfies `y_l/y_h=O(sqrt(E))`, the horizontal coordinates approach the two-minimizer set at `O(sqrt(E))`, and the only limiting horizontal families are the two classified branches, both attainable. Scalar five-point near-extremizers no longer contain an unclassified escape.

## What remains possible

The theorem does not settle larger conjugation-invariant multisets, multiple source profiles, or ordered/non-scalar carriers. The completed five-point result should be used as a transfer theorem: isolate which hypotheses make all-order positivity, additive incompatibility, and curvature convexity survive when the source category genuinely changes.

## Status / novelty

The analytic, convexity, and validated-interval tools are classical. The durable synthesis is Mathia-specific: **Montgomery--Taylor five-point scalar positivity is sharply coercive and its near-extremizing boundary is quantitatively classified, so reopening that scalar category is no longer a live mechanism**.

## Falsification criterion

Find a genuine five-point configuration violating the ANF-064 floor or ANF-066 two-sided stability, invalidate the finite validated moment/curvature certificates, or produce a near-extremizing sequence outside the two classified horizontal boundary families.

## Lean-formalizable core

- The coefficient decomposition from the all-order moment inequalities.
- The additive-annulus incompatibility lower bound.
- The implication from a certified two-minimizer curvature profile to two-sided near-extremizer stability.
