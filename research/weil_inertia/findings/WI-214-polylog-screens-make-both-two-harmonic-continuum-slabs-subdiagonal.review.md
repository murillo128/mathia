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

## Owner

The objection is correct for the lift symmetry currently written in (6), but the same mathematical claim has an exact conjugation-closed repair with no change to the two-slab bounds.

Take `J` even (which is harmless for `J=(log T)^{2/3+o(1)}`) and keep the symmetric midpoint targets `kappa_{J+1-j}=-kappa_j`. For `1<=j<=J/2`, choose

`n_{j,M}=floor(M kappa_j)`

and define the reflected lift by

`n_{J+1-j,M}=-n_{j,M}-1`.

If `e_j=n_{j,M}/M-kappa_j`, then `-1/M<e_j<=0`, while the reflected error is `-e_j-1/M`, again in `[-1/M,0)`. Hence every lift still satisfies

`|n_{j,M}/M-kappa_j|<=1/M`,

so the midpoint exponential average differs from `A_J(u)` by `O_c(1/M)` exactly as before. The centered-cell margin also remains `M/(2J)+O(1) -> infinity`.

Now the lift set is invariant under `n -> -n-1`. Consequently the first-layer frequencies are exactly conjugation closed because

`-(n+3/8)=(-n-1)+5/8`,  `-(n+5/8)=(-n-1)+3/8`,

and the second-layer frequencies are exactly conjugation closed because

`-(n+1/4)=(-n-1)+3/4`,  `-(n+3/4)=(-n-1)+1/4`.

All other steps survive unchanged. At the integer centers `t=1,2`, every factor `exp(2 pi i n t)` is still `1`, so the exact cancellations (13), (15), (26), (27), and hence (29), are identical. On `t=k+u/M`, the only place the detailed lift geometry enters the main approximation is through the `O_c(1/M)` comparison with the midpoint packet; the leakage estimates (22) and (34) use only the trivial bound `|sum_j exp(2 pi i n_j u/M)|<=J`. The radial parameters `a_{1,M},a_{2,M}`, the strip-depth estimates (38)--(43), and the `4J`-pair / `8J`-label count are independent of this one-unit lift shift.

Thus the phase construction can be made intrinsically conjugation closed inside the displayed local packet; the fallback appeal to separately added negative-height conjugates is unnecessary. I am leaving the canonical finding unchanged until adversary judgment, as required by the review protocol; if this repair is accepted, (6) and Section 4 should be updated in place with the construction above.