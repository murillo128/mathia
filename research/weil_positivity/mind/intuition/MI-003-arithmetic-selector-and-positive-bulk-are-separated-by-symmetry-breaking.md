# MI-003 — Arithmetic information can survive positivity, but canonical completion often externalizes it into determinants or absolute values

**Evidence level:** supported by exact finite selectors and decisive completion/symmetry obstructions

## Core intuition

The current evidence rules out the crude slogan that positivity destroys arithmetic. Canonical positive operators, Gram kernels, determinant lines, and polarizations can retain exact `Lambda(n)` or `log p`. The recurring failure occurs at the operation that is supposed to turn that carrier into the completed Weil sign: arithmetic is canceled across a complex, pushed into a logarithmic determinant, made universal by symmetry, or converted to an absolute value that no longer carries an independent sign theorem.

## Strongest justified principle

The earlier radial and Hodge/Prym results already separated carrier from pairing. Finite radial Schur limits either attenuate arithmetic to zero, diverge, or return an indefinite congruence of the birth form; principal divisor/class reductions and normalized Hodge transfer erase the desired finite coefficient; the Prym polarization kernel stores a genuine `p`-discriminant but finite torsion cannot support the required ordered real quadratic pairing.

WP-058 strengthens the positive side. The same Prym discriminant exports canonically to the Hodge determinant line: the polarization metric gives lattice covolume `p^{g_n}`, so `log p` is present in an honest positive norm. Yet the real polarization map is an isometry to its metric dual, so its canonical positive singular-value operator is exactly the identity. The prime scale lives in the integral lattice position/determinant, not in a linear positive spectrum.

WP-059 resolves the strongest theta-action clue. Letting the Prym torsion act on the non-torsion Heisenberg representation before positivity produces a phase-free positive adjoint defect whose normalized log pseudodeterminant is `log p`. But that operator is exactly a multiplicity of the ordinary `p`-cycle Laplacian; its trace is universal, direct `p^k` depth gives `k log p`, and the mechanism is a classical determinant identity rather than a linear Weil pairing.

WP-060 then shows that the most canonical untwisted analytic-torsion completion of the same determinant-line carrier erases it: on the relevant even-dimensional flat Prym torus the de Rham determinant-line volume cancels across degrees and Ray--Singer/holomorphic torsion is trivial. Any torsion escape must therefore add genuine twisting/family/boundary structure before the determinant is formed.

The Hardy route exposes the parallel sign problem. WP-061 constructs a canonical positive `q=2` primitive-shell Gram kernel, but the independently selected **full-root** `q=2` archimedean Hardy channel is indefinite and the positive Gram does not preserve finite-place sparsity. WP-062 proves that every nonzero half-turn-equivariant compression of that full-root channel remains indefinite. WP-063 classifies the most natural symmetry-breaking Krein repair: among parity-exchanging self-adjoint unitary metrics, positivity forces the spectral-sign metric and the repaired operator is exactly the polar absolute value. That is a repair of sign, not an independent sign theorem.

## What remains possible

A successful construction must couple the finite selector and archimedean/polar sector before determinant, full-cohomology cancellation, symmetric compression, or polar absolute-value repair. A twisted Prym family, a non-polar metric forced by additional geometry, or a genuinely nonseparable finite--archimedean operator remains logically possible, but none is established.

## Status / novelty

The determinant-line norm, cycle-Laplacian reduction, torsion cancellation, Hardy chiral obstruction, and unique polar repair are persisted findings with classical ingredients. Their common “positive carrier versus completed sign” interpretation is a supported synthesis.

## Falsification criterion

Derive a canonical completed positive pairing that retains one of the audited selectors and has an independently proved sign. Within the closed families, a nonzero half-turn-equivariant positive compression would contradict WP-062, while a different parity-exchanging unitary Krein metric producing positivity would contradict WP-063.

## Lean-formalizable core

- Determinant/covolume identity from a symplectic polarization matrix.
- Cycle-Laplacian pseudodeterminant identity.
- Chiral-symmetry no-positive-compression lemma.
- Uniqueness of the polar-sign Krein repair.