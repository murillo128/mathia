---
id: CLUE-prime-lattice-bruhat-tits-local-prime-geometry
type: research-clue
status: resolved
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/prime_lattice/README.md
  - research/prime_lattice/findings/PL-014-tate-adelic-self-dual-axis.md
  - research/prime_lattice/findings/PL-039-unramified-spherical-scattering-scalarization.md
  - research/prime_lattice/findings/PL-040-restricted-tensor-nonspherical-finite-place-obstruction.md
---

# Can Bruhat–Tits local geometry add arithmetic structure beyond the prime-exponent lattice?

## Observation

`prime_lattice` currently treats each rational prime as an independent exponent direction, with `log p` providing the corresponding additive energy/frequency, and already allows adelic/idèlic structure when a genuinely global completion is required. `PL-014` shows that the adelic completion supplies a canonical self-dual global axis but does not by itself localize the Riemann zero divisor.

The local automorphic audit has also exposed a sharper boundary. `PL-039` shows that on the canonical unramified spherical channel for `GL_2(Q_p)`, the local standard intertwiner is one-dimensional and all zeta-sensitive information is carried by the scalar local L-factor normalization. `PL-040` then shows that moving to a fixed smooth nonspherical adelic vector changes only finitely many finite places, so it does not create an operator-valued coupling across the full infinite family of prime coordinates.

A possible residual direction is to replace the bare prime axis by the canonical local geometry that sits behind the p-adic group itself: the Bruhat–Tits building. For `PGL_2(Q_p)` this is the `(p+1)`-regular tree; in higher rank it becomes a recursive simplicial complex. The question is not whether these buildings exist or have rich spectral theory, which is classical, but whether their intrinsic geometry carries any rational-prime-specific information that survives the scalarization and restricted-tensor obstructions already established in this line.

## Research question

Starting with the Bruhat–Tits tree `B_p` of `PGL_2(Q_p)`, does a canonical geometric or spectral construction — adjacency/Hecke operator, Laplacian, radial Green function, return-path generating function, boundary operator, or another intrinsic observable — produce the local prime-power structure

```text
p, p^2, p^3, ...
```

and its Euler-factor response without inserting the weights `p^(-ks)` by definition?

More strongly, after identifying the exact spherical scalar part already covered by `PL-039`, is there any canonical residual operator or higher-rank building datum whose adelic assembly couples infinitely many prime places in a way that is not reduced by `PL-040` to finitely supported nonspherical corrections times the same scalar L-factor product?

The intended comparison is therefore:

```text
prime as exponent-lattice axis
    -> only multiplicative coordinate data

prime as Bruhat–Tits local geometry
    -> recursive p-adic incidence / path / boundary structure
    -> ? intrinsic local spectral datum
    -> ? genuinely new global coupling
```

The direction is useful only if the second route retains arithmetic information that the first and the already-audited spherical scattering channel do not.

## Why it may matter

A positive answer would give `prime_lattice` a geometrically canonical enrichment: each prime would label a full local recursive geometry rather than merely a coordinate direction. That could provide a natural source for prime-power depth, local operators, and local-to-global assembly before any Riemann-zero data are inserted.

A negative answer would also be valuable. If every natural Bruhat–Tits construction relevant to the trivial zeta channel either depends only on the generic branching parameter, scalarizes to the usual Satake/Gindikin–Karpelevich Euler factor, or requires nonspherical data that are finitely supported in the restricted tensor product, then a broad class of "replace each prime axis by a p-adic geometry" proposals can be classicalized or killed at once rather than rediscovered piecemeal.

## Decisive test

Use the cheapest rank-one model first.

1. Take the Bruhat–Tits tree `B_p` of `PGL_2(Q_p)` with its canonical adjacency/Hecke operator and distinguished spherical base vertex.
2. Derive the radial resolvent, Green function, return-path generating function, or equivalent canonical spectral response directly from the tree. Do not assign `p^(-ks)` to depth `k` by hand merely to reconstruct the Euler product.
3. Identify exactly which part of the resulting response is the standard spherical Hecke/Satake or intertwining scalar already covered by `PL-039`.
4. Test whether any residual datum survives canonical spherical normalization and remains nontrivial on the ordinary Riemann-zeta channel.
5. Run a branching control: replace `B_p` by a generic `(q+1)`-regular tree or analogous non-prime local model. If the candidate depends only on `q` as a free branching parameter and has no mechanism selecting the exact rational-prime norm map, it is not a prime-specific escape.
6. Only if rank one leaves a genuine residual structure, test whether a higher-rank Bruhat–Tits building provides an intrinsic nonscalar local invariant whose global construction avoids the finite-exception support obstruction of `PL-040` and has a mathematically defined continuation into the critical strip.

Reject the direction if the rank-one calculation shows that every zeta-sensitive local quantity is already the classical scalar Euler/L-factor data, or if the same mechanism works unchanged for arbitrary regular-tree branching with no rational-prime discriminator.

## Evidence boundary

No new RH mechanism, positivity principle, zero-localization theorem, or non-scalar global operator is established here. Bruhat–Tits buildings, their Hecke/Laplacian spectral theory, and their relation to unramified representation theory are classical prior art.

`PL-039` creates a strong prior obstruction: the canonical unramified spherical channel carrying the ordinary Riemann Euler factor is one-dimensional, so any building construction that merely reproduces spherical harmonic analysis is expected to scalarize to known local L-factor data. `PL-040` creates a second obstruction: ordinary fixed smooth nonspherical adelic data are exceptional at only finitely many primes and therefore do not automatically produce the required infinite-prime operator coupling.

The unresolved question is narrower: whether the full local recursive geometry contains an intrinsic residual observable outside those two reductions, with a cheap rank-one falsification test and a clear generic-tree control. Until that test is passed, the building viewpoint should be treated only as a proposed enrichment of `prime_lattice`, not as evidence for a new research line or for a connection to the Riemann zero divisor.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/prime_lattice/findings/PL-104-bruhat-tits-universal-tempered-half-axis.md]]

The rank-one decisive test is negative. The adjacency/Hecke radial recurrence on the Bruhat–Tits tree gives the classical Satake parametrization `lambda(s)=q^s+q^(1-s)` and therefore a canonical tempered axis `Re(s)=1/2`, but the radial Green function, Plancherel measure, return-path data, and boundary-depth scaling depend only on the homogeneous branching parameter `q`. The same half-axis and spectral package occur on abstract `(q+1)`-regular trees, including controls such as `q=6` that have no local-field origin.

For `Q_p`, prime-power depth is indeed geometrized and can generate the usual `p^(-ks)` Mellin/Satake response, but on the ordinary unramified zeta channel this is exactly the classical scalar local L-factor already isolated by `PL-039`. No zeta-sensitive residual survives spherical normalization, and `PL-040` blocks the fixed-vector nonspherical repair across infinitely many primes. Under this clue's own gate, there is therefore no reason to escalate to higher-rank buildings without first specifying an additional genuinely global or nonspherical coupling outside the tested route.
