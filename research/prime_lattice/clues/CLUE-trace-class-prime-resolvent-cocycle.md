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

`PL-038` eliminates the most direct **scalar reciprocity/product-formula** repair to that objection. Pulling the quadratic Hilbert symbols back along `alpha -> product_p p^(alpha_p)` gives canonically arithmetic local bilinear phases that a generic Beurling system does not possess. However Hilbert reciprocity forces

```text
product_v (n(alpha),n(beta))_v = 1,
```

and for positive exponent-lattice inputs the real factor is already `1`, so the product over finite prime places is identically `1`. Moreover the quadratic Hilbert symbol is symmetric, so its induced projective commutator phase is locally trivial as well. Thus even **canonical arithmetic local data that passes the Beurling-discrimination test can collapse completely under its canonical scalar global normalization**. Reciprocity is necessary structure, but scalar reciprocity by itself is not the missing spectral rigidity.

`PL-039` now eliminates the most canonical **operator-valued automorphic scattering** repair on the ordinary zeta channel. For unramified rank-one/`GL_2` principal series, each local spherical space is one-dimensional and the standard intertwiner acts on its normalized spherical vector by the Gindikin--Karpelevich scalar

```text
c_p(u)=L_p(u)/L_p(u+1).
```

For the trivial channel the finite product is `zeta(u)/zeta(u+1)` in its convergence region; with `u=2s-1` and the archimedean factor this is the classical scalar modular scattering coefficient `Lambda(2s-1)/Lambda(2s)`. Dividing by `c_p(u)` leaves only normalized Weyl transport on the spherical line. Therefore the local operator family contains no additional matrix datum carrying the Riemann divisor after normalization: keeping the scalar returns the classical scattering route of `PL-033`, while removing it removes the zeta-sensitive factor. This closes the unramified spherical scattering branch without claiming that all non-spherical or target-relative operator constructions are exhausted.

`PL-040` closes the **standard finite-level non-spherical** repair to `PL-039`. Adelic automorphic representations and principal-series sections are restricted tensor products: a fixed smooth vector is equal to the distinguished spherical vector at all but finitely many finite primes. The global standard intertwiner therefore separates into the same infinite scalar L-factor normalization outside a finite set `S` and only a finite product/tensor of genuinely non-spherical normalized local operators at `S`. Adding a K-type, level, Iwahori vector, or other finite-place ramification to one standard Eisenstein channel can create real local matrix structure, but it cannot attach such operator data to the infinitely many prime directions simultaneously. Any route using an unbounded family of levels or an infinite nonspherical tensor would be a new global object and must establish its own canonicity, continuation, and coupling to the ordinary level-one zeta scalar.

`PL-041` closes the **canonical target-relative model-space co-shift** repair. For any inner function `B`, the defect space `K_B=H^2(C_+) \ominus B H^2(C_+)` carries the adjoint multiplier semigroup `T_t^B=M_(exp(-tz))^*|_(K_B)`, and the arithmetic prime family is only the sampling `T_p^B=T_(log p)^B`. Every zero of `B` gives the corresponding joint prime eigenmode, but a one-zero Blaschke factor at an arbitrary interior point has exactly the same semigroup, contraction, multiplicativity, and eigenvector structure. Hence compressing the prime dilations to the Nyman defect represents a chosen off-line divisor but does not localize it.

`PL-042` closes the next **standard Clark/Aleksandrov boundary-spectral** repair to that model. Every inner function has positive Clark measures and unitary rank-one model perturbations with boundary-supported spectrum. The degree-one Blaschke control makes the obstruction exact: an arbitrary interior zero `a` produces, for every Clark parameter, a positive atomic spectral measure and a unitary boundary eigenvalue. Thus positivity, unitarity, or boundary spectral support of the standard Clark family cannot force the Nyman/zeta defect zeros to the critical boundary; those properties are universal functional-model structure.

Accordingly, the clue survives only after further strengthening. Further work should **not** ask whether `S_1` membership, a determinant, an ordinary scalar `p,q,pq` cocycle law, a nontrivial scalar projective multiplier, a scalar Hilbert-symbol/product-formula normalization, the normalized unramified spherical standard intertwiner, a fixed finite-level nonspherical modification, the canonical Nyman/model-space co-shift, or its standard Clark boundary spectralization can supply the missing rigidity. The live question is whether a canonically specified **genuinely global or arithmetic target-relative** operator family is intrinsic to the ordinary zeta problem, has information content extending over infinitely many prime directions, remains nontrivial after L-factor normalization and reciprocity, and imposes a trace/positivity/localization identity that fails for arbitrary inner-function and Beurling controls. A coupling to the distinguished Nyman target, Möbius data, the explicit formula/Weil positivity, or another non-universal arithmetic observable could qualify; another standard functional-model representation of a pre-existing zeta inner factor would not.

Acceptance means this narrowed question is worth active investigation. It does not mean such an invariant exists, is new, or would imply RH.
