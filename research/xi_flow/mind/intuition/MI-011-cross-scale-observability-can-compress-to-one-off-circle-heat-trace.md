# MI-011 — Cross-scale collision observability can be algebraically tiny yet exponentially ill-conditioned

**Evidence level:** exact periodic one-channel reconstruction plus delayed, zero-delay, and local-patch conditioning obstructions through XF-133

## Core intuition

The periodic collision-identifiability barrier is not fundamentally a need for many scalar channels. A single off-circle heat trace can mix reflected Vieta shells and determine the full divisor exactly. But **exact compression is not stable compression**: the heat spectrum contains central directions whose contribution to that trace is exponentially small in the degree even when observation begins at the target slice and spans a macroscopic local complex patch.

The remaining Xi problem is therefore not to obtain formal access to a target-complete observable. It is to find a source-accessible quotient whose conditioning is matched to transition geometry, or prove that the actual Xi source excludes the hidden central directions responsible for the worst-case tomography instability.

## Strongest justified principle

XF-124--XF-129 establish the algebraic observability threshold. Sublinear histories and large terminal windows can be collision-blind, while the complete upper half of Vieta histories determines the periodic divisor. XF-130 compresses that identifying family into one scalar heat trace `Q_zeta(s)=E(zeta,s)` at any fixed `|zeta|!=1`; a one-root-spacing radial displacement gives only polynomial conditioning in the reflected-shell spatial inversion.

XF-131 identifies a separate temporal clock. The central Vieta shell supports an exact one-parameter family with prescribed periodic Newman transition time, but observation starting at delay `s_0` suppresses the distinguishing trace by `exp(-delta_M s_0)`, where `delta_M=pi^2N^2/L^2`. Stable transition discrimination therefore requires time resolution on the microscopic scale `L^2/N^2` for this family.

XF-132 shows that removing the delay does not make full-state tomography stable. Because the central heat rates are quadratically clustered, barycentric divided-difference packets can annihilate many temporal jets and keep the **entire future trace** exponentially small relative to an `O(1)` reflected-shell coefficient perturbation. These directions can be realized by arbitrarily small perturbations that remain simple and unit-circle rooted.

XF-133 makes the obstruction spatially robust. The same kind of central packet can be chosen before the probe and remains exponentially hidden uniformly for all future heat times over a fixed macroscopic local complex patch. Thus increasing local probe count or replacing one trace by continuum local observation does not cure the worst-case Vieta-state inversion.

## Counterevidence / boundary

XF-132--XF-133 concern stable recovery of the full reflected-shell/Vieta state. They do not prove that the periodic Newman transition time itself has the same zero-delay exponential condition number. XF-131 is transition-sharp only for delayed observation. A direct transition functional may discard central state directions that are expensive for tomography.

The patch obstruction also does not cover arbitrarily large spatial apertures, observation norms with exponentially weighted high derivatives, or a source theorem restricting admissible Xi coefficient directions. Those are possible escapes if independently justified and quantitatively controlled.

## Epistemic status

**Exact periodic one-channel identifiability together with exact exponential temporal/spatial conditioning barriers for full-state tomography; a stable source-to-transition observable remains open.**

## Falsification criterion

Produce a uniformly stable inverse from the XF-130 local trace family to the full Vieta state contradicting XF-132--XF-133, or refute the XF-131 transition-sharp delayed family. A source-positive continuation should instead derive a transition-adapted observable with a quantitative modulus, or prove an Xi-specific structural law excluding the central hidden packets before transporting source error to `Lambda`.
