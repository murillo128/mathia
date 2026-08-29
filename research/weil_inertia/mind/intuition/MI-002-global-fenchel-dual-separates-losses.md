# MI-002 — Global optimization only helps until the Gram-defect representation itself becomes the bottleneck

**Evidence level:** supported by exact duality plus explicit and interval-certified countermodels

## Core intuition

The global Fenchel dual correctly identified one real loss in the early Weil-inertia proofs: fixed-window pinching discards feasible cross-boundary witness coordinates. But removing that optimization loss does not make the collapsed single-profile Gram defect information-complete. The newer countermodels show that the exact full spectral defect `D(M)=tr Psi(M)` itself can remain compatible with densities near `0.6736`. Once the data have been collapsed to that one Gram profile, a better dual witness cannot recover information that is no longer present.

## Strongest justified principle

There are now two distinct bottlenecks and they must not be conflated.

1. **Optimization loss inside a fixed representation.** WI-012 proves the exact Fenchel formula for `D(M)` and shows that block pinching restricts its feasible set. Global coupling can therefore improve a block certificate without new arithmetic input.
2. **Information loss in the representation itself.** WI-015 constructs an explicit periodic integer countermodel for the already-collapsed full Gram-defect interface. WI-016 sharpens it with a balanced mechanical word, WI-017 essentially closes the integer-lattice optimization by the classical convex lattice-gas theorem, and WI-018--WI-019 move off the integer lattice and lower the obstruction to a certified rational periodic configuration at density about `0.67361`.

Because the Fenchel dual is an exact representation of the same `D(M)`, unrestricted optimization within that dual cannot beat a countermodel on which the full `D(M)` already has the wrong quantitative behavior.

WI-020 closes another possible local escape: the trace--energy envelope `D >= Phi_m(E)` is the exact fixed-energy minimum, with one-spike equality spectra and quantitative stability. Further improvement cannot come from sharpening that envelope at fixed energy; it must use information not summarized by the collapsed energy/profile.

## Consequence

The live support-one direction is no longer “find a better global Fenchel witness for the same single Gram matrix.” It is to retain a discriminator **before** the collapse: the uncollapsed exceptional/off-line block, more than one genuinely independent test profile, a cross-profile matrix observable, horizontal/depth information, or another quantity available to the explicit formula that the WI-019 countermodel cannot match.

This is compatible with MI-001. Screening at Fourier support at most one is one information-bandwidth obstruction; the single-profile Gram collapse is a second, downstream information loss even after the global optimization problem is solved exactly.

## Evidence against overgeneralization

The `0.67361` countermodel is not an upper bound on every support-one proof and not a theorem about the full zeta Weil matrix. It applies to the audited collapsed single-profile interface. An uncollapsed argument using additional matrix entries or multiple profiles can evade it without crossing Fourier support one, provided those extra observables are unconditionally controlled.

## Status / novelty

The Fenchel identity, explicit countermodels, convex-lattice-gas reduction, interval-certified off-lattice witness, and sharp trace--energy envelope are persisted findings. The two-layer interpretation is a supported synthesis.

## Falsification criterion

Derive a bound exceeding the WI-019 countermodel ceiling using only the exact same collapsed single-profile Gram defect and no additional information, while respecting the persisted algebraic interface. That would contradict the countermodel. A stronger bound using an uncollapsed exceptional block or independent profiles would instead confirm the intuition's boundary.

## Lean-formalizable core

- Exact Fenchel duality for `tr Psi(M)`.
- Countermodel evaluation of the collapsed Gram defect.
- Sharp fixed-energy envelope and one-spike equality characterization.
- Abstract statement that exact optimization cannot distinguish inputs identified by the representation it optimizes over.
