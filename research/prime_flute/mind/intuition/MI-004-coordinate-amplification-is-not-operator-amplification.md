# MI-004 — The clone comparison has reached a functional-calculus and global-assembly boundary

**Evidence level:** supported; compact relative resolvent, natural-identification equivalence, local geometric/operator budgets, and critical-symbol no-go are exact, while both global wave-comparison closures remain open

## Core intuition

The exact prime flute and the all-composite shift clone `q_n=p_n+1` are increasingly hard to distinguish in natural asymptotic operator categories. The remaining problem is no longer whether a large Fenchel--Nielsen coordinate or an `L^2` gauge choice can amplify the small tail defect. It is whether one can assemble the already-controlled local geometry into a global scattering/Schatten theorem, and—if so—whether the **value** of the resulting relative spectral object carries arithmetic information rather than merely existing by general operator theory.

## Strongest justified principle

PF-121--PF-125 give the baseline: a canonical marked asymptotically bilipschitz identification and compact first relative resolvent, hence equality of essential spectra. PF-112 fixes a hard local endpoint: the first relative resolvent of a genuinely nonisometric smooth two-dimensional metric pair is not trace class.

PF-126--PF-145 remove the main local geometric escape hatches. Body, cusp, split-ray, short-core, and handoff budgets are summable; all tail Margulis-short closed cores are classified; deep cusps can be matched exactly; and reflection removes the constant collar phase. The remaining geometric cost is the actual centered angular/radial interface trace, with a sharp unsuppressed `L^1` extension cost.

PF-146 gives a different operator route. On fixed matched short collars the **squared** relative resolvent is trace class with a summable local budget. PF-147 shows exactly what a global version would imply: the first relative resolvent would lie in `S_2\setminus S_1`, giving a canonical direct `det_2`/Koplienko regime. PF-150 proves the exponent is abstractly sharp: squared-resolvent `S_1` alone cannot force `S_r` for any `r<2`. Any sub-`S_2` improvement is therefore genuinely geometric, not a functional-calculus corollary.

PF-148 corrects an important possible overinterpretation of that boundary. If the global squared-resolvent difference is trace class, the squared bounded transforms themselves form a trace-class pair. Krein spectral shift and an ordinary perturbation determinant therefore exist at that transform level, and the invariance principle transports an ordinary Birman--Krein scattering phase back to the original Laplacians. Thus `S_2` for the first resolvent does **not** mean that first-order scattering phase is unavailable; it means that the phase comes through the stronger squared transform.

PF-149 closes a gauge loophole around this scattering problem. For the PF-125 marking, the trivial and density-corrected unitary `L^2` identifications are asymptotically equivalent and give the same wave operators whenever either exists. Future failure or success cannot be attributed to that natural volume-identification choice.

PF-151 closes the most canonical singular-trace rescue at the opposite endpoint. The order-`-2` Wodzicki residue density of an unweighted first resolvent is area density; every exact hyperbolic pant has area `2 pi`, so the whole-pant critical residue is topological and blind to cuff/gap fluctuations. A global noncompact Dixmier trace is not asserted, but the canonical local weak-`S_1` principal scalar is not a prime selector.

## What remains possible

Two global closures remain mathematically meaningful. The geometric route must sum the actual reflection-compatible interface traces in the weighted metric criterion. The operator route must globalize the PF-146 squared-resolvent `S_1` estimate through bodies, collars, cusps, interfaces, and localization commutators.

If either route proves complete wave operators, the next question is no longer whether a scattering phase exists: under the squared-transform route PF-148 already identifies a canonical one. The arithmetic question is whether the resulting spectral-shift/scattering function, resonance continuation, or stronger relative invariant distinguishes the exact prime flute from the exact composite clone in a way not forced by general trace-ideal/scattering theory.

## Status / novelty

The compact-resolvent comparison, local geometry, Schatten implications, invariance-principle phase, identification equivalence, and residue calculation are persisted findings with classical operator/hyperbolic ingredients. The synthesis is a narrowed boundary, not a proof of global wave operators, resonance equality, determinant continuation, or RH.

## Falsification criterion

A decisive advance should prove or refute one global assembly. An alleged shortcut is falsified if it relies only on first-resolvent trace class, changes between the two natural volume identifications, tries to cross below `S_2` from squared-resolvent `S_1` by abstract functional calculus alone, or uses the unweighted critical Wodzicki/Dixmier residue as a gap-sensitive scalar.

## Lean-formalizable core

- Sharp local collar extension and squared-resolvent ideal estimates.
- Powers--Størmer implication `S_1` of squares to `S_2` of roots.
- Diagonal sharpness counterexample below `S_2`.
- Kato asymptotic equivalence of the two volume identifications.
- Critical resolvent residue equals hyperbolic area density.
