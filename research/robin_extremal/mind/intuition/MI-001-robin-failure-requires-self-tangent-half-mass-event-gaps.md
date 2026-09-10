# MI-001 — Robin failure is a selector problem after finite dominant-face cone compatibility

**Evidence level:** exact CA localization, same-parameter prime-race cone, dominant-zero phase analysis, finite dominant-face recurrence, and additive-resolution budget through RE-032

## Core intuition

The Robin route can no longer hope that the standard and reciprocal zero coefficients make the threshold race cone intrinsically impossible. A single off-critical pair realizes the required signs near a suitable Chebyshev zero crossing, and the same phenomenon survives every nonzero finite packet of dominant modes on one off-critical vertical line.

The exceptional object is therefore the **CA threshold selector**, not finite spectral coefficient geometry. It must repeatedly sample cone-compatible recurrent phase windows, and using the discreteness of CA events against those windows requires quantitative phase/additive resolution that the current asymptotics do not supply automatically.

## Strongest justified principle

RE-017--RE-029 localize hypothetical failure to self-tangent CA thresholds, couple event depth to the same frontier displacement, and force the standard Chebyshev and logarithmic Mertens-product errors into an opposite-sign quantitative cone at one common parameter `Z`.

RE-030 tests the one-mode coefficient geometry and finds no contradiction: an off-critical pair realizes the cone near a reciprocal-positive standard-mode downcrossing. RE-031 converts that one-mode phase law to physical scale and shows that an event-spacing contradiction at additive scale `h(Z)` requires a relative source/spectral error `epsilon(Z)=o(h(Z)/(Z^(1-delta) log Z))`; square-root event resolution therefore needs a genuine power saving rather than any fixed logarithmic refinement.

RE-032 then removes the possibility that finite multi-frequency interference restores an automatic sign obstruction. For every nonzero finite packet with common real part `beta>1/2`, the reciprocal packet is an exact stable-filter transform of the standard packet. Zero-mean recurrence forces a downcrossing with positive reciprocal value, and finite-frequency recurrence reproduces such neighborhoods infinitely often. For any threshold exponent in the admitted range, points exist where the standard packet has exactly the required small negative magnitude while the reciprocal packet remains uniformly positive before multiplication by the common power.

## Program consequence

Target the selector-to-spectrum relation. Prove that the CA threshold sequence avoids the recurrent cone-compatible phase neighborhoods of the actual dominant spectral face, or obtain a power-saving approximation precise enough to combine the phase condition with CA event spacing. If the relevant zero contribution is not controlled by one finite vertical face, identify the genuinely infinite/multi-face structure and show how it changes the recurrence or sign geometry.

Do not spend effort seeking a contradiction from the signs of finitely many dominant zero coefficients alone; RE-032 classifies that route as compatible.

## Counterevidence / boundary

RE-032 concerns finite packets whose zeros share one real part and shows existence of cone-compatible phases, not that the CA selector visits them. It does not classify infinitely many comparable modes, several dominant real parts, truncation remainders, or the true arithmetic dependence between CA thresholds and spectral phases.

RE-031's explicit additive-resolution formula is derived in the one-dominant-zero setting. Its qualitative lesson about needing selector precision remains relevant, but a general finite-packet spacing theorem would require its own quantitative transversality/remainder analysis.

## Epistemic status

**Exact finite-face negative boundary: the threshold cone is compatible with every nonzero finite packet on a dominant off-critical vertical line, while one-mode event-spacing exclusion requires power-saving resolution; the remaining obstruction must come from the CA selector, a stronger source relation, or genuinely non-finite spectral structure.**

## Falsification criterion

Exhibit a nonzero finite same-real-part packet for which no arbitrarily large phase realizes the RE-032 threshold cone, or prove that finite dominant-mode coefficient geometry alone excludes the CA-selected cone without using selector information, remainder control, or additional source structure.
