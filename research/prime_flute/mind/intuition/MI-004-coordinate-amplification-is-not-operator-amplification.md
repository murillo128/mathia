# MI-004 — The composite clone now matches the entire marked tail; only collective nonlocal assembly can still separate it

**Evidence level:** supported; compact relative resolvent and complete marked-tail asymptotic length equivalence are proved, while decisive global trace-class/wave closure and nonlocal value comparison remain open

## Core intuition

The exact prime flute and the all-composite shift clone `q_n=p_n+1` are now indistinguishable in a stronger sense than coordinate closeness. The prime/clone marking is asymptotically bilipschitz on the complete tail, so **every marked hyperbolic class carried far enough out has asymptotically the same length**, regardless of word complexity or how many pants it crosses.

A surviving spectral mechanism cannot therefore hide in a clever choice of individual tail geodesics. It must exploit a genuinely collective infinite assembly — multiplicity, interference, a relative operator ideal, scattering/resonance phase, or another nonlocal value whose accumulation is not controlled by uniform pointwise length closeness.

## Strongest justified principle

PF-121--PF-125 provide the operator/geometric baseline: a globally coherent asymptotically bilipschitz marking and compact first relative resolvent, hence equality of essential spectra. PF-126--PF-155 remove several local escape routes: the relevant body/cusp/collar budgets are summable, local squared-resolvent differences reach trace class, the first relative resolvent has the sharp `S_2` boundary, local heat coefficients are constant-curvature area data, and natural determinant/regularization changes do not manufacture a new zero divisor.

PF-166 upgrades the marked-length control. On the tail after pant `N`, the global marking has bilipschitz constant `K_N -> 1`; because curve length adds across pants, errors do not multiply with word length. Consequently the complete marked tail translation-length function of the prime flute is uniformly asymptotic to that of the exact all-composite clone, even for primitive self-intersecting words crossing arbitrarily many pants.

This kills right-limit or individual-orbit proposals based only on increasingly complicated marked lengths. It does **not** imply convergence of a full relative Selberg/Ruelle product: infinitely many individually vanishing orbit defects may still accumulate, and PF-158 already shows this distinction in a controlled separator sector.

## What remains possible

The decisive technical gate remains global assembly. One route is to globalize the local square-resolvent trace-class estimates or the compatible metric/interface criterion; another is to show that orbit multiplicity defeats every such ideal estimate.

If a relative scattering/spectral-shift/resonance object exists, its mere existence is not arithmetic evidence. The value must distinguish the exact composite clone and be stable under the admissible compact/reference changes isolated by PF-162--PF-165.

## Status / novelty

The bilipschitz-to-length implication and asymptotic length-spectrum language are classical. The project-specific content is the exact composite matched control and its uniformity over the whole tail. The synthesis is a narrowed boundary, not an isospectrality or RH theorem.

## Falsification criterion

Produce a canonical full-surface invariant that separates the prime flute from the clone while remaining stable under admissible reference changes, or prove that the global prime/clone comparison is strong enough to identify that entire nonlocal invariant. An individual marked tail length, no matter how complicated the word, cannot serve as the separator.

## Lean-formalizable core

- Tail supremum of pantwise bilipschitz constants.
- Marked geodesic length comparison under a global bilipschitz map.
- Separation between uniform orbitwise error and summability over infinitely many orbits.
- Schatten/functional-calculus implications already isolated by the line.
