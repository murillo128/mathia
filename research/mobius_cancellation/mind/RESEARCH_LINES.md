# Möbius-cancellation research lines

This file records the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a task queue or history.

## Retain arithmetic structure before scalarization; the surviving scalar PNT-error correlation is already RH-scale

**Linked intuition:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`.

MC-397--MC-404 progressively consume source-mode averaging, divisor-pair multiplicity, lcm phase, moving endpoints, complete endpoints, generic truncation and finally every finite divisor-incidence enrichment. Formal family size and finite incidence nonlinearity are not independent cancellation resources once the downstream arithmetic has collapsed them to signature or lcm data.

MC-405 leaves the lcm semilattice by retaining the prime-power label in `M(floor(x/b))`, but the complete Mangoldt-weighted family is an exact first-order self-coupling of `M`. MC-406 then identifies the quotient actually seen downstream: only the `O(sqrt(x))` floor-quotient masses survive, and their PNT main kernel is exactly classical harmonic Möbius cancellation. MC-407 shows that the remaining increment pairing Abel-collapses to the scalar correlation

`C(x)=sum_(a<=x) mu(a)(psi(x/a)-x/a)`

plus the endpoint term.

MC-408 now classifies that scalar escape. Its Mellin transform is

`-zeta'(s)/(s zeta(s)^2)-1/((s-1)zeta(s))`,

so every nontrivial zeta zero produces a nonremovable pole whose leading order cannot cancel. The bound `C(x)=O_epsilon(x^(1/2+epsilon))` for every `epsilon>0` is equivalent to RH. Finite prefixes of `C` also determine the corresponding Möbius prefix by a lower-triangular recursion. The scalar correlation is therefore neither a compression nor an easier RH-scale auxiliary observable merely because it mixes Möbius and prime-counting error.

The live route is now **pre-scalarization arithmetic**. Either exploit the actual Selberg/source coefficients through a theorem not available for generic lcm incidence, or retain phase, congruence, translation, source labels or another genuinely nonseparable variable inside the quotient fibers and control it before exact aggregation. One may still attack `C(x)` directly as an RH criterion, but it no longer counts as an independently easier intermediate mechanism.

## Keep retained variables, invertibility, coordinate changes and analytic leverage distinct

A variable can survive one quotient and still be analytically redundant. Divisor tuples collapse to lcm; source labels collapse to floor-quotient masses; deterministic PNT mass collapses to harmonic Möbius cancellation; MC-407 identifies the residual increment coordinates with the same Möbius-weighted error convolution; and MC-408 shows that the final scalar correlation is both finite-prefix invertible and RH-equivalent at the square-root target.

Exact recoverability is therefore not the same resource as a cheaper estimate. Future candidates should be reduced through all exact regroupings, inversions and summation-by-parts identities before receiving credit for a second observable. Genuine progress requires an independently controlled signed relation **before** scalarization, or a source-specific theorem whose proof input is not already equivalent to the desired Mertens/RH-strength bound.