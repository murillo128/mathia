# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price source information after separating global discriminator survival from finite-horizon completion freedom

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-351--AF-365 separate exact discriminator survival from target-relative inversion cost. Every fixed real Riesz order has a zero-free Mellin multiplier on `Re s>0`, so a **global eventual** profile error `O(X^theta)` preserves every Dirichlet principal part in `Re s>theta`. At the same time, finite-band coordinate recovery can cost `e^u`, `e^(u+v)`, or `e^(u+v)/sqrt(v)` depending on the target. Exact pole fidelity and stable reconstruction are therefore different currencies.

AF-366 closes the finite-horizon loophole sharply. Any observation that factors through finitely many coefficients is blind to a tail

`d_n = r n^(rho-1) 1_(n>N)`

that inserts a prescribed Dirichlet pole at `rho`, even though its unweighted tail amplitude tends to zero as `N->infinity` when `Re rho<1`. Thus a large finite Riesz window does **not** inherit AF-365's global pole-fidelity conclusion merely by being accurate on its visible prefix.

The complementary source gate is exact: if two coefficient sequences differ by `O(n^(theta-1))` in the tail, their Dirichlet transforms differ holomorphically on `Re s>theta`; hence all principal parts there agree. Away from the boundary, the tail transform is bounded by `O(N^-eta/eta)` on `Re s>=theta+eta`. The live question is therefore to identify an independently justified arithmetic tail/continuation class, or another genuinely nonlocal certificate, strong enough for the destination to consume the preserved prime-pole discriminator without reconstructing the whole source.

## Couple the preserved prime-pole discriminator to a stably usable destination

**Linked intuitions:** `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365 says what survives under global transformed control; AF-366 says what finite data cannot determine over an unrestricted completion class. A destination theorem must therefore declare three objects separately: the finite data actually observed, the admissible source-tail or continuation class, and the topology/modulus in which the pole-sensitive conclusion is inferred.

If the destination factors through a linear Hilbert target, derive its representer and Picard profile and price the `u,v` costs. If it uses Mellin continuation or principal parts, prove the source-tail/global hypothesis that makes the continuation unique and quantitatively usable. Exact finite-horizon data, increasingly large `N`, and small unweighted tail coefficients are not substitutes for that hypothesis.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep source class, transform fidelity, finite observation and target conditioning as different currencies

Observation horizon, admissible tail class, smoothing order, principal-part fidelity, absolute attenuation, inverse conditioning, target spectral distribution, destination topology and destination slack are distinct resources. AF-362--AF-364 price target recovery, AF-365 proves global principal-part survival, and AF-366 shows that finite-prefix observation has an enormous completion fibre unless the source class constrains the unseen tail. Future work must keep these layers separate until a theorem explicitly connects them.