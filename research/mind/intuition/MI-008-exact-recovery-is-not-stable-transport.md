# MI-008 — Exact recovery and local conditioning do not determine stable target transport

**Evidence level:** supported cross-line synthesis

## Core intuition

A representation can identify the hidden state exactly, admit a condition-one local inverse, or expose the source signal at tiny scale while still failing to transport the final target. Conversely, a severe acquisition loss can disappear when the observation category is enlarged. The invariant cost is the **whole source-to-target composition**, including acquisition and the target projection actually consumed.

## Strongest justified principle

Arithmetic Fidelity separates exact category, finite-complexity recovery, and stability. AF-269 extends exact recurrence exclusion to finite-total transports; AF-270 gives an infinite periodic off-critical control inside the same recurrence/frequency category; AF-271 shows finite coefficient recovery depends on divisor complexity and stable recovery on separation.

Xi Flow gives both sides of the conditioning lesson. XF-181 makes the packet inverse locally isometric in adapted coordinates. XF-182 shows raw positive heat still sees higher packet modes with graded power loss. XF-183 removes that loss relatively only by dividing by exponentially small mass. XF-184 then uses mesoscopic complex Jacobi phase to obtain a uniformly conditioned **absolute** acquisition bank. The expensive stage can move or disappear when the acquisition category changes.

Visual Exploration provides a stable decoder calibration. Exact finite phases identify height, but an omitted prime already has no continuous fixed-support decoder and has quantitatively growing collision complexity. Stable recovery must be assessed against matched controls, not inferred from set-theoretic identity.

Nyman--Beurling identifies the target oracle even more sharply. NB-050 expresses recursive repair slack as a finite continuous-grid enrichment gap; NB-051 shows its first-order two-scale limit can be the global natural-versus-continuous Nyman projection gap `Delta_*`, so mesh refinement does not automatically make the target repair cheap. Prime Flute similarly reduces compactness to relative angle between heavy extension ranges, with a local cross-form falsifier.

## Program consequence

For every recovery result, separate exact identifiability, coordinate conditioning, observable acquisition, target projection/sign, and the matched control class. A good inverse is useful only when the required coordinates are obtainable in a source-faithful topology; a refined mesh is useful only if the target gap is proved to shrink; and a hard decoder is interesting only when the same hardness is absent from an appropriate null model.

## Counterevidence / boundary

Stable transport is not universally impossible. XF-184 is a positive example where a broader holomorphic observation removes a remote packet barrier. NB-051 is a negative warning that an apparently local discretization gap can converge to a global target component. The principle is a bookkeeping requirement: locate the cost in the full composition rather than attributing it prematurely to one stage.

## Epistemic status

**Supported separation of identifiability, conditioning, acquisition, and target transport, strengthened by a positive acquisition-category escape and a closure-level target-gap normal form.**

## Falsification criterion

In one cited setting, derive the final target theorem from exact identification/local conditioning alone while bypassing the identified acquisition or target modulus under the same hypotheses, or invalidate a load-bearing separation such as AF-270/271, XF-184, VIS-163--165, NB-050/051, or PF-287.