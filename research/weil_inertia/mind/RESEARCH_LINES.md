# Weil-inertia research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Keep optimization loss separate from information loss

**Linked intuitions:** `MI-002-global-fenchel-dual-separates-losses`.

Global Fenchel coupling can remove artificial blockwise optimization loss, but no optimizer can reconstruct a discriminator already erased by the represented Gram/pressure data. Audit the complete represented object before strengthening inequalities on it.

## Prove source coercivity for the normalized odd Schur complement

**Linked intuitions:** `MI-001-screening-is-an-information-bandwidth-obstruction` and `MI-006-source-rigidity-can-eliminate-screening-extremizers`.

The fixed-period branch is quantitatively rigid, but raw conditioning is not the right growing-period target. WI-128 makes subextensive screening force a macroscopic bottom raw-Vandermonde near-null sector; WI-130 shows that close pair centers can produce exactly such raw collapse while the true `g/h` quotient remains transverse, and WI-131 removes the shortcut through duplicated real projections.

WI-132 isolates the orientation-sensitive invariant. After normalizing each odd direction by its horizontal depth, `S=U^*(I-P_V)U` is the grouped Schur-complement Gram matrix and `a=lambda_min(S)` satisfies the exact finite bound `n >= 2N-Q+4aD_2`, with `D_2=sum m_z(Im z)^2`. A decisive positive should derive, from unconditional zeta source constraints, a lower bound on `a` (or an aggregate lower-tail substitute) on configurations carrying macroscopic `D_2`. A decisive negative would build source-admissible growing configurations with macroscopic square depth and `a -> 0`.

Full Riesz stability of the normalized conjugation-adapted family is sufficient but stronger than necessary. The Schur quotient itself is the preferred theorem surface.

## Move from residual rank to quantitative source coercivity

**Linked intuitions:** `MI-003-coupled-welding-uniformity-is-the-fourth-moment-gate`, `MI-004-w-conditioning-is-l2-compressible-but-l1-expensive`, and `MI-005-rank-restoration-is-not-quantitative-coercivity`.

The pairwise residual branch has been classified far beyond rank: full-packed blocks become rigid finite geometries, while multi-target rank restoration can still have collapsing singular values. A surviving fourth-moment route must prove a quantitative source lower bound from information absent in the covered full-packed blocks rather than relying on generic full rank or diverging whitening.
