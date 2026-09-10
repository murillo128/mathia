# MI-022 — Prefix truncation must respect cancellation orbits before any damping is trusted

**Evidence level:** exact root-rate and damping analysis through AF-243

## Core intuition

A coarse RH-equivalent output exponent can tolerate substantial final error while remaining intolerant of source truncations that cut through an exact cancellation orbit. Smoothing the resulting output does not restore the information destroyed before the transform was completed.

## Strongest justified principle

AF-234--AF-238 show that sublinear and even fixed linear prefixes of natural zeta/xi jets can create unconditional exponential root rates above one by interrupting contributions that should cancel. Completing away one known family of poles merely transfers the false signal to the nearest surviving critical-line zero pair.

AF-239 shows that fixed binomial damping avoids this only by changing the discriminator to a strictly stronger strip statement. AF-240--AF-242 prove that carefully moving damping can preserve the RH root rate and suppress fixed critical orbits. AF-243 then supplies the decisive control: if the underlying source access remains a nonvanishing linear prefix, that damping still preserves the false prefix artifact. The defect is therefore upstream of the damping layer.

## Program consequence

Demand cancellation-coherent source access first: completed blocks, whole orbits, contours, or another source-faithful representation in which the cancellations required by the root-rate quotient occur before truncation. Only then optimize damping or sparse output sampling.

## Counterevidence / boundary

These findings rule out broad prefix architectures, not every compressed representation. A non-prefix transform may preserve the necessary orbit information at lower cost. Moving damping is also mathematically useful once the source representation is faithful; the negative claim is only that it cannot repair an already broken prefix.

## Epistemic status

**Exact structural separation between source-side cancellation coherence and output-side damping; no cheap faithful source representation is yet proved.**

## Falsification criterion

Construct a genuinely shallow source representation that provably yields the correct RH root-rate class without reconstructing the missing cancellation orbit, or show that AF-243's prefix artifact disappears under an admissible damping regime covered by its hypotheses.