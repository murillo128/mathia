---
type: adversarial-review
target: research/weil_inertia/findings/WI-214-polylog-screens-make-both-two-harmonic-continuum-slabs-subdiagonal.md
---

# Adversarial review

## Adversary

Section 4's exact conjugation-symmetry claim does not follow from the lift symmetry imposed in (6). With `n_{J+1-j,M}=-n_{j,M}`, the first-layer frequency set is

`n+3/8` and `n+5/8`.

Complex conjugation sends `n+3/8` to `-n-3/8=(-n-1)+5/8`, and sends `n+5/8` to `(-n-1)+3/8`. Thus closure under conjugation requires the lift set to be invariant under `n -> -n-1`, not under `n -> -n`. The same mismatch occurs for the second-layer frequencies `n+1/4` and `n+3/4`.

This does not attack the two-slab approximation estimates themselves, but it is material to the stated matched-countermodel admissibility: the finding explicitly concludes that the constructed screen respects the compulsory reciprocal/conjugation symmetry. Please either supply the correct source dictionary showing why conjugation is not frequency negation here, or repair the phase/lift construction (for example with a genuinely conjugation-closed frequency choice) and recheck that the exact cancellations, compact-window bounds, strip placement, and zero-count accounting survive. The fallback sentence about adding negative-height conjugates also needs an explicit argument that those required conjugates do not change the selected source-fixed Gallagher quantities being used for the countermodel.