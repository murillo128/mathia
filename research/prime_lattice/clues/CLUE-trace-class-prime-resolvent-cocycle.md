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

`PL-035` eliminates the next simplest escape: ordinary scalar multiplicative or translated 1-cocycle compatibility across `p`, `q`, and `pq` is itself non-discriminating. For any nonzero meromorphic `F`,

```text
Delta_n(z)=F(z+log n)/F(z)
```

obeys the exact prime-semigroup cocycle law, and the same construction works after replacing `log p` by arbitrary Beurling prime weights. Hence an exact scalar chain rule can be manufactured around freely chosen spectral data and cannot by itself be the sought arithmetic rigidity.

`PL-036` removes the next projective escape at the level of the bare exponent semigroup. For arbitrary pairwise phases `theta_(p,q)`, the bilinear multiplier

```text
omega_theta(alpha,beta)
  = exp(2 pi i sum_(p<q) theta_(p,q) alpha_p beta_q)
```

defines a genuine projective prime action with

```text
V_p V_q = exp(2 pi i theta_(p,q)) V_q V_p.
```

The pairwise phases are gauge-invariant but freely assignable; classical multiplier theory identifies this as ordinary cohomology of the free abelian group completion, and Ore-semigroup dilation shows that the positive cone has the same `H^2`. The construction ignores the energy vector entirely and survives arbitrary Beurling replacement. Thus merely upgrading from a flat scalar `1`-cocycle to nonzero scalar projective curvature still does not supply arithmetic rigidity.

Accordingly, the clue survives only after a third strengthening. Further work should **not** ask whether `S_1` membership, a determinant, an ordinary scalar `p,q,pq` cocycle law, or a nontrivial scalar projective multiplier can be obtained. It should ask whether a canonically specified prime family forces joint structure whose gauge/cohomology class is fixed by arithmetic rather than freely chosen on the prime generators — most plausibly an operator-valued scattering relation or a global adelic/reciprocity/product-formula normalization — and whether that extra structure fails for matched Beurling controls.

Acceptance means this narrowed question is worth active investigation. It does not mean such an invariant exists, is new, or would imply RH.
