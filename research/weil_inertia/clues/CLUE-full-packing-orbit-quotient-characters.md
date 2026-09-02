---
id: CLUE-weil-inertia-full-packing-orbit-quotient-characters
type: research-clue
status: proposed
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-102-full-recurrent-packing-is-an-exact-collapsed-circle-rotation.md
  - research/weil_inertia/formalization/WI102CollapsedRotation.lean
  - research/weil_inertia/findings/WI-096-residual-prime-rank-defect-is-exact-free-cycle-count.md
  - research/weil_inertia/findings/WI-099-residual-prime-rank-defect-is-single-rotation-resonance.md
---

# Do full-packing defect modes form quotient characters that constrain shared-source intersections?

## Observation

The WI-102 formalization makes more structure first-class than the canonical finding uses. After the common hole is collapsed, Lean defines the generated rotation subgroup

\[
H=\langle R\rangle\le \mathbf Z/t\mathbf Z
\]

and the orbit space itself as the additive quotient

\[
Q=(\mathbf Z/t\mathbf Z)/H,
\]

then proves `|H|=t/g` and `|Q|=g` for `g=gcd(R,t)`. WI-102 uses the same arithmetic only to count the `g` rotation cycles. WI-096 and WI-099 independently identify the true row kernel as functions constant on the equal free cycles, subject to one global zero-mean relation, but they do not organize those cycle coordinates by the quotient-group structure exposed by Lean.

At full packing there are no path components, and the WI-102 collapse equivalence conjugates the exceptional permutation to `x -> x+R`. Combining the persisted results therefore suggests a stronger normal form: the row kernel should be naturally the mean-zero function space on `Q`, equivalently the augmentation ideal of the regular representation of the cyclic quotient. Since `H` is the subgroup of multiples of `g` in `Z/tZ`, `Q` identifies with `Z/gZ`, so its nontrivial characters would give a canonical basis rather than an arbitrary choice of `g-1` cycle coordinates. Pulled back through the explicit order collapse, those modes become piecewise characters on the original `p` residue coordinates, with a phase jump across the deleted interval.

## Research question

First, can the full-packing Ramanujan row kernel be identified exactly and constructively as

\[
\ker_{\rm row}G_{p,q}^{(N)}
\simeq
\left\{F:Q\to\mathbf C:\sum_{x\in Q}F(x)=0\right\},
\qquad
Q=(\mathbf Z/t\mathbf Z)/\langle R\rangle,
\]

with the nontrivial characters of `Q` pulling back to an explicit basis in the original `p`-frequency coordinates?

More importantly, does this quotient-character representation impose a new simultaneous constraint when two full-packing residual interactions share the same source modulus `p` at one observation length `N`? For two targets `q_1,q_2`, let `K_i` be the corresponding row-kernel subspaces and `g_i=gcd(R_i,t_i)`. Does a nonzero vector in `K_1\cap K_2` require compatibility between the two quotient characters or a common nontrivial quotient of `Q_1` and `Q_2`? A particularly sharp first possibility to test is whether

\[
\gcd(g_1,g_2)=1
\quad\Longrightarrow\quad
K_1\cap K_2=\{0\}
\]

throughout the simultaneous full-packing regime, or whether the different collapse maps allow common source modes even when the quotient orders are coprime.

## Why it may matter

WI-102 is explicitly a stopping rule for extracting more scalar pairwise rank information from the zero-slack sector and points instead toward simultaneous/source-labelled consistency. The quotient object introduced by Lean supplies a concrete coordinate system for exactly that next question: each saturated pairwise defect is not merely `g-1` dimensions, but potentially a family of source-space modes labelled by nontrivial characters of a finite cyclic quotient.

If shared-source intersections are strongly restricted by quotient compatibility, extensive pairwise defects could fail to coexist even when every individual pair has the allowed WI-096/WI-102 rank defect. That would be genuinely new information for many-modulus aggregation. Conversely, if coprime quotient orders or incompatible character labels still admit large common source intersections, that would be a useful negative result showing that the Lean quotient structure is only a repackaging of pairwise cycle coordinates and supplies no additional simultaneous rigidity.

## Decisive test

Prove the single-pair quotient normal form first, without using numerical rank tolerance: identify `Q` with `Z/gZ`, pull every nontrivial quotient character back through the WI-102 collapse, verify directly from the WI-096 residue-sum equations that these vectors lie in the true row kernel, and prove that they span its `g-1` dimensions. The examples underlying the full three-cycle and five-cycle packings provide small exact checks, but the proof should be symbolic.

Then fix one source prime `p` and one observation length `N`, enumerate exact target primes for which two or more residual edges are simultaneously full-packed, and compute the intersections of their pulled-back character spaces in the shared `p`-frequency coordinates. A single exact example with `gcd(g_1,g_2)=1` and `K_1\cap K_2\ne\{0\}` kills the sharp coprime-order conjecture. If the conjecture survives, derive the compatibility condition directly from the two piecewise collapse maps and test whether the general intersection dimension is controlled by a common quotient/character order rather than by ambient dimension alone.

## Evidence boundary

Lean currently proves the collapsed rotation, the generated subgroup cardinality, and the quotient cardinality. It does not formalize WI-096's exact `tau=c-1` bridge, identify the Ramanujan row kernel with functions on the quotient, construct quotient-character null vectors, or prove any simultaneous intersection theorem. WI-096/WI-099 make the single-pair mean-zero cycle-coordinate model available mathematically, so the proposed character description is motivated by combining persisted results with the extra quotient structure exposed by formalization; its claimed usefulness for shared-source consistency remains completely unvalidated. No many-modulus, Yang-covariance, or zeta-zero consequence is asserted.