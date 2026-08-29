# MI-002 — First-order transport forgets the interior, and canonical WP curvature still universalizes

**Evidence level:** supported

## Core intuition

Prime-Circle first-order transport repeatedly collapses to endpoint, exact-form, or universal symmetry data. The newer Weil--Petersson calculations show that merely passing to a second derivative is also insufficient: the canonical nonlinear curvature does couple distinct birth sectors, but on the full roots-of-unity cover it is governed by a fixed universal twisted resolvent on the thrice-punctured base and carries no free critical spectral parameter.

## Strongest justified principle

The earlier first-order no-go remains intact: circle-preserving accessory transport is exact on the relevant real slice, and natural projective/Euclidean/Schwarzian transports do not retain interior arithmetic memory. PC-040--PC-043 now sharpen the second-order boundary.

- The Weil--Petersson metric on the full cyclic cover diagonalizes in character modes with a universal holonomy profile.
- Normalized pullback along divisor refinements is exactly isometric and path flat, so the metric itself creates no prime-order refinement holonomy.
- Weil--Petersson curvature is genuinely nonzero between orthogonal birth sectors, but its coupling is the universal Green/resolvent operator on the fixed base with exact character conservation.
- The relevant resolvent is `2(L_theta+2)^(-1)`, corresponding to the regular automorphic parameter `s=2` (or `-1`), not to the critical line. Interpreting the same constant through the opposite sign convention as `s(1-s)=2` is a sign error.

Thus **nonlinearity is not enough when symmetry reduces the nonlinear response to a universal fixed-base operator**.

## What remains possible

A surviving uniformization mechanism must break the full-root-cover reduction itself. Natural possibilities already suggested by the geometry are the primitive-only composite birth surface, deformations off the maximally symmetric roots-of-unity locus, genuinely shell-dependent moduli, or a global accessory/Liouville response for which the old/new vertex pattern is not reducible to rational holonomy on one fixed base.

Higher response is relevant only if it introduces a new mathematically forced variable or coupling. Repeatedly differentiating a universal full-cover formula without breaking its symmetry would not create an RH selector.

## Status / novelty

The flat refinement, universal curvature formula, and fixed-energy identification are persisted evidence. The synthesis is a supported constraint on how a future nonlinear Prime-Circle mechanism must depart from the symmetric cover model.

## Falsification criterion

Produce a canonical nonlinear invariant on the audited full cyclic-cover family whose level dependence is not reconstructible from the universal base resolvent, rational holonomy characters, and the covering degree. Alternatively, show that the primitive-only or off-symmetric deformation still reduces to the same universal package; that would close the present escape.

## Lean-formalizable core

- Exact normalized pullback/isometry identities for divisor refinement.
- Character-conservation identities in the curvature tensor.
- Algebraic sign check locating the Green operator at `L_theta+2` rather than a critical-line spectral parameter.
