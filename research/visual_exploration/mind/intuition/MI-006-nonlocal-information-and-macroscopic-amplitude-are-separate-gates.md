# MI-006 — A support-safe edge companion is a renormalized moment-cancellation problem

**Evidence level:** exact finite-CUE covariance/support reductions plus linear, quadratic, and moment-null companion controls through VIS-144

## Core intuition

The restricted-support escape from edge-edge covariance is not merely a frequency-placement problem. Once one factor approaches the Montgomery edge, the companion is forced into a shrinking low-frequency channel whose deterministic finite-CUE response also shrinks. The source must therefore pay a normalization bill at the same time that the available theorem support narrows.

Finite source windows reveal a useful extra degree of freedom: in the ultra-low-frequency regime the universal CUE-centered response is quadratic, and a signed packet can cancel that second-moment term exactly. The remaining question is whether arithmetic information occupies a different low-frequency functional and survives that cancellation at controlled variance and transfer cost.

## Strongest justified principle

VIS-130--VIS-141 fix the finite-CUE null, identify the four-level cross-window requirement, and prove that classical Rudnick--Sarnak support cannot contain two edge factors. Retaining one edge factor forces an independent companion bandwidth `b` toward zero.

VIS-142 shows that bounded-total-variation packets then have CUE-centered mean `O(b)` uniformly, so scalar rescue costs at least inverse bandwidth. VIS-143 keeps the finite source window and sharpens the ultra-low-frequency regime to `O(Mb^2)` when `Mb` is small. VIS-144 proves this quadratic scale is genuine under the natural bounded-aspect-ratio assumptions and identifies its coefficient with the finite kernel second moment. For signed packets, imposing `int q^2 dnu(q)=0` cancels the complete universal quadratic mean term while leaving Fourier support unchanged; only a quartic-order null remainder is forced by the current expansion.

## Program consequence

Compute the corresponding low-frequency zeta/arithmetic expansion before designing more statistics. The decisive test is whether the arithmetic correction has a nonzero component not proportional to the same second-moment functional. If so, choose a moment-null signed packet and prove that its surviving arithmetic scale dominates the amplified CUE remainder, variance, finite-height transfer, and moving-family theorem error. If not, close this restricted-support redesign and return to direct covariance or wider-support four-level information.

## Counterevidence / boundary

Moment cancellation is only a deterministic null-mean fact. Signed weights can have large total variation and worsen stochastic noise; the zeta correction may share the same quadratic coefficient and be canceled with the null; and no required moving-window uniformity theorem has been proved. The original edge-edge route is unaffected by these low-frequency controls.

## Epistemic status

**Exact restricted-support redesign boundary: shrinking companions have a finite-window quadratic CUE response whose leading moment can be canceled algebraically, but arithmetic selectivity and the full normalized error budget remain unproved.**

## Falsification criterion

Show that the relevant zeta lower-order term is proportional to the same quadratic frequency moment through the required accuracy, or construct a moment-null packet for which the claimed universal CUE cancellation fails under the frozen finite-window definitions.
