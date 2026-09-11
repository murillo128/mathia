# MI-016 — Finite-radius Weil positivity requires cancellation-preserving source discrepancy, not a small PNT remainder

**Evidence level:** supported

## Core intuition

Localized Weil theory moves a hypothetical RH failure to a finite source window, but the useful source term is not total prime mass or an absolutely small Prime Number Theorem remainder. The completed non-prime background is already indefinite, and the density-one part of the von Mangoldt measure cancels only a specific pole contribution. The missing positive branch requires an order-one **signed discrepancy charge** supplied by the actual arithmetic fluctuations.

The latest result shows that taking absolute values destroys exactly the needed scale. The source theorem must preserve cancellation.

## Strongest justified claim

WI-236--WI-237 show that Bombieri finite truncations detect off-line packets but may lose coercivity through coefficient cost and height escape. WI-238 therefore supplies an independent finite-radius source-side route via Suzuki's localized completed Weil form.

WI-239--WI-240 eliminate generic crossing explanations. The universal logarithmic core crosses zero on its own, and the full gamma-plus-pole form with the von Mangoldt contribution deleted develops unbounded odd negative index. Positivity, if true, must be produced by the arithmetic source rather than by abstract spectral geometry.

WI-241 replaces the von Mangoldt measure by its density-one continuum term and finds an exact cancellation of the pole into a bounded positive resolvent, but the remaining gamma-plus-resolvent background is still indefinite on slow odd modes. The full source burden becomes the signed discrepancy `Lambda-1` against those modes.

WI-242 derives the exact slow-dilate partial-summation formula. The relevant integral weights `E(x)=psi(x)-x` by `x^(-3/2)` with a smooth scale kernel. Substituting a pointwise envelope for `|E|` gives the wrong order: standard unconditional PNT errors produce an exponentially growing bound, while the usual RH estimate `O(sqrt(x) log^2 x)` still yields polynomial growth in the aperture. The kind of absolute square-root-plus-log saving that would make the envelope uniformly bounded is incompatible with Littlewood oscillation.

Under RH, by contrast, the signed discrepancy converges to the exact finite constant required by the background. The order-one source charge is therefore a cancellation-sensitive RH-scale phenomenon.

## Synthesis of evidence

The finite-radius route has become a signed-correlation problem. A successful theorem should keep `d(psi-x)` inside the localized autocorrelation/Mellin pairing and exploit a relation that is destroyed by absolute values. Candidate mechanisms include an explicit-formula identity, a source-specific sign/covariance law, or a finite-prime invariant that controls the dangerous slow-mode family collectively.

This is stricter than “use a better PNT bound.” Even an RH-quality pointwise estimate is too weak after triangle inequality. The proof architecture itself must preserve the oscillation.

## Counterevidence / boundary cases

WI-242 does not show that no pointwise information can ever be useful when combined with sign or spectral localization; it only rules out ordinary absolute-envelope arguments. The slow-dilate family is a diagnostic family, not a proof that every dangerous mode has identical structure.

The RH limit for the discrepancy is conditional and does not provide an unconditional sign theorem. Suzuki's neighboring RH-equivalent weighted-prime criterion is prior-art guidance, not evidence that the present autocorrelation condition is equivalent to RH.

## Epistemic status

**Supported source-side narrowing:** mean density, generic completion, and absolute PNT-error magnitude cannot supply the required localized sign. The surviving currency is cancellation-preserving signed von-Mangoldt discrepancy against the dangerous mode geometry.

## Novelty/prior-art status

Suzuki localization, PNT error bounds, Littlewood oscillation, and partial summation retain their finding-level prior-art status. This intuition states their consequence for the current finite-radius program.

## Falsification criterion

Derive the required uniform order-one slow-mode compensation from a standard absolute envelope for `psi(x)-x` without using additional cancellation, or invalidate the exact WI-242 integration-by-parts scale. Strategically, prove a cancellation-preserving source identity that controls the signed discrepancy on the full dangerous family; that would cross the current gate.
