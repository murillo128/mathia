# MI-047 — Endpoint anti-dephasing is an information-times-energy problem in the source quotient

**Evidence level:** exact finite-endpoint synthesis from [MC-332](../../findings/MC-332-arbitrary-mode-dependent-prime-rows-exactly-dephase-the-reciprocal-endpoint.md) through [MC-339](../../findings/MC-339-maximal-correlation-information-budget.md).

MC-332 shows that arbitrary dependence of prime coefficients on endpoint mode is too expressive: the conjugate-character matched filter erases the phase exactly even though its evaluation matrix has only source-rank dimension. MC-333--MC-335 separate rowspace rank, total Frobenius energy, cross-mode variation and low polynomial degree. MC-336--MC-337 then show that degree and syntactic self-phase exclusion are coordinate dependent: in source-phase coordinates the matched filter can be degree one, and exact algebraic relations among source phases may reconstruct an excluded phase at a different degree cost.

The invariant replacement is **own-source predictability**. For coefficient `i`, let `x_i` be the source phase it would need to cancel and let `H_i` be the admitted observation subspace. Put

`rho_i = ||P_(H_i) conjugate(x_i)||_2`,

and let `rho^2` be the average of `rho_i^2`. MC-338 proves an exact projection/energy inequality: if `E` is normalized coefficient Frobenius energy and `delta` is normalized RMS dephasing error, then

`delta >= (1-rho sqrt(E))_+`.

Equivalently, achieving error `delta<1` requires `E >= (1-delta)^2/rho^2`. Exact dephasing is cheap only when the architecture can predict each coefficient's own phase; if that predictability is `rho^2~1/m`, exact cancellation costs energy of order `m`.

MC-339 identifies `rho` with standard information quantities for binary source phases. When `H_i=L^2(sigma(Y_i))`, `rho_i=||E[conjugate(x_i)|Y_i]||_2`. After removing the trivial mean, the excess predictability is exactly the squared Hirschfeld--Gebelein--Rényi maximal correlation between the own phase and its observation. Along a Markov information chain those maximal correlations multiply, so lossy stages cannot secretly restore cheap matched filtering. A Shannon-information corollary bounds the excess by mutual information, giving a directly interpretable sufficient condition: bounded coefficient energy plus vanishing average information about the own source phase leaves asymptotically full dephasing error.

This subsumes the earlier coordinate examples rather than discarding them. Low Walsh degree, source-variable exclusion and parity-quotient reconstruction are useful when they let one compute or bound `rho`; rank and variation remain separate because they do not determine either predictability or energy. The source-relative question is not whether the coefficient formula *mentions* its target phase, but how accurately its admitted information determines that phase after every exact source relation and reparameterization, and what analytic norm must be spent to exploit that information.

The live route is therefore an analytic-information theorem for the actual Möbius coefficient family: exhibit a source-natural observation channel, prove small own-phase maximal correlation/information in the relevant quotient, and simultaneously control normalized coefficient energy/conditioning. A complexity restriction that does not imply those quantities can still hide the matched filter.

**Boundary.** MC-338--MC-339 are exact for the finite reciprocal endpoint and binary/source-character observation model. The HGR composition statement requires the declared Markov information flow, and mutual information is only a convenient sufficient bound. None of these results proves that a useful arithmetic coefficient family obeys the needed information/energy restrictions, bounds `M(x)`, or proves RH.