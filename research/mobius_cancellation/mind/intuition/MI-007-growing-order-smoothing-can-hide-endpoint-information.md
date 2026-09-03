# MI-007 — Growing-order smoothing can manufacture smallness while pushing current-scale information out of view

**Evidence level:** supported by exact kernel bounds and inversion identities in MC-042--MC-045

## Core intuition

Changing the Riesz order with scale genuinely leaves the fixed-order divisor statement of MC-042, but it introduces two independent ways for an apparently strong estimate to stop measuring Möbius cancellation. The normalization can become small for every bounded coefficient sequence, and even after removing that mass decay the kernel can become exponentially insensitive to the current endpoint.

Thus a variable-order smoothed bound is meaningful only together with a quantitative information-transfer theorem showing that the same data still sees the ordinary sum at the scale where RH cancellation is needed.

## Strongest justified principle

MC-042 closes every fixed order: its Mellin multiplier is zero-free in the target half-plane, so a fixed Riesz mean retains the same reciprocal-zeta divisor burden as ordinary Möbius cancellation.

MC-043 identifies the first variable-order failure. For every `|a_n|<=1`,

`|R_{tau,a}(x)| <= x/Gamma(tau+2)`,

and the all-positive sequence essentially saturates this mass when `tau=o(x)`. If `tau(x) ~ c log x/log log x`, this trivial scale is `x^(1-c+o(1))`. Near `c=1/2`, the normalization alone reaches the square-root exponent even with no cancellation at all.

MC-044 removes that normalization and finds a second loss. For the mass-normalized order-`k` statistic, changing only the last `L` coefficients changes the observation by at most `2(L/X)^(k+1)`, although the ordinary sum can change by order `L`; an exact square-free-support control already realizes the gap. Fixed-strength visibility of a coefficient near scale `N` moves to future scale `Y=Omega(kN)`.

MC-045 closes the obvious objection that the endpoint control broke multiplicativity. A completely multiplicative sign twist supported on a terminal prime slab preserves Möbius multiplicativity and exact square-free support, changes the ordinary endpoint sum by `X^(alpha+o(1))` for `17/30<alpha<3/4`, yet has vanishing one-scale pretentious distance and changes every fixed positive integer-order same-scale Riesz sum by `o(X^(1/2))`. One-scale support, multiplicativity, pretentious closeness, and finitely many fixed-order smoothings still do not determine endpoint cancellation.

The full same-order function of scale is not informationless. On intervals between integers the exact differential identity

`S_0 = (1/k!) product_{j=1}^k (D+j) S_k`

recovers the ordinary sum. But a diagonal estimate on `S_{k(x)}(x)` does not supply the required same-order neighboring-scale derivatives. Invertibility of the full transform and usefulness of one changing-order observable are different statements.

## What remains possible

A viable variable-order route can stay quantitatively below the normalization-vacuity threshold and carry same-order multiscale control, translated/localized kernels, derivative information, or a source-specific Tauberian theorem that forbids the terminal prime-slab controls. The extra theorem must use information stronger than one-scale multiplicativity plus pretentious closeness. Another smoothing law may also work if its inverse information budget is independently weaker than RH.

The obstruction does not say smoothing is useless. It says that increasing order is not monotone in arithmetic information.

## Status / novelty

Riesz means, Gamma asymptotics, endpoint kernel estimates, pretentious metrics, and differential inversion are classical mechanisms. The persisted synthesis is the information-budget boundary: **a stronger-looking smoothed exponent can come from universal kernel mass or endpoint blindness rather than signed cancellation**.

## Falsification criterion

Derive ordinary square-root-scale Möbius cancellation from a diagonal growing-order estimate while allowing the MC-043 all-positive mass control and MC-045 multiplicative terminal prime-slab controls under the same hypotheses. A theorem using genuinely additional multiscale or arithmetic structure would evade rather than falsify the intuition.

## Lean-formalizable core

- Universal Riesz kernel-mass bound.
- Gamma-vacuity exponent threshold.
- Terminal-block sensitivity bound after mass normalization.
- Multiplicative terminal-prime one-scale invisibility control.
- Exact same-order differential inversion.
