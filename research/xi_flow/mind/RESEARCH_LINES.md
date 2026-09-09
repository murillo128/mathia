# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Bypass exponentially ill-conditioned full-state tomography and seek a transition-relevant source observable

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-006-periodic-vieta-coordinates-diagonalize-the-nonlinear-heat-flow`, `MI-007-ultra-infrared-vieta-modes-should-be-quotiented-by-destination-energy`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-009-guarded-energy-can-enforce-static-real-divisor-feasibility`, `MI-010-endpoint-renormalization-is-source-fixed-before-discretization`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`.

XF-114--XF-130 separate source admission from periodic target observability. The q-scale source cone can be coercive and exactly realizable while remaining collision-nonidentifying under large families of local histories. Conversely, the periodic divisor is exactly recoverable from the upper-half Vieta histories and even from one off-circle scalar heat trace. Algebraically, one root-spacing displacement off the circle mixes the reflected shells strongly enough for exact recovery.

XF-131--XF-133 show that this exact one-channel observability is not a stable source bridge by itself. XF-131 gives a transition-sharp delayed-trace family: the central Vieta shell carries an exact prescribed periodic Newman time, yet any observation delay beyond the microscopic heat clock `L^2/(pi^2 N^2)` suppresses the distinguishing trace exponentially. XF-132 finds a separate zero-delay obstruction: central heat-rate clustering creates coefficient directions with `O(1)` state size but an exponentially small complete future trace, even inside the simple unit-circle-rooted class. XF-133 shows that adding finitely many probes, a growing probe family, or even continuum observation on a fixed macroscopic local complex patch does not remove this worst-case tomography instability.

The live theorem is therefore no longer “derive enough observations to reconstruct the periodic divisor.” Full-state reconstruction can be exponentially ill-conditioned even when algebraically exact. The useful target is a **source-justified observable or inequality adapted directly to transition geometry**, or a source theorem proving that the actual Xi state avoids the central hidden directions. Any proposed source-to-trace bridge must quantify temporal delay, central heat-spectrum conditioning, spatial aperture, and source error in the norm actually needed to control `Lambda`.

## Decide the q-scale versus prime-band fork explicitly

The q-scale source problem is stronger than solved positivity: exact realizability and uniform history matching coexist with arbitrary matched transition times, while the target has exact but unstable cross-scale tomography. A q-scale continuation should therefore connect the **actual source** to a transition-relevant stable quotient, not merely to a formally identifying full-state observable.

Moving to `xi=Theta(1)` beginning at `lambda_2` remains a separate route. It must handle distributional prime-power atoms and replace the perturbative point-sampling/shadow interface. Q-scale Toeplitz coercivity, exact realization, periodic observability, and the central conditioning obstructions must not be transferred to the prime band without a new source-to-destination theorem.

## Keep source coercivity, realization, identifiability, conditioning, source access, and transition coercivity separate

A positive source cone can be exactly realizable and still contain fibers with radically different collision geometry. A target observable can identify the complete divisor exactly and still possess exponentially small singular directions. Conversely, full-state instability does not prove that the transition time itself is equally unstable: a direct transition functional may quotient the hidden directions.

Future results should state whether they change source admission, node realization, periodic algebraic identifiability, temporal/spatial conditioning, source accessibility, a transition-specific quotient, prime-band access, or the actual inequality controlling `Lambda`. These are distinct theorem surfaces.
