# MI-005 — Category, assembly topology, operator ideal, spectral type, relative scale, and transport direction are part of the arithmetic claim

**Evidence level:** supported by exact category-sensitive findings across the active Mathia lines

## Core intuition

A source signal can be present yet unusable because it lives in the wrong range, requires unbounded conditioning, sits in an operator ideal with the wrong spectral density, has incompatible spectral type, transports only in the wrong direction, or collapses under the topology/scale used for final assembly. Category is therefore part of the theorem, not post-processing bookkeeping.

The newest Arithmetic-Fidelity results sharpen the operator-ideal layer: stagewise membership, a bounded ideal resource, ideal-norm fidelity, scalar determinant fidelity, and relative spectral-shape fidelity are distinct levels.

## Strongest justified principle

AF-105--AF-107 separate original-range WOT assembly, WOT-closed admissibility, and collective compactness. AF-108--AF-109 show that WOT plus a uniform `S_p` budget preserves Schatten membership, while conservation of the `S_p` norm is the exact gate to norm convergence. In positive trace class, finite-window trace tightness is the additional resource needed for trace/Fredholm fidelity.

AF-110--AF-112 show that infinitesimal eigenvalue clouds can make ordinary and regularized determinants converge only to zero-free exponentials or `1`, even while finite spectral mass remains. AF-113 shows that a nontrivial profile can survive after normalization by the operator scale, but only with relative-mass tightness. Absolute and relative spectral fidelity are different categories.

Prime Circle adds the spectral-type control: compatible radial geometry has the classical half-density and continuous log-cylinder spectrum. Prime Lattice adds the order-direction gate; Weil Inertia adds confluence/resolution; Xi Flow adds collision and localization category changes. None can be crossed by naming a different topology after the desired invariant is seen.

## Consequence for synthesis

A useful realization must specify source/target range, uniform norm/ideal budget, assembly topology, admissible closure class, spectral type, absolute or relative scaling, boundary category, and direction of order transport. It must prove that the required discriminator survives with a quantitative source-forced margin in exactly that category.

## Status / novelty

The component functional analysis and operator theory are classical. The synthesis is the compatibility gate: **finite correctness and scalar spectral convergence do not imply fidelity of the limiting operator or of its relative spectral profile**.

## Falsification criterion

Construct a source-forced category crossing the current range/assembly/ideal/scale barriers while preserving target discrimination, or show that one of the stated distinctions collapses under the exact hypotheses of a concrete line.

## Lean-formalizable core

- WOT closure under uniform Schatten budget.
- Norm-conservation criterion for ideal convergence.
- Trace tightness.
- Infinitesimal determinant collapse.
- Relative-scale spectral tightness.
