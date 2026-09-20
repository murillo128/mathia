# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the zeta-zero Mellin layer below the cubic transition error floor

**Linked intuitions:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`, `MI-045-fixed-gap-meet-join-data-collapse-to-finite-congruence-decoration`, `MI-046-growing-gap-arithmetic-complexity-pays-a-reciprocal-continuation-tariff`, `MI-047-mesoscopic-continuation-phase-can-miss-the-prime-pair-parity-sector`, `MI-048-cubic-phase-can-reopen-arithmetic-support-yet-average-to-a-universal-control`.

PL-391--PL-399 separate frozen multiplicative geometry from the continuation-faithful transition layer and price growing-gap information by a reciprocal `1/d` tail. PL-400 shows that the subcubic real channel misses the even-gap prime-pair sector; PL-401 restores that sector at `d~r^(1/3)` through the cubic phase but finds that the first singular-series average uses only Gallagher's mean and is reproduced by a parity-only control.

PL-402 changes the interpretation of that collapse without undoing it. Classical Goldston--Suriajaya continuation of the same pair singular series has

`F(s) = const * zeta(s) zeta(s+1) / zeta(2s+2) * G(s)`,

so every nontrivial zero `rho` appears at `s_rho=rho/2-1`. After the natural Riesz normalization, the zero layer is `x^(rho/2-2)`; on RH its radial exponent is `-7/4`, while an off-line zero produces a strictly larger power. This is prior-art arithmetic, not a new RH criterion from Prime Lattice.

The cubic continuation kernel is compatible with that layer rather than annihilating it. For `g(u)=sin(pi u^3/6)/u`, its oscillatory Mellin transform is

`g_hat(s) = (1/3) (pi/6)^(-(s-1)/3) Gamma((s-1)/3) sin(pi(s-1)/6)`,

and `g_hat(rho/2-1) != 0` for every nontrivial zeta zero. The universal Gallagher mean in PL-401 is therefore only the leading layer; subleading linear singular-series information can be zero-sensitive.

The quantitative obstruction is resolution. The same Mellin picture has a deterministic `s=0` contribution at order `H^-1`, while the RH zero layer begins at `H^-7/4`. The current cubic transition approximation aggregates only to order `H^-1` on a fixed cubic annulus, so it stops three quarters of a power too early. The live question is whether the exact continuation statistic can be expanded and renormalized through every contribution larger than the zero layer, with a regulator/cutoff that justifies Mellin inversion and a remainder small enough to expose the `H^(rho/2-2)` residues.

## Keep leading mean collapse, subleading Mellin arithmetic and transfer to actual prime pairs separate

PL-401 remains decisive for the leading cubic average: matching parity density reproduces it exactly. PL-402 shows that this does not justify the stronger claim that linear singular-series averages are intrinsically zero-blind. Their meromorphic continuation already contains the zeta divisor, and the cubic kernel has no structural zero at those pole locations.

A viable continuation argument must therefore specify which asymptotic layer it extracts. It must subtract or control the deterministic contributions above `H^-7/4`, justify the finite-window or smoothed Mellin transform, retain uniform transition errors at that scale, and distinguish the singular-series model from an actual `Lambda(r)Lambda(r+d)` correlation theorem. A visible zero-sensitive Riesz layer in classical prior art is a route reopening, not yet a transfer theorem for the exact Prime-Lattice continuation observable.