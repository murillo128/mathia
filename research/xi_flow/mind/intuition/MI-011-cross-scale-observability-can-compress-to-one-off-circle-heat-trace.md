# MI-011 — Exact heat-trace identification can be arbitrarily local while transition transport requires antipodal-scale visibility

**Evidence level:** exact state-identification and transition-conditioning boundaries through XF-148

## Core intuition

The periodic polynomial state is algebraically easy to identify compared with the de Bruijn--Newman transition parameter. One off-circle trace, two nearby real traces, or one arbitrarily short moving real scan can determine the state exactly. None of that controls the modulus of `Lambda_per`.

The current matched family gives a geometric version of the distinction. Complete future observation on any fixed proper centered real aperture remains exponentially transition-blind. Even sparse or disconnected nonlocal linear sensing with polynomially bounded count and weight cannot aggregate away the loss unless its spatial support actually enters a shrinking neighborhood of the antipode.

## Strongest justified principle

XF-143--XF-144 prove essentially zero geometric threshold for exact state identifiability. XF-145 shows superexponential transition blindness on root-spacing tubes over short heat windows. XF-146 extends the central packet obstruction through the full future history of that tube.

XF-147 derives the fixed-aperture law: every centered interval omitting a nonzero antipodal neighborhood has an exponentially bad transition modulus for all future heat time. The obstruction stops forcing superpolynomial conditioning only when the unobserved antipodal gap shrinks to `O(L sqrt(log N/N))`.

XF-148 shows that this is a support-reach phenomenon, not a connected-scan artifact. Arbitrary predetermined sparse/disconnected space-time supports and polynomially normalized finite-measure sensors inherit the same exponential ceiling according to their nearest antipodal reach. For the matched pair the threshold is sharp at the raw-trace level when the initial slice is sampled.

## Program consequence

Do not optimize injective state recovery or add more sensors away from the visibility layer. The next target-side theorem must show source-faithful access to the near-antipodal layer with controlled normalization, or the source side must prove that Xi excludes the maximal-contact matched packet or an equivalent transition-sharp family.

A proposed decoder should state its observation support, sensor norm/normalization, source restriction, and inverse modulus for `Lambda_per` itself.

## Counterevidence / boundary

Near-antipodal access is only the point where this adversary ceases to force superpolynomial instability; it is not a stable reconstruction theorem for `Lambda_per`. The results concern raw real heat traces and polynomially normalized finite-measure linear sensors. Derivative/distributional or data-adaptive observation models require separate analysis.

## Epistemic status

**Exact algebraic identifiability together with exact all-future geometric transition-conditioning barriers; a stable source-to-transition observable remains open.**

## Falsification criterion

Construct a polynomially conditioned `Lambda_per` decoder for the XF-148 matched pair whose predetermined polynomially normalized support stays farther than `omega(L sqrt(log N/N))` from the antipode, or invalidate the exact pointwise envelope. A positive continuation should instead cross the derived support/source boundary.
