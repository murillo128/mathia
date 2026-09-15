# MI-021 — One convergent singular-remainder trace now closes the full moving Green endpoint transfer

**Evidence level:** exact conditional reduction from [PL-320](../../findings/PL-320-source-trace-full-tail-volterra-matching.md), completed by the conditional-moment Green theorem [PL-321](../../findings/PL-321-conditional-moment-green-transfer.md), using the endpoint identity of PL-319.

For the logarithmic endpoint coordinate `Q`, PL-320 writes the full tail profile `g` as

`F(Q)=2Q g(Q)-U(Q)+H_(Q0)g(Q)+c_(Q0)(Q)g(Q)`,  `U(Q)=int_(Q0)^Q g(P)dP`.

Assume `g(Q)->0`, the completed-Weil source trace `F(Q)->F_infinity`, and the local singular translation remainder `H_(Q0)g(Q)->H_infinity`. Then the residual right-hand side converges and the exact Volterra equation forces a coefficient `C` with

`g(Q)=C Q^(-1/2)+m(Q)`,  `Qm(Q)->0`,

while the improper integral `int m(Q)dQ` converges. Thus the leading half-order coefficient and the pointwise anti-concentration needed at the moving diagonal are consequences of the same singular-remainder trace rather than separate assumptions.

PL-321 closes the remaining transfer gap. If `m` is locally integrable, has a convergent improper moment `M`, and satisfies `Qm(Q)->0`, then for every fixed `r>0` the moving Green functional obeys

`A_s[m](r) -> e^-r M` as `s->0`.

The mechanism is explicit: before the moving diagonal the exact Green kernel factors into `a_s(r) w_s(Q) E_s(r,Q)`, where `a_s->e^-r`, `w_s` tends pointwise to `1` and has uniformly bounded variation, and `E_s-1` is exponentially small. Stieltjes/Dirichlet summation therefore transports a conditionally convergent moment. The condition `Qm->0` controls the moving and post-diagonal mass. Absolute `L^1` is unnecessary.

For the actual completed-Weil branch, the source equation already provides the convergent full source trace and established boundary theory gives `g=O(Q^-1/2)`. The analytic endpoint-transfer problem is therefore reduced to the single local condition

`H_(Q0)g(Q) -> H_infinity`.

Once that is proved, the coefficient, residual moment, moving-diagonal law and rank-one Green transfer follow in sequence from PL-320--PL-321.

**Boundary.** This is universal endpoint analysis, not an arithmetic sign mechanism. It does not prove convergence of the singular translation remainder, positivity of the endpoint moment, rational-prime rigidity, or RH. The important change is narrower: the previous absolute-integrability alternative is gone, so no extra `L^1` theorem should be counted as an independent endpoint gate.