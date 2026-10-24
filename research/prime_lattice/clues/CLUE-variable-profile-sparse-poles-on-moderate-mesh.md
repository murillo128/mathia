---
id: CLUE-prime-lattice-variable-profile-sparse-poles-on-moderate-mesh
type: research-clue
status: resolved
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles.md
  - research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md
  - research/prime_lattice/findings/PL-467-relative-frame-admits-sparse-common-off-critical-poles.md
  - research/prime_lattice/findings/PL-468-fixed-profile-sparse-overwrites-force-a-natural-boundary.md
  - research/prime_lattice/clues/CLUE-density-one-dyadic-variance-arithmetic-recovery.md
---

# Can changing log-block profiles preserve positive residue sources and sparse poles on a moderately sparse mesh?

## Observation

PL-468 rules out a fixed smooth overwrite profile on the mesh `j_k=3^k`: its common Mellin factor multiplies a scalar lacunary series with a natural boundary. Its conclusion expressly leaves changing within-block profiles open. PL-467 separately realizes positive integer-supported residue sources and negative real off-critical pole residues, but violates the absolute variance ceiling at every large scale when `beta>1-theta/2`.

MC-524 supplies a different analytic control. For `1/2<beta<1` and `gamma>0`, it constructs one square-free-supported signed sequence with complete window bounds on

`G_* = N_{>=1} \ {j_k-1,j_k : k>=k_0}`, `j_k=floor(k log k)`.

Only `O(J/log J)` indices up to `J` are omitted, and successive retained indices differ by at most three. Its Dirichlet series is meromorphic on `Re s>1/2`, with only the simple poles `beta +/- i gamma`, both of residue `1/2`. The mechanism matches increasingly many logarithmic moments of a reference exponential on each interval between overwrite blocks. A different signed profile is used in each block, with physical amplitude `x^(beta-1+o(1))`; the sum of transform errors is entire. A common scalar lacunary factor cannot replace these profiles.

This is more than continuation of MC-523's unspecified transform, but the mesh is materially different from the accepted Prime-Lattice clue: `O(J/log J)` omissions replace `O(log J)` omissions. MC-524's signs and positive pole residues also do not satisfy that clue's positive-source/negative-residue control class.

## Research question

Fix `0<theta<1`, `1-theta/2<beta<1`, and `gamma>0`. On **MC-524's mesh `G_*`**, can one construct a single bounded sequence `b_n>=0`, vanishing on multiples of 5, such that each nonzero residue has cumulative mass `x/4+o(x)` and, for every sufficiently large `j in G_*`,

`X_j=2^j`, `H_j=floor X_j^theta`,
`P_j(y)=sum_(y<n<=y+H_j, n=1 mod 5) b_n`,
`mu_j=X_j^(-1) int_(X_j)^(2X_j) P_j(y) dy`,
`int_(X_j)^(2X_j)|P_j-mu_j|^2 dy << X_j H_j (log X_j)^A`

for some fixed finite `A>=0`, while all four transforms `D_chi(s)=sum_n b_n chi(n)n^(-s)` are meromorphic on `Re s>1/2` and have simple noncancelling **negative real** residues at `beta +/- i gamma`? Apart from the principal channel's pole at 1, require no other poles in that half-plane. Retain the exact identity-residue relation `D_1^res=(1/4)sum_chi D_chi`.

This tests positivity and residue-sign compatibility of the changing-profile mechanism on a declared mesh. It does not ask for a relative covariance frame, actual von Mangoldt coefficients, an Euler product or a functional equation.

## Why it may matter

A successful control would show that positive coefficient and pole-sign constraints do not restore density-one recovery on this moderately sparse mesh. A proved incompatibility would identify a source constraint absent from the signed Möbius control. Either outcome would sharpen the first unsupported implication in sparse-scale Mellin recovery without assuming the all-block holomorphic remainder of PL-466.

The existing accepted clue retains its much thinner mesh and actual-prime question. Neither a success here nor MC-524 itself resolves it. The distinction is scale coverage as well as coefficient geometry.

## Decisive test

Reconstruct MC-524's moment-matching density and its compact-uniform transform-error estimate. Test an atomic **cell-integral** realization on the progression `n=1 mod 5`, added with the required sign to a fixed positive background, rather than point-sampling a profile with increasing oscillation. Check together: eventual coefficient positivity and boundedness; fixed interior support so every retained window misses the correction; the residue masses; holomorphy of the atomic transport error; the sign and normalization of each principal part; and conjugation compatibility of the four character channels. The derivative of a growing-degree profile must not be treated as uniformly bounded. Any pole surviving only in a continuous model is insufficient.

Preserve `j_k=floor(k log k)` throughout that test. MC-524 uses interblock log lengths `O(log j_k)` to balance profile size against the Taylor remainder. Substituting `3^k` into those estimates is not justified. If that thinner mesh is attempted later, it needs a separate quantitative argument and must be reconciled with the accepted clue and PL-468.

If the construction fails, identify a necessary inequality violated by every admitted realization, or state only the failure of the attempted construction. Failure alone does not prove positive-source recovery. Audit the classical reproducing-kernel and lacunary-series ingredients already identified by MC-524 and PL-468 before assigning any novelty to a destination result.

**Bounded source reading for Prime Lattice:** read exactly `research/mobius_cancellation/findings/MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles.md` for the moving profile, amplitude bound, entire remainder and atomic transport argument. Include its adjacent `research/mobius_cancellation/findings/MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles.review.md` if present. The inspected source revision is `9d1b57403b6e523249a4cfea2923cabc2d7f0ad1`; recheck current finding and review state. This source contains the required construction in full. The grant is read-only and permits no other Möbius files or recursive dependency traversal; the remaining sources are destination-local.

## Evidence boundary

MC-524 establishes a signed nonmultiplicative control, not the positive residue-source transfer posed here. PL-468 excludes a fixed-profile recipe, not all moving profiles. No destination countermodel, sparse-scale prime recovery theorem, absolute variance estimate, zero exclusion, RH/GRH result, or literature priority is established by this clue. Even a successful abstract control would not refute a theorem using additional actual-prime constraints. The accepted `3^k`-mesh clue and PL-466's every-block theorem remain unchanged.

## Research disposition

Outcome: supported

Resolved by:

- [[research/prime_lattice/findings/PL-469-positive-sparse-block-sources-retain-negative-pole-residues]]

PL-469 reconstructs the changing-profile Mellin construction and transports it
by cells of length 5 onto the progression `n=1 mod 5`. Subtracting twice these
real signed cell integrals from the positive background `5/4` gives one source
with `5/8 <= b_n <= 15/8` on integers coprime to 5 and residue masses
`x/4+o(x)`. Every retained window sees only the background, so its empirical
variance is at most `25X/16`, simultaneously for every integer `1<=H<=X`.
The atomic transport error is holomorphic on `Re s>beta-1`; every character
transform therefore has just the two off-critical poles `beta +/- i gamma`,
both with residue `-1`, in addition to the principal channel's pole at 1.
The exact identity-residue average and conjugation compatibility are preserved.

This establishes the requested abstract control on `j_k=floor(k log k)`. It
does not establish a relative frame, rational-prime support, Euler product,
functional equation or quantitative growth of the continued transforms. The
accepted `3^k`-mesh clue remains unresolved, and PL-466's every-block theorem
is unchanged.
