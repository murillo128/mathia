# MI-015 — Canonical global prime data needs source-forced cross-block dynamics to constrain zeta

**Evidence level:** literature-backed reciprocity/global-selector boundaries and exact adelic class-field character-block collapse through PL-250

## Core intuition

Prime Lattice does not lack canonical global arithmetic data. The problem is that standard linear readouts decompose it into neighboring character channels, with Riemann zeta sitting in a trivial block that is algebraically protected from the richer Frobenius information.

Thus “keep the whole global object” is still insufficient when its canonical linearization is block diagonal. The missing mechanism is a source-forced relation that actually couples those blocks and remains meaningful in the principal target.

## Strongest justified principle

PL-240--PL-248 show that reciprocity families carry mixed-prime information but clean principal residues discard it, while affine/Kac--Moody corrections either stay row-local, retain free scalar choices, or obtain function-field localization only after extra purity input.

PL-249 supplies canonical class-field geometry: finite abelian covers attach Frobenius monodromy to rational-prime orbits, but the trivial character sends every Frobenius to `1`, giving exactly `zeta_Q`. PL-250 keeps the full cover via the regular representation and still finds a canonical split. Finite Fourier transform decomposes `C[G]` into character lines, `G`-equivariant operators are block diagonal, and Artin determinants factor as `zeta_L= zeta_Q product_{chi≠1}L(s,chi)`. The principal block is not dynamically informed by the others.

## Program consequence

Seek a nonlinear invariant, canonically non-equivariant correspondence, or independently justified global positivity/duality relation that forces cross-character interaction and yields an actual statement about the trivial zeta block. The source must determine the coupling; inventing a mixing matrix does not count.

## Counterevidence / boundary

PL-250 is finite abelian and linear/equivariant. It does not rule out nonabelian, nonlinear, cohomological, or genuinely global relations that couple factors. Nor does factorization prove that no theorem about the whole cover can constrain an individual factor; such a theorem simply has not been supplied by the standard Artin formalism.

## Epistemic status

**Exact principal-block isolation through both scalar projection and full abelian equivariant retention; source-forced cross-block dynamics remains open.**

## Falsification criterion

Exhibit a standard linear `G`-equivariant full-cover operation whose principal block depends nontrivially on other characters, or invalidate the Artin block decomposition used by PL-250. A positive continuation should derive a canonical coupling outside that class and prove its principal-zeta effect.
