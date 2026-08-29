---
id: CLUE-prime-lattice-trace-class-prime-resolvent-cocycle
type: research-clue
status: accepted
origin: mind
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-024-bost-connes-log-prime-covariance.md
  - research/prime_lattice/findings/PL-025-unitary-prime-shift-covariance-full-spectrum.md
  - research/prime_lattice/findings/PL-026-trace-class-covariance-spectral-shift-obstruction.md
  - research/prime_lattice/findings/PL-028-resolvent-mod-compact-covariance-vacuity.md
---

# Can a specified prime action carry nontrivial trace-class relative resolvent data?

## Observation

The audited prime-shift operator classes leave a narrow unresolved gap. Exact unitary logarithmic covariance is too rigid, additive trace-class covariance at the Hamiltonian level forces at-most-linear counting, and compact or `S_q`, `q>1`, covariance after taking a compact resolvent is automatic. PL-028 identifies `S_1` as the first ordinary Schatten level not forced by Riemann-zero density, while also showing that the scalar translation `H -> H+log p` already contributes a trace-class resolvent difference by itself.

## Research question

Is there a **canonically specified prime action** — preferably arising from the one-sided exponent-lattice representation, a target-relative Hardy/Nyman construction, or a noncompact adelic reference — for which the unitary/isometric part of a relative resolvent cocycle is trace class and has a nontrivial spectral-shift or determinant invariant not reducible to scalar translation, Bost--Connes partition data, or compact-resolvent tautology?

## Why it may matter

A positive answer would identify a mathematically precise operator layer between the prime-lattice symmetry no-go results and a full Hilbert--Pólya construction. A negative answer could close the remaining Schatten-level escape and strengthen the conclusion that prime-coordinate translations are only scaffolding unless coupled to an external target/completion.

## Decisive test

Choose one prime action and reference representation forced by already-persisted Prime-Lattice structure. Prove or disprove trace-classness of the **action-dependent** relative resolvent difference after subtracting the scalar `+log p` contribution. If trace class, compute its trace/spectral-shift/Fredholm determinant and test whether it survives Beurling matched controls and avoids reduction to known Bost--Connes/Connes data. If every canonical candidate is either non-trace-class, automatic, or classicalized, reject the clue.

## Evidence boundary

No such action-dependent `S_1` cocycle has been constructed in the persisted evidence. PL-028 only proves that this level is not automatic and explicitly leaves noncompact-reference scattering and specified prime actions outside its no-go. The clue makes no claim that a useful determinant exists, is novel, or is related to Riemann zeros.

## Research disposition

Accepted as a **narrow operator-design question**, not as evidence for RH or for novelty.

`PL-034` performs the first decisive candidate/prior-art audit. The canonical Bost--Connes prime isometry gives

```text
mu_p^* (H-z)^(-1) mu_p = (H+log p-z)^(-1),
```

so its action-dependent residual after subtracting scalar translation is exactly zero. On the other hand, classical Hardy/model-space work of Amosov--Baranov--Kapustin shows that trace-class perturbations of the unilateral shift semigroup can carry prescribed spectral components, while trace-classness of the unitary cocycle itself is trivial in their explicit model. Classical resolvent-comparable perturbation theory also supplies determinants and spectral-shift functions once `S_1` comparability is assumed.

Accordingly, the clue survives only after strengthening its target. Further work should **not** ask whether `S_1` membership or a determinant can be obtained. It should ask whether a canonically specified family indexed jointly by the primes forces a nonzero relative invariant with an arithmetic compatibility law — for example multiplicative/cocycle relations across `p`, `q`, and `pq` — that cannot be freely prescribed through an inner/model-space scattering datum and that survives Beurling matched controls.

Acceptance means this narrowed question is worth active investigation. It does not mean such an invariant exists, is new, or would imply RH.
