# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove a diagonal-scale flat sparse quadratic large-sieve bound

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`.

The conductor and fixed-order algebraic escapes are largely exhausted. MC-266--MC-267 show that the radial support hierarchy is just the Krawtchouk transform of the Hamming-weight distribution of the actual lower-prime Legendre sign vectors; universal recurrence and association-scheme algebra are information-neutral.

MC-268 replaces the wasteful monomial moment by the endpoint-optimal Christoffel square. MC-269 then identifies its arithmetic content exactly. If `B_m` is the family of lower-prime subsets of size at most `m`, the target is the flat second moment

`sum_(|T|=t) |sum_(S in B_m) chi_T(q_S)|^2 <= L_y binom(N_y,t) |B_m|`,

and `binom(N_y,t)|B_m|` is the literal diagonal. At the useful choice `m=t+1`, exclusion is compatible with losses `L_y=o(k_y/m)`.

The live theorem is therefore a sparse-family quadratic large sieve at essentially diagonal scale for the **exact** matrix whose rows are fixed-weight shell-prime products and whose columns are lower-prime products of size at most `m`. Generic all-moduli quadratic large sieves pay an ambient modulus/source-length scale far too large for this target.

MC-269 also rules out a broad proof strategy. Expanding radially and taking absolute values layer by layer compares every layer with the tiny diagonal atom `1/|B_m|`; even low layers then require extreme precision such as `eta_2=o(m^-2)` at the live scale. A successful proof should preserve cancellation among off-diagonal source pairs or exploit a stronger structural orthogonality of the exact sparse matrix.

## Keep basis changes, detector efficiency and arithmetic cancellation separate

MC-267 says Krawtchouk coordinates do not create information. MC-268 says the positive detector still matters greatly. MC-269 says that after choosing the optimal detector, its residual is no longer a high-moment combinatorial object but a flat quadratic second moment.

Future work should distinguish four layers: universal basis identities, optimal positive endpoint detection, exact nonlinear lifting to the sparse character matrix, and source-specific cancellation in that matrix. The first three can remove artificial proof loss; only the fourth can exclude the blind support.
