# MI-006 — Asymptotically fixed Mellin drift is information-neutral

**Evidence level:** proved for the convergent-frequency twists covered by MC-038

## Core intuition

Allowing a scale-dependent oscillatory phase does not automatically create a new cancellation mechanism. If the Mellin frequency converges to a finite limit, the drift can be absorbed into the same coarse Möbius/Mertens information by Abel summation. The apparent extra degree of freedom is asymptotically only a change of character.

## Strongest justified principle

MC-038 proves that endpoint-dependent Möbius Mellin twists with `tau_N -> tau_*` satisfy the critical square-root bound exactly when the ordinary RH-equivalent Mertens bound does. The same self-absorption holds for the annular Mellin formulation and for natural finite-log Fourier modes whose physical frequency converges.

Thus a bounded or convergent phase schedule does not evade the coarse-mode obstruction identified by the annular decomposition. A genuinely distinct signed mechanism must use information that cannot be frozen to one limiting character: coupled cancellation among modes, nonconvergent/high-frequency schedules with uniform control, or another source-forced operation that changes the information content rather than merely its phase coordinates.

## Evidence synthesis and boundaries

The statement is not that all oscillatory Möbius estimates are equivalent to RH or that high-frequency twists are useless. It is specifically a no-go for asymptotically fixed Mellin characters under the exact MC-038 hypotheses. Nonconvergent frequencies may interact with moving cutoffs and annular faces in a genuinely different way, but that would require uniform estimates strong enough to survive the moving character.

This complements MI-005: iterable scale contraction could still amplify a true signed residual, but slowly drifting coordinates cannot themselves supply that residual.

## Status / novelty

Abel summation and Mellin-character manipulations are classical. The persisted contribution is the source-specific information audit: asymptotically fixed phase drift is a coordinate change, not an additional arithmetic channel.

## Falsification criterion

Construct a convergent-frequency family within the MC-038 class whose critical estimate is strictly weaker than, or not equivalent to, the ordinary Mertens/RH bound; or show that the Abel self-absorption loses a source term that survives at the critical exponent.

## Lean-formalizable core

- Abel-summation comparison between a convergent Mellin twist and its limiting character.
- Equivalence of the critical bound under the stated convergence hypotheses.
