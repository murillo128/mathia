# MI-062 — The critical Ford mark is a bounded-mass signed edge observable of the local zeta potential

**Evidence level:** exact positive reduction plus matched-control and classical potential-theoretic boundary from [NB-234](../../findings/NB-234-growing-depth-moment-hierarchy-reconstructs-critical-ford-mark.md), [NB-235](../../findings/NB-235-critical-ford-transition-reduces-to-microlocal-landau-gonek-remainder.md), and [NB-236](../../findings/NB-236-poincare-lelong-turns-ford-depth-localization-into-bounded-edge-potential.md), building on NB-230--NB-233.

NB-234 shows that on every fixed critical layer the residue can be reconstructed from profiled depth--phase moments with an order `K(Q)` that grows slowly with source capacity, while every predetermined fixed `K` remains blind in a matched spectral control. The nonlinear exponential depth mark is therefore not a fixed-moment statistic.

NB-235 identifies what that hierarchy approximates in classical zeta language. The critical coefficient is a microscopic Landau zero sum with an additional horizontal Ford-depth cutoff. The shell profile has zero total integral, so the ordinary Landau--Gonek prime-power diagonal disappears; black-box smoothing of the global cumulative formula pays the full cumulative remainder and does not exploit the microscopic window.

NB-236 changes representation again. Let `Psi(s)=K_(X,H)(s) chi(d(s))`, where `K_(X,H)` is the exact holomorphic carrier and `chi` is a smooth cutoff in Ford depth. Poincare--Lelong gives the weighted zero coefficient as a pairing of `log|zeta|` with `Delta Psi`. Since the carrier is holomorphic,

`Delta Psi = X^2 K chi'' - 2X K' chi'`,

so the kernel is supported only on the two transition strips of the horizontal cutoff. It also satisfies `int Delta Psi dA=0`, hence annihilates constants and, under the justified integration by parts, harmonic comparison functions.

The Ford scales cancel sharply in the kernel norm. With `Y=X/R` and `J_0=R/H`, NB-236 proves

`||Delta Psi||_1 << Y + J_0^(-1)`.

On the critical Ford diagonal this is `O(1)`. Smooth horizontal depth localization therefore has **bounded tariff**: there is no unavoidable extra power of `X`, `H` or `J_0` merely from selecting the correct horizontal layer.

This does not solve the coefficient. Taking absolute values against `log|zeta|` discards exactly the remaining resource and yields no `o(1)` gain. The load-bearing object is the signed local potential fluctuation across the two edge strips. A source theorem should show that the zeta potential there is sufficiently close to a harmonic background, or otherwise has a small signed correlation with `Delta Psi`. Such a theorem would control the exact Ford coefficient directly; the growing moment hierarchy remains a sufficient surrogate rather than the only formulation.

The reusable lesson is a three-stage audit. First determine the source resolution needed to identify the mark. Then ask whether imposing that localization itself creates a large analytic tariff. Only after that price is known ask for cancellation of the localized source observable. Here the first stage needs growing resolution, the second stage is unexpectedly cheap after Poincare--Lelong, and the unresolved third stage is a bounded-mass signed potential estimate.

**Boundary.** NB-236 uses a smooth rather than hard depth cutoff, and bounded `L^1` mass is only a tariff calculation. It does not prove that the signed pairing is small, that `log|zeta|` admits the required local harmonic approximation, or that Nyman--Beurling approximation controls this source quantity. The Poincare--Lelong identity is generic complex analysis; the source-specific content is the Ford carrier/scaling and any future theorem controlling the local zeta potential.