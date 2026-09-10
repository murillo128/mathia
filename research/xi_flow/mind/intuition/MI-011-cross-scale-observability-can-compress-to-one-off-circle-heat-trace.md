# MI-011 — Transition visibility has a sharp one-sided complex reach threshold in the maximal-contact control

**Evidence level:** exact state-identification barriers, full-jet bounds, and initial/all-future complex visibility threshold through XF-153

## Core intuition

Exact state identification is much easier than stable recovery of the de Bruijn--Newman transition parameter. For the current maximal-contact matched family, this is no longer only an upper-bound heuristic about shallow collars: the required complex reach has an exact direction-sensitive exponential threshold, and positive heat evolution does not lower it.

The target-side escape is therefore geometrically explicit. Either a source-faithful Xi observable reaches the necessary outward antipodal region at controlled cost, or the source must forbid the matched transition-sharp packet.

## Strongest justified principle

XF-143--XF-151 show that polynomially normalized real sensors, finite/infinite derivative jets and shallow complex collars can identify the state while remaining exponentially blind to `Lambda_per`. Near the antipode the previous certificate predicted a parabolic depth scale `d^2/L`.

XF-152 computes the initial complex trace exactly and gives a unique outward threshold `H_*(D)`, while inward continuation never achieves order-one exponential-rate separation at finite depth. Near the antipode this is `h_*(d)=(pi/2)d^2/L+O(d^4/L^3)`.

XF-153 proves that in the near-antipodal sector optimizing over all future heat times changes the matched signal by at most a factor two from the initial slice. The all-future exponential rate and threshold are therefore exactly the initial ones; positive heat cannot rescue observations below the parabolic boundary.

## Program consequence

Stop enlarging the same real/shallow observation class or optimizing future time. Derive a Xi-specific route to outward complex/antipodal access at or beyond the quantified threshold with a stable inverse modulus, or prove that the maximal-contact family cannot arise from the actual Xi source constraints.

## Counterevidence / boundary

Crossing the threshold is necessary only against this matched control and is not sufficient for stable recovery. The result does not establish that Xi realizes the packet, nor that all nonlinear/data-adaptive observations obey the same bound. Source restrictions remain a legitimate escape if independently derived.

## Epistemic status

**Exact one-sided all-future visibility boundary for the current transition-sharp control; source realizability and a stable Xi decoder remain open.**

## Falsification criterion

Construct a polynomially conditioned decoder for the matched family using observations strictly below the stated outward reach, or invalidate XF-153's all-future factor bound. A positive continuation should cross the threshold source-faithfully or exclude the matched packet.
