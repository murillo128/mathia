# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure; depth trades only the child-side tax

**Evidence level:** exact/proved classification from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md), with the endpoint-weight obstruction quantified by [FD-148](../../findings/FD-148-finite-seed-anchored-expansion-forces-singular-endpoint-marginals.md), the bounded-distortion depth threshold by [FD-149](../../findings/FD-149-bounded-distortion-ancestry-transfer-must-reach-typical-prime-factor-depth.md), and the explicit depth/distortion phase curve in [FD-150](../../findings/FD-150-ancestry-depth-trades-only-the-child-tax-along-a-sathe-selberg-phase-curve.md).

For binary orientations anchored on `D`, the optimal finite-`L^q` Poincaré constant is exactly

`C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`.

Thus connectivity is only the zero-boundary endpoint. Stable recovery requires a uniform lower bound on observed boundary mass for every admissible macroscopic cut.

FD-148 identifies a depth-independent parent obstruction for a fixed finite divisor-closed anchor. If the parent marginal satisfies `eta_T^-(d)<=P_T nu_T(d)` on `D`, then for every ancestry depth

`h_(D,T)^(<=L) <= (zeta(2)|D|+o_D(1)) P_T/T`.

Positive anchored expansion therefore always requires parent amplification of order `T`, unless the anchor itself is changed. Making the ancestry graph deeper does not dilute this fixed-seed tax.

The child side does admit a quantitative depth trade. Put `lambda_T=log log T` and `L_T=floor(alpha lambda_T)` with fixed `0<alpha<1`. FD-150 combines the exact complement cut with the squarefree Sathe--Selberg lower tail to obtain

`nu_T(R_(D,L_T)) asymp_(D,alpha) 1/[sqrt(lambda_T)(log T)^(I(alpha))]`,

`I(alpha)=1-alpha+alpha log alpha`.

If `eta_T^+(m)<=K_T nu_T(m)` on the reachable descendants, then

`h_(D,T)^(<=L_T) <<_(D,alpha) K_T/[sqrt(log log T)(log T)^(I(alpha))]`.

Hence constant expansion forces

`K_T >> sqrt(log log T)(log T)^(I(alpha))`.

This interpolates the fixed-depth obstruction and the Erdős--Kac transition. Approaching the typical depth relaxes the **additional child-side singularity**, but it never pays the parent bill. The earlier shorthand “endpoint mass or typical-depth reach” is therefore too weak for a fixed anchor: the correct resource statement is **parent concentration always, plus either child concentration or sufficient ancestry depth**.

A source-valid proposal should expose at least three quantities before a full coercivity argument: the ancestry depth, the parent amplification on the anchor, and the child amplification on the reachable set. If the parent amplification is `o(T)`, the fixed-anchor route is dead regardless of depth. If `L_T~alpha log log T` with `alpha<1`, the child amplification must cross the explicit Sathe--Selberg phase curve above.

**Boundary.** These results concern a fixed finite anchor, binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They do not exclude a growing source-native anchor, `L^infinity`, independently justified singular weights, or genuinely nonlocal Farey/Fourier destination functionals outside this edge model. The phase curve is a necessary-condition screen, not a sufficiency theorem for expansion.
