# MI-002 — First-order transport and circle-preserving accessory geometry are flat

**Evidence level:** proved for the audited mechanisms; supported as a broader design rule

## Core intuition

The original prime-circle data repeatedly lose their interior refinement when they are converted into a **first-order equivariant transport law**. The newer uniformization evidence shows that this is not limited to elementary transfer matrices: even the natural tangential accessory field on the circle-preserving moduli slice is an exact one-form, while that slice is Weil–Petersson Lagrangian. A viable geometric memory mechanism therefore has to survive beyond first-order transport.

## Strongest justified impossibility principle

Four mathematically different constructions now exhibit the same flatness pattern.

1. PC-013: projective moving-frame transport telescopes as a product of successive gauge changes.
2. PC-014: exact Euclidean Helmholtz transfer satisfies a semigroup law and remembers only total path length.
3. PC-018: the Schwarzian factor-introduction defect is an exact cocycle, so its square curvature vanishes.
4. PC-030: on the real slice where all punctures remain on the original circle, the Weil–Petersson symplectic form vanishes and the tangential accessory form is
   \[
   \Theta=\frac12 d(S|_{\mathcal L}),
   \]
   hence `dTheta=0` and its circulation vanishes on an ordered chamber.

The common lesson is stronger than “one-dimensional products telescope.” Whenever the canonical first-order response is a functorial transport, cocycle, or gradient on the symmetry-preserving deformation space, its holonomy cannot carry the desired interior arithmetic refinement.

## What remains genuinely open

PC-030 does **not** kill the nonlinear uniformization branch. The symmetric Hessian of the restricted Liouville action, the nonzero Weil–Petersson metric on the real slice, global monodromy, interactions among several shell levels, and deformations leaving the circle-preserving locus are not first-order exact transports. These are precisely the places where curvature or mixed response may survive.

The relevant distinction is therefore not “local versus global” by itself. A globally determined first-order vector field can still be exact. The surviving object must contain a non-concatenative second variation, a noncommuting/multi-path effect, or another obstruction to reduction to one scalar potential.

## Status / novelty

The telescoping, semigroup, cocycle, Lagrangian-fixed-locus, and Liouville-generating-function ingredients are classical or exactly derived. The durable synthesis is the repeated **flatness test** they impose on future prime-circle proposals.

## Falsification criterion

Find a canonical first-order circle-preserving transport derived from the current geometry whose holonomy around a contractible ordered deformation loop is nontrivial after gauge removal, or show that one of the four audited exactness statements fails under its stated hypotheses.

## Lean-formalizable core

- Telescoping and semigroup identities for the discrete transports.
- Cocycle identity implying zero factor-introduction curvature.
- Abstract fixed-locus lemma: an anti-holomorphic Kähler isometry has Lagrangian fixed locus when dimensions match.
- Exactness of the restricted accessory one-form and vanishing of its loop integral on a contractible chamber.
