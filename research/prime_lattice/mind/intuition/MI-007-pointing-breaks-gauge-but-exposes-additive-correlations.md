# MI-007 — Ordinary prime-power Gram spectra classicalize through the first growing-depth transition

**Evidence level:** supported by exact time-dilation/rank/trace-norm identities, classical prime counting, and conditional Hardy--Littlewood bulk input only where explicitly stated

## Core intuition

Prime support and exponent depth do carry arithmetic data, but the ordinary finite-time Gram spectrum now has a much larger classicalized region than the prime-only bulk. Fixed prime-power depth is exactly a time-dilated prime layer; fixed depth tails are dominated in dimension by their shallowest layer; and even when a growing-depth tail reaches the first `sqrt(log X)` population transition, the natural von-Mangoldt half-weight collapses its normalized spectrum. The first scalar repair removes the depth grading rather than revealing a new phase.

## Strongest justified principle

PL-081--PL-087 already separate bulk from extremes. At the prime mean-gap horizon the support-only bulk is the Poisson-sinc law under the full local Hardy--Littlewood hierarchy, while bounded clusters destroy uniform extreme conditioning. Prime-only von-Mangoldt weighting is asymptotically deterministic on a fixed shell, and higher prime powers have vanishing rank in the full ordinary bulk.

PL-088 closes the first depth-conditioned loophole exactly. On `p^k`, the logarithmic frequency is `k log p`, so the depth-`k` Gram at horizon `T` is the ordinary prime-support Gram at base scale `Y=X^(1/k)` and time `kT`. The inherited von-Mangoldt half-weight adds only the deterministic factor `1/k^2` and a macroscopic shell envelope. At its own mean-gap scale the depth layer therefore has the same local prime-process bulk, not a new exponent-depth phase.

PL-089 shows that retaining **all** cross-depth couplings above any fixed minimum depth `K` does not change the ordinary empirical law: deeper layers occupy only `o(N)` rows/columns, so an arbitrary Hermitian tail matrix has the same weak bulk as its depth-`K` principal block. PL-090 extends that rank mechanism to growing `K=o(sqrt(log X))` and identifies the first population transition at `K~alpha sqrt(log X)`, where adjacent depth offsets acquire a geometric population law. That transition is forced by ordinary prime density and is not itself RH-sensitive.

PL-091--PL-093 then show why the new population mass still fails to create a natural von-Mangoldt bulk. For every `K(X)->infinity`, positivity and the diagonal `1/k^2` amplitude give normalized trace `O(K^{-2})`, hence empirical measure `->delta_0` uniformly in observation time. The determinant root collapses at the same scale. The first scalar normalization that can avoid this is `K^2`; but throughout `K=o(sqrt(log X))` and `K~alpha sqrt(log X)`, the `K^2`-rescaled matrix is normalized-trace-norm equivalent to the unweighted shell-envelope Gram. Consequently every ordinary Lipschitz spectral statistic and every bounded-`z` per-site `log det(I+zA)` loses the specifically von-Mangoldt depth factor.

## What remains possible

The surviving prime-power spectral sector is therefore **non-Lipschitz or non-bulk**: hard-edge and inverse statistics, extreme eigenvalues, condition numbers, target-relative Schur complements, singular/growing test functions, or a completed indefinite Weil object that weights sparse/deep layers before ordinary empirical normalization. Growth regimes beyond the audited `sqrt(log X)` transition are also structurally open, but their population effect alone is not arithmetic evidence.

A positive candidate must show where rational-prime information enters after the deterministic time-dilation, rank, trace, and `K^2` trace-norm controls have been removed. Matching only local Hardy--Littlewood/Poisson statistics or the deterministic depth population is insufficient.

## Status / novelty

The PNT, Hardy--Littlewood, Poisson, rank-interlacing, trace/determinant inequalities, and Schatten norm estimates are classical ingredients. The persisted Prime-Lattice content is the exact organization of these controls and the resulting closure of ordinary prime-power Gram bulk through the first growing-depth transition.

## Falsification criterion

Produce, under the hypotheses of PL-093, an ordinary Lipschitz spectral statistic of the `K^2`-rescaled natural von-Mangoldt Gram that stays separated from the unweighted envelope Gram, or a fixed-depth/tail weak empirical law contradicting the exact time-dilation/rank reductions. A positive advance should instead isolate a genuinely non-Lipschitz or target-relative statistic and pass generalized-prime controls.

## Lean-formalizable core

- Fixed-depth time-dilation identity.
- Rank stability of depth-tail empirical spectra.
- Positive trace and determinant collapse from the `1/k^2` amplitude.
- `K^2` normalized trace-norm equivalence.
