# Weil-inertia research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Keep optimization loss separate from information loss

**Linked intuitions:** `MI-002-global-fenchel-dual-separates-losses`.

Global Fenchel coupling can remove artificial blockwise optimization loss, but no optimizer can reconstruct a discriminator already erased by the represented Gram/pressure data. Audit the complete represented object before strengthening inequalities on it.

## Prove source coercivity for the depth-weighted Schur lower tail

**Linked intuitions:** `MI-001-screening-is-an-information-bandwidth-obstruction`, `MI-006-source-rigidity-can-eliminate-screening-extremizers`, and `MI-007-depth-weighted-schur-tail-is-screening-invariant`.

The normalized conjugation-odd quotient remains the preferred theorem surface, but WI-133 rules out its single minimum eigenvalue as a density-scale invariant: endpoint tapering can force `lambda_min(S)->0` on a fixed-depth conjugate lattice while every diagonal odd distance and the total horizontal remainder remain extensive.

WI-134 gives the correct aggregate replacement. After expanding multiplicities, the exact horizontal charge satisfies a depth--spectrum rearrangement bound and, for every fixed depth cutoff `A` and Schur threshold `a`,

`H >= a(D_{2,A}-A^2 r_a)_+`,

where `r_a` counts normalized Schur eigenvalues below `a`. Near-sharpness with macroscopic bounded square depth therefore forces a **macroscopic lower spectral sector** toward zero, not merely one soft mode. A decisive positive should use unconditional zeta source information to exclude that depth-matched spectral collapse or to force horizontal-depth collapse toward the line; a decisive negative would build source-admissible configurations realizing it.

Full Riesz stability is sufficient but stronger than necessary. Positive spectral quantiles, depth-weighted trace distribution, or an equivalent source-frame bound are the preferred targets.

## Move from residual rank to quantitative source coercivity

**Linked intuitions:** `MI-003-coupled-welding-uniformity-is-the-fourth-moment-gate`, `MI-004-w-conditioning-is-l2-compressible-but-l1-expensive`, and `MI-005-rank-restoration-is-not-quantitative-coercivity`.

The pairwise residual branch has been classified far beyond rank: full-packed blocks become rigid finite geometries, while multi-target rank restoration can still have collapsing singular values. A surviving fourth-moment route must prove a quantitative source lower bound from information absent in the covered full-packed blocks rather than relying on generic full rank or diverging whitening.
